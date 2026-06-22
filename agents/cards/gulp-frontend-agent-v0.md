# Agent card — Gulp Frontend Agent (v0)

**Documentation-first:** **`operational_doc_pack`** — documentation-backed operational specialist pack in MARS Agent Registry §4 / §4.1; **not** proof of Gulp code in this repository, **not** autonomous runtime, **not** a deployed agent service. Execution is **human + Cursor/Codex** per [frontend-production-model.md](../../projects/mars-website-factory/frontend-production-model.md) and `governance/execution-model.md`. *Historical:* catalog once used **legacy-bridge** for the imported Web-GPT **Gulp Frontend** profile — alignment footnote only. **Future MARS runtime** integration remains **planned only** (no runtime claim).

---

| Field | Value |
|--------|--------|
| **agent_id** | `gulp_frontend_agent` |
| **display_name** | Gulp Frontend Agent |
| **status** | `operational_doc_pack` (registry §4 / §4.1 — documentation-backed pack; human + Cursor/Codex; **not** autonomous runtime. *Historical:* **legacy-bridge** footnote for Web-GPT import profile.) |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Frontend Gulp Agent — operational doc pack](../frontend-gulp-agent/README.md) — prompts, workflow, QA/reporting (`gulp_frontend_agent`; not a runnable starter)
- [Frontend production model](../../projects/mars-website-factory/frontend-production-model.md)
- [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stages `WF_V0_S10_FRONTEND_HANDOFF`, `WF_V0_S11_FRONTEND_PRODUCTION`
- [Block Registry v0](../../projects/mars-website-factory/block-registry-v0.md)
- [Agent registry §4.1](../registry.md) — stable `agent_id`
- Legacy imported profile: [web-gpt-sources/04_agents.md](../../web-gpt-sources/04_agents.md) (Gulp Frontend Agent section)

---

## primary_responsibilities

- **Source-first architecture:** implement and edit under agreed **`src/`** (or project equivalent); rebuild to produce deployable static output.
- **Modular SCSS:** partials per section/component; shared tokens/variables per [frontend-production-model.md](../../projects/mars-website-factory/frontend-production-model.md) and [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md).
- **Single Base Container Law:** reuse project primary `.container` — no per-block duplicate container geometry ([site-wide-style-foundation-contract-v1.md](../../projects/mars-website-factory/site-wide-style-foundation-contract-v1.md) §4, [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) WF-GRID-006).
- **Section Owns Its Rhythm Law:** layout region owns external vertical rhythm — not first/last internal child ([frontend-section-spacing-rule-v1.md](../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md) §2.6).
- **Reusable sections:** composition via includes/partials (**gulp-file-include** intent per legacy profile; **SAFE UNKNOWN** if project uses a different include mechanism until documented).
- **gulp-file-include:** HTML assembly from partials matching **`section_map`** / handoff mappings — target shape, not an in-repo starter claim.
- **data-* hooks:** scoped behavior binding per handoff `data_attribute_hooks` — prefer `data-*` over ad-hoc globals.
- **Responsive implementation:** mobile-first breakpoints aligned with frozen design and Frontend Handoff.
- **Production-safe output:** build produces **`dist/`** (or agreed dir); deliverables are reproducible from source.

---

## non_goals

- **Forbidden: editing `dist/` directly** — never hand-patch generated output; fix sources and rebuild ([Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)).
- **Forbidden: unsafe global CSS pollution** — no unscoped resets/`!important` waves without explicit HITL sign-off per handoff contract.
- **Forbidden: framework assumptions** — no default React/Vue/Svelte/etc. unless **`target_stack`** and governance explicitly allow (**STRUCTURE CHANGE** if scope shifts).
- **Forbidden: runtime/CMS assumptions** — static factory model unless **`integration_notes`** documents a real integration with owner (**SAFE UNKNOWN** otherwise).
- **Not autonomous deployment** — no implied CI/CD, hosting, or live publish without separate ops contracts and evidence.

---

## upstream_inputs

- Frontend handoff spec; frozen design exports; copy deck — Workflow v0 Stages 10–11.

---

## downstream_outputs

- Source files (HTML/SCSS/JS per project); build instructions; PR or change bundle — Workflow v0 Stage 11.

---

## contracts_used

- **Frontend Handoff Contract v0** — primary consumption contract.
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — handoff + production gates.

---

## registries_used

- **Frontend Handoff Contract v0**; **Block Registry v0**; **Site Type Registry v0** (defaults/emphasis) per workflow.

---

## qa_relationships

- **Frontend QA Agent** validates build, semantics, responsive, a11y heuristics — downstream Stage 12.
- Build success: **SAFE UNKNOWN** if CI not defined for project ([frontend-production-model.md](../../projects/mars-website-factory/frontend-production-model.md) honesty).

---

## escalation_rules

- Unsupported frontend requirement (framework/CMS/non-static) → **UNKNOWN** / **STRUCTURE CHANGE** at Stages 10–11 per Workflow v0.
- Unknown stack or missing CI → document **SAFE UNKNOWN**; do not claim green build.

---

## HITL_requirements

- **G6:** tech + design sign-off on PR/file set vs frozen design (Workflow v0 Stage 11).
- Tech lead approves handoff before Frontend Production (Stage 10 gate).

---

## SAFE_UNKNOWN_policy

- Presence of `gulp-starter` or specific task graph in repo → **SAFE UNKNOWN** until evidenced ([frontend-production-model.md](../../projects/mars-website-factory/frontend-production-model.md)).

---

## execution_model

- **Human-guided Cursor execution** (Phase 1) — engineer implements per handoff; **not** autonomous agent loops, **not** autonomous deployment.

---

## implementation_status

- **Documentation-only role definition** — MARS does not ship a Website Factory Gulp runtime in this pack.

---

## future_runtime_notes

- May map to Tool Layer (build, lint) and Execution Bridge when/if automated — **TBD**; must still respect source-first and handoff contracts.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — aligned with frontend-production-model + frontend-handoff-contract-v0. |
| 2026-05-15 | Status normalized to `operational_doc_pack` (registry §4 / §4.1); legacy-bridge as historical footnote only. |
