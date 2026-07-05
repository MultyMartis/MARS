# FP-0002 V9-06D9E Home Slider / Vendor / Pagination Repair Report v1

**Date:** 2026-07-05  
**Commit base:** `57c0008fe5d756474d45e7636dbd83fa2a703ad6` (D9-D)  
**Verdict:** PASS

## Executive summary

D9-E repaired Home slider visual parity without touching D9-D Home main transplant, DB, or ACF. Two theme source files changed:

1. **Specialists heading** — D9-D accidentally transplanted comfort heading into `specialists.php`
2. **Vendor CSS order** — Swiper CSS loaded after `v9-style.css`, overriding custom pagination bullet styles

Bounded runtime delivery: 2 files. Route smoke ALL_200.

## Root causes

| Finding | Classification |
|---------|----------------|
| Wrong specialists heading/id | WRONG_DOM_CLASSES |
| Unstyled/default Swiper dots | MISSING_VENDOR_CSS_ORDER (effective PAGINATION_CSS_MISSING) |
| Swiper JS/init | Already correct in `v9-shell.js` |

## Changed source files

- `theme/shpigovsky/template-parts/home/specialists.php`
- `theme/shpigovsky/inc/home-vendors.php`

## Evidence pack

`validation/v9-06d9e-home-slider-vendor-pagination-repair/`

## Known remaining gap (out of scope)

- `template-parts/home/faq.php` still has comfort heading transplant typo — not slider-related; note for D9-F QA

## Next step

`CREATE_V9_06D9F_VISUAL_PARITY_QA_TASK`
