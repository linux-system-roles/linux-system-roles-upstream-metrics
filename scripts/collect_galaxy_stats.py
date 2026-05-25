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
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent

# Configuration
LEGACY_API_URL = "https://galaxy.ansible.com/api/v1/roles"
LEGACY_NAMESPACE = "linux-system-roles"
LEGACY_PAGE_SIZE = 50
LEGACY_EXCLUDE = ["template", "mssql"]
LEGACY_ADDITIONAL_ROLES = [
    {"namespace": "willshersystems", "name": "sshd"}
]

COLLECTIONS = [
    {"namespace": "fedora", "name": "linux_system_roles"},
    {"namespace": "microsoft", "name": "sql"}
]


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
            # Don't retry on HTTP errors (4xx, 5xx) - they're not transient
            raise


def collect_legacy_roles(api_key):
    """Collect download counts for legacy individual roles via API"""
    print("Collecting Galaxy legacy roles statistics...")

    api_url = LEGACY_API_URL
    namespace = LEGACY_NAMESPACE
    page_size = LEGACY_PAGE_SIZE
    exclude = LEGACY_EXCLUDE

    # Prepare API request
    headers = {
        'accept': 'application/json',
    }

    if api_key:
        headers['Authorization'] = f'Token {api_key}'

    params = {
        'namespace': namespace,
        'page_size': page_size
    }

    # Fetch ALL roles from API (handle pagination)
    all_roles = []
    page = 1
    while True:
        params['page'] = page
        response = retry_request(api_url, headers=headers, params=params)

        data = response.json()
        roles = data.get('results', [])

        if not roles:
            break

        all_roles.extend(roles)

        # Check if there's a next page
        if not data.get('next'):
            break

        page += 1
        print(f"  Fetching page {page}...")

    print(f"  Total roles found: {len(all_roles)}")

    # Filter and collect role data
    role_data = []
    for role in all_roles:
        role_name = role['name']

        # Skip excluded roles
        if role_name in exclude:
            print(f"  Skipping excluded role: {role_name}")
            continue

        download_count = role.get('download_count', 0)
        role_data.append({
            'name': role_name,
            'download_count': download_count
        })
        print(f"  {role_name}: {download_count:,} downloads")

    # Collect additional roles from other namespaces
    additional_roles = LEGACY_ADDITIONAL_ROLES
    if additional_roles:
        print(f"\nCollecting additional roles from other namespaces...")
        for additional in additional_roles:
            add_namespace = additional['namespace']
            add_name = additional['name']

            # Fetch this specific role using query parameters
            try:
                add_params = {
                    'namespace': add_namespace,
                    'name': add_name
                }
                response = retry_request(api_url, headers, add_params)
                data = response.json()

                results = data.get('results', [])
                if results:
                    role_info = results[0]
                    download_count = role_info.get('download_count', 0)
                    role_data.append({
                        'name': add_name,
                        'download_count': download_count
                    })
                    print(f"  {add_namespace}/{add_name}: {download_count:,} downloads")
                else:
                    print(f"  WARNING: {add_namespace}/{add_name} not found")
            except Exception as e:
                print(f"  ERROR fetching {add_namespace}/{add_name}: {e}")

    # Sort by name
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


def collect_collections():
    """Collect download counts for collections via Galaxy API"""
    print("Collecting Galaxy collections statistics...")

    collections = COLLECTIONS

    collection_data = []
    for collection in collections:
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
    # Get quarter from environment
    quarter = os.getenv('QUARTER')
    if not quarter:
        print("ERROR: QUARTER environment variable not set")
        print("Usage: QUARTER=2025-Q1 GALAXY_API_KEY=xxx python collect_galaxy_stats.py")
        sys.exit(1)

    # Get API key from environment
    api_key = os.getenv('GALAXY_API_KEY')
    if not api_key:
        print("WARNING: GALAXY_API_KEY not set, API requests may be rate-limited")

    # Output directory
    output_dir = ROOT_DIR / "data" / quarter
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect legacy roles
    legacy_roles = collect_legacy_roles(api_key)
    legacy_csv = output_dir / "galaxy_legacy.csv"
    write_csv(legacy_csv, legacy_roles, ['name', 'download_count'])

    # Collect collections
    collections = collect_collections()
    collections_csv = output_dir / "galaxy_collections.csv"
    write_csv(collections_csv, collections, ['namespace', 'name', 'full_name', 'download_count'])

    print(f"\n✅ Galaxy statistics collection complete for {quarter}")
    print(f"   Legacy roles: {legacy_csv}")
    print(f"   Collections:  {collections_csv}")


if __name__ == '__main__':
    main()
