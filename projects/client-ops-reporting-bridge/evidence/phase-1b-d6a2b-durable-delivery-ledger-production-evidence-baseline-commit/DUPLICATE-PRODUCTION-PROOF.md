# Duplicate Production Proof

**Token:** `D6A2_DUPLICATE_SUPPRESSION_PRESERVED`

One intentional replay of synthetic event `d6a2a001-27d6-4a2e-bd6a-000000000001` during D6A2:

| Field | Value |
|-------|-------|
| HTTP | `200` |
| Result | `DUPLICATE_SUPPRESSED` |
| Telegram runs | `0` |
| delivery_state | remains `SENT` |
| Second Telegram message | none |

Workflow executions therefore: **32 → 34**. D6A2B must not generate execution 35.
