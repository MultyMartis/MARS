# WORKSTREAM-A-LOCK

**Token:** D6B2_WORKSTREAM_A_BASELINE_LOCKED

Pre-apply production Workstream A baseline preserved:

| Item | Expected / Observed |
|------|---------------------|
| Workflow versionId | dc8746bf-df9c-425d-9b3f-4ace452ac5ef |
| Nodes | 20 (incl. Classify Telegram Delivery Outcome, Delivery Ledger Finalize Update) |
| delivery_state model | PENDING / SENT / FAILED |
| MAX_RETRIES | 0 |
| MAX_SAFE_CONCURRENCY | 1 |
| HTTP 202 meaning | unchanged |
| Duplicate suppression | unchanged (D6A2 proven) |

D6B2 did **not** alter Telegram outcome classifier, finalizer, or ledger semantics.
