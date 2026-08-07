# Rollback Plan

Do **not** execute on success.

## Rollback targets

1. Restore previous `mars_1c_import_wrapper.php` v1.2.0 from D6G tip `2a688106`.
2. Remove `mars_1c_completion_dispatch.php` / `mars_1c_no_import_watchdog.php` / watchdog gateway if needed.
3. Restore prior `mars_1c_wrapper.local.php` from operator backup (secrets never in Git).
4. Re-enable Windows completion poller only if explicitly authorized emergency fallback.
5. Re-enable Windows producer watchdog only as emergency fallback.

## Preserve always

- import logs under `/storage/mars-tools/cron/logs/`
- terminal results under `/storage/mars-tools/cron/runs/`
- Data Table history
- delivered Telegram messages
- this forensic evidence pack

## Gate

`D6G1_ROLLBACK_PLAN_READY`
