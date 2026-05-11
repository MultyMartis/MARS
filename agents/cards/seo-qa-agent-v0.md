# Agent card — SEO QA Agent (v0)

**Documentation-first:** **planned** role — **not** a live SEO crawler or ranking monitor in MARS. **Human/Cursor** checklist execution. **Future MARS orchestration** **planned only**; **no autonomous runtime**.

---

| Field | Value |
|--------|--------|
| **agent_id** | `seo_qa_agent` |
| **display_name** | SEO QA Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [SEO Strategy Agent](./seo-strategy-agent-v0.md)
- [SEO / marketing layer](../../projects/mars-website-factory/seo-marketing-layer.md) — hypothesis and intent SoT
- [Site Type Registry v0](../../projects/mars-website-factory/site-type-registry-v0.md)
- [Page Blueprint QA Checklist v0](../../projects/mars-website-factory/page-blueprint-qa-checklist-v0.md) — **Blueprint QA** alignment
- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S06_BLUEPRINT_QA`
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **SEO structure validation:** blueprint and IA alignment to approved topic/intent model from **SEO Strategy**.
- **Heading hierarchy:** logical `h1`–`h6` intent vs contract fields; no decorative heading misuse without flag.
- **Metadata logic:** title/description/canonical/social fields per **Page Blueprint Contract v0** where defined.
- **Internal linking checks:** orphan risks, hub/spoke support links, and CTA destinations vs IA graph.
- **Commercial SEO checks:** money-page emphasis, service clustering, and cannibalization flags (**hypothesis-level**, not SERP promises).
- **AI visibility considerations:** summarizability, entity clarity, and structured-data *intent* notes — **SAFE UNKNOWN** for stack-specific rich-result eligibility.

---

## non_goals

- **Must not** issue **fake ranking guarantees** or **fabricated SEO authority claims** — rankings depend on engines, competition, and technical delivery outside blueprint scope.
- Does **not** replace technical SEO implementation audit (server, Core Web Vitals evidence, crawl budget) unless explicitly in scope for a task.
- Does **not** claim indexation, crawl, or analytics integration exists in MARS without evidence.

---

## upstream_inputs

- Blueprint set; IA; strategy/SEO memos — Workflow v0 Stage 6.

---

## downstream_outputs

- SEO QA findings in joint Stage 6 report; severity tags; pass/fail/conditional recommendation.

---

## contracts_used

- **Page Blueprint Contract v0**; **Page Blueprint QA Checklist v0**.
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)

---

## registries_used

- **Site Type Registry v0** (SEO posture defaults).

---

## qa_relationships

- Stage 6 co-primary with **Conversion QA Agent** and **Validator Agent (integration)** — coordinate duplicate checklist items (**TBD** split).
- Blocks Design Handoff until pass or **HITL** waiver (Workflow v0).

---

## escalation_rules

- Strategy vs blueprint SEO conflict → return to Stage 3/5 with **STRUCTURE CHANGE** or approved exception.

---

## HITL_requirements

- Failed or high-risk → **NEED HUMAN APPROVAL** to waive or return to **S05** (Workflow v0 Stage 6).

---

## SAFE_UNKNOWN_policy

- Engine behavior, SERP features, and competitive SERP positions → **SAFE UNKNOWN** unless external data is attached to the task with provenance.

---

## execution_model

- **Human/Cursor** SEO QA checklist — **not** autonomous ranking optimization bot.

---

## implementation_status

- **Documentation only** — no SEO QA engine in MARS core.

---

## future_runtime_notes

- Optional integration with crawl tools or GSC exports — **TBD**; evidence-based documentation only.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — SEO Strategy, Site Type Registry, Blueprint QA; forbid ranking/authority fabrications. |
