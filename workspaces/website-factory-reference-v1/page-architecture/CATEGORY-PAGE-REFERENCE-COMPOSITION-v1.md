# CATEGORY_PAGE Reference Composition v1

**Site type:** CATALOG  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Page type:** `CATEGORY_PAGE`  
**Scaffold:** `src/pages/category-page-reference.html`  
**Authority:** [wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md) Wave C5 · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** fidelity verified. **Not** CMS-bound. **Not** backend filtering or search.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3.4 Wave C5 — CATEGORY_PAGE Scaffold and Composition |
| **Primary scaffold mode** | **product-listing CATEGORY_PAGE** (PLP) |
| **Build evidence** | `dist/category-page-reference.html` — build PASS (Wave C5) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **page_type** | `CATEGORY_PAGE` |
| **Canonical name** | Category PLP |
| **Industry alias** | PLP-like |
| **Registry source** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.4 Charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | CATEGORY_PAGE contract §11 |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order and semantics |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | REQ/POL surfaces |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Scaffold vs partial boundary |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RSC · SC · PC |
| Scaffold Manifest | [CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md](CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md) | Build and validation evidence |

---

## 4. Page-Type Binding

| Binding | Value |
|---------|-------|
| **Registered page type** | `CATEGORY_PAGE` |
| **Scaffold source** | `src/pages/category-page-reference.html` |
| **Dist output** | `dist/category-page-reference.html` |
| **Site-type primary** | `CATALOG` |
| **Also applicable** | `ECOMMERCE`, `CORPORATE` (catalog subtree) per PAGE-TYPE-REGISTRY-v1 |

---

## 5. Site-Type Applicability

| site_type_code | Applicability | Notes |
|----------------|---------------|-------|
| **CATALOG** | **Primary** | PLP corridor reference for G2 catalog pilot |
| **ECOMMERCE** | Applicable | Same block stack; commerce actions remain stubbed in reference |
| **CORPORATE** | Applicable | Catalog subtree only |
| **LANDING** | **N/A** | CATEGORY_PAGE forbidden on LANDING site type |
| **PROMO** | **N/A** | No catalog PLP in default PROMO blueprint |

---

## 6. Shell Composition

```text
HEADER_NAV
MAIN
FOOTER
└── LEGAL_LINKS
```

| Shell zone | Include path | DOM role |
|------------|--------------|----------|
| HEADER_NAV | `partials/layout/header.html` → `partials/sections/header-nav.html` | Site-level `<header>` |
| MAIN | `src/pages/category-page-reference.html` → `<main id="main" class="wf-category-page">` | Single `<main>` |
| FOOTER | `partials/sections/footer.html` (after `</main>`) | Site-level `<footer>` |
| LEGAL_LINKS | nested in FOOTER → `partials/components/legal-links.html` | `<nav>` inside FOOTER bottom slot |

---

## 7. Main Composition

**Primary mode:** product-listing PLP — neutral product grid with presentation-only search and filters.

```text
MAIN
├── BREADCRUMBS
├── PAGE_IDENTITY (scaffold-owned)
├── CATEGORIES
├── SEARCH (expanded contextual variation)
├── CATALOG_LAYOUT (scaffold-owned wrapper)
│   ├── mobile FILTERS trigger (scaffold-owned)
│   ├── FILTERS
│   └── RESULT_SURFACE (scaffold-owned)
│       ├── RESULT_CONTEXT (scaffold-owned)
│       ├── PRODUCT_GRID
│       │   └── PRODUCT_CARD × N
│       └── PAGINATION
```

**CATEGORY_GRID:** excluded from primary C5 scaffold — documented for category-hub variation (see §12).

---

## 8. Block Sequence

Ordered MAIN sequence in `src/pages/category-page-reference.html`:

1. `breadcrumbs.html`
2. Page identity header (`h1` + intro — scaffold-owned)
3. `categories.html`
4. `search.html` (expanded variation, unique instance IDs)
5. Mobile filters trigger (scaffold-owned button)
6. `filters.html`
7. Result context (scaffold-owned)
8. `product-grid.html` (includes `product-card.html` × 5)
9. `pagination.html`

---

## 9. Nested Compositions

