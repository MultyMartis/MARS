# FP-0002 V9-06E17 — DB Checkpoint

**Wave:** V9-06E17  
**Date:** 2026-07-07

## Checkpoint

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e17-site-settings-ia-skeleton-pre-20260707-235348` |
| DB dump | `mars_wp_fp0002.sql` (2,115,304 bytes) |
| SHA256 | `29030308DE6CE1F2A5C694AB2B1C4B6332837603EAA90CD2015903CC7C31D7A0` |
| Snapshots | `db-snapshots/options-acf-snapshot.txt`, `options-count.txt` |

## Restore

```text
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e17-site-settings-ia-skeleton-pre-20260707-235348\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e17-site-settings-ia-skeleton/db-checkpoint.json`
