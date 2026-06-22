# Frontend rules — Gulp-oriented static model

Rules apply to **target project source** (external/local gulp-starter or equivalent), not to files inside this MARS doc pack.

## Source and output

- **Source-first:** implement under the project’s agreed **`src/`** (or documented equivalent). All durable fixes live in source.
- **No manual `dist/` edits:** never patch compiled HTML/CSS/JS in output folders; rebuild from source ([`frontend-handoff-contract-v0.md`](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)).

## HTML composition

- **gulp-file-include** (or project-equivalent): assemble pages from partials per handoff **`section_map`** / **`partials_mapping`**.
- **`@@include` safety:** only include trusted partial paths; avoid user-controlled include parameters; keep include graph understandable (no deep accidental cycles).
- **Semantic HTML:** meaningful headings order, landmarks (`header`, `main`, `nav`, `footer` as appropriate), buttons vs links used correctly.
- **SEO-safe markup:** single logical H1 per page context; honest meta/copy slots; structured data only when content is actually rendered.
- **No inline JS:** behavior in modules/entry scripts; exceptions only if handoff explicitly allows and HITL acknowledges.
- **No inline CSS:** avoid `style=""` for whole sections; scoped SCSS partials instead.

## SCSS

- **Modular SCSS:** section/block partials; shared tokens/mixins in dedicated files; avoid monolithic dumps unless project policy says otherwise.
- **Universal Style Scale Law (mandatory):** compact role-named spacing/radius primitives (`--pad-*`, `--radius-full`) — **no** selector-specific spacing tokens (`--footer-*`, `--header-*` for primitive scale); **no** one-block alias chains; **physical** `padding-top/right/bottom/left` — not logical `padding-block` / `padding-inline` by default. Authority: [universal-style-scale-law-v1.md](../../projects/mars-website-factory/universal-style-scale-law-v1.md) · [css-variable-first-law-v1.md](../../projects/mars-website-factory/css-variable-first-law-v1.md).
- **Reusable sections/components:** match HTML partial boundaries; naming aligned with project convention (e.g. kebab-case files).
- **Isolation:** prefer block-scoped selectors; avoid unscoped global resets that stomp third-party widgets without review.

## JavaScript

- **`data-*` hooks:** prefer e.g. `[data-component="…"]` for binding; separate **styling classes** from **behavior hooks** where practical.
- **No unsafe global pollution:** avoid new `window.*` without explicit review; prefer modules/IIFE patterns per project policy.
- **Progressive enhancement:** critical content usable without JS; document **SAFE UNKNOWN** if a third-party plugin forces globals.

## Layout and UX

- **Responsive discipline:** mobile-first unless handoff specifies otherwise; honor **`responsive_rules`** and design breakpoints.
- **Russian no word-splitting (mandatory for RU landings):** **Authority** [russian-no-word-splitting-typography-v1.md](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md); **QA preset** [ru-landing-qa-preset-v1.md](../../projects/mars-website-factory/ru-landing-qa-preset-v1.md). No mid-word breaks; fix overflow via layout before word-breaking CSS; do not duplicate full rules here.
- **Accessibility basics:** focus order, visible focus, accordion `aria-expanded` / `aria-controls`, form errors with appropriate roles when specified.
- **Assets discipline:** paths under agreed asset roots; lazy-loading rules per handoff; no invented CDN URLs.

## Library integration (when required)

- Add plugins only when needed; keep init in agreed entry (`main.js` or project equivalent); stable **`data-*`** hooks for modals/sliders/masks.
- **Anti-pattern:** mixing competing scroll owners (e.g. slider + manual `scrollBy`) in one block — one interaction owner.

---

**SAFE UNKNOWN:** exact folder names, SCSS `@use` vs `@import` policy, and JS bundler shape are **target-repo specific** — verify before editing.
