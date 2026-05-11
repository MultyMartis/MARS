# Agent card — Wireframe Generator Agent (v0)

**Documentation-first:** **planned** role — **not** autonomous diagram software in MARS. **Human/Cursor** execution today. **Future MARS orchestration** **planned only**; **no autonomous runtime**.

**Explicit:** **Wireframes are structural artifacts, not final UI** — low-fidelity boxes and flows only; final look, branding, and component polish belong to **Full Design Generator** / design freeze path.

---

| Field | Value |
|--------|--------|
| **agent_id** | `wireframe_generator_agent` |
| **display_name** | Wireframe Generator Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md)
- [UX Structure Agent](./ux-structure-agent-v0.md) (companion role — flow/pacing intent)
- [Design Handoff Contract v0](../../projects/mars-website-factory/design-handoff-contract-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S08_DESIGN_PRODUCTION` (co-primary with Full Design Generator Agent)
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **Low-fi structures:** grayscale layout skeletons per template/page without final branding.
- **Layout skeletons:** regions mapped to blueprint **`block_id`** / section semantics.
- **Block geometry:** relative proportions, columns, and stacking order intent at wireframe fidelity.
- **CTA placement:** structural position of primary/secondary actions (not final button styling).
- **Responsive wireframe intent:** key breakpoint sketches or annotations (mobile/tablet/desktop) as documentation — depth **TBD** per project.

---

## non_goals

- **Wireframes are structural artifacts, not final UI** — no production asset handoff without escalation to high-fi track.
- Does **not** replace **Information Architecture** for site-level routing.
- Does **not** silently change blueprint **`block_id`** stacks — mismatch → escalate.

---

## upstream_inputs

- Design handoff pack; approved blueprints; **UX Structure** notes — Workflow v0 Stage 8.

---

## downstream_outputs

- Wireframe set (tool-agnostic: exported images, FigJam, markdown+ASCII, etc. — **format explicit per project**).

---

## contracts_used

- **Design Handoff Contract v0**; **Page Blueprint Contract v0**.
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)

---

## registries_used

- **Block Registry v0** (semantic → layout mapping).

---

## qa_relationships

- **Design QA** checks skeleton vs handoff and blueprint before high-fi or freeze.
- Contradictions with **UX Structure** intent → revision loop or **HITL** ruling.

---

## escalation_rules

- Handoff requires unsupported layout pattern → **SAFE UNKNOWN** / **STRUCTURE CHANGE** with human decision.

---

## HITL_requirements

- **G4** / **G5** per workflow-map for UX/client and design visibility — exact cadence **TBD** per org.

---

## SAFE_UNKNOWN_policy

- Tooling and file format for wireframes → **SAFE UNKNOWN** until project standard is chosen; do not imply repo-hosted wireframe service.

---

## execution_model

- **Human/Cursor** production of wireframe artifacts — **not** an automated wireframe bot.

---

## implementation_status

- **Documentation only** — no wireframe generator implementation in MARS core.

---

## future_runtime_notes

- Control Plane could schedule wireframe tasks when design tools expose stable APIs — **TBD**; **no** guaranteed integration.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — Blueprint, UX Structure, Design Handoff alignment; structural-not-final stance. |
