# FP-0002 V9-06E27B DB Checkpoint v1

**Wave:** V9-06E27B  
**Baseline:** `2570a9a3cf6ee30858ec586a3a76ec03317f8539`  
**Generated:** 2026-07-09

## Checkpoint summary

| Item | Value |
|---|---|
| Result | PASS |
| Checkpoint path | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e27b-low-risk-obsolete-cleanup-pre-20260709-171947` |
| DB dump | `mars_wp_fp0002.sql` |
| SHA256 | `BD9557230A86D7F77E05387C1466C216C4937E72E42912FF028BA45C181855E5` |
| Size | 2,011,954 bytes |
| Database | `mars_wp_fp0002` |
| Prefix | `fp02_` |

## Snapshots included

- `options.json` — page_on_front, page_for_posts, permalink_structure, privacy policy
- `candidates_before.json` — pages #9, #10, #17, #21, #25
- `protected_pages.json` — pages #3, #4, #6, #7, #8, #19
- `protected_posts.json` — demo post #750
- `protected_services.json` — service #73
- `menu_items.json` + checksum
- `pages.json`, `posts.json`, `services.json`
- `core_routes_before.json`, `candidate_routes_before.json`
- `RESTORE.md`

## Restore

```text
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e27b-low-risk-obsolete-cleanup-pre-20260709-171947\mars_wp_fp0002.sql"
```

Evidence: `validation/v9-06e27b-low-risk-obsolete-cleanup/db-checkpoint.json`
