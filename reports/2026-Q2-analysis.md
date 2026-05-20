# Linux System Roles - 2026-Q2 Quarterly Metrics Analysis

**Period:** April 1 - June 30, 2026  
**Report Date:** May 20, 2026  
**Status:** ⚠️ **PARTIAL QUARTER DATA** - Analysis based on ~55% of quarter (50 days)

---

## Executive Summary

**⚠️ This quarter is in progress - data covers approximately 55% of Q2 (through May 20, 2026).**

Q2 2026 shows strong PR activity with excellent merge rates (94.4%), but faces a significant challenge with Galaxy downloads declining across both legacy roles (-40% projected) and collections (-62% projected). External PR acceptance has also dropped notably to 78.6% from 95.2% last quarter, suggesting quality or alignment issues that need immediate attention.

---

## Key Findings

### Improvements
- **PR merge rate improved to 94.4%** (up from 92.5% in Q1) - team is efficiently processing contributions
- **PR volume trending up** - projecting 233 PRs for full quarter (+33% vs Q1's 175)
- **Issue resolution rate improved to 28.6%** (up from 21.4% in Q1)

### Critical Concerns
1. **Galaxy Collections downloads plummeting** - 81.8K downloads so far vs 389K in Q1; projecting -62% QoQ decline to ~149K
2. **Galaxy Legacy downloads declining sharply** - 87.1K new downloads so far vs 266K in Q1; projecting -40% QoQ decline
3. **External PR acceptance rate dropped significantly** - 78.6% acceptance vs 95.2% in Q1 (16.6 percentage point decline); 5 of 16 external PRs not merged
4. **Issue creation rate very low** - only 7 issues created (projecting ~13 for full quarter vs 14 in Q1), could indicate users not reporting problems

### Top Recommendations
1. **Immediate (within 2 weeks):**
   - Investigate Galaxy download decline root cause: check Ansible Galaxy service changes, distribution packaging updates, or emerging competitor tools
   - Review the 5 unmerged external PRs to identify patterns: quality issues, unclear requirements, or documentation gaps

2. **Short-term (through end of Q2):**
   - Set up weekly download monitoring dashboard to track if decline continues or stabilizes
   - Create external contributor guide to improve PR quality and acceptance rate
   - Reach out to major users to understand if they've shifted to alternative solutions

3. **Ongoing:**
   - Monitor external contribution funnel health (creation → acceptance rate)
   - Track download trends by individual role to identify which are most affected

---

## Key Metrics Overview

### Pull Requests (Partial Q2 Data)
| Metric | Q2 2026 (partial) | Q1 2026 | QoQ Change | Projected Q2 Full |
|--------|-------------------|---------|------------|-------------------|
| **PRs Created** | 128 | 175 | -26.9% | ~233 (+33%)* |
| **PRs Merged** | 118 | 161 | -26.7% | ~215 (+33%)* |
| **PRs Open** | 3 | 1 | +200% | ~3 |
| **Merge Rate** | **94.4%** | 92.5% | **+1.9pp** | ~94% |
| **External PRs Created** | 16 | 22 | -27.3% | ~29 (+32%)* |
| **External PRs Merged** | 11 | 20 | -45.0% | ~20 (-0%)* |
| **External Acceptance** | **78.6%** | 95.2% | **-16.6pp** ⚠️ | ~78% |
| **External %** | 12.5% | 12.6% | -0.1pp | ~12.5% |

*Projected values assume current pace continues through end of quarter

### Issues (Partial Q2 Data)
| Metric | Q2 2026 (partial) | Q1 2026 | QoQ Change | Projected Q2 Full |
|--------|-------------------|---------|------------|-------------------|
| **Issues Created** | 7 | 14 | -50.0% | ~13 (-7%)* |
| **Issues Closed** | 2 | 3 | -33.3% | ~4 (+33%)* |
| **Resolution Rate** | **28.6%** | 21.4% | **+7.2pp** | ~31% |
| **External Issues Created** | 7 | 13 | -46.2% | ~13 (0%)* |
| **External %** | 100% | 92.9% | +7.1pp | ~100% |

*Projected values assume current pace continues

### Galaxy Downloads

**Legacy Roles (Cumulative Total: 3,440,878)**
| Metric | Q2 2026 (partial) | Q1 2026 | QoQ Change | Projected Q2 Full |
|--------|-------------------|---------|------------|-------------------|
| **Quarterly Downloads** | 87,149 | 266,020 | -67.2% | **~158,453 (-40.4%)** ⚠️ |
| **Daily Download Rate** | ~1,743/day | ~2,956/day | -41.0% | ~1,743/day |

**Collections (Fedora + Microsoft SQL)**
| Metric | Q2 2026 (partial) | Q1 2026 | QoQ Change | Projected Q2 Full |
|--------|-------------------|---------|------------|-------------------|
| **Total Downloads** | 81,752 | 389,449 | -79.0% | **~148,640 (-61.8%)** ⚠️ |
| **fedora.linux_system_roles** | 71,725 | 369,140 | -80.6% | ~130,409 (-64.7%) |
| **microsoft.sql** | 10,027 | 20,309 | -50.6% | ~18,231 (-10.2%) |

---

## Trend Analysis

### PR Activity: Strong Volume, Declining External Acceptance
- **Overall PR pace is excellent**: 128 PRs in 50 days projects to ~233 for the full quarter, a 33% increase over Q1
- **Merge efficiency remains high**: 94.4% merge rate shows the team is processing contributions effectively
- **External acceptance is concerning**: Only 78.6% of external PRs (excluding those still open) are being merged, down from 95.2% in Q1
  - 5 external PRs were created but not merged (and 2 are still open)
  - This 16.6 percentage point drop suggests either declining PR quality or unclear contribution guidelines

**Historical Context:**
- Q1 2026: 175 PRs (92.5% merge rate, 95.2% external acceptance)
- Q4 2025: 69 PRs (97.1% merge rate, 94.1% external acceptance)
- Q3 2025: 110 PRs (93.9% merge rate, 83.3% external acceptance)

**Verdict:** PR volume trending positive, but external contributor funnel needs attention.

### Issue Management: Low Volume, Improved Resolution
- **Issue creation is very low**: Only 7 issues created (projecting ~13 vs 14 in Q1)
  - Could indicate users not reporting problems or finding alternative channels
  - 100% of issues are from external users
- **Resolution rate improved to 28.6%** (up from 21.4%), but still means 71% of issues remain open
- **Issue backlog likely growing**: More issues created than closed in most quarters

**Historical Context:**
- Q1 2026: 14 created, 3 closed (21.4% resolution)
- Q4 2025: 12 created, 6 closed (50.0% resolution)
- Q3 2025: 25 created, 14 closed (56.0% resolution)

**Verdict:** Low issue volume is unusual - worth investigating if reporting channels have changed. Resolution rate improving but still low.

### Galaxy Downloads: Significant Decline Across All Metrics

**This is the most concerning trend of Q2.**

**Legacy Roles:**
- Q2 daily rate: ~1,743 downloads/day
- Q1 daily rate: ~2,956 downloads/day
- **Decline: -41%** in daily download rate
- Projecting only 158K downloads for full Q2 vs 266K in Q1 (-40% QoQ)

**Collections:**
- Q2 is on pace for only 149K downloads vs 389K in Q1 (-62% QoQ)
- fedora.linux_system_roles particularly affected: projecting -65% decline
- microsoft.sql projecting -10% decline (less severe)

**Historical Context:**
- Legacy downloads have grown steadily from 1.6M (Q2 2024) to 3.4M (current)
- But *quarterly gains* have varied: 195K → 312K → 259K → 266K → 87K (partial)
- Collections saw strong growth through Q2 2025 (304K) but have been volatile since

**Potential Causes to Investigate:**
1. Ansible Galaxy service changes or outages
2. Distribution packaging changes (Fedora/RHEL moving to different distribution method)
3. Emerging competitor tools or alternative role sources
4. Changes in automation/CI patterns (bulk downloaders stopping)
5. Seasonal variation (May historically slower?)

**Verdict:** This decline is too large to be a data collection issue. Immediate investigation required.

---

## Highlights & Achievements

### What Went Well
1. **PR throughput on track for record quarter**: Projecting 233 PRs created, highest since Q3 2023 (124 PRs) if trend continues
2. **Excellent merge efficiency**: 94.4% merge rate shows healthy code review and contribution process
3. **Issue resolution improving**: 28.6% resolution rate is up 7.2 percentage points from Q1
4. **Strong community engagement**: 100% of issues are externally reported, showing active user base

### Most Downloaded Roles (Cumulative as of May 20, 2026)
Based on all-time cumulative downloads:
1. **timesync**: 920,898 total downloads
2. **sshd**: 650,985 total downloads
3. **network**: 346,387 total downloads
4. **cockpit**: 210,674 total downloads
5. **journald**: 188,266 total downloads

Note: Cannot determine fastest-growing roles for Q2 without Q1 per-role baseline data.

---

## Risks & Concerns

### 🔴 Critical Risks

1. **Steep Galaxy download decline (both legacy & collections)**
   - **Impact**: If trend continues, Q2 could see 40-62% drop in downloads
   - **Evidence**: Legacy at 1,743/day vs 2,956/day in Q1; Collections projecting 149K vs 389K
   - **Action Needed**: Root cause analysis within 2 weeks

2. **External PR acceptance rate dropped to 78.6%**
   - **Impact**: Discourages community contributions, could reduce external engagement
   - **Evidence**: 5 external PRs rejected/not merged in Q2 so far vs only 1 in Q1
   - **Action Needed**: Review rejected PRs for patterns, improve contributor documentation

### 🟡 Medium Risks

3. **Very low issue creation rate**
   - **Impact**: May indicate users not reporting problems or finding alternative channels
   - **Evidence**: Only 7 issues created (projecting ~13 vs 14 in Q1, 25 in Q3 2025)
   - **Action Needed**: Survey users to confirm issues are being captured

4. **Issue backlog likely growing**
   - **Impact**: Growing backlog could indicate resource constraints or prioritization issues
   - **Evidence**: Resolution rate improving but still only 28.6%
   - **Action Needed**: Monitor open issue count trend

---

## Growth Opportunities

1. **Capitalize on strong PR momentum**
   - PR volume up 33% - consider highlighting in community communications
   - Feature popular contributions in blog posts or release notes
   - Recognize top external contributors to encourage continued participation

2. **Improve external contributor success rate**
   - Current 78.6% acceptance suggests room for improvement
   - Create "first PR" templates and contribution guide
   - Pair new contributors with maintainers for initial PRs

3. **Understand and reverse download decline**
   - If decline is due to distribution changes, work with distros to improve discoverability
   - If users are switching to competitors, understand why and adapt
   - If it's a seasonal pattern, document it for future planning

4. **Focus on high-impact roles**
   - timesync, sshd, network, cockpit, and journald are most popular
   - Ensure these roles have excellent docs, examples, and test coverage
   - Consider case studies showing real-world usage

---

## Recommendations

### Immediate Actions (Next 2 Weeks)

1. **Investigate Galaxy download decline**
   - Check Ansible Galaxy service status and any recent API/policy changes
   - Review distribution packaging for Fedora/RHEL - any changes to how roles are delivered?
   - Analyze download patterns by role to identify if specific roles are affected
   - Contact major known users to ask if they've changed their consumption patterns
   - Check competitor landscape - are there new alternative role sources?

2. **Review external PR rejection patterns**
   - Analyze the 5 external PRs that weren't merged
   - Identify common issues: test failures, style problems, unclear requirements?
   - Update CONTRIBUTING.md with specific examples and requirements
   - Consider PR template with checklist to improve quality before submission

### Short-Term Actions (Through End of Q2)

3. **Set up download monitoring dashboard**
   - Weekly download tracking by role and collection
   - Alert thresholds for significant declines
   - Compare to historical patterns to identify seasonality

4. **Improve external contributor experience**
   - Create "good first issue" labels and onboarding guide
   - Set up office hours or async Q&A for new contributors
   - Document common PR pitfalls and how to avoid them

5. **Issue tracking audit**
   - Verify users know how to report issues (documentation, README)
   - Check if issues are being reported elsewhere (mailing lists, Slack, etc.)
   - Consider user survey to understand issue reporting barriers

### Ongoing Monitoring

6. **Track external contribution funnel health**
   - Monitor: External PRs created → Merged → Acceptance rate
   - Goal: Return to 90%+ external acceptance rate by Q3
   - Leading indicator of community health

7. **Download trend analysis**
   - Track weekly download rates to confirm Q2 projections
   - Identify which roles are most affected
   - Correlate with known events (releases, conferences, blog posts)

8. **Issue backlog management**
   - Track open issue count over time
   - Categorize issues by priority and effort
   - Set quarterly goals for issue resolution

---

## Data Notes

- **Partial Quarter**: This analysis covers approximately 55% of Q2 2026 (50 days of 91-day quarter)
- **Projections**: Full-quarter projections assume current pace continues through June 30
- **Galaxy Legacy**: Cumulative downloads; quarterly gains calculated from quarter-over-quarter deltas
- **Galaxy Collections**: Quarterly download counts for fedora.linux_system_roles and microsoft.sql
- **Per-Role Growth**: Cannot calculate Q2 role-level growth without Q1 baseline per-role data
- **Merge/Acceptance Rates**: Exclude PRs/issues still open from denominator to avoid penalizing in-flight work

---

## Appendix: Metric Calculation Formulas

- **PR Merge Rate** = (PRs Merged) / (PRs Created - PRs Open) × 100
- **External Acceptance Rate** = (External PRs Merged) / (External PRs Created - External PRs Open) × 100
- **External Contribution %** = (External PRs Created) / (PRs Created) × 100
- **Issue Resolution Rate** = (Issues Closed) / (Issues Created) × 100
- **QoQ Growth** = ((Current Quarter - Previous Quarter) / Previous Quarter) × 100
- **Projected Full Quarter** = (Partial Quarter Value) / (Fraction of Quarter Elapsed)

---

**Report Generated:** May 20, 2026  
**Next Update:** End of Q2 2026 (after June 30)
