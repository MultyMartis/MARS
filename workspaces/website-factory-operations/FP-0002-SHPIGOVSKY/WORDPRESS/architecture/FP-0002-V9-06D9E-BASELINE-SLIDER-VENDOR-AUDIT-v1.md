# FP-0002 V9-06D9E Baseline Slider Vendor Audit v1

**Date:** 2026-07-05  
**Task:** V9-06D9-E Home Slider / Vendor / Pagination Visual Parity Repair

## Summary

Baseline audit compared static V9 `dist/` and `src/` against WP runtime before repair.

## Critical findings

| Component | Issue | Root cause |
|-----------|-------|------------|
| **specialists** | Wrong heading «Комфорт, приватность, забота»; duplicate `comfort-heading` id | WRONG_DOM_CLASSES (D9-D transplant) |
| **home-gallery / reviews / specialists dots** | Default Swiper blue/gray bullets instead of bordered V9 dots | MISSING_VENDOR_CSS_ORDER — swiper CSS loaded after `v9-style.css` |
| **comfort / videos** | Fancybox markup OK | NONE |

## Static authority

- DOM: `src/partials/sections/{specialists,home-gallery,reviews}.html`
- Init: `src/js/main.js` (`initSpecialists`, `initHomeGallery`, `initReviews`)
- Pagination CSS: `src/scss/style.scss` → compiled in `v9-style.css`

## Evidence

`validation/v9-06d9e-home-slider-vendor-pagination-repair/baseline-slider-vendor-audit.json`
