# MARS Website Factory — Frontend Prompt Discipline v0

**Status:** **documentation only** — discipline rules for **frontend execution prompts** in the factory’s Gulp-oriented static model. **Not** a code generator, **not** a build runner, **not** evidence that any frontend codegen pipeline exists today.

**Version:** v0.

**Related:** [frontend-production-model.md](frontend-production-model.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [section-payload-model-v0.md](section-payload-model-v0.md), [block-registry-v0.md](block-registry-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md), [`../../agents/frontend-gulp-agent/README.md`](../../agents/frontend-gulp-agent/README.md) (Gulp Frontend Agent operational doc pack), [`../../agents/mars-forge/semantic-source-lock.md`](../../agents/mars-forge/semantic-source-lock.md) (when **MARS Forge** overlay applies).

**RU commercial landings:** use [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md); typography authority [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md). **Anti-drift invariants:** [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md).

---

## 1. Purpose

Frontend production in the factory follows a **Gulp-oriented, source-first** static model ([frontend-production-model.md](frontend-production-model.md)). The **Gulp Frontend Agent** is **`operational_doc_pack`** in the registry — documentation-backed specialist pack, human + Cursor/Codex, **not** in-repo code or autonomous runtime ([agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md)).

This document defines the **prompt discipline** that applies whenever a factory prompt instructs **frontend implementation work** — whether executed by a human in Cursor or, eventually, by a planned specialist agent.

---

## 2. Scope of frontend prompts

A frontend prompt is one whose `artifacts out` lands under the project’s frontend source tree (e.g. `src/...`) and references the **Frontend Handoff Contract v0** ([frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md)).

In scope:

- section / block partials,
- SCSS partials and shared tokens,
- scoped JS modules and entry scripts,
- asset references and lazy loading,
- responsive rules and a11y markup,
- build configuration **only** when the prompt explicitly targets it.

Out of scope (default):

- generated `dist/*`,
- CI provisioning,
- deploy pipelines,
- runtime services,
- CMS / backend bindings.

---

## 3. Frontend execution prompts (structure)

A frontend execution prompt extends [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) §3.5 with the following required anchors:

| Section | Frontend-specific content |
|---------|----------------------------|
| `context` | Stage anchor (`WF_V0_S11_FRONTEND_PRODUCTION`), page slug, section/block id. |
| `artifacts in` | `frontend_handoff_id` (+ design baseline) per [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md). |
| `target_stack` | Echoed from handoff (e.g. `gulp-static`); no aspirational frameworks. |
| `scope.in` | Source paths under `src/...`. |
| `scope.out` | `dist/*`, neighboring sections, global resets. |
| `constraints` | Source-first; modular SCSS; data-attribute hooks; no undeclared globals. |
| `forbidden_patterns` | Echoed from handoff. |
| `QA_requirements` | Echoed from handoff. |
| `SAFE_UNKNOWN_notes` | CI job name, exact build command, hosting target, etc. |
| `reporting requirements` | Frontend implementation REPORT per [reporting-standard-v0.md](reporting-standard-v0.md) §4.2. |

---

## 3a. MARS Forge overlay — semantic source charter (when selected)

When the operator routes work under **`mars_forge_frontend_agent`** (Forge discipline), frontend prompts **must additionally** satisfy the charter in [`../../agents/mars-forge/semantic-source-lock.md`](../../agents/mars-forge/semantic-source-lock.md) §1:

- **Active design version** and **canonical visual source path**.
- **Forbidden** design paths / versions.
- **`shared-assets` path** (if used) — **assets only**, never structural SoT (see that doc §3).
- **Workspace / target path** for implementation.

If the prompt omits these, the executor stops and reports **SAFE UNKNOWN** rather than guessing from archives, old PDFs, or unstated mockup folders.

---

## 3b. V5 / frontend prompt invariant block (reusable)

When scope is Triumph V5 lane or similar Gulp static frontend work, paste into `constraints` or `forbidden_patterns`:

```text
Project invariants:
- Main breakpoint: 1024/1025.
- Do not invent 980/981 breakpoints.
- Desktop: 1025px+.
- Tablet/mobile: max-width 1024px.
- Keep split layouts inside existing section-shell/content container.
- Do not use &nbsp; between long words in headings.
- For native <details>, open is the single source of truth.
- If build fails, dist is stale; do not claim success.
- Do not touch forms unless explicitly requested.
```

Full rule prose: [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md).

### Factory operator-canonical invariant block (2026-06-23)

Paste into `constraints` for any Website Factory frontend task after operator manual calibration:

```text
Current src is operator-canonical.
Do not overwrite manual changes.
Do not invent new design values.
Do not use data-safe-unknown in production HTML.
Write visible HTML text in semantic normal case.
Use CSS text-transform for uppercase presentation.
Use data-* attributes for JS behavior hooks.
Prevent FOUT, FOIT and layout shifts.
Serve production fonts as local WOFF2 with preload and font-display:block when operator requires zero visible font switch.
Do not use Google Fonts + swap and claim zero FOUT while operator still sees a font switch.
```

Authority: [operator-canonical-source-law-v1.md](operator-canonical-source-law-v1.md) · [no-new-design-values-after-operator-calibration-law-v1.md](no-new-design-values-after-operator-calibration-law-v1.md) · [no-production-safe-unknown-attribute-law-v1.md](no-production-safe-unknown-attribute-law-v1.md) · [semantic-text-casing-law-v1.md](semantic-text-casing-law-v1.md) · [data-attribute-js-hook-law-v1.md](data-attribute-js-hook-law-v1.md) · [font-and-layout-stability-law-v1.md](font-and-layout-stability-law-v1.md).

---

## 4. Section implementation prompts

A section implementation prompt is the most common frontend prompt. It targets **one block_id** ([block-registry-v0.md](block-registry-v0.md)) on **one page_slug**.

Discipline:

- one block per prompt (not “all blocks on the page”);
- references `section_map` and `partials_mapping` rows from the handoff;
- produces one HTML partial + matching styles in `src/scss/style.scss` + (optional) scoped JS module;
- does **not** modify atoms / shared tokens unless the prompt explicitly targets them;
- emits **STRUCTURE CHANGE** if the section requires new tokens or shared components.

---

## 5. SCSS discipline

Per [frontend-production-model.md](frontend-production-model.md) and [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md):

| Rule | Detail |
|------|--------|
| **Modular SCSS** | Section/block partials per component; shared tokens in a dedicated entry. |
| **No monolithic dumps** | Avoid single-file mega-sheets unless project policy explicitly allows. |
| **Tokens via shared entry** | New tokens introduced under shared variables; never inline arbitrary hex/px buried in a section partial. |
| **Universal Style Scale** | Consume compact `--pad-*` / role-based radius — no selector-named spacing aliases; no alias chains; physical padding/margin properties — [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md). |
| **No `!important` waves** | A handful of justified instances, never used to “fix” cascade issues without review. |
| **No global resets** | Element-level resets only via the agreed shared reset partial; never per-section. |
| **Naming** | Block-aligned BEM-ish or project convention; consistent with handoff `SCSS_mapping`. |
| **Mobile-first** | Breakpoints per design tokens; min-width media queries; document any max-width usage in **SAFE_UNKNOWN_notes** if non-default. |

---

## 6. Modularity

| Rule | Detail |
|------|--------|
| One block, one HTML partial. | Page entry assembles partials in blueprint order. |
| One block, styles in `src/scss/style.scss` (no new project partials). | No cross-block selectors. |
| Atoms (button, badge, icon) live under `src/partials/atoms/`. | Shared imports only. |
| Page-level aggregation under `src/pages/<slug>.html`. | Page styles appended to `src/scss/style.scss` in cascade order. |
| No inline JavaScript in HTML partials. | Behavior via scoped JS modules anchored on data-attributes. |
| No inline `<style>` blocks. | Styles always live in `src/scss/style.scss`. |

---

## 7. No unsafe globals

| Rule | Detail |
|------|--------|
| **No new `window.*`** without explicit note in **SAFE_UNKNOWN_notes** or HITL_required entry. |
| **No global selectors** that affect third-party widgets without review. |
| **No global JS state** — scope by module / IIFE / class instance bound via `data-*` attribute. |
| **No global event handlers** without explicit hook in handoff `JS_requirements`. |
| **No undeclared dependencies** — every used library appears in the handoff or in the project’s build config. |

---

## 8. Source-first rule

Per [frontend-production-model.md](frontend-production-model.md) §“Honesty” and [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) §“Source-first / dist-not-edited rule”:

- All implementation work targets **`src/...`** (or the project-agreed equivalent).
- **Never** hand-edit `dist/...` to “fix” production output; fix sources and rebuild.
- The agreed output dir, if non-default, is recorded in `integration_notes` of the handoff and echoed in the prompt.

A REPORT that lists `dist/*` paths under **Updated files** is a **violation** unless the prompt explicitly targets the output dir (rare).

---

## 9. No dist editing

Concrete forbidden actions:

- patching `dist/*.html`,
- patching `dist/*.css`,
- patching `dist/*.js`,
- running search-and-replace across `dist/`,
- committing `dist/` content as a “fix”.

If a downstream consumer (preview environment, CDN, archive) needs a `dist/` snapshot, that is a **delivery** concern (S15) and follows a separate prompt with explicit packaging steps — **not** an edit prompt.

---

## 10. Data-* JS philosophy

Per [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md) §“Data-attribute JS hooks” and the legacy Gulp profile referenced in [frontend-production-model.md](frontend-production-model.md):

| Rule | Detail |
|------|--------|
| Use `data-component="<name>"` (or project convention) as the **primary** binding point. |
| Use `data-*` instance modifiers for variants (e.g. `data-component="faq-accordion" data-variant="compact"`). |
| Do **not** rely on `#id` soup for behavior binding. |
| Modules **own** their data-attributes — do not bind two unrelated behaviors to one attribute. |
| The handoff’s `data_attribute_hooks` list is **canonical**; new hooks require an updated handoff (mutable until S11) or a **STRUCTURE CHANGE**. |
| JS modules must be **idempotent**: re-initialization on the same element does not double-bind. |

---

## 11. Reusable section philosophy

The Block Registry v0 ([block-registry-v0.md](block-registry-v0.md)) supplies canonical `block_id`s. Sections that recur across pages share **the same partial** and **the same SCSS partial**, parameterized through includes / data attributes — not duplicated.

Rules:

- A new block proposed by a section prompt requires a **registry mapping** ([block-registry-v0.md](block-registry-v0.md)) or **SAFE_UNKNOWN_notes** entry.
- Reusable sections live under `src/partials/sections/` (or project-agreed path).
- Per-page customizations are expressed through:
  - include parameters (e.g. via `gulp-file-include` arguments),
  - data attributes,
  - SCSS modifier classes that align with the section partial.
- Duplicating a section to “tweak it” is **forbidden** — extend the partial or propose a registry-aligned variant.

---

## 12. Responsive expectations

- **Mobile-first** per design tokens.
- **Breakpoints** documented in the handoff `responsive_rules` field.
- **QA viewports** typically 375 / 768 / 1280 (project-adjustable) per Frontend QA lane ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §11.4) — **supplementary generic responsive validation only.**
- **RU commercial landings:** use [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) (mandatory widths + typography checks).
- **Sticky / off-canvas** behaviors clearly bounded by viewport range.
- **Print styles** out of scope by default; require explicit prompt.

