# Linux System Roles - 2026-Q2 Quarterly Metrics Analysis

**Report Date:** May 20, 2026  
**Data Status:** ⚠️ **PARTIAL** - Q2 2026 is in progress (50 days into 91-day quarter)

---

## Executive Summary

**This analysis covers incomplete Q2 2026 data as of May 20, 2026 (approximately 55% through the quarter).** The project demonstrates strong PR merge efficiency (94.4%) and improved issue resolution from earlier in the quarter, but faces significant challenges in external contributor engagement and Galaxy downloads. PR activity is on pace for a strong quarter (projecting ~295 PRs), though 37 open PRs represent an unprecedented backlog. Most concerning: Galaxy Collections downloads are tracking for a 58-62% decline versus Q1, and issue resolution remains critically low at 28.6% despite showing improvement from 0%.

---

## Key Findings

### Improvements
- **Issue Resolution:** Up from 0% to 28.6% (2 issues closed mid-quarter)
- **PR Merge Rate:** Strong 94.4% efficiency maintained

### Critical Concerns
1. **Galaxy Collections Downloads Collapsing:** Tracking for 62% decline (389K → ~149K projected)
2. **PR Backlog Unprecedented:** 37 open PRs vs typical 1-6 in prior quarters
3. **External Contributor Decline:** Only 9.9% external PRs vs 12.6% in Q1
4. **Issue Resolution Still Low:** 28.6% rate well below historical 50-56%

### Top Recommendations
1. **Immediate:** Investigate Galaxy download collapse (62% decline is catastrophic)
2. **Short-term:** Clear PR backlog to ≤15 by end of Q2
3. **Ongoing:** Maintain issue resolution momentum (target ≥50% rate)

---

## Key Metrics Overview

### Pull Request Activity (Partial Q2 Data)
- **PRs Created:** 162 (projects to ~295 for full quarter)
- **PRs Merged:** 118 (projects to ~215 for full quarter)
- **PRs Currently Open:** 37 ⚠️ (highest backlog observed)
- **External PRs Created:** 16 (9.9% of total, down from 12.6% in Q1)
- **External PRs Merged:** 11
- **PR Merge Rate:** 94.4% (up from 92.5% in Q1)
- **External PR Acceptance Rate:** 78.6% (down from 95.2% in Q1)

**QoQ Comparison (Q2 vs Q1 - Projected):**
- PR creation pace: On track for +69% increase (295 projected vs 175 in Q1)
- External contribution %: -21% decline (9.9% vs 12.6%)
- Merge efficiency: +2 percentage points improvement

