# STATIC-VALIDATION

**Token:** `D6A2_DEPLOYED_LEDGER_STATIC_VALIDATION_PASS`

Post-apply GET validation (workflow inactive):

| Check | Result |
|-------|--------|
| Node count = 20 | PASS |
| Ledger nodes present | PASS |
| Telegram `continueOnFail` | PASS |
| Finalize operation = update | PASS |
| Finalize filters: event_id + delivery_state=PENDING | PASS |
| Finalize writes only delivery_state | PASS |
| Does not write intake_state / event_status | PASS |
| Pattern B: Respond Accepted → Telegram | PASS |
| Non-first-seen bypasses Telegram | PASS |
| Rejected bypasses Telegram | PASS |
| Auth + Telegram credentials unchanged | PASS |
| Retry loops absent | PASS |
| max_retries=0 / concurrency=1 | PASS |

Machine evidence: `STATIC-VALIDATION.json`
