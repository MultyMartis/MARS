# WF-R01.3.4 PRODUCT_PAGE Scope Decision v1

**Status:** ACCEPTED  
**Wave:** WF-R01.3.4 Wave C6 — PRODUCT_PAGE Scope or Scaffold Decision  
**Date:** 2026-06-20  
**Authority:** [wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md](wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md) · [wf-r01-3-4-catalog-reference-inventory-v1.md](wf-r01-3-4-catalog-reference-inventory-v1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Document status** | **ACCEPTED** |
| **Stage A** | **COMPLETE** |
| **Stage B decision** | **MINIMAL PRODUCT_PAGE SCAFFOLD AUTHORIZED AND COMPLETED** |
| **Outcome** | **Outcome A** |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Registry ID** | `PRODUCT_PAGE` |
| **Canonical name** | Product PDP |
| **Industry alias** | PDP-like |
| **Registry source** | [PAGE-TYPE-REGISTRY-v1.md](../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) |
| **Site-type applicability** | `CATALOG` (primary) · `ECOMMERCE` · `CORPORATE` (catalog subtree) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.4 Charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | PRODUCT_PAGE contract §12; C6 default |
| Catalog Reference Inventory | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | PDP source readiness §15 |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | REQ/POL/N/A surfaces |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC evidence chain |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RSC · SC · PC |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Canonical block inventory |
| CATEGORY_PAGE composition (pattern) | `workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md` | Scaffold precedent |

---

## 4. Registry Binding

| Binding | Value |
|---------|-------|
| **Registered page type** | Yes — Core minimum set (10 types) |
| **Purpose** | PDP: specs, gallery, trust, conversion (RFQ / ATC / CTA) |
| **Forbidden on LANDING/PROMO** | Yes — catalog subtree only |
| **New Registry IDs created in C6** | **None** |

---

## 5. Shell Matrix Binding

| Surface | Matrix | C6 scaffold |
|---------|--------|-------------|
| HEADER_NAV | REQ | Present — 1 |
| MAIN | REQ | Present — 1 |
| BREADCRUMBS | REQ | Present |
| PAGINATION | N/A | **Absent** |
| FOOTER | REQ | Present — 1 |
| LEGAL_LINKS | REQ (nested) | Present in FOOTER |
| SEARCH slot | POL (header utility) | Via HEADER_NAV only — not duplicated in MAIN |
| FILTERS | N/A | **Absent** |

---

## 6. Source Evidence

| Zone | Source state | Evidence | Decision |
|------|--------------|----------|----------|
| HEADER_NAV | SOURCE READY | Reference partial | Reuse |
| BREADCRUMBS | SOURCE READY | Reference partial | Reuse |
| Product identity | PARTIAL SOURCE | BZPM `producthero.twig` (structural) | Scaffold-owned region |
| Media / gallery | PARTIAL SOURCE | BZPM hero media anatomy | Scaffold-owned placeholder — no gallery `block_id` |
| Commercial zone | PARTIAL SOURCE | BZPM commerce-card patterns | Scaffold-owned region |
| Specifications | PARTIAL SOURCE | BZPM `producttabs.twig` | Scaffold-owned `<dl>` |
| Description | PARTIAL SOURCE | BZPM producttabs description | Scaffold-owned region |
| CTA / lead | PARTIAL SOURCE | Charter bind policy | `LEAD_FORM` canonical partial |
| Related items | SAFE UNKNOWN | No dedicated block | **Excluded** from C6 |
| Trust | Composition zone | Site-specific patterns | `TRUST` partial — optional policy zone |
| FOOTER / LEGAL_LINKS | SOURCE READY | Reference partials | Reuse |

**Inventory verdict (C1 §15):** **PDP SOURCE READY WITH GAPS** — minimal scaffold path authorized.

---

## 7. Canonical PDP Zones

| Zone | Registry backing | C6 treatment |
|------|------------------|--------------|
| Product identity | No dedicated `block_id` | Scaffold-owned |
| Media / gallery | No dedicated `block_id` | Scaffold-owned placeholder |
| Commercial summary | No dedicated `block_id` | Scaffold-owned |
| Specifications | No dedicated `block_id` | Scaffold-owned |
| Description | No dedicated `block_id` | Scaffold-owned |
| LEAD_FORM | `LEAD_FORM` — CATALOG applicable | Canonical partial |
| TRUST | `TRUST` — CATALOG applicable | Canonical partial |
| RELATED_PRODUCTS | **Absent** | Excluded |
| GALLERY / PRODUCT_MEDIA | **Absent** | Not invented |

---

## 8. Existing Block Bindings

| block_id | Partial | C6 use |
|----------|---------|--------|
| HEADER_NAV | `sections/header-nav.html` | Shell |
| BREADCRUMBS | `components/breadcrumbs.html` | MAIN |
| LEAD_FORM | `sections/lead_form.html` | MAIN — CATALOG RFQ path |
| TRUST | `sections/trust.html` | MAIN — policy-dependent |
| FOOTER | `sections/footer.html` | Shell |
| LEGAL_LINKS | `components/legal-links.html` | Nested in FOOTER |

**Not bound:** PRODUCT_CARD · PRODUCT_GRID · FILTERS · PAGINATION · CTA (CTA `allowed_site_types` excludes CATALOG — commercial CTA is scaffold-owned link to `#lead-form`)

---

## 9. Scaffold-Owned Regions

| Region | Why scaffold-owned | Hook policy | Coverage effect |
|--------|-------------------|-------------|-----------------|
| Product identity | No Registry `block_id` | No `data-block-id` | No RPC · no false universal block |
| Media region | No GALLERY/PRODUCT_MEDIA `block_id` | CSS placeholder only | No RPC · SAFE UNKNOWN gallery contract |
| Commercial region | No PDP commerce `block_id` | Static request-price state | No RPC |
| Specification region | No SPECIFICATIONS `block_id` | Semantic `<dl>` | No RPC |
| Description region | No DESCRIPTION `block_id` | Semantic paragraphs | No RPC |
| Primary CTA link | CTA block not CATALOG-applicable | Anchor to `#lead-form` | No RPC |

---

## 10. SAFE UNKNOWN

| Item | Notes |
|------|-------|
| Dedicated gallery `block_id` | Future Registry decision — not in C6 |
| Dedicated specifications `block_id` | Future Registry decision — not in C6 |
| Related products grid | Optional `PRODUCT_GRID` reuse — deferred |
| Tabs / accordion runtime on PDP | No accepted identity — excluded |
| SIBCAR live OpenCart PDP | Prototype-only secondary — not universal canon |
| SEARCH_RESULTS_PAGE scaffold | Coverage Model lists as CATALOG scaffold requirement — **not** a Registry v1 page type; reconciliation deferred to C8 |
| Full PDP vertical depth | Wave C7 binding docs — not C6 |

---

## 11. Product Card Reuse Decision

| Field | Value |
|-------|-------|
| **Registry role** | Listing-unit reference (`PRODUCT_GRID` child) |
| **PDP applicability** | Registry notes “grid or PDP summary” but partial is PLP-card shaped |
| **Decision** | **A — PRODUCT_CARD is not used as PDP core** |
| **Rationale** | C4B partial is grid-card anatomy (h3 title link, compact specs). C6 uses scaffold-owned PDP regions informed by BZPM structural sources. Avoids false listing-card-as-PDP architecture. |

---

## 12. Runtime Exclusions

Excluded from C6 by authority:

- cart · checkout · wishlist · compare
- quantity · variants · live availability
- backend pricing · gallery carousel · zoom
- tabs/accordion runtime · related-products grid
- OpenCart Twig/PHP · BZPM production data · live TEST coupling
- new Registry block IDs · Vocabulary Canon changes

---

## 13. Scope Overload Test

| Risk | Present | Blocking | Decision |
|------|---------|----------|----------|
| Multiple new block IDs | No | — | PASS |
| New gallery contract | No — stub only | — | PASS |
| New specifications contract | No — `<dl>` stub | — | PASS |
| Related-products contract | No — excluded | — | PASS |
| Ecommerce runtime | No | — | PASS |
| Production data / CMS | No | — | PASS |
| Vocabulary Canon change | No | — | PASS |
| Hidden C7 vertical implementation | No | — | PASS |
| Full PDP design system | No | — | PASS |

**Verdict:** Scope overload **not detected** — minimal scaffold authorized.

---

## 14. Scaffold Authorization Decision

```text
MINIMAL PRODUCT_PAGE SCAFFOLD AUTHORIZED
```

Stage B executed. Deliverables:

- `src/pages/product-page-reference.html`
- `page-architecture/PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md`
- `page-architecture/PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md`
- `src/scss/pages/_product-page-reference.scss`

---

## 15. Coverage Implications

| Dimension | Before C6 | After C6 (evidence-based) |
|-----------|-----------|---------------------------|
| **RC** | 32/32 | **32/32** (unchanged) |
| **RPC** | 23/32 | **23/32** (unchanged — reuse only) |
| **RSC** | 2/10 · 1/1 LANDING · 1/1 CATEGORY_PAGE | **3/10 · 1/1 LANDING · 1/1 CATEGORY_PAGE · 1/1 PRODUCT_PAGE** |
| **SC** | LANDING PASS · CATALOG PARTIAL | **LANDING PASS · CATALOG PARTIAL** (unchanged — C8 required) |
| **PC** | 1/1 LANDING · 1/1 CATALOG corridor | **1/1 LANDING · 1/1 CATALOG corridor** (PRODUCT_PAGE composition extends corridor evidence; numerator unchanged until C8) |

---

## 16. CATALOG SC Implications

CATALOG SC remains **PARTIAL**. Completed toward minimum set:

- CATEGORY_PAGE scaffold ✓
- PRODUCT_PAGE scaffold ✓ (C6)
- Catalog partials (FILTERS · SEARCH · grids/cards) ✓

**Remaining:**

- SEARCH_RESULTS_PAGE scaffold (Coverage Model § CATALOG scaffolds — **no Registry v1 page type**; matrix documents as future extension)
- Wave C8 formal evaluation
- Vertical profile binding (C7 — documentation)

**Decision:** CATALOG SC **cannot** advance to PASS in C6.

---

## 17. Handoff

| Next | Authority |
|------|-----------|
| **WF-R01.3.4 Wave C7 — Vertical Profile Binding** | MANUFACTURER + AUTO binding docs; no live-site dependency |
| **Wave C8** | G2 readiness evaluation; SEARCH_RESULTS_PAGE authority reconciliation |

PRODUCT_PAGE scaffold **does not block** C7 — vertical binding may proceed with honest partial states.

---

## 18. Evidence Paths

- `workspaces/website-factory-reference-v1/src/pages/product-page-reference.html`
- `workspaces/website-factory-reference-v1/dist/product-page-reference.html`
- `workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md`
- `workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md`
- `workspaces/website-factory-reference-v1/src/scss/pages/_product-page-reference.scss`
- `reports/wf-r01-3-4-wave-c6-product-page-decision-v1.md`

---

## 19. Decision

```text
PRODUCT_PAGE SCOPE ACCEPTED
MINIMAL PRODUCT_PAGE SCAFFOLD AUTHORIZED AND COMPLETED
```

*Scope decision version: v1 · Wave C6 · ACCEPTED.*
