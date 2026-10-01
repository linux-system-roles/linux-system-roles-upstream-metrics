# Linux System Roles - Upstream Metrics

Automated quarterly metrics reporting for the Linux System Roles project, tracking GitHub activity and Ansible Galaxy downloads.

## Overview

Collects metrics on:
- **GitHub Activity**: Pull requests and issues from linux-system-roles repositories
- **Ansible Galaxy**: Download counts for legacy roles and collections

## Automated Quarterly Collection

GitHub Actions automatically collects metrics on the **last day of each quarter**:
- **March 31** - Collects Q1 data (Jan 1 - Mar 31)
- **June 30** - Collects Q2 data (Apr 1 - Jun 30)
- **September 30** - Collects Q3 data (Jul 1 - Sep 30)
- **December 31** - Collects Q4 data (Oct 1 - Dec 31)

The workflow creates a Pull Request with the collected data and graphs.

### After Data Collection

Once the PR is merged, generate the quarterly analysis report using the AI skill:

```
/analyze-quarterly-metrics 2026-Q2
```

This generates a comprehensive analysis with trends, risks, and recommendations in `reports/2026-Q2-analysis.md`.

## Local Development

### Prerequisites

1. **Python 3.9+**:
   ```bash
   pip install -r requirements.txt
   ```

2. **GitHub CLI (`gh`)**:
   ```bash
   # Install: https://cli.github.com/
   gh auth login
   ```

3. **Environment Variables**:
   ```bash
   export GITHUB_TOKEN="ghp_..."     # Required: Service account token with repo + read:org scopes
   export GALAXY_API_KEY="..."       # Optional: Service account token for Galaxy API
   ```

   **About GITHUB_TOKEN:**
   - **REQUIRED** - Must be a service account token with `repo` and `read:org` scopes
   - **Why:** Used to check if PR authors are repository collaborators (maintainers vs external contributors)
   - **Without it:** ALL PRs will be incorrectly classified as "external"
   
   **About GALAXY_API_KEY:**
   - **Optional** - data collection works without it
   - **Why use it?** Prevents API rate limiting during Galaxy data collection
   - **When needed?** If you hit rate limits (429 errors) during Galaxy API calls

### Quick Start

Run the complete workflow for the current quarter:
```bash
make quarterly-report
```

Or for a specific quarter:
```bash
make quarterly-report QUARTER=2026-Q2
```

### Makefile Targets

```bash
make quarterly-report   # Full workflow: collect + update + graphs
make collect-github     # Collect GitHub PRs/Issues
make collect-galaxy     # Collect Galaxy downloads
make update-summary     # Update summary CSV files
make generate-graphs    # Generate all graphs
make clean              # Remove temporary files
```

## Data Sources

### GitHub
- **Organization:** linux-system-roles (all repos except tft-tests, test-harness, auto-maintenance, .github, template)
- **External repo:** willshersystems/ansible-sshd
- **Time-based queries:** Uses `gh pr list -S "created:2026-04-01..2026-06-30"`
- **Excludes:** Bot PRs/issues, `ci:` PRs, `docs(changelog)` PRs, `[citest_skip]` PRs

**⚠️ Methodology Changes (May 2026):**

1. **Issues Closed Counting:** Prior to May 2026, "Issues Closed" only counted issues that were both created AND closed within the same quarter. Starting May 2026, the metric correctly counts ALL issues closed in the quarter regardless of creation date.
   - Historical data (before May 2026): Undercounts closed issues
   - Future data (May 2026+): Accurate count of issues closed in quarter
   - Comparisons across this boundary are not directly valid

2. **Bot and Automated PR Exclusions:** Starting May 2026, newly excluded:
   - PRs/issues created by bots (using `author.is_bot` field)
   - PRs with `[citest_skip]` in the title (automated test-skip PRs)

   *(Note: `ci:` and `docs(changelog)` PRs were already excluded in historical data since 2023-Q3)*

   Historical data (2023-Q3 through 2026-Q1) includes bot and `[citest_skip]` PRs, slightly inflating counts.

### Ansible Galaxy
- **Legacy roles:** linux-system-roles namespace + willshersystems/sshd
- **Collections:** fedora.linux_system_roles, microsoft.sql, infra.leapp
- **Snapshot-based:** Current totals only (no historical queries available)
- **Delta calculation:** Current quarter total minus previous quarter total

## Graphs Generated

**Historical (all quarters):**
- `github-prs.png` - PR statistics over time (6 metrics)
- `github-issues.png` - Issue statistics over time (4 metrics)
- `galaxy-legacy-total.png` - Cumulative legacy downloads
- `galaxy-legacy-total-delta.png` - Quarterly delta downloads
- `galaxy-collections-total.png` - Cumulative collections downloads (all collections combined)
- `galaxy-collections-total-delta.png` - Quarterly delta downloads (all collections combined)
- `galaxy-collection-*.png` - Collection downloads per quarter

**Quarter-specific:**
- `galaxy-legacy-per-role-2026-Q2.png` - Per-role cumulative totals
- `galaxy-legacy-per-role-delta-2026-Q2.png` - Per-role quarterly growth

## GitHub Actions Workflow

### Manual Trigger

1. Go to **Actions** → **Quarterly Metrics Report**
2. Click **Run workflow**
3. Optionally override quarter and date range
4. Click **Run workflow**

The workflow creates a Pull Request with the collected data.

### Required Secrets

- **`GH_PUSH_TOKEN`** (**REQUIRED**) - Service account token with `repo` and `read:org` scopes
  - **Why required:** The default `GITHUB_TOKEN` cannot check collaborator status across repositories, causing all PRs to be incorrectly classified as "external"
  - **What it is:** GitHub token from a service account with access to the linux-system-roles organization
  - **Validation:** The workflow will fail with a clear error if this token is missing or lacks proper permissions
- **`GALAXY_API_KEY`** (Optional) - Service account token for Ansible Galaxy API
  - **Why use it:** Prevents Galaxy API rate limiting during data collection
  - **What it is:** API token from a service account on galaxy.ansible.com

## Troubleshooting

### GitHub Authentication
```bash
gh auth status    # Check authentication
gh auth login     # Re-authenticate
```

### Rate Limiting
If you see "rate limited" errors from Galaxy API:
```bash
export GALAXY_API_KEY="your-api-key"
```

### Network Timeouts
Retry logic handles most timeouts automatically (3 attempts with exponential backoff). If issues persist, check GitHub/Galaxy API status.

## License

See [LICENSE](LICENSE) file.
