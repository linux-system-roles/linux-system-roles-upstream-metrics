#!/usr/bin/env python3
"""
Generate graphs from quarterly metrics data.

Graphs generated:
1. Pull Requests Stats per Quarter (6 metrics) - all historical data
2. Issues Stats per Quarter (4 metrics) - all historical data
3. Legacy Roles Downloads per Role (current quarter, cumulative totals)
4. Legacy Roles Quarterly Delta per Role (downloads gained during current quarter)
5. Total Legacy Roles Downloads (cumulative) - all historical data
6. Total Legacy Roles Quarterly Delta (new downloads per quarter) - all historical data
7. fedora.linux_system_roles Downloads - all historical data
8. microsoft.sql Downloads - all historical data
"""

import os
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent

# Graph configuration
GRAPH_STYLE = 'seaborn-v0_8'
GRAPH_DPI = 300
GRAPH_FIGSIZE = (12, 6)
SHOW_GRID = True
SHOW_TRENDS = True

# Color scheme
COLORS = {
    'maintainer': '#2E86AB',     # Blue
    'external': '#A23B72',       # Purple
    'merged': '#06A77D',         # Green
    'open': '#F18F01',           # Orange
    'closed': '#C73E1D'          # Red
}


def setup_plot_style():
    """Set up matplotlib style"""
    try:
        plt.style.use(GRAPH_STYLE)
    except OSError as e:
        print(f"Warning: Style '{GRAPH_STYLE}' not found ({e}), using default")
        plt.style.use('default')


def save_graph(output_filename):
    """Helper to save graph with consistent settings"""
    output_path = ROOT_DIR / "reports" / "images" / output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=GRAPH_DPI, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {output_path}")


