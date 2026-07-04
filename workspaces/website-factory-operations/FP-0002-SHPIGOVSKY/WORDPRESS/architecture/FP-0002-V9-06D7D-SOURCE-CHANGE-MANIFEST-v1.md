# FP-0002 V9-06D7D Source Change Manifest v1

**Date:** 2026-07-05  
**Theme version:** `0.6.0-d7d-service-templates`

## Added

- `inc/service-helpers.php`
- `template-parts/service/subnav.php`
- `template-parts/service/children.php`
- `template-parts/service/mid-cta.php`
- `template-parts/service/bordered-info.php`

## Updated

- `single-service.php` — variant main class orchestration  
- `functions.php` — require service-helpers, version bump  
- `inc/service-template-loader.php` — ACF/hierarchy variant resolution  
- All service stack + section template-parts (skeleton → V9 markup)  
- `components/internal-page-nav.php`, `components/program-cta-band.php`  

## Preserved

- D7-A global shell/assets  
- D7-B home source  
- D7-C services hub source  

## Not changed

- Plugin source  
- ACF JSON  
- V9 src/dist  
- Runtime  

Evidence: `validation/v9-06d7d-service-template-source/service-source-change-manifest.json`

## Result

COMPLETE
