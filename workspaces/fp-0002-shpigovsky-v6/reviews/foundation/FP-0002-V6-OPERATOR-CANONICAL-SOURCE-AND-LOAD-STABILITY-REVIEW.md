# FP-0002 V6 OPERATOR-CANONICAL SOURCE AND LOAD STABILITY REVIEW

**Date:** 2026-06-23  
**Pilot:** `workspaces/fp-0002-shpigovsky-v6/`  
**Branch:** `mars/post-cycle8-live-tests`

## Operator source authority

Current files under `src/` are **operator-canonical**. Manual operator calibration of Header, Hero, Footer, and `style.scss` is the sole implementation authority. Previous generated implementations, specifications, reviews, screenshots, token maps, and commits are **historical evidence only**.

## Protected manual files

| File | Operator changes (summary) | Protected |
|------|------------------------------|-----------|
| `src/partials/layout/header.html` | `site-header__btns-wrap` grouping; messenger/button layout | YES |
| `src/partials/sections/hero.html` | `hero__media--wrapper` structure | YES |
| `src/partials/layout/footer.html` | legal column, contact meta `<em>`, layout blocks | YES |
| `src/scss/style.scss` | typography weights/sizes, hero/footer/header geometry, social icon circles | YES |
| `src/js/main.js` | zero skeleton | YES |
| `gulpfile.js` | unchanged this task | YES |

## Protected design values

All operator-authored dimensions, spacing, typography, colors, radii, and button geometry in current `style.scss` are frozen. **Agent design values changed: 0.**

## Agent changes to canonical source

| File | Change type |
|------|-------------|
| `header.html` | Removed `data-safe-unknown`; semantic button/nav casing; placeholder `href="#"` for unknown URLs |
| `hero.html` | Removed `data-safe-unknown`; semantic CTA casing; hero `width`/`height` attributes |
| `footer.html` | Removed `data-safe-unknown`; semantic button casing; placeholder `href="#"` where needed |
| `index.html` | Inter font weights trimmed to 300;400;500 |
| `style.scss` | Comment sync only (font URL note) |

## data-safe-unknown removal

| File | Removed |
|------|--------:|
| `header.html` | 12 |
| `hero.html` | 1 |
| `footer.html` | 19 |
| **Total active src** | **32** |
| **Remaining active src** | **0** |
| **Remaining compiled HTML** | **0** |

## HTML semantic casing

| File | Before | After | CSS owner |
|------|--------|-------|-----------|
| `header.html` | ЗАКАЗАТЬ ЗВОНОК | Заказать звонок | `.btn` (`text-transform: uppercase`) |
| `hero.html` | ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ | Записаться на консультацию | `.btn` |
| `footer.html` | ЗАКАЗАТЬ ЗВОНОК | Заказать звонок | `.btn` |
| `footer.html` | ЗАПИСАТЬСЯ | Записаться | `.btn` |

**Uppercase violations remaining:** 0  
**Official uppercase exceptions:** NONE (no acronyms in visible button copy)

## CSS uppercase ownership

Existing `.btn { text-transform: uppercase; }` in `style.scss` — no new typography values introduced.

## Current JS behavior

**NONE** — `src/js/main.js` remains zero skeleton.

## JS hook audit

| Function | Selector | Risk | Action |
|----------|----------|------|--------|
| NONE | NONE | NONE | NOT APPLICABLE |

**Migration required:** NONE  
**Unused data hooks added:** 0

## Font delivery before

- Inter via Google Fonts `<link>` in `index.html`
- Weights requested: 300;400;500;600;700
- `display=swap`
- `preconnect` to `fonts.googleapis.com` and `fonts.gstatic.com`
- No local WOFF2 in `src/fonts/`

## Previous proven solution

| Solution | Evidence | Applicable | Decision |
|----------|----------|------------|----------|
| Google Fonts early `<head>` + preconnect | Triumph Manipulator `head.html` partials | YES | Retained |
| Self-host + preload WOFF2 | Manipulator v5/v6 hardening audit | NO (no licensed local Inter files) | Document PARTIAL risk |
| `font-display: block` on FA subset | Manipulator v6 `screen-icons.css` | PARTIAL (FA bundled via Gulp bridge in main CSS) | Icon boxes reserved at 40×40 |

## Font delivery after

