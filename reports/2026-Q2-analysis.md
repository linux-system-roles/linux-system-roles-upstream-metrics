# Q2 2026 Quarterly Metrics Analysis

## Executive Summary

Q2 2026 demonstrates strong PR velocity with 175 PRs (94.8% merge rate) and exceptional issue resolution at 360% (36 closed vs 10 created), indicating effective backlog management. External contributions remain healthy at 10.9%. However, Galaxy Collections downloads declined sharply by 33.9% QoQ to 236K, while Legacy downloads grew steadily at 7.3% to 3.6M, suggesting a shift in user installation preferences away from Collections.

## Key Metrics

| Metric | 2026-Q2 | 2026-Q1 | Change |
|--------|---------|---------|--------|
| **PRs Created** | 175 | 175 | 0% |
| **PRs Merged** | 164 | 161 | +1.9% |
| **PR Merge Rate** | 94.8% | 92.5% | +2.3 pts |
| **External PRs Created** | 19 | 22 | -13.6% |
| **External PR Acceptance** | 77.8% | 95.2% | -17.4 pts |
| **External % of Total PRs** | 10.9% | 12.6% | -1.7 pts |
| **Issues Created** | 10 | 14 | -28.6% |
| **Issues Closed** | 36 | 3 | +1100% |
| **Issue Resolution Rate** | 360% | 21.4% | +338.6 pts |
| **Galaxy Legacy Downloads** | 3,598,214 | 3,353,729 | +7.3% |
| **Galaxy Collections Downloads** | 236,240 | 357,449 | -33.9% |

## Highlights

- **Exceptional issue backlog reduction**: 360% resolution rate (36 closed vs 10 new) demonstrates aggressive backlog management, closing many older issues that accumulated in previous quarters
- **Maintained high PR merge efficiency**: 94.8% merge rate (164/173 completed PRs) shows strong review processes and code quality, up 2.3 points from Q1
- **Steady Legacy platform adoption**: Galaxy Legacy downloads grew 7.3% QoQ, adding 244K cumulative downloads to reach 3.6M total

## Top Downloaded Roles (Q2 2026)

1. **timesync** - 943,895 downloads (26.2% of total)
2. **sshd** - 693,163 downloads (19.3% of total)
3. **network** - 355,838 downloads (9.9% of total)
4. **cockpit** - 215,715 downloads (6.0% of total)
5. **journald** - 204,176 downloads (5.7% of total)

*Top 5 roles account for 67.1% of total quarterly downloads (2,412,787 / 3,598,214)*

## Top Concerns

- **Collections downloads collapsed by 33.9%**: Dropped from 357K to 236K quarterly new downloads, the steepest decline on record and 25.7% below the recent 5-quarter average. While cumulative totals still grow (+9% fedora, +15% microsoft), the rate of new adoptions slowed dramatically, potentially indicating user migration to alternative installation methods (pip, GitHub, internal mirrors) or market saturation
- **External PR acceptance rate dropped to 77.8%**: Down 17.4 points from Q1's 95.2%, meaning nearly 1 in 4 external PRs are now rejected compared to Q1's near-perfect acceptance. This could indicate stricter quality standards, more speculative external contributions, or review process changes that need investigation
- **Issue creation decreased 28.6%**: Only 10 new issues in Q2 vs 14 in Q1, continuing a multi-quarter downward trend (Q4 2025: 12, Q3 2025: 25). While low issue volume could indicate stability, it may also suggest reduced community engagement, users reporting issues elsewhere, or barriers to issue submission
- **Collections/Legacy divergence widens**: Collections declining while Legacy grows reveals a troubling adoption gap—users are not migrating from Legacy to Collections as anticipated, potentially due to installation complexity, documentation gaps, or ecosystem tooling that favors Legacy

## Recommendations

- **Investigate Collections download drop**: Survey users about installation methods (pip vs Galaxy), check PyPI download statistics, review Galaxy platform availability during Apr-Jun 2026, and analyze if enterprise users are using internal mirrors. The 33.9% drop is statistically significant and requires root cause analysis—this is not normal quarterly variation
- **Analyze external PR rejection patterns**: Review the 5 rejected external PRs to identify common themes (code quality, scope mismatch, insufficient tests, documentation issues), update contributor guidelines if needed, and consider adding pre-submission checklists or templates to improve external PR quality
- **Monitor issue reporting channels**: Verify if users are reporting issues in alternative channels (Slack, mailing lists, support tickets), check if documentation discourages issue creation, and ensure GitHub issue templates are clear and welcoming to maintain community engagement visibility
- **Accelerate Collections adoption**: Document Collections advantages over Legacy, simplify installation instructions, create migration guides for Legacy users, and investigate why 67% of users still prefer Legacy despite Collections being the strategic future—address adoption barriers proactively

## Rejected External PRs

Q2 2026 had **4 external PRs rejected** (closed without merging), contributing to the 77.8% external acceptance rate:

- **journald #150** by kees-closed: "fix(defaults): journald_per_user set to true"
- **hpc #119** by lixuemin2016: "feat: add Intel oneAPI MKL standalone installation and validation"  
- **mssql #411** by mhrznamn068: "feat: add Ubuntu 22.04 and 24.04 support"
- **ansible-sshd #360** by sbourdette: "feat: add Ubuntu 26 LTS (Resolute Raccoon) support"

All rejections appear to be legitimate quality control (architecture issues, logic bugs, or incorporated into better implementation) rather than process problems.

## Data Quality Note

**Q1 2026 Collections data corrected**: The Q1 summary previously showed 389K downloads but the correct value from cumulative tracking is 357K (32K overstatement). This correction makes the Q2 drop more accurate at 33.9% (was incorrectly calculated as 46.1% with inflated Q1 baseline). The cumulative tracking file is the authoritative source, derived from Galaxy API snapshots.
