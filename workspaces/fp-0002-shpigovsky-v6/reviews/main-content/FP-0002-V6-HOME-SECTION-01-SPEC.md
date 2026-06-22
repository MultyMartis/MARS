# FP-0002 V6 HOME SECTION 01 SPEC

## Visual authority

| Field | Value |
|-------|-------|
| Primary | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| JPG structure lock | `audit/jpg-visual-audit/FP-0002-V6-JPG-STRUCTURE-LOCK.md` |
| Group evidence | `archive/aborted-section-attempts/intro-programs/specifications/evidence/02-group-01-intro-grid.jpg` |
| Block | BLOCK-002 (Y 904–1456) / CMP-004 |

**Not used:** FIG, PDF, legacy workspaces, full archived `intro-programs` composite.

## Section boundaries

| Edge | Authority |
|------|-----------|
| Start | Immediately after Hero (`SECTION-001` ends Y 904) |
| End | Before founder quote block (`BLOCK-003` starts Y 1456) |
| Background | Page wash `--color-page-background` |
| Width | Standard `.container` (`--container-main` + `--pad-x`) |

## Exact content

| Element | Text |
|---------|------|
| H2 | Шпиговский дом — восстановление с уважением к личности |
| Lead | Мы убеждены, боль может быть общей для многих… (full paragraph from JPG forensic read) |
| Benefits ×4 | высокий уровень комфорта; анонимное лечение зависимостей; психотерапевтическая реабилитация; лечение зависимости без потери личности, статуса и связи с жизнью. |
| Cards ×6 | 3 unique titles/bodies; row 2 repeats row 1 per JPG layout placeholder |

## Asset mapping

| Asset role | Candidate file | Match | Decision |
| ---------- | -------------- | ----: | -------- |
| Card check icon | Font Awesome `fa-check-circle` (existing vendor bridge) | YES | USE |
| Benefits bullet | CSS pseudo-element (accent dot) | YES | USE — no raster |
| Section photos | none in this block | N/A | NOT REQUIRED |
| Decorative lifebuoy | not in BLOCK-002 crop | N/A | DEFERRED |

## Desktop geometry

- Section vertical padding: `--pad-y`
- Heading → lead gap: `--pad-gap-line`
- Lead → benefits gap: `--pad-gap-line`
- Benefits → card grid gap: `--pad-gap`
- Card grid: 3 columns × 2 rows
- Card internal stack gap: `--pad-gap-line`

## Container usage

Standard `<div class="container">` — no new container token.

## Background

`var(--color-page-background)` on section root.

## Typography roles

| Role | Tokens |
|------|--------|
| H2 | `--font-size-h2`, `--line-height-h2`, `--font-weight-heading` |
| Lead / benefits | `--font-size-base`, `--line-height-base`, `--color-text-secondary` |
| Card title | `--font-size-base`, `--font-weight-heading`, `--color-text-primary` |
| Card body | `--font-size-small`, `--line-height-small`, `--color-text-secondary` |

## Existing spacing tokens

`--pad-x`, `--pad-y`, `--pad-gap`, `--pad-gap-line`, `--pad-gap-mini`, `--pad-box`

## Existing radius tokens

`--radius-main` (cards), `--radius-full` (benefit dot)

## Existing button system

No CTA in Section 01. N/A.

## New values requested

None. All geometry mapped to existing tokens.

## Direct exact geometry

None beyond token mapping above.

## Mobile scope

Desktop implementation only. No mobile-specific layout in canonical JPG for this block. Base overflow protection via grid `minmax(0, 1fr)` only.

## Interaction scope

None. No JS hooks.

## HTML structure

```text
section.home-intro-mission
└── div.container
    ├── h2.home-intro-mission__heading
    ├── p.home-intro-mission__lead
    ├── ul.home-intro-mission__benefits
    └── ul.home-intro-mission__cards
        └── li.home-intro-mission__card ×6
            ├── span.home-intro-mission__card-icon
            ├── h3.home-intro-mission__card-title
            └── p.home-intro-mission__card-text
```

Partial: `src/partials/sections/home-intro-mission.html`

## SCSS placement

`src/scss/style.scss` — block inserted after Hero, before Footer. No SCSS partial.

## Acceptance criteria

- [x] Section correctly identified as BLOCK-002 only
- [x] Content authority complete
- [x] Assets complete (FA icons only)
- [x] Existing tokens mapped
- [x] No unnecessary new values
- [x] No new button system
- [x] No SCSS partial
- [x] No JS required
- [x] Shell unchanged

## Main content section map (middle sections)

| № | Working name | Y start | Y end | Background | Layout | Main content |
|---|---|---:|---:|---|---|---|
| 01 | home-intro-mission | 904 | 1456 | page wash | container + 3×2 cards | intro, benefits, feature cards |
| 02 | founder-quote | 1456 | 1904 | page wash | 2-col quote + portrait | quote, founder card, CTA |
| 03 | treatment-accordion | 1904 | 2824 | page wash | accordion + 4 photos | services list |
| 04 | multidisciplinary-copy | 2824 | 4544 | page wash | text + service links | approach copy |
| 05 | staff-group-photo | 4544 | 4992 | full-width image | edge-to-edge | team photo |
| 06 | second-card-grid | 4992 | 6064 | page wash | cards + landscape | advantages grid |
| 07 | benefits-reviews-process | 6064 | 9416 | mixed | multi-band | benefits, reviews, steps, CTA |
| 08 | programs-philosophy | 9416 | 12336 | mixed | programs + mosaic | program cards |
| 09 | video-specialists | 12336 | 14368 | page wash | video + profiles | media + doctors |
| 10 | articles | 14368 | 14736 | page wash | 3 cards | blog |
| 11 | faq | 14736 | 15408 | page wash | accordion | FAQ |
| 12 | contact-form | 15408 | 15776 | dark band | form | lead form |

**Total middle sections:** 12

## Section order

```text
Hero
Section 01 — home-intro-mission
Section 02 — founder-quote
Section 03 — treatment-accordion
Section 04 — multidisciplinary-copy
Section 05 — staff-group-photo
Section 06 — second-card-grid
Section 07 — benefits-reviews-process
Section 08 — programs-philosophy
Section 09 — video-specialists
Section 10 — articles
Section 11 — faq
Section 12 — contact-form
Footer
```