- Inter via Google Fonts `<link>` in `index.html`
- Weights requested: **300;400;500 only** (matches active CSS)
- `display=swap`
- `preconnect` present
- No duplicate Inter requests
- Hero raster: intrinsic `width="2230" height="1246"`

## Font files and weights

| Font | Weight | Source | Above fold | Preloaded | font-display | Status |
|------|--------|--------|------------|-----------|--------------|--------|
| Inter | 300 | Google Fonts CSS | YES | NO (CSS link only) | swap (URL param) | ACTIVE |
| Inter | 400 | Google Fonts CSS | YES | NO | swap | ACTIVE |
| Inter | 500 | Google Fonts CSS | YES (buttons/nav emphasis) | NO | swap | ACTIVE |
| Font Awesome Pro 5.15.4 | brands/solid | Gulp shared bridge → `style.css` | YES (search, footer) | NO | vendor default | ACTIVE |

## Preload and preconnect

- **Preconnect:** `fonts.googleapis.com`, `fonts.gstatic.com` — PRESENT
- **Preload:** NONE (external CSS discovery; no local WOFF2 files committed)

## Font-display

`display=swap` via Google Fonts URL parameter.

## FOUT/FOIT validation

| Check | Before | After |
|-------|--------|-------|
| Visible fallback-font flash | OBSERVED (600/700 unused weights + swap) | MATERIALLY REDUCED |
| FOIT / blank text | NOT OBSERVED | NOT OBSERVED |
| Global invisibility hack | NOT USED | NOT USED |

## Layout shift sources

**Before (qualitative):** font metric swap on phones, hero panel, footer phone; FA YouTube glyph resize.

**After (Playwright CLS, cold load, 1398×2200):** `cls_total ≈ 0.0064` — minor shifts in `site-header__phones`, `hero__panel`, `site-footer__phone`, FA YouTube icon. No observable header/nav/button geometry break after `networkidle`.

## Icon stability

- Messenger/social/contact icons: fixed 40×40 flex boxes (operator-authored)
- Search: `16×16` box via `--icon-size-small`
- YouTube FA: minor sub-pixel width shift on load (documented)

## Image stability

- Hero PNG: intrinsic dimensions in HTML
- Logo SVG: height constrained by operator CSS (`80px` header/footer logo containers)

## CSS load order

1. Google Fonts stylesheet (`<head>`)
2. `assets/css/style.css` (includes FA vendor bridge via Sass `meta.load-css`)
3. `assets/js/main.js` (`defer`)

## Design regressions

**NONE OBSERVED** — operator geometry preserved; only DOM hygiene and delivery optimization.

## Factory governance

Published laws under `projects/mars-website-factory/`:

- `operator-canonical-source-law-v1.md`
- `no-new-design-values-after-operator-calibration-law-v1.md`
- `no-production-safe-unknown-attribute-law-v1.md`
- `semantic-text-casing-law-v1.md`
- `data-attribute-js-hook-law-v1.md`
- `font-and-layout-stability-law-v1.md`

Updated: OPERATIONAL-INDEX, pre-SCSS checklist, implementation pipeline, QA checklist, gulp agent card, prompt discipline, safe-unknown-boundary.

## Remaining risks

- **PARTIAL · EXTERNAL FONT DELIVERY RISK** — Inter depends on Google network; sub-pixel CLS on font swap remains possible.
- Placeholder `href="#"` on unknown nav/social URLs until content binding task.

## Final verdict

**PASS WITH DOCUMENTED PARTIAL EXTERNAL FONT RISK**

```text
operator_canonical_source_law: ACTIVE
design_value_freeze: ACTIVE
production_data_safe_unknown: 0
semantic_html_casing_law: ACTIVE
fout_foit_status: RESOLVED_OR_MATERIALLY_REDUCED
layout_shift_status: VALIDATED (cls_total ≈ 0.0064)
main_content_status: NOT_STARTED
responsive_status: NOT_STARTED
```

**Evidence:**

- `reviews/foundation/visual/FP-0002-V6-FIRST-PAINT-COLD.png`
- `reviews/foundation/visual/FP-0002-V6-FONTS-LOADED.png`
- `reviews/foundation/visual/FP-0002-V6-FONT-STABILITY-FULL.png`
- `reviews/foundation/visual/FP-0002-V6-FONT-STABILITY-METRICS.json`
