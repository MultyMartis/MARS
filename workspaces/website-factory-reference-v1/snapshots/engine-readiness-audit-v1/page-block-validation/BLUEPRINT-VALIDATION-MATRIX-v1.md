# Website Factory — Blueprint Validation Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** Blueprint-level validation critical points — **documentation only**  
**Authority:** [BLUEPRINT-BLOCK-MAPPING-v1.md](../block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md), [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md)

**Scope:** Core Blueprints — `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

---

## Summary

| Blueprint | site_type_code | Required pages (production) | Site-wide REQUIRED blocks | Top failure mode |
|-----------|----------------|----------------------------|---------------------------|------------------|
| LANDING | `LANDING` | `LANDING_PAGE` | HERO, BENEFITS, PROCESS, TRUST, FAQ, LEAD_FORM, CTA, CONTACTS, FOOTER, LEGAL_LINKS | Commerce drift |
| PROMO | `PROMO` | HOME, SERVICE, ABOUT, CONTACT, LEGAL | HERO, SERVICES, ABOUT, CONTACTS, FOOTER, LEGAL_LINKS | Missing money pages |
| CATALOG | `CATALOG` | HOME, CATEGORY, PRODUCT, CONTACT, LEGAL | CATEGORIES, PRODUCT_GRID, PRODUCT_CARD, CONTACTS, FOOTER, LEGAL_LINKS | Cart/checkout leak |
| ECOMMERCE | `ECOMMERCE` | HOME, CATEGORY, PRODUCT, CONTACT, LEGAL + cart/checkout routes | CATEGORIES, PRODUCT_GRID, PRODUCT_CARD, CART, CHECKOUT, PAYMENT, … | RFQ-as-primary |
| CORPORATE | `CORPORATE` | HOME, ABOUT, CONTACT, LEGAL | HERO, SERVICES, ABOUT, TRUST, CONTACTS, FOOTER, LEGAL_LINKS | Subtree undocumented |

---

## LANDING Blueprint

**Blueprint ref:** [LANDING-BLUEPRINT-v1.md](../blueprints/LANDING-BLUEPRINT-v1.md)  
**site_type_code:** `LANDING`

### Required pages

| page_type | Mark | Validation |
|-----------|------|------------|
| `LANDING_PAGE` | REQUIRED | Must exist at `/` |
| `HOME_PAGE` | FORBIDDEN | CRITICAL if present |
| `LEGAL_PAGE` | OPTIONAL³ | 4 URLs when production |
| Catalog/commerce pages | FORBIDDEN | CRITICAL |

### Required blocks (site-wide / primary page)

`HERO` · `BENEFITS` · `PROCESS` · `TRUST` · `FAQ` · `LEAD_FORM` · `CTA` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS`

### Critical validation points

1. Single conversion surface — one primary `LANDING_PAGE`
2. No multi-page IA (`HOME_PAGE`, `SERVICE_PAGE`)
3. No catalog/commerce blocks site-wide
4. `LEAD_FORM` + `CTA` both present on primary page
5. Legal Pack: `LEGAL_LINKS` on primary page footer

### Common failure scenarios

| Failure | Cause | Severity |
|---------|-------|----------|
| LANDING without HERO | Incomplete funnel | CRITICAL |
| LANDING without LEAD_FORM | No primary conversion | ERROR |
| LANDING with CART | Blueprint misclassification | CRITICAL |
| HOME_PAGE on LANDING site | Multi-page drift | CRITICAL |
| Missing LEGAL_LINKS | Legal Pack gate | ERROR |

---

## PROMO Blueprint

**Blueprint ref:** [PROMO-BLUEPRINT-v1.md](../blueprints/PROMO-BLUEPRINT-v1.md)  
**site_type_code:** `PROMO`

### Required pages

| page_type | Mark |
|-----------|------|
| `HOME_PAGE` | REQUIRED |
| `SERVICE_PAGE` | REQUIRED (≥1) |
| `ABOUT_PAGE` | REQUIRED |
| `CONTACT_PAGE` | REQUIRED |
| `LEGAL_PAGE` | REQUIRED³ |
| `LANDING_PAGE` | OPTIONAL (campaigns) |

### Required blocks (site-wide minimum)

`HERO` · `SERVICES` · `ABOUT` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS`

### Critical validation points

1. Every REQUIRED page type has page contract + block stack
2. `SERVICE_PAGE` stacks include `LEAD_FORM`
3. No catalog/commerce blocks site-wide
4. No site-wide sticky PPC CTA (LANDING pattern)

### Common failure scenarios

| Failure | Cause | Severity |
|---------|-------|----------|
| Missing SERVICE_PAGE | Incomplete PROMO IA | CRITICAL |
| SERVICE_PAGE without LEAD_FORM | Money page gap | ERROR |
| PRODUCT_GRID anywhere | Catalog drift | CRITICAL |
| Missing ABOUT_PAGE | Trust gap | ERROR |

---

## CATALOG Blueprint

**Blueprint ref:** [CATALOG-BLUEPRINT-v1.md](../blueprints/CATALOG-BLUEPRINT-v1.md)  
**site_type_code:** `CATALOG`

### Required pages

| page_type | Mark |
|-----------|------|
| `HOME_PAGE` | REQUIRED |
| `CATEGORY_PAGE` | REQUIRED (≥1) |
| `PRODUCT_PAGE` | REQUIRED (≥1) |
| `CONTACT_PAGE` | REQUIRED |
| `LEGAL_PAGE` | REQUIRED³ |
| Cart/checkout routes | FORBIDDEN |

### Required blocks (site-wide minimum)

`CATEGORIES` · `PRODUCT_GRID` · `PRODUCT_CARD` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS`

