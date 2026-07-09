# FP-0002 V9-06E27D Menu Retarget Result

**Date:** 2026-07-09  
**Result:** PASS  
**Method:** `custom_url_binding`

## Menu item #301

| Field | Before | After |
|---|---|---|
| `_menu_item_type` | post_type | custom |
| `_menu_item_object` | page | custom |
| `_menu_item_object_id` | 6 | 0 |
| `_menu_item_url` | (empty) | `/uslugi/zavisimosti/` |
| Label | Зависимости | Зависимости |
| menu_order | 2 | 2 |
| Primary menu count | 6 | 6 |

`wp_get_nav_menu_items('primary')` URL after: `/uslugi/zavisimosti/`
