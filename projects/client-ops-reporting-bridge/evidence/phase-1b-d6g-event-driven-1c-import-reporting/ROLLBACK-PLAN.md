# ROLLBACK-PLAN

Do **not** execute on success. Exact rollback targets:

## OpenCart / SITE-002

1. Remove/disable admin route files for `tool/mars_1c_exchange`
2. Revert `column_left` menu entry «Обмен с 1С»
3. Remove permission keys from user groups (or leave inert)
4. Restore prior `mars_1c_import_wrapper.php` from pre-D6G backup under deployment folder
5. Remove `mars_1c_import_run_contract.php` if rolling fully
6. Refresh `/storage/modification/` per SITE-002 practice

## Windows tasks

1. Restore `MARS_SITE_002_Client_Ops_Producer` action to prior producer scheduled script (if needed)
2. Disable/delete `MARS_SITE_002_Import_Completion_Poller`
3. Leave monitor task as-is unless prestate differs

## Runtime checkouts

- Reset producer/monitor checkouts to pre-D6G commit (`c59f8297` baseline) **only** under explicit rollback charter

## Preserve always

- Real import logs
- Delivered Telegram message history
- Data Table rows
- Terminal run evidence under `runs/` and local terminal cache
- Existing 1C XML exchange files

## Gate

`D6G_ROLLBACK_PLAN_READY` — PASS (documented; not executed)
