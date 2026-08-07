# Watchdog Forensic

## Why no NO_FRESH Telegram arrived on 2026-08-07

1. Windows task `MARS_SITE_002_Client_Ops_Producer` did fire at **2026-08-07T13:28:28+07:00**.
2. Local Node watchdog inspected `import-terminals/_current/run-state.json`.
3. That mirror still held **yesterday’s** completed run `mars-20260806-160514-5d2cdb3b` with `final_status` set.
4. Pre-fix logic treated any `_current.final_status` as `TERMINAL_EXISTS` **without checking reporting date** → `WATCHDOG_FALSE_SKIP`.
5. Separately, even a correct watchdog would not replace the missing success/attention report for the real scheduled run that had already completed at 08:00 Moscow; that required completion dispatch.

## Root cause labels

- Primary watchdog: `WATCHDOG_FALSE_SKIP`
- Contributing task result noise: `WATCHDOG_FAILED` possible on earlier LastTaskResult `0x800710E0` (interactive/session), but reproduced false-skip is definitive for silence of NO_FRESH.

## Fix / architecture

- Server-side watchdog deployed: `/storage/mars-tools/cron/mars_1c_no_import_watchdog.php`
- HTTP gateway: `/public_html/mars-tools/cron/mars_1c_watchdog_http_gateway.php` (token auth)
- Verified 2026-08-07 skip reason after scheduled terminal present: `TERMINAL_EXISTS` for `mars-20260807-080002-5bbdaf1c`
- Windows producer/watchdog task **disabled** (server-side primary)
- Local Node watchdog date check fixed for residual tooling
- Beget panel cron for watchdog gateway still required for fully unattended NO_FRESH (SSH `crontab -l` empty — panel-managed, same as import cron)

## Gates

- `D6G1_WATCHDOG_ROOT_CAUSE_PROVEN`
- `D6G1_WATCHDOG_FUNCTIONAL`
- `D6G1_WATCHDOG_SERVER_SIDE` (preferred) — code + HTTP path proven; panel schedule must remain configured like import cron
