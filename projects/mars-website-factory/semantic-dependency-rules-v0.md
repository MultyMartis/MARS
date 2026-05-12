# MARS Website Factory — Semantic Dependency Rules v0

**Status:** **documentation only** — **normative patterns** for which semantic changes **should** invalidate or re-open which downstream artifacts, approvals, and QA. **Not** an invalidation engine; aligns with [dependency-invalidation-v0.md](dependency-invalidation-v0.md) and adds **semantic-class** triggers.

**Version:** v0.

**Related:** [semantic-relationship-overview-v0.md](semantic-relationship-overview-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [regeneration-semantics-v0.md](regeneration-semantics-v0.md), [cta-semantics-v0.md](cta-semantics-v0.md), [trust-semantics-v0.md](trust-semantics-v0.md), [seo-intent-model-v0.md](seo-intent-model-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md).

---

## 1. Dependency kinds

| Kind | Definition | Example |
|------|------------|---------|
| **Hard dependency** | Downstream meaning **cannot** stay valid without revisiting if upstream changes. | Primary `cta_object` label/destination change → Conversion QA stale. |
| **Soft dependency** | Downstream **should** be reviewed; may remain valid with explicit waiver + evidence. | CTA color tweak only (Design) → may not invalidate SEO QA. |
| **Semantic dependency** | Dependency **through meaning**, not file path (may span sections). | `offer_object` price claim change → FAQ + trust surfaces. |
| **Visual dependency** | Design-only layout dependency with no semantic content change — still may require **Design QA** rerun, not always semantic invalidation. |
| **Trust dependency** | Any change that touches credibility, compliance, or proof. | New `proof_entity` without release → blocks delivery. |
| **SEO dependency** | Affects cannibalization, intent, or technical SEO truth. | `seo_intent` primary topic change → related page cluster QA. |
| **Navigation dependency** | Affects IA graph, breadcrumbs, internal link equity. | `navigation_entity` rename → all linked pages’ Frontend nav. |
| **Cluster dependency** | Multi-page **shared** semantic baseline ([multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)). | Service merge → cluster-wide Blueprint + SEO QA. |

---

## 2. Invalidation severity (semantic)

| Severity | Meaning | Typical handling |
|----------|---------|------------------|
| **S0 — blocking** | Delivery / release **must not** proceed until resolved. | Contradictory legal/geo; fake trust category per policy. |
| **S1 — lane reset** | Named QA lane verdicts stale for scope. | CTA change → Conversion QA reset. |
| **S2 — artifact reset** | Specific artifact revision stale. | Hero blueprint section after `cta_object` change. |
| **S3 — advisory** | Human judgment; optional waiver. | Minor CTA microcopy if conversion risk accepted. |

---

## 3. Illustrative rules (documentation patterns)

Patterns use **“invalidates”** as **should be declared stale / rerun** — **not** auto-execution.

### 3.1 CTA change

```text
CTA change (primary label, destination, or friction class)
  → invalidates Conversion QA (typically S1)
  → may invalidate Hero blueprint/design/frontend (S2) if hero embodies CTA
  → may invalidate sticky CTA implementations site-wide (S2, scope-bounded)
  → does not necessarily invalidate IA (S3 / none) unless CTA change reflects new audience/route
```

### 3.2 Trust / proof change

```text
proof_entity or trust_object material change
  → invalidates Conversion QA + Design QA for affected surfaces (S1)
  → may invalidate SEO QA if schema or on-page claims touched (S1–S2)
  → may invalidate FAQ entity bindings (S2)
```

### 3.3 SEO intent change

```text
seo_intent primary change
  → invalidates SEO QA for page + declared neighborhood (S1–cluster)
  → may invalidate IA if URL/topic ownership shifts (S0–S1, STRUCTURE CHANGE risk)
  → may invalidate internal link navigation_entity references (S2)
```

### 3.4 Geo change

```text
geo_object service area change
  → invalidates local trust blocks, map modules, NAP Frontend (S1–S2)
  → may invalidate SEO QA (doorway / thin local pages) (S1)
```

### 3.5 Navigation change

```text
navigation_entity (global) change
  → cluster dependency: invalidates Frontend nav consuming artifact + Blueprint QA for label consistency (S1–S2)
```

---

## 4. Propagation scope

- **Page-local** — default when change is scoped to one blueprint.
- **Cluster** — topic/service cluster per reference project / multi-page docs.
- **Site-wide** — global nav, site-wide trust policy, shared CTA policy.

Partial rerun semantics match [dependency-invalidation-v0.md](dependency-invalidation-v0.md) §5–6: **scope-bounded**, **HITL-anchored**, **explicit in REPORT**.

---

## 5. SAFE UNKNOWN handling

When **dependency strength** (hard vs soft) is unclear:

1. Emit **SAFE UNKNOWN** with what is unknown and suggested default severity (**bias to S1** when conversion/legal/trust touched).
2. Record **NEED HUMAN APPROVAL** if waiver would downgrade severity.
3. **Do not** assume “no invalidation” for trust/offer/geo/primary CTA edits.

---

## 6. Explicit non-claims

- No **graph traversal runtime** computing closures.
- No **automatic partial rerun** — operators and prompts decide rerun scope per governance.

---

*End of Semantic Dependency Rules v0.*
