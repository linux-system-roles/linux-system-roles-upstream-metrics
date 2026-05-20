#!/bin/bash

# collect stats about PRs and issues in the given time frame
# by default, look for "external contributors" not role maintainers

set -euo pipefail

# Retry a command with exponential backoff on network errors
retry_command() {
    local max_attempts=3
    local attempt=1
    local delay=5
    local exit_code=0

    while [ $attempt -le $max_attempts ]; do
        if "$@"; then
            return 0
        else
            exit_code=$?

            # Check if we should retry (network/timeout errors)
            if [ $attempt -lt $max_attempts ]; then
                echo "  Attempt $attempt failed, retrying in ${delay}s..." >&2
                sleep $delay
                delay=$((delay * 2))
            fi

            attempt=$((attempt + 1))
        fi
    done

    echo "  Command failed after $max_attempts attempts" >&2
    return $exit_code
}

# "cache" of user lookups
# assumes that if someone is a collaborator on any system roles repo,
# that person is a collaborator on all system roles repos
# this is generally the case for PRs
declare -A USERS
# how many PRs were created for the given role
declare -A PRS_CREATED
# how many PRs were merged
declare -A PRS_MERGED
# how many PRs are open
declare -A PRS_OPEN
# how many PRs were created by non-maintainers
declare -A PRS_CREATED_NON_MAINT
# how many PRs were merged from non-maintainers
declare -A PRS_MERGED_NON_MAINT
# how many PRs are open from non-maintainers
declare -A PRS_OPEN_NON_MAINT
# how many issues were created for the given role
declare -A ISSUES_CREATED
# how many issues were closed
declare -A ISSUES_CLOSED
# how many issues were created by non-maintainers
declare -A ISSUES_CREATED_NON_MAINT
# how many issues were closed from non-maintainers
declare -A ISSUES_CLOSED_NON_MAINT

# silence shellcheck about unset vars
upstream_org="${upstream_org:?upstream_org is unset}"
repo="${repo:?repo is unset}"
if [ -z "${DATE_RANGE:-}" ]; then
    echo ERROR: Please specify DATE_RANGE like this
    echo DATE_RANGE=2024-01-01..2024-06-30
    exit 1
fi

# is the given user a role repo maintainer
user_is_maintainer() {
    local username
    username="$1"
    if [ -z "${USERS[$username]:-}" ]; then
        if retry_command gh api --silent \
          "/repos/$upstream_org/$repo/collaborators/$username" 2> /dev/null; then
            USERS["$username"]=0
        else
            USERS["$username"]=1
        fi
    fi
    return "${USERS[$username]}"
}

# get PRs with retry
get_prs() {
    retry_command gh pr list -R "$upstream_org/$repo" \
      -S "created:$DATE_RANGE" \
      --state all \
      --json number,author,state,title \
      --jq '.[] | "\(.number) \(.author.login) \(.author.is_bot) \(.state) \(.title)"'
}

# get issues created in date range
get_issues_created() {
    retry_command gh issue list -R "$upstream_org/$repo" \
      -S "created:$DATE_RANGE" \
      --state all \
      --json number,author,state \
      --jq '.[] | "\(.number) \(.author.login) \(.author.is_bot) \(.state)"'
}

# get issues closed in date range
get_issues_closed() {
    retry_command gh issue list -R "$upstream_org/$repo" \
      -S "closed:$DATE_RANGE" \
      --state closed \
      --json number,author \
      --jq '.[] | "\(.number) \(.author.login) \(.author.is_bot)"'
}

get_prs > prs.txt
while read -r number author is_bot state title; do
    # exclude bot PRs completely
    if [[ "$is_bot" == "true" ]]; then
        continue
    fi
    # exclude changelog, ci related, and automated citest_skip prs
    if [[ "$title" =~ ^ci: ]]; then
        continue
    fi
    if [[ "$title" =~ ^docs\(changelog\) ]]; then
        continue
    fi
    if [[ "$title" =~ \[citest_skip\] ]]; then
        continue
    fi
    PRS_CREATED["$repo"]=$(("${PRS_CREATED[$repo]:-0}" + 1))
    # see if author is a maintainer
    if ! user_is_maintainer "$author"; then
        PRS_CREATED_NON_MAINT["$repo"]=$(("${PRS_CREATED_NON_MAINT[$repo]:-0}" + 1))
    fi
    case "$state" in
    MERGED) PRS_MERGED["$repo"]=$(("${PRS_MERGED[$repo]:-0}" + 1))
            if ! user_is_maintainer "$author"; then
                PRS_MERGED_NON_MAINT["$repo"]=$(("${PRS_MERGED_NON_MAINT[$repo]:-0}" + 1))
            fi ;;
    CLOSED) : ;;  # PR closed without merging - no action needed
    OPEN) PRS_OPEN["$repo"]=$(("${PRS_OPEN[$repo]:-0}" + 1))
            if ! user_is_maintainer "$author"; then
                PRS_OPEN_NON_MAINT["$repo"]=$(("${PRS_OPEN_NON_MAINT[$repo]:-0}" + 1))
            fi ;;
    *) : ;;  # Unknown state - ignore
    esac