def generate_github_prs_graph(quarter):
    """Generate GitHub PRs stats per quarter (all 6 metrics) - shows ALL historical data"""
    print("Generating GitHub PRs graph...")

    summary_file = ROOT_DIR / "data" / "github_prs_summary.csv"
    if not summary_file.exists():
        print("  No github_prs_summary.csv found")
        return

    df = pd.read_csv(summary_file).sort_values('Quarter')
    # Show ALL data, not just last N quarters
    print(f"  Showing {len(df)} quarters of data")

    figsize = GRAPH_FIGSIZE
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(len(df))
    quarters = df['Quarter'].values

    colors = COLORS

    # Plot all 6 metrics
    ax.plot(x, df['PRs Created'], marker='o', linewidth=2, markersize=8,
            label='PRs Created', color=colors['maintainer'])
    ax.plot(x, df['PRs Merged'], marker='s', linewidth=2, markersize=8,
            label='PRs Merged', color=colors['merged'])
    ax.plot(x, df['PRs Open'], marker='^', linewidth=2, markersize=8,
            label='PRs Open', color=colors['open'])
    ax.plot(x, df['External PRs Created'], marker='D', linewidth=2, markersize=6,
            label='External Created', color=colors['external'], linestyle='--')
    ax.plot(x, df['External PRs Merged'], marker='v', linewidth=2, markersize=6,
            label='External Merged', color=colors['closed'], linestyle='--')
    ax.plot(x, df['External PRs Open'], marker='<', linewidth=2, markersize=6,
            label='External Open', color='#FF6B6B', linestyle='--')

    ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Pull Requests', fontsize=12, fontweight='bold')
    ax.set_title('GitHub Pull Requests Statistics per Quarter', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(quarters, rotation=45, ha='right')
    ax.legend(loc='best', fontsize=10)

    if SHOW_GRID:
        ax.grid(alpha=0.3)

    save_graph("github-prs.png")


def generate_github_issues_graph(quarter):
    """Generate GitHub Issues stats per quarter (all 4 metrics) - shows ALL historical data"""
    print("Generating GitHub Issues graph...")

    summary_file = ROOT_DIR / "data" / "github_issues_summary.csv"
    if not summary_file.exists():
        print("  No github_issues_summary.csv found")
        return

    df = pd.read_csv(summary_file).sort_values('Quarter')
    # Show ALL data, not just last N quarters
    print(f"  Showing {len(df)} quarters of data")

    figsize = GRAPH_FIGSIZE
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(len(df))
    quarters = df['Quarter'].values

    colors = COLORS

    # Plot all 4 metrics
    ax.plot(x, df['Issues Created'], marker='o', linewidth=2, markersize=8,
            label='Issues Created', color=colors['maintainer'])
    ax.plot(x, df['Issues Closed'], marker='s', linewidth=2, markersize=8,
            label='Issues Closed', color=colors['merged'])
    ax.plot(x, df['External Issues Created'], marker='D', linewidth=2, markersize=6,
            label='External Created', color=colors['external'], linestyle='--')
    ax.plot(x, df['External Issues Closed'], marker='v', linewidth=2, markersize=6,
            label='External Closed', color=colors['closed'], linestyle='--')

    ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Issues', fontsize=12, fontweight='bold')
    ax.set_title('GitHub Issues Statistics per Quarter', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(quarters, rotation=45, ha='right')
    ax.legend(loc='best', fontsize=10)

    if SHOW_GRID:
        ax.grid(alpha=0.3)

    plt.tight_layout()

    save_graph("github-issues.png")


def generate_legacy_roles_per_role_graph(quarter):
    """Generate legacy roles downloads per role (current quarter only, sorted)"""
    print("Generating Galaxy legacy roles per-role graph...")

    data_dir = ROOT_DIR / "data" / quarter
    if not data_dir.exists():
        print(f"  Quarter directory {quarter} does not exist - skipping per-role graph")
        return

    data_file = data_dir / "galaxy_legacy.csv"
    if not data_file.exists():
        print(f"  No galaxy_legacy.csv found for {quarter}")
        return

    df = pd.read_csv(data_file)

    # Sort by download count (ascending - smallest to highest)
    df = df.sort_values('download_count', ascending=True)

    figsize = (10, 12)
    fig, ax = plt.subplots(figsize=figsize)

    y_pos = np.arange(len(df))
    colors = COLORS

    ax.barh(y_pos, df['download_count'].values, color=colors['merged'])

    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['name'].values, fontsize=9)
    ax.set_xlabel('Downloads', fontsize=12, fontweight='bold')
    ax.set_title(f'Galaxy Legacy Roles Downloads ({quarter})',
                 fontsize=14, fontweight='bold')

    if SHOW_GRID:
        ax.grid(axis='x', alpha=0.3)

    # Add value labels
    for i, val in enumerate(df['download_count'].values):
        ax.text(val, i, f' {val:,}', va='center', fontsize=8)

    plt.tight_layout()

    save_graph(f"galaxy-legacy-per-role-{quarter}.png")


def generate_legacy_roles_quarterly_delta_graph(quarter):
    """Generate legacy roles quarterly downloads delta (growth during the quarter)"""
    print("Generating Galaxy legacy roles quarterly delta graph...")

    # Read historical per-role CSV
    history_file = ROOT_DIR / "data" / "galaxy_legacy_per_role_history.csv"
    if not history_file.exists():
        print(f"  No per-role history file found - skipping delta graph")
        return

    history_df = pd.read_csv(history_file)

    # Check if current quarter exists in history
    if quarter not in history_df.columns:
        print(f"  Quarter {quarter} not found in history - skipping delta graph")
        return

    # Find previous quarter column
    quarters = [col for col in history_df.columns if col != 'Role' and col.startswith('20')]
    quarters = sorted(quarters)

    if quarter not in quarters:
        print(f"  Quarter {quarter} not in history columns - skipping delta graph")
        return

    current_idx = quarters.index(quarter)
    if current_idx == 0:
        print(f"  No previous quarter available - skipping delta graph")
        return

    prev_quarter = quarters[current_idx - 1]
    print(f"  Comparing {quarter} to {prev_quarter}")

    # Extract current and previous quarter data
    current_df = history_df[['Role', quarter]].copy()
    current_df.columns = ['name', 'download_count_current']
    current_df['download_count_current'] = pd.to_numeric(current_df['download_count_current'], errors='coerce').fillna(0)

    prev_df = history_df[['Role', prev_quarter]].copy()
    prev_df.columns = ['name', 'download_count_prev']
    prev_df['download_count_prev'] = pd.to_numeric(prev_df['download_count_prev'], errors='coerce').fillna(0)

    # Merge on role name
    merged = pd.merge(current_df, prev_df, on='name', how='outer')

    # Fill NaN with 0 (for roles that didn't exist in previous quarter)
    merged['download_count_prev'] = merged['download_count_prev'].fillna(0)
    merged['download_count_current'] = merged['download_count_current'].fillna(0)

    # Calculate delta (downloads gained during this quarter)
    merged['delta'] = (merged['download_count_current'] - merged['download_count_prev']).astype(int)

    # Sort by delta (ascending - smallest to highest growth)
    merged = merged.sort_values('delta', ascending=True)

    figsize = (10, 12)
    fig, ax = plt.subplots(figsize=figsize)

    y_pos = np.arange(len(merged))
    colors = COLORS

    # Use different colors for positive and negative deltas
    bar_colors = [colors['merged'] if val >= 0 else colors['closed'] for val in merged['delta'].values]

    ax.barh(y_pos, merged['delta'].values, color=bar_colors)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(merged['name'].values, fontsize=9)
    ax.set_xlabel('Downloads This Quarter (Delta)', fontsize=12, fontweight='bold')
    ax.set_title(f'Galaxy Legacy Roles - Quarterly Growth ({quarter})',
                 fontsize=14, fontweight='bold')

    if SHOW_GRID:
        ax.grid(axis='x', alpha=0.3)

    # Add value labels
    for i, val in enumerate(merged['delta'].values):
        ax.text(val, i, f' {int(val):+,}', va='center', fontsize=8)

    plt.tight_layout()

    save_graph(f"galaxy-legacy-per-role-delta-{quarter}.png")


def generate_legacy_total_graph(quarter):
    """Generate total legacy roles downloads - shows ALL historical data"""
    print("Generating Galaxy legacy total downloads graph...")

    summary_file = ROOT_DIR / "data" / "galaxy_legacy_summary.csv"
    if not summary_file.exists():
        print("  No galaxy_legacy_summary.csv found")
        return

    df = pd.read_csv(summary_file).sort_values('Quarter')
    # Show ALL data, not just last N quarters
    print(f"  Showing {len(df)} quarters of data")

    figsize = GRAPH_FIGSIZE
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(len(df))
    quarters = df['Quarter'].values
    downloads = df['Total Downloads'].values

    colors = COLORS

    ax.plot(x, downloads, marker='o', linewidth=3, markersize=10,
            color=colors['merged'], label='Total Downloads')

    # Add trend line if enabled
    if SHOW_TRENDS and len(x) > 2:
        z = np.polyfit(x, downloads, 1)
        p = np.poly1d(z)
        ax.plot(x, p(x), "--", alpha=0.5, color=colors['closed'],
                linewidth=2, label='Trend')

    ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Downloads (Cumulative)', fontsize=12, fontweight='bold')
    ax.set_title('Galaxy Legacy Roles - Total Downloads Over Time',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(quarters, rotation=45, ha='right')
    ax.legend(loc='best')

    if SHOW_GRID:
        ax.grid(alpha=0.3)

    # Add value labels
    for i, val in enumerate(downloads):
        ax.text(i, val, f'{val:,.0f}', ha='center', va='bottom',
                fontweight='bold', fontsize=9)

    plt.tight_layout()

    save_graph("galaxy-legacy-total.png")


def generate_legacy_quarterly_delta_total_graph(quarter):
    """Generate quarterly delta for total legacy downloads (new downloads per quarter)"""
    print("Generating Galaxy legacy quarterly delta total graph...")

    summary_file = ROOT_DIR / "data" / "galaxy_legacy_summary.csv"
    if not summary_file.exists():
        print("  No galaxy_legacy_summary.csv found")
        return

    df = pd.read_csv(summary_file).sort_values('Quarter')

    if len(df) < 2:
        print("  Need at least 2 quarters to calculate delta")
        return

    # Calculate quarterly delta
    df['Delta'] = df['Total Downloads'].diff()

    # Remove first row (no delta for first quarter)
    df_delta = df[1:].copy()

    print(f"  Showing {len(df_delta)} quarters of delta data")

    figsize = GRAPH_FIGSIZE
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(len(df_delta))
    quarters = df_delta['Quarter'].values
    deltas = df_delta['Delta'].values

    colors = COLORS

    # Bar chart of quarterly growth
    ax.bar(x, deltas, color=colors['merged'], alpha=0.8, label='Quarterly Growth')

    ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
    ax.set_ylabel('New Downloads (Quarterly)', fontsize=12, fontweight='bold')
    ax.set_title('Galaxy Legacy Roles - Quarterly Download Growth',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(quarters, rotation=45, ha='right')
    ax.legend(loc='best')

    if SHOW_GRID:
        ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for i, val in enumerate(deltas):
        ax.text(i, val, f'{val:,.0f}', ha='center', va='bottom',
                fontweight='bold', fontsize=9)

    plt.tight_layout()

    save_graph("galaxy-legacy-total-delta.png")


def generate_collection_graph(quarter, collection_name):
    """Generate individual collection downloads graph - shows ALL historical data"""
    print(f"Generating {collection_name} downloads graph...")

    summary_file = ROOT_DIR / "data" / "galaxy_collections_summary.csv"
    if not summary_file.exists():
        print("  No galaxy_collections_summary.csv found")
        return

    df = pd.read_csv(summary_file).sort_values('Quarter')
    # Show ALL data, not just last N quarters
    print(f"  Showing {len(df)} quarters of data")

    if collection_name not in df.columns:
        print(f"  Collection {collection_name} not found in summary")
        return

    figsize = GRAPH_FIGSIZE
    fig, ax = plt.subplots(figsize=figsize)

    x = np.arange(len(df))
    quarters = df['Quarter'].values
    downloads = df[collection_name].values

    colors = COLORS
    color = colors['maintainer'] if 'fedora' in collection_name else colors['external']

    ax.plot(x, downloads, marker='o', linewidth=3, markersize=10,
            color=color, label=collection_name)

    # Add trend line if enabled
    if SHOW_TRENDS and len(x) > 2:
        z = np.polyfit(x, downloads, 1)
        p = np.poly1d(z)
        ax.plot(x, p(x), "--", alpha=0.5, color=colors['closed'],
                linewidth=2, label='Trend')

    ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
    ax.set_ylabel('Downloads (Quarterly)', fontsize=12, fontweight='bold')
    ax.set_title(f'{collection_name} - Downloads per Quarter',
                 fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(quarters, rotation=45, ha='right')
    ax.legend(loc='best')

    if SHOW_GRID:
        ax.grid(alpha=0.3)

    # Add value labels
    for i, val in enumerate(downloads):
        ax.text(i, val, f'{val:,.0f}', ha='center', va='bottom',
                fontweight='bold', fontsize=9)

    # Sanitize filename and save
    safe_name = collection_name.replace('.', '-')
    save_graph(f"galaxy-collection-{safe_name}.png")


def main():
    # Get quarter from environment
    quarter = os.getenv('QUARTER')
    if not quarter:
        print("ERROR: QUARTER environment variable not set")
        print("Usage: QUARTER=2025-Q1 python generate_graphs.py")
        sys.exit(1)

    # Setup plot style
    setup_plot_style()

    # Ensure output directory exists
    output_dir = ROOT_DIR / "reports" / "images"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating graphs for {quarter}...")
    print("=" * 60)

    # Generate all graphs
    generate_github_prs_graph(quarter)
    generate_github_issues_graph(quarter)
    generate_legacy_roles_per_role_graph(quarter)
    generate_legacy_roles_quarterly_delta_graph(quarter)
    generate_legacy_total_graph(quarter)
    generate_legacy_quarterly_delta_total_graph(quarter)
    generate_collection_graph(quarter, 'fedora.linux_system_roles')
    generate_collection_graph(quarter, 'microsoft.sql')

    print("=" * 60)
    print(f"✅ Graph generation complete for {quarter}")
    print(f"   Output directory: {output_dir}")


if __name__ == '__main__':
    main()
