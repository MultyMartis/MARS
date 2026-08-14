# ACCESS 429 FAILURE v1

**Window:** 2026-08-14 10:00 Europe/Moscow  
**Exec:** 30813  
**Class:** `REMINDER_EVALUATION_ABORTED_BY_SHEETS_429`

## Sequence

1. Schedule ran (10:00:39 MSK).
2. Read Reminder CONFIG succeeded.
3. Gate: inside window, proceed=true.
4. Read CLEAN for Reminder succeeded (129 rows `lead_clean_v2`).
5. Read ACCESS_CONTROL for Reminder → HTTP 429 `The service is receiving too many requests from you`.
6. Native `retryOnFail` was on (maxTries=3, wait=30000) but node `executionTime` ~26–29s — full 3×30s sequence did **not** complete.
7. pending_count never computed.
8. decision effectively `ERROR_BEFORE_DECISION`.
9. Telegram attempts=0; claims=0; `last_window` not stamped.

Acceptance lead remained pending. Business date was **not** marked sent.

Prior isolated `QUOTA_COOLDOWN_DONE` did not prove production readiness at the live window.
