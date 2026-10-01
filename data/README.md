# Data Directory Structure

This directory contains historical metrics data and quarterly summaries.

## Directory Structure

```
data/
├── YYYY-QN/                          # Quarter-specific detailed data
│   ├── prs.csv                       # Per-repo PR statistics
│   ├── issues.csv                    # Per-repo issue statistics
│   ├── galaxy_legacy.csv             # Per-role legacy downloads (cumulative)
│   └── galaxy_collections.csv        # Per-collection downloads (cumulative)
│
├── github_prs_summary.csv            # Historical PR totals by quarter
├── github_issues_summary.csv         # Historical issue totals by quarter
├── galaxy_legacy_summary.csv         # Historical legacy downloads (cumulative totals)
├── galaxy_collections_summary.csv    # Historical collection downloads (quarterly deltas)
└── galaxy_collections_cumulative.csv # Cumulative tracking for delta calculation
```

## File Descriptions

### Quarter-Specific Data (data/YYYY-QN/)

Detailed per-repository/per-role data collected each quarter.

**prs.csv** - GitHub pull request statistics per repository
- Columns: Role, PRs Created, PRs Merged, PRs open, Created non-maint, Merged non-maint, Open non-maint

**issues.csv** - GitHub issue statistics per repository
- Columns: Role, Issues Created, Issues Closed, Created non-maint, Closed non-maint

**galaxy_legacy.csv** - Ansible Galaxy legacy role downloads
- Columns: name, download_count
- Note: download_count is CUMULATIVE (total downloads since role creation)

**galaxy_collections.csv** - Ansible Galaxy collection downloads
- Columns: namespace, name, full_name, download_count
- Note: download_count is CUMULATIVE (total downloads since collection creation)

### Summary Files (Historical Aggregates)

**github_prs_summary.csv** - Aggregated PR statistics by quarter
- Columns: Quarter, PRs Created, PRs Merged, PRs Open, External PRs Created, External PRs Merged, External PRs Open
- Values: Sum of all repositories for that quarter

**github_issues_summary.csv** - Aggregated issue statistics by quarter
- Columns: Quarter, Issues Created, Issues Closed, External Issues Created, External Issues Closed
- Values: Sum of all repositories for that quarter

**galaxy_legacy_summary.csv** - Total legacy role downloads by quarter
- Columns: Quarter, Total Downloads
- Values: CUMULATIVE total (sum of all roles' cumulative downloads)
- Use for tracking overall growth trend

**galaxy_collections_summary.csv** - Collection downloads per quarter
- Columns: Quarter, fedora.linux_system_roles, microsoft.sql, infra.leapp, Total Downloads
- Note: per-collection columns are data-driven (added automatically as new collections are collected); Total Downloads is always the last column
- Values: QUARTERLY DELTAS (new downloads in that quarter, not cumulative)
- Calculated by subtracting previous quarter's cumulative from current quarter's cumulative

**galaxy_collections_cumulative.csv** - Cumulative tracking (internal use)
- Columns: Quarter, fedora.linux_system_roles, microsoft.sql, infra.leapp (per-collection columns are added automatically as new collections are collected)
- Values: CUMULATIVE totals at end of each quarter
- Used by update_quarterly_summary.py to calculate deltas
- Automatically updated when running quarterly workflow

## Workflow

When you run `make quarterly-report QUARTER=YYYY-QN`:

1. **Data Collection:**
   - Collects detailed data → saves to `data/YYYY-QN/*.csv`
   - These files contain per-repo/per-role details

2. **Summary Update:**
   - Runs `update_quarterly_summary.py`
   - Aggregates detailed data into totals
   - For GitHub: simple sum of all repos
   - For Galaxy Collections: calculates delta from cumulative tracking
   - Updates the 4 summary CSV files

3. **Graph Generation:**
   - Reads from summary CSV files
   - Generates graphs showing historical trends
   - Saves graphs to `reports/images/`

4. **Report Generation:**
   - Reads from summary CSVs and current quarter data
   - Generates Markdown report with embedded graphs
   - Saves to `reports/YYYY-QN.md`

## Adding Historical Data

To add historical data:

1. **GitHub PRs/Issues:** Add rows to `github_prs_summary.csv` and `github_issues_summary.csv`

2. **Galaxy Legacy:** Add rows to `galaxy_legacy_summary.csv` with cumulative totals

3. **Galaxy Collections:**
   - Add cumulative totals to `galaxy_collections_cumulative.csv`
   - Add quarterly deltas to `galaxy_collections_summary.csv`
   - Calculate deltas: current_quarter_cumulative - previous_quarter_cumulative

## Notes

- Quarter format: `YYYY-QN` (e.g., `2024-Q4`)
- All CSVs use standard CSV format with headers
- Summary files are sorted by quarter (oldest to newest)
- The system automatically maintains consistency between files
