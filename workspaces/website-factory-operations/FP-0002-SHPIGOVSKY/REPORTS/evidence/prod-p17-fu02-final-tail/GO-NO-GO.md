# GO / NO-GO — P17-FU02

## INTERNAL PRE-CUTOVER READINESS = GO

All remaining WordPress/MARS internal tails closed or exactly planned. No discovery left for launch except operator NS and P18 execution of existing plans.

## MANUAL NS CUTOVER = OPERATOR ACTION REQUIRED

NS switch is intentionally not performed.

| Gate | State |
|------|-------|
| Current zone inventoried (NS01) | PASS |
| Target Beget zone in panel (NS02) | OPERATOR (manual, before switch) |
| Mail DNS plan (NS03–NS11) | PLAN READY |
| Target NS published set (NS12) | RECORDED; panel confirm at switch |
| Registrar access (NS13) | OPERATOR |
| Rollback NS recorded (NS14) | PASS (`ns1/ns2.hosting.reg.ru`) |
| Content freeze (NS15) | RUNBOOK READY; not active until launch |
| Fresh full backup after freeze (NS16) | PROCESS READY; **not** this wave |
| mars-runtime resolved | PASS (removed) |
| Webroot hygiene | PASS |
| Users/admin | PASS |
| Legacy redirects 7/7 | PASS |
| DB/file cutover plans | PASS (executable without discovery) |
| Forms/SMTP sequenced | PASS (not configured) |
| Indexing closed | PASS (intentional) |

**NS cutover decision: WAITING FOR OPERATOR** after freeze + fresh backup + Beget zone prep.
