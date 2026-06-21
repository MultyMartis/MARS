# CHECKOUT Utility Reference Composition v1

**Site type:** ECOMMERCE (primary staging context)  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Surface class:** **Utility scaffold** — **not** registered `page_type`  
**Scaffold:** `src/pages/checkout-utility-reference.html`  
**Reference route role:** `/checkout/`  
**Authority:** [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) · [wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md](../../projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [global-shell-contract-v1.md](../../projects/mars-website-factory/global-shell-contract-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** working checkout. **Not** CHECKOUT_PAGE registration. **Not** RSC accrual without page-type addendum.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3.5 W6-D — Commerce Utility Scaffolds |
| **Build evidence** | `dist/checkout-utility-reference.html` — build PASS (W6-D) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Surface name** | CHECKOUT utility reference scaffold |
| **Registered page_type** | **NONE** |
| **Typical route role** | `/checkout/` (documentation intention only) |
| **Distinction from bounded host** | Global shell · breadcrumbs · PAGE_IDENTITY · sibling CHECKOUT + PAYMENT |
| **Distinction from CHECKOUT_PAGE** | No PAGE-TYPE-REGISTRY row · no RSC accrual |

---

## 3. Utility Status

| Field | Value |
|-------|-------|
| **Classification** | **UTILITY SCAFFOLD** |
| **Registered page_type** | **NONE** |
| **RSC eligibility** | **NO** — utility route without page-type addendum |
| **PC membership** | **PLANNED / NOT ACCRUED** — ECOMMERCE corridor PC is G4-only |
| **RPC effect** | **None** — CHECKOUT and PAYMENT partials already accrued at W6-B2/B3 |

---

## 4. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.5 charter | `projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md` | W6-D wave · utility scaffold requirement |
| W6-A preflight | `projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md` | Checkout stack composition |
| W6-G3R reconciliation | `projects/mars-website-factory/wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md` | G3 scaffold gap closure |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Utility vs page-type boundary |
| Page-Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | Utility route `/checkout/` |
| Scaffold Manifest | [CHECKOUT-UTILITY-SCAFFOLD-MANIFEST-v1.md](CHECKOUT-UTILITY-SCAFFOLD-MANIFEST-v1.md) | Build validation |

---

## 5. Purpose

Document the reference composition for the **CHECKOUT utility scaffold**: global shell, shallow breadcrumbs, scaffold-owned page identity, canonical CHECKOUT block with static order summary, and sibling PAYMENT block. Supports G3 ECOMMERCE staging evidence without claiming production readiness, delivery integration, or payment processing.

---

## 6. Shell

```text
HEADER_NAV

MAIN
├── reference disclosure
├── BREADCRUMBS
├── PAGE_IDENTITY
├── CHECKOUT
└── PAYMENT

FOOTER
└── LEGAL_LINKS
```

| Surface | Requirement | Present |
|---------|-------------|---------|
| HEADER_NAV | REQ | Yes |
| MAIN | REQ | `<main id="main" class="wf-checkout-utility">` |
| BREADCRUMBS | POL | **Included** — shallow fictional trail |
| FOOTER | REQ | Yes |
| LEGAL_LINKS | REQ | Nested in FOOTER |
| SEARCH / FILTERS / PAGINATION | N/A | **Absent** |

---

## 7. Block Sequence

```text
HEADER_NAV

MAIN
├── reference disclosure (scaffold-owned)
├── BREADCRUMBS
├── scaffold-owned PAGE_IDENTITY
├── CHECKOUT
└── PAYMENT

FOOTER
└── LEGAL_LINKS
```

Ordered MAIN includes:

1. Reference disclosure paragraph
2. `components/breadcrumbs.html` — shallow trail · current label `Checkout`
3. PAGE_IDENTITY (scaffold-owned)
4. `components/checkout.html` — block_id `CHECKOUT`
5. `components/payment.html` — block_id `PAYMENT`

**Layout:** Sequential sibling blocks. CHECKOUT owns order summary context. PAYMENT is **not** nested inside CHECKOUT partial root.

**DELIVERY:** **Not implemented.** CHECKOUT partial may expose neutral `data-checkout-slot` extension region only — not a DELIVERY block hook.

---

## 8. Scaffold-Owned Regions

| Region | Class root | `data-block-id` | Content |
|--------|------------|-----------------|---------|
| Reference disclosure | `wf-checkout-utility__disclosure` | **None** | Non-page-type honesty banner |
| PAGE_IDENTITY | `wf-checkout-utility__identity` | **None** | Eyebrow · one H1 · route role note |
| Main inner wrapper | `wf-checkout-utility__inner` | **None** | Container + section rhythm |

---

## 9. Required Blocks

| block_id | Partial | Role |
|----------|---------|------|
| HEADER_NAV | `layout/header.html` → `sections/header-nav.html` | Global shell |
| BREADCRUMBS | `components/breadcrumbs.html` | Shallow navigation trail |
| CHECKOUT | `components/checkout.html` | Static checkout form + order summary |
| PAYMENT | `components/payment.html` | Fictional payment method selection |
| FOOTER | `sections/footer.html` | Global shell |
| LEGAL_LINKS | `components/legal-links.html` (nested) | Legal navigation |

---

## 10. Forbidden Blocks

| block_id | Reason |
|----------|--------|
| CART | Cart belongs on `/cart/` utility scaffold |
| DELIVERY | G4-only — not implemented |
| LEAD_FORM | Out of checkout utility scope |
| PRODUCT_GRID | Out of checkout utility scope |
| CHECKOUT (duplicate) | Exactly one CHECKOUT hook required |
| PAYMENT (duplicate) | Exactly one PAYMENT hook required |

---

## 11. CHECKOUT Role

| Field | Value |
|-------|-------|
| **block_id** | `CHECKOUT` |
| **Partial** | `src/partials/components/checkout.html` |
| **Hook** | `data-block-id="checkout"` |
| **Count** | **One** |
| **Order summary** | Owned inside CHECKOUT partial |
| **DELIVERY slot** | Neutral extension slot only — **not** DELIVERY block |
| **Modification** | **None** — canonical partial reused as-is |

---

## 12. PAYMENT Role

| Field | Value |
|-------|-------|
| **block_id** | `PAYMENT` |
| **Partial** | `src/partials/components/payment.html` |
| **Hook** | `data-block-id="payment"` |
| **Count** | **One** |
| **Composition** | Sibling block after CHECKOUT |
| **Modification** | **None** — canonical partial reused as-is |

---

## 13. Variation Policy

| Variation | Policy |
|-----------|--------|
| Default checkout form | **Visible** — fictional customer/address fields |
| Payment methods | Static radio selection — presentation-only |
| Order confirmation | **Not implemented** |
| DELIVERY region | Extension slot only — no DELIVERY partial |

---

## 14. Fictional Content Policy

| Field | Value |
|-------|-------|
| **PAGE_IDENTITY** | Neutral scaffold copy · route role `/checkout/` |
| **CHECKOUT partial** | Fictional customer · address · static summary |
| **PAYMENT partial** | Fictional payment methods |
| **Production data** | **Forbidden** |
| **Real payment data** | **Forbidden** |

---

## 15. Runtime Boundary

| Capability | State |
|------------|-------|
| Checkout submission | **None** |
| Payment processing | **None** |
| Storage / cookies | **None** |
| fetch / XHR | **None** |
| Order creation | **None** |
| Cart persistence | **None** |
| Analytics | **None** |
| Production URLs | **None** |

---

## 16. Accessibility

| Check | State |
|-------|-------|
| One H1 | `checkout-utility-title` in PAGE_IDENTITY |
| Identity region | `aria-labelledby="checkout-utility-title"` |
| Breadcrumbs | `<nav aria-label="Breadcrumb">` · `aria-current="page"` |
| CHECKOUT headings | H2 inside canonical partial |
| PAYMENT headings | H2 inside canonical partial |
| Field labels / fieldsets | Present in canonical partials |
| Duplicate IDs | **None** — single CHECKOUT and single PAYMENT instance |

**WCAG certification:** **Not claimed**

---

## 17. Responsive Notes

| Breakpoint behaviour | Policy |
|---------------------|--------|
| PAGE_IDENTITY | Long title wraps via `overflow-wrap` |
| CHECKOUT | Canonical partial owns internal two-column layout |
| PAYMENT | Stacks below CHECKOUT with page-level spacing |
| Horizontal overflow | **None** expected — `wf-container` inner |
| Summary order | Order summary inside CHECKOUT partial — unchanged |

---

## 18. Coverage Boundary

| Metric | Effect |
|--------|--------|
| **RSC** | **None** — utility scaffold without registered page_type |
| **RPC** | **None** — CHECKOUT/PAYMENT partials already accrued |
| **PC** | **None** — ECOMMERCE PC accrual is G4-only |
| **SC** | **Staging evidence input** — not formal SC PASS |

---

## 19. Evidence Paths

| Artefact | Path |
|----------|------|
| Source scaffold | `workspaces/website-factory-reference-v1/src/pages/checkout-utility-reference.html` |
| Dist output | `workspaces/website-factory-reference-v1/dist/checkout-utility-reference.html` |
| Page SCSS | `workspaces/website-factory-reference-v1/src/scss/pages/_checkout-utility-reference.scss` |
| Manifest | `workspaces/website-factory-reference-v1/page-architecture/CHECKOUT-UTILITY-SCAFFOLD-MANIFEST-v1.md` |
| W6-D report | `reports/wf-r01-3-5-w6-d-commerce-utility-scaffolds-v1.md` |

---

## 20. Decision

**CHECKOUT utility reference composition v1 — PUBLISHED.**

Approved sequence locked for W6-D. Feeds G3 ECOMMERCE staging scaffold evidence. **Not** CHECKOUT_PAGE registration. **Not** RSC accrual. **Not** ECOMMERCE PC evidence. **Not** G3 PASS.
