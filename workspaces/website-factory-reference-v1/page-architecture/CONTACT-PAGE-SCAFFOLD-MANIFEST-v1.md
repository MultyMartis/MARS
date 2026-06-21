# CONTACT_PAGE Scaffold Manifest v1

**Page type:** `CONTACT_PAGE`  
**Site type:** `PROMO` (primary)  
**Scaffold file:** `src/pages/contact-page-reference.html`  
**Output:** `dist/contact-page-reference.html`  
**Status:** PUBLISHED / VALIDATED  
**Metric:** RSC — global **+1** when G2-R2 P2 evidence accepted

**Authority:** [wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md](../../projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED / VALIDATED** |
| **Validation wave** | WF-R01.3 G2-R2 P2 |
| **Build** | PASS |
| **Structural validation** | PASS |
| **Accessibility minimum** | PASS |
| **Live browser spot-check** | DEFERRED — minor note |

---

## 2. Page Type

| Field | Value |
|-------|-------|
| **page_type** | `CONTACT_PAGE` |
| **Registry** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) § CONTACT_PAGE |
| **Allowed site types** | PROMO · CATALOG · ECOMMERCE · CORPORATE |
| **Primary corridor** | PROMO money-page scaffold package (G2-R2) |

---

## 3. Authority

| Document | Path |
|----------|------|
| G2-R2 P1 preflight | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md` |
| G2-R2 charter | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md` |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| Composition | [CONTACT-PAGE-REFERENCE-COMPOSITION-v1.md](CONTACT-PAGE-REFERENCE-COMPOSITION-v1.md) |

---

## 4. Source Path

`workspaces/website-factory-reference-v1/src/pages/contact-page-reference.html`

---

## 5. Dist Path

`workspaces/website-factory-reference-v1/dist/contact-page-reference.html`

---

## 6. SCSS Path

| Layer | Path |
|-------|------|
| Entry import | `src/scss/main.scss` — `@use 'pages/contact-page-reference'` |
| Page layout | `src/scss/pages/_contact-page-reference.scss` |
| Block styles | Existing — `_contact_block.scss` · `_lead_form.scss` unchanged |

---

## 7. Shell Requirements

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main" class="wf-contact-page">
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
| 1 | `partials/components/breadcrumbs.html` | BREADCRUMBS (Tier B) |
| 2 | scaffold-owned PAGE_IDENTITY | — |
| 3 | `partials/sections/contact_block.html` | CONTACTS |
| 4 | `partials/sections/lead_form.html` | LEAD_FORM |
| Shell | `partials/sections/footer.html` | FOOTER (+ LEGAL_LINKS) |

---

## 9. Scaffold-Owned Regions

| Region | Selector | `data-block-id` |
|--------|----------|-----------------|
| PAGE_IDENTITY | `.wf-contact-page__identity` | None |
| Inner wrapper | `.wf-contact-page__inner` | None |

---

## 10. Excluded Blocks

MAP · TRUST · FAQ · CTA · HERO · ABOUT · TEAM · PROCESS · BENEFITS · SERVICES · catalog/commerce blocks · CONTACT CONTEXT wrapper

---

## 11. Build Command

```bash
npm run build
```

**Workspace:** `workspaces/website-factory-reference-v1/`

---

## 12. Structural Validation

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
| One H1 | PASS |
| One CONTACTS hook (`data-block-id="contact_block"`) | PASS |
| One LEAD_FORM hook (`data-block-id="lead_form"`) | PASS |
| One FOOTER | PASS |
| LEGAL_LINKS in footer | PASS |
| Excluded hooks absent | PASS |
| No duplicate `#lead-form` / `#lead-name` / `#lead-phone` | PASS |
| No unresolved includes | PASS |

---

## 13. Accessibility Validation

| Check | Result |
|-------|--------|
| One H1 linked to identity region | PASS |
| Heading hierarchy | PASS |
| Breadcrumb nav semantics | PASS |
| Contact text accessible | PASS |
| Form labels associated | PASS |
| Error regions present | PASS |
| No auto-focus | PASS |
| No placeholder-only labels | PASS |

**WCAG certification:** **Not claimed**

---

## 14. Runtime Boundary

| Check | Result |
|-------|--------|
| Form network request | **None** — `mockSubmit` path |
| Map embed / API | **None** |
| New page JS | **None** |
| Analytics | **None** |

**JavaScript reused:** `lifecycle.js` · `form.js` · `header_nav.js` · `main.js`

---

## 15. Fictional Data

| Source | Data |
|--------|------|
| CONTACTS partial | `+1 (555) 123-4567` · `hello@example.com` · demo hours |
| Map link | Generic Google Maps homepage — placeholder |
| PAGE_IDENTITY | Neutral scaffold copy |
| Real production contacts | **Absent** |

---

## 16. RSC Eligibility

| Field | Value |
|-------|-------|
| **Eligible** | **Yes** |
| **Delta** | **+1 CONTACT_PAGE** |
| **RSC before P2** | **3/10** |
| **RSC after P2** | **4/10** |
| **Evidence chain** | Registry row · source · SCSS · composition · manifest · build · report · Git |

---

## 17. PC Boundary

| Metric | Effect |
|--------|--------|
| **PROMO PC** | **Not accrued** — single page scaffold ≠ corridor PC |
| **CATALOG PC** | Unchanged |
| **LANDING PC** | Unchanged |

---

## 18. PROMO SC Boundary

| Field | Value |
|-------|-------|
| **PROMO SC evaluation** | **Not executed** |
| **PROMO SC PASS** | **Not granted** |
| **G2-R2 package** | **Not complete** — ABOUT_PAGE · SERVICE_PAGE remain |

---

## 19. Known Limitations

| Limitation | Notes |
|------------|-------|
| Breadcrumbs trail | Canonical partial uses generic demo trail — not contact-specific IA |
| Live browser QA | Deferred — structural/CSS/build sanity pass only |
| Form delivery | Presentation-only — no backend |
| Map | External link only — no embed |
| Production readiness | **Not claimed** |

---

## 20. Git Evidence

| Field | Value |
|-------|-------|
| **Commit message** | `foundry: complete G2-R2 CONTACT_PAGE scaffold` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Commit binding** | Set on commit — see P2 report §22 |

---

## 21. Decision

**CONTACT_PAGE scaffold manifest v1 — PUBLISHED / VALIDATED.**

Reference scaffold structurally complete for G2-R2 P2. RSC **+1** accrued. PROMO PC and PROMO SC unchanged. P3 ABOUT_PAGE authorized — not started.
