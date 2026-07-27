#!/usr/bin/env python3
"""
Collect Ansible Galaxy statistics for Linux System Roles.

This script collects:
1. Legacy roles download counts via Galaxy API v1
2. Collection download counts via Galaxy API v3

Output:
- data/{quarter}/galaxy_legacy.csv
- data/{quarter}/galaxy_collections.csv
"""

import os
import sys
import csv
import time
import requests
import yaml
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
CONFIG_FILE = ROOT_DIR / "config.yaml"

LEGACY_API_URL = "https://galaxy.ansible.com/api/v1/roles"
LEGACY_PAGE_SIZE = 50


def load_config():
    with open(CONFIG_FILE) as f:
        return yaml.safe_load(f)


def retry_request(url, headers=None, params=None, max_attempts=3):
    """Make HTTP request with retry logic for transient failures"""
    delay = 5
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            return response
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt < max_attempts:
                print(f"  Request failed (attempt {attempt}/{max_attempts}), retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2
            else:
                raise
        except requests.exceptions.HTTPError as e:
            raise


def collect_legacy_roles(api_key, namespaces_config):
    """Collect download counts for legacy individual roles via API"""
    print("Collecting Galaxy legacy roles statistics...")

    headers = {
        'accept': 'application/json',
    }
    if api_key:
        headers['Authorization'] = f'Token {api_key}'

    role_data = []

    for ns_config in namespaces_config:
        namespace = ns_config['name']
        include_list = ns_config.get('include')
        exclude_list = ns_config.get('exclude', [])

        print(f"\n  Namespace: {namespace}")

        if include_list:
            for role_name in include_list:
                try:
                    params = {
                        'namespace': namespace,
                        'name': role_name
                    }
                    response = retry_request(LEGACY_API_URL, headers, params)
                    data = response.json()
                    results = data.get('results', [])
                    if results:
                        download_count = results[0].get('download_count', 0)
                        role_data.append({
                            'name': role_name,
                            'download_count': download_count
                        })
                        print(f"    {namespace}/{role_name}: {download_count:,} downloads")
                    else:
                        print(f"    WARNING: {namespace}/{role_name} not found")
                except Exception as e:
                    print(f"    ERROR fetching {namespace}/{role_name}: {e}")
        else:
            params = {
                'namespace': namespace,
                'page_size': LEGACY_PAGE_SIZE
            }

            all_roles = []
            page = 1
            try:
                while True:
                    params['page'] = page
                    response = retry_request(LEGACY_API_URL, headers=headers, params=params)
                    data = response.json()
                    roles = data.get('results', [])
                    if not roles:
                        break
                    all_roles.extend(roles)
                    if not data.get('next'):
                        break
                    page += 1
                    print(f"    Fetching page {page}...")
            except Exception as e:
                print(f"    ERROR fetching namespace {namespace}: {e}")
                continue

            print(f"    Total roles found: {len(all_roles)}")

            for role in all_roles:
                role_name = role['name']
                if role_name in exclude_list:
                    print(f"    Skipping excluded role: {role_name}")
                    continue
                download_count = role.get('download_count', 0)
                role_data.append({
                    'name': role_name,
                    'download_count': download_count
                })
                print(f"    {role_name}: {download_count:,} downloads")

    role_data.sort(key=lambda x: x['name'])
    return role_data


def get_collection_downloads_from_api(namespace, name):
    """Get download count from Galaxy API v3"""
    api_url = f"https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/index/{namespace}/{name}/"
    print(f"  Fetching from API: {namespace}.{name}")

    try:
        response = retry_request(api_url)
        data = response.json()
        download_count = data.get('download_count', 0)
        print(f"    Found: {download_count:,} downloads")
        return download_count
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            raise RuntimeError(f"Collection not found: {namespace}.{name} (404)") from e
        else:
            raise RuntimeError(f"Failed to fetch {namespace}.{name}: HTTP {e.response.status_code}") from e
    except Exception as e:
        raise RuntimeError(f"Failed to fetch {namespace}.{name}: {e}") from e


def collect_collections(collections_config):
    """Collect download counts for collections via Galaxy API"""
    print("Collecting Galaxy collections statistics...")

    collection_data = []
    for collection in collections_config:
        namespace = collection['namespace']
        name = collection['name']

        print(f"  Collection: {namespace}.{name}")
        download_count = get_collection_downloads_from_api(namespace, name)

        collection_data.append({
            'namespace': namespace,
            'name': name,
            'full_name': f"{namespace}.{name}",
            'download_count': download_count
        })

    return collection_data


def write_csv(filepath, data, fieldnames):
    """Write data to CSV file"""
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Wrote {len(data)} rows to {filepath}")


def main():
    quarter = os.getenv('QUARTER')
    if not quarter:
        print("ERROR: QUARTER environment variable not set")
        print("Usage: QUARTER=2025-Q1 GALAXY_API_KEY=xxx python collect_galaxy_stats.py")
        sys.exit(1)

    api_key = os.getenv('GALAXY_API_KEY')
    if not api_key:
        print("WARNING: GALAXY_API_KEY not set, API requests may be rate-limited")

    config = load_config()
    galaxy_config = config['galaxy']

    output_dir = ROOT_DIR / "data" / quarter
    output_dir.mkdir(parents=True, exist_ok=True)

    legacy_roles = collect_legacy_roles(api_key, galaxy_config['legacy_roles']['namespaces'])
    legacy_csv = output_dir / "galaxy_legacy.csv"
    write_csv(legacy_csv, legacy_roles, ['name', 'download_count'])

    collections = collect_collections(galaxy_config['collections'])
    collections_csv = output_dir / "galaxy_collections.csv"
    write_csv(collections_csv, collections, ['namespace', 'name', 'full_name', 'download_count'])

    print(f"\n✅ Galaxy statistics collection complete for {quarter}")
    print(f"   Legacy roles: {legacy_csv}")
    print(f"   Collections:  {collections_csv}")


if __name__ == '__main__':
    main()
