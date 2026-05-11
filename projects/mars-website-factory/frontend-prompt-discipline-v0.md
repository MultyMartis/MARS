# MARS Website Factory — Frontend Prompt Discipline v0

**Status:** **documentation only** — discipline rules for **frontend execution prompts** in the factory’s Gulp-oriented static model. **Not** a code generator, **not** a build runner, **not** evidence that any frontend codegen pipeline exists today.

**Version:** v0.

**Related:** [frontend-production-model.md](frontend-production-model.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [section-payload-model-v0.md](section-payload-model-v0.md), [block-registry-v0.md](block-registry-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [agent-prompt-behavior-v0.md](agent-prompt-behavior-v0.md), [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [reporting-standard-v0.md](reporting-standard-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md).

---

## 1. Purpose

Frontend production in the factory follows a **Gulp-oriented, source-first** static model ([frontend-production-model.md](frontend-production-model.md)). The **Gulp Frontend Agent** is **legacy-bridge** in the registry — a **documented** specialist profile, **not** in-repo code ([agent-map.md](agent-map.md), [`../../agents/registry.md`](../../agents/registry.md)).

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

## 4. Section implementation prompts

A section implementation prompt is the most common frontend prompt. It targets **one block_id** ([block-registry-v0.md](block-registry-v0.md)) on **one page_slug**.

Discipline:

- one block per prompt (not “all blocks on the page”);
- references `section_map` and `partials_mapping` rows from the handoff;
- produces one HTML partial + matching SCSS partial + (optional) scoped JS module;
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
| **No `!important` waves** | A handful of justified instances, never used to “fix” cascade issues without review. |
| **No global resets** | Element-level resets only via the agreed shared reset partial; never per-section. |
| **Naming** | Block-aligned BEM-ish or project convention; consistent with handoff `SCSS_mapping`. |
| **Mobile-first** | Breakpoints per design tokens; min-width media queries; document any max-width usage in **SAFE_UNKNOWN_notes** if non-default. |

---

## 6. Modularity

| Rule | Detail |
|------|--------|
| One block, one HTML partial. | Page entry assembles partials in blueprint order. |
| One block, one SCSS partial (or grouped per project convention). | No cross-block selectors. |
| Atoms (button, badge, icon) live under `src/partials/atoms/`. | Shared imports only. |
| Page-level aggregation under `src/pages/<slug>.html`. | Page-level SCSS aggregator under `src/scss/pages/_<slug>.scss`. |
| No inline JavaScript in HTML partials. | Behavior via scoped JS modules anchored on data-attributes. |
| No inline `<style>` blocks. | Styles always live in SCSS partials. |

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
- **QA viewports** typically 375 / 768 / 1280 (project-adjustable) per Frontend QA lane ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md) §11.4).
- **Sticky / off-canvas** behaviors clearly bounded by viewport range.
- **Print styles** out of scope by default; require explicit prompt.

---

## 13. QA expectations

Frontend prompts produce artifacts that face **Frontend QA** (S12). The execution prompt should anticipate:

- **Build success** — local `gulp build` (or agreed task) result captured in the REPORT;
- **Markup semantics** — single H1, landmark elements, heading order;
- **Responsive spot-checks** — viewports per project;
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

---

## 17. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial frontend prompt discipline (documentation only). |
