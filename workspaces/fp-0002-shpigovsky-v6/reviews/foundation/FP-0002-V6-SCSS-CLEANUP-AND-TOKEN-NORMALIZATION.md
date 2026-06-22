# FP-0002 V6 SCSS CLEANUP AND TOKEN NORMALIZATION

**Date:** 2026-06-22  
**Checkpoint before:** `c7453aa`  
**HEAD after cleanup:** (see commit)  
**Verdict:** READY FOR OPERATOR REVIEW

---

## Scope

SCSS cleanup for SECTION-001 Header and Hero only. No HTML/DOM changes. No JS. No responsive. No new sections. Factory CSS Variable First Law adoption.

---

## Files audited

| File | Action |
|------|--------|
| `src/scss/base/_root.scss` | Component tokens added |
| `src/scss/utils/_variables.scss` | Sass bridges removed; compile-time paths only |
| `src/scss/base/_base.scss` | Audited — no change |
| `src/scss/base/_typography.scss` | Audited — no change |
| `src/scss/layout/_header.scss` | Token binding + redundancy removal |
| `src/scss/sections/_hero.scss` | CTA content sizing; token binding |
| `src/scss/components/_button.scss` | Created — base control styles |
| `src/scss/components/_icon.scss` | Created — icon size hooks |
| `src/scss/vendors/_fontawesome.scss` | Audited — no change |
| `src/scss/style.scss` | Component imports added |

---

## Arbitrary values inventory

| File | Selector | Property | Value | Classification | Decision |
|------|----------|----------|-------|----------------|----------|
| `_hero.scss` | `.hero__button` | `width` | `297px` | ARBITRARY_VALUE | **REMOVED** |
| `_hero.scss` | `.hero__button` | `max-width` | `calc(100% - 40px)` | ARBITRARY_VALUE | **REMOVED** |
| `_hero.scss` | `.hero__button` | `height` | `45px` | COMPONENT_TOKEN | → `min-height: var(--control-height-primary)` |
| `_header.scss` | various | `font-family` repeat | Inter stack | REDUNDANT_RULE | **REMOVED** (inherits body) |
| `_header.scss` | various | `text-decoration: none` on links | — | REDUNDANT_RULE | **REMOVED** (global `a`) |
| `_header.scss` | `.site-header__container` | `padding-top` | `18px` | BLOCK_LEVEL_TOKEN | **KEPT** |
| `_header.scss` | `.site-header__bottom` | `padding-bottom` | `18px` | BLOCK_LEVEL_TOKEN | **KEPT** |
| `_header.scss` | `.site-header__logo-image` | `width/height` | `182×82` | EXACT_GEOMETRY_EXCEPTION | **KEPT** |
| `_header.scss` | `.site-header__callback` | `font-size` | `12px` | BLOCK_LEVEL_TOKEN | **KEPT** (compact label, not button role) |
| `_hero.scss` | `.hero__panel` | `width` | `600px` | EXACT_GEOMETRY_EXCEPTION | **KEPT** |
| `_hero.scss` | `.hero__panel` | `max-width` | `calc(100% - 40px)` | TECHNICAL_CSS_VALUE | → `calc(100% - var(--space-40))` |
| `_hero.scss` | `$hero-panel-cta-gap` | `gap` | `12px` | EXACT_GEOMETRY_EXCEPTION | **KEPT** (JPG stack) |
| `_hero.scss` | `$hero-stack-bottom-offset` | `padding-bottom` | `66px` | EXACT_GEOMETRY_EXCEPTION | **KEPT** |
| `_hero.scss` | `$hero-panel-border` | `border-color` | `rgba(255,255,255,0.35)` | EXACT_GEOMETRY_EXCEPTION | **KEPT** |
| `_variables.scss` | `$color-*` bridges | Sass aliases | var() | REDUNDANT_RULE | **REMOVED** |
| `_variables.scss` | `$container-*` | Sass px | duplicates | REDUNDANT_RULE | **REMOVED** |

---

## Values removed

- `width: 297px` on `.hero__button`
- `max-width: calc(100% - 40px)` on `.hero__button`
- Fixed `height: 45px` on `.hero__button` (replaced with `min-height` token)
- Sass `$hero-cta-width`, `$hero-cta-height`, `$hero-cta-radius` variables
- Duplicate Sass color/container bridges in `_variables.scss`
- Redundant `font-family`, `text-decoration` on header elements

