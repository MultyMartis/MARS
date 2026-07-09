# FP-0002 V9-06E26A DB Checkpoint v1

## Result

PASS — fresh full DB dump created before E26A source/runtime/data changes.

## Checkpoint

| Item | Value |
|------|-------|
| Wave | V9-06E26A |
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e26a-about-page-wordpress-acf-port-pre-20260709-115450` |
| Dump | `mars_wp_fp0002.sql` |
| DB | `mars_wp_fp0002` |
| Prefix | `fp02_` |
| E26 baseline | `83a5cce667147d0963bbd63face431dc05f0cd44` |

## Snapshots

- `page-11-snapshot.json` — page `/o-centre/` pre-change postmeta
- `preservation-snapshot.json` — hero CTA, reusable block options, reviews options

## Restore

```bash
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e26a-about-page-wordpress-acf-port-pre-20260709-115450\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e26a-about-page-wordpress-acf-port/db-checkpoint.json`
