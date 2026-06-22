# QA checklist — Gulp Frontend Agent (target project)

Use after **source** edits in the **target** gulp-starter (or equivalent) project. Record honest pass/fail/partial in REPORT.

## Build and output

- [ ] **Build check:** project’s documented build command run; exit success or failure captured (**SAFE UNKNOWN** if not run).
- [ ] **No `dist/` manual edits:** confirm fixes were applied in `src/` only.

## Layout and responsive

- [ ] **Responsive check:** spot widths from handoff **`responsive_rules`** (e.g. 375 / 768 / 1280) — **supplementary** unless project is non-RU.
- [ ] **RU typography / no word-splitting (RU commercial — mandatory):** run [ru-landing-qa-preset-v1.md](../../projects/mars-website-factory/ru-landing-qa-preset-v1.md); authority [russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md). REPORT: `RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial | FAIL | SAFE UNKNOWN`.
- [ ] **Overflow check:** horizontal scroll, sticky/fixed elements not clipping tap targets.
- [ ] **One SCSS file gate (mandatory):** project styles only in `src/scss/style.scss`; no new project partials; no project `@use`/`@import` — [one-project-scss-file-law-v1.md](../../projects/mars-website-factory/one-project-scss-file-law-v1.md). REPORT: `ONE SCSS FILE GATE — PASS | FAIL | SAFE UNKNOWN`.
- [ ] **Unified radius gate (mandatory):** `--radius-main` / `--radius-full` only; legacy `--radius-small|medium|large` absent; `--button-letter-spacing` absent — [universal-style-scale-law-v1.md](../../projects/mars-website-factory/universal-style-scale-law-v1.md) · [no-button-letter-spacing-law-v1.md](../../projects/mars-website-factory/no-button-letter-spacing-law-v1.md). REPORT: `RADIUS SYSTEM GATE — PASS | FAIL | SAFE UNKNOWN`.
- [ ] **Universal button system gate (mandatory):** all CTAs use `.btn`; modifiers `.btn_dark` / `.btn--primary` only; no parallel block button geometry — [universal-button-system-law-v1.md](../../projects/mars-website-factory/universal-button-system-law-v1.md). REPORT: `UNIVERSAL BUTTON SYSTEM GATE — PASS | FAIL | SAFE UNKNOWN`.
- [ ] **Operator source gate (mandatory):** current `src` inspected; operator changes protected — [operator-canonical-source-law-v1.md](../../projects/mars-website-factory/operator-canonical-source-law-v1.md). REPORT: `OPERATOR SOURCE AUTHORITY GATE — PASS | FAIL | SAFE UNKNOWN`.
- [ ] **HTML quality gate (mandatory):** no `data-safe-unknown`; semantic HTML casing; uppercase via CSS — [no-production-safe-unknown-attribute-law-v1.md](../../projects/mars-website-factory/no-production-safe-unknown-attribute-law-v1.md) · [semantic-text-casing-law-v1.md](../../projects/mars-website-factory/semantic-text-casing-law-v1.md). REPORT: `HTML QUALITY GATE — PASS | FAIL | SAFE UNKNOWN`.
- [ ] **JS hook gate:** behavior via `data-*` only when JS exists — [data-attribute-js-hook-law-v1.md](../../projects/mars-website-factory/data-attribute-js-hook-law-v1.md). Off-canvas: [off-canvas-component-contract-v1.md](../../projects/mars-website-factory/off-canvas-component-contract-v1.md). REPORT: `JS HOOK GATE — PASS | FAIL | NOT APPLICABLE`.
- [ ] **WF Grid Discipline (mandatory):** header / hero / major sections / footer inner content align to same container grid — [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md). No `<section>` or `<nav>` with container-only width class. Primary `.container` reused — no duplicate `__container` geometry (WF-GRID-006). REPORT: `WF GRID DISCIPLINE — PASS | FAIL | SAFE UNKNOWN`.
- [ ] **Section rhythm ownership (mandatory):** layout region owns top/bottom rhythm — not first/last internal child — [frontend-section-spacing-rule-v1.md](../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) §2.6. REPORT: `SECTION RHYTHM GATE — PASS | FAIL | SAFE UNKNOWN`.
- [ ] **WF Layout Discipline (mandatory):** inner-zone authority — hero fr/minmax (no default `%`), card/trust/finance patterns per [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md). REPORT: `WF LAYOUT DISCIPLINE — PASS | FAIL | SAFE UNKNOWN`.

## Markup and accessibility

- [ ] **Semantic HTML:** heading order, landmarks, interactive elements use correct tags.
- [ ] **Accessibility basics:** focus visible, accordion/button ARIA as required, form error regions if specified.
- [ ] **Form behavior:** required fields, success state, no PII leakage in client logs.

## Behavior and style

- [ ] **JS hooks:** `data-*` attributes present per **`data_attribute_hooks`**; one clear owner module.
- [ ] **SCSS isolation:** new rules scoped to block; no surprise global resets/`!important` waves.
- [ ] **Section consistency:** order matches **`section_map`**; includes resolve.

## Assets and SEO

- [ ] **Asset paths:** images/fonts resolve; lazy rules respected where specified.
- [ ] **Font delivery gate (mandatory):** local WOFF2 for production fonts when operator requires zero FOUT; preload critical weights; no Google Fonts in production HTML; `font-display: block` when swap produces visible switch — [font-and-layout-stability-law-v1.md](../../projects/mars-website-factory/font-and-layout-stability-law-v1.md). REPORT: `FONT STABILITY GATE — PASS | FAIL | PARTIAL | SAFE UNKNOWN`. Operator visual confirmation required — automated CLS does not override operator-observed FOUT.
- [ ] **SEO basics:** H1 policy, title/description slots, honest schema if present.

## Risk

- [ ] **Performance risks:** oversized images, blocking scripts, third-party embed weight — note heuristically.
- [ ] **SAFE UNKNOWN:** unchecked items listed with reason (timebox, no device access, CI not defined).

---

**Not claimed:** full automated accessibility audit, Lighthouse CI, visual diff against Figma — unless tooling and scope are explicit in the prompt.
