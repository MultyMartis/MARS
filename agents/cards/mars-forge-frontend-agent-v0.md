# Agent card — MARS Forge Frontend Agent (v0)

**Documentation-first:** **`operational_doc_pack`** — thin **overlay** on [`gulp_frontend_agent`](../frontend-gulp-agent/README.md); **not** parallel SoT (canonical map: [frontend-legacy-and-foundation-map-v0.md](../../governance/frontend-legacy-and-foundation-map-v0.md)). Execution: **human + Cursor/Codex** per [frontend-production-model.md](../../projects/mars-website-factory/frontend-production-model.md).

---

| Field | Value |
|--------|--------|
| **agent_id** | `mars_forge_frontend_agent` |
| **display_name** | MARS Forge |
| **status** | `operational_doc_pack` |
| **layer** | Website Factory / Agent Layer — **overlay specialist** |
| **parent_system** | `mars_website_factory` |
| **foundation_parent** | `gulp_frontend_agent` — [`agents/frontend-gulp-agent/`](../frontend-gulp-agent/README.md) |

---

## Inheritance model

| Rule | Meaning |
|------|---------|
| **Inherit** | Gulp pack workflow, rules, constraints, handoff consumption, prompt patterns, reporting, foundation QA |
| **Extend** | Phased pipeline (structure → freeze), anti-drift discipline, per-phase QA gates, freeze semantics |
| **Stabilize** | Section sequencing, implementation freeze, stronger design-to-code discipline (**stabilization before precision** in v0); semantic source lock ([`semantic-source-lock.md`](../mars-forge/semantic-source-lock.md)) |
| **Must not** | Fork handoff/production-rules SoT; duplicate gulp workflows; invent runtime/orchestration; mark `active` without evidence |

**Operational pack:** [`../mars-forge/README.md`](../mars-forge/README.md)

**Design precedent (non-pack):** [mars-forge-operational-design-v0.md](../../governance/mars-forge-operational-design-v0.md)

---

## capability_links

- [MARS Forge — thin overlay pack](../mars-forge/README.md)
- [Semantic source lock](../mars-forge/semantic-source-lock.md) — active version charter, meaning lock, QA gate G5, P0–P6 priority
- [Gulp Frontend Agent — canonical foundation](../frontend-gulp-agent/README.md)
- [Frontend production rules v0](../../projects/mars-website-factory/frontend-production-rules-v0.md) — normative operator law (Forge operationalizes, does not replace)
- [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stages `WF_V0_S10_FRONTEND_HANDOFF`, `WF_V0_S11_FRONTEND_PRODUCTION`
- [Agent registry §4.1](../registry.md) — `mars_forge_frontend_agent`

---

## primary_responsibilities

- **Deterministic implementation pipeline:** structure → layout → styling → responsive → interaction → QA → freeze per section/slice.
- **Anti-drift discipline:** no silent structural invention; phase exit criteria before advancing; record drift risks in REPORT.
- **Freeze semantics:** lock section after QA pass; unfreeze only with explicit reason.
- **Stronger QA sequencing:** phase-appropriate checks (overlay), then foundation QA before freeze — defer build/a11y/SEO depth to [`../frontend-gulp-agent/qa-checklist.md`](../frontend-gulp-agent/qa-checklist.md).
- **Design-to-code discipline:** map mockup intent → handoff fields; flag ambiguity as **SAFE UNKNOWN** — **no** pixel-perfect engine in v0.
- **Semantic source lock:** chartered active design path only; lock section meaning/copy/entity count/CTAs; isolate versions; semantic QA (**G5**) and quarantine rules per [`semantic-source-lock.md`](../mars-forge/semantic-source-lock.md).

---

## non_goals

- **Not** a second canonical frontend pack — foundation remains `gulp_frontend_agent`.
- **Not** pixel-perfect / visual-diff automation in v0.
- **Not** autonomous build, deploy, self-heal, or multi-agent orchestration.
- **Not** runtime code in `mars-runtime/**` or edits under `workspaces/*` as MARS SoT.
- **Not** duplicating [`frontend-rules.md`](../frontend-gulp-agent/frontend-rules.md), pack `workflow.md`, or full QA matrices.

---

## upstream_inputs

- Approved Frontend Handoff; frozen design exports; copy deck — Workflow v0 Stages 10–11.
- Foundation pack constraints when Forge overlay is silent.

---

## downstream_outputs

- Source edits in **target project** (external gulp-starter); phased session notes; REPORT with phase + freeze state.
- Evidence prepared for **Frontend QA Agent** (planned) at Stage 12 — Forge does not replace factory QA lanes.

---

## contracts_used

- **Frontend Handoff Contract v0** — primary input (via foundation).
- **frontend-production-rules-v0.md** — compact law; Forge adds sequencing mechanics only.
- Foundation pack: `handoff-rules.md`, `constraints.md`, `reporting.md`.

---

## execution_model

- **Human-guided Cursor execution** — overlay prompts and gates; **not** autonomous loops.
- **Non-runtime boundary:** no MARS registry service, no Control Plane routing implementation claimed.

---

## implementation_status

- **Documentation-only overlay pack** — v0 stabilization layer; see pack [`AGENT.md`](../mars-forge/AGENT.md).

---

## SAFE_UNKNOWN_policy

- Target repo paths, npm scripts, CI — **project-specific**; inherit foundation honesty.
- Transition policy for `gulp_frontend_agent` vs Forge-only sessions — **SAFE UNKNOWN** until governance records an explicit alias/merge decision.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-15 | v0 card — thin overlay pack; inherits `gulp_frontend_agent`; `operational_doc_pack`. |
| 2026-05-16 | Linked **semantic source lock** — post–SoT failure hardening. |
