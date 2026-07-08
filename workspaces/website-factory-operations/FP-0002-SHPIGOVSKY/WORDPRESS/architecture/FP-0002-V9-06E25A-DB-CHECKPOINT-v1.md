# FP-0002 V9-06E25A — DB Checkpoint

**Wave:** V9-06E25A Service Duplicate Action Visibility Repair  
**Generated:** 2026-07-09

## Purpose

Lightweight safety checkpoint before admin UI visibility corrections. Duplicate handler can create drafts on click; checkpoint enables rollback without touching E25 test artifact **746**.

## Checkpoint

| Item | Value |
|---|---|
| Path | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e25a-service-duplicate-action-visibility-repair-pre-20260708T181800Z` |
| Dump | `mars_wp_fp0002.sql` |
| SHA256 | `28050E4EF55A07D6BE562B6FAE46CC1DC8FE9051BC354D90B0DE9C4ACF587277` |
| Size | 2,071,993 bytes |
| Services | 19 (includes draft duplicate 746) |

## Snapshots in checkpoint folder

- `service-posts-snapshot.json`
- `draft-duplicate-746-snapshot.json`
- `e24-hero-cta-postmeta-snapshot.json`
- `global-hero-options-snapshot.json`
- `restore-instructions.txt`

## Restore

```bash
mysql -h127.0.0.1 -uroot mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e25a-service-duplicate-action-visibility-repair-pre-20260708T181800Z\mars_wp_fp0002.sql"
```

## Evidence

`validation/v9-06e25a-service-duplicate-action-visibility-repair/db-checkpoint.json`

**Result:** PASS
