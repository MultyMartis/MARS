# Rollback Plan

1. Watchdog cron: if later created, delete Beget row via panel/API (`row_number` from inventory) — do **not** re-enable Windows producer/poller
2. Kill-switch code: redeploy D6G1 PHP set from `8d6cd285` tools
3. Local config: remove `CLIENT_OPS_DISPATCH_ENABLED` key or leave true; keep webhook secrets
4. Admin twig/model: restore D6G1 versions
5. Post_1C runner: remove ShowWindow block if needed
6. Never re-enable `MARS_SITE_002_Import_Completion_Poller` as normal dependency
7. Never re-enable old producer success/error timer path as normal dependency

Do not execute rollback on success of remaining items; cron absence is operator follow-up not rollback.
