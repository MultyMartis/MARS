# CART Utility Reference Composition v1

**Site type:** ECOMMERCE (primary staging context)  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Composition version:** v1  
**Status:** PUBLISHED  
**Surface class:** **Utility scaffold** — **not** registered `page_type`  
**Scaffold:** `src/pages/cart-utility-reference.html`  
**Reference route role:** `/cart/`  
**Authority:** [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](../../projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) · [wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md](../../projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md) · [reference-scaffold-contract-v1.md](../../projects/mars-website-factory/reference-scaffold-contract-v1.md) · [global-shell-contract-v1.md](../../projects/mars-website-factory/global-shell-contract-v1.md)

**Honesty boundary:** Reference composition documentation only. **Not** production acceptance. **Not** working cart. **Not** CART_PAGE registration. **Not** RSC accrual without page-type addendum.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Publication wave** | WF-R01.3.5 W6-D — Commerce Utility Scaffolds |
| **Build evidence** | `dist/cart-utility-reference.html` — build PASS (W6-D) |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Surface name** | CART utility reference scaffold |
| **Registered page_type** | **NONE** |
| **Typical route role** | `/cart/` (documentation intention only) |
| **Distinction from bounded host** | Global shell · breadcrumbs · PAGE_IDENTITY · full utility surface |
| **Distinction from CART_PAGE** | No PAGE-TYPE-REGISTRY row · no RSC accrual |

---

## 3. Utility Status

| Field | Value |
|-------|-------|
| **Classification** | **UTILITY SCAFFOLD** |
| **Registered page_type** | **NONE** |
| **RSC eligibility** | **NO** — utility route without page-type addendum |
| **PC membership** | **PLANNED / NOT ACCRUED** — ECOMMERCE corridor PC is G4-only |
| **RPC effect** | **None** — canonical CART partial already accrued at W6-B1 |

---

## 4. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.5 charter | `projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md` | W6-D wave · utility scaffold requirement |
| W6-A preflight | `projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md` | Utility route composition policy |
| W6-G3R reconciliation | `projects/mars-website-factory/wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md` | G3 scaffold gap closure |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Utility vs page-type boundary |
| Page-Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | Utility route `/cart/` |
| Scaffold Manifest | [CART-UTILITY-SCAFFOLD-MANIFEST-v1.md](CART-UTILITY-SCAFFOLD-MANIFEST-v1.md) | Build validation |

---

## 5. Purpose

Document the reference composition for the **CART utility scaffold**: global shell, shallow breadcrumbs, scaffold-owned page identity, and one canonical CART block in populated default state. Supports G3 ECOMMERCE staging evidence without claiming production readiness, cart persistence, or checkout integration.

---

## 6. Shell

```text
HEADER_NAV

MAIN
├── reference disclosure
├── BREADCRUMBS
├── PAGE_IDENTITY
└── CART

FOOTER
└── LEGAL_LINKS
```

| Surface | Requirement | Present |
|---------|-------------|---------|
| HEADER_NAV | REQ | Yes |
| MAIN | REQ | `<main id="main" class="wf-cart-utility">` |
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
└── CART

