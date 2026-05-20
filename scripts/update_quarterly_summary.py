#!/usr/bin/env python3
"""
Update quarterly summary CSV files with aggregated data from the current quarter.

This script:
1. Reads the current quarter's detailed CSVs (prs.csv, issues.csv, galaxy_*.csv)
2. Aggregates the data into totals
3. Updates or appends to the summary files in data/:
   - github_prs_summary.csv
   - github_issues_summary.csv
   - galaxy_legacy_summary.csv
   - galaxy_collections_summary.csv
"""

import os
import sys
from pathlib import Path
import pandas as pd

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent


def update_summary_file(filepath, quarter_data, key_column='Quarter'):
    """Update or append to a summary CSV file"""

    if filepath.exists():
        df = pd.read_csv(filepath)

        # Check if quarter already exists
        if quarter_data[key_column] in df[key_column].values:
            # Remove old row and add new one
            df = df[df[key_column] != quarter_data[key_column]]
            df = pd.concat([df, pd.DataFrame([quarter_data])], ignore_index=True)
            print(f"  Updated existing entry for {quarter_data[key_column]}")
        else:
            # Append new row
            df = pd.concat([df, pd.DataFrame([quarter_data])], ignore_index=True)
            print(f"  Added new entry for {quarter_data[key_column]}")

        # Sort by quarter
        df = df.sort_values(key_column)
    else:
        # Create new file
        df = pd.DataFrame([quarter_data])
        print(f"  Created new file with {quarter_data[key_column]}")

    # Write back to CSV
    df.to_csv(filepath, index=False)

    return df


def aggregate_github_prs(quarter):
    """Aggregate GitHub PRs data"""
    data_dir = ROOT_DIR / "data" / quarter
    prs_file = data_dir / "prs.csv"

    if not prs_file.exists():
        print(f"  WARNING: {prs_file} not found")
        return None

    prs_df = pd.read_csv(prs_file)

    summary = {
        'Quarter': quarter,
        'PRs Created': int(prs_df['PRs Created'].sum()),
        'PRs Merged': int(prs_df['PRs Merged'].sum()),
        'PRs Open': int(prs_df['PRs open'].sum()),
        'External PRs Created': int(prs_df['Created non-maint'].sum()),
        'External PRs Merged': int(prs_df['Merged non-maint'].sum()),
        'External PRs Open': int(prs_df['Open non-maint'].sum())
    }

    print(f"\n  PRs Created: {summary['PRs Created']:,}")
    print(f"  PRs Merged: {summary['PRs Merged']:,}")
    print(f"  External PRs Created: {summary['External PRs Created']:,}")

    return summary


def aggregate_github_issues(quarter):
    """Aggregate GitHub Issues data"""
    data_dir = ROOT_DIR / "data" / quarter
    issues_file = data_dir / "issues.csv"

    if not issues_file.exists():
        print(f"  WARNING: {issues_file} not found")
        return None

    issues_df = pd.read_csv(issues_file)

    summary = {
        'Quarter': quarter,
        'Issues Created': int(issues_df['Issues Created'].sum()),
        'Issues Closed': int(issues_df['Issues Closed'].sum()),
        'External Issues Created': int(issues_df['Created non-maint'].sum()),
        'External Issues Closed': int(issues_df['Closed non-maint'].sum())
    }

    print(f"\n  Issues Created: {summary['Issues Created']:,}")
    print(f"  Issues Closed: {summary['Issues Closed']:,}")
    print(f"  External Issues Created: {summary['External Issues Created']:,}")

    return summary


def aggregate_galaxy_legacy(quarter):
    """Aggregate Galaxy Legacy roles data (cumulative totals)"""
    data_dir = ROOT_DIR / "data" / quarter
    galaxy_file = data_dir / "galaxy_legacy.csv"

    if not galaxy_file.exists():
        print(f"  WARNING: {galaxy_file} not found")
        return None

    galaxy_df = pd.read_csv(galaxy_file)
    total_downloads = int(galaxy_df['download_count'].sum())

    summary = {
        'Quarter': quarter,
        'Total Downloads': total_downloads
    }

    print(f"\n  Total Downloads (cumulative): {total_downloads:,}")

    return summary


