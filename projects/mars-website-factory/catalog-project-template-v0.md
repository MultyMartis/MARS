# Operational template — Catalog / PLP-scale project (v0)

**Status:** **documentation-only** pattern for **category + product listing** experiences (catalog sites, large retail, B2B part numbers). **Not** an e-commerce runtime, **not** cart/checkout implementation claims.

**Normative references:** [site-type-registry-v0.md](site-type-registry-v0.md), [block-registry-v0.md](block-registry-v0.md), [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md), [semantic-object-model-v0.md](semantic-object-model-v0.md) (`navigation_entity`, `offer_object`), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md).

---

## 1. Category hierarchy

| Level | Semantic job | Typical artifacts |
|-------|--------------|-------------------|
| L1 — Site root | Brand + top navigation | IA, global nav blueprint |
| L2 — Department / mega-category | User mental model | Category strategy doc |
| L3 — Subcategory | SEO + facet entry | PLP blueprint per template |
| L4+ — (optional) | Deep technical catalogs | Facet taxonomy doc |

**Internal linking:** document hub/spoke and breadcrumb policy per [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md).

---

## 2. PLP (product listing page) semantics

- **Primary listing objective** — compare vs buy vs research ([page-objective-model-v0.md](page-objective-model-v0.md)).
- **Default sort** and **why** (aligns to conversion intent).
- **Empty state** — honest messaging when no products match (**SAFE UNKNOWN** for live inventory unless integrated).

---

## 3. Product trust

- **Card-level** trust: ratings, badges, certifications — **evidence-backed** only ([trust-semantics-v0.md](trust-semantics-v0.md)).
- **Spec tables** — unit consistency; link to canonical PIM/source (**SAFE UNKNOWN** if no PIM).

---

## 4. Filter risks

| Risk | Documentation response |
|------|------------------------|
| Facet explosion | Cap facets; document performance **assumptions** as **SAFE UNKNOWN** for real stack |
| Dead-end filters | UX + QA: zero-result path |
| SEO crawl traps | URL parameter policy in SEO/IA docs ([seo-intent-model-v0.md](seo-intent-model-v0.md)) |
| Inconsistent filter labels | Semantic consistency rules |

---

## 5. SEO structure

- **Templates vs instances** — which fields vary per PLP (H1, intro, canonical).
- **Pagination / rel** strategy — document intent; **no** claim of automated crawl budget fix.
- **Thin category pages** — escalate to HITL if content cannot support indexable quality.

---

## 6. Internal linking

- **Related categories**, **breadcrumbs**, **editorial** links — per [site-semantic-graph-v0.md](site-semantic-graph-v0.md) (conceptual graph).
- **Cannibalization** — PLP vs blog vs promo landing overlap ([multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)).

---

## 7. Scalable frontend constraints

Align with **Gulp Frontend Agent** discipline ([frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)):

- **Component boundaries** for product cards, filters, pagination.
- **SCSS modularity** — avoid unmaintainable mega-selectors.
- **data-*** hooks for filter JS — no inline magic numbers without design tokens.
- **No `dist/` hand edits** — rebuild from source.

---

## 8. QA focus

- **Filter + sort** state persistence (document expected behavior).
- **Accessibility** — keyboard traps in facets.
- **Cross-page** price/stock consistency — if static demo, label as demo ([safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md)).

---

## 9. SAFE UNKNOWN

- Live **inventory**, **pricing**, **tax** engines — **unknown** until integration spec exists.
- Search backend (Algolia, etc.) — **unknown** for this repo’s doc phase.

---

*Template v0 — structure and honesty for large catalog surfaces.*