| Parent | Child | Relationship |
|--------|-------|--------------|
| FOOTER | LEGAL_LINKS | Nested compliance cluster — `data-composition-slot="legal_links"` |
| PRODUCT_GRID | PRODUCT_CARD | First card carries canonical `data-block-id="product_card"`; additional cards use `data-demo-variation` only |
| CATALOG_LAYOUT | FILTERS + RESULT_SURFACE | Sidebar/content columns at desktop; stacked at mobile |

---

## 10. Required Blocks

Per Page-Type Shell Matrix row for `CATEGORY_PAGE`:

| Surface / Block | Matrix | C5 scaffold |
|-----------------|--------|-------------|
| HEADER_NAV | REQ | Present — exactly 1 |
| MAIN | REQ | Present — exactly 1 |
| BREADCRUMBS | REQ | Present |
| PAGINATION | REQ | Present |
| FOOTER | REQ | Present — exactly 1 |
| LEGAL_LINKS | REQ (nested) | Present in FOOTER |
| PRODUCT_GRID | Composition-required | Present |
| PRODUCT_CARD | Composition-required | Present within grid |

---

## 11. Policy-Dependent Blocks

| Surface / Block | Matrix | C5 decision |
|-----------------|--------|-------------|
| SEARCH slot | POL | **Included** — expanded contextual variation in MAIN |
| FILTERS slot | POL | **Included** — sidebar + mobile panel |
| CATEGORIES | POL | **Included** — sibling category navigation |

---

## 12. Scaffold-Owned Regions

| Region | Purpose | Registry block_id |
|--------|---------|-------------------|
| PAGE_IDENTITY | Category heading + neutral intro | **None** — scaffold metadata |
| CATALOG_LAYOUT | Sidebar/content column wrapper | **None** — layout wrapper only |
| mobile FILTERS trigger | Opens `#wf-filters-panel` on mobile | **None** — scaffold chrome |
| RESULT_CONTEXT | Neutral result count + presentation disclaimer | **None** — utility content |

**Not created:** `RESULT_TOOLBAR`, `SORT_CONTROLS`, `RESULT_COUNT` as Registry block IDs.

---

## 13. Partial Mapping

| block_id / surface | Partial path | SCSS path | Include parameters |
|--------------------|--------------|-----------|-------------------|
| `HEADER_NAV` | `partials/sections/header-nav.html` | `scss/sections/_header-nav.scss` | via `layout/header.html` |
| `BREADCRUMBS` | `partials/components/breadcrumbs.html` | `scss/components/_breadcrumbs.scss` | default |
| `CATEGORIES` | `partials/components/categories.html` | `scss/components/_categories.scss` | default |
| `SEARCH` | `partials/components/search.html` | `scss/components/_search.scss` | `variation: expanded`, unique IDs |
| `FILTERS` | `partials/components/filters.html` | `scss/components/_filters.scss` | default (`id="wf-filters-panel"`) |
| `PRODUCT_GRID` | `partials/components/product-grid.html` | `scss/components/_product-grid.scss` | default |
| `PRODUCT_CARD` | `partials/components/product-card.html` | `scss/components/_product-card.scss` | nested in grid |
| `PAGINATION` | `partials/components/pagination.html` | `scss/components/_pagination.scss` | default |
| `FOOTER` | `partials/sections/footer.html` | `scss/sections/_footer.scss` | after `</main>` |
| `LEGAL_LINKS` | `partials/components/legal-links.html` | `scss/components/_legal-links.scss` | nested in FOOTER |

**Page-level SCSS:** `scss/pages/_category-page-reference.scss` — container spacing, catalog columns, mobile trigger.

---

## 14. Asset and JavaScript Mapping

| Module | Path | Init scope |
|--------|------|------------|
| WfLifecycle core | `js/core/lifecycle.js` | Page boot |
| header_nav | `js/sections/header_nav.js` | HEADER_NAV |
| filters | `js/components/filters.js` | `[data-module="filters"]` — mobile panel, demo count |
| search | `js/components/search.js` | `[data-module="search"]` — expanded instance |
| main | `js/main.js` | Lifecycle boot |

**No CATEGORY_PAGE-specific JS module.** No network calls. No URL mutation.

---

## 15. Responsive Composition

