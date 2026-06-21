# SEARCH_RESULTS_PAGE Reference Composition v1

**Site type:** CATALOG  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Page type:** `SEARCH_RESULTS_PAGE`  
**Scaffold:** `src/pages/search-results-page-reference.html`  
**Authority:** [wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md](../../../projects/mars-website-factory/wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md) · [wf-r01-3-g2-r3-a2-search-results-reference-preflight-composition-decisions-v1.md](../../../projects/mars-website-factory/wf-r01-3-g2-r3-a2-search-results-reference-preflight-composition-decisions-v1.md) · [reference-scaffold-contract-v1.md](../../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** fidelity verified. **Not** CMS-bound. **Not** backend search, filtering, sort, or pagination runtime.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3 G2-R3 A3 — SEARCH_RESULTS_PAGE Scaffold |
| **Primary scaffold mode** | **non-zero search results** (default build) |
| **Build evidence** | `dist/search-results-page-reference.html` — build PASS (G2-R3 A3) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **page_type** | `SEARCH_RESULTS_PAGE` |
| **Canonical name** | Search results listing |
| **Industry alias** | SRP-like |
| **Registry source** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G2-R3 charter | `projects/mars-website-factory/wf-r01-3-g2-r3-search-results-page-authority-reconciliation-charter-v1.md` | Package contract |
| G2-R3 A1 | `projects/mars-website-factory/wf-r01-3-g2-r3-a1-search-results-registry-matrix-expansion-v1.md` | Registry/matrix alignment |
| G2-R3 A2 | `projects/mars-website-factory/wf-r01-3-g2-r3-a2-search-results-reference-preflight-composition-decisions-v1.md` | Composition approval |
| Coverage addendum | `projects/mars-website-factory/wf-r01-3-1-coverage-model-search-results-page-addendum-v1.md` | RSC eligibility |
| Vocabulary addendum | `projects/mars-website-factory/foundry-vocabulary-search-results-page-addendum-v1.md` | Terminology |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | REQ/POL surfaces |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC accrual chain |
| Scaffold Manifest | [SEARCH-RESULTS-PAGE-SCAFFOLD-MANIFEST-v1.md](SEARCH-RESULTS-PAGE-SCAFFOLD-MANIFEST-v1.md) | Build evidence |

---

## 4. Purpose

Document the reference composition for `SEARCH_RESULTS_PAGE` — a query-driven catalog results host with canonical block reuse, scaffold-owned query/summary/sort/empty regions, and presentation-only fictional data. Supports CATALOG SC evidence without claiming production search runtime.

---

## 5. Shell

```text
HEADER_NAV
MAIN
FOOTER
└── LEGAL_LINKS
```

| Shell zone | Include path | Matrix |
|------------|--------------|--------|
| HEADER_NAV | `partials/layout/header.html` | REQ |
| MAIN | `<main id="main" class="wf-search-results-page">` | REQ |
| FOOTER | `partials/sections/footer.html` | REQ |
| LEGAL_LINKS | nested in FOOTER | REQ |

---

## 6. Default State

| Field | Value |
|-------|-------|
| **Primary mode** | Non-zero fictional search results |
| **Query** | Static fictional string: `sample query` |
| **Result count** | Static fictional count: `12 results found` |
| **EMPTY_STATE** | Present in source · **hidden** in default build |
| **Runtime** | Presentation-only — no search execution |

---

## 7. Block Sequence

```text
MAIN
├── BREADCRUMBS
├── QUERY_IDENTITY (scaffold-owned)
├── SEARCH
├── RESULT_SUMMARY (scaffold-owned)
├── SORT (scaffold-owned)
├── search-results layout
│   ├── FILTERS
│   └── results column
│       ├── PRODUCT_GRID
│       └── PAGINATION
└── EMPTY_STATE (scaffold-owned, hidden)
```

---

## 8. Scaffold-Owned Regions

| Region | block_id | RSC | Notes |
|--------|----------|-----|-------|
| QUERY_IDENTITY | **none** | **no** | One H1 · fictional query context |
| RESULT_SUMMARY | **none** | **no** | Static result count |
| SORT | **none** | **no** | Presentation-only select · no JS |
| EMPTY_STATE | **none** | **no** | Variation evidence · hidden by default |

---

## 9. Required Blocks

| block_id | Include | Count |
|----------|---------|-------|
| HEADER_NAV | layout shell | 1 |
| BREADCRUMBS | `components/breadcrumbs.html` | 1 |
| SEARCH | `components/search.html` | 1 |
| PAGINATION | `components/pagination.html` | 1 |
| FOOTER | `sections/footer.html` | 1 |
| LEGAL_LINKS | nested in FOOTER | 1 |

---

## 10. Policy Blocks

| block_id | Include | Count | Notes |
|----------|---------|-------|-------|
| FILTERS | `components/filters.html` | 1 | POL per Shell Matrix · presentation-only |

---

## 11. Excluded Blocks

```text
CATEGORIES
HERO
LEAD_FORM
CTA
ABOUT
TEAM
TRUST
SERVICES
PROCESS
FAQ
CONTACTS
PROMO blocks
cart/checkout blocks
```

---

## 12. QUERY_IDENTITY Role

Scaffold-owned page identity region containing eyebrow, single H1 with fictional query echo, no `data-block-id`, no Registry identity, no RPC accrual.

---

## 13. SEARCH Role

Canonical SEARCH partial — expanded variation — one instance. Presentation-only query entry; form submit prevented by reference JS; no backend, routing, or autosuggest.

---

## 14. RESULT_SUMMARY Role

Scaffold-owned static result count text. Not aria-live (no dynamic behavior). Does not duplicate H1 semantics.

---

## 15. SORT Role

Scaffold-owned presentation-only `<select>` with associated label. No JS, no query mutation, no network.

---

## 16. FILTERS Role

Canonical FILTERS partial reused once. Local UI interaction allowed (panel open/close, checkbox state) without network or query mutation.

---

## 17. PRODUCT_GRID Role

Canonical PRODUCT_GRID partial — fictional product cards, neutral demonstration content, `href="#"` in cards, one listing instance.

---

## 18. PAGINATION Role

Canonical PAGINATION partial — presentation-only nav, `href="#"`, current page marked, one instance.

---

## 19. EMPTY_STATE Variation

Scaffold-owned zero-hit region documented as variation evidence. Default build keeps region **hidden** — no JS state machine, no live switching between zero/non-zero views.

---

## 20. Runtime Boundary

```text
No search endpoint
No fetch/XHR
No URL router
No autosuggest
No analytics
No CMS query binding
No filter execution against real catalog
No sort execution
No pagination routing
No empty-state state machine
```

---

## 21. Fictional Data Policy

All query text, result counts, product cards, filter counts, and pagination labels are neutral fictional demonstration values. No real client data, brands, prices tied to production catalog, or live URLs.

---

## 22. Accessibility

| Requirement | Implementation |
|-------------|----------------|
| One H1 | QUERY_IDENTITY |
| Breadcrumb current item | shallow trail · `aria-current="page"` |
| Search label | canonical SEARCH partial |
| Sort label | `for="search-results-sort"` |
| Filters labels/legends | canonical FILTERS partial |
| Pagination nav | canonical PAGINATION · `aria-label` |
| Empty state heading | `h2` when variation enabled |
| Hidden empty state | `hidden` attribute — excluded from active flow |

**Not claimed:** WCAG certification.

---

## 23. Responsive Notes

Desktop: filters column + results column grid. Mobile/tablet: filters trigger, stacked summary/sort, full-width grid, pagination wrap. Long query and H1 use `overflow-wrap: anywhere`. `min-width: 0` on layout columns.

---

## 24. Coverage Role

| Dimension | Effect |
|-----------|--------|
| **RSC** | **+1** for `SEARCH_RESULTS_PAGE` scaffold when manifest validated |
| **RC** | Unchanged |
| **RPC** | Unchanged — block partials already counted |
| **CATALOG PC** | **Excluded** — not a PC corridor member |

---

## 25. CATALOG PC Boundary

`SEARCH_RESULTS_PAGE` is **not** a CATALOG PC corridor page type. A3 does **not** accrue or modify CATALOG PC (**1/1** unchanged).

---

## 26. CATALOG SC Relationship

CATALOG SC remains **PARTIAL** after A3. Scaffold evidence supports future **G2-R4** CATALOG SC re-evaluation. A3 does **not** declare CATALOG SC PASS.

---

## 27. Evidence Paths

```text
workspaces/website-factory-reference-v1/src/pages/search-results-page-reference.html
workspaces/website-factory-reference-v1/dist/search-results-page-reference.html
workspaces/website-factory-reference-v1/src/scss/pages/_search-results-page-reference.scss
workspaces/website-factory-reference-v1/page-architecture/SEARCH-RESULTS-PAGE-REFERENCE-COMPOSITION-v1.md
workspaces/website-factory-reference-v1/page-architecture/SEARCH-RESULTS-PAGE-SCAFFOLD-MANIFEST-v1.md
reports/wf-r01-3-g2-r3-a3-search-results-page-scaffold-v1.md
```

---

## 28. Decision

**PUBLISHED** — `SEARCH_RESULTS_PAGE` reference composition approved and implemented per G2-R3 A2 authority. Default non-zero-results mode with hidden empty-state variation. Ready for manifest validation and RSC accrual in A3 report.
