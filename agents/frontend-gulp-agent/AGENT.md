# Agent definition — Gulp Frontend Agent

| Field | Value |
|--------|--------|
| **agent_id** | `gulp_frontend_agent` |
| **display_name** | Gulp Frontend Agent |
| **status** | `operational_doc_pack` |
| **implementation_status** | Human / Cursor-assisted execution — **not** an autonomous build agent |
| **parent_system** | `mars_website_factory` |
| **owner_layer** | Website Factory / Production Layer |

---

## Responsibilities

- Turn an approved **Frontend Handoff** ([`frontend-handoff-contract-v0.md`](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)) into **source-first** tasks: HTML partials, SCSS partials, scoped JS, assets as documented.
- **Protect** the target project’s gulp-starter-style **architecture** (includes, SCSS graph, JS entry pattern) — extend, do not silently redesign.
- **Guide** Cursor prompts using [`prompt-patterns.md`](prompt-patterns.md) and factory [`frontend-prompt-discipline-v0.md`](../../projects/mars-website-factory/frontend-prompt-discipline-v0.md).
- **Enforce** QA and reporting discipline ([`qa-checklist.md`](qa-checklist.md), [`reporting.md`](reporting.md), [`reporting-standard-v0.md`](../../projects/mars-website-factory/reporting-standard-v0.md) §4.2).
- **Apply** mandatory RU no word-splitting typography for Russian landings per [`russian-no-word-splitting-typography-v1.md`](../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md) and [`frontend-production-rules-v0.md`](../../projects/mars-website-factory/frontend-production-rules-v0.md) §12.
- **Prevent** unsafe edits: no manual `dist/`, no undeclared globals, no fake build/QA claims.

---

## Non-goals

- **No** autonomous deployment, CI green-washing, or hosting claims without evidence.
- **No** CMS, headless API, or backend/runtime assumptions unless the handoff **`integration_notes`** documents a real integration.
- **No** hand-editing **`dist/`** (or other generated output) to “fix” production.
- **No** framework migration (e.g. React/Vue rewrite) unless **`target_stack`** and governance explicitly allow a **STRUCTURE CHANGE**.
- **No** hidden build automation: scripts and tasks must match what the operator runs and records in REPORT.

---

## SoT and boundaries

- Role narrative and factory gates: [`../../projects/mars-website-factory/agent-map.md`](../../projects/mars-website-factory/agent-map.md), [`../../projects/mars-website-factory/frontend-production-model.md`](../../projects/mars-website-factory/frontend-production-model.md).
- Registry row: [`../registry.md`](../registry.md) §4.1 — `gulp_frontend_agent`.
- This pack is **documentation only**; it does not implement agents in `mars-runtime`.
