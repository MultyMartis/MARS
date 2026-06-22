# Website Factory One Project SCSS File Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**

**Scope:** All Website Factory execution cases; Gulp Frontend Agent; block specifications; SCSS production; visual QA; Cursor frontend prompts.

**Enforcement:** **DOCUMENTED MANDATORY GATE** — **AUTOMATED ENFORCEMENT — NOT YET IMPLEMENTED**

**Registry:** [website-factory-cross-layer-artefact-registry-v1.md](website-factory-cross-layer-artefact-registry-v1.md) · [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

**Related laws:**

- [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md) — compact `--radius-main` / `--radius-full` radius system
- [css-variable-first-law-v1.md](css-variable-first-law-v1.md) — token lookup before production values
- [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) — foundation variables live in the single entry file

---

## Core law

All **project-owned** SCSS must be maintained in **one file**:

```text
src/scss/style.scss
```

Frontend agents must **append and edit styles in that file**. They must **not** create section, component, layout, page, or responsive SCSS partials unless the operator explicitly authorizes a modular SCSS architecture.

---

## What must live in `style.scss`

- project font declarations
- project CSS variables (`:root`)
- reset
- base styles
- typography
- common utilities
- shared components
- Header
- Hero
- page sections
- Footer
- modal styles
- form styles
- responsive styles (when authorized)
- project-specific vendor overrides

Organize with prominent section comments in cascade order. See **Structure law** below.

---

## What may remain external

Do **not** copy into `style.scss`:

- Font Awesome vendor CSS
- external library CSS
- generated vendor bundles
- externally hosted fonts
- third-party source files
- licensed controlled shared assets

Vendor integration may remain a separate Gulp input or external dependency. **Project overrides** for vendor components must still live in `style.scss`.

---

## Prohibited project structure (default)

Unless operator exception is documented:

```text
src/scss/base/_root.scss
src/scss/base/_reset.scss
src/scss/base/_typography.scss
src/scss/components/_button.scss
src/scss/components/_icon.scss
src/scss/layout/_header.scss
src/scss/layout/_footer.scss
src/scss/sections/_hero.scss
src/scss/sections/_section-name.scss
src/scss/pages/_page-name.scss
```

Also prohibited for project-owned styles:

```scss
@use 'base/root';
@use 'layout/header';
@use 'sections/hero';
```

---

## Explicit exception

Modular SCSS architecture is allowed **only** with operator approval documented in the project passport or a scoped charter. Exception must contain:

- reason
- scope
- list of permitted files
- lifecycle / expiry
- operator approval reference

Without this:

```text
SCSS FILE ARCHITECTURE GATE — FAIL
ONE SCSS FILE GATE — FAIL
SCSS AUTHORIZATION — DENIED
```

---

## Structure law

Recommended section order (omit empty sections):

```text
01. Fonts
02. Variables
03. Reset
04. Base
05. Typography
06. Common utilities
07. Shared components
08. Header
09. Hero
10. Main sections
11. Footer
12. Modals
13. Responsive
```

Each major block uses a single prominent comment banner. Prefer flat BEM selectors; avoid deep nesting chains that hide final selectors. No duplicate selector blocks without documented reason (state, hover, media, contextual exception).

---

## Gulp entry

Single SCSS compile entry:

```text
src/scss/style.scss → dist/assets/css/style.css
```

No glob compilation of project partials. No multiple project SCSS entry points.

---

## Agent instructions (normative)

Before styling:

1. Open existing `src/scss/style.scss`.
2. Find the correct section.
3. Add styles there.
4. Do **not** create a new SCSS file.
5. Do **not** add `@use` / `@import` for project styles.
6. Preserve cascade order.
7. Use `--radius-main` or `--radius-full`.
8. Do **not** use `--button-letter-spacing`.
9. Use the universal `.btn` system for all CTAs ([universal-button-system-law-v1.md](universal-button-system-law-v1.md)).

---

## Prompt standard (mandatory snippet)

Every future frontend Cursor prompt must include:

```text
All project SCSS must be written in src/scss/style.scss.
Do not create SCSS partials.
Use --radius-main for standard rounding.
Use --radius-full for circles/pills.
Do not define or use --button-letter-spacing.
All CTAs use .btn with approved modifiers (.btn_dark, .btn--primary).
Block-specific classes control placement only — not button geometry.
```

---

## Production gates

| Gate | Document |
|------|----------|
| Pre-SCSS | [frontend-pre-scss-validation-checklist-v1.md](frontend-pre-scss-validation-checklist-v1.md) |
| Block spec | [block-implementation-specification-contract-v1.md](block-implementation-specification-contract-v1.md) |
| SCSS review | [frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md) |
| Visual QA | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) |
| Agent pack | [agents/frontend-gulp-agent/frontend-rules.md](../../agents/frontend-gulp-agent/frontend-rules.md) |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-23 | v1 — One Project SCSS File Law; FP-0002 V6 consolidation authority |
