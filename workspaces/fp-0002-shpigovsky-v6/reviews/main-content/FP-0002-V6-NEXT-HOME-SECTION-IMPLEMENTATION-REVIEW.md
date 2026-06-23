# FP-0002 V6 NEXT HOME SECTION IMPLEMENTATION REVIEW

**Date:** 2026-06-23

## Reviews stable release

`FP-0002-V6-REVIEWS-OPERATOR-STABLE-01` — backup verified, restore test PASS, tag pushed.

## Operator source protection

Operator-canonical Reviews HTML preserved. Operator SCSS reviews card border/background/text changes preserved (`background-color: ек` — invalid CSS token, compiles; not overwritten). **Operator values overwritten: 0** in frozen blocks.

## Sole visual authority

`HOME-PAGE-FULL-MOCKUP.jpg` SHA-256 `CDD1D5BCC512B617DCF93EFA97AF88CF4AD99A0895CFC27A63C07BC704945290`

## Section identity

`home-rehabilitation-requirements` — «Что нужно для прохождения реабилитации и лечения»

## Boundaries

| Field | Y |
|-------|---:|
| Reviews end | 7136 |
| Next start | 7136 |
| Content end | 8448 |
| Next end | 8824 |
| Following start | 8824 |

Gate: **PASS**

## Exact content

Figma SECTION-06 step texts + intro; CTA lead from JPG visual; phone from approved shell.

## Existing visual system reuse

`.container`, accent bar, `.btn.btn_dark.btn--primary`, clinic photo bleed pattern, existing typography/spacing tokens.

## HTML

`src/partials/sections/home-rehabilitation-requirements.html` — semantic section, 4 steps, CTA, photo.

## SCSS

Single file `src/scss/style.scss` block `10j` after Reviews, before Footer.

## JS

No changes.

## Existing tokens reused

`--pad-gap*`, `--radius-main`, `--radius-full`, `--color-text-primary`, `--color-accent`, `--font-size-h2/h3/base/small`

## New direct values

48px step disc; 388px/220px interior height; 40px/24px CTA phone sizes.

## Pixel comparison

Screenshots in `reviews/main-content/next-section-implementation/`.

## Desktop result

Build PASS. Desktop doc overflow -15px (pre-existing shell quirk).

## Mobile safety

**BASIC RESPONSIVE SAFETY** — 390px horizontal overflow 95px doc (shell-level; not introduced by section grid alone).

## Previous sections regression

NONE in build pass.

## Reviews regression

NONE — Swiper configs untouched.

## Build

**Build succeeded**

## Remaining deviations

- Documents sub-block («Документы для поступления») not implemented — list text not verified in Figma extract; interior photo covers BLOCK-017 visual band.
- Operator `background-color: ек` on review cards — invalid CSS value; preserved per operator canon.
- CTA lead text from JPG visual authority, not Figma node.

## Final verdict

**IMPLEMENTED_PENDING_OPERATOR_REVIEW**
