# FP-0002 V9-06E27D Exact Implementation Plan

**Date:** 2026-07-09  
**Method:** `custom_url_binding`  
**Reason:** URL unchanged; service CPT #73 already owns runtime route; avoids CPT nav object binding risk

## Step A — Menu retarget

| Field | Value |
|---|---|
| Menu item | `#301` |
| Method | `custom_url_binding` |
| Meta | `_menu_item_type=custom`, `_menu_item_object=custom`, `_menu_item_object_id=0`, `_menu_item_url=/uslugi/zavisimosti/` |
| Preserve | label, order, parent, menu assignment |

## Step B — Trash shadow pages

| Page ID | Action |
|---:|---|
| 6 | `wp_trash_post(6)` |
| 7 | `wp_trash_post(7)` |
| 8 | `wp_trash_post(8)` |

No redirects. No permalink changes. No rewrite flush.
