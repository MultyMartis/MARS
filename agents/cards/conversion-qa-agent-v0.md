# Agent card — Conversion QA Agent (v0)

**Documentation-first:** **planned** role — **not** a live A/B test engine or analytics automaton in MARS. **Human/Cursor** checklist execution. **Future MARS orchestration** **planned only**; **no autonomous runtime**.

**Explicit:** **Conversion QA ≠ business outcome guarantees** — this role validates **clarity, consistency, and structural readiness** of conversion paths vs contracts and strategy; it does **not** promise leads, revenue, or lift.

---

| Field | Value |
|--------|--------|
| **agent_id** | `conversion_qa_agent` |
| **display_name** | Conversion QA Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Marketing Strategy Agent](./marketing-strategy-agent-v0.md)
- [SEO / marketing layer](../../projects/mars-website-factory/seo-marketing-layer.md) — positioning and funnel narrative SoT
- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md)
- [UX Structure Agent](./ux-structure-agent-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S06_BLUEPRINT_QA`
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **CTA validation:** presence, labeling, destination resolvability, and redundancy control vs **Marketing Strategy** and IA.
- **Trust-path validation:** proof, policy, and credential surfaces appear where high-friction actions occur.
- **Friction analysis:** form length, optional fields, and step count *intent* vs strategy (**SAFE UNKNOWN** when copy deck missing).
- **Conversion consistency:** repeated offers and messaging align across templates and blueprints.
- **Commercial flow validation:** lead vs purchase vs booking paths match stated business model from intake/strategy.
- **Lead capture review:** consent copy placeholders, required fields, and handoff to CRM/email **intent** — no live integration claim without evidence.

---

## non_goals

- **Conversion QA ≠ business outcome guarantees** — no promised conversion rate, CPL, or ROI from this agent role.
- Does **not** replace privacy/legal review for consent and data processing.
- Does **not** configure ad platforms or analytics (**planned-implementation** elsewhere).

---

## upstream_inputs

- Blueprint set; IA; strategy/messaging artifacts — Workflow v0 Stage 6.

---

## downstream_outputs

- Conversion QA findings in joint Stage 6 report; defects; pass/fail/conditional recommendation.

---

## contracts_used

- **Page Blueprint Contract v0**; [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md).

---

## registries_used

- **Site Type Registry v0** (conversion emphasis defaults where defined).

---

## qa_relationships

- Stage 6 alongside **SEO QA Agent** and **Validator Agent (integration)**.
- Feeds **Design** and **Frontend** stages indirectly by ensuring blueprint CTAs are coherent pre-visual work.

---

## escalation_rules

- CTA flow impossible or contradictory → **STRUCTURE CHANGE** back to IA/Strategy (Workflow v0).

---

## HITL_requirements

- Failed or high-risk → **NEED HUMAN APPROVAL** to waive or return to **S05** (Workflow v0 Stage 6).

---

## SAFE_UNKNOWN_policy

- Missing analytics baselines or CRM truth → **SAFE UNKNOWN**; findings are structural, not performance-proven.

---

## execution_model

- **Human/Cursor** conversion checklist — **not** autonomous funnel optimization.

---

## implementation_status

- **Documentation only** — no conversion QA runtime in MARS core.

---

## future_runtime_notes

- Optional bindings to experiment specs or event schemas — **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — Marketing Strategy pack, Blueprint Contract, UX Structure; no outcome guarantees. |
