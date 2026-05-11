# Agent card — SEO Strategy Agent (v0)

**Documentation-first:** **planned** role — **not** runtime, **not** autonomous SEO service. **Human/Cursor workflows** execute this lane today. **Future MARS runtime** is **planned only**.

---

| Field | Value |
|--------|--------|
| **agent_id** | `seo_strategy_agent` |
| **display_name** | SEO Strategy Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S03_STRATEGY`
- [SEO / marketing layer](../../projects/mars-website-factory/seo-marketing-layer.md)
- [Site Type Registry v0](../../projects/mars-website-factory/site-type-registry-v0.md)
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **SEO architecture:** topical clusters, intent mapping, and on-page strategy hypotheses aligned with `site_type_id`.
- **Page hierarchy:** guidance for IA (parent/child topics, hub/spoke intent) — feeds IA Agent downstream, not a final sitemap alone.
- **GEO logic:** market/language/region considerations where evidenced; otherwise **SAFE UNKNOWN**.
- **AI visibility considerations:** best-practice documentation-level guidance (e.g. clear structure, factual grounding) — **not** guarantees of AI citation or inclusion.
- **Internal linking logic:** rationale for cross-page reinforcement consistent with approved IA direction.
- **Commercial SEO structure:** balance of informational vs transactional pages in **hypothesis** form, aligned with Marketing Strategy Agent outputs.

---

## non_goals

- **Forbidden: fake ranking guarantees** — no promised positions, traffic levels, or timelines without measured data and explicit scope.
- **Forbidden: fake AI inclusion guarantees** — no claims that content will appear in LLM answers, AI Overviews, or third-party AI surfaces.
- Does **not** implement schema, meta tags, or live technical deploys (frontend/SEO QA lanes).
- Does **not** replace legal/compliance review for regulated claims.

---

## upstream_inputs

- Intake; **`site_type_id`**; brand guidelines (**if** any); marketing strategy pack from parallel Stage 3 work.

---

## downstream_outputs

- SEO hypothesis doc; risks; topics/intent narrative — paired with strategy memo from Workflow v0 Stage 3.

---

## contracts_used

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)
- [Page Blueprint Contract v0](../../projects/mars-website-factory/page-blueprint-contract-v0.md) — downstream consumer of SEO fields at blueprint time (by reference).

---

## registries_used

- **Site Type Registry v0**; **Block Registry v0** (indirect) per Workflow v0 Stage 3.

---

## qa_relationships

- **SEO QA Agent** (planned) provides checklist depth on implemented pages; **Validator Agent (integration)** for cross-stage policy consistency — **planned**, no omniscient automation claim ([qa-validation-model.md](../../projects/mars-website-factory/qa-validation-model.md)).

---

## escalation_rules

- Conflicting SEO vs commercial goals → **NEED HUMAN APPROVAL** or **STRUCTURE CHANGE**; block IA until resolved (Workflow v0).

---

## HITL_requirements

- **G2:** marketing lead approves SEO hypotheses with strategy per Workflow v0.

---

## SAFE_UNKNOWN_policy

- SERP/competitive data not available → document **SAFE UNKNOWN**; do not invent competitor metrics or search volumes.

---

## execution_model

- **Human/Cursor** research and drafting — **not** autonomous crawlers or rank trackers unless explicitly contracted and evidenced.

---

## implementation_status

- **Documentation only.**

---

## future_runtime_notes

- May consume allowed research tools under Tool Layer when implemented — **SAFE UNKNOWN** today.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — explicit forbids on ranking and AI visibility guarantees. |
