# FP-0002 V9-06D7C Source Change Manifest v1

**Date:** 2026-07-05  
**Theme version:** `0.5.0-d7c-services-hub`

## Changed PHP (10)

- `theme/shpigovsky/functions.php` — version bump; require services-hub-helpers
- `theme/shpigovsky/inc/services-hub-helpers.php` — **new** read-only ACF/CPT helpers
- `theme/shpigovsky/page-templates/services-hub.php` — V9 orchestration
- `theme/shpigovsky/template-parts/services-hub/*.php` — 6 sections
- `theme/shpigovsky/template-parts/components/service-card.php` — **new** reusable card

## Unchanged by design

- Plugin source  
- ACF JSON  
- V9 src/dist  
- D7-B home template source (except shared final-form component)  
- Runtime  

Evidence: `validation/v9-06d7c-services-hub-template-source/services-hub-source-change-manifest.json`

## Result

COMPLETE
