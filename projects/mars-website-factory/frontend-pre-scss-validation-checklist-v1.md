# Website Factory Frontend Pre-SCSS Validation Checklist v1

**Status:** **documented** — minimal human checklist before SCSS implementation.  
**Not:** runtime linter, Stylelint config, or CI job (unless project adopts separately).

**Authority:** [frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md) gate G-SCS · [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md) · [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md)

---

## When to use

Before writing or merging **block/section SCSS** for any Factory frontend project after HTML structure review.

---

## Checklist

| # | Check | PASS criterion |
|---|-------|----------------|
| 1 | Site-Wide Style Foundation | Operator-approved or scoped PARTIAL waiver documented |
| 2 | Block Implementation Specification | `scss_authorized: true` for target block |
| 3 | Spacing binding | Every margin/padding/gap cites foundation token or exception ID |
| 4 | Typography binding | Every `font-size` cites typography role; line-height per OL or exception |
| 5 | Container binding | Every max-width/wrapper cites container rule |
| 6 | Radius binding | Every `border-radius` cites radius token or exception |
| 7 | Color binding | Every color cites color role — no uninvented hex |
| 8 | Arbitrary values | No new px outside OL-01 scale without traceability row |
| 9 | Source traceability | Evidence ID link exists for each exception |
| 10 | Skipped gate | No SCSS if HTML review or block spec skipped |
| 11 | Compiled CSS laws | Plan for [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) spot-check after build |
| 12 | LOCAL FIX ban | QA defects route to spec/foundation/audit — not one-off magic numbers |
| 13 | **CSS Variable First Law** | [css-variable-first-law-v1.md](css-variable-first-law-v1.md) token lookup complete |
| 14 | Token inventory | All design values classified — see checklist below |

### Style scale gate (mandatory)

- [ ] Existing core spacing scale inspected.
- [ ] Existing radius scale inspected.
- [ ] No selector-specific spacing tokens proposed.
- [ ] No one-use alias tokens proposed.
- [ ] No alias chain proposed.
- [ ] Every new token has multiple-consumer or true component justification.
- [ ] Unique geometry kept local and documented.
- [ ] Physical padding/margin properties used.
- [ ] Logical padding/margin/inset properties absent.
- [ ] Base `.container` reused.
- [ ] Section owns its external rhythm.
- [ ] Internal parent owns sibling gaps.

**On violation:** `STYLE SCALE GATE — FAIL` · `TOKEN ADMISSION GATE — FAIL` · `SCSS AUTHORIZATION — DENIED`

### One SCSS file gate (mandatory)

- [ ] The existing `src/scss/style.scss` was inspected.
- [ ] All project styles will be added to `style.scss`.
- [ ] No new project SCSS partial is planned.
- [ ] No new project `@use` / `@import` / `@forward` is planned.
- [ ] `--radius-main` is used for standard rounding.
- [ ] `--radius-full` is used only for circles/pills.
- [ ] `--radius-small` / `--radius-medium` / `--radius-large` are absent.
- [ ] `--button-letter-spacing` is absent.
- [ ] Button `letter-spacing` is not being introduced.
- [ ] Cascade placement is defined before implementation.

**Authority:** [one-project-scss-file-law-v1.md](one-project-scss-file-law-v1.md) · [no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md)

**On violation:** `ONE SCSS FILE GATE — FAIL` · `RADIUS SYSTEM GATE — FAIL` · `SCSS AUTHORIZATION — DENIED`

### Universal button system gate (mandatory)

- [ ] Existing `.btn` system inspected.
- [ ] Every new CTA uses `.btn`.
- [ ] Required modifiers identified.
- [ ] Block-specific class controls placement only.
- [ ] No parallel button system is proposed.
- [ ] No selector-specific button token is proposed.
- [ ] No button letter-spacing is proposed.
- [ ] Button/link semantic element is correct.
- [ ] Focus-visible state is preserved.
- [ ] Disabled state is defined where applicable.

**Authority:** [universal-button-system-law-v1.md](universal-button-system-law-v1.md) · [no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md)

**On violation:** `UNIVERSAL BUTTON SYSTEM GATE — FAIL` · `SCSS AUTHORIZATION — DENIED`

### Token lookup gate (mandatory)

- [ ] All design values completed token lookup.
- [ ] Reused variables listed.
- [ ] New token proposals listed.
- [ ] Exact exceptions listed.
- [ ] Technical values listed.
- [ ] Arbitrary values count = **0**.
- [ ] Hidden fallback literals count = **0**.
- [ ] Repeated unregistered values count = **0**.