### Critical validation points

1. PLP (`CATEGORY_PAGE`) has `PRODUCT_GRID` — no `CART`
2. PDP (`PRODUCT_PAGE`) has `PRODUCT_CARD` + `CTA` (RFQ/contact)
3. No `CART`, `CHECKOUT`, `PAYMENT` anywhere
4. No LANDING-style sticky CTA site-wide

### Common failure scenarios

| Failure | Cause | Severity |
|---------|-------|----------|
| CATALOG with CART | Misclassified ECOMMERCE | CRITICAL |
| CATEGORY_PAGE with CHECKOUT | Commerce on PLP | CRITICAL |
| Missing PRODUCT_GRID on PLP | Broken catalog | CRITICAL |
| LEAD_FORM as ECOMMERCE-primary on PDP | Wrong conversion model | ERROR |

---

## ECOMMERCE Blueprint

**Blueprint ref:** [ECOMMERCE-BLUEPRINT-v1.md](../blueprints/ECOMMERCE-BLUEPRINT-v1.md)  
**site_type_code:** `ECOMMERCE`

### Required pages

| page_type | Mark |
|-----------|------|
| `HOME_PAGE` | REQUIRED |
| `CATEGORY_PAGE` | REQUIRED |
| `PRODUCT_PAGE` | REQUIRED |
| `CONTACT_PAGE` | REQUIRED |
| `LEGAL_PAGE` | REQUIRED³ |
| `/cart/`, `/checkout/` utility | REQUIRED (Blueprint) |

### Required blocks (site-wide minimum)

`CATEGORIES` · `PRODUCT_GRID` · `PRODUCT_CARD` · `CART` · `CHECKOUT` · `PAYMENT` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS`

### Critical validation points

1. Transaction path: PDP → cart route → checkout route
2. `PAYMENT` on checkout only
3. `LEAD_FORM` **not** primary conversion site-wide
4. `REVIEWS` on PDP when reviews feature enabled

### Common failure scenarios

| Failure | Cause | Severity |
|---------|-------|----------|
| ECOMMERCE without CHECKOUT route | Incomplete transaction | CRITICAL |
| LEAD_FORM primary on PDP | CATALOG conversion model | ERROR |
| CHECKOUT on CATEGORY_PAGE | Block placement error | CRITICAL |
| Missing PAYMENT on checkout | Transaction incomplete | CRITICAL |

---

## CORPORATE Blueprint

**Blueprint ref:** [CORPORATE-BLUEPRINT-v1.md](../blueprints/CORPORATE-BLUEPRINT-v1.md)  
**site_type_code:** `CORPORATE`

### Required pages

| page_type | Mark |
|-----------|------|
| `HOME_PAGE` | REQUIRED |
| `ABOUT_PAGE` | REQUIRED |
| `CONTACT_PAGE` | REQUIRED |
| `LEGAL_PAGE` | REQUIRED³ |
| `SERVICE_PAGE` | OPTIONAL |
| `CATEGORY_PAGE`, `PRODUCT_PAGE` | OPTIONAL (subtree only) |

### Required blocks (site-wide minimum)

`HERO` · `SERVICES` · `ABOUT` · `TRUST` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS`

### Critical validation points

1. Subtree routes documented with inherited CATALOG or ECOMMERCE block rules
2. No site-wide LANDING sticky CTA pattern
3. Enterprise trust stack on HOME and ABOUT

### Common failure scenarios

| Failure | Cause | Severity |
|---------|-------|----------|
| Catalog subtree without CATEGORY_PAGE | Undocumented IA | ERROR |
| CART on corporate marketing pages | Subtree bleed | CRITICAL |
| Missing TRUST on HOME | Enterprise trust gap | WARNING |
| Subtree uses CATALOG rules but site_type still CORPORATE only | Validation ambiguity | WARNING — document route groups |

---

## Blueprint × page validation order

```
1. Validate site_type_code + Blueprint selection
2. Validate required pages exist (SITE-TYPE-PAGE-MATRIX)
3. Per page: PAGE-TYPE-VALIDATION-MATRIX
4. Site-wide: BLUEPRINT-BLOCK-MAPPING FORBIDDEN sweep
5. LEGAL cross-route: LEGAL_LINKS on marketing pages
```

---

## SAFE UNKNOWN

- Automated Blueprint validator — **FUTURE**
- Extended Type blueprints — **out of scope**

---

*Blueprint Validation Matrix version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