| Viewport | Behavior |
|----------|----------|
| Desktop (≥1024px) | FILTERS sidebar column + RESULT_SURFACE content column; mobile trigger hidden |
| Tablet / mobile (<1024px) | Stacked layout; FILTERS panel via trigger; SEARCH expanded form full width |
| CATEGORIES | Horizontal chip wrap per component styles |
| PRODUCT_GRID | Responsive columns per `_product-grid.scss` |
| PAGINATION | Wrap/scroll per component styles |

Breakpoints: workspace foundations (`$bp-lg: 1024px`) — no new universal breakpoint introduced.

---

## 16. Accessibility Minimum

| Check | Status |
|-------|--------|
| Single `<main id="main">` | Pass |
| Heading hierarchy (`h1` page → `h2` grid) | Pass |
| BREADCRUMBS `nav` + `aria-label` | Pass |
| CATEGORIES `nav` + `aria-label` | Pass |
| SEARCH `role="search"` + label | Pass |
| FILTERS fieldsets/labels + mobile trigger `aria-expanded` / `aria-controls` | Pass |
| PRODUCT_GRID list semantics | Pass |
| PRODUCT_CARD heading/link | Pass |
| PAGINATION `aria-current="page"` | Pass |
| Keyboard order | Pass — no focus trap |
| Visible focus | Pass — component + page trigger styles |

**Not claimed:** WCAG certification.

---

## 17. Placeholder Content Policy

Neutral English demonstration content only:

- Category name, Product model A/B, Available, Made to order, Request price
- No BZPM/SIBCAR brand, real prices, production URLs, or live catalog data

---

## 18. Excluded Behavior

| Excluded | Reason |
|----------|--------|
| Backend filtering | Presentation-only FILTERS partial |
| Backend search / results routing | Presentation-only SEARCH partial |
| Pagination routing / query params | Structural reference state |
| Cart / wishlist / compare | Out of C5 scope |
| CATEGORY_GRID in primary scaffold | Category-hub mode deferred — see manifest |
| PRODUCT_PAGE scaffold | Wave C6 |
| SEARCH_RESULTS_PAGE | Not in Registry v1 minimum |

**Explicit policy:** SEARCH and FILTERS are presentation-only references. They do not control the neutral result set in C5.

---

## 19. Coverage Claims

| Dimension | C5 claim |
|-----------|----------|
| **RSC** | **+1** global when scaffold structurally validated — see manifest |
| **PC** | **+1** CATALOG corridor — this composition published and implemented |
| **RPC** | **No change** — reuses existing partials |
| **SC** | **Does not** grant CATALOG SC PASS alone — see Wave C5 REPORT |

---

## 20. Known Limitations

- Single-route reference scaffold — not multi-category site tree
- No CMS or OpenCart binding
- No fidelity verification against BZPM production
- CATEGORY_GRID hub variation documented but not implemented in primary scaffold
- PRODUCT_PAGE and SEARCH_RESULTS_PAGE scaffolds absent — CATALOG SC incomplete

---

## 21. Evidence Paths

| Artefact | Path |
|----------|------|
| Source page | `workspaces/website-factory-reference-v1/src/pages/category-page-reference.html` |
| Dist page | `workspaces/website-factory-reference-v1/dist/category-page-reference.html` |
| Page SCSS | `workspaces/website-factory-reference-v1/src/scss/pages/_category-page-reference.scss` |
| Manifest | `workspaces/website-factory-reference-v1/page-architecture/CATEGORY-PAGE-SCAFFOLD-MANIFEST-v1.md` |
| Wave C5 REPORT | `reports/wf-r01-3-4-wave-c5-category-page-scaffold-v1.md` |
| Structural provenance (informative) | `projects/ocpilot/sites/site-002/...` — **not** copied |

---

## 22. Decision

| Field | Value |
|-------|-------|
| **Decision** | **PUBLISHED** — CATEGORY_PAGE Reference Composition v1 is normative PLP corridor documentation for CATALOG site-type reference |
| **Primary mode** | product-listing CATEGORY_PAGE |
| **CATEGORY_GRID** | Excluded from primary scaffold; category-hub variation noted |
| **Next wave** | WF-R01.3.4 Wave C6 — PRODUCT_PAGE Scope or Scaffold Decision |

---

*Published: 2026-06-20 — WF-R01.3.4 Wave C5*
