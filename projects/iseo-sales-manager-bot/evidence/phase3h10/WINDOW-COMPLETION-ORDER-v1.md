# WINDOW COMPLETION ORDER — Phase 3H.10

Failing 10:00/10:15 windows:

- `last_window` / success markers **not** set as sent for those business dates (error before completion)
- Observability may record ERROR_SHEETS_429_ACCESS class stamps where Stamp Sheets Error ran
- 10:30 success wrote `SKIPPED_OUTSIDE_WINDOW` only

Repair preserves: do not mark window complete before valid delivery semantics for SHOULD_SEND.
