# Agent card — Marketing Strategy Agent (v0)

**Documentation-first:** **planned** agent **role** card — **not** runtime, **not** autonomous. Execution today is **human/Cursor workflow** only. **Future MARS runtime** integration **planned only**.

---

| Field | Value |
|--------|--------|
| **agent_id** | `marketing_strategy_agent` |
| **display_name** | Marketing Strategy Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S03_STRATEGY`
- [SEO / marketing layer](../../projects/mars-website-factory/seo-marketing-layer.md)
- [Agent map](../../projects/mars-website-factory/agent-map.md)
- [Site Type Registry v0](../../projects/mars-website-factory/site-type-registry-v0.md) (constraints)

---

## primary_responsibilities

- **Positioning:** narrative, differentiation, and audience-aligned value proposition within intake + `site_type_id` constraints.
- **CTA strategy:** primary/secondary CTAs, funnel steps, and destination intent aligned with IA (downstream) — no orphan CTAs without destination intent (Workflow v0).
- **Trust logic:** proof points, risk reversal, and credibility patterns appropriate to brand/compliance sensitivity.
- **Commercial intent:** offers, pricing narrative (hypothesis-level), and conversion goals stated without over-claiming metrics.
- **Conversion architecture:** landing narrative, objection handling, and journey hooks that inform IA and blueprints — **hypothesis/documentation** layer only.

---

## non_goals

- **Not responsible for visual design implementation** — no Figma/production design execution; hands off to design lane per workflow.
- Does **not** own technical SEO implementation details (see SEO Strategy Agent).
- Does **not** guarantee revenue, conversion rates, or campaign performance — **no** fabricated benchmarks (**SAFE UNKNOWN** when data absent).
- Does **not** bypass HITL on brand-sensitive messaging.

---

## upstream_inputs

- Intake; **`site_type_id`**; brand guidelines (**if** any) — Workflow v0 Stage 3.

---

## downstream_outputs

- Strategy memo; CTA / conversion narrative; risks list — complements SEO hypothesis doc from SEO Strategy Agent in same stage.

---

## contracts_used

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — strategic layer, QA gates, escalation.
- [Task Contract v0](../../workflows/task-contract-v0.md) — narrative alignment for scope/constraints.

---

## registries_used

- **Site Type Registry v0** — constraints and defaults; **Block Registry v0** indirect (which story types blocks must support) per Workflow v0.

---

## qa_relationships

- Internal consistency QA: messaging vs audience vs site type; Validator integration may later enforce cross-lane checks — **planned** ([qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

## escalation_rules

- Conflicting commercial vs brand compliance → **NEED HUMAN APPROVAL** / **STRUCTURE CHANGE** per Workflow v0 Stage 3.

---

## HITL_requirements

- **G2:** marketing lead approves strategy (and paired SEO hypotheses where applicable) per Workflow v0.

---

## SAFE_UNKNOWN_policy

- Missing proof, market data, or offer clarity → **SAFE UNKNOWN** with written assumptions **or** **UNKNOWN** / park until resolved — no false specificity.

---

## execution_model

- **Human/Cursor** — strategy drafting and review; **not** autonomous campaign execution.

---

## implementation_status

- **Documentation only.**

---

## future_runtime_notes

- May pair with SEO Strategy Agent under a single Task bundle in future Control Plane designs — **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — explicit non-goal: no visual design implementation. |
