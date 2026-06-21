# ECOMMERCE Reference Blueprint-Instance v1

**Site type:** `ECOMMERCE`  
**Reference workspace:** `workspaces/website-factory-reference-v1/`  
**Version:** v1  
**Date:** 2026-06-21  
**Status:** **PUBLISHED · STAGING EVIDENCE · NOT PRODUCTION COMMERCE**  
**Authority:** [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](../../../projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) §17 · [wf-r01-3-5-w6-d-commerce-utility-scaffolds-v1.md](../../../reports/wf-r01-3-5-w6-d-commerce-utility-scaffolds-v1.md) · [wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md](../../../projects/mars-website-factory/wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md)

**Honesty boundary:** ECOMMERCE **staging** reference slice documentation only. **Not** production checkout. **Not** payment gateway. **Not** SC PASS. **Not** PC accrual. **Not** RSC accrual for utility routes.

---

## 1. Identity

| Field | Value |
|-------|-------|
| **Artefact class** | Reference Blueprint-instance (SC component — staging HITL) |
| **site_type_code** | `ECOMMERCE` (Core 5 — existing) |
| **Slice name** | ECOMMERCE G3 staging reference chain |
| **Publication wave** | WF-R01.3.5 W7-CD (combines charter W7-D intent) |

---

## 2. Staging Chain

```text
CATALOG inheritance (CATEGORY_PAGE · PRODUCT_PAGE · SEARCH_RESULTS_PAGE)
    ↓
PRODUCT_PAGE context (PDP · fictional ATC path)
    ↓
CART utility scaffold (/cart/ reference route)
    ↓
CHECKOUT utility scaffold (/checkout/ reference route)
    └── PAYMENT integration (checkout region)
```

**DELIVERY:** not implemented — **G4-only** at G3 minimum (charter §26 · W6-G3R §22).

---

## 3. Page and Scaffold Surfaces

| Surface | Classification | Source | Composition | Manifest | Registered page_type |
|---------|----------------|--------|-------------|----------|----------------------|
| `CATEGORY_PAGE` | Registered scaffold | `category-page-reference.html` | [CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md](CATEGORY-PAGE-REFERENCE-COMPOSITION-v1.md) | CATEGORY manifest | **Yes** |
| `PRODUCT_PAGE` | Registered scaffold | `product-page-reference.html` | [PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md](PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md) | PRODUCT manifest | **Yes** |
| `SEARCH_RESULTS_PAGE` | Registered scaffold | `search-results-page-reference.html` | [SEARCH-RESULTS-PAGE-REFERENCE-COMPOSITION-v1.md](SEARCH-RESULTS-PAGE-REFERENCE-COMPOSITION-v1.md) | SEARCH manifest | **Yes** |
| `/cart/` utility | Utility scaffold | `cart-utility-reference.html` | [CART-UTILITY-REFERENCE-COMPOSITION-v1.md](CART-UTILITY-REFERENCE-COMPOSITION-v1.md) | [CART-UTILITY-SCAFFOLD-MANIFEST-v1.md](CART-UTILITY-SCAFFOLD-MANIFEST-v1.md) | **None** |
| `/checkout/` utility | Utility scaffold | `checkout-utility-reference.html` | [CHECKOUT-UTILITY-REFERENCE-COMPOSITION-v1.md](CHECKOUT-UTILITY-REFERENCE-COMPOSITION-v1.md) | [CHECKOUT-UTILITY-SCAFFOLD-MANIFEST-v1.md](CHECKOUT-UTILITY-SCAFFOLD-MANIFEST-v1.md) | **None** |

**Catalog inheritance:** CATALOG slice scaffolds provide PLP/PDP/search context; site-type primary on compositions is `CATALOG` — **reused for ECOMMERCE staging** per charter §17 and hybrid matrix rules.

---

## 4. Commerce Block Evidence

| block_id | Partial | Host / surface | Maturity | RPC | G3 role |
|----------|---------|----------------|----------|-----|---------|
| CART | `components/cart.html` | Utility scaffold + bounded host | PARTIAL / T1+ | **+1 earned** | **Present** |
| CHECKOUT | `components/checkout.html` | Utility scaffold + bounded host | PARTIAL / T1+ | **+1 earned** | **Present** |
| PAYMENT | `components/payment.html` | Checkout utility + bounded host | PARTIAL / T1+ | **+1 earned** | **Present** |
| DELIVERY | — | — | Not implemented | Gap #4 | **G4-only** at G3 |
| PRODUCT_GRID / PRODUCT_CARD | Catalog partials | CATEGORY · PRODUCT · SEARCH | Implemented | Prior waves | Catalog context |

---

## 5. Coverage Boundaries

| Dimension | Staging slice effect |
|-----------|---------------------|
| RC | **No change** — 32/32 |
| RPC | **No change** — 29/32 (blocks earned at W6-B; scaffolds +0) |
| RSC | **No change** — 7/11; utility routes **do not accrue** without page-type addendum |
| SC | **Staging evidence input** — ECOMMERCE SC **NOT PASS** |
| PC | **Not accrued** — `PRODUCT_PAGE → CART → CHECKOUT` corridor **G4-only** for accrual |

---

## 6. Runtime Boundary

Static cart example · static checkout structure · fictional products/prices/payment methods · presentation-only controls · no network requests · no order creation · no payment gateway · no production URLs.

---

## 7. Dist Outputs (build PASS at W6-D)

| Surface | Dist path |
|---------|-----------|
| CART utility | `dist/cart-utility-reference.html` |
| CHECKOUT utility | `dist/checkout-utility-reference.html` |
| PRODUCT_PAGE | `dist/product-page-reference.html` |
| CATEGORY_PAGE | `dist/category-page-reference.html` |
| SEARCH_RESULTS_PAGE | `dist/search-results-page-reference.html` |

**Reference workspace HTML surface count:** **18** (post W6-D).

---

## 8. SC Staging Checklist (evaluation input — not PASS)

| Check | State |
|-------|-------|
| Catalog → PDP context exists | **SATISFIED** — inherited scaffolds |
| CART utility global-shell scaffold | **SATISFIED** — W6-D VALIDATED |
| CHECKOUT utility global-shell scaffold | **SATISFIED** — W6-D VALIDATED |
| PAYMENT on checkout surface | **SATISFIED** — W6-B3 + W6-D |
| DELIVERY region | **OPEN** — G4 deferred |
| Production commerce runtime | **ABSENT** — by design |
| Formal SC PASS | **NOT GRANTED** — G3-F only |

---

## 9. G4 Deferred Work

- `DELIVERY` partial + checkout integration (W6-C)
- ECOMMERCE PC corridor accrual (`PRODUCT_PAGE → CART → CHECKOUT`) — W6-I addendum
- Optional `CART_PAGE` / `CHECKOUT_PAGE` registry (W6-E addendum)
- ECOMMERCE legal E1–E4 — WF-R01.7 / future
- Full Core 5 blueprint-instance completion (G4-E)

---

## 10. Evidence Paths

```text
reports/wf-r01-3-5-w6-b1-cart-reference-block-v1.md
reports/wf-r01-3-5-w6-b2-checkout-reference-block-v1.md
reports/wf-r01-3-5-w6-b3-payment-reference-block-v1.md
reports/wf-r01-3-5-w6-d-commerce-utility-scaffolds-v1.md
projects/mars-website-factory/wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md
```

---

*ECOMMERCE Reference Blueprint-instance v1 — staging evidence only. Not production commerce.*
