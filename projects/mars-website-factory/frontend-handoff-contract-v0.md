# MARS Website Factory — Frontend Handoff Contract v0

**Status:** **documented** — human-readable **frontend production input** contract. **Not** a JSON Schema, **not** runtime validation, **not** a claim that **Gulp Frontend Agent** or any build runs automatically in this repository.

---

## Purpose

- Converts an **approved blueprint** and **approved design direction** (see [Design Handoff Contract v0](design-handoff-contract-v0.md)) into **actionable frontend production requirements** for static implementation.
- Prepares work for the **Gulp Frontend Agent** (documented as **legacy-bridge** / planned specialist; see [frontend-production-model.md](frontend-production-model.md), [agents/registry.md](../../agents/registry.md)) so HTML/SCSS/JS can be produced with fewer clarification loops.
- Aligns with **gulp-starter–style** static architecture: **`src`** partials, compiled output, modular SCSS, data-attribute hooks — as **target** shape ([frontend-production-model.md](frontend-production-model.md)); the repo does **not** assert a `gulp-starter` folder exists (**SAFE UNKNOWN** if absent).
- Does **not** imply **CMS**, **server runtime**, **API-backed** pages, or **live** content integration in v0 — those are out of scope unless a separate integration contract exists.

---

## Relation to Gulp Frontend Agent

The **Gulp Frontend Agent** consumes this handoff as **requirements**: **`section_map`** → includes/partials; **`SCSS_mapping`** → partial graph; **`JS_requirements`** → scoped behaviors. v0 does **not** define agent prompts, CLI entrypoints, or CI jobs.

---

## Relation to Block Registry

[Block Registry v0](block-registry-v0.md) supplies canonical **`block_id`** values. **`section_map`** and **`partials_mapping`** should reference **`block_id`** (and optional instance labels) consistently with the blueprint and design **`section_visual_map`**. Do **not** introduce new section semantics without a registry mapping or an explicit **SAFE_UNKNOWN_notes** record.

---

## Relation to Frontend Production Rules

