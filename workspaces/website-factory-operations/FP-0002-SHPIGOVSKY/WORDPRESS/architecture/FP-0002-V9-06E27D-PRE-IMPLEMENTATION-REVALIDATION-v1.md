# FP-0002 V9-06E27D Pre-Implementation Revalidation

**Date:** 2026-07-09  
**Result:** PASS

## Menu item #301

- Exists: YES (`nav_menu_item`, Primary menu)
- Label: `Зависимости`
- Linked object: page `#6` (pre-state)
- URL resolves to `/uslugi/zavisimosti/`
- No duplicate Primary item for service `#73`

## Legacy shadow pages

| ID | Title | Status | Menu ref | Result |
|---:|---|---|---|---|
| 6 | Зависимости | publish | #301 only | PASS |
| 7 | Психическое здоровье | publish | none | PASS |
| 8 | Расстройства пищевого поведения | publish | none | PASS |

None bound to front/posts/privacy options.

## Service CPT

| ID | Route | HTTP | Result |
|---:|---|---:|---|
| 73 | `/uslugi/zavisimosti/` | 200 | PASS |
| 77 | `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS |
| 84 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS |
| 74 | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | PASS |