---

## 13. QA expectations

Frontend prompts produce artifacts that face **Frontend QA** (S12). The execution prompt should anticipate:

- **Build success** — local `gulp build` (or agreed task) result captured in the REPORT;
- **Markup semantics** — single H1, landmark elements, heading order;
- **Responsive spot-checks** — viewports per project; **RU commercial:** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) + `RU TYPOGRAPHY / NO WORD-SPLITTING` REPORT line;
- **Link / asset paths** — relative paths resolve in the build output;
- **A11y heuristics** — focus management, ARIA labels for interactive elements, color contrast intent;
- **Performance heuristics** — LCP element discipline, lazy below-fold assets, deferred non-critical JS;
- **JS scope** — no leaks into `window.*` beyond declared hooks.

CI assertions remain **SAFE UNKNOWN** unless the prompt cites in-repo CI evidence ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md) §8).

---

## 14. Tie to Gulp Frontend Agent

The **Gulp Frontend Agent** ([agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md)) is the **planned** specialist for this lane and the **documented** consumer of the [Frontend Handoff Contract v0](frontend-handoff-contract-v0.md). Phase 1 reality:

- Frontend prompts are **human-executed in Cursor** ([cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [`../../governance/execution-model.md`](../../governance/execution-model.md)).
- The Gulp Frontend Agent profile gives the **prompt discipline a target shape**; it does **not** prove that an agent runs builds today.
- Any future runtime binding goes through the **Execution Bridge** ([`../../mars-runtime/execution-bridge-v0.md`](../../mars-runtime/execution-bridge-v0.md)) — **SAFE UNKNOWN** until evidenced.

---

## 15. Non-claims (explicit)

This discipline does **not** claim:

- a frontend code-generation pipeline already exists in this repo;
- Cursor runs `gulp build` automatically without user action;
- a CI configuration is provisioned;
- a deployment pipeline is wired;
- the Gulp Frontend Agent is implemented;
- Validator runs on the frontend artifact automatically.

What it **does** claim:

- prompts that touch frontend source **must** follow these discipline rules;
- violations are visible in the REPORT;
- QA and HITL gates remain authoritative;
- SAFE UNKNOWN applies anywhere implementation evidence is missing.

---

## 16. Anti-patterns

| Anti-pattern | Why forbidden | Honest alternative |
|--------------|---------------|---------------------|
| “Generate the whole page with all sections.” | Breaks one-block-per-prompt; risk of fabricated tokens/sections. | One block per prompt; assemble at page level after sections are approved. |
| Adding tokens inside a section partial | Breaks shared-token model. | Introduce tokens via shared entry; reference from section partial. |
| Patching `dist/` to ship | Violates §9. | Fix source, rebuild, capture build in REPORT. |
| Inlining JS handlers in HTML | Violates §6 / §10. | Use scoped module bound via data-component. |
| Adding new `window.*` silently | Violates §7. | Declare in `SAFE_UNKNOWN_notes` or refactor to scoped module. |
| Claiming “build green” without running it | Violates §13 / [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md). | Run build or emit SAFE UNKNOWN on build. |
| “Tested in all browsers” without evidence | Fabrication. | Enumerate viewports actually tested or SAFE UNKNOWN. |
| Implementing from archive / older `design/v*` screens when charter names another active path | Triumph-class **semantic drift** (wrong entity count, wrong section meaning). | State active path in prompt; obey [`mars-forge/semantic-source-lock.md`](../../agents/mars-forge/semantic-source-lock.md) §2–§3 §8 — **P0–P6** priority. |

---

## 17. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial frontend prompt discipline (documentation only). |
| 2026-05-16 | **§3a** — Forge overlay semantic charter pointer; Related + anti-pattern for cross-version drift. |
| 2026-05-24 | **§3b** — reusable V5/frontend prompt invariant block; link [frontend-production-invariants-v1.md](frontend-production-invariants-v1.md). |
