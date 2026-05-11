# Agent card — Page Blueprint Agent (v0)

**Documentation-first:** **planned** role — **not** runtime blueprint engine, **not** autonomous page generation. **Human/Cursor** execution today. **Future MARS runtime** **planned only**.

---

| Field | Value |
|--------|--------|
| **agent_id** | `page_blueprint_agent` |
| **display_name** | Page Blueprint Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md)
- [Page Blueprint QA Checklist v0](../../projects/mars-website-factory/page-blueprint-qa-checklist-v0.md)
- [Block Registry v0](../../projects/mars-website-factory/block-registry-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S05_BLUEPRINT`
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **Block sequencing:** per-page ordered **`block_id`** stacks consistent with **Block Registry v0** and `site_type_id` rules.
- **CTA pacing:** placement and frequency of CTAs aligned with strategy and **mobile reading flow**.
- **Mobile reading flow:** order and density that support small-screen consumption patterns.
- **Scanability:** headings, chunking, and list/table use per contract fields and checklist categories.
- **Blueprint contract generation:** produce blueprint instances conforming to **Page Blueprint Contract v0** (normalized orchestration fields for downstream design/frontend/QA).

---

## non_goals

- Does **not** replace **UX Structure Agent** for layout hierarchy detail where that role is used (Workflow v0 lists both; division **TBD** per project).
- Does **not** produce final visual design or HTML/CSS.
- Does **not** silently drop blocks when registry mismatch — escalate per Workflow v0 Stage 5.

---

## upstream_inputs

- IA pack; strategy/SEO; **`site_type_id`**; design/frontend constraint hints from registry defaults — Workflow v0 Stage 5.

---

## downstream_outputs

- Blueprint set (per URL/template instance per IA); cross-page link graph notes — contract-shaped artifacts.

---

## contracts_used

- **Page Blueprint Contract v0** — primary output shape.
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — stage gates and escalation.

---

## registries_used

- **Block Registry v0**; **Site Type Registry v0**; **Page Blueprint Contract v0**.

---

## qa_relationships

- **Page Blueprint QA Checklist v0** and **SEO QA / Conversion QA / Validator** at Stage 6 — blueprints must pass or be waived with HITL per workflow.
- Registry mismatch → fix blueprint or amend registry under governance — **no** silent drops.

---

## escalation_rules

- **Registry mismatch** (block not allowed for `site_type_id`) → **STRUCTURE CHANGE** path: amend registry or blueprint with traceability (Workflow v0).

---

## HITL_requirements

- **G3:** PM + tech lead approve blueprint batch before blueprint QA sign-off for handoff (Workflow v0).

---

## SAFE_UNKNOWN_policy

- When contract field is undecided for a page type → **SAFE UNKNOWN** with explicit flag; checklist ambiguity → written assumption or checklist amendment request (Workflow v0 Stage 6 alignment).

---

## execution_model

- **Human/Cursor** drafting of blueprint documents — **not** autonomous multi-page emitters.

---

## implementation_status

- **Documentation only** — no blueprint compiler in-repo for Website Factory.

---

## future_runtime_notes

- Control Plane may validate blueprint JSON/schema when schemas are frozen — **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — Block Registry, Blueprint Contract, Blueprint QA Checklist references. |
