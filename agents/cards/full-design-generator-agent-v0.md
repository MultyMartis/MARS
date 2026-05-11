# Agent card — Full Design Generator Agent (v0)

**Documentation-first:** **planned** role — **not** a shipped high-fidelity generator runtime in MARS. **Human/Cursor** execution today (design tools operated by humans). **Future MARS orchestration** **planned only**; **no autonomous runtime**.

**Explicit:** **No guaranteed Figma/runtime integration exists yet** in this repository — any design-tool automation is **out of scope** for v0 honesty unless separately evidenced.

---

| Field | Value |
|--------|--------|
| **agent_id** | `full_design_generator_agent` |
| **display_name** | Full Design Generator Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Design Handoff Contract v0](../../projects/mars-website-factory/design-handoff-contract-v0.md)
- [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md) — downstream consumption notes
- [Design QA Agent](./design-qa-agent-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S08_DESIGN_PRODUCTION`
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **High-fidelity UI concepts:** polished layouts reflecting approved tokens/direction from handoff (**when** design system material exists).
- **Component composition:** how design-system or ad-hoc components assemble per blueprint sections.
- **Visual consistency:** cross-template alignment so **Design QA** can diff against rules.
- **Responsive UI interpretation:** breakpoint-specific layouts documented or exported per project standard.
- **Design freeze preparation:** package that supports **G5** freeze and **Frontend Handoff** — asset list, naming, and open issues explicit.

---

## non_goals

- Does **not** claim **Figma** (or any tool) **MCP/runtime** **integration** **exists** **in-repo** for Website Factory v0.
- Does **not** authorize production deploy or bypass **Design QA**.
- Does **not** replace legal/compliance review for regulated claims or imagery.

---

## upstream_inputs

- Wireframes (**optional**); design handoff pack; brand system — Workflow v0 Stage 8.

---

## downstream_outputs

- High-fidelity designs or spec exports — **format explicit per project** (Workflow v0); asset manifest for frontend handoff.

---

## contracts_used

- **Design Handoff Contract v0**; **Frontend Handoff Contract v0** (readiness for Stage 10).
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)

---

## registries_used

- **Site Type Registry v0**; **Design System Rules** (via [registries.md](../../projects/mars-website-factory/registries.md)) where applicable.

---

## qa_relationships

- **Design QA Agent** gates fidelity vs blueprint + handoff before frontend.
- Failures cycle to revision until pass or documented **HITL** waiver.

---

## escalation_rules

- Cross-template inconsistency → **STRUCTURE CHANGE** or revision loop (Workflow v0 Stage 8 **SAFE UNKNOWN** escalation).
- **SECURITY RISK** (assets, compliance) → stop line until cleared.

---

## HITL_requirements

- **G5** closure: design lead / client approves **frozen** design for frontend (Workflow v0 Stage 9).

---

## SAFE_UNKNOWN_policy

- Export format, design tool, or token pipeline undecided → **SAFE UNKNOWN** in artifacts; no implied CI/CD or design-token build pipeline.

---

## execution_model

- **Human/Cursor** high-fidelity design work — **not** autonomous multi-screen UI emission.

---

## implementation_status

- **Documentation only** — no full-design generator service in MARS core.

---

## future_runtime_notes

- Possible MCP or API bridges to design tools — **TBD**; must remain evidence-based in repo docs when introduced.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — Design Handoff, Frontend Handoff, Design QA; no guaranteed tool integration. |
