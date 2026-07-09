# FP-0002 V9-06E27D DB Checkpoint

**Task:** V9-06E27D Page Service Ownership Implementation  
**Date:** 2026-07-09  
**Result:** PASS

## Checkpoint

| Item | Value |
|---|---|
| Path | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e27d-page-service-ownership-implementation-pre-20260709-183427` |
| Dump | `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e27d-page-service-ownership-implementation-pre-20260709-183427/mars_wp_fp0002.sql` |
| SHA256 | `EF99EA958B38290777E27AFDCDD1958FB823492E6494A2241FBE0001E3C66D13` |
| Size | 2012709 bytes |
| DB | `mars_wp_fp0002` |
| Prefix | `fp02_` |

## Pre-operation snapshots

- Menu item `#301` (post row + meta + Primary menu term)
- Legacy shadow pages `#6`, `#7`, `#8`
- Protected pages `#3`, `#4`, `#19`
- Service CPT `#73`, `#77`, `#84`, `#74` + child tree
- Demo post `#750`
- Primary / Footer / Legal menus
- Options: page_on_front, page_for_posts, permalink_structure, blog_public, privacy_policy_page
- Accepted route HTTP probes (12 routes)

## Restore

```
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e27d-page-service-ownership-implementation-pre-20260709-183427\mars_wp_fp0002.sql"
```

Partial rollback: restore menu `#301` meta from `menu_item_301.json`; restore pages from Trash.
