# SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01

**Issued:** 2026-07-09  
**Parent checkpoint:** [SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md](SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md)  
**Operation:** `SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`  
**OCPilot run:** 4.239  
**Environment:** https://bzpm.ru/ (Production)

## Wrapper change

| Remote path | Version | Change |
|-------------|---------|--------|
| `/storage/mars-tools/cron/mars_1c_import_wrapper.php` | **1.1.1** | TXT total `Duration` uses actual run wall start (`$started`) passed into `mars_report_begin()` |

## Root cause (fixed)

`mars_mode_run()` called `mars_report_begin()` after import completed, so TXT `Duration` measured report-write latency (~0s) instead of full run wall time.

## Unchanged

- Import sequence (`1c` → `1c_offers`)
- Sergey legacy controllers
- Beget cron schedule `0 8 * * *` Moscow
- HTTP gateway
- DB/product/category/stock/price writes
- Public site code

## Confirmation pending

Next scheduled 1C import must produce TXT report with **nonzero** `Duration` matching LOG wall time.

## Rollback

Re-upload pre-patch wrapper SHA `e991afb2b0202f622c7e6f1cbd627826f4cdef79fedc45b9e3054d337ae28b62` from Storage deployment `server-source-before/`.

## Report

[sites/site-002/reports/SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md](../reports/SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md)
