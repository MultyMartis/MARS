# FP-0002 V6 GLOBAL SCSS FOUNDATION REVIEW

## Scope

Global SCSS foundation for FP-0002 V6: local fonts policy, reset, root tokens, typography, universal container, Font Awesome Pro 5.15.4 from shared MARS source. Header/Hero geometry preserved. No new sections. No responsive layout.

## Source authority

- `foundation/FP-0002-V6-SITE-WIDE-STYLE-FOUNDATION.md`
- `foundation/FP-0002-V6-STYLE-FOUNDATION.json`
- SECTION-001 approved Header/Hero SCSS
- `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`

## Previous checkpoint

`684e1690a9883ee4f716937a126cbde3ffd91182`

## Font audit

| File | Family | Weight | Style | Format | SHA-256 | Role |
| ---- | ------ | -----: | ----- | ------ | ------- | ---- |
| — | — | — | — | — | — | **No authorized font files** in `INCOMING/` or `src/fonts/` |

Searched: `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/` (recursive), `workspaces/fp-0002-shpigovsky-v6/src/fonts/`.

## Selected project fonts

**None.** System stack applied per operator rule when project fonts absent.

## Font-face declarations

None — `_fonts.scss` intentionally empty.

## SCSS architecture

**Before:** `utils/variables`, `utils/mixins`, `base/reset`, `layout/container`, `layout/header`, `sections/hero`

**After:** `utils/variables`, `base/fonts`, `base/root`, `base/reset`, `base/base`, `base/typography`, `vendors/fontawesome`, `layout/header`, `sections/hero`

Removed: `layout/_container.scss` (container moved to `base/_base.scss`).

## Root tokens

**Count:** 47 CSS custom properties in `:root` (typography, layout, spacing, colors, radius, motion).

## Typography tokens

See `foundation/FP-0002-V6-FRONTEND-GLOBAL-FOUNDATION.json`.

## Layout tokens

`--container-main: 1220px`, `--container-hero: 1360px`, `--page-padding-inline: 40px`.

## Spacing tokens

`--space-5` through `--space-90` (10 steps).

## Color tokens

8 color roles — values from SECTION-001 approved SCSS.

## Radius tokens

4 radius roles + pill.

## Reset rules

Box-sizing, scrollbar-gutter, media defaults, list/heading margin normalization, fieldset/legend, `[hidden]`, `prefers-reduced-motion`.

## Base HTML rules

`scroll-behavior: smooth` (with reduced-motion override), body defaults, inherit-color links, focus-visible, `.visually-hidden`, `.container`.

## Typography scale

Documented in foundation JSON with APPROVED / PROPOSED / SAFE UNKNOWN per role.

## Universal container

`.container` in `base/_base.scss`. Header/Hero containers unchanged structurally.

## Font Awesome Pro source

`shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` — `css/`, `webfonts/` (no `scss/` in shared tree).

## Font Awesome Pro integration

- Gulp `prepareFaBridge` copies `all.min.css` → `src/scss/vendors/fa-all.css` (gitignored)
- Gulp `faWebfonts` copies `*.woff` / `*.woff2` → `dist/assets/webfonts/`
- `vendors/_fontawesome.scss` uses `meta.load-css('fa-all')`

## Font Awesome build manifest

`reviews/foundation/FP-0002-V6-FONT-AWESOME-PRO-MANIFEST.md`

## External dependency check

No Google Fonts, no CDN font URLs in compiled CSS.

## Header token migration

Site-wide colors via Sass aliases → CSS variables (`$color-page-background` etc.). Container geometry unchanged (`1220px`, `40px` padding, `18px` top padding).

## Hero token migration

`max-width: var(--container-hero)`; accent/inverse colors via `--color-accent`, `--color-text-inverse`. Block geometry unchanged.

## Visual regression

Screenshot: `reviews/foundation/visual/FP-0002-V6-GLOBAL-FOUNDATION-SECTION-001.png`  
Viewport: 1398×1000. Header + Hero render complete.

## Computed styles

| Element | Property | Before | After | Expected | Status |
| ------- | -------- | -----: | ----: | -------- | ------ |
| body | font-size | browser default | 16px | 16px base | OK |
| body | line-height | normal | 20px | 1.25 | OK |
| nav_link | font-size | 15px | 15px | 15px | OK |
| phone | font-size | 18px | 18px | 18px | OK |
| hero_tagline | font-size | 16px | 16px | 16px | OK |
| hero_title | font-size | 40px | 40px | 40px | OK |
| header_container | max-width | 1220px | 1220px | 1220px | OK |
| hero_root | max-width | 1360px | 1360px | 1360px | OK |
| hero_image | height | auto/intrinsic | 759.89px | intrinsic | OK |
| hero_cta | height | 45px | 45px | 45px | OK |

Source: `reviews/foundation/visual/_foundation-computed-styles.json`

## Accessibility

`:focus-visible` preserved with accent outline. No global `outline: none`. `prefers-reduced-motion` in reset (accessibility, not layout).

## Responsive lock

No Header/Hero responsive layout. No new breakpoint media queries for composition.

## JS lock

`src/js/main.js` not modified.

## Build result

`npm run build` — **SUCCESS** (Sass, FA webfonts, project assets).

## SAFE UNKNOWN

- Project font-family files (SU-007) — not in INCOMING; system stack interim
- Exact display/heading font from JPG — not provable without font files or FIG
- H2/H3 global sizes — PROPOSED until SECTION-002+

## Final verdict

**PARTIAL** — global foundation and Font Awesome Pro complete; **project font binding pending** authorized font files. Header/Hero geometry preserved.

---

## Supplement — V1 typography recovery (2026-06-22)

**Checkpoint before:** `c7453aa`  
**Review:** `FP-0002-V6-V1-TYPOGRAPHY-AND-FA-SEARCH-REVIEW.md`

- **Font:** Inter via V1 Google Fonts URL (`wght@300;400;500;600;700`, `display=swap`)
- **Root tokens:** `--font-family-base` → Inter; weight tokens 400/500/600
- **Header search:** `fas fa-search` as eighth nav `<li>`; `search.svg` removed
- **Computed Inter:** confirmed on body, Header, Hero (`_typography-computed-styles.json`)
- **Geometry:** header 1220×186, hero 1360×759.891 — unchanged
- **Verdict:** **READY FOR OPERATOR REVIEW** (typography connected)
