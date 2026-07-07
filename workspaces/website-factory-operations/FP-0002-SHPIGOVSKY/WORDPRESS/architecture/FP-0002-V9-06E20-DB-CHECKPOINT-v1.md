# FP-0002 V9-06E20 DB Checkpoint

**Wave:** V9-06E20 Remove Reviews Alias From Site Settings  
**Date:** 2026-07-08  
**Result:** PASS

## Checkpoint

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e20-remove-reviews-alias-from-site-settings-pre-20260708-022042` |
| Dump | `mars_wp_fp0002.sql` |
| SHA256 | `61D475EB22DA8DAE7CD4AA95D9D7747F9ECDC2983CDF081303DD597F1E2C03FB` |
| Size | 2,193,011 bytes |
| Tool | Laragon `mysql-8.4.3-winx64\bin\mysqldump.exe` |

## Snapshots

- `options-reviews-snapshot.json` — fp02-reviews_* and legacy options_reviews_* keys (pre-repair)

## Restore

```bash
mysql --host=127.0.0.1 --user=mli_shpigovsky_app mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e20-remove-reviews-alias-from-site-settings-pre-20260708-022042\mars_wp_fp0002.sql"
```

Metadata only in Git. Dump and backup payload **not** committed.