### Issue Management (Partial Q2 Data)
- **Issues Created:** 7 (projects to ~13 for full quarter)
- **Issues Closed:** 2 ⚠️ (projects to ~4 for full quarter)
- **External Issues Created:** 7 (100% of total)
- **External Issues Closed:** 2
- **Issue Resolution Rate:** 28.6% (up from 0%, but still well below Q1's 21.4%)

**QoQ Comparison:**
- Issue creation tracking similar to Q1 (14 issues)
- Resolution rate: Critical improvement mid-quarter (0% → 28.6%), but projected 31% is still concerning

### Galaxy Downloads

#### Legacy Roles (Cumulative Total: 3,440,878)
- **Quarterly Downloads (Q2 so far):** 87,149
- **Projected Full Quarter:** ~159,000 (40% decline from Q1's 266,020)
- **QoQ Growth:** Tracking for significant decline

**Historical Quarterly Downloads:**
- 2025-Q3: 312,244
- 2025-Q4: 258,742
- 2026-Q1: 266,020
- 2026-Q2 (projected): ~159,000

#### Collections 
- **Q2 Downloads (so far):** 81,752
  - fedora.linux_system_roles: 71,725
  - microsoft.sql: 10,027
- **Projected Full Quarter:** ~149,000 (62% decline from Q1's 389,449)
- **QoQ Growth:** Tracking for catastrophic decline

**Collection Cumulative Totals (End of Q2):**
- fedora.linux_system_roles: 2,572,336
- microsoft.sql: 112,578
- Total: 2,684,914

**Historical Quarterly Downloads:**
- 2025-Q3: 359,885
- 2025-Q4: 331,969
- 2026-Q1: 389,449
- 2026-Q2 (projected): ~149,000

---

## Trend Analysis

### PR Activity: High Volume, Excellent Efficiency, Growing Backlog

**Positives:**
- Merge rate of 94.4% is the second-highest in recent history (only 2025-Q4's 98.5% was higher)
- PR creation pace is strong - projecting 295 PRs for the full quarter would be a 69% increase over Q1
- Team is actively merging work (118 merged already, on pace for ~215)

**Concerns:**
- **37 open PRs is unprecedented** - previous quarters typically ended with 1-6 open PRs
- This suggests either a spike in PR volume outpacing review capacity, or PRs requiring more iteration
- At current pace, we may end Q2 with 60+ open PRs if merge velocity doesn't accelerate

### External Contributions: Declining Engagement and Acceptance

**Declining Participation:**
- External contribution percentage dropped to 9.9%, down from 12.6% in Q1 and 26.1% in Q4 2025
- Only 16 external PRs created so far (projecting ~29 for full quarter vs 22 in Q1)
- This represents a multi-quarter downward trend in external engagement

**Lower Acceptance Rate:**
- External PR acceptance rate fell to 78.6%, down from 95.2% in Q1
- This is concerning: lower acceptance could discourage future contributions
- Suggests either quality issues with external PRs or stricter review standards

### Issue Management: Improvement But Still Critical

**Recent Progress:**
- 2 issues resolved mid-quarter (up from 0 in earlier snapshot)
- Resolution rate improved to 28.6%, showing responsiveness
- Both resolved issues were external, demonstrating community engagement

**Remaining Concerns:**
- Projected 31% resolution rate for full quarter is still far below historical norms (50-56% in Q3-Q4 2025)
- 5 issues remain open, all from external contributors
- Issue resolution continues to lag PR activity, suggesting capacity constraints

### Galaxy Downloads: Sharp Decline Across Both Platforms

**Legacy Roles Slowdown:**
- Quarterly downloads declined from steady ~260-310K range to projected ~159K (40% drop)
- This breaks a pattern of consistent 250K-300K quarterly downloads
- Potential causes: competition, platform changes, or user migration to collections

**Collections Collapse:**
- Tracking for a catastrophic 62% decline (389K → ~149K projected)
- fedora.linux_system_roles is the primary driver: 389K in Q1 → projecting only ~149K in Q2
- microsoft.sql: 20K in Q1 → projecting ~18K in Q2 (similar 9% decline)
- The decline affects both collections, suggesting systemic issues

**Top Downloaded Roles (Q2 Cumulative Totals):**
1. timesync: 920,898
2. sshd: 650,985
3. network: 346,387
4. cockpit: 210,674
5. selinux: 191,690
6. journald: 188,266
7. bootloader: 173,621
8. postfix: 146,101
9. crypto_policies: 142,654
10. storage: 112,064

---

## Highlights & Achievements

1. **Excellent PR Merge Efficiency:** 94.4% merge rate demonstrates strong code quality and effective review processes
2. **High PR Velocity:** On pace for 295 PRs (69% increase over Q1), showing active development
3. **Strong Core Roles:** Top roles (timesync, sshd, network) continue to see substantial usage with 900K+, 650K+, and 346K+ cumulative downloads respectively
4. **Consistent Merging:** 118 PRs merged already shows team is actively clearing review queue
5. **Mid-Quarter Course Correction:** Issue resolution improved from 0 to 2, showing responsiveness to backlog

---

## Risks & Concerns

### Critical (Require Immediate Action)

1. **Galaxy Collections Download Collapse**
   - Tracking for 62% decline in Q2 (389K → ~149K)
   - fedora.linux_system_roles down from 369K → ~130K projected
   - microsoft.sql also declining (20K → ~18K projected)
   - This may indicate:
     - Platform/distribution changes affecting discoverability
     - Users migrating away from Ansible Galaxy
     - Competition from alternative automation tools
     - Technical issues with Galaxy federation or API
     - Changes in Ansible ecosystem (e.g., automation hub adoption)

2. **Low Issue Resolution Rate**
   - Despite improvement to 28.6%, still projects to only 31% for full quarter
   - Historical norms were 50-56% in Q3-Q4 2025
   - 5 external issues remain unresolved mid-quarter
   - Risk of contributor frustration and technical debt accumulation

### High Priority

3. **Unprecedented PR Backlog**
   - 37 open PRs is 6-37x higher than recent quarters
   - Risk of contributor frustration if PRs stall
   - Potential merge conflicts as PRs age
   - May indicate review capacity constraints

4. **Declining External Contributor Engagement**
   - External contribution % dropped to 9.9% (vs 12.6% in Q1, 26.1% in Q4 2025)
   - External PR acceptance rate fell to 78.6% (vs 95.2% in Q1)
   - Multi-quarter downward trend in external participation
   - Lower acceptance + slower issue resolution = recipe for losing contributors

5. **Legacy Galaxy Downloads Decline**
   - 40% decline in quarterly downloads (266K → ~159K projected)
   - Breaks pattern of stable 250-300K quarterly performance
   - May indicate broader ecosystem shift away from legacy roles

---

## Growth Opportunities

1. **Leverage High-Traffic Roles for Promotion**
   - timesync (920K+), sshd (650K+), and network (346K+) are heavily adopted
   - Could use these as anchors to promote lesser-known but valuable roles
   - Consider: documentation cross-links, usage examples, blog posts, video tutorials

2. **Re-engage External Contributors**
   - Address the 5 remaining open external issues to show responsiveness
   - Review external PR acceptance criteria - is feedback clear and actionable?
   - Implement "good first issue" labeling to attract new contributors
   - Highlight the 28.6% resolution rate improvement as evidence of renewed focus

3. **Investigate and Reverse Galaxy Download Decline**
   - Analyze Galaxy federation health for fedora.linux_system_roles
   - Check for platform/discoverability changes on Galaxy
   - Compare with other federated collections to identify if issue is project-specific
   - Survey users on alternative distribution channels (Git submodules, Automation Hub, etc.)
   - Monitor Ansible ecosystem trends (AAP adoption, automation hub migration)
   - Consider cross-promotion with Ansible community channels

4. **Capitalize on High PR Merge Rate**
   - 94.4% merge rate shows strong quality and effective collaboration
   - Use this efficiency as a selling point for external contributors
   - Document and share review process as a model for other projects
   - Highlight in community outreach and contributor guides

5. **Expand microsoft.sql Collection Ecosystem**
   - microsoft.sql showing steady ~10K quarterly downloads
   - Opportunity to grow SQL Server automation community
   - Could promote this collection to Windows/SQL Server admin communities

---

## Recommendations

### Immediate Actions (Next 2 Weeks)

1. **Emergency Investigation: Galaxy Download Collapse**
   - **Priority:** Critical - 62% decline requires immediate root cause analysis
   - Review Galaxy federation configuration for both collections
   - Check for recent platform changes, API issues, or rate limiting
   - Compare download patterns with other federated collections
   - Analyze Galaxy search rankings and discoverability
   - Survey top 5 roles for any technical/access issues
   - Check Ansible community forums for user migration patterns
   - **Goal:** Identify root cause by June 1, implement fixes by mid-June
   - **Owner:** Project leads + DevOps

2. **Continue Issue Resolution Momentum**
   - 2 issues closed mid-quarter shows progress - maintain this pace
   - Triage remaining 5 open external issues immediately
   - Assign owners and set resolution targets for each
   - Establish policy: acknowledge all external issues within 48 hours
   - **Goal:** Achieve ≥50% issue resolution rate by end of Q2
   - **Owner:** Maintainers team

### Short-term Actions (Through End of Q2)

3. **Clear PR Backlog**
   - Establish target: reduce open PRs to ≤15 by June 30
   - Prioritize external PRs to maintain contributor goodwill
   - Consider dedicated "PR review days" or pairing reviewers
   - Close or convert stale PRs (>30 days inactive) with clear communication
   - **Goal:** Return to <10 open PRs by Q3
   - **Owner:** Core reviewers

4. **Improve External Contributor Experience**
   - Review and clarify external PR rejection reasons
   - Ensure all external PR feedback is actionable and constructive
   - Create "good first issue" labels to attract new contributors
   - Publish contributor success stories and highlight merged external PRs
   - **Goal:** Increase external PR acceptance rate back to >90%
   - **Owner:** Community managers + maintainers

5. **Galaxy Download Recovery Plan**
   - Based on root cause analysis from Action #1, develop recovery strategy
   - Potential actions:
     - Fix technical issues (federation, API, discoverability)
     - Launch promotion campaign for top roles
     - Create migration guides if users are shifting platforms
     - Engage with Ansible community to understand ecosystem changes
   - **Goal:** Stabilize downloads at Q1 levels (~380K/quarter) by Q3
   - **Owner:** Marketing + DevOps

### Medium-term Actions (Q3 2026)

6. **External Contributor Engagement Campaign**
   - Launch "good first issue" program
   - Host virtual contributor onboarding sessions
   - Improve documentation for external contributors
   - Recognize and celebrate external contributions publicly
   - **Goal:** Increase external contribution % to >15% by Q4

7. **Diversify Distribution Channels**
   - If Galaxy decline is ecosystem-wide, prepare alternative distribution
   - Evaluate Automation Hub, direct Git consumption, container registries
   - Document alternative installation methods
   - **Goal:** Reduce dependency on single distribution platform

---

## Data Quality Notes

### Methodology Updates
As documented in the README, the following methodology changes were implemented in May 2026:

1. **Issues Closed Counting:** Now counts ALL issues closed in the quarter (regardless of creation date)
   - Historical data (pre-May 2026): Undercounted closed issues
   - Current data (May 2026+): Accurate count
   - **Impact:** Historical comparisons for "Issues Closed" are not directly valid

2. **Bot and Automated PR Exclusions:** Now excludes bot PRs and `[citest_skip]` PRs
   - Historical data: Includes these, slightly inflating counts
   - Current data: Excludes these
   - **Impact:** PR counts may appear lower, but represent actual human contributions more accurately

### Partial Data Considerations
- **Current snapshot:** May 20, 2026 (day 50 of 91-day quarter)
- **Completion:** ~55%
- **Projection method:** Linear extrapolation (actual × 1.82)
- **Limitations:** 
  - Assumes consistent daily rate
  - Does not account for sprint cycles, holidays, or seasonal patterns
  - Galaxy download data is snapshot-based, not historical query
  - PR backlog (37 open) may skew projections if cleared rapidly

---

## Appendix: Detailed Calculations

### Metric Formulas Used

- **PR Merge Rate:** (PRs Merged) / (PRs Created - PRs Open) × 100
  - Example: 118 / (162 - 37) × 100 = 94.4%
  - Excludes PRs still under review
- **External PR Acceptance:** (External PRs Merged) / (External PRs Created - External PRs Open) × 100
  - Example: 11 / 14 × 100 = 78.6% (assuming 2 external PRs still open)
- **External Contribution %:** (External PRs Created) / (PRs Created) × 100
  - Example: 16 / 162 × 100 = 9.9%
- **Issue Resolution Rate:** (Issues Closed) / (Issues Created) × 100
  - Example: 2 / 7 × 100 = 28.6%
- **QoQ Growth:** ((Current - Previous) / Previous) × 100

### Q2 2026 Projections Methodology

Given we are approximately 55% through Q2 (May 20 of 91-day quarter from Apr 1 - Jun 30):
- **Days elapsed:** 50 (Apr 1 - May 20)
- **Total days:** 91 (Apr: 30, May: 31, Jun: 30)
- **Projection multiplier:** 91/50 = 1.82
- **Linear projection formula:** Current value × 1.82

**Examples:**
- PRs Created: 162 × 1.82 = ~295
- Issues Closed: 2 × 1.82 = ~4 (rounds to 4)
- Legacy Downloads: 87,149 × 1.82 = ~159,000
- Collections Downloads: 81,752 × 1.82 = ~149,000

**Note:** Projections assume consistent daily rate; actual results may vary due to:
- Sprint cycles and release cadences
- Vacation periods and holidays  
- Community contribution patterns
- Seasonal variations in Galaxy downloads

### Historical Context

**PR Activity Comparison:**
- 2025-Q3: 110 created, 93 merged, 5 open (84.5% merge rate)
- 2025-Q4: 69 created, 66 merged, 2 open (98.5% merge rate)
- 2026-Q1: 175 created, 161 merged, 1 open (92.5% merge rate)
- 2026-Q2: 162 created (so far), 118 merged, 37 open (94.4% merge rate)
- 2026-Q2 (projected): ~295 created, ~215 merged, ~40 open

**Issue Activity Comparison:**
- 2025-Q3: 25 created, 14 closed (56% resolution)
- 2025-Q4: 12 created, 6 closed (50% resolution)
- 2026-Q1: 14 created, 3 closed (21% resolution)
- 2026-Q2: 7 created, 2 closed (28.6% resolution)
- 2026-Q2 (projected): ~13 created, ~4 closed (~31% resolution)

**Galaxy Legacy Downloads:**
- 2024-Q2: 1,628,935 (cumulative)
- 2025-Q2: 2,516,723 (cumulative), 195,518 (quarterly)
- 2025-Q3: 2,828,967 (cumulative), 312,244 (quarterly)
- 2025-Q4: 3,087,709 (cumulative), 258,742 (quarterly)
- 2026-Q1: 3,353,729 (cumulative), 266,020 (quarterly)
- 2026-Q2: 3,440,878 (cumulative), 87,149 (partial quarter)
- 2026-Q2 (projected): ~3,512,000 (cumulative), ~159,000 (quarterly)

**Galaxy Collections Downloads:**
- 2024-Q2: 625,000 (cumulative), 183,112 (quarterly)
- 2025-Q2: 1,553,859 (cumulative), 304,490 (quarterly)
- 2025-Q3: 1,913,744 (cumulative), 359,885 (quarterly)
- 2025-Q4: 2,245,713 (cumulative), 331,969 (quarterly)
- 2026-Q1: 2,603,162 (cumulative), 389,449 (quarterly)
- 2026-Q2: 2,684,914 (cumulative), 81,752 (partial quarter)
- 2026-Q2 (projected): ~2,752,000 (cumulative), ~149,000 (quarterly)

---

**Next Analysis:** 2026-Q3 (Expected: October 2026)

---

*This report was generated using the `/analyze-quarterly-metrics` skill for automated quarterly analysis of Linux System Roles upstream metrics.*
