# PRODUCT_PAGE Scaffold Manifest v1

**Page type:** `PRODUCT_PAGE`  
**Site type:** `CATALOG` (primary)  
**Scaffold file:** `src/pages/product-page-reference.html`  
**Output:** `dist/product-page-reference.html`  
**Status:** STRUCTURALLY VALIDATED · STUB-DECLARED  
**Metric:** RSC — global **+1** when Wave C6 evidence accepted

**Authority:** [wf-r01-3-4-product-page-scope-decision-v1.md](../../projects/mars-website-factory/wf-r01-3-4-product-page-scope-decision-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

---

## Manifest identity

| Field | Value |
|-------|-------|
| **manifest_version** | v1 |
| **status** | STRUCTURALLY VALIDATED |
| **page_type** | `PRODUCT_PAGE` |
| **site_type_code** | `CATALOG` (primary); also `ECOMMERCE`, `CORPORATE` catalog subtree |
| **Scaffold path** | `workspaces/website-factory-reference-v1/src/pages/product-page-reference.html` |
| **Dist path** | `workspaces/website-factory-reference-v1/dist/product-page-reference.html` |
| **Build command** | `npm run build` (in reference workspace) |
| **Global RSC denominator** | **10** primary page types (PAGE-TYPE-REGISTRY-v1 Core minimum set) |
| **Global RSC numerator (post-C6)** | **3** — `LANDING_PAGE` + `CATEGORY_PAGE` + `PRODUCT_PAGE` |
| **CATALOG corridor RSC** | **2/3** scaffolds — CATEGORY_PAGE + PRODUCT_PAGE (SEARCH_RESULTS_PAGE deferred) |
| **Commit binding** | `c8a661d` — `foundry: complete WF-R01.3.4 product page scaffold` |

---

## Stub honesty declaration

| Property | Declaration |
|----------|-------------|
| **Stub type** | Single-page minimal PDP reference scaffold |
| **Production scaffold** | **No** — reference implementation only |
| **CMS binding** | **None** |
| **Route model** | Single reference page (`product-page-reference.html`) |
| **Backend behavior** | **None** — commercial state presentation-only |
| **Gallery** | CSS placeholder — **no** carousel/zoom runtime |
| **Commerce** | Request-price static state — **no** cart/checkout |

---

## Shell mapping

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main" class="wf-product-page">
FOOTER      →  sections/footer.html (after </main>)
  └── LEGAL_LINKS → components/legal-links.html (nested)
```

### Contextual slots (inside MAIN)

| Surface | Matrix | Manifest |
|---------|--------|----------|
| BREADCRUMBS | REQ | Present |
| PAGINATION | N/A | **Absent** |
| SEARCH slot | POL (header) | Header utility only — not in MAIN |
| FILTERS slot | N/A | **Absent** |

---

## Block sequence

Ordered MAIN includes:

1. `components/breadcrumbs.html`
2. Product identity (scaffold-owned)
3. Product core — media + commercial (scaffold-owned)
4. Specifications (scaffold-owned)
5. Description (scaffold-owned)
6. `sections/lead_form.html`
7. `sections/trust.html`

---

## Scaffold-owned regions

| Region | Class root | `data-block-id` |
|--------|------------|-----------------|
| Product identity | `wf-product-page__identity` | None |
| Media | `wf-product-page__media` | None |
| Commercial | `wf-product-page__commercial` | None |
| Specifications | `wf-product-page__specifications` | None |
| Description | `wf-product-page__description` | None |

---

## Partial paths

| block_id | Path |
|----------|------|
| HEADER_NAV | `src/partials/sections/header-nav.html` |
| BREADCRUMBS | `src/partials/components/breadcrumbs.html` |
| LEAD_FORM | `src/partials/sections/lead_form.html` |
| TRUST | `src/partials/sections/trust.html` |
| FOOTER | `src/partials/sections/footer.html` |
| LEGAL_LINKS | `src/partials/components/legal-links.html` |

---

## SCSS paths

| Layer | Path |
|-------|------|
| Entry | `src/scss/main.scss` |
| Page layout | `src/scss/pages/_product-page-reference.scss` |
| Components | Existing — unchanged in C6 |

---

## JavaScript modules

| Module | Path |
|--------|------|
| lifecycle | `src/js/core/lifecycle.js` |
| form | `src/js/core/form.js` |
| header_nav | `src/js/sections/header_nav.js` |
| main | `src/js/main.js` |

**No new PRODUCT_PAGE-specific JS.**

---

## Asset dependencies

CSS-only media placeholders — no production images.

---

## Source provenance (informative)

| Source | Role |
|--------|------|
| BZPM `producthero.twig` | PDP hero/media/commercial anatomy — **not** copied |
| BZPM `producttabs.twig` | Spec/description tab structure — **not** copied |
| SRC-SIBCAR `pdp-hero.html` | AUTO secondary zone reference — **not** copied |

---

## Build result

| Field | Value |
|-------|-------|
| **Command** | `npm run build` |
| **Workspace** | `workspaces/website-factory-reference-v1/` |
| **Exit code** | **0** (Wave C6 validation run) |
| **Dist output** | `dist/product-page-reference.html` present |
| **CSS** | `dist/css/main.css` compiled |
| **JS** | Modules copied to `dist/js/` |

---

## Structural validation result

| Check | Result |
|-------|--------|
| Registered page type | PASS — `PRODUCT_PAGE` |
| Source page present | PASS |
| Dist page present | PASS |
| HEADER_NAV exactly 1 | PASS |
| MAIN exactly 1 | PASS |
| FOOTER exactly 1 | PASS |
| LEGAL_LINKS nested in FOOTER | PASS |
| BREADCRUMBS present | PASS |
| PAGINATION absent | PASS |
| FILTERS absent | PASS |
| Product identity present | PASS |
| Media region present | PASS |
| Commercial region present | PASS |
| Specifications present | PASS |
| Description present | PASS |
| New block IDs | PASS — none created |
| Unresolved includes | PASS — none |
| Build | PASS |

**Overall:** **STRUCTURALLY VALIDATED**

**Not claimed:** FIDELITY VERIFIED · PRODUCTION PASS

---

## Coverage claims

| Dimension | Before C6 | After C6 (evidence-based) |
|-----------|-----------|---------------------------|
| **RC** | 32/32 | **32/32** (unchanged) |
| **RPC** | 23/32 | **23/32** (unchanged) |
| **RSC** | 2/10 · 1/1 LANDING · 1/1 CATEGORY_PAGE | **3/10 · 1/1 LANDING · 1/1 CATEGORY_PAGE · 1/1 PRODUCT_PAGE** |
| **SC** | LANDING PASS · CATALOG PARTIAL | **LANDING PASS · CATALOG PARTIAL** |
| **PC** | 1/1 LANDING · 1/1 CATALOG corridor | **1/1 LANDING · 1/1 CATALOG corridor** (extended evidence) |

---

## Known limitations

- No gallery runtime · no related products · no tabs
- PRODUCT_CARD not used as PDP core
- SEARCH_RESULTS_PAGE scaffold not implemented
- CATALOG SC PASS not declared — C8 required

---

## SAFE UNKNOWN

- Dedicated gallery/specifications Registry blocks
- SEARCH_RESULTS_PAGE Registry extension vs Coverage Model scaffold list
- Full MANUFACTURER/AUTO vertical PDP binding (C7)

---

## Report path

`reports/wf-r01-3-4-wave-c6-product-page-decision-v1.md`

---

## Commit binding

`c8a661d` — `foundry: complete WF-R01.3.4 product page scaffold`

*Manifest version: v1 · Wave C6 · commit `c8a661d`.*
