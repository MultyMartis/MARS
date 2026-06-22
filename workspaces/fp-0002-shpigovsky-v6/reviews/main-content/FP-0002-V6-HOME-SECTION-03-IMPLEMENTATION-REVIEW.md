# FP-0002 V6 HOME SECTION 03 IMPLEMENTATION REVIEW

## Section 02 stable release

`FP-0002-V6-HOME-SECTION-02-OPERATOR-STABLE-01` — tag `fp-0002-v6-section-02-operator-stable-01` — backup verified PASS.

## Operator source protection

Section 01 and Section 02 operator HTML/SCSS preserved; only Section 03 block added after Section 02.

## Sole visual authority

`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`

## Crop and boundaries

Audit: `reviews/main-content/section-03-audit/` — Section 03 Y 2610–3740; Section 04 start Y 3740.

## Exact content

H2, lead, 4 accordion categories, 4 expanded sub-lines — sourced from canonical JPG readability + FIG text cross-check for lead.

## Decorative images excluded

Background lifebuoy watermark and bottom 4 photo cards excluded — no exact approved content assets.

## HTML

`src/partials/sections/home-treatment-prevention.html` — included after Section 02 in `src/pages/index.html`.

## SCSS

Block `10c. Home treatment prevention` in `src/scss/style.scss`.

## Existing styles reused

`.container`, existing typography/color/spacing/radius tokens, Font Awesome icons.

## Direct geometry values

| Value | Evidence |
|------:|----------|
| 15px | view-all link FIG `1:962` |
| 3px | lead accent bar mockup |
| 26px | accordion chevron circle FIG `1:1216` |
| 10px | chevron/triangle icon scale mockup |

## Pixel comparison

`reviews/main-content/section-03-implementation/FP-0002-V6-SECTION-03-COMPARISON.png`

## Desktop result

IMPLEMENTED_PENDING_OPERATOR_REVIEW — accordion + typography match canonical crop; bottom photo row intentionally omitted.

## Mobile safety

BASIC RESPONSIVE SAFETY — stacked header, dotted leaders hidden, overflow 0.

## Section 01 regression

NONE

## Section 02 regression

NONE

## Shell regression

NONE

## Build

PASS — `npm run build` succeeded.

## Remaining deviations

Bottom 4 service photo cards not implemented (decorative policy). Collapsed accordion panels 2–4 empty until operator supplies sub-content authority.

## Final verdict

```text
SECTION 03 PIXEL-PERFECT IMPLEMENTATION — PENDING OPERATOR REVIEW
TEXT AUTHORITY — PASS
DECORATIVE IMAGES ADDED — ZERO
SECTION 04 — NOT STARTED
```
