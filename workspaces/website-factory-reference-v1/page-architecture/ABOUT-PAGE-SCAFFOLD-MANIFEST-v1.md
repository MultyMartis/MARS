# ABOUT_PAGE Scaffold Manifest v1

**Page type:** `ABOUT_PAGE`  
**Site type:** `PROMO` (primary)  
**Scaffold file:** `src/pages/about-page-reference.html`  
**Output:** `dist/about-page-reference.html`  
**Status:** PUBLISHED / VALIDATED  
**Metric:** RSC — global **+1** when G2-R2 P3 evidence accepted

**Authority:** [wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md](../../projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [page-type-shell-matrix-v1.md](../../projects/mars-website-factory/page-type-shell-matrix-v1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED / VALIDATED** |
| **Validation wave** | WF-R01.3 G2-R2 P3 |
| **Build** | PASS |
| **Structural validation** | PASS |
| **Accessibility minimum** | PASS |
| **Live browser spot-check** | DEFERRED — minor note |

---

## 2. Page Type

| Field | Value |
|-------|-------|
| **page_type** | `ABOUT_PAGE` |
| **Registry** | [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) § ABOUT_PAGE |
| **Allowed site types** | PROMO · CORPORATE |
| **Primary corridor** | PROMO money-page scaffold package (G2-R2) |

---

## 3. Authority

| Document | Path |
|----------|------|
| G2-R2 P1 preflight | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-scaffold-preflight-composition-decisions-v1.md` |
| G2-R2 charter | `projects/mars-website-factory/wf-r01-3-g2-r2-promo-money-page-scaffold-completion-charter-v1.md` |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| Composition | [ABOUT-PAGE-REFERENCE-COMPOSITION-v1.md](ABOUT-PAGE-REFERENCE-COMPOSITION-v1.md) |

---

## 4. Source Path

`workspaces/website-factory-reference-v1/src/pages/about-page-reference.html`

---

## 5. Dist Path

`workspaces/website-factory-reference-v1/dist/about-page-reference.html`

---

## 6. SCSS Path

| Layer | Path |
|-------|------|
| Entry import | `src/scss/main.scss` — `@use 'pages/about-page-reference'` |
| Page layout | `src/scss/pages/_about-page-reference.scss` |
| Block styles | Existing — `_about.scss` · `_team.scss` · `_trust.scss` unchanged |

---

## 7. Shell Requirements

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main" class="wf-about-page">
FOOTER      →  sections/footer.html (after </main>)
  └── LEGAL_LINKS → components/legal-links.html (nested)
```

| Surface | Requirement | Present |
|---------|-------------|---------|
| HEADER_NAV | REQ | Yes |
| MAIN | REQ | Yes — exactly one |
| BREADCRUMBS | REQ — included | Yes |
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
| 3 | `partials/components/about.html` | ABOUT |
| 4 | `partials/components/team.html` | TEAM |
| 5 | `partials/sections/trust.html` | TRUST |
| Shell | `partials/sections/footer.html` | FOOTER (+ LEGAL_LINKS) |

---

## 9. Scaffold-Owned Regions

| Region | Selector | `data-block-id` |
|--------|----------|-----------------|
| PAGE_IDENTITY | `.wf-about-page__identity` | None |
| Inner wrapper | `.wf-about-page__inner` | None |

---

## 10. Excluded Blocks

PROCESS · SERVICES · BENEFITS · CTA · LEAD_FORM · CONTACTS · FAQ · MAP · HERO · catalog/commerce blocks · COMPANY_STORY · MISSION · HISTORY · VALUES

---

## 11. Breadcrumb Decision

| Field | Value |
|-------|-------|
| **Canonical path** | `src/partials/components/breadcrumbs.html` |
| **P2 debt** | CONTACT_PAGE used catalog-default trail — documented limitation |
| **P3 decision** | **Solution A** — universal shallow variant via `currentLabel` include parameter |
| **ABOUT_PAGE trail** | `Home` → `About` |
| **Partial modification** | Minimal parameterization — optional `currentLabel` triggers shallow two-item trail |
| **Default behaviour** | Unparameterized includes retain catalog demo trail |
| **Regression** | CATEGORY_PAGE · PRODUCT_PAGE · CONTACT_PAGE · breadcrumbs-reference — build PASS |

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
| One H1 | PASS |
| One ABOUT hook (`data-block-id="about"`) | PASS |
| One TEAM hook (`data-block-id="team"`) | PASS |
| One TRUST hook (`data-block-id="trust"`) | PASS |
| One FOOTER | PASS |
| LEGAL_LINKS in footer | PASS |
| Excluded hooks absent | PASS |
| No duplicate IDs | PASS |
| No unresolved includes | PASS |
| No production URLs / real company data | PASS |

---

## 14. Accessibility Validation

| Check | Result |
|-------|--------|
| One H1 linked to identity region | PASS |
| Heading hierarchy H1 → H2 → H3 | PASS |
| Breadcrumb nav semantics | PASS |
| ABOUT narrative text accessible | PASS |
| TEAM names/roles text accessible | PASS |
| TRUST metrics/badges text accessible | PASS |
| Decorative media hidden from AT | PASS |
| No auto-focus | PASS |

**WCAG certification:** **Not claimed**

---

## 15. Runtime Boundary

| Check | Result |
|-------|--------|
| New page JS | **None** |
| Network requests | **None** |
| TEAM modal/profile runtime | **None** |
| Analytics | **None** |

**JavaScript reused:** `lifecycle.js` · `header_nav.js` · `main.js`

---

## 16. Fictional Data

| Source | Data |
|--------|------|
| PAGE_IDENTITY | Neutral scaffold copy |
| ABOUT partial | Fictional organisation narrative |
| TEAM partial | Fictional personas — Alex Morgan et al. |
| TRUST partial | Reference metrics · generic logo text · demo badges |
| Real production data | **Absent** |

---

## 17. RSC Eligibility

| Field | Value |
|-------|-------|
| **Eligible** | **Yes** |
| **Delta** | **+1 ABOUT_PAGE** |
| **RSC before P3** | **4/10** |
| **RSC after P3** | **5/10** |
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
| **G2-R2 package** | **Not complete** — SERVICE_PAGE remains |

---

## 20. Known Limitations

| Limitation | Notes |
|------------|-------|
| CONTACT_PAGE breadcrumbs | Still uses catalog-default trail — P2 debt unchanged |
| Live browser QA | Deferred — structural/CSS/build sanity pass only |
| W3 PARTIAL blocks | ABOUT · TEAM · TRUST at PARTIAL/T1+ maturity |
| Production readiness | **Not claimed** |

---

## 21. Git Evidence

| Field | Value |
|-------|-------|
| **Commit message** | `foundry: complete G2-R2 ABOUT_PAGE scaffold` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Commit binding** | `c1aee8f` — `foundry: complete G2-R2 ABOUT_PAGE scaffold` |

---

## 22. Decision

**ABOUT_PAGE scaffold manifest v1 — PUBLISHED / VALIDATED.**

Reference scaffold structurally complete for G2-R2 P3. RSC **+1** accrued. PROMO PC and PROMO SC unchanged. P4 SERVICE_PAGE authorized — not started.
