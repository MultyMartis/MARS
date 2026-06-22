# FP-0002 V6 SECTION-002 SPECIFICATION

**Status:** READY FOR OPERATOR VISUAL REVIEW · **PARTIAL ASSET REQUIRED**  
**Semantic name:** `intro-programs`  
**Pilot:** First Variable-First production block after SECTION-001

---

## Identity

| Field | Value |
|-------|-------|
| Section ID | SECTION-002 |
| Semantic name | `intro-programs` |
| HTML partial | `src/partials/sections/intro-programs.html` |
| SCSS | `src/scss/sections/_intro-programs.scss` |
| Internal groups | GROUP-01 … GROUP-07 (merged major section) |
| Blocks | BLOCK-002 … BLOCK-008 |

---

## Visual source

| Field | Value |
|-------|-------|
| JPG | `HOME-PAGE-FULL-MOCKUP.jpg` |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |
| Y range | 904–4544 (exclusive end) |
| Evidence | `specifications/section-002/evidence/01-section-002-full.jpg` |

---

## Boundaries

| Edge | Y (JPG) | Evidence |
|------|---------|----------|
| Top | 904 | Hero ends; light page wash begins |
| Bottom | 4544 | Full-width staff group photo (SECTION-003) begins |
| Left/right | Page wash; content band ~container-main + padding | HIGH |

---

## Purpose

Composite content band: clinic value intro, six feature cards, founder quote, treatment/program accordion with clinical photos, multidisciplinary approach copy.

---

## Content

See JSON `content` block. Card row 2 repeats row 1 on JPG (layout placeholder) — documented; unique copy SAFE UNKNOWN for cards 4–6 if operator expects distinct text.

---

## DOM structure

```text
section.intro-programs
├── div.intro-programs__group--intro (GROUP-01 / CMP-004)
├── div.intro-programs__group--quote (GROUP-02 / CMP-005)
├── div.intro-programs__group--treatment (GROUP-03–04 / CMP-006 + CMP-007)
└── div.intro-programs__group--approach (GROUP-05–07 / team copy)
```

---

## Assets

| Asset role | Required | Source found | Status |
|------------|----------|--------------|--------|
| Founder portrait | YES | NOT FOUND | **ASSET_REQUIRED** |
| Clinical photo ×4 | YES | NOT FOUND | **ASSET_REQUIRED** |
| Lifebuoy decor (optional bg) | NO | NOT FOUND | DEFERRED |
| Card check icon | YES | Font Awesome `fa-check-circle` | APPROVED pattern |
| Service link arrow | YES | Font Awesome `fa-external-link-alt` | APPROVED pattern |
| Accordion chevron | YES | Font Awesome `fa-chevron-down` | APPROVED pattern |

---

## Container model

`container-main` (1220px) + `page-padding-inline` (40px). Quote group: two-column grid. Cards: 3×2 grid. Clinical: 4-column grid.

---

## Layout model

Desktop only. Same-wash internal groups separated by `section-gap-same-bg` (30px top padding between groups). No responsive media queries.

---

## Typography roles

| Role | Token |
|------|-------|
| Section H2 | `--font-size-h2`, `--line-height-h2`, `--font-weight-heading` |
| Lead/body | `--font-size-base`, `--line-height-base`, `--color-text-secondary` |
| Card title | `--font-size-base`, `--font-weight-semibold` |
| Card body | `--font-size-small`, `--line-height-small` |
| Highlight uppercase | `--font-size-small`, `--font-weight-medium` |
| Service labels | `--font-size-small`, uppercase |

---

## Color roles

| Role | Token |
|------|-------|
| Section background | `--color-page-background` |
| Card surface | `--color-surface` |
| Primary text | `--color-text-primary` |
| Secondary text | `--color-text-secondary` |
| Accent (bar, icons, quote) | `--color-accent` |
| Borders | `--border-color-subtle` |

---

## Spacing roles

| Role | Token |
|------|-------|
| Group padding | `--section-padding-standard` |
| Same-bg gap | `--section-gap-same-bg` |
| Heading gap | `--heading-content-gap` |
| Text stack | `--text-stack-gap` |
| Card grid gap | `--grid-gap-standard` |
| Card padding | `--card-padding-standard` |
| Accordion row | `--accordion-row-spacing` (margin) |

---

## Component families

CMP-004 service-card-6-grid, CMP-005 quote-block-with-portrait, CMP-006 accordion-row, CMP-007 clinical-image-square-4.

---

## Variables reused

`--container-main`, `--page-padding-inline`, `--color-page-background`, `--color-surface`, `--color-text-primary`, `--color-text-secondary`, `--color-accent`, `--border-color-subtle`, `--border-width`, `--font-family-heading`, `--font-size-h1`, `--font-size-h2`, `--font-size-base`, `--font-size-small`, `--font-size-large`, `--line-height-*`, `--font-weight-*`, `--radius-medium`, `--radius-pill`, `--icon-size-small`, `--section-padding-standard`, `--section-gap-same-bg`, `--heading-content-gap`, `--text-stack-gap`, `--grid-gap-standard`, `--card-padding-standard`, `--accordion-row-spacing`, `--space-5` … `--space-90`, `--control-*`, `--button-*` (founder CTA via `button--compact`).

---

## New tokens proposed

NONE — all rhythm tokens already in Site-Wide Style Foundation; registered in `:root` during this pilot.

---

## Block-level tokens

| Token / variable | Value | Role |
|------------------|-------|------|
| `$intro-programs-accent-bar-width` | `var(--space-5)` | Red vertical highlight bar |
| `$intro-programs-quote-mark-size` | `var(--font-size-h1)` | Opening quote glyph |
| `$intro-programs-clinical-aspect-ratio` | `1` | Clinical photo squares |

---

## Exact geometry exceptions

| Item | Value | Source |
|------|-------|--------|
| Quote mark size | `var(--font-size-h1)` | CMP-005 JPG |
| Clinical aspect | `1` | CMP-007 square photos |

---

## Technical CSS values

`0`, `100%`, `auto`, `1` (aspect-ratio), `1px` borders via tokens, `minmax(0, 1fr)`, `rotate(45deg)` for bullet diamond, `0.55em` bullet vertical align (relative em), `display: none` for collapsed accordion panels (static desktop collapsed state).

---

## Arbitrary values prohibited

`arbitrary_values_allowed: false` — enforced.

---

## Token lookup result

`token_lookup_complete: true` — see `FP-0002-V6-SECTION-002-SOURCE-TO-TOKEN-MAP.md`.

---

## HTML authorization

`html_authorized: true` — HTML review APPROVED FOR SCSS.

---

## SCSS authorization

`scss_authorized: true`  
`arbitrary_values_count: 0`  
`hidden_fallback_literals_count: 0`

---

## JavaScript boundary

`javascript_authorized: false` — accordion static; no toggles.

---

## Responsive boundary

`responsive_authorized: false` — desktop only.

---

## SAFE UNKNOWN

- Cards 4–6 unique copy if JPG duplication is not final content
- Lifebuoy decorative background asset path
- Accordion expanded interaction states
- Founder CTA and service link URLs/actions
- Exact founder portrait crop dimensions until asset supplied
