# FP-0002 V9-06D7D Service Layout Variant Rules v1

**Date:** 2026-07-05

## Theme variants

- `subdivision` → `subdivision-stack.php`
- `leaf` → `leaf-stack.php`
- `alcohol-special` → `alcohol-stack.php`

## ACF mapping

| ACF value | Theme variant |
|-----------|---------------|
| subdivision | subdivision |
| standard | leaf |
| extended | leaf |
| alcohol_special | alcohol-special |
| placeholder | leaf |

## Hierarchy fallback (no DB writes)

1. Read `service_layout_variant` when ACF active.  
2. If empty: slug `lechenie-alkogolnoy-zavisimosti` → alcohol-special.  
3. If empty: published child services exist → subdivision.  
4. Else → leaf.

## Seeded routes

| Service | URL | Expected variant | Detection rule | Result |
|---------|-----|------------------|----------------|--------|
| 73 | /uslugi/zavisimosti/ | subdivision | ACF or children | PASS |
| 74 | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | alcohol-special | ACF or slug | PASS |
| 77 | /uslugi/psihicheskoe-zdorovie/ | subdivision | ACF or children | PASS |
| 84 | /uslugi/rasstroystva-pischevogo-povedeniya/ | subdivision | ACF or children | PASS |

Evidence: `validation/v9-06d7d-service-template-source/service-layout-variant-map.json`

## Result

COMPLETE
