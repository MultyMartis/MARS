# FP-0002 V9-06E19 DB Checkpoint v1

**Wave:** V9-06E19  
**Date:** 2026-07-08

## Checkpoint

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e19-reusable-blocks-admin-visibility-repair-pre-20260708-005100` |
| Dump | `mars_wp_fp0002.sql` (copied from E18 pre-repair; post-E18 DB state unchanged) |
| SHA256 | `4CDF0695B845E8B93BD4B1DC7AC0B15345DA83A7CB02BBB9E9E4B6D07BE10A43` |
| DB | `mars_wp_fp0002` |
| Prefix | `fp02_` |

## Note

`mysqldump` unavailable in shell PATH. Pre-repair dump copied from E18 checkpoint because no DB content mutations occurred between E18 delivery and E19 repair start.

## Restore

```bash
mysql --host=127.0.0.1 --user=mli_shpigovsky_app mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e19-reusable-blocks-admin-visibility-repair-pre-20260708-005100\mars_wp_fp0002.sql"
```
