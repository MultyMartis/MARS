# Agent card — Validator Agent (Website Factory integration) (v0)

**Documentation-first:** this card describes the **orchestration-level validation role** for the **MARS Website Factory** narrative — **not** a second autonomous “super-validator” runtime, **not** omniscient automation. It complements the catalog **Validator Agent** row in `agents/registry.md` §4 (legacy **FlyCheck** alignment). Execution remains **human/Cursor** and checklist-driven today. **Future MARS runtime** Validator routing is **planned only**.

**Explicit statement:** **Validator integration ≠ omniscient autonomous validator** — no claim of exhaustive policy enforcement, full security coverage, or automatic pass/fail without human governance ([qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

| Field | Value |
|--------|--------|
| **agent_id** | `validator_agent_integration` |
| **display_name** | Validator Agent (Website Factory integration) |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer (cross-lane **orchestration helper** intent) |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [QA and validation model](../../projects/mars-website-factory/qa-validation-model.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stages 6, 12, 13 (`validate` alignment per [execution-flow.md](../../workflows/execution-flow.md))
- [Agent registry — Validator Agent](../registry.md) §4
- [Dependency map](../../governance/dependency-map.md) — `mars_website_factory` → `agent_registry`
- [Task Contract v0](../../workflows/task-contract-v0.md) — signals on Tasks

---

## primary_responsibilities

- **Orchestration-level validation role:** cross-check artifacts against **Task** scope, documented **forbidden paths**, and structural expectations **as design** — when a human or future router invokes validation.
- **Cross-stage consistency:** intake ↔ site type ↔ strategy ↔ IA ↔ blueprints ↔ handoffs ↔ frontend outputs — flag drift, orphan CTAs, broken link graphs, contract field gaps.
- **SAFE UNKNOWN enforcement:** require explicit labeling when evidence is missing; block silent “green” narratives that contradict **SAFE UNKNOWN** policy ([safe-unknown-boundary.md](../../projects/mars-website-factory/safe-unknown-boundary.md), [system-signals-dictionary.md](../../governance/system-signals-dictionary.md)).
- **Escalation routing:** emit **UNKNOWN**, **NEED HUMAN APPROVAL**, **STRUCTURE CHANGE**, **SECURITY RISK** per signal vocabulary; route to nearest upstream fix stage per Workflow v0 failure classes.
- **Validation gates:** align with blueprint QA (Stage 6), frontend QA (Stage 12), and Final Validation (Stage 13) — **combination with specialist QA TBD** per workflow (no fixed split claim).

---

## non_goals

- Does **not** replace **SEO QA**, **Conversion QA**, **Design QA**, or **Frontend QA** specialist depth.
- Does **not** implement automated policy engine, secrets scanning, or production firewall — **not** evidenced in Website Factory pack.
- Does **not** guarantee completeness of all risks — Validator remains bounded by inputs and declared policies.

---

## upstream_inputs

- Artifacts from whichever stage is under validation; Task/scope narrative; registries and contracts referenced by that stage.

---

## downstream_outputs

- Validation reports with **PASS** / **FAIL — fix** / **NEED HUMAN APPROVAL** / **SAFE UNKNOWN** outcomes per [qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md) gate vocabulary.

---

## contracts_used

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — QA gates and escalation.
- [Task Contract v0](../../workflows/task-contract-v0.md); [system-signals-dictionary.md](../../governance/system-signals-dictionary.md)

---

## registries_used

- Consumes whichever **Website Factory** registry/contract SoT applies to the validated slice (`website_factory_*` entities per [dependency-map.md](../../governance/dependency-map.md) §4).

---

## qa_relationships

- **Complements** specialist QA agents; exact split **TBD** ([agent-map.md](../../projects/mars-website-factory/agent-map.md), Workflow v0).
- Whether Validator is one LLM call or checklist tooling → **implementation TBD** ([qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

## escalation_rules

- **QA rejection** without waiver → block design freeze, frontend freeze, delivery (Workflow v0 escalation rules).
- **SECURITY RISK** → stop line per security policy — Validator narrative **aligns** with governance; **no** auto-remediation claim.

---

## HITL_requirements

- High-risk waivers and ambiguous validation outcomes → **NEED HUMAN APPROVAL** per approval gates and workflow.

---

## SAFE_UNKNOWN_policy

- Validator must **not** force definitive claims where pack says **SAFE UNKNOWN**; escalation to human when assumptions could change delivery truth.

---

## execution_model

- **Human/Cursor** validation passes and future Control Plane **validate** stage — **not** continuous autonomous auditing.

---

## implementation_status

- **Documentation only** — **no** separate Validator runtime for Website Factory evidenced in-repo.

---

## future_runtime_notes

- Control Plane may route `validate` steps to Validator policy hooks + specialist tools per [control-plane/contract.md](../../control-plane/contract.md) — wire format **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — orchestration validation; explicit non-omniscience. |
