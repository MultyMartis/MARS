# HISTORICAL-ROW-RECONCILIATION-DECISION

**Token:** `D6A2_HISTORICAL_ROW_RECONCILIATION_DEFERRED`

## Historical event (untouched)

| Field | Value |
|-------|-------|
| event_id | `c84e29bf-79b1-5aea-98c4-9dc8d651fc96` |
| intake_state | FIRST_SEEN |
| event_status | ATTENTION |
| delivery_state | **PENDING** (still) |
| Historical Telegram | message_id `7` (D5R2A) |
| D6A2 mutations on this row | **0** |

## Why deferred

Row is evidence of **pre-D6A** architecture (Telegram succeeded; ledger finalizer did not yet exist). Retroactive PENDING→SENT requires separate reconciliation authority based on execution `3416` / message_id `7`.

Do **not** mix with D6B.

**Also acceptable alternate label:** `D6A2_HISTORICAL_ROW_RECONCILIATION_SEPARATELY_RECOMMENDED` — deferred here to keep D6A2 scope clean; a dedicated reconciliation charter may be opened after D6A2 evidence commit.