def aggregate_galaxy_collections(quarter):
    """
    Aggregate Galaxy Collections data and calculate quarterly delta.

    The API provides cumulative totals, but we want to store quarterly new downloads.
    We maintain a separate cumulative tracking file to calculate deltas.
    """
    data_dir = ROOT_DIR / "data" / quarter
    collections_file = data_dir / "galaxy_collections.csv"

    if not collections_file.exists():
        print(f"  WARNING: {collections_file} not found")
        return None

    collections_df = pd.read_csv(collections_file)

    # Get current cumulative totals from API
    current_cumulative = {}
    for _, row in collections_df.iterrows():
        collection_name = row['full_name']
        downloads = int(row['download_count'])
        current_cumulative[collection_name] = downloads

    # Read cumulative tracking file to get previous totals
    cumulative_file = ROOT_DIR / "data" / "galaxy_collections_cumulative.csv"
    previous_cumulative = {}

    if cumulative_file.exists():
        cumulative_df = pd.read_csv(cumulative_file)
        # Exclude current quarter if it exists, then get the last row
        previous_df = cumulative_df[cumulative_df['Quarter'] != quarter]
        if len(previous_df) > 0:
            last_row = previous_df.iloc[-1]
            previous_cumulative['fedora.linux_system_roles'] = int(last_row.get('fedora.linux_system_roles', 0))
            previous_cumulative['microsoft.sql'] = int(last_row.get('microsoft.sql', 0))
            print(f"  Previous quarter: {last_row['Quarter']}")
            print(f"    fedora cumulative: {previous_cumulative['fedora.linux_system_roles']:,}")
            print(f"    microsoft cumulative: {previous_cumulative['microsoft.sql']:,}")

    # Calculate quarterly deltas
    fedora_delta = current_cumulative.get('fedora.linux_system_roles', 0) - previous_cumulative.get('fedora.linux_system_roles', 0)
    microsoft_delta = current_cumulative.get('microsoft.sql', 0) - previous_cumulative.get('microsoft.sql', 0)
    total_delta = fedora_delta + microsoft_delta

    # Update cumulative tracking file
    new_cumulative_row = {
        'Quarter': quarter,
        'fedora.linux_system_roles': current_cumulative.get('fedora.linux_system_roles', 0),
        'microsoft.sql': current_cumulative.get('microsoft.sql', 0)
    }

    if cumulative_file.exists():
        cumulative_df = pd.read_csv(cumulative_file)
        # Check if quarter already exists
        if quarter in cumulative_df['Quarter'].values:
            # Remove old row and add new one
            cumulative_df = cumulative_df[cumulative_df['Quarter'] != quarter]
            cumulative_df = pd.concat([cumulative_df, pd.DataFrame([new_cumulative_row])], ignore_index=True)
        else:
            # Append new row
            cumulative_df = pd.concat([cumulative_df, pd.DataFrame([new_cumulative_row])], ignore_index=True)
    else:
        cumulative_df = pd.DataFrame([new_cumulative_row])

    cumulative_df = cumulative_df.sort_values('Quarter')
    cumulative_df.to_csv(cumulative_file, index=False)
    print(f"  Updated cumulative tracking: {cumulative_file}")

    # Build summary with quarterly deltas
    summary = {
        'Quarter': quarter,
        'fedora.linux_system_roles': fedora_delta,
        'microsoft.sql': microsoft_delta,
        'Total Downloads': total_delta
    }

    print(f"\n  fedora.linux_system_roles: {fedora_delta:,} (quarterly new downloads)")
    print(f"  microsoft.sql: {microsoft_delta:,} (quarterly new downloads)")
    print(f"  Total: {total_delta:,}")

    return summary


