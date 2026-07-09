# FP-0002 V9-06E27D Rollback Instructions

**Date:** 2026-07-09

## Step A — Menu item #301

Restore meta from checkpoint `menu_item_301.json`:

- `_menu_item_type` = `post_type`
- `_menu_item_object` = `page`
- `_menu_item_object_id` = `6`
- `_menu_item_url` = `` (empty)

Validate: Primary menu `Зависимости` links to page `#6`.

## Step B — Shadow pages

WP Admin → Pages → Trash → Restore:

- `#6` Зависимости
- `#7` Психическое здоровье
- `#8` Расстройства пищевого поведения

Or: `wp post update <id> --post_status=publish`

## Full DB restore

```
mysql --host=127.0.0.1 --user=root mars_wp_fp0002 < "X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-06e27d-page-service-ownership-implementation-pre-20260709-183427\mars_wp_fp0002.sql"
```

Checkpoint: `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/v9-06e27d-page-service-ownership-implementation-pre-20260709-183427`
