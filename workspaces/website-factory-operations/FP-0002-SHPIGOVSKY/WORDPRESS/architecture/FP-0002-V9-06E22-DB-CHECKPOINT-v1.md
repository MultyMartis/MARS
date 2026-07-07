# FP-0002 V9-06E22 DB Checkpoint

**Wave:** V9-06E22 Remove Global Heroes Settings  
**Date:** 2026-07-08

## Checkpoint

| Item | Value |
|------|-------|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e22-remove-global-heroes-settings-pre-20260708-034456` |
| Dump | `mars_wp_fp0002.sql` |
| SHA256 | `5FBB2EB8BD98C769945CA564EE84F9D3506DDC46D8E0FACA6DB1DD0EBD815506` |
| Size | 1,776,030 bytes |
| DB | `mars_wp_fp0002` |
| Prefix | `fp02_` |

## Snapshots (checkpoint folder)

- `options-batch2-snapshot.json`
- `options-global-hero-snapshot.json`
- `options-reviews-preservation-snapshot.json`
- `local-hero-meta-snapshot.json`
- `local-hero-groups-snapshot.json`

## Restore

```bash
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e22-remove-global-heroes-settings-pre-20260708-034456\mars_wp_fp0002.sql"
```

Committed metadata: `validation/v9-06e22-remove-global-heroes-settings/db-checkpoint.json`
