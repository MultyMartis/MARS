# Website Factory Universal Button System Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**  
**Scope:** All Website Factory execution cases; Gulp Frontend Agent; block specifications; SCSS production; visual QA; Cursor frontend prompts.  
**Not:** runtime linter, Stylelint config, or CI job (unless project adopts separately).

---

## Core law

All Website Factory buttons and button-like links use **one shared system**.

**Required base class:** `.btn`

**Allowed standard modifiers:**

- `.btn_dark`
- `.btn--primary`

Modifiers may be combined.

Block-specific classes may control **placement only**. They must **not** recreate button geometry or interaction styles.

---

## Element law

`.btn` may be used on `<button>`, `<a>`, and submit controls (`<button type="submit">`, `<input type="submit">` when approved).

Semantic element choice depends on behavior:

| Behavior | Element |
|----------|---------|
| Navigation | `<a href="…">` |
| Interface action | `<button type="button">` |
| Form submission | `<button type="submit">` or approved submit control |

---

## Base / modifier responsibility

### `.btn`

Owns: geometry, alignment, padding, height, border, radius, typography base, transition, basic interaction, icon gap.

### `.btn_dark`

Owns: dark background, dark border, light text, inverse hover.

### `.btn--primary`

Owns: accent primary behavior (including `.btn--primary.btn:hover` accent fill).

When combined with `.btn_dark`, filled accent at rest is permitted for primary CTA variants documented in block specifications.

### Block-specific class

Owns **only**: placement, local layout, justified width exception, positioning, block-level typography exceptions (e.g. compact label `font-size` — not height/padding/radius).

---

## Required universal tokens

In project `:root`:

| Role | Token |
|------|-------|
| Horizontal button padding | `--pad-btns` |
| Main button height | `--main-size-btns` |
| Minimal icon gap | `--pad-gap-mini` (reuse) |
| Full radius (pills) | `--radius-full` (reuse) |

Color roles: use project-approved color tokens (`--color-text-primary`, `--color-text-inverse`, `--color-accent`, `--color-surface`, etc.) — do **not** create selector-specific button color tokens.

---

## Prohibitions

- Separate Header / Hero / Footer button systems
- Selector-specific button tokens (`--header-button-*`, `--hero-button-*`, `--footer-button-*`)
- Fixed widths without evidence
- Button `letter-spacing` ([no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md))
- Custom radius outside `--radius-full` for buttons
- Deep specificity or `!important`
- Duplicated hover logic in block selectors
- `<div>` styled as button
- `<a href="#">` as fake action
- `<button>` without `type` inside forms
- Parallel legacy systems (`.button`, `.button--primary`, block-local button geometry)

---

## Accessibility

- `:focus-visible` — accessible outline; never `outline: none` without replacement
- `:disabled` and `[aria-disabled="true"]` — `cursor: not-allowed`, `pointer-events: none`, shared opacity
- Icons inherit via `currentColor`; SVG `fill: currentColor` when compatible

---

## SCSS placement

All button system styles live in **`src/scss/style.scss`** only ([one-project-scss-file-law-v1.md](one-project-scss-file-law-v1.md)).

---

## Cross-links

| Layer | Document |
|-------|----------|
| Pre-SCSS gate | [frontend-pre-scss-validation-checklist-v1.md](frontend-pre-scss-validation-checklist-v1.md) |
| Block spec | [block-implementation-specification-contract-v1.md](block-implementation-specification-contract-v1.md) |
| Visual QA | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) |
| Production rules | [frontend-production-rules-v0.md](frontend-production-rules-v0.md) |
| Style scale | [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md) |
| One SCSS file | [one-project-scss-file-law-v1.md](one-project-scss-file-law-v1.md) |
| Letter spacing | [no-button-letter-spacing-law-v1.md](no-button-letter-spacing-law-v1.md) |
| Foundation | [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — Universal Button System Law; FP-0002 V6 normalization authority |
