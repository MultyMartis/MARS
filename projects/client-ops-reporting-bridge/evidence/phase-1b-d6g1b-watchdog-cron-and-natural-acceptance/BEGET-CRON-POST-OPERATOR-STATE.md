# Beget Cron Post-Operator State

## Evidence strength order used

1. Beget API `cron/getList` — **AUTH still failing** (`status=error`, `answer=null`). Stored password contour remains invalid for API auth.
2. Server-side scheduled import execution — **authoritative for import cron**.
3. Operator Beget panel confirmation (screenshot/charter) — **authoritative for watchdog task creation/enablement** while API is unavailable.
4. Watchdog stdout/state — **not yet present** (no natural 09:00 execution artifact found at capture).

## Import task

- Name: `SITE-002 MARS 1C Import Wrapper`
- Schedule: `0 8 * * *` (Europe/Moscow wall-clock)
- Enabled: YES (operator panel + continuous natural runs 2026-08-08..2026-08-12 @ 08:00+03)
- Proof: terminals + reports + `beget_cron_stdout.log` mtime Aug 12 08:00 + n8n webhook executions

## Watchdog task

- Name: `SITE-002 MARS 1C No-Import Watchdog`
- Schedule: `0 9 * * *` (Europe/Moscow)
- Enabled: YES (operator panel ON)
- Cursor/API create in D6G1A: failed (`AUTH_ERROR`); operator created manually
- Duplicate automation leftovers: none observed in server artifacts; API inventory unavailable
- Natural execution artifact `beget_watchdog_stdout.log`: **absent** at capture → awaiting first natural 09:00 boundary after enablement, or log path not yet written

## Conclusion

- `D6G1B_BEGET_IMPORT_CRON_CONFIRMED`
- `D6G1B_BEGET_WATCHDOG_CRON_CONFIRMED` (panel/operator authoritative; API not usable)
- `D6G1B_NO_DUPLICATE_WATCHDOG_CRON` (no duplicate watchdog artifacts; panel shows one task; API cannot enumerate)
