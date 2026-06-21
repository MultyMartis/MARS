# SERVICE_PAGE Scaffold Manifest v1

**Page type:** `SERVICE_PAGE`  
**Site type:** `PROMO` (primary)  
**Scaffold file:** `src/pages/service-page-reference.html`  
**Output:** `dist/service-page-reference.html`  
**Status:** PUBLISHED / VALIDATED  
**Metric:** RSC — global **+1** when G2-R2 P4 evidence accepted

**Authority:** [wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md](../../projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED / VALIDATED** |
| **Validation wave** | WF-R01.3 G2-R2 P4 |
| **Build** | PASS |
| **Structural validation** | PASS |
| **Accessibility minimum** | PASS |
| **Live browser spot-check** | DEFERRED — minor note |

---

## 2. Page Type

| Field | Value |
|-------|-------|
| **page_type** | `SERVICE_PAGE` |
| **Registry** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) § SERVICE_PAGE |
| **Allowed site types** | PROMO · CORPORATE |
| **Primary corridor** | PROMO money-page scaffold package (G2-R2) |

---

## 3. Authority

| Document | Path |
|----------|------|
| G2-R2 P1 preflight | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md` |
| G2-R2 charter | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md` |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| Composition | [SERVICE-PAGE-REFERENCE-COMPOSITION-v1.md](SERVICE-PAGE-REFERENCE-COMPOSITION-v1.md) |

---

## 4. Source Path

`workspaces/website-factory-reference-v1/src/pages/service-page-reference.html`

---

## 5. Dist Path

`workspaces/website-factory-reference-v1/dist/service-page-reference.html`

---

## 6. SCSS Path

| Layer | Path |
|-------|------|
| Entry import | `src/scss/main.scss` — `@use 'pages/service-page-reference'` |
| Page layout | `src/scss/pages/_service-page-reference.scss` |
| Block styles | Existing — benefits · process · faq · cta_band · lead_form unchanged |

---

## 7. Shell Requirements

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main" class="wf-service-page">
FOOTER      →  sections/footer.html (after </main>)
  └── LEGAL_LINKS → components/legal-links.html (nested)
