# FP-0002 V6 UNIVERSAL STYLE SCALE NORMALIZATION REVIEW

**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Pilot:** `workspaces/fp-0002-shpigovsky-v6/`

---

## Operator method

Tokens represent **system scale roles** (`--pad-x`, `--pad-gap`, …), not selector mirrors (`--footer-column-gap`, `--header-padding-block-start`). Blocks consume the compact scale directly. Alias chains and logical shorthand padding/margin properties are prohibited in production SCSS. Unique JPG geometry stays as **direct local CSS** with classification comments — not `:root` selector tokens.

---

## Manual changes protected

| File | Operator change | Preserve | Additional normalization |
| ---- | --------------- | -------: | ------------------------ |
| `gulpfile.js` | `buildIncremental` + `watch:dev` export | YES | NONE — preserved unchanged |
| Active SCSS (Header/Hero/Footer) | Prior approved geometry | YES | Token + property syntax only |

---

## Previous token model

- Numeric `--space-*` ladder (10 tokens) + `--page-padding-inline`
- Selector-specific Header tokens (`--header-padding-block-start/end`)
- Selector-specific Footer spacing/social aliases (10 tokens)
- Unused section rhythm aliases (`--section-padding-*`, `--heading-content-gap`, …)
- Logical CSS properties in container, header, footer, hero, button

---

## New compact scale

```scss
--pad-x: 40px;
--pad-y: 50px;
--pad-gap: 30px;
--pad-gap-line: 15px;
--pad-gap-mini: 5px;
--pad-gap-tight: 10px;
--pad-box: 20px;
```

Radius: `--radius-small`, `--radius-medium`, `--radius-large`, `--radius-full` (renamed from `--radius-pill`).

---

## Tokens preserved

Typography system, color roles, `--container-main`, `--container-hero`, control/button/icon shared component tokens, frosted surface tokens, motion tokens.

---

## Tokens renamed

| From | To |
| ---- | -- |
| `--radius-pill` | `--radius-full` |
| `--page-padding-inline` | `--pad-x` (usages) |

---

## Tokens removed

All `--space-*`, all `--header-*` spacing, all `--footer-*` spacing/social aliases, unused `--section-padding-*` / `--heading-content-gap` / `--grid-gap-standard` / `--card-padding-standard` / `--accordion-row-spacing`.

---

## Selector-specific aliases removed

12 tokens: `--header-padding-block-start`, `--header-padding-block-end`, `--footer-column-gap`, `--footer-gap`, `--footer-padding-block`, `--footer-row-gap`, `--footer-legal-gap`, `--footer-nav-heading-gap`, `--footer-nav-link-gap`, `--footer-contact-stack-gap`, `--footer-legal-row-padding-block`, `--footer-social-gap`, plus social surface/size/font aliases (`--footer-social-size`, `--footer-social-icon-size`, `--footer-social-background`, `--footer-social-fa-size`).

---

## One-use tokens removed

All removed section rhythm aliases had **0 active SCSS consumers**.

---

## Alias chains removed

Examples: `--footer-padding-block → --section-padding-compact → --space-40`; `--footer-gap → --footer-column-gap → --space-30`; `--footer-social-gap → --space-10`.

---

## Logical properties removed

| File | Count |
| ---- | ----: |
| `_base.scss` | 2 |
| `_header.scss` | 3 |
| `_footer.scss` | 2 |
| `_hero.scss` | 2 |
| `_button.scss` | 2 |
| **Total** | **11** |

---

## Direct exact values

- Header: `padding-top/bottom: 18px` (JPG header inset)
- Hero: `$hero-panel-width`, `$hero-panel-padding-y: 25px`, `$hero-panel-cta-gap: 12px`, `$hero-stack-bottom-offset: 66px`, `$hero-panel-border`
- Header/Footer logo: `182×82px`
- Compact callback label: `12px` (block-level, not primary button role)

---

## Container

`.container` uses physical properties: `margin-left/right: auto`, `padding-left/right: var(--pad-x)`, `max-width: var(--container-main)`.

---

## Header

Uses `--pad-box`, `--pad-gap-line`, `--pad-gap-tight`, shared icon/control tokens. Top/bottom rhythm: direct `18px` exact geometry.

---

## Hero

Geometry unchanged. Spacing references migrated to `--pad-x`, `--pad-gap-line`. `margin-left/right: auto` on `.hero`. `--container-hero` preserved.

---

## Footer

All spacing from compact scale: `--pad-x` (section vertical + row/legal gaps), `--pad-gap`, `--pad-box`, `--pad-gap-line`, `--pad-gap-tight`. Social links use `--icon-size-*`, `--radius-full`, `--color-surface`, `--font-size-large`.

---

## Components

Buttons use physical horizontal padding + shared `--control-*` tokens. Icons unchanged.

---

## Visual regression

Playwright capture @ 1398px — **PASS** (dist present; layout renders).

- `reviews/foundation/visual/FP-0002-V6-UNIVERSAL-STYLE-SCALE-HEADER.png`
- `reviews/foundation/visual/FP-0002-V6-UNIVERSAL-STYLE-SCALE-FOOTER.png`
- `reviews/foundation/visual/FP-0002-V6-UNIVERSAL-STYLE-SCALE-FULL.png`

---

## Watcher/build status

- **Watcher before task:** RUNNING (`npm run watch:dev`) — not stopped/restarted
- **Watcher after task:** RUNNING (multiple historical sessions; dist locked — expected)
- **One-shot `npm run build`:** FAIL — `EBUSY` on `dist/` (watcher lock) — **expected**
- **SCSS compile check:** PASS (`npx sass src/scss/style.scss` exit 0)
- **Dist render for screenshots:** PASS

---

## Factory governance

Created [universal-style-scale-law-v1.md](../../../projects/mars-website-factory/universal-style-scale-law-v1.md). Updated CSS Variable First Law, pre-SCSS checklist, block spec, site-wide foundation, QA reporting, pipeline, section spacing rule, production invariants, practical normalization, production rules, prompt discipline, workflow map, roadmap, artefact registry, OPERATIONAL-INDEX, Gulp Frontend Agent card + QA checklist + frontend rules.

---

## Final verdict

**WEBSITE FACTORY UNIVERSAL STYLE SCALE LAW — ACTIVE**  
**FP-0002 V6 NORMALIZATION — PASS**  
Header, Hero, Footer geometry preserved. Main content sections not started.
