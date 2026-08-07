# Server Deployment

Operation: `SITE-002-PROD-D6G1-SERVER-SIDE-COMPLETION-DISPATCH-01`

Uploaded + hash-verified:

- `storage/mars-tools/cron/mars_1c_import_wrapper.php` (v1.3.0)
- `storage/mars-tools/cron/mars_1c_import_run_contract.php`
- `storage/mars-tools/cron/mars_1c_completion_dispatch.php`
- `storage/mars-tools/cron/mars_1c_no_import_watchdog.php`
- `public_html/mars-tools/cron/mars_1c_watchdog_http_gateway.php`
- OpenCart admin model/twig for report UI label

Local config (non-Git) updated with webhook URL + auth secret keys (values not in Git).

## Operator follow-up (Beget panel)

Add/confirm cron (Moscow), same contour as import:

`0 9 * * *` → `https://bzpm.ru/mars-tools/cron/mars_1c_watchdog_http_gateway.php?token=<run_token>`

SSH `crontab -l` is empty on this host (panel-managed), matching the existing import schedule pattern.