**On violation:** `SCSS GATE — FAIL`

### Container gate (mandatory)

- [ ] Base `.container` (or project primary container class) reused where applicable.
- [ ] No duplicate component container geometry (`max-width` + horizontal centering + horizontal padding outside primary container owner).
- [ ] No new container token without approved visual exception.

**On violation:** `CONTAINER GATE — FAIL` · `SCSS AUTHORIZATION — DENIED`

### Section rhythm gate (mandatory)

- [ ] Section/layout region owns top and bottom rhythm.
- [ ] First internal child does not simulate section top spacing.
- [ ] Last internal child does not simulate section bottom spacing.
- [ ] Parent owns spacing between siblings.
- [ ] Internal padding is not used as a section-boundary workaround.

**On violation:** `SECTION RHYTHM GATE — FAIL` · `SCSS AUTHORIZATION — DENIED`

### Operator source gate (mandatory)

- [ ] Current `src` inspected (read files — do not assume from specs).
- [ ] Operator modifications identified and protected.
- [ ] No previous artefact will overwrite current `src`.
- [ ] Planned edits are minimal and local.

**Authority:** [operator-canonical-source-law-v1.md](operator-canonical-source-law-v1.md)

**On violation:** `OPERATOR SOURCE AUTHORITY GATE — FAIL` · `IMPLEMENTATION DENIED`

### Font delivery gate (mandatory when production font is Inter or custom webfont)

- [ ] Local WOFF2 files exist under `src/fonts/` for each used weight.
- [ ] `@font-face` in `src/scss/style.scss` with `font-display: block` when operator requires zero visible font switch.
- [ ] Critical above-fold weights preloaded in `<head>` before main stylesheet.
- [ ] Google Fonts / external font CSS links absent from production HTML.
- [ ] Only required weights included (no 600/700 unless used).
- [ ] Font provenance documented.
- [ ] Operator visual font confirmation pending — do not claim APPROVED from automated CLS alone.

**Authority:** [font-and-layout-stability-law-v1.md](font-and-layout-stability-law-v1.md)

**On violation:** `FONT STABILITY GATE — FAIL` · `SCSS AUTHORIZATION — DENIED`

### Design value freeze gate (mandatory when freeze ACTIVE)

- [ ] No new spacing, dimension, font, color, button, or radius values proposed.
- [ ] Every changed value is operator-authored or exception-approved.

**Authority:** [no-new-design-values-after-operator-calibration-law-v1.md](no-new-design-values-after-operator-calibration-law-v1.md)

**On violation:** `DESIGN VALUE FREEZE GATE — FAIL`

### HTML quality gate (mandatory)

- [ ] `data-safe-unknown` absent in production HTML.
- [ ] Visible text uses semantic case; uppercase via CSS `text-transform`.
- [ ] Official acronyms preserved.

**Authority:** [no-production-safe-unknown-attribute-law-v1.md](no-production-safe-unknown-attribute-law-v1.md) · [semantic-text-casing-law-v1.md](semantic-text-casing-law-v1.md)

### JS hook gate (mandatory when JS present)

- [ ] Behavior selectors use `data-*`; no unused hooks.

**Authority:** [data-attribute-js-hook-law-v1.md](data-attribute-js-hook-law-v1.md)

### Font stability gate (mandatory on stability tasks)

- [ ] Font delivery audited; critical weights limited; dimensions reserved for icons/images.

**Authority:** [font-and-layout-stability-law-v1.md](font-and-layout-stability-law-v1.md)

---

## REPORT line

```text
PRE-SCSS VALIDATION — PASS | FAIL (list #) | BLOCKED (gate)
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Created from cross-layer audit |
| 2026-06-22 | v1.1 — CSS Variable First Law token lookup gate; SCSS GATE — FAIL on arbitrary values |
| 2026-06-22 | v1.2 — Container gate + Section rhythm gate |
| 2026-06-23 | v1.3 — Style scale gate; Token admission gate; physical property rule; Universal Style Scale Law |
| 2026-06-23 | v1.4 — One SCSS file gate; unified radius; no button letter-spacing |
| 2026-06-23 | v1.5 — Universal Button System gate |
| 2026-06-23 | v1.6 — Font delivery gate; local WOFF2 default; operator visual font gate (FP-0002) |
| 2026-06-23 | v1.7 — **Analysis-before-implementation:** after operator rejection, checklist item 2 (`scss_authorized`) remains **false** until clean audit approved |
