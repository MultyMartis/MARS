# LIVE-BASELINE-GET-ONLY

**Method:** GET-only n8n + Data Table APIs
**Verdict:** `D6A_LIVE_BASELINE_RECONFIRMED`

| Field | Expected | Observed |
|-------|----------|----------|
| Workflow ID | tkM4H0G0gM3q9Foi | tkM4H0G0gM3q9Foi |
| Name | MARS Client Ops Bridge — bzpm.ru | match |
| active | false | false |
| nodes | 17 | 17 |
| versionId | 3d2fd6fc-bc17-4e0f-b9e5-086c959afd29 | match |
| executions | 32 | 32 |
| running | 0 | 0 |
| Data Table ID | H6VYhwz7RXZCBMmu | match |
| columns | 15 | 15 |
| rows | 3 | 3 |
| event_id | c84e29bf-79b1-5aea-98c4-9dc8d651fc96 | 1 row |
| intake_state | FIRST_SEEN | FIRST_SEEN |
| event_status | ATTENTION | ATTENTION |
| delivery_state | PENDING | PENDING |

**Data Table ops in live workflow:** `Dedupe Lookup` (get), `Dedupe Claim Insert` (insert) — **no** post-Telegram update node.

**Telegram node:** `continueOnFail=false` (pre-D6A live) — offline compose will set continue-on-fail for finalization reachability.

No repair of historical PENDING row.
