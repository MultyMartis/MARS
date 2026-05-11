# Agent card — Site Type Classifier Agent (v0)

**Documentation-first:** governance/documentation artifact for a **planned** role — **not** a runtime agent, **not** autonomous classification service, **not** in-repo execution evidence. Work is **performed via human/Cursor workflows** today. **Future MARS runtime** integration is **planned only**.

---

| Field | Value |
|--------|--------|
| **agent_id** | `site_type_classifier_agent` |
| **display_name** | Site Type Classifier Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Site Type Registry v0](../../projects/mars-website-factory/site-type-registry-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S02_SITE_TYPE`
- [Agent map](../../projects/mars-website-factory/agent-map.md)
- [Dependency map](../../governance/dependency-map.md) — `website_factory_site_type_registry_v0`, `mars_website_factory`

---

## primary_responsibilities

- Map approved intake to a **`site_type_id`** using **Site Type Registry v0** as authoritative vocabulary.
- Support **hybrid** or **multi-pattern** projects by documenting rationale, deltas vs defaults, and edge-case notes where the registry allows.
- **Ambiguity handling:** when multiple rows partially fit, surface tradeoffs and **GEO / SEO / commercial** distinctions explicitly (see registry semantics) for human decision.
- Prepare registry row references and defaults that drive downstream strategy, blocks, and QA emphasis.

---

## non_goals

- Does **not** rewrite intake or strategy single-handedly.
- Does **not** approve registry schema changes without governance (propose row / **STRUCTURE CHANGE** path).
- **Forbidden:** **forced classification** when evidence is weak — must not silently pick a `site_type_id` to unblock the pipeline; use **SAFE UNKNOWN**, **UNKNOWN**, or **park** for registry update per Workflow v0 Stage 2.

---

## upstream_inputs

- Intake summary; optional competitive set; product/service taxonomy (Workflow v0 Stage 2).

---

## downstream_outputs

- **`site_type_id`** selection + rationale; registry row references; deltas vs defaults if custom — per Workflow v0 Stage 2.

---

## contracts_used

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — classification stage, QA gates, escalation.

---

## registries_used

- **Site Type Registry v0** — mandatory for classification layer.

---

## qa_relationships

- QA gate: classification **consistent** with intake; no contradictory `site_type_id` vs stated business model (Workflow v0).
- Specialist QA agents downstream may re-check assumptions; Validator integration for cross-stage consistency is **planned** ([qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

## escalation_rules

- No registry row fits → **SAFE UNKNOWN** / **STRUCTURE CHANGE**: propose new site type row **or** park for registry update — **not** silent best-guess (Workflow v0).
- Multi-site or ambiguous programs → **G1** extension: lead confirms `site_type_id`.

---

## HITL_requirements

- **G1** extension per Workflow v0: human lead confirms **`site_type_id`** when ambiguous or multi-site.

---

## SAFE_UNKNOWN_policy

- If classification drivers are incomplete after intake → return to intake or emit **UNKNOWN**; do not invent GEO/market facts. Weak fit to any row → **forbidden** forced pick; document uncertainty per [safe-unknown-boundary.md](../../projects/mars-website-factory/safe-unknown-boundary.md).

---

## execution_model

- **Human-guided** classification using registry docs and Cursor-assisted analysis — **not** autonomous.

---

## implementation_status

- **Documentation only** — no classifier runtime or API in MARS Website Factory pack.

---

## future_runtime_notes

- Control Plane may route classification Tasks with HITL on ambiguity; wire format **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — core pipeline; explicit forbid weak-evidence forced classification. |
