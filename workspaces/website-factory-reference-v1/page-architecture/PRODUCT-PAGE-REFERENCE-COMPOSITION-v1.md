# PRODUCT_PAGE Reference Composition v1

**Site type:** CATALOG  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Page type:** `PRODUCT_PAGE`  
**Scaffold:** `src/pages/product-page-reference.html`  
**Authority:** [wf-r01-3-4-product-page-scope-decision-v1.md](../../projects/mars-website-factory/wf-r01-3-4-product-page-scope-decision-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** fidelity verified. **Not** CMS-bound. **Not** ecommerce runtime.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3.4 Wave C6 — PRODUCT_PAGE Scope or Scaffold Decision |
| **Primary scaffold mode** | **minimal PRODUCT_PAGE** (PDP) |
| **Build evidence** | `dist/product-page-reference.html` — build PASS (Wave C6) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **page_type** | `PRODUCT_PAGE` |
| **Canonical name** | Product PDP |
| **Industry alias** | PDP-like |
| **Registry source** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| Scope Decision | `projects/mars-website-factory/wf-r01-3-4-product-page-scope-decision-v1.md` | C6 Stage A/B gate |
| WF-R01.3.4 Charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | PRODUCT_PAGE contract §12 |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | REQ/POL surfaces |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Scaffold boundary |
| Scaffold Manifest | [PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md](PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md) | Build validation |

---

## 4. Page-Type Binding

| Binding | Value |
|---------|-------|
| **Registered page type** | `PRODUCT_PAGE` |
| **Scaffold source** | `src/pages/product-page-reference.html` |
| **Dist output** | `dist/product-page-reference.html` |
| **Site-type primary** | `CATALOG` |
| **Also applicable** | `ECOMMERCE`, `CORPORATE` (catalog subtree) |

---

## 5. Site-Type Applicability

| site_type_code | Applicability | Notes |
|----------------|---------------|-------|
| **CATALOG** | **Primary** | RFQ / request-price commercial state |
| **ECOMMERCE** | Applicable | Commerce actions remain stubbed in reference |
| **CORPORATE** | Applicable | Catalog subtree only |
| **LANDING** | **N/A** | PRODUCT_PAGE forbidden on LANDING |
| **PROMO** | **N/A** | No catalog PDP in default PROMO blueprint |

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
| MAIN | `src/pages/product-page-reference.html` → `<main id="main" class="wf-product-page">` | Single `<main>` |
| FOOTER | `partials/sections/footer.html` (after `</main>`) | Site-level `<footer>` |
| LEGAL_LINKS | nested in FOOTER → `partials/components/legal-links.html` | `<nav>` inside FOOTER |

---

## 7. Main Composition

**Primary mode:** minimal PDP — scaffold-owned detail regions with canonical conversion/trust partials.

```text
MAIN
├── BREADCRUMBS
├── PRODUCT_IDENTITY_REGION (scaffold-owned)
├── PRODUCT_CORE (scaffold-owned wrapper)
│   ├── MEDIA_REGION (scaffold-owned)
│   └── COMMERCIAL_REGION (scaffold-owned)
├── SPECIFICATION_REGION (scaffold-owned)
├── DESCRIPTION_REGION (scaffold-owned)
├── LEAD_FORM (canonical)
└── TRUST (canonical — policy-dependent)
```

---

## 8. Block Sequence

Ordered MAIN sequence in `src/pages/product-page-reference.html`:

1. `components/breadcrumbs.html`
2. Product identity header (eyebrow · `h1` · summary · availability — scaffold-owned)
3. Product core two-column layout (scaffold-owned)
   - Media region (placeholder + static thumb placeholders)
   - Commercial region (reference · request-price · primary CTA link)
4. Specification region (`<dl>` — scaffold-owned)
5. Description region (paragraphs — scaffold-owned)
6. `sections/lead_form.html`
7. `sections/trust.html`

---

## 9. Canonical Block Bindings

| block_id | Matrix / policy | C6 scaffold |
|----------|-----------------|-------------|
| HEADER_NAV | REQ | Present — 1 |
| BREADCRUMBS | REQ | Present |
| LEAD_FORM | Contextual — CATALOG RFQ | Present |
| TRUST | Recommended — CATALOG | Present |
| FOOTER | REQ | Present — 1 |
| LEGAL_LINKS | REQ (nested) | Present |

---

## 10. Scaffold-Owned Regions

| Region | Markup class prefix | `data-block-id` | Notes |
|--------|---------------------|-----------------|-------|
| Product identity | `wf-product-page__identity` | **None** | One `h1` |
| Media | `wf-product-page__media` | **None** | CSS placeholder — no carousel |
| Commercial | `wf-product-page__commercial` | **None** | Request-price primary state |
| Specifications | `wf-product-page__specifications` | **None** | Semantic `<dl>` |
| Description | `wf-product-page__description` | **None** | No tabs runtime |
| Primary CTA link | `wf-product-page__primary-cta` | **None** | Links to `#lead-form` |

---

## 11. Required Regions

Per minimal PDP contract and structural validation:

| Region | Required | Present |
|--------|----------|---------|
| Product identity | Yes | Yes |
| Media | Yes | Yes |
| Commercial | Yes | Yes |
| Specifications | Yes | Yes |
| Description | Yes | Yes |
| Breadcrumbs | Yes (matrix REQ) | Yes |

---

## 12. Policy-Dependent Regions

| Region | Policy | C6 decision |
|--------|--------|-------------|
| LEAD_FORM | CATALOG RFQ path | **Included** |
| TRUST | Recommended for CATALOG | **Included** |
| SEARCH in MAIN | POL — header utility only | **Excluded from MAIN** |
| RELATED_PRODUCTS | SAFE UNKNOWN | **Excluded** |

---

## 13. Excluded Regions

| Region / behavior | Reason |
|-------------------|--------|
| FILTERS | N/A on PRODUCT_PAGE per shell matrix |
| PAGINATION | N/A on PDP |
| PRODUCT_GRID | Not required for minimal PDP |
| PRODUCT_CARD as PDP core | Decision A — listing unit not reused as root |
| CTA band | CTA `allowed_site_types` excludes CATALOG |
| Gallery runtime | No canonical gallery block |
| Cart / checkout / variants | Runtime exclusions |

---

## 14. Partial Mapping

| block_id | Path |
|----------|------|
| HEADER_NAV | `src/partials/sections/header-nav.html` |
| BREADCRUMBS | `src/partials/components/breadcrumbs.html` |
| LEAD_FORM | `src/partials/sections/lead_form.html` |
| TRUST | `src/partials/sections/trust.html` |
| FOOTER | `src/partials/sections/footer.html` |
| LEGAL_LINKS | `src/partials/components/legal-links.html` |

Scaffold-owned regions: inline in `product-page-reference.html` — no partial files.

---

## 15. SCSS and JavaScript Mapping

| Layer | Path |
|-------|------|
| Entry | `src/scss/main.scss` |
| Page layout | `src/scss/pages/_product-page-reference.scss` |
| Reused partial SCSS | Existing — unchanged in C6 |

| Module | Path | C6 use |
|--------|------|--------|
| lifecycle | `src/js/core/lifecycle.js` | Shell |
| form | `src/js/core/form.js` | LEAD_FORM mock submit |
| header_nav | `src/js/sections/header_nav.js` | HEADER_NAV |
| main | `src/js/main.js` | Init |

**No new PRODUCT_PAGE JavaScript.**

---

## 16. Responsive Composition

| Breakpoint policy | Behavior |
|-------------------|----------|
| Desktop (≥ lg) | Two-column PRODUCT_CORE — media left, commercial right |
| Mobile / tablet | Stacked PRODUCT_CORE — media then commercial |
| Container | `wf-container` — project default paddings |

---

## 17. Accessibility Minimum

- One `<main>` · one `h1` (product title)
- Section `h2` headings for media, commercial, specs, description
- Breadcrumbs nav with `aria-label`
- Availability text — not color-only
- Primary CTA — focus-visible treatment
- LEAD_FORM — existing accessible form partial
- Media placeholder — visually hidden explanatory text

**Not claimed:** WCAG certification.

---

## 18. Placeholder Policy

Neutral demonstration content only:

- Product model A · Reference 100 · Request price · Available
- Material · Dimensions · Capacity · Power · Weight
- No real BZPM SKUs · prices · phones · production URLs · client images

Media: CSS gradient placeholder + static thumb boxes — no remote images.

---

## 19. Runtime Exclusions

No cart · checkout · wishlist · compare · quantity · variants · gallery carousel · zoom · tabs runtime · network catalog calls · OpenCart/PHP.

---

## 20. Coverage Claims

| Dimension | C6 contribution |
|-----------|-----------------|
| **RSC** | **+1** global — `PRODUCT_PAGE` scaffold validated |
| **RPC** | **Unchanged** — reuse only |
| **PC** | Extends CATALOG corridor documentation — numerator unchanged until C8 |
| **SC** | CATALOG remains **PARTIAL** |

---

## 21. SAFE UNKNOWN

- Dedicated gallery / specifications Registry blocks
- Related products zone
- SEARCH_RESULTS_PAGE scaffold authority
- Full vertical PDP depth (C7)
- ECOMMERCE add-to-cart path

---

## 22. Evidence Paths

- `src/pages/product-page-reference.html`
- `dist/product-page-reference.html`
- `src/scss/pages/_product-page-reference.scss`
- [PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md](PRODUCT-PAGE-SCAFFOLD-MANIFEST-v1.md)
- [wf-r01-3-4-product-page-scope-decision-v1.md](../../projects/mars-website-factory/wf-r01-3-4-product-page-scope-decision-v1.md)
- [wf-r01-3-4-wave-c6-product-page-decision-v1.md](../../reports/wf-r01-3-4-wave-c6-product-page-decision-v1.md)

---

## 23. Decision

```text
PUBLISHED — minimal PRODUCT_PAGE reference composition
STRUCTURALLY VALIDATED — stub-declared honesty
```

*Composition version: v1 · Wave C6.*
