# Agent card — Frontend QA Agent (v0)

**Documentation-first:** **planned** role — **not** an automated QA runner in MARS today, **not** autonomous. **Human/Cursor** checklist and tooling-assisted reviews. **Future MARS runtime** **planned only**.

---

| Field | Value |
|--------|--------|
| **agent_id** | `frontend_qa_agent` |
| **display_name** | Frontend QA Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [QA and validation model](../../projects/mars-website-factory/qa-validation-model.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S12_FRONTEND_QA`
- [Frontend production model](../../projects/mars-website-factory/frontend-production-model.md)
- [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md) — QA-related fields
- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md) — metadata/headings consistency

---

## primary_responsibilities

- **Semantic validation:** landmarks, heading order heuristics, meaningful structure vs blueprint intent.
- **Responsive validation:** key breakpoints / viewport spot-checks per handoff and site-type QA emphasis.
- **Accessibility checks:** heuristic a11y pass (labels, contrast flags where tooling exists) — depth **TBD** per project; no false “WCAG certified” claim without audit evidence.
- **Section consistency:** implemented sections vs **Block Registry** / handoff **`section_map`**.
- **Component consistency:** repeated patterns (headers, cards, CTAs) behave consistently across templates.
- **Frontend anti-pattern detection:** e.g. inline critical hacks, manual `dist` edits, unscoped globals, hook violations — align with [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md) forbidden patterns.

---

## non_goals

- Does **not** replace security audit or legal/compliance sign-off.
- Does **not** alone authorize production deploy (Human Approval stage).
- Does **not** imply Lighthouse CI / visual regression / automated a11y engines are in-repo unless evidenced (**SAFE UNKNOWN** per [qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

## upstream_inputs

- Built static pages; frontend handoff spec; QA checklists — Workflow v0 Stage 12.

---

## downstream_outputs

- Frontend QA report; severity-tagged defect backlog; **pass** / **fail** / **conditional** recommendation.

---

## contracts_used

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)
- [Frontend Handoff Contract v0](../../projects/mars-website-factory/frontend-handoff-contract-v0.md)

---

## registries_used

- **Site Type Registry v0** (QA emphasis); **Page Blueprint Contract v0** (metadata, headings).

---

## qa_relationships

- Complements **Validator Agent (integration)** — specialist depth on frontend lane vs cross-cutting policy (see [qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).
- **Explicit rule:** **QA failure blocks delivery** unless a **HITL override** exists (documented waiver with audit trail per Workflow v0 Stage 12 — **NEED HUMAN APPROVAL** for blocker waivers).

---

## escalation_rules

- **QA rejection** cycles to Stage 11 until pass or approved exception path (Workflow v0).
- **Blocker** list non-empty → block downstream Final Validation / delivery unless waived with HITL + **SECURITY RISK** if applicable.

---

## HITL_requirements

- Waivers for **blockers** → **NEED HUMAN APPROVAL** + **SECURITY RISK** when applicable (Workflow v0 Stage 12).

---

## SAFE_UNKNOWN_policy

- Unknown performance baseline or tooling → report **SAFE UNKNOWN**; do not fabricate Lighthouse scores.

---

## execution_model

- **Human/Cursor** — manual checks plus optional local tools; **not** continuous autonomous monitoring.

---

## implementation_status

- **Documentation only** — no shipped Frontend QA bot in MARS core.

---

## future_runtime_notes

- May integrate CI jobs when Tool Layer matures — **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — QA failure blocks delivery unless HITL override. |
