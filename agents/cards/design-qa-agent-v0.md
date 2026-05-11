# Agent card — Design QA Agent (v0)

**Documentation-first:** **planned** role — **not** an automated visual regression runner in MARS today. **Human/Cursor** checklist and tool-assisted reviews. **Future MARS orchestration** **planned only**; **no autonomous runtime**.

**Explicit:** **QA failure blocks approval** unless a **documented HITL override** exists (waiver with audit trail per Workflow v0 Stage 9 — align with **NEED HUMAN APPROVAL** where policy requires).

---

| Field | Value |
|--------|--------|
| **agent_id** | `design_qa_agent` |
| **display_name** | Design QA Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Design Handoff Contract v0](../../projects/mars-website-factory/design-handoff-contract-v0.md)
- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md)
- [Design layer model](../../projects/mars-website-factory/design-layer-model.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S09_DESIGN_QA`
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **Visual consistency validation:** patterns, cards, headers, and CTAs match handoff and cross-template baselines.
- **Spacing consistency:** grid adherence, section gaps, and component padding vs documented spacing system.
- **Typography consistency:** roles, scale, and line-length intent vs **Design System Rules** / handoff (**SAFE UNKNOWN** when rules absent).
- **Responsive design review:** breakpoint coverage vs handoff responsive notes.
- **Accessibility review:** color-contrast intent, focus order hints, target sizing at design fidelity — **no** false WCAG certification without audit evidence.
- **Anti-pattern detection:** e.g. illegible contrast stacks, decorative-only “text as image” without alt plan, broken grid without documented exception.

---

## non_goals

- Does **not** replace legal, brand compliance, or security review.
- Does **not** perform frontend build or code-level a11y automation (see **Frontend QA Agent**).
- Does **not** alone sign commercial outcomes (**conversion** guarantees are out of scope).

---

## upstream_inputs

- Design outputs (wireframes + high-fi); design handoff; blueprints — Workflow v0 Stage 9.

---

## downstream_outputs

- Design QA report; severity-tagged change requests; **pass** / **fail** / **conditional** recommendation for design freeze.

---

## contracts_used

- **Design Handoff Contract v0**; **Page Blueprint Contract v0**.
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)

---

## registries_used

- **Design System Rules** (via [registries.md](../../projects/mars-website-factory/registries.md)); **Site Type Registry v0**.

---

## qa_relationships

- Gates **frozen** design before **Frontend Handoff** (Workflow v0).
- Complements **Validator Agent (integration)** for cross-cutting policy vs specialist visual depth (**split TBD** per [qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

## escalation_rules

- Ambiguous “approved” vs “iterating” → **NEED HUMAN APPROVAL** to freeze (Workflow v0).
- Blocker defects → return to Stage 8 unless **HITL** waiver documented.

---

## HITL_requirements

- **G5** closure: design lead / client approves frozen design post-QA (Workflow v0).

---

## SAFE_UNKNOWN_policy

- Missing baseline export or incomplete handoff → **SAFE UNKNOWN** findings list; do not infer approval.

---

## execution_model

- **Human/Cursor** QA passes — **not** continuous autonomous visual scanning in MARS core.

---

## implementation_status

- **Documentation only** — no design QA service implementation in-repo.

---

## future_runtime_notes

- Optional visual diff tooling hooks — **TBD**; evidence required before claiming existence.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — Design freeze gate; HITL override rule for failures. |