FOOTER
└── LEGAL_LINKS
```

Ordered MAIN includes:

1. Reference disclosure paragraph
2. `components/breadcrumbs.html` — shallow trail · current label `Cart`
3. PAGE_IDENTITY (scaffold-owned)
4. `components/cart.html` — block_id `CART`

**Layout:** Sequential sections. Canonical CART partial retains self-contained section container.

---

## 8. Scaffold-Owned Regions

| Region | Class root | `data-block-id` | Content |
|--------|------------|-----------------|---------|
| Reference disclosure | `wf-cart-utility__disclosure` | **None** | Non-page-type honesty banner |
| PAGE_IDENTITY | `wf-cart-utility__identity` | **None** | Eyebrow · one H1 · route role note |
| Main inner wrapper | `wf-cart-utility__inner` | **None** | Container + section rhythm |

---

## 9. Required Blocks

| block_id | Partial | Role |
|----------|---------|------|
| HEADER_NAV | `layout/header.html` → `sections/header-nav.html` | Global shell |
| BREADCRUMBS | `components/breadcrumbs.html` | Shallow navigation trail |
| CART | `components/cart.html` | Fictional populated cart |
| FOOTER | `sections/footer.html` | Global shell |
| LEGAL_LINKS | `components/legal-links.html` (nested) | Legal navigation |

---

## 10. Forbidden Blocks

| block_id | Reason |
|----------|--------|
| CHECKOUT | Checkout belongs on `/checkout/` utility scaffold |
| PAYMENT | Payment belongs on `/checkout/` utility scaffold |
| DELIVERY | G4-only — not implemented |
| LEAD_FORM | Out of cart utility scope |
| PRODUCT_GRID | Out of cart utility scope |
| CART (duplicate) | Exactly one CART hook required |

---

## 11. CART Role

| Field | Value |
|-------|-------|
| **block_id** | `CART` |
| **Partial** | `src/partials/components/cart.html` |
| **Hook** | `data-block-id="cart"` |
| **Count** | **One** |
| **Default state** | Populated fictional line items |
| **Empty variation** | Included in canonical partial as hidden `data-cart-variation="empty"` — **not** duplicated |
| **Modification** | **None** — canonical partial reused as-is |

---

## 12. Variation Policy

| Variation | Policy |
|-----------|--------|
| Populated cart | **Default visible** on utility scaffold |
| Empty cart | **Hidden** in canonical partial — no separate block ID |
| Checkout CTA | Presentation-only link in CART partial — no routing |

---

## 13. Fictional Content Policy

| Field | Value |
|-------|-------|
| **PAGE_IDENTITY** | Neutral scaffold copy · route role `/cart/` |
| **CART partial** | Fictional SKUs · static quantities · static totals |
| **Production data** | **Forbidden** |
| **Real customer data** | **Forbidden** |

---

## 14. Runtime Boundary

| Capability | State |
|------------|-------|
| Cart persistence | **None** |
| Storage / cookies | **None** |
| fetch / XHR | **None** |
| Checkout submission | **None** |
| Payment processing | **None** |
| Order creation | **None** |
| Analytics | **None** |
| Production URLs | **None** |

---

## 15. Accessibility

| Check | State |
|-------|-------|
| One H1 | `cart-utility-title` in PAGE_IDENTITY |
| Identity region | `aria-labelledby="cart-utility-title"` |
| Breadcrumbs | `<nav aria-label="Breadcrumb">` · `aria-current="page"` |
| CART block heading | H2 inside canonical partial — logical hierarchy |
| Field labels | Quantity inputs labelled in canonical partial |
| Duplicate IDs | **None** — single CART instance |

**WCAG certification:** **Not claimed**

---

## 16. Responsive Notes

| Breakpoint behaviour | Policy |
|---------------------|--------|
| PAGE_IDENTITY | Long title wraps via `overflow-wrap` |
| CART | Canonical partial owns internal layout |
| Horizontal overflow | **None** expected — `wf-container` inner |
| Footer order | FOOTER after MAIN — unchanged |

---

## 17. Coverage Boundary

| Metric | Effect |
|--------|--------|
| **RSC** | **None** — utility scaffold without registered page_type |
| **RPC** | **None** — CART partial already at W6-B1 |
| **PC** | **None** — ECOMMERCE PC accrual is G4-only |
| **SC** | **Staging evidence input** — not formal SC PASS |

---

## 18. Evidence Paths

| Artefact | Path |
|----------|------|
| Source scaffold | `workspaces/website-factory-reference-v1/src/pages/cart-utility-reference.html` |
| Dist output | `workspaces/website-factory-reference-v1/dist/cart-utility-reference.html` |
| Page SCSS | `workspaces/website-factory-reference-v1/src/scss/pages/_cart-utility-reference.scss` |
| Manifest | `workspaces/website-factory-reference-v1/page-architecture/CART-UTILITY-SCAFFOLD-MANIFEST-v1.md` |
| W6-D report | `reports/wf-r01-3-5-w6-d-commerce-utility-scaffolds-v1.md` |

---

## 19. Decision

**CART utility reference composition v1 — PUBLISHED.**

Approved sequence locked for W6-D. Feeds G3 ECOMMERCE staging scaffold evidence. **Not** CART_PAGE registration. **Not** RSC accrual. **Not** ECOMMERCE PC evidence. **Not** G3 PASS.
