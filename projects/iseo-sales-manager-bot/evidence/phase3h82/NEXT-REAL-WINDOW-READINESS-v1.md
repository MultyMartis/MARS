# NEXT REAL WINDOW READINESS v1

**Next natural window:** **2026-08-15 10:00 Europe/Moscow**  
(business date `2026-08-15`; today 2026-08-14 afternoon MSK)

## PASS requires (do not claim now)

- schedule execution starts automatically
- selected real lead still pending
- critical Sheets reads succeed immediately or within bounded retries
- pending_count >= 1
- recipients=4
- claims=4
- Telegram attempts=4 / successes=4
- duplicates=0
- day marked sent only after successful send semantics

## Evidence hooks (no extra forensic if success is clear)

From the 10:00 (and if needed 10:15) Admin execution:

- schedule execution ID
- pending_count
- Sheets retry counts (`sheets_fail_count` / `pending_reminder_last_retry_attempts`)
- recipient count
- claims / Telegram attempts / successes
- final decision
- `pending_reminder_last_window`

Allowed window: 10:00 inclusive … 10:20 exclusive; 15-minute schedule → 10:00 and 10:15.

Do **not** run production reminder manually.
