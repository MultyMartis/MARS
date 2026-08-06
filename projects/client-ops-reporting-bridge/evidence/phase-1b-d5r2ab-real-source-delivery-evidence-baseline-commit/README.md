# Evidence — Phase 1B-D5R2AB

Offline evidence baseline commit for the first verified SITE-002 real-source Client Ops delivery (D5R2 historical failure + D5R2A temporary-activation success).

## Pack contents

| File | Role |
|------|------|
| `D5R2AB-CHARTER.json` | Phase charter / no-live caps |
| `D5R2AB-DECISION.json` | Final decision / readiness |
| `ACCEPTED-CHANGESET-INVENTORY.md` | Exact A+B allowlist |
| `D5R2-HISTORICAL-FAILURE.md` | HTTP 404 before intake |
| `D5R2A-DELIVERY-FACTS.md` | Temporary activation + FIRST_SEEN facts |
| `HTTP-202-EVIDENCE-PROVENANCE.md` | stdout parse FAILED vs GET-only 202 |
| `N8N-EXECUTION-3416.md` | Execution success facts |
| `DATA-TABLE-POSTSTATE.md` | rows 2→3 / event 0→1 |
| `TELEGRAM-DELIVERY-EVIDENCE.md` | one delivery / message_id 7 |
| `CHARTER-HISTORY.md` | D5 / D5R2 / D5R2A identities |
| `FINAL-CONTAINMENT.md` | Final inactive containment |
| `RUNTIME-RECONFIRMATION.md` | Clean @ `8bb6e8f0` |
| `CLIENT-OPS-LIVE-RECONFIRMATION.md` | GET-only match |
| `CLIENT-OPS-LIVE-RECONFIRMATION.json` | Sanitized GET-only snapshot |
| `SECURITY-REVIEW.md` | Leakage review |
| `TEST-RESULTS.md` | Offline suite results |
| `GIT-SAFETY.md` | Clean worktree / MAIN index / ref advance |

## Key accepted facts

- D5R2: HTTP **404**, intake none, charter **CONSUMED**
- D5R2A: temporary activate → one POST → HTTP **202/FIRST_SEEN** (GET-only authority) → execution **3416** → Data Table **3/1** → Telegram **message_id=7** → deactivate → `active=false`
- Runtime: clean @ `8bb6e8f0f56388c12fdb013cf4cc1b27eb84331c`
- Durable SENT ledger: **DEFERRED**
- Freshness semantics: **FRESHNESS_STATUS_SEMANTICS_REQUIRES_SEPARATE_REPAIR**