---

## Rules removed

- Hero CTA hard width constraint
- Hero CTA safety max-width
- Sass `$color-*` runtime bridges
- Header per-element font-family repetition

---

## Dead rules removed

- `$hero-cta-width` and associated width/max-width on button
- Unused Sass spacing aliases consumed only via removed `$` bridges in header (replaced with `var(--space-*)`)

---

## Variables reused

`--container-main`, `--container-hero`, `--page-padding-inline`, `--space-10`, `--space-15`, `--space-20`, `--space-25`, `--space-30`, `--space-40`, `--font-size-small`, `--font-size-large`, `--font-size-nav`, `--font-size-base`, `--font-size-h1`, `--line-height-*`, `--font-weight-*`, `--color-*`, `--radius-medium`, `--radius-large`, `--border-width`, `--border-color-subtle`

---

## New component tokens

`--control-height-primary`, `--control-height-compact`, `--control-padding-inline`, `--control-padding-inline-compact`, `--control-border-width`, `--control-radius`, `--button-font-size`, `--button-line-height`, `--button-font-weight`, `--button-letter-spacing`, `--icon-size-small`, `--icon-size-medium`, `--border-width`, `--border-color-subtle`, `--surface-frosted-background`, `--surface-frosted-blur`, `--transition-base`

---

## Block-level tokens

- Header shell `padding-top` / `padding-bottom`: `18px`
- Header callback label: `font-size: 12px`

---

## Exact geometry exceptions

- Logo: `182×82px`
- Hero panel width: `600px`
- Hero panel-to-CTA gap: `12px`
- Hero stack bottom offset: `66px`
- Hero frosted panel border: `rgba(255, 255, 255, 0.35)`

---

## Technical CSS values

- `width: 100%`, `height: auto`, `min-width: 0`, `inset: 0`
- `white-space: nowrap` on nav/phones/CTA (text safety)
- `1px` borders via `--border-width`
- Panel `max-width: calc(100% - var(--space-40))`

---

## Hero button correction

**Before:**

```scss
width: 297px;
max-width: calc(100% - 40px);
height: 45px;
padding: 0 20px;
```

**After:**

```scss
display: inline-flex;
align-items: center;
justify-content: center;
min-height: var(--control-height-primary);
padding-inline: var(--control-padding-inline);
```

**Width mode:** content-sized (intrinsic from label + padding)

---

## Header cleanup

- Container geometry preserved (`1220px` / `40px` via tokens)
- Sass `$` color/container bridges → `var(--*)`
- Spacing → `--space-*`
- Typography → foundation tokens
- Callback/search → control compact tokens
- Messenger icons → `--icon-size-medium`
- FA search preserved

---

## Hero cleanup

- CTA hard width removed
- Typography → foundation tokens
- Panel surface → `--surface-frosted-*`
- Panel padding → `--space-25` / `--space-40`
- Hero max-width `1360px` preserved via `--container-hero`

---

## Before/after computed styles

See `reviews/foundation/visual/_scss-cleanup-computed-styles.json` (post-build capture).

| Element | Before width | After width |
|---------|--------------|-------------|
| `.hero__button` | `297px` fixed | intrinsic (~content + padding) |

---

## Visual regression

Screenshot: `reviews/foundation/visual/FP-0002-V6-SCSS-CLEANUP-SECTION-001.png`

Expected: Header/Hero layout preserved; CTA narrower/wider per content — **not** 297px forced.

---

## Remaining deviations

- Header callback `12px` label — block-level, not primary button role
- Hero `12px` panel-CTA gap — JPG exact exception (off OL-01 scale)

---

## Arbitrary values remaining

**0**

---

## Factory law compliance

- [css-variable-first-law-v1.md](../../../../projects/mars-website-factory/css-variable-first-law-v1.md) — **ACTIVE**
- Pre-SCSS gate updated
- Foundation JSON flags set

---

## Build result

`npm run build` — **SUCCESS**

---

## Final verdict

**READY FOR OPERATOR REVIEW**
