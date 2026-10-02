# Linux System Roles — Quarterly Metrics Analysis: 2026-Q3

## Executive Summary

Q3 2026 is a **complete quarter** (Jul–Sep; Galaxy snapshot taken Oct 1, 2026).
The quarter's standout win is external engagement: external contributions rose to
**18.1%** of all PRs (up from 10.9% in Q2), and the team cleared its issue backlog
(23 closed vs 17 created). The main concern is the **PR merge rate dropping to
82.2%** (from 94.8%), driven by 15 PRs still open at quarter close.

## Key Metrics

| Metric | 2026-Q3 | 2026-Q2 | Change |
|---|---|---|---|
| PRs Created | 144 | 175 | −17.7% |
| PRs Merged | 106 | 164 | −35.4% |
| Merge Rate* | 82.2% | 94.8% | −12.6 pp |
| External PRs Created | 26 | 19 | +36.8% |
| External Acceptance* | 77.3% | 77.8% | −0.5 pp |
| External % of PRs | 18.1% | 10.9% | +7.2 pp |
| Issues Created / Closed | 17 / 23 | 10 / 36 | resolution 135% |
| Galaxy Legacy (cumulative) | 3,862,177 | 3,598,214 | +7.3% |
| Galaxy Collections (quarterly delta) | 287,667 | 236,240 | +21.8% |

\*Merge and acceptance rates exclude PRs still under review.

## Highlights

- **External contribution share jumped to 18.1%** of all PRs — the highest in
  recent quarters — with 26 external PRs created (up from 19).
- **Issue backlog reduced**: 23 issues closed against 17 created (135% resolution
  rate); 21 of 23 closures were external issues.
- **Collections growth accelerated**: quarterly new collection downloads up 21.8%
  QoQ, led by fedora.linux_system_roles (+26.7%).

## Top Downloaded Roles (cumulative)

1. **timesync** — 977,711
2. **sshd** — 769,620
3. **network** — 372,703
4. **journald** — 231,413
5. **cockpit** — 224,635

**Fastest growing this quarter:** sshd (+76,457), timesync (+33,816),
journald (+27,237), bootloader (+24,621).

## Top Concerns

- **Merge rate fell to 82.2%** (from 94.8%); 15 PRs remained open at quarter close
  vs just 2 in Q2 — a growing review backlog.
- **microsoft.sql collection downloads fell 49.6%** QoQ (7,702 vs 15,277 quarterly
  new downloads).
- **External PRs rejected** in 4 repos: ansible-sshd (2), systemd (1),
  firewall (1), podman (1) — roughly 23% of external PRs not accepted.
- **PR volume down 17.7%** QoQ (144 vs 175); worth watching if it continues.

## Recommendations

- **Clear the PR review backlog**: triage the 15 open Q3 PRs to recover the merge
  rate.
- **Review the 4 rejected external PRs** for contributor-experience gaps; a brief
  "why closed" note improves retention.
- **Investigate the microsoft.sql download drop** — confirm whether it is a Galaxy
  reporting artifact or a real decline.
- **Sustain external momentum**: 18.1% external share is a high-water mark; keep
  onboarding and contribution docs current.

*Note: infra.leapp appears this quarter at baseline (delta 0 by design on its
first observation); real quarterly growth will show from Q4 onward.*
