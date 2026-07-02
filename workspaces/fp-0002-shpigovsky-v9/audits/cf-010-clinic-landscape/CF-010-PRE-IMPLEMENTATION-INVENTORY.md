# CF-010 Pre-Implementation Inventory — Clinic Landscape

**Date:** 2026-06-29  
**Authority:** `472be1ab` (operator manual polish) + HEAD `fdd1899c`  
**Task:** FP-0002 V8 CF-010 clinic landscape neutralization

---

## Candidate table

| Candidate | Partial/source | Consumers | Root class | Structure | Visual role | CSS source | JS/hooks | Classification |
|---|---|---:|---|---|---|---|---|---|
| home-clinic-landscape | `src/partials/sections/home-clinic-landscape.html` | 3 | `.home-clinic-landscape` | section > container > bleed > img | Full-width clinic exterior/territory photo band | `style.scss` L1574–1595, L3876–3878, L6197–6199 | none | **SAME_CF010_FAMILY** |
| home-staff-photo | `src/partials/sections/home-staff-photo.html` | 1 (index) | `.home-staff-photo` | section > container > bleed > img | Staff group photo band | separate SCSS block | none | **SIMILAR_BUT_DIFFERENT** |
| home-gallery | `src/partials/sections/home-gallery.html` | 1 (index) | `.home-gallery` | gallery grid + Fancybox | Interior gallery with captions | separate SCSS + JS | Fancybox | **SIMILAR_BUT_DIFFERENT** (HOLD) |

---

## Exact consumer count

**3** active consumers of `home-clinic-landscape.html`:

1. `src/pages/index.html` — include param `"no-top-padding"`
2. `src/pages/usluga-podrazdel-v1.html` — include param `""`
3. `src/pages/usluga-konechnaya-v1.html` — include param `"service-leaf-landscape-v1"`

## Inline copies

**0** — single shared partial only.

## Duplicate partials

**0**

## Duplicate CSS

**0** duplicate CSS blocks; one family with page-scoped padding override:

`.page-service-leaf-v1 .home-clinic-landscape.service-leaf-landscape-v1`

## Page-specific wrappers

**0** wrapper partials; leaf page passes modifier class via include param.

## Planned confirmed consumers

- O-Centre page: forecasted in reuse maps (`FP-0002-HOME-COMPONENT-REUSE-MAP-v1.md`) — **not implemented**, requires future anatomy audit.
- Registry pre-classified as `SHARED_BUT_PAGE_NAMED`.

## Asset dependencies

- `assets/img/content/pre-reviews/shpigovsky-clinic-landscape.webp` (1139×584)
- Source path in partial; no picture/source element.

## Unresolved candidates

**None** for CF-010 family boundary.

---

## Family classification gate (pre-implementation)

| Field | Value |
|---|---|
| Classification | **SHARED_BUT_PAGE_NAMED** |
| Included consumers | index, usluga-podrazdel-v1, usluga-konechnaya-v1 |
| Excluded | home-staff-photo (different image role/dimensions), home-gallery (HOLD) |
| Implementation decision | **NEUTRALIZE** → `clinic-landscape` |

## Evidence

- Identical HTML structure across 3 consumers (same partial).
- Same CSS model (bleed wrapper, fixed-height cover image, mobile height override).
- Same semantic role (decorative/environment clinic exterior band).
- No Home-only content in markup; aria-label is clinic-territory generic.
- Shared include registry documents 3 consumers and `SHARED_BUT_PAGE_NAMED`.