done < prs.txt
rm -f prs.txt

# Count issues created in the date range
get_issues_created > issues_created.txt
# shellcheck disable=SC2034
while read -r number author is_bot state; do
    # exclude bot issues completely
    if [[ "$is_bot" == "true" ]]; then
        continue
    fi
    ISSUES_CREATED["$repo"]=$(("${ISSUES_CREATED[$repo]:-0}" + 1))
    # see if author is a maintainer
    if ! user_is_maintainer "$author"; then
        ISSUES_CREATED_NON_MAINT["$repo"]=$(("${ISSUES_CREATED_NON_MAINT[$repo]:-0}" + 1))
    fi
done < issues_created.txt
rm -f issues_created.txt

# Count issues closed in the date range (separate query to catch older issues)
get_issues_closed > issues_closed.txt
# shellcheck disable=SC2034
while read -r number author is_bot; do
    # exclude bot issues completely
    if [[ "$is_bot" == "true" ]]; then
        continue
    fi
    ISSUES_CLOSED["$repo"]=$(("${ISSUES_CLOSED[$repo]:-0}" + 1))
    # see if author is a maintainer
    if ! user_is_maintainer "$author"; then
        ISSUES_CLOSED_NON_MAINT["$repo"]=$(("${ISSUES_CLOSED_NON_MAINT[$repo]:-0}" + 1))
    fi
done < issues_closed.txt
rm -f issues_closed.txt

if [ -n "${PRS_CSVFILE:-}" ]; then
    if [ ! -s "${PRS_CSVFILE}" ]; then
        echo Role,PRs Created,PRs Merged,PRs open,Created non-maint,Merged non-maint,Open non-maint > "$PRS_CSVFILE"
    fi
    echo "$repo,${PRS_CREATED[$repo]:-0},${PRS_MERGED[$repo]:-0},${PRS_OPEN[$repo]:-0},${PRS_CREATED_NON_MAINT[$repo]:-0},${PRS_MERGED_NON_MAINT[$repo]:-0},${PRS_OPEN_NON_MAINT[$repo]:-0}" >> "$PRS_CSVFILE"
else
    echo In the range "$DATE_RANGE" in "$upstream_org/$repo":
    echo PRs created: "${PRS_CREATED[$repo]:-0}"
    echo PRs merged: "${PRS_MERGED[$repo]:-0}"
    echo PRs open: "${PRS_OPEN[$repo]:-0}"
    echo PRs created by non-maintainers: "${PRS_CREATED_NON_MAINT[$repo]:-0}"
    echo PRs merged from non-maintainers: "${PRS_MERGED_NON_MAINT[$repo]:-0}"
    echo PRs open from non-maintainers: "${PRS_OPEN_NON_MAINT[$repo]:-0}"
fi
if [ -n "${ISSUES_CSVFILE:-}" ]; then
    if [ ! -s "${ISSUES_CSVFILE}" ]; then
        echo Role,Issues Created,Issues Closed,Created non-maint,Closed non-maint > "$ISSUES_CSVFILE"
    fi
    echo "$repo,${ISSUES_CREATED[$repo]:-0},${ISSUES_CLOSED[$repo]:-0},${ISSUES_CREATED_NON_MAINT[$repo]:-0},${ISSUES_CLOSED_NON_MAINT[$repo]:-0}" >> "$ISSUES_CSVFILE"
else
    echo In the range "$DATE_RANGE" in "$upstream_org/$repo":
    echo Issues created: "${ISSUES_CREATED[$repo]:-0}"
    echo Issues closed: "${ISSUES_CLOSED[$repo]:-0}"
    echo Issues created by non-maintainers: "${ISSUES_CREATED_NON_MAINT[$repo]:-0}"
    echo Issues closed from non-maintainers: "${ISSUES_CLOSED_NON_MAINT[$repo]:-0}"
fi
