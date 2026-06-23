# FP-0002 V6 GALLERY REPAIR AND PRE-REVIEWS RECOVERY

**Date:** 2026-06-23  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Branch:** `mars/post-cycle8-live-tests`

## Operator rejection

Rejected commits `f0eadaf` (gallery) and prior false-green report in `FP-0002-V6-SECTION-03-LINKS-AND-GALLERY-REVIEW.md`. Operator-canonical `src/` preserved; operator diff in `home-treatment-prevention.html` + `style.scss` (Section 03 service links calibration) retained.

## Current source protection

Operator changes after `a8039f0`: service icon class `fad fa-external-link-square-alt` (×4), Section 03 panel/service spacing calibration. **Operator values overwritten: 0.**

## Gallery root cause

**`SWIPER_CSS_NOT_CONNECTED`** — `style.scss` `@import '../../node_modules/swiper/swiper-bundle.min.css'` compiled to broken browser URL; vendor file existed in `dist/assets/vendor/swiper/` but was not linked. Without Swiper base CSS, `.swiper-wrapper` lacked `display:flex` and slides stacked vertically.

## Swiper CSS delivery

Fixed: `<link rel="stylesheet" href="assets/vendor/swiper/swiper-bundle.min.css">` in `index.html` `<head>` before project CSS. Removed broken `@import` from `style.scss`. Gulp `vendorSwiper` unchanged. **CDN used: NO.**

## Swiper JS initialization

`window.Swiper` available; `data-gallery-slider` init in `main.js` with `DOMContentLoaded` guard. **Instance count after fix: 1.**

## Corrected gallery boundaries

| Field | v2 value |
|-------|----------|
| Gallery start Y | 3610 |
| Gallery content end Y | 3810 |
| Gallery end Y | 3810 |
| Next section start Y | 3860 |
| Boundary consistency | **PASS** |

Evidence: `reviews/main-content/gallery-audit-v2/`

## Horizontal desktop result

Playwright metrics: `wrapperDisplay: flex`, `slideFlexShrink: 0`, `slideCount: 4`, `instanceCount: 1`. Desktop screenshot: `gallery-repair/FP-0002-V6-GALLERY-REPAIRED-DESKTOP.png`.

## Tablet result

`slidesPerView: 3.15` at 768–1024. Screenshot: `FP-0002-V6-GALLERY-REPAIRED-768.png`, `FP-0002-V6-GALLERY-REPAIRED-1024.png`.

## Mobile result

`slidesPerView: 2.15` at ≤767. Screenshots: `FP-0002-V6-GALLERY-REPAIRED-390.png`, `FP-0002-V6-GALLERY-REPAIRED-320.png`.

## Next-slide peek

YES — fractional `slidesPerView` on tablet/mobile; desktop shows four slides in one row.

## Four Figma assets

Preserved: `shpigovsky-gallery-01..04.webp` — unchanged.

## Gallery interactions

Loop/autoplay/navigation/pagination/lightbox: **DISABLED**. Mouse drag and touch swipe: **ACTIVE** (Swiper `grabCursor: true`).

## Previous incomplete block map

v1 listed only Gallery + Why-us. **REJECTED_INCOMPLETE.**

## Corrected pre-reviews block map

`FP-0002-V6-PRE-REVIEWS-BLOCK-MAP-V2.md` — 5 blocks before Reviews; Reviews start Y **6064**.

## Existing implementations found

`home-gallery.html`, `home-why-us.html`, card system from Section 01. No prior partials for staff/feature-grid/landscape.

## Existing visual system mapping

`.container`, `.home-recovery-intro__card*` (why-us), new blocks reuse `--radius-main`, `--pad-gap`, border tokens. **New visual systems: 0.**

## Blocks recovered

| Block | Partial | Status |
|-------|---------|--------|
| Staff group photo | `home-staff-photo.html` | IMPLEMENTED |
| Centered 6-card grid | `home-feature-grid.html` | IMPLEMENTED |
| Clinic landscape | `home-clinic-landscape.html` | IMPLEMENTED |

## Why-us status

**PRESERVE** — matches Figma SECTION-04 texts; 8 icon cards operator-calibrated.

## Reviews boundary

Reviews start Y **6064**. **NOT STARTED** — no review markup added.

## Regressions

Section 01/02/03, Header, Footer, responsive shell: **NONE** observed in build + capture pass.

## Build result

**Build succeeded** (`npm run build`).

## Remaining deviations

- Decorative lifebuoy watermark on mockup 6-card grid **not** reproduced (no approved asset; design freeze).
- `1025px` validated via `1024px` capture + desktop `1398px` row (no material layout delta).
- BLOCK-012 benefit grid at 6064 reclassified as Reviews band start — not a separate pre-reviews block.

## Final verdict

**REPAIRED_PENDING_OPERATOR_REVIEW** — horizontal gallery + pre-reviews blocks restored; Reviews not started; no stable tag.
