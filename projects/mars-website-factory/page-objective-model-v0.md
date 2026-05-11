# MARS Website Factory — Page objective model v0

**Status:** **documentation only** — semantic vocabulary for **page-level intent** aligned with [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) (`page_goal`, `commercial_intent`, `SEO_intent`, `CTA_strategy`, `trust_strategy`). **Not** a scoring engine or automated classification service.

**Related:** [seo-intent-model-v0.md](seo-intent-model-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md).

---

## Core dimensions

| Concept | Definition |
|---------|------------|
| **Primary objective** | The **single** outcome the page optimizes for (one URL, one primary). |
| **Secondary objective** | Supporting outcomes (education, trust, navigation) that must **not** eclipse the primary without HITL. |
| **Conversion class** | Coarse bucket: `lead`, `call`, `local_visit`, `transaction`, `browse_plp`, `soft_engagement`, `entity_clarity` — align with **site_type_id** rows, not a closed global enum unless registry extends. |
| **Intent class** | User task intent the page matches (informational, commercial, navigational, local, entity). |
| **Informational / commercial balance** | How much of the page serves **learn/read** vs **act/buy**; mismatches vs **commercial_intent** trigger escalation. |
| **SEO acquisition intent** | What **search** or **discovery** demand the page honestly serves ([seo-intent-model-v0.md](seo-intent-model-v0.md)). |
| **CTA expectations** | Primary/secondary/sticky rules per [cta-semantics-v0.md](cta-semantics-v0.md) and blueprint **CTA_strategy**. |
| **Trust requirements** | Minimum proof surfaces and **forbidden claims** per [trust-semantics-v0.md](trust-semantics-v0.md) and **trust_strategy**. |
| **Escalation cases** | Conflicting objectives, regulated claims, geo falsification risk, AI-surface misrepresentation → **NEED HUMAN APPROVAL** or **STRUCTURE CHANGE**. |

---

## Examples (illustrative)

### Service landing

| Field | Example |
|-------|---------|
| **Primary objective** | Qualified lead (inspection request). |
| **Secondary** | Educate on process; reduce anxiety. |
| **Conversion class** | `lead` + `call` secondary. |
| **Intent class** | Commercial + local transactional. |
| **Balance** | Medium copy depth; commercial bias after proof. |
| **SEO acquisition** | Local service queries. |
| **CTA expectations** | One primary **lead_capture**; tel/sticky as secondary. |
| **Trust** | Licenses, cases, real reviews only. |
| **Escalation** | Guaranteed outcomes, unverifiable stats. |

### GEO page

| Field | Example |
|-------|---------|
| **Primary objective** | Correct local conversion (order / zone check). |
| **Secondary** | Clarify coverage vs hub. |
| **Conversion class** | `local_visit` / `transaction` per business. |
| **Intent class** | Local + commercial. |
| **Balance** | Operational truth first; commercial second. |
| **SEO acquisition** | Geo-modified queries; **no** thin clones. |
| **CTA expectations** | Primary aligned with true polygon; hub link secondary. |
| **Trust** | **local_trust**, maps, hours — must match ops. |
| **Escalation** | Polygon drift; “serves everywhere” when not true. |

### Catalog page (PLP)

| Field | Example |
|-------|---------|
| **Primary objective** | Faceted browse + PDP click-through; optional RFQ. |
| **Secondary** | Category education, comparison. |
| **Conversion class** | `browse_plp` + optional `lead`. |
| **Intent class** | Commercial + informational support. |
| **Balance** | Spec-led cards + optional deep intro. |
| **SEO acquisition** | Category head + long-tail; facet policy in technical addendum. |
| **CTA expectations** | **catalog_navigation** primary; RFQ secondary where valid. |
| **Trust** | Brands, certifications; **no** fake stock/price. |
| **Escalation** | Thin faceted URLs; incompatible RFQ density. |

### AI visibility page

| Field | Example |
|-------|---------|
| **Primary objective** | Citable **entity** facts; reduce misinformation risk. |
| **Secondary** | Corrections channel; deep methodology (optional). |
| **Conversion class** | `soft_engagement` / `entity_clarity`. |
| **Intent class** | Entity + informational; **not** disguised hard-sell. |
| **Balance** | Information-heavy; commercial cues minimal and honest. |
| **SEO acquisition** | Branded + entity clarification — **not** a promise of LLM inclusion. |
| **CTA expectations** | Late, soft **direct_contact** or correction path only. |
| **Trust** | Sources, dates, explicit limits of control over third-party models. |
| **Escalation** | Overclaiming model behavior; fake FAQs for schema. |

---

*Last updated: 2026-05-11.*
