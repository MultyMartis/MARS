# FP-0002 V9-06D9D Implementation Plan v1

**Date:** 2026-07-05  
**Task:** V9-06D9-D Home Main + Footer Static V9 Transplant

## Decision

Current WordPress Home `<main>` MVP scaffold is **not** visual authority. Rebuild from static V9 `index.html` section order.

## Static authority

| Surface | Path |
|---------|------|
| Home orchestration | `workspaces/fp-0002-shpigovsky-v9/src/pages/index.html` |
| Section partials | `workspaces/fp-0002-shpigovsky-v9/src/partials/sections/` |
| Footer | `workspaces/fp-0002-shpigovsky-v9/src/partials/layout/footer.html` |

## WordPress targets

- `theme/shpigovsky/front-page.php` — full V9 section order
- `theme/shpigovsky/template-parts/home/*.php` — 18 static section partials
- `theme/shpigovsky/template-parts/layout/footer.php` — V9 footer structure
- `theme/shpigovsky/template-parts/navigation/footer-social.php` — static social fallback
- `theme/shpigovsky/template-parts/components/scroll-to-top.php` — V9 control
- `theme/shpigovsky/inc/home-vendors.php` — Swiper/Fancybox/Inputmask on front page
- `theme/shpigovsky/assets/img/**`, `assets/svg/**`, `assets/video/**`, `assets/vendor/**`

## Constraints

- No DB writes
- No ACF JSON changes
- No menu mutation
- Bounded runtime copy only

## Result

Implementation plan executed. Evidence: `validation/v9-06d9d-home-main-footer-static-v9-transplant/implementation-plan.json`
