# MARS Website Factory — Section payload model v0

**Status:** **documentation only** — **semantic** structure for a **page section** (aligned with **`block_id`** from [block-registry-v0.md](block-registry-v0.md)). This is **not** implementation JSON, **not** final React/Vue props, **not** a runtime schema, and **not** enforced serialization.

**Related:** [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md) (**block_mapping**), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md).

---

## Purpose

Give authors (human or future agent) a **checklist-shaped** way to describe each section’s **role in the page story**: objectives, dependencies, adjacency rules, and QA hooks. Payloads remain **prose-first** in v0; tabular encoding is optional.

---

## Conceptual fields (per section instance)

| Concept | Description |
|---------|-------------|
| **section_id** | Project-scoped instance id (e.g. `hero_main`, `faq_pricing`) — disambiguates repeated block patterns. |
| **section_role** | Maps to **`block_id`**; may add instance qualifier in **notes**. |
| **objective** | What this section must achieve for the [page objective model](page-objective-model-v0.md). |
| **CTA relation** | Primary/secondary/none; links to [cta-semantics-v0.md](cta-semantics-v0.md) labels. |
| **trust relation** | Which [trust-semantics-v0.md](trust-semantics-v0.md) categories this section supports or consumes. |
| **SEO role** | Heading duty, snippet support, schema honesty — see [seo-intent-model-v0.md](seo-intent-model-v0.md). |
| **hierarchy_level** | Outline / landmark importance (e.g. sole H1 carrier vs supporting). |
| **mobile_importance** | `critical` / `standard` / `defer` for above-fold and tap priority. |
| **scanability** | Expected skim pattern (chips, bullets, accordions, tables). |
| **required_dependencies** | Upstream content/legal approvals, assets, data feeds. |
| **forbidden_adjacency** | e.g. **final_cta** immediately after thin **hero** without proof; two competing primaries. |
| **QA hooks** | Assertions reviewers check (contrast, accordion keyboard, stock truth). |

---

## Examples (illustrative prose bundles)

### hero

- **objective:** Establish offer + primary geo/service in one scan.
- **CTA relation:** Often carries **primary** CTA semantic (`lead_capture` or `direct_contact`).
- **trust relation:** Light **expertise** or **local** cue acceptable; avoid fake review stars.
- **SEO role:** Single H1; aligned with **SEO_intent**.
- **forbidden_adjacency:** Long legal wall before first value prop (unless regulated vertical requires it — HITL).

### faq

- **objective:** Resolve objections; support honest **FAQPage** only if Q&A real.
- **CTA relation:** Usually **micro_conversion** or none; may anchor to **estimate_request**.
- **trust relation:** **operational_trust**, **transparency_trust**.
- **SEO role:** High when queries are question-shaped; **thin boilerplate** forbidden.

### pricing

- **objective:** Clarify commercial terms or ranges.
- **CTA relation:** Often pairs with **estimate_request** or **consultation**.
- **trust relation:** **compliance_trust**, **transparency_trust**.
- **forbidden_adjacency:** Surprise mandatory upsell modals from pricing table rows.

### geo_trust

- **objective:** Prove locality and service reality.
- **CTA relation:** Supports **direct_contact** / **catalog_navigation** after trust.
- **trust relation:** **local_trust** core surface.
- **QA hooks:** Polygon, hours, photos — ops-verified.

### calculator

- **objective:** Interactive scoping (materials, ROI, loan).
- **CTA relation:** Often **estimate_request** bridge.
- **trust relation:** **transparency_trust** (inputs/limits); **compliance** if financial.
- **required_dependencies:** Formula source, legal disclaimer, error bounds.

### final_cta

- **objective:** Repeat **primary** with reduced cognitive load.
- **CTA relation:** Same semantic as hero primary — **no** competing label without HITL.
- **forbidden_adjacency:** Immediately after unrelated **catalog_grid** without transition copy.

---

## SAFE UNKNOWN

Per-section props schema, machine diff format, and automated adjacency validation — **not** specified in v0.

---

*Last updated: 2026-05-11.*
