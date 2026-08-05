# HARNESS RESULTS v1

Offline/static checks for Phase 3F.2 (sanitized).

| # | Check | Result |
|---|-------|--------|
| 1 | Workflow backups + SHA256SUMS present | PASS |
| 2 | Canonical tip includes 56c3d9ed/031eecb6/28ebb27d | PASS |
| 3 | Callback token OPS=Admin fnvToken | PASS (live) |
| 4 | Token persisted before CLEAN write | PASS (processor patch) |
| 5 | Клиент A business rows = 1 | PASS |
| 6 | Lifecycle reconciled processed + Мопс | PASS (HTTP CLEAN update + event) |
| 7 | Stats epoch CONFIG keys | PASS (HTTP CONFIG rewrite) |
| 8 | Reminders forced false | PASS (CONFIG rewrite) |
| 9 | Reporting workbook created private | PASS |
| 10 | Reporting seed Клиент A once | PASS |
| 11 | `/leads` source = LEADS | PASS (Admin sheet retarget) |
| 12 | Archive tabs created | PASS |
| 13 | Archive full row copy | PARTIAL (quota-limited follow-up) |
| 14 | `/lead_history` full UX | PARTIAL (normalize mention; full pager pending) |
| 15 | Live synthetic TEST_LEADS callback | PENDING OPERATOR |
| 16 | AI OFF / SM-v2 inactive / workflows created=0 | PASS |
| 17–76 | Remaining charter matrix | See acceptance receipt for PARTIAL/PENDING |

**Harness verdict:** CORE LIVE CHECKS PASS; operator visual acceptance + synthetic callback pending.
