# CATEGORY_PAGE Scaffold Manifest v1

**Page type:** `CATEGORY_PAGE`  
**Site type:** `CATALOG` (primary)  
**Scaffold file:** `src/pages/category-page-reference.html`  
**Output:** `dist/category-page-reference.html`  
**Status:** STRUCTURALLY VALIDATED · STUB-DECLARED  
**Metric:** RSC — global **+1** when Wave C5 evidence accepted

**Authority:** [wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md) Wave C5 · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

---

## Manifest identity

| Field | Value |
|-------|-------|
| **manifest_version** | v1 |
| **status** | STRUCTURALLY VALIDATED |
| **page_type** | `CATEGORY_PAGE` |
| **site_type_code** | `CATALOG` (primary); also `ECOMMERCE`, `CORPORATE` catalog subtree |
| **Scaffold path** | `workspaces/website-factory-reference-v1/src/pages/category-page-reference.html` |
| **Dist path** | `workspaces/website-factory-reference-v1/dist/category-page-reference.html` |
| **Build command** | `npm run build` (in reference workspace) |
| **Global RSC denominator** | **10** primary page types (PAGE-TYPE-REGISTRY-v1 Core minimum set) |
| **Global RSC numerator (post-C5)** | **2** — `LANDING_PAGE` + `CATEGORY_PAGE` |
| **CATALOG corridor RSC** | **1/1** for PLP scaffold |
| **Commit binding** | PENDING COMMIT BINDING |

---

## Stub honesty declaration

| Property | Declaration |
|----------|-------------|
| **Stub type** | Single-page PLP reference scaffold — product-listing mode |
| **Production scaffold** | **No** — reference implementation only |
| **CMS binding** | **None** |
| **Route model** | Single reference page (`category-page-reference.html`) |
| **Backend behavior** | **None** — search, filters, pagination are presentation-only |
| **Primary mode** | product-listing CATEGORY_PAGE |
| **Category-hub mode** | CATEGORY_GRID excluded — documented for future variation |

---

## Shell mapping

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main" class="wf-category-page">
FOOTER      →  sections/footer.html (after </main>)
  └── LEGAL_LINKS → components/legal-links.html (nested)
