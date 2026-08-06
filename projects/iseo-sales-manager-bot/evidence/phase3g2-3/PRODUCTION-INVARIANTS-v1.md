# PRODUCTION INVARIANTS v1

**Phase:** 3G.2.3

| Invariant | Status |
|-----------|--------|
| LEADS unchanged by this phase | PASS (no lead writes) |
| LEAD_EVENTS unchanged by this phase | PASS |
| Reporting rows unchanged | PASS |
| Statistics unchanged (unless genuine lead) | PASS |
| Profile rows exactly 4 | PASS |
| AI OFF | PASS |
| Reminders OFF | PASS |
| Sole Gmail intake = Operational.dev | PASS |
| Admin.dev active 85 nodes same ID | PASS |
| Operational.dev active 45 nodes | PASS |
| Sales-Manager-v2 inactive | PASS |
| Workflows created | **0** |
| Customer contact | **0** |
| Access changes | **0** |
| Production leads modified | **0** |
| Real leads lost / duplicated | **0 / 0** |

Patch surface: Admin.dev **Start** node only (+ repo libs/docs/evidence).
