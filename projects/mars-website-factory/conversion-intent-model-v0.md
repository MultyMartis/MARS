# MARS Website Factory — Conversion intent model v0

**Status:** **documentation only** — extends **commercial_intent**, **CTA_strategy**, and **conversion_points** from [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md). **Not** funnel analytics as implemented here, **not** guaranteed conversion rates.

**Related:** [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md).

---

## Core thesis

**Conversion ≠ only forms.** Conversion intent covers **any** measurable user commitment path: call, visit, cart, signup, save-for-later, or **soft** progress — always **honest** about friction and next steps.

---

## Dimensions

| Dimension | Meaning |
|-----------|---------|
| **Primary conversion** | Single dominant outcome per URL (align **page_goal**). |
| **Secondary conversion** | Allowed supporting paths — must not hijack primary without HITL. |
| **Conversion friction** | Cognitive steps, fields, prerequisites, trust gaps — **document**, do not hide. |
| **Trust friction** | User reluctance drivers (price fear, privacy, complexity) addressed by **trust_strategy** ordering. |
| **CTA readiness** | Implied user stage vs CTA depth (e.g. **catalog_navigation** before **lead_capture** on cold PLP traffic). |
| **Page maturity** | Narrative readiness for “money” modules: proof present, legal clear, tracking consented. |
| **Escalation triggers** | Conflicting primaries, dark patterns, missing consent on PII, impossible **sticky_cta** behavior per IA. |

---

## Relationship to SEO intent

Commercial pages often blend **SEO** and **conversion** intents. **Escalation** when **SEO_intent** is informational but **commercial_intent** is `high` with aggressive CTAs — requires **NEED HUMAN APPROVAL** or IA/blueprint split.

---

## Explicit non-claims

No **conversion lift** promises, no **psychological manipulation** playbook, and **no** automated CTA scoring in v0.

---

*Last updated: 2026-05-11.*