```

### Contextual slots (inside MAIN)

| Surface | Matrix | Manifest |
|---------|--------|----------|
| BREADCRUMBS | REQ | Present |
| PAGINATION | REQ | Present |
| SEARCH slot | POL | Present — expanded variation |
| FILTERS slot | POL | Present — sidebar + mobile trigger |

---

## Block sequence

Ordered MAIN includes:

1. `components/breadcrumbs.html`
2. Page identity (`h1` + intro — scaffold-owned)
3. `components/categories.html`
4. `components/search.html` (expanded)
5. Mobile filters trigger (scaffold-owned)
6. `components/filters.html`
7. Result context (scaffold-owned)
8. `components/product-grid.html` → `product-card.html` × 5
9. `components/pagination.html`

---

## Nested compositions

| Parent | Child |
|--------|-------|
| FOOTER | LEGAL_LINKS |
| PRODUCT_GRID | PRODUCT_CARD (first card canonical hook) |
| CATALOG_LAYOUT | FILTERS + RESULT_SURFACE |

---

## Partial paths

| block_id | Path |
|----------|------|
| HEADER_NAV | `src/partials/sections/header-nav.html` |
| BREADCRUMBS | `src/partials/components/breadcrumbs.html` |
| CATEGORIES | `src/partials/components/categories.html` |
| SEARCH | `src/partials/components/search.html` |
| FILTERS | `src/partials/components/filters.html` |
| PRODUCT_GRID | `src/partials/components/product-grid.html` |
| PRODUCT_CARD | `src/partials/components/product-card.html` |
| PAGINATION | `src/partials/components/pagination.html` |
| FOOTER | `src/partials/sections/footer.html` |
| LEGAL_LINKS | `src/partials/components/legal-links.html` |

---

## SCSS paths

| Layer | Path |
|-------|------|
| Entry | `src/scss/main.scss` |
| Page layout | `src/scss/pages/_category-page-reference.scss` |
| Components | Existing component SCSS — unchanged in C5 |

---

## JavaScript modules

| Module | Path |
|--------|------|
| lifecycle | `src/js/core/lifecycle.js` |
| header_nav | `src/js/sections/header_nav.js` |
| filters | `src/js/components/filters.js` |
| search | `src/js/components/search.js` |
| main | `src/js/main.js` |

---

## Asset dependencies

Neutral demonstration content only — no production images required beyond existing product-card placeholders in partial.

---

## Reference sources (structural provenance — informative)

| Source | Role |
|--------|------|
| BZPM `category.twig` | PLP layout provenance — **not** copied |
| BZPM `productcard.twig` | Card structure provenance — partial already built in C4B |
| BZPM `plp-stoly-after.html` | Layout stress reference — **not** copied |

---

## Build result

| Field | Value |
|-------|-------|
| **Command** | `npm run build` |
| **Workspace** | `workspaces/website-factory-reference-v1/` |
| **Exit code** | **0** (Wave C5 validation run) |
| **Dist output** | `dist/category-page-reference.html` present |
| **CSS** | `dist/css/main.css` compiled |
| **JS** | All modules copied to `dist/js/` |

---

## Structural validation result

| Check | Result |
|-------|--------|
| Registered page type | PASS — `CATEGORY_PAGE` |
| Source page present | PASS |
| Dist page present | PASS |
| HEADER_NAV exactly 1 | PASS |
| MAIN exactly 1 | PASS |
| FOOTER exactly 1 | PASS |
| LEGAL_LINKS nested in FOOTER | PASS |
| BREADCRUMBS present | PASS |
| PAGINATION present | PASS |
| SEARCH per composition | PASS |
| FILTERS per composition | PASS |
| CATEGORIES per composition | PASS |
| PRODUCT_GRID present | PASS |
| PRODUCT_CARD in grid | PASS |
| Forbidden blocks absent | PASS |
| Duplicate canonical hooks | PASS — none |
| Unresolved includes | PASS — none |
| Build | PASS |

**Overall:** **STRUCTURALLY VALIDATED**

**Not claimed:** FIDELITY VERIFIED · PRODUCTION PASS

---

## Coverage claims

| Dimension | Before C5 | After C5 (evidence-based) |
|-----------|-----------|---------------------------|
| **RC** | 32/32 | **32/32** (unchanged) |
| **RPC** | 23/32 | **23/32** (unchanged — reuse only) |
| **RSC** | 1/10 global · 1/1 LANDING | **2/10 global · 1/1 LANDING · 1/1 CATEGORY_PAGE** |
| **SC** | LANDING PASS | **LANDING PASS** · CATALOG **PARTIAL** |
| **PC** | 1/1 LANDING | **1/1 LANDING · 1/1 CATALOG corridor** |

---

## Known limitations

- Presentation-only SEARCH and FILTERS — no result-set control
- No PRODUCT_PAGE or SEARCH_RESULTS_PAGE scaffolds
- CATEGORY_GRID excluded from primary PLP mode
- No vertical profile binding (Wave C7)
- No G2 gate activation from scaffold alone

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Fidelity vs BZPM production PLP | **Not evaluated** |
| CMS field binding for category intro | **Not in scope** |
| Sort controls as future block_id | **Undecided** — not created in C5 |

---

## Evidence report

`reports/wf-r01-3-4-wave-c5-category-page-scaffold-v1.md`

---

## Cross-references

| Artifact | Path |
|----------|------|
| Reference Composition | [CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md](CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md) |
| LANDING manifest (pattern) | [LANDING-SCAFFOLD-MANIFEST-v1.md](../LANDING-SCAFFOLD-MANIFEST-v1.md) |
| Page Type Registry | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) |

---

*Published: 2026-06-20 — WF-R01.3.4 Wave C5*
