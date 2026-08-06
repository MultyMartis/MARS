# DEPLOYMENT

## Production FTP deploy (SITE-002)

Operation id: `SITE-002-PROD-D6G-EVENT-DRIVEN-1C-IMPORT-01`

Deployed artifacts:

- `mars_1c_import_wrapper.php` (v1.2.0)
- `mars_1c_import_run_contract.php`
- OpenCart admin `mars_1c_exchange` pack
- `column_left` menu patch

Post-deploy:

- Wrapper PHP string corruption detected (HTTP 500) → repaired and redeployed
- Gateway dry-run/status returned HTTP 200 after repair
- Admin permissions granted to 3 user groups for `tool/mars_1c_exchange`

## Runtime deploy

Producer + monitor checkouts fast-forwarded to canonical D6G commits; schedule wrapper pins track HEAD.

## Cache

OpenCart modification refresh performed per SITE-002 practice (scoped; not broad storage wipe).
