# FP-0002 V9-06E4 Service Subdivision Layout/Image Audit

**Date:** 2026-07-06  
**Route:** `/uslugi/zavisimosti/` (Service #73)

## Hero image

- Template: `template-parts/service/inner-hero.php` — **correct** `services-inner-hero-v2`
- `hero_media` ACF on #73: **empty**
- Theme asset `service-subdivision-hero.webp`: **present** in git + runtime
- Fix: theme default fallback and/or controlled `hero_media` seed in E5

## Layout drift

`subdivision-stack.php` omits static V9 sections:

- `service-subdivision-nature-v1`
- `service-subdivision-team-stats-v1`
- `clinic-landscape`
- `specialists`
- `founder-quote`
- `comfort`
- `reviews`

`stages.php` renders `service-leaf-stages-v1` instead of `service-subdivision-stages-v1`.

## service-subdivision-start-heading

Present via `mid-cta.php` → `program-cta-band-section` id `service-subdivision-start`. Background missing due to **CSS_PATH** (`/assets/...` 404), not missing markup.

Evidence JSON: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/service-subdivision-layout-image-audit.json`
