# SENT Production Proof

**Token:** `D6A2_SYNTHETIC_SENT_VERIFIED`
**Customer delivery:** false (synthetic / non-customer)

| Field | Value |
|-------|-------|
| Synthetic event_id | `d6a2a001-27d6-4a2e-bd6a-000000000001` |
| FIRST_SEEN execution | `3417` |
| HTTP | `202 ACCEPTED` |
| Initial delivery_state | `PENDING` |
| Terminal delivery_state | `SENT` |
| intake_state | `FIRST_SEEN` |
| event_status | `OK` |
| Telegram attempts | 1 |
| Telegram deliveries | 1 |
| Sanitized message_id | `8` |
| Real customer delivery | 0 |

HTTP 202 means intake accepted / FIRST_SEEN — **not** by itself terminal delivery completion. Terminal SENT is proven by ledger finalization after Telegram success.
