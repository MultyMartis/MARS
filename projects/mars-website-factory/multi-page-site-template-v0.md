# Operational template — Multi-page site (v0)

**Status:** **documentation-only** pattern for **site-level** coherence beyond a single landing. **Not** automated graph maintenance or runtime cluster optimization.

**Normative references:** [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md), [site-semantic-graph-v0.md](site-semantic-graph-v0.md), [semantic-inheritance-v0.md](semantic-inheritance-v0.md), [dependency-invalidation-v0.md](dependency-invalidation-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md).

---

## 1. Cluster logic

| Cluster | Pages included | Primary authority page | Notes |
|---------|----------------|------------------------|-------|
| | | | |

**Cluster** = shared intent / shared proof / shared conversion story. Document **why** pages belong together.

---

## 2. Page hierarchy

- **Depth** vs **breadth** tradeoff for navigation ([semantic-object-model-v0.md](semantic-object-model-v0.md) `navigation_entity`).
- **Entry paths** — organic vs paid vs direct (assumptions marked **SAFE UNKNOWN** if channel data absent).

---

## 3. Navigation

- Global nav **order** and **grouping** — IA artifact.
- **Footer** legal/support links — ownership (often HITL with counsel).
- **Cross-links** — editorial vs template-driven ([site-semantic-graph-v0.md](site-semantic-graph-v0.md)).

---

## 4. Trust inheritance

Per [semantic-inheritance-v0.md](semantic-inheritance-v0.md) — **inheritance ≠ runtime propagation**; it is a **documentation rule** for consistency:

- Site-level **trust_object** defaults and page-level overrides.
- **When override is forbidden** (regulated claims).

---

## 5. Semantic graph considerations

- **Authority flow** — which page may claim “official” pricing, policy, warranty.
- **GEO trees** — parent region vs child city pages ([geo-landing-template-v0.md](geo-landing-template-v0.md)).
- **Offer** consistency — promotions scoped per page vs site-wide.

---

## 6. Invalidation propagation

When page **P** changes:

| Change type | Likely invalidated pages | QA scope |
|-------------|---------------------------|----------|
| Primary CTA / offer | Cluster siblings, hub | Full cluster QA |
| Proof / certification | All pages citing same proof | Cross-artifact QA |
| Nav restructure | Entire site frontend | Site-level regression narrative |

Use [dependency-invalidation-v0.md](dependency-invalidation-v0.md) and [artifact-transfer-qa-rules-v0.md](artifact-transfer-qa-rules-v0.md) vocabulary.

---

## 7. QA focus

- **Page vs site** QA matrix rows ([reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md)).
- **Cannibalization** checks ([multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)).

---

## 8. SAFE UNKNOWN

- Live **analytics** on internal search / nav effectiveness — **unknown** until measurement spec exists.

---

*Template v0 — conceptual graph and handoff discipline only.*
