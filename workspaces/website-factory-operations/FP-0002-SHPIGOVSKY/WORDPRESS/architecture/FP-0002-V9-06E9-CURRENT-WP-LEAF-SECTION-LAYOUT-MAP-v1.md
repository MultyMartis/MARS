# FP-0002 V9-06E9 Current WP Leaf Section Layout Map

**Route:** `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`  
**Template:** `alcohol-stack.php` via `single-service.php`

## Before E9

- Template wrapped stack in `<article class="shpigovsky-service shpigovsky-service--alcohol">` (EXTRA_WRAPPER)
- Program used title-only fallback (WRONG_IMAGE)
- Subnav used generic leaf anchors (WRONG_ORDER)
- Reviews/final-form section ids drifted from static V9

## After E9

- Sections render directly under `<main class="page-service-leaf-v1__main ...">`
- Section order matches static V9 (17 sections)
- Program block uses V9 image fallback items with static modifier classes
- Alcohol subnav matches static V9 anchor list
- `id="service-leaf-reviews"` and `id="service-leaf-final-form-heading"` restored

JSON: `validation/v9-06e9-service-leaf-static-v9-layout-parity-repair/current-wp-leaf-section-layout-map.json`
