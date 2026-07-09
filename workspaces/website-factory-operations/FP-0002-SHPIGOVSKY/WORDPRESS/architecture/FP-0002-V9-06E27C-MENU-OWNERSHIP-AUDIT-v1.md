# FP-0002 V9-06E27C — Menu Ownership Audit

**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/menu-ownership-audit.json`

## Menus scanned

- Primary (`primary`)
- Footer
- Legal

## Conflict item

| Menu | Item ID | Label | Linked object | URL path | Route owner | Mismatch | Recommendation |
|---|---:|---|---|---|---|---|---|
| Primary | 301 | Зависимости | page `#6` | `/uslugi/zavisimosti/` | service `#73` | **YES** | `RECOMMENDED_MENU_RETARGET_LATER` → service `#73` |

## Non-conflict notes

- Pages `#7` and `#8` have **no** nav menu references.
- Footer service links in theme (`navigation.php`) use hardcoded URLs to `/uslugi/zavisimosti/` etc. — these resolve to service CPT at runtime and do not depend on page objects.

## E27D menu action (planned, not executed)

1. Update menu item `#301` `_menu_item_object_id` from `6` to `73`.
2. Update `_menu_item_object` from `page` to `service`.
3. Validate Primary menu after retarget before trashing page `#6`.