[Frontend Production Rules](registries.md#6-frontend-production-rules) (planned module in [registries.md](registries.md)) govern **src-first** workflow, **forbidden** manual **`dist`** edits, JS scope, and include conventions. This contract’s **`forbidden_patterns`**, **`performance_requirements`**, and **`integration_notes`** must stay **compatible** with those rules where they exist.

---

## Relation to Frontend QA Agent

**Frontend QA Agent** (planned; [qa-validation-model.md](qa-validation-model.md)) uses **`QA_requirements`**, **`accessibility_requirements`**, **`performance_requirements`**, and **`SEO_markup_requirements`** as acceptance-oriented input. Build success and path checks remain in [frontend-production-model.md](frontend-production-model.md).

---

## Source-first / dist-not-edited rule

All implementation work targets **source files** under the project’s agreed tree (e.g. **`src/`**). **Do not** hand-edit generated **`dist/`** (or equivalent build output) to “fix” production issues — fix **sources** and rebuild. Record the agreed output dir in **integration_notes** if non-default.

---

## Modular SCSS and no unsafe global CSS

- **Modular SCSS:** section/block partials import shared tokens/variables; avoid monolithic single-file dumps unless project policy explicitly allows.
- **No unsafe global CSS:** avoid unscoped element resets that stomp third-party widgets without review; new global selectors or **`!important`** waves require explicit sign-off in **HITL_required** / **notes**.

---

## Data-attribute JS hooks

Prefer **`data-*`** hooks (e.g. **`data-component="accordion"`**) for behavior binding instead of ad-hoc **`#id`** soup or undocumented **`window.*`** globals. **`data_attribute_hooks`** lists required hooks per interactive region.

---

## No fake CMS claim

This contract describes **static** page assembly and **build-time** includes. It does **not** claim WordPress, headless CMS, or preview webhooks unless **`integration_notes`** documents a **real** integration with owner and URL — otherwise state **SAFE UNKNOWN** or **`n/a`**.

---

## Non-runtime boundary

This contract is **documentation** for humans and future agents. It is **not** a MARS runtime artifact, **not** an enforced API, and **not** evidence of automated deployment.

---

## Required fields (v0)

Each frontend handoff is a **logical document** (one instance per page or canonical variant). Fields are **required** unless marked optional. Use **`n/a`** only when inapplicable **and** explained in **SAFE_UNKNOWN_notes**.

| Field | Role |
|--------|------|
| **frontend_handoff_id** | Stable ID for this handoff instance. |
| **source_blueprint_id** | **`blueprint_id`** from [Page Blueprint Contract v0](page-blueprint-contract-v0.md). |
| **source_design_handoff_id** | **`design_handoff_id`** from [Design Handoff Contract v0](design-handoff-contract-v0.md); use **`n/a`** only if design is merged into this doc with rationale (exceptional). |
| **target_stack** | e.g. `gulp-static`, `html-includes-scss-vanilla` — align with project reality, not aspirational frameworks. |
| **page_slug** | URL path segment or file stem for build entry (e.g. `roof-inspection-moscow`). |
| **page_type** | Echo **`site_type_id`** or more specific template name (`service_landing`, etc.). |
| **section_map** | Ordered list of **`block_id`** → partial/include path or logical component name under **`src`**. |
| **partials_mapping** | How blocks map to **`gulp-file-include`** (or equivalent) partials; nesting rules. |
| **SCSS_mapping** | SCSS partial paths per block/section; shared variables/mixins entry. |
| **JS_requirements** | Behaviors per page: accordion, form validation hook, sticky CTA — **deps** (vanilla vs lib) in prose. |
| **data_attribute_hooks** | Required **`data-*`** attributes and expected JS ownership (module or entry file). |
| **responsive_rules** | Breakpoints, mobile-first notes, exceptions vs [Design Handoff](design-handoff-contract-v0.md) **`responsive_behavior`**. |
| **asset_requirements** | Paths under **`src`/assets**, lazy rules, picture/srcset intent. |
| **form_behavior** | Client-side validation level, success state, analytics hooks (**no** PII in logs without policy). |
| **accessibility_requirements** | Landmarks, labels, live regions, focus management — links to blueprint/design a11y notes. |
| **performance_requirements** | LCP element, lazy embeds, CSS/JS budget hints (**heuristic** unless tooling assigned). |
| **SEO_markup_requirements** | Single H1, meta/canonical placeholders, JSON-LD **only** if content honest per blueprint. |
| **integration_notes** | Analytics IDs, third-party embeds, **no** fake CMS — or **`n/a`**. |
| **forbidden_patterns** | e.g. inline critical one-off styles for whole sections; editing **`dist`**; undeclared globals. |
| **QA_requirements** | Frontend-specific checks (links, build, viewport spot list). |
| **HITL_required** | `rare` \| `selective` \| `often` \| `yes` — before merge or publish. |
| **SAFE_UNKNOWN_notes** | Build command version, exact `src` root, CDN policy gaps. |

---

## Example — `service_landing` frontend handoff (gulp-starter–aligned)

| Field | Example value |
|--------|----------------|
| **frontend_handoff_id** | `fh_svc_roof_inspection_moscow_v1` |
| **source_blueprint_id** | `svc_roof_inspection_moscow_v1` |
| **source_design_handoff_id** | `dh_svc_roof_inspection_moscow_v1` |
| **target_stack** | `gulp-static` (Gulp 4 + gulp-file-include + Dart Sass) |
| **page_slug** | `roof-inspection-moscow` |
| **page_type** | `service_landing` |
| **section_map** | `hero` → `src/partials/sections/hero-service.html`; `trust_block` → `.../trust-icons.html`; `process_steps` → `.../process-horizontal.html`; `faq` → `.../faq-accordion.html`; `lead_form` → `.../lead-form-short.html`; `final_cta` → `.../final-cta.html`; `sticky_cta` → `.../sticky-cta-mobile.html` (include only on mobile via build flag or duplicate block with visibility classes per **Frontend Production Rules**). |
| **partials_mapping** | Page shell `src/pages/roof-inspection-moscow.html` includes sections in blueprint order; each section partial may include atoms from `src/partials/atoms/`. |
| **SCSS_mapping** | Page pulls `src/scss/pages/_roof-inspection.scss` aggregating `@use` of `.../sections/_hero-service`, `_faq-accordion`, `_lead-form`, `_sticky-cta`; shared tokens `src/scss/_tokens.scss`. |
| **JS_requirements** | Accordion keyboard support; **sticky_cta** show/hide on scroll (throttled); **lead_form** client-side required-field hints only — server submit **n/a** for static demo. |
| **data_attribute_hooks** | `[data-component="faq-accordion"]` on **faq** root; `[data-component="sticky-cta"]` on sticky bar; `[data-form="lead-short"]` on form for validation script. |
| **responsive_rules** | Mobile-first; **sticky_cta** active max-width 767px; **process_steps** switches to vertical stack below 900px. |
| **asset_requirements** | Hero `src/img/services/roof-hero.webp` + fallback JPG; lazy below-fold case images. |
| **form_behavior** | HTML5 `required` + inline error regions; success: replace form with thank-you partial (static content). |
| **accessibility_requirements** | One **`main`**; accordion buttons with `aria-expanded`; form errors with `role="alert"` on submit. |
| **performance_requirements** | Hero LCP image preload in `<head>` for this page only; defer non-critical JS; no third-party font loading without subset plan. |
| **SEO_markup_requirements** | Title/description copy slots match blueprint; FAQ schema only if FAQ partial renders full Q&A text. |
| **integration_notes** | Placeholder GA4 `data-analytics` attributes; **no** CMS — content is static includes. |
| **forbidden_patterns** | No hand patches under `dist/`; no new `window.*` without tech lead note in **SAFE_UNKNOWN_notes** if experimental. |
| **QA_requirements** | `gulp build` clean; link checker on internal anchors; spot-check 375 / 768 / 1280; tel: links valid. |
| **HITL_required** | `selective` — legal copy in form footer. |
| **SAFE_UNKNOWN_notes** | Exact repo path for `gulp-starter` clone **unknown** in this monorepo; CI job name **TBD**. |

---

*Contract version: v0 — documentation only; last updated 2026-05-11.*
