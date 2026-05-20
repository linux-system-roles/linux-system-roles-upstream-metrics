# Linux System Roles - 2026-Q2 Quarterly Metrics Analysis

**Report Date:** May 20, 2026  
**Data Status:** ⚠️ **PARTIAL** - Q2 2026 is in progress (50 days into 91-day quarter)

---

## Executive Summary

**This analysis covers incomplete Q2 2026 data as of May 20, 2026 (approximately 55% through the quarter).** The project shows strong PR merge efficiency (94.4%) but faces concerning trends in external contributor engagement, issue management, and Galaxy downloads. PR activity is on pace for a solid quarter (projecting ~295 PRs), but 37 open PRs represent the highest backlog in recent history. Most critically, Galaxy Collections downloads are tracking for a potential 58% decline versus Q1, and zero issues have been resolved despite 7 created.

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

**QoQ Comparison (Q2 vs Q1):**
- PR creation pace: On track for +69% increase (295 projected vs 175 in Q1)
- External contribution %: -21% decline (9.9% vs 12.6%)
- Merge efficiency: +2 percentage points improvement

### Issue Management (Partial Q2 Data)
- **Issues Created:** 7 (projects to ~13 for full quarter)
- **Issues Closed:** 0 ⚠️
- **External Issues:** 7 (100% of total)
- **Issue Resolution Rate:** 0% (down from 21.4% in Q1)

**QoQ Comparison:**
- Issue creation tracking lower than Q1 (14 issues)
- Resolution rate: Critical decline (0% vs 21.4% in Q1)

### Galaxy Downloads

