# Agent card — Information Architecture Agent (v0)

**Documentation-first:** **planned** role — **not** a live sitemap engine, **not** autonomous site generation. **Human/Cursor** execution today. **Future MARS orchestration** **planned only**; **no autonomous runtime** in this repository.

---

| Field | Value |
|--------|--------|
| **agent_id** | `information_architecture_agent` |
| **display_name** | Information Architecture Agent |
| **status** | `planned` |
| **layer** | Website Factory / Agent Layer |
| **parent_system** | `mars_website_factory` |

---

## capability_links

- [Site Type Registry v0](../../projects/mars-website-factory/site-type-registry-v0.md)
- [SEO Strategy Agent](./seo-strategy-agent-v0.md)
- [SEO / marketing layer](../../projects/mars-website-factory/seo-marketing-layer.md) — intent and on-page hierarchy inputs (hypothesis-level; no ranking claims)
- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md) — Stage `WF_V0_S04_IA`
- [Agent map](../../projects/mars-website-factory/agent-map.md)

---

## primary_responsibilities

- **Navigation structure:** primary/secondary nav models, mega-menu vs flat decisions, wayfinding aligned to **site_type_id** and approved strategy.
- **Page hierarchy:** parent/child relationships, hub vs spoke patterns, template families vs one-off pages.
- **URL logic:** slug patterns, canonical URL intent, versioning/migration notes when legacy maps exist (**SAFE UNKNOWN** when stack/CMS undecided).
- **SEO hierarchy:** how topical clusters and pillar/support pages relate to **SEO Strategy** outputs — structure only, not performance guarantees.
- **Trust distribution:** where proof, policy, credentials, and social proof surfaces live in the tree relative to conversion paths.
- **Route planning:** critical user journeys mapped to concrete routes; dead-end avoidance per Workflow v0 Stage 4 QA gates.
- **Commercial structure:** alignment of service/product URLs, pricing or lead paths, and CTA destinations with **Marketing Strategy** narrative.

---

## non_goals

- Does **not** generate **arbitrary page trees without business evidence** — every major node needs traceability to intake, strategy, or explicit **HITL**-approved assumption (**SAFE UNKNOWN** documented, not invented scope).
- Does **not** own per-page block ordering (see **Page Blueprint Agent**).
- Does **not** produce final visual design, wireframes, or HTML/CSS.

---

## upstream_inputs

- Approved intake; **site_type_id**; strategy + SEO hypothesis artifacts — Workflow v0 Stage 4.

---

## downstream_outputs

- IA pack: sitemap, template list, URL/content requirements, navigation spec — shapes Stage 5 blueprints.

---

## contracts_used

- [Website Factory Workflow v0](../../projects/mars-website-factory/website-factory-workflow-v0.md)

---

## registries_used

- **Site Type Registry v0**; **Block Registry v0** (template ↔ block expectations per Workflow v0).

---

## qa_relationships

- Stage 4 QA gates (reachability, journey coverage); contradictions with strategy/SEO → escalate before blueprint work.
- **Blueprint QA** and downstream SEO/Conversion QA consume IA assumptions — gaps should surface as **SAFE UNKNOWN** or **STRUCTURE CHANGE**, not silent fixes.

---

## escalation_rules

- **CTA flow impossible** given IA → return to Strategy or IA with **STRUCTURE CHANGE** (Workflow v0).
- **Unknown stack** (CMS/hosting/routing) → **SAFE UNKNOWN** with explicit documented assumptions.

---

## HITL_requirements

- **G3** (partial): PM + tech lead on scope/size; major IA shifts may re-trigger **G2** (Workflow v0).

---

## SAFE_UNKNOWN_policy

- Undecided hosting/CMS/routing → flag **SAFE UNKNOWN**; do not fabricate URL implementation detail.
- When registry has no matching template pattern → propose registry amendment or **park** — no silent best-guess expansion of the tree.

---

## execution_model

- **Human/Cursor** authoring of IA documents and diagrams — **not** an autonomous site crawler or auto-sitemap service.

---

## implementation_status

- **Documentation only** — no IA engine or persisted graph service in-repo for Website Factory.

---

## future_runtime_notes

- Control Plane might validate sitemap graphs against contracts when schemas exist — **TBD**.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-11 | v0 card — IA stage; Site Type Registry, SEO Strategy pack, Workflow v0 references. |
