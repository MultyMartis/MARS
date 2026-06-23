# FP-0002 V6 PRE-REVIEWS IMAGE FIX REVIEW

**Date:** 2026-06-23  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`

## Operator source protection

Operator-canonical `src/` preserved. No restore/reset applied. Operator diff in `home-why-us.html` and Section 03 calibration retained. **Operator values overwritten: 0.**

## Staff image

| Field | Value |
|-------|-------|
| Source path | `src/img/content/pre-reviews/shpigovsky-staff-group.webp` |
| Source type | LOSSLESS_CROP_OF_EXISTING_WEBP |
| Figma exact node | NOT FOUND (`.fig` not extracted in this pass) |
| White margin cause | BAKED_IN_EXPORT_CANVAS — light side margins inside asset |
| Dimensions before | 1398×448 |
| Dimensions after | 1139×443 |
| Crop bounds | left 129, top 0, right 1267, bottom 442 |
| Radius | `var(--radius-main)` on `.home-staff-photo__image` |
| Object-fit | `cover` |

## Clinic landscape

| Field | Value |
|-------|-------|
| Source path | `src/img/content/pre-reviews/shpigovsky-clinic-landscape.webp` |
| Source type | LOSSLESS_CROP_OF_EXISTING_WEBP |
| Figma exact node | NOT FOUND |
| White margin cause | BAKED_IN_EXPORT_CANVAS — white vertical bars left/right |
| Dimensions before | 1398×584 |
| Dimensions after | 1139×584 |
| Crop bounds | left 129, top 0, right 1267, bottom 583 |
| Radius | `var(--radius-main)` on `.home-clinic-landscape__image` |
| Object-fit | `cover` |

## New direct values

| Value | Purpose |
|-------|---------|
| Crop algorithm thresholds (238/15) | Technical margin detection in `scripts/_crop_pre_reviews_images.py` only |

## Pre-reviews polish

Other pre-reviews blocks unchanged except HTML intrinsic dimensions and image radius. Gallery, Why-us, Feature grid geometry preserved.

## Build result

**Build succeeded** (`npm run build`).

## Screenshots

- `reviews/main-content/pre-reviews-image-fix/FP-0002-V6-STAFF-IMAGE-FIX-DESKTOP.png`
- `reviews/main-content/pre-reviews-image-fix/FP-0002-V6-STAFF-IMAGE-FIX-MOBILE.png`
- `reviews/main-content/pre-reviews-image-fix/FP-0002-V6-CLINIC-LANDSCAPE-FIX-DESKTOP.png`
- `reviews/main-content/pre-reviews-image-fix/FP-0002-V6-CLINIC-LANDSCAPE-FIX-MOBILE.png`

## Final verdict

**CORRECTED_PENDING_OPERATOR_REVIEW** — white margins removed; radius applied; operator geometry preserved.
