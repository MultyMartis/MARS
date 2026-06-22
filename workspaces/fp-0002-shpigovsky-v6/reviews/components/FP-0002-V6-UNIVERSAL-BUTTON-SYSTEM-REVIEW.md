# FP-0002 V6 UNIVERSAL BUTTON SYSTEM REVIEW

**Date:** 2026-06-23  
**Pilot:** `workspaces/fp-0002-shpigovsky-v6/`  
**Checkpoint base:** `06eba64711e052a4a7a1be7cfb4238e1f36ef002`

---

## Operator instruction

Enforce Website Factory Universal Button System Law: single `.btn` base, `.btn_dark` and `.btn--primary` modifiers, no parallel block button geometry, token normalization in `:root`, markup migration for Header/Hero/Footer, Factory governance update, visual QA.

---

## Existing button systems

| System | Selectors | Status |
|--------|-----------|--------|
| Legacy shared | `.button`, `.button--compact` | **REMOVED** |
| Header local | `.site-header__callback` (full geometry) | **MIGRATED** — placement + compact label typography only |
| Hero local | `.hero__button` (full geometry) | **MIGRATED** — placement hook only |
| Footer local | `.site-footer__callback`, `.site-footer__cta` + `.button` | **MIGRATED** — placement hooks only |

---

## Token mapping

| Required role | Current token | Decision |
|---------------|---------------|----------|
| Horizontal button padding | `--control-padding-inline` (20px) | **REUSE** via alias `--pad-btns` |
| Main button height | `--control-height-primary` (45px) | **REUSE** via alias `--main-size-btns` |
| Minimal icon gap | `--pad-gap-mini` (5px) | **REUSE** direct |
| Full radius | `--radius-full` (999px) | **REUSE** direct |
| Dark background/border | `--color-text-primary` (#475371) | **REUSE** (maps operator `main-dark-color`) |
| Light text | `--color-text-inverse` (#fff) | **REUSE** (maps operator `font-light-color`) |
| Dark text | `--color-text-primary` | **REUSE** (maps operator `font-dark-color`) |
| Accent | `--color-accent` (rgb(179, 38, 30)) | **REUSE** (maps operator `accent-color-01`) |
| Inverse hover surface | `--color-surface` (#fff) | **REUSE** for `.btn_dark:hover` |
| Transition | `0.3s ease` | **DIRECT** system value (matches `--transition-duration` / `--transition-timing`) |

**Removed button-only tokens:** `--button-font-size`, `--button-line-height`, `--button-font-weight` (geometry/typography now owned by `.btn` using `--font-size-button`).

**Preserved control family tokens:** `--control-height-primary`, `--control-height-compact`, `--control-padding-inline`, `--control-padding-inline-compact`, `--control-border-width` (shared with non-button controls).

---

## Base `.btn`

Implemented in `src/scss/style.scss` §07 Shared components:

- `display: flex`, centered alignment
- `height: var(--main-size-btns)` (45px)
- `padding: 0 var(--pad-btns)` (20px inline)
- `gap: var(--pad-gap-mini)`
- `border-radius: var(--radius-full)` (pill)
- transparent default, `border-color` / `color`: `--color-text-primary`
- `font-weight: 400`, `text-transform: uppercase`, `text-decoration: none`
- transition on background, border, color (0.3s ease)

---

## `.btn_dark`

- Rest: `--color-text-primary` fill/border, `--color-text-inverse` text
- Hover: `--color-surface` fill/border, `--color-text-primary` text

---

## `.btn--primary`

- Combined rest (with `.btn_dark`): `--color-accent` fill/border
- Hover (`.btn--primary.btn:hover` and combined): `--color-accent` fill/border, light text

---

## Semantic elements

| Location | Element | Correct |
|----------|---------|---------|
| Header callback | `<button type="button">` | YES |
| Hero CTA | `<button type="button">` | YES |
| Footer callback | `<button type="button">` | YES |
| Footer signup | `<button type="button">` | YES |

---

## Header migration

**Before:** `class="site-header__callback"` (local full geometry)  
**After:** `class="btn site-header__callback"`  
**Variant:** default outline `.btn`  
**Structural:** `flex: 0 0 auto`, `font-size: 12px` (compact label typography only)

---

## Hero migration

**Before:** `class="hero__button"` (local full geometry, accent fill)  
**After:** `class="btn btn_dark btn--primary hero__button"`  
**Variant:** primary filled accent  
**Structural:** `flex: 0 0 auto`

---

## Footer migration

**Callback before:** `class="site-footer__callback"`  
**Callback after:** `class="btn site-footer__callback"` — default outline  

**Signup before:** `class="site-footer__cta button"`  
**Signup after:** `class="btn btn_dark btn--primary site-footer__cta"` — primary filled accent  

**Structural:** placement + compact label typography on callback only

---

## Legacy selectors removed

- `.button`
- `.button--compact`

---

## Geometry duplicates removed

From `.site-header__callback`, `.hero__button`, `.site-footer__callback`:

- `min-height` / `height`
- horizontal `padding`
- `border` / `border-radius`
- `background-color` / `color`
- `font-weight`
- `text-transform`
- `white-space`
- `cursor`
- duplicate `display` / flex alignment on hero button

---

## Icon inheritance

`.btn svg { fill: currentColor; }` — Font Awesome inherits via `color`.

---

## Focus-visible

`.btn:focus-visible { outline: 2px solid var(--color-accent); outline-offset: 2px; }` — matches global accessible foundation.

---

## Disabled state

`.btn:disabled`, `.btn[aria-disabled='true']` — `cursor: not-allowed`, `pointer-events: none`, `opacity: 0.5`.

---

## Compile result

**PASS** — `npx sass src/scss/style.scss .recovery-temp/fp0002-button-system-compile-check.css` exit 0. Watcher left running (not stopped/restarted).

---

## Visual regression

| Screenshot | Path | Status |
|------------|------|--------|
| Header | `reviews/components/visual/FP-0002-V6-BUTTON-SYSTEM-HEADER.png` | CAPTURED |
| Hero | `reviews/components/visual/FP-0002-V6-BUTTON-SYSTEM-HERO.png` | CAPTURED |
| Footer | `reviews/components/visual/FP-0002-V6-BUTTON-SYSTEM-FOOTER.png` | CAPTURED |
| Full | `reviews/components/visual/FP-0002-V6-BUTTON-SYSTEM-FULL.png` | CAPTURED |

**Note:** Buttons migrated from `--radius-main` (30px) to `--radius-full` (pill) per Universal Button System Law. Compact callback height unified to `--main-size-btns` (45px) from prior 32px compact control — intentional normalization.

---

## Factory governance

Created: `projects/mars-website-factory/universal-button-system-law-v1.md` (R-033)

Updated: OPERATIONAL-INDEX, workflow-map, frontend-implementation-pipeline, frontend-pre-scss-validation-checklist, site-wide-style-foundation-contract, frontend-production-rules, frontend-qa-reporting-standard, block-implementation-specification-contract, universal-style-scale-law, one-project-scss-file-law, website-factory-cross-layer-artefact-registry, gulp-frontend-agent card, frontend-gulp-agent qa-checklist.

---

## Final verdict

**WEBSITE FACTORY UNIVERSAL BUTTON SYSTEM LAW — ACTIVE**

- Parallel button systems: **0**
- Selector-specific button tokens: **0**
- Button letter-spacing: **0**
- Header/Hero/Footer: **PRESERVED** (structure + CTA presence; pill radius + unified height normalized)
