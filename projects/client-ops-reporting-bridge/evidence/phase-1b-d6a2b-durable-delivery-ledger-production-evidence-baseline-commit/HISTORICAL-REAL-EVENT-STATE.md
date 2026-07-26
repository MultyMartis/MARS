# Historical Real Event State

| Field | Value |
|-------|-------|
| event_id | `c84e29bf-79b1-5aea-98c4-9dc8d651fc96` |
| intake_state | `FIRST_SEEN` |
| event_status | `ATTENTION` |
| delivery_state | `PENDING` |
| Historical Telegram (D5R2A) | delivered once; sanitized message_id `7` |
| D6A2 row mutation | **0** |
| D6A2B row mutation | **0** |

**Token:** `D6A2_HISTORICAL_ROW_RECONCILIATION_DEFERRED`

Do not rewrite repository claims as though production row had been reconciled to `SENT`. A future separate charter may use historical execution `3416` + message_id `7` for retroactive reconciliation — **not** part of D6A2B or silently part of D6B.
