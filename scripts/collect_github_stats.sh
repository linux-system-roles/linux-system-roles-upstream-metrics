#!/bin/bash
# Wrapper script to collect GitHub stats from multiple organizations
# Reads config.yaml and collects stats for each org, combining into single CSV files

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$ROOT_DIR/config.yaml"

# Check required environment variables
if [ -z "$QUARTER" ]; then
    echo "ERROR: QUARTER environment variable not set"
    exit 1
fi

if [ -z "$DATE_RANGE" ]; then
    echo "ERROR: DATE_RANGE environment variable not set"
    exit 1
fi

if [ ! -f "$CONFIG_FILE" ]; then
    echo "ERROR: Config file not found: $CONFIG_FILE"
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

# Parse filter settings from config.yaml
EXCLUDE_BOTS=$(python3 -c "
import yaml
with open('$CONFIG_FILE') as f:
    config = yaml.safe_load(f)
print(str(config['github'].get('filters', {}).get('exclude_bots', True)).lower())
")
PR_TITLE_EXCLUDE_PATTERNS=$(python3 -c "
import yaml
with open('$CONFIG_FILE') as f:
    config = yaml.safe_load(f)
print('\x1f'.join(config['github'].get('filters', {}).get('pr_title_exclude_patterns', [])))
")
export EXCLUDE_BOTS
export PR_TITLE_EXCLUDE_PATTERNS

# Parse organizations from config.yaml
ORG_COUNT=$(python3 -c "
import yaml
with open('$CONFIG_FILE') as f:
    config = yaml.safe_load(f)
print(len(config['github'].get('organizations', [])))
")

for (( i=0; i<ORG_COUNT; i++ )); do
    ORG_NAME=$(python3 -c "
import yaml
with open('$CONFIG_FILE') as f:
    config = yaml.safe_load(f)
print(config['github']['organizations'][$i]['name'])
")

    EXCLUDE_REPOS=$(python3 -c "
import yaml
with open('$CONFIG_FILE') as f:
    config = yaml.safe_load(f)
org = config['github']['organizations'][$i]
print(' '.join(org.get('exclude', [])))
")

    echo "================================================"
    echo "Collecting from $ORG_NAME organization"
    echo "================================================"

    REPOS=$(gh repo list "$ORG_NAME" -L 100 --json name -q '.[].name')

    for repo in $REPOS; do
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

        upstream_org="$ORG_NAME" \
        repo="$repo" \
        DATE_RANGE="$DATE_RANGE" \
        PRS_CSVFILE="$PRS_CSV" \
        ISSUES_CSVFILE="$ISSUES_CSV" \
        "$SCRIPT_DIR/collect_github_repo_stats.sh"
    done

    echo ""
    echo "✓ $ORG_NAME data collected"
    echo ""
done

# Parse individual repositories from config.yaml
REPO_ENTRIES=$(python3 -c "
import yaml
with open('$CONFIG_FILE') as f:
    config = yaml.safe_load(f)
for r in config['github'].get('repositories', []):
    print(r['org'] + ' ' + r['repo'])
")

if [ -n "$REPO_ENTRIES" ]; then
    while IFS=' ' read -r org repo; do
        echo "================================================"
        echo "Collecting from $org/$repo"
        echo "================================================"

        upstream_org="$org" \
        repo="$repo" \
        DATE_RANGE="$DATE_RANGE" \
        PRS_CSVFILE="$PRS_CSV" \
        ISSUES_CSVFILE="$ISSUES_CSV" \
        "$SCRIPT_DIR/collect_github_repo_stats.sh"

        echo ""
        echo "✓ $org/$repo data collected"
        echo ""
    done <<< "$REPO_ENTRIES"
fi

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
