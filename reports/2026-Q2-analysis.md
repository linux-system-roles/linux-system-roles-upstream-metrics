# Linux System Roles - 2026-Q2 Quarterly Metrics Analysis

**Report Date:** May 20, 2026  
**Status:** ⚠️ Partial quarter data (~55% complete through May 20)

---

## Executive Summary

Q2 2026 demonstrates strong PR efficiency (94.4% merge rate, up from 92.5%) and healthy PR volume growth (projecting +33% QoQ), but faces two critical challenges: Galaxy downloads declining sharply across both legacy roles (-40% projected) and collections (-62% projected), and external PR acceptance dropped 16.6 percentage points to 78.6%.

---

## Key Metrics

| Metric | Q2 2026 (Partial) | Q2 Projected | Q1 2026 | Change |
|--------|-------------------|--------------|---------|--------|
| **PRs Created** | 128 | ~233 | 175 | +33% ✓ |
| **PRs Merged** | 118 | ~215 | 161 | +33% ✓ |
| **PR Merge Rate** | 94.4% | ~94% | 92.5% | +1.9pp ✓ |
| **External PRs Created** | 16 | ~29 | 22 | +32% ✓ |
| **External Acceptance** | 78.6% | ~78% | 95.2% | **-16.6pp** ⚠️ |
| **External % of Total** | 12.5% | ~12.5% | 12.6% | -0.1pp |
| **Issues Created** | 7 | ~13 | 14 | -7% |
| **Issues Closed** | 2 | ~4 | 3 | +33% ✓ |
| **Issue Resolution Rate** | 28.6% | ~31% | 21.4% | +7.2pp ✓ |
| **Galaxy Legacy Downloads** | 87K | ~158K | 266K | **-40%** ⚠️ |
| **Galaxy Collections** | 82K | ~149K | 389K | **-62%** ⚠️ |

---

## Highlights

- **PR volume trending up strongly**: Projecting 233 PRs for full quarter, a 33% increase over Q1's 175 PRs—on track for highest quarterly PR count in recent history
- **Excellent merge efficiency**: 94.4% merge rate shows team is processing contributions effectively, up from 92.5% in Q1
- **Issue resolution improving**: Resolution rate increased to 28.6% from 21.4% in Q1, showing better responsiveness to user-reported issues
- **Strong external engagement**: External PRs account for 12.5% of all PRs, and 100% of issues are externally reported, demonstrating active community participation

---

## Top Downloaded Roles

Based on cumulative downloads as of May 20, 2026:

1. **timesync**: 920,898 downloads
2. **sshd**: 650,985 downloads
3. **network**: 346,387 downloads
4. **cockpit**: 210,674 downloads
5. **journald**: 188,266 downloads

*Note: Cannot calculate fastest growing/declining roles for Q2 without Q1 per-role baseline data.*

---

## Top Concerns

1. **Galaxy downloads collapsing across both platforms**: Legacy roles tracking for -40% QoQ decline (266K → ~158K projected) with daily download rate dropping from 2,956/day to 1,743/day. Collections facing even steeper -62% decline (389K → ~149K projected). This is too significant to be a data artifact—requires immediate investigation into potential causes: Ansible Galaxy API changes, distribution packaging updates, emerging competitor tools, or user migration patterns.

2. **External PR acceptance rate dropped significantly**: Only 78.6% of external PRs merged (excluding those still under review) compared to 95.2% in Q1, a 16.6 percentage point decline. Five external PRs were created but not merged, suggesting either declining PR quality, unclear contribution guidelines, or stricter review standards. This could discourage future community contributions.

3. **Low issue creation rate**: Only 7 issues created (projecting ~13 for full quarter vs 14 in Q1). While not an immediate crisis, this could indicate users aren't reporting problems, have found alternative channels, or are moving away from the project. Worth investigating whether issue reporting barriers exist.

4. **External contribution funnel at risk**: Combined effect of lower external PR acceptance (78.6%) and low issue reporting creates risk to community health. Need to ensure external contributors feel supported and valued.

---

## Recommendations

1. **Immediate (next 2 weeks)**: Launch investigation into Galaxy download decline root cause:
   - Check Ansible Galaxy service status, API changes, or policy updates
   - Review distribution packaging for Fedora/RHEL—any changes to role delivery methods?
   - Analyze download patterns by role to identify if specific roles are affected
   - Contact major known users to understand consumption pattern changes
   - Check competitor landscape for new alternative role sources

2. **Short-term (by end of Q2)**: Improve external contributor experience to reverse acceptance rate decline:
   - Review the 5 unmerged external PRs to identify common patterns (test failures, style issues, unclear requirements)
   - Update CONTRIBUTING.md with specific examples, requirements, and common pitfalls
   - Consider adding PR template with pre-submission checklist
   - Set up weekly download monitoring dashboard with alert thresholds

3. **Ongoing**: Monitor and strengthen community health metrics:
   - Track external contribution funnel: PRs created → merged → acceptance rate (target: return to >90%)
   - Monitor download trends by individual role to identify which are most affected
   - Reach out to users to understand issue reporting patterns and barriers
   - Set quarterly goal for issue resolution rate (target: >50% by Q3)

4. **Follow-up**: Based on Galaxy investigation findings, develop recovery strategy:
   - If technical issues: work with Ansible Galaxy team to resolve
   - If distribution changes: collaborate with distros to improve discoverability
   - If user migration: understand why and adapt project direction
   - If competitor emergence: assess feature gaps and competitive positioning

---

**📄 Report saved to:** `reports/2026-Q2-analysis.md`