#### Legacy Roles (Cumulative Total: 3,440,113)
- **Quarterly Downloads (Q2 so far):** 86,384
- **Projected Full Quarter:** ~173,000 (35% decline from Q1's 266,020)
- **QoQ Growth:** Tracking for significant decline

**Historical Quarterly Downloads:**
- 2025-Q3: 312,244
- 2025-Q4: 258,742
- 2026-Q1: 266,020
- 2026-Q2 (projected): ~173,000

#### Collections 
- **Q2 Downloads (so far):** 81,283
  - fedora.linux_system_roles: 71,296
  - microsoft.sql: 9,987
- **Projected Full Quarter:** ~162,000 (58% decline from Q1's 389,449)
- **QoQ Growth:** Tracking for major decline

**Historical Quarterly Downloads:**
- 2025-Q3: 359,885
- 2025-Q4: 331,969
- 2026-Q1: 389,449
- 2026-Q2 (projected): ~162,000

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

### Issue Management: Critical Failure

**Zero issues resolved** despite 7 created is a major red flag:
- Issue resolution rate of 0% vs 21.4% in Q1 (which was already low)
- All 7 issues created were external issues - 100% external rate
- This suggests:
  - Review capacity is entirely focused on PRs, leaving issues unaddressed
  - Potential contributor frustration as reported issues languish
  - Growing technical debt as bugs/requests accumulate

### Galaxy Downloads: Sharp Decline Across Both Platforms

**Legacy Roles Slowdown:**
- Quarterly downloads declined from steady ~260-310K range to projected ~173K (35% drop)
- This breaks a pattern of consistent 250K-300K quarterly downloads
- Potential causes: competition, platform changes, or user migration to collections

**Collections Collapse:**
- Tracking for a catastrophic 58% decline (389K → ~162K projected)
- fedora.linux_system_roles is the primary driver: 369K in Q1 → projecting only ~142K in Q2
- microsoft.sql holding steady (~20K), suggesting the issue is specific to Linux System Roles federation

**Top Downloaded Roles (Q2 Partial Data):**
1. timesync: 920,787
2. sshd: 650,808
3. network: 346,303
4. cockpit: 210,646
5. selinux: 191,642
6. journald: 188,227
7. bootloader: 173,578
8. postfix: 146,081
9. crypto_policies: 142,625
10. storage: 112,056

---

## Highlights & Achievements

1. **Excellent PR Merge Efficiency:** 94.4% merge rate demonstrates strong code quality and effective review processes
2. **High PR Velocity:** On pace for 295 PRs (69% increase over Q1), showing active development
3. **Strong Core Roles:** Top roles (timesync, sshd, network) continue to see substantial usage
4. **Consistent Merging:** 118 PRs merged already shows team is actively clearing review queue

---

## Risks & Concerns

### Critical (Require Immediate Action)

1. **Zero Issue Resolution**
   - 0% resolution rate with 7 open issues
   - All external issues ignored may damage community trust
   - Growing backlog of potential bugs/feature requests

2. **Galaxy Collections Download Collapse**
   - Tracking for 58% decline in Q2 (389K → ~162K)
   - fedora.linux_system_roles specifically down 62% (369K → ~142K projected)
   - This may indicate:
     - Platform/distribution changes affecting discoverability
     - Users migrating away from Ansible Galaxy
     - Competition from alternative automation tools
     - Technical issues with Galaxy federation

### High Priority

3. **Unprecedented PR Backlog**
   - 37 open PRs is 6-37x higher than recent quarters
   - Risk of contributor frustration if PRs stall
   - Potential merge conflicts as PRs age

4. **Declining External Contributor Engagement**
   - External contribution % dropped to 9.9% (vs 12.6% in Q1, 26.1% in Q4 2025)
   - External PR acceptance rate fell to 78.6% (vs 95.2% in Q1)
   - Lower acceptance + ignored issues = recipe for losing contributors

5. **Legacy Galaxy Downloads Decline**
   - 35% decline in quarterly downloads (266K → ~173K projected)
   - Breaks pattern of stable 250-300K quarterly performance

---

## Growth Opportunities

1. **Leverage High-Traffic Roles for Promotion**
   - timesync, sshd, and network roles are heavily used
   - Could use these as anchors to promote lesser-known but valuable roles
   - Consider: documentation cross-links, usage examples, blog posts

2. **Re-engage External Contributors**
   - Address the 7 open external issues to show responsiveness
   - Review external PR acceptance criteria - is feedback clear and actionable?
   - Implement "good first issue" labeling to attract new contributors

3. **Investigate and Reverse Galaxy Download Decline**
   - Analyze Galaxy federation health for fedora.linux_system_roles
   - Check for platform/discoverability changes
   - Survey users on alternative distribution channels (Git submodules, automation hub, etc.)
   - Consider cross-promotion with Ansible community channels

4. **Capitalize on High PR Merge Rate**
   - 94.4% merge rate shows strong quality
   - Use this efficiency as a selling point for external contributors
   - Document and share review process as a model for other projects

---

## Recommendations

### Immediate Actions (Next 2 Weeks)

1. **Address Issue Backlog Emergency**
   - Triage all 7 open issues (6 external) immediately
   - Assign owners and set resolution targets
   - Establish policy: acknowledge all external issues within 48 hours
   - **Goal:** Achieve >50% issue resolution rate by end of Q2

2. **Investigate Galaxy Download Decline**
   - Review Galaxy federation configuration for fedora.linux_system_roles
   - Check for recent platform changes or API issues
   - Compare download patterns with other federated collections
   - Survey top 5 roles for any technical/access issues
   - **Goal:** Identify root cause by June 1

### Short-term Actions (Through End of Q2)

3. **Clear PR Backlog**
   - Establish target: reduce open PRs to ≤15 by June 30
   - Prioritize external PRs to maintain contributor goodwill
   - Consider dedicated "PR review days" or pairing reviewers
   - Close or convert stale PRs (>30 days inactive)

4. **Improve External Contributor Experience**
   - Review and clarify external PR rejection reasons
   - Ensure all external PR feedback is actionable and constructive
   - Create "good first issue" labels to attract new contributors
   - **Goal:** Increase external PR acceptance rate back to >90%

---

## Appendix: Detailed Calculations

### Metric Formulas Used

- **PR Merge Rate:** (PRs Merged) / (PRs Created - PRs Open) × 100
  - Excludes PRs still under review
- **External PR Acceptance:** (External PRs Merged) / (External PRs Created - External PRs Open) × 100
- **External Contribution %:** (External PRs Created) / (PRs Created) × 100
- **Issue Resolution Rate:** (Issues Closed) / (Issues Created) × 100
- **QoQ Growth:** ((Current - Previous) / Previous) × 100

### Q2 2026 Projections Methodology

Given we are approximately 55% through Q2 (May 20 of 91-day quarter from Apr 1 - Jun 30):
- **Linear projection:** Multiply current values by ~1.82 (91/50)
- **Note:** Projections assume consistent daily rate; actual results may vary due to:
  - Sprint cycles and release cadences
  - Vacation periods and holidays
  - Community contribution patterns

### Historical Context

**PR Activity Comparison:**
- 2025-Q3: 110 created, 93 merged, 5 open
- 2025-Q4: 69 created, 66 merged, 2 open
- 2026-Q1: 175 created, 161 merged, 1 open
- 2026-Q2: 162 created (so far), 118 merged, 37 open

**Issue Activity Comparison:**
- 2025-Q3: 25 created, 14 closed (56% resolution)
- 2025-Q4: 12 created, 6 closed (50% resolution)
- 2026-Q1: 14 created, 3 closed (21% resolution)
- 2026-Q2: 7 created, 0 closed (0% resolution)

---

**Next Analysis:** 2026-Q3 (Expected: October 2026)
