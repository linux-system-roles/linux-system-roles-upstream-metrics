#!/bin/bash
# Wrapper script to collect GitHub stats from multiple organizations
# Reads config.yaml and collects stats for each org, combining into single CSV files

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Check required environment variables
if [ -z "$QUARTER" ]; then
    echo "ERROR: QUARTER environment variable not set"
    exit 1
fi

if [ -z "$DATE_RANGE" ]; then
    echo "ERROR: DATE_RANGE environment variable not set"
    exit 1
fi

DATA_DIR="$ROOT_DIR/data/$QUARTER"
mkdir -p "$DATA_DIR"

PRS_CSV="$DATA_DIR/prs.csv"
ISSUES_CSV="$DATA_DIR/issues.csv"

# Initialize CSV files with headers
echo "Role,PRs Created,PRs Merged,PRs open,Created non-maint,Merged non-maint,Open non-maint" > "$PRS_CSV"
echo "Role,Issues Created,Issues Closed,Created non-maint,Closed non-maint" > "$ISSUES_CSV"

echo "Collecting GitHub statistics for $QUARTER ($DATE_RANGE)..."
echo ""

# Organization 1: linux-system-roles (all repos except excluded)
echo "================================================"
echo "Collecting from linux-system-roles organization"
echo "================================================"

# Get all repos from linux-system-roles org
REPOS=$(gh repo list linux-system-roles -L 100 --json name -q '.[].name')

# Exclusion list from config.yaml
EXCLUDE_REPOS="tft-tests test-harness auto-maintenance linux-system-roles.github.io .github template linux-system-roles-upstream-metrics"

for repo in $REPOS; do
    # Check if repo is in exclusion list
    skip=false
    for excluded in $EXCLUDE_REPOS; do
        if [ "$repo" = "$excluded" ]; then
            skip=true
            break
        fi
    done

    if [ "$skip" = true ]; then
        continue
    fi

    echo "  $repo"

    # Call collect_github_stats.sh for this repo
    upstream_org=linux-system-roles \
    repo="$repo" \
    DATE_RANGE="$DATE_RANGE" \
    PRS_CSVFILE="$PRS_CSV" \
    ISSUES_CSVFILE="$ISSUES_CSV" \
    "$SCRIPT_DIR/collect_github_stats.sh"
done

echo ""
echo "✓ linux-system-roles data collected"
echo ""

# Organization 2: willshersystems/ansible-sshd
echo "================================================"
echo "Collecting from willshersystems/ansible-sshd"
echo "================================================"

upstream_org=willshersystems \
repo=ansible-sshd \
DATE_RANGE="$DATE_RANGE" \
PRS_CSVFILE="$PRS_CSV" \
ISSUES_CSVFILE="$ISSUES_CSV" \
"$SCRIPT_DIR/collect_github_stats.sh"

echo ""
echo "✓ willshersystems/ansible-sshd data collected"
echo ""

# Summary
echo "================================================"
echo "✅ GitHub statistics collection complete"
echo "================================================"
echo "PRs CSV:    $PRS_CSV"
echo "Issues CSV: $ISSUES_CSV"
echo ""
echo "Total repositories:"
wc -l < "$PRS_CSV" | xargs echo -n
echo " entries (including header)"
