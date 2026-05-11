# Agent card — UX Structure Agent (v0)

**Documentation-first:** **planned** role — **not** a layout engine, **not** autonomous UX generation. **Human/Cursor** execution today. **Future MARS orchestration** **planned only**; **no autonomous runtime** in this repository.

**Explicit:** **UX ≠ visual styling** — this role owns **structure, flow, pacing, and interaction intent**; color, type treatment, and pixel-level styling belong to **AI Designer** / design production unless a project collapses roles under **HITL** documented merge.

---

| Field | Value |
|--------|--------|
| **agent_id** | `ux_structure_agent` |
| **display_name** | UX Structure Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md)
- [Block Registry v0](../../projects/mars-website-factory/block-registry-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S05_BLUEPRINT` (co-primary with Page Blueprint Agent)
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **Reading flow:** vertical rhythm of content chunks, progressive disclosure, and cognitive order vs blueprint **`block_id`** sequence.
- **CTA pacing:** frequency and placement *intent* (not visual button styling) aligned with strategy and mobile constraints.
- **Mobile UX:** touch targets intent, fold behavior, sticky vs static chrome assumptions — documented as **SAFE UNKNOWN** when not specified.
- **Scanability:** chunking, list/table use intent, landmark rhythm — coordinated with blueprint headings metadata where applicable.
- **Hierarchy pacing:** how emphasis builds through the page (story arc) without prescribing final pixels.
- **Friction reduction:** form steps, optional fields, and trust-step sequencing intent tied to blueprint fields.
- **Section transitions:** how one block hands off to the next (narrative bridge, repeated CTA suppression rules) within **Block Registry** semantics.

---

## non_goals

- Does **not** replace **visual design** — no final typography, color, or component skin (**UX ≠ visual styling**).
- Does **not** alone define URL/site tree (see **Information Architecture Agent**).
- Does **not** implement frontend code.

---

## upstream_inputs

- IA pack; approved strategy/SEO; **site_type_id**; blueprint drafts — Workflow v0 Stage 5.

---

## downstream_outputs

- UX structure notes embedded in or alongside blueprint instances (contract-shaped fields or annex per project convention).

---

## contracts_used

- **Page Blueprint Contract v0** — primary coordination surface.
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)

---

## registries_used

- **Block Registry v0**; **Site Type Registry v0** (UX_model / density defaults where defined).

---

## qa_relationships

- **Page Blueprint QA** and **Conversion QA** validate that UX intent is expressible and not contradictory to CTAs and trust paths.
- Division vs **Page Blueprint Agent** for overlapping concerns remains **TBD** per project — document split in task notes (**SAFE UNKNOWN** if unset).

---

## escalation_rules

- Blueprint cannot satisfy reading flow without forbidden registry change → **STRUCTURE CHANGE** or registry amendment path (Workflow v0).

---

## HITL_requirements

- **G3:** PM + tech lead approve blueprint batch including UX-structure coherence before blueprint QA sign-off (Workflow v0 Stage 5–6).

---

## SAFE_UNKNOWN_policy

- Unspecified motion, animation, or micro-interaction depth → **SAFE UNKNOWN**; do not imply a design tool or runtime behavior exists.

---

## execution_model

- **Human/Cursor** annotation and refinement of blueprint-level UX intent — **not** autonomous layout generation.

---

## implementation_status

- **Documentation only** — no UX rules engine in-repo.

---

## future_runtime_notes

- Optional schema fields on blueprint JSON for `ux_structure` annex — **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — Blueprint Contract + Block Registry; UX ≠ visual styling. |
