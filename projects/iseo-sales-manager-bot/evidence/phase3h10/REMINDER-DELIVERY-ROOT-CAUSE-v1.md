# REMINDER DELIVERY ROOT CAUSE — Phase 3H.10

## Primary

**WAIT_RETRY_DATETIME_INVALID** — `Wait Reminder Sheets Retry` used `resume: afterTimeInterval` with an expression amount that n8n rejected at runtime, so ACCESS **429** retries never resumed.

## Secondary

1. **SHEETS_429** on `Read ACCESS_CONTROL for Reminder` (triggering the broken Wait)
2. **TELEGRAM_SEND_PATH_NOT_REACHED** (claims/Telegram never entered)
3. **CONFIG_RECIPIENT_CACHE_DRIFT** (CONFIG count `4` vs live ACCESS `3` after intentional MOD_A disable) — observability only; not the send blocker

## Not root cause (these windows)

- `invalid_grant` — not observed on Aug 18–20 reminder slots (Sheets auth HEALTHY for CONFIG/CLEAN)
- Schedule missing — triggers ran
- Zero pending skip — pending not evaluated; path died earlier
- MOD_A disable — intentional; must not be restored

## Exact first failing stage

`Wait Reminder Sheets Retry` after ACCESS 429 classification.