```

| Surface | Requirement | Present |
|---------|-------------|---------|
| HEADER_NAV | REQ | Yes |
| MAIN | REQ | Yes — exactly one |
| BREADCRUMBS | POL — included | Yes |
| FOOTER | REQ | Yes |
| LEGAL_LINKS | REQ | Yes — nested |
| SEARCH / FILTERS / PAGINATION | N/A | No |

---

## 8. Canonical Includes

| Order | Include path | block_id |
|-------|--------------|----------|
| Shell | `partials/layout/header.html` | HEADER_NAV |
| 1 | `partials/components/breadcrumbs.html` | BREADCRUMBS (Tier B) — shallow variant |
| 2 | scaffold-owned PAGE_IDENTITY | — |
| 3 | scaffold-owned SERVICE_DETAIL_CONTEXT | — |
| 4 | `partials/sections/benefits.html` | BENEFITS |
| 5 | `partials/sections/process.html` | PROCESS |
| 6 | `partials/sections/faq.html` | FAQ |
| 7 | `partials/sections/cta_band.html` | CTA |
| 8 | `partials/sections/lead_form.html` | LEAD_FORM |
| Shell | `partials/sections/footer.html` | FOOTER (+ LEGAL_LINKS) |

---

## 9. Scaffold-Owned Regions

| Region | Selector | `data-block-id` |
|--------|----------|-----------------|
| PAGE_IDENTITY | `.wf-service-page__identity` | None |
| SERVICE_DETAIL_CONTEXT | `.wf-service-page__detail` | None |
| Inner wrapper | `.wf-service-page__inner` | None |

---

## 10. Excluded Blocks

SERVICES · ABOUT · TEAM · TRUST · CONTACTS · MAP · HERO · PRICING · catalog/commerce blocks · SERVICE_DESCRIPTION · SERVICE_CONTENT · SERVICE_DETAIL · SERVICE_FEATURES · SERVICE_CARD

---

## 11. Breadcrumb Decision

| Field | Value |
|-------|-------|
| **Canonical path** | `src/partials/components/breadcrumbs.html` |
| **Parameter contract** | `trail: shallow` · `currentLabel: Service` |
| **SERVICE_PAGE trail** | `Home` → `Service` |
| **Partial modification** | **None** — P3 shallow parameterization reused |
| **CONTACT debt** | Unchanged — catalog-default trail preserved |
| **Regression** | CATEGORY_PAGE · PRODUCT_PAGE · ABOUT_PAGE · breadcrumbs-reference — build PASS |

---

## 12. Build Command

```bash
npm run build
```

**Workspace:** `workspaces/website-factory-reference-v1/`

---

## 13. Structural Validation

| Check | Result |
|-------|--------|
| One source HTML | PASS |
| One page SCSS | PASS |
| One composition | PASS |
| One manifest | PASS |
| One HEADER_NAV | PASS |
| One MAIN | PASS |
| One BREADCRUMBS | PASS |
| One PAGE_IDENTITY | PASS |
| One SERVICE_DETAIL_CONTEXT | PASS |
| One H1 | PASS |
| One BENEFITS hook (`data-block-id="benefits"`) | PASS |
| One PROCESS hook (`data-block-id="process"`) | PASS |
| One FAQ hook (`data-block-id="faq"`) | PASS |
| One CTA hook (`data-block-id="cta_band"`) | PASS |
| One LEAD_FORM hook (`data-block-id="lead_form"`) | PASS |
| One FOOTER | PASS |
| LEGAL_LINKS in footer | PASS |
| SERVICES hook absent | PASS |
| Excluded hooks absent | PASS |
| SERVICE_DETAIL_CONTEXT has no data-block-id | PASS |
| No duplicate IDs | PASS |
| No unresolved includes | PASS |
| No production URLs / real service data | PASS |

---

## 14. Accessibility Validation

| Check | Result |
|-------|--------|
| One H1 linked to identity region | PASS |
| Heading hierarchy H1 → H2 → H3 | PASS |
| Breadcrumb nav semantics | PASS |
| Detail section labelled | PASS |
| FAQ native controls | PASS |
| Form labels associated | PASS |
| CTA controls accessible | PASS |
| No auto-focus | PASS |

**WCAG certification:** **Not claimed**

---

## 15. Runtime Boundary

| Check | Result |
|-------|--------|
| New page JS | **None** |
| Network requests on form | **None** — mockSubmit |
| Analytics | **None** |

**JavaScript reused:** `lifecycle.js` · `modal.js` · `form.js` · `header_nav.js` · `main.js`

---

## 16. Fictional Data

| Source | Data |
|--------|------|
| PAGE_IDENTITY | Neutral scaffold copy |
| SERVICE_DETAIL_CONTEXT | Fictional scope narrative and support list |
| BENEFITS partial | Neutral placeholder outcome props |
| PROCESS partial | Neutral placeholder workflow steps |
| FAQ partial | Neutral placeholder Q&A |
| CTA partial | Demo action labels |
| LEAD_FORM partial | Demo form fields |
| Real production data | **Absent** |

---

## 17. RSC Eligibility

| Field | Value |
|-------|-------|
| **Eligible** | **Yes** |
| **Delta** | **+1 SERVICE_PAGE** |
| **RSC before P4** | **5/10** |
| **RSC after P4** | **6/10** |
| **Evidence chain** | Registry row · source · SCSS · composition · manifest · build · report · Git |

---

## 18. PC Boundary

| Metric | Effect |
|--------|--------|
| **PROMO PC** | **Not accrued** — single page scaffold ≠ corridor PC |
| **CATALOG PC** | Unchanged |
| **LANDING PC** | Unchanged |

---

## 19. PROMO SC Boundary

| Field | Value |
|-------|-------|
| **PROMO SC evaluation** | **Not executed** |
| **PROMO SC PASS** | **Not granted** |
| **G2-R2 package** | **Implementation complete** — P5 exit pending |

---

## 20. Known Limitations

| Limitation | Notes |
|------------|-------|
| CONTACT_PAGE breadcrumbs | Still uses catalog-default trail — P2 debt unchanged |
| Live browser QA | Deferred — structural/CSS/build sanity pass only |
| W3 PARTIAL blocks | BENEFITS · PROCESS · FAQ · CTA · LEAD_FORM at existing maturity |
| SERVICES exclusion | One-service focus — no related-services block |
| Production readiness | **Not claimed** |

---

## 21. Git Evidence

| Field | Value |
|-------|-------|
| **Commit message** | `foundry: complete G2-R2 SERVICE_PAGE scaffold` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Commit binding** | `ce45379` — `foundry: complete G2-R2 SERVICE_PAGE scaffold` |

---

## 22. Decision

**SERVICE_PAGE scaffold manifest v1 — PUBLISHED / VALIDATED.**

Reference scaffold structurally complete for G2-R2 P4. RSC **+1** accrued. PROMO PC and PROMO SC unchanged. P5 PROMO exit authorized — not started.
