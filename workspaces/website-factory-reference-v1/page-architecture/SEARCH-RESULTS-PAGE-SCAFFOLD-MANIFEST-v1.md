# SEARCH_RESULTS_PAGE Scaffold Manifest v1

**Page type:** `SEARCH_RESULTS_PAGE`  
**Site type:** `CATALOG` (primary)  
**Scaffold file:** `src/pages/search-results-page-reference.html`  
**Output:** `dist/search-results-page-reference.html`  
**Status:** PUBLISHED / VALIDATED  
**Metric:** RSC — global **+1** when G2-R3 A3 evidence accepted

**Authority:** [wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md](../../../projects/mars-website-factory/wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md) G2-R3 A3 · [reference-scaffold-contract-v1.md](../../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED / VALIDATED** |
| **Validation wave** | WF-R01.3 G2-R3 A3 |
| **Build** | PASS |
| **Structural validation** | PASS |
| **Accessibility minimum** | PASS |
| **Responsive minimum** | STRUCTURAL/CSS PASS — live browser deferred |

---

## 2. Page Type

| Field | Value |
|-------|-------|
| **page_type** | `SEARCH_RESULTS_PAGE` |
| **Registry state** | REGISTERED / **SCAFFOLD COMPLETE** |
| **Site-type primary** | `CATALOG` |

---

## 3. Authority

G2-R3 charter · A1 registry expansion · A2 preflight composition · Coverage addendum · Vocabulary addendum · Global Shell Contract · Shell Matrix · Reference Scaffold Contract · PAGE-TYPE-REGISTRY-v1.

---

## 4. Source Path

`workspaces/website-factory-reference-v1/src/pages/search-results-page-reference.html`

---

## 5. Dist Path

`workspaces/website-factory-reference-v1/dist/search-results-page-reference.html`

---

## 6. SCSS Path

| Layer | Path |
|-------|------|
| Entry | `src/scss/main.scss` |
| Page layout | `src/scss/pages/_search-results-page-reference.scss` |

---

## 7. Shell Requirements

| Surface | Matrix | Manifest |
|---------|--------|----------|
| HEADER_NAV | REQ | Present |
| MAIN | REQ | Present — one `<main>` |
| BREADCRUMBS | POL | Present — shallow trail |
| SEARCH | REQ | Present |
| FILTERS | POL | Present |
| PAGINATION | REQ | Present |
| FOOTER | REQ | Present |
| LEGAL_LINKS | REQ | Nested in FOOTER |

---

## 8. Canonical Includes

| block_id | Path | Count |
|----------|------|-------|
| BREADCRUMBS | `src/partials/components/breadcrumbs.html` | 1 |
| SEARCH | `src/partials/components/search.html` | 1 |
| FILTERS | `src/partials/components/filters.html` | 1 |
| PRODUCT_GRID | `src/partials/components/product-grid.html` | 1 |
| PAGINATION | `src/partials/components/pagination.html` | 1 |
| FOOTER | `src/partials/sections/footer.html` | 1 |
| LEGAL_LINKS | `src/partials/components/legal-links.html` | 1 (nested) |

---

## 9. Scaffold-Owned Regions

| Region | Selector | block_id | Default |
|--------|----------|----------|---------|
| QUERY_IDENTITY | `.wf-search-results-page__identity` | none | visible |
| RESULT_SUMMARY | `.wf-search-results-page__summary` | none | visible |
| SORT | `.wf-search-results-page__sort` | none | visible |
| EMPTY_STATE | `.wf-search-results-page__empty` | none | **hidden** |

---

## 10. Default State

Non-zero fictional results mode. QUERY_IDENTITY · SEARCH · RESULT_SUMMARY · SORT · FILTERS · PRODUCT_GRID · PAGINATION visible. EMPTY_STATE present but hidden.

---

## 11. Empty-State Variation

Zero-hit region documented in composition §19. Source includes hidden EMPTY_STATE for variation evidence. No JS switching in default build.

---

## 12. Excluded Blocks

CATEGORIES · HERO · LEAD_FORM · CTA · ABOUT · TEAM · TRUST · SERVICES · PROCESS · FAQ · CONTACTS · PROMO blocks · cart/checkout blocks.

---

## 13. Build Command

```bash
npm run build
```

Executed in `workspaces/website-factory-reference-v1/` — exit code **0**.

---

## 14. Structural Validation

| Check | Result |
|-------|--------|
| One source page | PASS |
| One page SCSS | PASS |
| One composition | PASS |
| One manifest | PASS |
| One MAIN · one H1 | PASS |
| Hook counts (SEARCH/FILTERS/PRODUCT_GRID/PAGINATION = 1 each) | PASS |
| Excluded hooks (CATEGORIES/HERO/LEAD_FORM/CTA = 0) | PASS |
| EMPTY_STATE hidden | PASS |
| No duplicate IDs | PASS |
| No unresolved includes | PASS |

---

## 15. Accessibility Validation

One H1 · shallow breadcrumb current item · search label · sort label associated · filters legends · pagination nav · empty heading present but hidden · keyboard-focus styles on page controls · no duplicate IDs.

**Not claimed:** WCAG certification · live browser audit.

---

## 16. Runtime Boundary

Presentation-only reference. SEARCH submit prevented (no network). FILTERS local UI only. SORT static. PAGINATION `href="#"`. No router · no analytics · no CMS · no empty-state state machine.

---

## 17. Fictional Data

Static query `sample query` · count `12 results found` · neutral product cards · fictional filter counts · placeholder pagination links.

---

## 18. RSC Eligibility

| Field | Value |
|-------|-------|
| **Eligible** | **Yes** |
| **Delta** | **+1** |
| **Before A3** | **6/11** |
| **After A3** | **7/11** |

Evidence chain: registered page type · source HTML · page SCSS · composition · manifest · build PASS · structural validation · A3 report · Git evidence.

---

## 19. CATALOG PC Boundary

CATALOG PC **1/1** — **UNCHANGED**. SEARCH_RESULTS_PAGE excluded from PC corridor.

---

## 20. CATALOG SC Boundary

CATALOG SC **PARTIAL** — **NOT PASSED** after A3. G2-R4 evaluation required.

---

## 21. Known Limitations

- Live browser spot-check **deferred**
- EMPTY_STATE variation not toggled in default build
- PRODUCT_GRID retains generic `Products` heading from canonical partial
- CONTACT breadcrumb label debt unchanged (out of A3 scope)

---

## 22. Git Evidence

Binding commit: `6570fcb` on `mars/post-cycle8-live-tests` — message `foundry: complete G2-R3 SEARCH_RESULTS_PAGE scaffold`.

---

## 23. Decision

**PUBLISHED / VALIDATED** — `SEARCH_RESULTS_PAGE` reference scaffold complete. RSC **+1** accrued (**7/11**). CATALOG SC remains PARTIAL pending G2-R4.
