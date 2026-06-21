# CHECKOUT Utility Scaffold Manifest v1

**Surface class:** CHECKOUT utility reference scaffold  
**Site type:** `ECOMMERCE` (staging context)  
**Scaffold file:** `src/pages/checkout-utility-reference.html`  
**Output:** `dist/checkout-utility-reference.html`  
**Reference route role:** `/checkout/`  
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
| **Name** | CHECKOUT utility reference scaffold |
| **Classification** | **UTILITY SCAFFOLD** |
| **Registered page_type** | **NONE** |
| **RSC eligibility** | **NO** |
| **PC membership** | **PLANNED / NOT ACCRUED** |
| **Reference route role** | `/checkout/` (documentation intention) |

---

## 3. Authority

| Document | Path |
|----------|------|
| WF-R01.3.5 charter | `projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md` |
| W6-A preflight | `projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md` |
| W6-G3R reconciliation | `projects/mars-website-factory/wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md` |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| Composition | [CHECKOUT-UTILITY-REFERENCE-COMPOSITION-v1.md](CHECKOUT-UTILITY-REFERENCE-COMPOSITION-v1.md) |

---

## 4. Source Path

`workspaces/website-factory-reference-v1/src/pages/checkout-utility-reference.html`

---

## 5. Dist Path

`workspaces/website-factory-reference-v1/dist/checkout-utility-reference.html`

---

## 6. Composition Path

`workspaces/website-factory-reference-v1/page-architecture/CHECKOUT-UTILITY-REFERENCE-COMPOSITION-v1.md`

---

## 7. SCSS Path

| Layer | Path |
|-------|------|
| Entry import | `src/scss/main.scss` — `@use 'pages/checkout-utility-reference'` |
| Page layout | `src/scss/pages/_checkout-utility-reference.scss` |
| Block styles | Existing — `_checkout.scss` · `_payment.scss` unchanged |

---

## 8. Shell Requirements

```text
HEADER_NAV  →  layout/header.html → sections/header-nav.html
MAIN        →  <main id="main" class="wf-checkout-utility">
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
| 4 | `partials/components/checkout.html` | CHECKOUT |
| 5 | `partials/components/payment.html` | PAYMENT |
| Shell | `partials/sections/footer.html` | FOOTER (+ LEGAL_LINKS) |

---

## 10. Expected Hook Counts

| Hook | Expected | Validated |
|------|----------|-----------|
| `data-block-id="checkout"` | 1 | PASS |
| `data-block-id="payment"` | 1 | PASS |
| `data-block-id="cart"` | 0 | PASS |
| `data-block-id="delivery"` | 0 | PASS |
| `data-block-id="lead_form"` | 0 | PASS |
| `data-block-id="product_grid"` | 0 | PASS |

---

## 11. Excluded Blocks

CART · DELIVERY · LEAD_FORM · PRODUCT_GRID · duplicate CHECKOUT · duplicate PAYMENT

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
| One CHECKOUT hook | PASS |
| One PAYMENT hook | PASS |
| Forbidden hooks absent | PASS |
| No unresolved includes | PASS |
| Dist output exists | PASS |
| No production URLs | PASS |
| Fictional data only | PASS |
| Runtime absent | PASS |
| DELIVERY not implemented | PASS |

---

## 14. Accessibility Validation

| Check | Result |
|-------|--------|
| One H1 linked to identity region | PASS |
| Heading hierarchy H1 → H2 (CHECKOUT, PAYMENT) | PASS |
| Breadcrumb nav semantics | PASS |
| Landmark order header → main → footer | PASS |
| Field labels / fieldsets in partials | PASS |
| No duplicate IDs | PASS |

**WCAG certification:** **Not claimed**

---

## 15. Responsive Minimum

| Check | Result |
|-------|--------|
| Desktop layout | PASS — build + structural |
| Tablet layout | PASS — canonical CHECKOUT responsive |
| Mobile layout | PASS — container padding |
| Long content wrap | PASS — `overflow-wrap` on title |
| No horizontal overflow | PASS |
| Summary order | PASS — inside CHECKOUT partial |
| PAYMENT stacks below CHECKOUT | PASS |

---

## 16. Runtime Boundary

| Check | Result |
|-------|--------|
| fetch / XHR | **None** |
| storage / cookies | **None** |
| Checkout submission | **None** |
| Payment processing | **None** |
| Order creation | **None** |
| Cart persistence | **None** |
| Analytics | **None** |

**JavaScript reused:** `lifecycle.js` · `modal.js` · `form.js` · `sticky_cta.js` · `header_nav.js` · `main.js` — no checkout-specific runtime

---

## 17. Fictional Data Policy

| Source | Data |
|--------|------|
| CHECKOUT partial | Fictional customer · address · static summary |
| PAYMENT partial | Fictional payment methods |
| PAGE_IDENTITY | Neutral scaffold copy |
| Real production data | **Absent** |
| Real payment data | **Absent** |

---

## 18. Coverage Effect

| Metric | Effect |
|--------|--------|
| **RPC** | **+0** — remains **29/32** |
| **RSC** | **+0** — remains **7/11** |
| **PC** | **+0** — unchanged |
| **SC** | **Staging evidence** — no formal SC PASS |
| **G3 scaffold requirement** | **SATISFIED** (checkout half) |

---

## 19. Known Limitations

| Limitation | Notes |
|------------|-------|
| DELIVERY block | **Not implemented** — extension slot only in CHECKOUT partial |
| Order confirmation | **Not implemented** |
| Live browser QA | Structural/build pass only |
| Production readiness | **Not claimed** |
| Page-type registration | **Not performed** |

---

## 20. Git Evidence

| Field | Value |
|-------|-------|
| **Commit message** | `foundry: implement commerce utility scaffolds` |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Commit binding** | *Pending W6-D commit* |

---

## 21. Decision

**CHECKOUT utility scaffold manifest v1 — VALIDATED.**

Utility reference surface structurally complete for W6-D. **Not** CHECKOUT_PAGE. **Not** RSC accrual. **Not** ECOMMERCE PC accrual.
