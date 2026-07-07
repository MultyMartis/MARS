# FP-0002 V9-06E18 — DB Checkpoint

**Wave:** V9-06E18  
**Date:** 2026-07-08

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e18-reusable-blocks-batch-1-fields-pre-20260708-001410` |
| DB dump | `mars_wp_fp0002.sql` (1,570,586 bytes) |
| SHA256 | `4CDF0695B845E8B93BD4B1DC7AC0B15345DA83A7CB02BBB9E9E4B6D07BE10A43` |
| Snapshots | `db-snapshots/options-acf-snapshot.txt`, `options-count.txt` |

## Restore

```text
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e18-reusable-blocks-batch-1-fields-pre-20260708-001410\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e18-reusable-blocks-batch-1-fields/db-checkpoint.json`
