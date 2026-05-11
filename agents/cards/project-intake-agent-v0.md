# Agent card — Project Intake Agent (v0)

**Documentation-first:** this file is a **governance/documentation** artifact. It describes a **planned** agent **role**, **not** an autonomous runtime service, **not** executable MARS agent code, and **not** evidence of automated execution. Today, work mapped to this role is **executed through human- and Cursor-supervised workflows** per `governance/execution-model.md`. **Future MARS runtime** integration (Control Plane routing, Task bundles) is **planned only** and **out of scope** until implementation exists in-repo.

---

| Field | Value |
|--------|--------|
| **agent_id** | `project_intake_agent` |
| **display_name** | Project Intake Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [MARS Website Factory — Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S01_INTAKE`
- [Agent map (factory role prose SoT)](../../projects/mars-website-factory/agent-map.md)
- [Dependency map — `mars_website_factory`](../../governance/dependency-map.md) §4
- [Capability map — C16](../../governance/capability-map.md) (Website Factory, strategic planned)
- [SAFE UNKNOWN boundary](../../projects/mars-website-factory/safe-unknown-boundary.md)
- [System signals dictionary](../../governance/system-signals-dictionary.md)

---

## primary_responsibilities

- **Business intake:** capture briefs, stakeholder goals, and delivery expectations in a structured form suitable for downstream Tasks.
- **Goal extraction:** articulate measurable or narrative goals, audience hypotheses, and success criteria where evidence exists.
- **Constraints:** record brand, legal/compliance, technical, and scope boundaries (`scope_in` / `scope_out` intent per workflow narrative).
- **Project classification preparation:** supply stable inputs for **Site Type Classification** (goals, constraints, markets) without prematurely fixing `site_type_id`.
- **Missing-context escalation:** when required business context is absent, emit **UNKNOWN**, **SAFE UNKNOWN** (only with explicit written assumptions and policy), or **NEED HUMAN APPROVAL** — never silent invention of facts.

---

## non_goals

- Does **not** assign `site_type_id` (Site Type Classifier Agent and HITL).
- Does **not** author final marketing/SEO strategy (downstream strategy agents).
- Does **not** imply autonomous client interviews, CRM access, or live data pulls without contracts and evidence.
- Does **not** replace PM/legal sign-off; intake accuracy remains **HITL**-gated per [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md).

---

## upstream_inputs

- Client briefs, stakeholder notes, existing analytics (**optional**), compliance flags, prior site exports (**optional**) — as listed in Workflow v0 Stage 1.

---

## downstream_outputs

- Intake summary; Task-shaped scope draft (goal, constraints, risk hypothesis); open questions list — per Workflow v0 Stage 1.

---

## contracts_used

- Narrative alignment with [Task Contract v0](../../workflows/task-contract-v0.md) fields where a scope draft is produced (documentation-level, not a runtime schema).
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — intake stage definitions and escalation classes.

---

## registries_used

- None mandatory at intake; may reference **Site Type Registry v0** for vocabulary only (no forced classification).

---

## qa_relationships

- **Completeness QA gate** (Workflow v0): goals, audience, constraints, approval chain identified before exit from intake.
- **Validator Agent (integration):** may later cross-check intake artifacts against Task scope invariants — **planned**; no automated Validator evidenced for Website Factory today ([qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

## escalation_rules

- Thin intake → **pause** at Stage 1; emit **UNKNOWN** or bounded **SAFE UNKNOWN** per policy; **park** if assumptions are not allowed.
- Conflicts in stakeholder goals → **NEED HUMAN APPROVAL** before downstream stages per workflow failure classes.

---

## HITL_requirements

- **G1** (per [workflow-map.md](../../projects/mars-website-factory/workflow-map.md) / Workflow v0): PM/lead confirms intake accuracy and **scope_in** / **scope_out**.

---

## SAFE_UNKNOWN_policy

- Any unstated stack, hosting, markets, or compliance posture → label **SAFE UNKNOWN** or **UNKNOWN** explicitly; do not fabricate bindings. Aligns with [safe-unknown-boundary.md](../../projects/mars-website-factory/safe-unknown-boundary.md) and Workflow v0 Stage 1 **SAFE UNKNOWN escalation** row.

---

## execution_model

- **Human / Cursor workflows today:** prompts, reviews, and edits under Phase 1 execution model — **not** an autonomous agent process.

---

## implementation_status

- **Documentation only.** No dedicated runtime, adapter, or scheduler for this role in MARS core as a shipped Website Factory engine.

---

## future_runtime_notes

- Intended to map to Control Plane **route** + **Task** lifecycle when/if runtime exists; `required_agents` and `hitl_gates` remain design alignment only ([control-plane/contract.md](../../control-plane/contract.md)).

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — core Website Factory pipeline (documentation-only). |
