# FP-0002 V6 SECTION-001 SOURCE-TO-TOKEN MAP

**Scope:** SECTION-001 — Header + Hero  
**Rule:** Every proposed value requires JPG evidence or foundation binding.

---

## Traceability table

| Spec ID | JPG evidence | Observed value | Foundation binding | Proposed value | Confidence | Exception |
| ------- | ------------ | -------------- | ------------------ | -------------- | ---------- | --------- |
| S001-GEO-001 | Full section crop | Y 0–904 | EX-002 | height 904px | HIGH | EX-002 |
| S001-GEO-002 | evidence/02-header | Logo x 130–312 y 18–100 | — | element bounds | MEDIUM | — |
| S001-GEO-003 | evidence/07-header | Phones x 851–1200 y 38–80 | — | element bounds | MEDIUM | — |
| S001-GEO-004 | probe nav band | Nav y 132–174 | — | element bounds | MEDIUM | — |
| S001-GEO-005 | probe y174 | Y=174 dark_frac spike | OBSERVED_JPG_ESTIMATE | **CSS FORBIDDEN** | LOW | — |
| S001-GEO-006 | evidence/03-hero | Hero CTA y 792 h 45 w 297 | — | 45px height | HIGH | EX-S001-001 |
| S001-CNT-001 | Operator decision | — | `container-main` | max-width 1220px | HIGH | — |
| S001-CNT-002 | Geometry map median | x 130–1267 w 1138 | OBSERVED_JPG_VALUE | informational only | MEDIUM | — |
| S001-CNT-003 | Factory convention | — | `container-padding-inline-desktop` DEFERRED | block proposal 50px | LOW | HOLD |
| S001-SPC-001 | Header row visual | Logo–address ~25px | `grid-gap-standard` / `text-stack-gap` | margin 20–30px | LOW | block proposal 20px |
| S001-SPC-002 | Header meta lines | line stack ~8px | OL-01 padding/margin | 10px | LOW | block proposal |
| S001-SPC-003 | Messenger icons | ~10px between | OL-01 gap | 10px gap | MEDIUM | — |
| S001-SPC-004 | ROW-01/02 gap | ~15–20px | `accordion-row-spacing` | margin 15px | MEDIUM | — |
| S001-SPC-005 | Nav links | ~30px horizontal | `grid-gap-standard` | gap 30px | MEDIUM | APPROVED |
| S001-SPC-006 | Hero panel stack | tagline–title ~15px | `text-stack-gap` | margin 20px | LOW | — |
| S001-SPC-007 | Panel–CTA gap | ~20px | `text-stack-gap` | margin 20px | MEDIUM | — |
| S001-TYP-001 | evidence/02-header | Nav ~14–16px | DEFERRED global | 15px block | LOW | block proposal |
| S001-TYP-002 | evidence/02-header | Phones ~16–18px | DEFERRED global | 18px block | MEDIUM | block proposal |
| S001-TYP-003 | evidence/03-hero | Tagline ~16px | DEFERRED global | 16px block | MEDIUM | block proposal |
| S001-TYP-004 | evidence/03-hero | Title ~36–48px | DEFERRED global | 40px block | MEDIUM | block proposal |
| S001-TYP-005 | evidence/03-hero | CTA label ~13px | DEFERRED global | 13px block | MEDIUM | block proposal |
| S001-COL-001 | probe sample | 230,239,246 | `page-background` role | role only | MEDIUM | HEX HOLD |
| S001-COL-002 | header crop | dark blue-grey text | `primary-text` role | role only | MEDIUM | HEX HOLD |
| S001-COL-003 | hero overlay | white text | `inverse` role | role only | HIGH | HEX HOLD |
| S001-COL-004 | hero CTA | red fill | `accent` role | role only | LOW | HEX HOLD |
| S001-BTN-001 | evidence/02-header | outline pill ~32px | DEFERRED `button-height-standard` | FAM-BTN-HEADER-OUTLINE block | MEDIUM | block family |
| S001-BTN-002 | probe hero_red | h 45px red fill | DEFERRED `button-height-standard` | **45px** hero CTA | HIGH | EX-S001-001 |
| S001-RAD-001 | header CTA visual | pill shape | DEFERRED `radius-button` | 50% height pill | MEDIUM | block |
| S001-RAD-002 | hero panel visual | large corners | DEFERRED `radius-hero-panel` | **20px** block | MEDIUM | BP-S001-HERO-005 |
| S001-RAD-003 | hero photo top | rounded corners | DEFERRED | **20px** `hero-media-radius` | MEDIUM | BP-S001-HERO-006 |
| S001-LAY-001 | full mockup | photo under nav | `container-bleed-media` | inset media field 1361px @ 18px | HIGH | BP-S001-HERO-001 |
| S001-INT-001 | static JPG | — | — | sticky SAFE UNKNOWN | — | — |
| S001-INT-002 | static JPG | — | — | dropdown SAFE UNKNOWN | — | — |
| S001-RES-001 | no mobile art | — | — | mobile SAFE UNKNOWN | — | breakpoint 1024px |

---

## Foundation tokens used in SECTION-001

| Token | Value | Property class | Status |
|-------|-------|----------------|--------|
| `container-main` | 1220px | max-width | APPROVED_OPERATOR_RULE |
| `grid-gap-standard` | 30px | gap | APPROVED_OPERATOR_RULE |
| `text-stack-gap` | 20px | margin | PROPOSAL |
| `accordion-row-spacing` | 15px | margin | APPROVED_OPERATOR_RULE |
| `heading-content-gap` | 30px | margin | APPROVED_OPERATOR_RULE (contextual) |

---

## Block-level proposals (not site-wide)

| ID | Proposal | Evidence |
|----|----------|----------|
| BP-S001-001 | Hero CTA height 45px | probe `hero_red_button.h=45` |
| BP-S001-002 | Header CTA outline family separate from red primary | evidence/02-header |
| BP-S001-003 | Typography px per role table in Implementation Spec | crops |
| BP-S001-004 | Container inline padding proposal after inset math | x_start 130 vs 1220 |
| BP-S001-HERO-001 | Hero media inset **18px** inline; visual width **1361px** @ 1398 page | JPG probe x 18–1378 |
| BP-S001-HERO-002 | Hero media height **728px** (photo y 174–903) | JPG crop; `HERO_MEDIA_COMPONENT_GEOMETRY` |
| BP-S001-HERO-003 | `object-position: 36% 58%` | PIL crop MAE vs JPG reference |
| BP-S001-HERO-004 | Hero stack bottom offset **66px** (CTA bottom to media bottom) | probe CTA y 792 h 45; media end y 903 |
| BP-S001-HERO-005 | Frosted panel **600×auto**, padding 25/40, radius **20px** | overlay x 400–1000 |
| BP-S001-HERO-006 | Hero media radius **20px** | evidence/01-section-001-full corner visual |
| BP-S001-HERO-007 | Hero CTA **297×45px**, radius 22px, `rgb(149,47,43)` | probe + center sample |

---

## Forbidden mappings

| Value | Why forbidden |
|-------|---------------|
| 174px CSS height/split | OBSERVED_JPG_ESTIMATE — operator rule |
| 1138px max-width | OBSERVED_JPG_VALUE — not CSS container |
| 30px hero CTA height | Contradicts observed 45px |
| `accordion-row-spacing` as gap | property_class margin only |
