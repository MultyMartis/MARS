# CART Utility Scaffold Manifest v1

**Surface class:** CART utility reference scaffold  
**Site type:** `ECOMMERCE` (staging context)  
**Scaffold file:** `src/pages/cart-utility-reference.html`  
**Output:** `dist/cart-utility-reference.html`  
**Reference route role:** `/cart/`  
**Status:** VALIDATED  
**Registered page_type:** **NONE**

**Authority:** [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) · [wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md](../../projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [global-shell-contract-v1.md](../../projects/mars-website-factory/global-shell-contract-v1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **VALIDATED** |
| **Validation wave** | WF-R01.3.5 W6-D |
| **Build** | PASS |
| **Structural validation** | PASS |
| **Accessibility minimum** | PASS |
| **Runtime boundary** | PASS — static only |

---

## 2. Scaffold Identity

| Field | Value |
|-------|-------|
| **Name** | CART utility reference scaffold |
| **Classification** | **UTILITY SCAFFOLD** |
| **Registered page_type** | **NONE** |
| **RSC eligibility** | **NO** |
| **PC membership** | **PLANNED / NOT ACCRUED** |
| **Reference route role** | `/cart/` (documentation intention) |

---

## 3. Authority

| Document | Path |
|----------|------|
| WF-R01.3.5 charter | `projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md` |
| W6-A preflight | `projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md` |
| W6-G3R reconciliation | `projects/mars-website-factory/wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md` |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| Composition | [CART-UTILITY-REFERENCE-COMPOSITION-v1.md](CART-UTILITY-REFERENCE-COMPOSITION-v1.md) |

---

## 4. Source Path

`workspaces/website-factory-reference-v1/src/pages/cart-utility-reference.html`

---

## 5. Dist Path

`workspaces/website-factory-reference-v1/dist/cart-utility-reference.html`

---

## 6. Composition Path

`workspaces/website-factory-reference-v1/page-architecture/CART-UTILITY-REFERENCE-COMPOSITION-v1.md`

---

## 7. SCSS Path

| Layer | Path |
|-------|------|
| Entry import | `src/scss/main.scss` — `@use 'pages/cart-utility-reference'` |
| Page layout | `src/scss/pages/_cart-utility-reference.scss` |
| Block styles | Existing — `_cart.scss` unchanged |

---

## 8. Shell Requirements

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main" class="wf-cart-utility">
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
| Reference disclosure | Scaffold policy | Yes |

---

## 9. Canonical Includes

| Order | Include path | block_id / role |
|-------|--------------|-----------------|
| Shell | `partials/layout/header.html` | HEADER_NAV |
| 1 | scaffold-owned disclosure | — |
| 2 | `partials/components/breadcrumbs.html` | BREADCRUMBS |
| 3 | scaffold-owned PAGE_IDENTITY | — |
| 4 | `partials/components/cart.html` | CART |
| Shell | `partials/sections/footer.html` | FOOTER (+ LEGAL_LINKS) |

---

## 10. Expected Hook Counts

| Hook | Expected | Validated |
|------|----------|-----------|
| `data-block-id="cart"` | 1 | PASS |
| `data-block-id="checkout"` | 0 | PASS |
| `data-block-id="payment"` | 0 | PASS |
| `data-block-id="delivery"` | 0 | PASS |
| `data-block-id="lead_form"` | 0 | PASS |
| `data-block-id="product_grid"` | 0 | PASS |

---

## 11. Excluded Blocks

CHECKOUT · PAYMENT · DELIVERY · LEAD_FORM · PRODUCT_GRID · duplicate CART

---

## 12. Build Command

```bash
npm run build
```

**Workspace:** `workspaces/website-factory-reference-v1/`

---

## 13. Validation Checklist

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
| One CART hook | PASS |
| Forbidden hooks absent | PASS |
| No unresolved includes | PASS |
| Dist output exists | PASS |
| No production URLs | PASS |
| Fictional data only | PASS |
| Runtime absent | PASS |

---

## 14. Accessibility Validation

| Check | Result |
|-------|--------|
| One H1 linked to identity region | PASS |
| Heading hierarchy H1 → H2 (CART) | PASS |
| Breadcrumb nav semantics | PASS |
| Landmark order header → main → footer | PASS |
| Field labels in CART partial | PASS |
| No duplicate IDs | PASS |

**WCAG certification:** **Not claimed**

---

## 15. Responsive Minimum

| Check | Result |
|-------|--------|
| Desktop layout | PASS — build + structural |
| Tablet layout | PASS — canonical CART responsive |
| Mobile layout | PASS — container padding |
| Long content wrap | PASS — `overflow-wrap` on title |
| No horizontal overflow | PASS — `overflow-x: hidden` on body |
| Footer order | PASS |

---

## 16. Runtime Boundary

| Check | Result |
|-------|--------|
| fetch / XHR | **None** |
| storage / cookies | **None** |
| Cart persistence | **None** |
| Checkout submission | **None** |
| Payment processing | **None** |
| Order creation | **None** |
| Analytics | **None** |

**JavaScript reused:** `lifecycle.js` · `modal.js` · `form.js` · `sticky_cta.js` · `header_nav.js` · `main.js` — no cart-specific runtime

---

## 17. Fictional Data Policy

| Source | Data |
|--------|------|
| CART partial | Fictional SKUs · static prices · static totals |
| PAGE_IDENTITY | Neutral scaffold copy |
| Real production data | **Absent** |
| Real customer data | **Absent** |

---

## 18. Coverage Effect

| Metric | Effect |
|--------|--------|
| **RPC** | **+0** — remains **29/32** |
| **RSC** | **+0** — remains **7/11** |
| **PC** | **+0** — unchanged |
| **SC** | **Staging evidence** — no formal SC PASS |
| **G3 scaffold requirement** | **SATISFIED** (cart half) |

---

## 19. Known Limitations

| Limitation | Notes |
|------------|-------|
| Empty cart variation | Hidden in canonical partial — not toggled on utility scaffold |
| Live browser QA | Structural/build pass only |
| Production readiness | **Not claimed** |
| Page-type registration | **Not performed** |

---

## 20. Git Evidence

| Field | Value |
|-------|-------|
| **Commit message** | `foundry: implement commerce utility scaffolds` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Commit binding** | `0429317` — `foundry: implement commerce utility scaffolds` |

---

## 21. Decision

**CART utility scaffold manifest v1 — VALIDATED.**

Utility reference surface structurally complete for W6-D. **Not** CART_PAGE. **Not** RSC accrual. **Not** ECOMMERCE PC accrual.