def update_galaxy_per_role_history(quarter):
    """Update the historical per-role Galaxy legacy downloads CSV"""
    data_dir = ROOT_DIR / "data" / quarter
    galaxy_file = data_dir / "galaxy_legacy.csv"

    if not galaxy_file.exists():
        print(f"  No galaxy_legacy.csv found for {quarter} - skipping per-role history update")
        return

    # Read current quarter's per-role data
    current_df = pd.read_csv(galaxy_file)

    # Read historical per-role CSV
    history_file = ROOT_DIR / "data" / "galaxy_legacy_per_role_history.csv"

    if history_file.exists():
        history_df = pd.read_csv(history_file)

        # Check if quarter column already exists
        if quarter in history_df.columns:
            print(f"  Quarter {quarter} column already exists - updating values")
            # Convert quarter column to Int64 if it's string
            if history_df[quarter].dtype == 'object':
                history_df[quarter] = pd.to_numeric(history_df[quarter], errors='coerce').astype('Int64')

            # Update existing column
            for _, row in current_df.iterrows():
                role_name = row['name']
                download_count = int(row['download_count'])

                # Find role in history and update
                if role_name in history_df['Role'].values:
                    history_df.loc[history_df['Role'] == role_name, quarter] = download_count
                else:
                    # Add new role if it doesn't exist
                    new_row = {'Role': role_name, quarter: download_count}
                    # Fill previous quarters with NaN
                    for col in history_df.columns:
                        if col != 'Role' and col != quarter:
                            new_row[col] = pd.NA
                    history_df = pd.concat([history_df, pd.DataFrame([new_row])], ignore_index=True)
        else:
            print(f"  Adding new quarter column: {quarter}")
            # Add new quarter column with integer dtype
            history_df[quarter] = pd.Series(dtype='Int64')

            for _, row in current_df.iterrows():
                role_name = row['name']
                download_count = int(row['download_count'])

                # Find role in history and update
                if role_name in history_df['Role'].values:
                    history_df.loc[history_df['Role'] == role_name, quarter] = download_count
                else:
                    # Add new role
                    new_row = {'Role': role_name, quarter: download_count}
                    # Fill previous quarters with NaN (will be saved as empty)
                    for col in history_df.columns:
                        if col != 'Role' and col != quarter:
                            new_row[col] = pd.NA
                    history_df = pd.concat([history_df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        # Create new history file
        print(f"  Creating new per-role history file")
        history_data = {'Role': current_df['name'].tolist(), quarter: current_df['download_count'].tolist()}
        history_df = pd.DataFrame(history_data)

    # Sort by role name
    history_df = history_df.sort_values('Role')

    # Save updated history (replace NaN with empty string for CSV)
    history_df.to_csv(history_file, index=False, na_rep='')
    print(f"  Updated per-role history: {history_file}")
    print(f"  Roles tracked: {len(history_df)}")


def main():
    # Get quarter from environment
    quarter = os.getenv('QUARTER')
    if not quarter:
        print("ERROR: QUARTER environment variable not set")
        print("Usage: QUARTER=2024-Q4 python update_quarterly_summary.py")
        sys.exit(1)

    print(f"Updating quarterly summaries for {quarter}...")
    print("=" * 60)

    # Update GitHub PRs
    print("\n📊 GitHub PRs:")
    prs_summary = aggregate_github_prs(quarter)
    if prs_summary:
        prs_file = ROOT_DIR / "data" / "github_prs_summary.csv"
        update_summary_file(prs_file, prs_summary)

    # Update GitHub Issues
    print("\n🐛 GitHub Issues:")
    issues_summary = aggregate_github_issues(quarter)
    if issues_summary:
        issues_file = ROOT_DIR / "data" / "github_issues_summary.csv"
        update_summary_file(issues_file, issues_summary)

    # Update Galaxy Legacy
    print("\n📦 Galaxy Legacy Roles:")
    legacy_summary = aggregate_galaxy_legacy(quarter)
    if legacy_summary:
        legacy_file = ROOT_DIR / "data" / "galaxy_legacy_summary.csv"
        update_summary_file(legacy_file, legacy_summary)

    # Update Galaxy Collections
    print("\n📚 Galaxy Collections:")
    collections_summary = aggregate_galaxy_collections(quarter)
    if collections_summary:
        collections_file = ROOT_DIR / "data" / "galaxy_collections_summary.csv"
        update_summary_file(collections_file, collections_summary)

    # Update Galaxy per-role history
    print("\n📜 Galaxy Per-Role History:")
    update_galaxy_per_role_history(quarter)

    print("\n" + "=" * 60)
    print(f"✅ All quarterly summaries updated for {quarter}")


if __name__ == '__main__':
    main()
