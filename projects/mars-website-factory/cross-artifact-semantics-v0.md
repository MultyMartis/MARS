# MARS Website Factory — Cross-Artifact Semantics v0

**Status:** **documentation only** — how **semantic objects** move **across artifact classes** in the factory pipeline. Describes **obligations and handoff discipline**, not automatic serialization or runtime sync.

**Version:** v0.

**Related:** [artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md), [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md).

---

## 1. Artifact columns and semantic flow

Semantic objects are **re-stated or referenced** at each stage; downstream artifacts **must not invent** upstream meaning without a new revision and explicit invalidation handling.

| Stage / artifact | Role for semantic objects |
|------------------|---------------------------|
| **Blueprint** | **Canonical bind** for page/section: IDs, labels, intent fields, trust/CTA/SEO/geo/navigation bindings per [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [section-payload-model-v0.md](section-payload-model-v0.md). |
| **Design** | **Visual realization** of the same objects: emphasis, grouping, states — may not change **commercial or legal meaning** without upstream revision. |
| **Frontend** | **Implementation realization**: URLs, `data-*`, text nodes, schema markup — must trace to blueprint/design lineage. |
| **QA** | **Evidence-based** comparison of implemented vs declared semantics ([qa-prompt-rules-v0.md](qa-prompt-rules-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md)). |
| **Delivery** | **Frozen snapshot** of semantic objects as released; post-delivery drift is a **new lifecycle** episode ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)). |

---

## 2. Propagation patterns (examples)

### 2.1 CTA propagation

- Blueprint declares `cta_object` (primary + alternates).
- Design reflects hierarchy (color, size, placement).
- Frontend encodes hrefs, forms, tracking policy per handoff.
- **Mismatch:** Design adds a **new** primary CTA not in blueprint → **semantic mismatch**; fix by blueprint revision + invalidation, not silent Design→Frontend skip.

### 2.2 Trust propagation

- `trust_object` and `proof_entity` flow: Blueprint → Design presentation → Frontend markup (e.g. quotes, logos, schema).
- **Trust propagation** fails when Frontend uses different attribution or removes disclaimers present in Blueprint.

### 2.3 SEO propagation

- `seo_intent` from Strategy/Blueprint constrains titles, H1 patterns, internal links in Frontend.
- **SEO propagation** to **Delivery** includes meta templates and canonical policy; changing slug/primary keyword without IA invalidation is **semantic downgrade** risk.

### 2.4 Geo propagation

- `geo_object` flows into NAP sections, maps, local FAQ, `direct_contact` CTAs.
- Multi-page sites: cluster pages must **inherit** or **explicitly narrow** geo — silent divergence is **geo inconsistency** ([semantic-consistency-rules-v0.md](semantic-consistency-rules-v0.md)).

### 2.5 Navigation propagation

- `navigation_entity` originates in IA; Blueprint per page may override **local** nav only within contract.
- Frontend nav components must match **approved** IA snapshot; changing labels only in Frontend is **orphan navigation semantics**.

---

## 3. Failure modes (vocabulary)

| Term | Definition |
|------|------------|
| **Semantic mismatch** | Two artifacts assert incompatible meaning for the same scope (e.g. different primary CTA). |
| **Semantic drift** | Gradual divergence over revisions without a single incompatible event — often caught by **stale QA** or spot review. |
| **Semantic downgrade** | Meaning **weakened** vs approved baseline (e.g. removal of required disclaimer, loss of trust signal) without HITL. |
| **Semantic freeze break** | Change to a **frozen** semantic object or relationship without following [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) — invalidates downstream approvals/QA per execution semantics. |

---

## 4. Relationship to transfer rules

[artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md) governs **immutability, lineage, approval inheritance**. This document adds: **which semantic object classes** must appear in **transfer notes** when an artifact is handed off. Omission → **SAFE UNKNOWN** consumption risk.

---

## 5. SAFE UNKNOWN

- Wire format (JSON blocks) for semantic objects in handoff files — **not** defined in v0.
- Whether external DAM/CMS holds a parallel copy of `proof_entity` — outside MARS pack.

---

*End of Cross-Artifact Semantics v0.*
