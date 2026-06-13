# Website Factory — Page Type Validation Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** validation rules per canonical `page_type` — **documentation only**  
**Authority:** [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md), [CORE-PAGE-ARCHITECTURES-v1.md](../page-architecture/CORE-PAGE-ARCHITECTURES-v1.md)

**Scope:** 10 page types from [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md)

**Severity legend:** [VALIDATION-SEVERITY-SYSTEM-v1.md](VALIDATION-SEVERITY-SYSTEM-v1.md)

---

## Summary matrix

| page_type | Primary validation focus | Missing HERO | Missing LEAD_FORM | FORBIDDEN commerce |
|-----------|-------------------------|--------------|-------------------|-------------------|
| `HOME_PAGE` | Hub entry blocks | CRITICAL | INFO (optional) | CRITICAL |
| `LANDING_PAGE` | Full funnel stack | CRITICAL | ERROR | CRITICAL |
| `SERVICE_PAGE` | Money page conversion | CRITICAL | ERROR | CRITICAL |
| `CATEGORY_PAGE` | PLP grid | ERROR | INFO | CRITICAL |
| `PRODUCT_PAGE` | PDP + trust | ERROR | WARNING (CATALOG) | CRITICAL |
| `ABOUT_PAGE` | Trust narrative | ERROR | ERROR if primary | CRITICAL |
| `CONTACT_PAGE` | NAP / channels | INFO | INFO | CRITICAL |
| `FAQ_PAGE` | FAQ hub | INFO | INFO | CRITICAL |
| `REVIEWS_PAGE` | Social proof hub | ERROR | INFO | CRITICAL |
| `LEGAL_PAGE` | No marketing stack | N/A (forbidden) | N/A (forbidden) | CRITICAL |

---

## HOME_PAGE

**Allowed site types:** `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

### Required blocks

| block_id | Severity if missing | Notes |
|----------|---------------------|-------|
| `HERO` | CRITICAL | Brand / shop entry |
| `FOOTER` | ERROR | |
| `LEGAL_LINKS` | ERROR | When Legal Pack applies |
| `CONTACTS` | ERROR | NAP or teaser to CONTACT_PAGE |
| `CTA` | ERROR | PROMO, CORPORATE |
| `SERVICES` | ERROR | PROMO, CORPORATE only |
| `CATEGORIES` | ERROR | CATALOG, ECOMMERCE only |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `CART` | CRITICAL |
| `CHECKOUT` | CRITICAL |
| `PAYMENT` | CRITICAL |

### Validation severity

| Condition | Severity |
|-----------|----------|
| Missing `HERO` | CRITICAL |
| Missing `LEGAL_LINKS` | ERROR |
| Missing `FAQ` (optional) | WARNING |
| `CART` on home body | CRITICAL |

---

## LANDING_PAGE

**Allowed site types:** `LANDING` (required); `PROMO`, `CORPORATE` (optional campaign)

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `HERO` | CRITICAL |
| `BENEFITS` | ERROR |
| `PROCESS` | ERROR |
| `TRUST` **or** `TESTIMONIALS` | ERROR (OR-group) |
| `FAQ` | WARNING → ERROR for production LANDING |
| `LEAD_FORM` | ERROR |
| `CTA` | ERROR |
| `CONTACTS` | ERROR |
| `FOOTER` | ERROR |
| `LEGAL_LINKS` | ERROR |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `CART`, `CHECKOUT`, `PAYMENT` | CRITICAL |
| `CATEGORIES`, `PRODUCT_GRID`, `PRODUCT_CARD`, `CATEGORY_GRID` | CRITICAL |
| `SERVICES`, `ABOUT`, `TEAM`, `PARTNERS` | ERROR |
| `REVIEWS` | ERROR |

### Validation severity

| Condition | Severity |
|-----------|----------|
| Missing `HERO` | CRITICAL |
| Missing `LEAD_FORM` | ERROR |
| Missing `FAQ` | WARNING (strict LANDING: treat as ERROR) |
| `CART` present | CRITICAL |

---

## SERVICE_PAGE

**Allowed site types:** `PROMO`, `CORPORATE`

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `HERO` | CRITICAL |
| `BENEFITS` **or** `FEATURES` | ERROR (OR-group) |
| `FAQ` | WARNING |
| `LEAD_FORM` | ERROR |
| `CTA` | ERROR |
| `FOOTER`, `LEGAL_LINKS` | ERROR |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `PRODUCT_GRID`, `CATEGORIES`, `CART`, `CHECKOUT` | CRITICAL |

---

## CATEGORY_PAGE

**Allowed site types:** `CATALOG`, `ECOMMERCE`, `CORPORATE` (subtree)

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `HERO` | ERROR |
| `PRODUCT_GRID` | CRITICAL |
| `FOOTER`, `LEGAL_LINKS` | ERROR |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `CART`, `CHECKOUT` | CRITICAL |
| `BENEFITS`, `PROCESS`, `SERVICES` (primary funnel) | ERROR |

### Validation severity

| Condition | Severity |
|-----------|----------|
| Missing `PRODUCT_GRID` | CRITICAL |
| `CHECKOUT` on PLP | CRITICAL |
| Missing `FAQ` (optional) | INFO |

---

## PRODUCT_PAGE

**Allowed site types:** `CATALOG`, `ECOMMERCE`, `CORPORATE` (subtree)

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `PRODUCT_CARD` | CRITICAL |
| `TRUST` | ERROR |
| `CTA` | ERROR |
| `FOOTER`, `LEGAL_LINKS` | ERROR |
| `REVIEWS` | ERROR (ECOMMERCE when reviews enabled) |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `CART`, `CHECKOUT` on PDP body | CRITICAL |
| `LEAD_FORM` as primary | ERROR (ECOMMERCE) |

---

## ABOUT_PAGE

**Allowed site types:** `PROMO`, `CORPORATE`

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `HERO` | ERROR |
| `ABOUT` | CRITICAL |
| `FOOTER`, `LEGAL_LINKS` | ERROR |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| Commerce blocks (`CART`, `CHECKOUT`, `PRODUCT_GRID`, …) | CRITICAL |
| `LEAD_FORM` as primary | ERROR |

---

## CONTACT_PAGE

**Allowed site types:** `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `CONTACTS` | CRITICAL |
| `FOOTER`, `LEGAL_LINKS` | ERROR |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `CART`, `CHECKOUT` | CRITICAL |

### Validation severity

| Condition | Severity |
|-----------|----------|
| Missing `CONTACTS` | CRITICAL |
| Missing `HERO` (optional) | INFO |
| Missing `MAP` (optional) | INFO |

---

## FAQ_PAGE

**Allowed site types:** `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `FAQ` | CRITICAL |
| `FOOTER`, `LEGAL_LINKS` | ERROR |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `CART`, `CHECKOUT`, `LEAD_FORM` as primary funnel | ERROR / CRITICAL |

### Validation severity

| Condition | Severity |
|-----------|----------|
| Missing `FAQ` | CRITICAL |
| Missing `HERO` (optional) | INFO |

---

## REVIEWS_PAGE

**Allowed site types:** `PROMO`, `CORPORATE` (optional elsewhere)

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| `HERO` | ERROR |
| `TESTIMONIALS` **and/or** `REVIEWS` | ERROR (OR-group) |
| `FOOTER`, `LEGAL_LINKS` | ERROR |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `CART`, `CHECKOUT` | CRITICAL |

---

## LEGAL_PAGE

**Allowed site types:** All Core (production)

### Required blocks

| block_id | Severity if missing |
|----------|---------------------|
| *(none — marketing blocks forbidden on route)* | — |
| Legal document body | CRITICAL (content gate — outside block registry) |

### Forbidden blocks

| block_id | Severity if present |
|----------|---------------------|
| `HERO`, `LEAD_FORM`, `CTA`, `PRICING`, `BENEFITS`, `PRODUCT_GRID`, `CART`, `CHECKOUT` | ERROR |
| `LEGAL_LINKS` as marketing stack duplicate | WARNING |

### Cross-route validation

| Check | Severity |
|-------|----------|
| `LEGAL_LINKS` missing on **non-legal** marketing pages | ERROR |
| Marketing block on `LEGAL_PAGE` body | ERROR |

**Ref:** [LEGAL-PAGE-CONTRACT-v1.md](../page-architecture/LEGAL-PAGE-CONTRACT-v1.md)

---

## ECOMMERCE utility routes (reference)

Not separate `page_type` in v1 registry; when validating `/cart/` or `/checkout/`:

| Route | REQUIRED | FORBIDDEN (severity) |
|-------|----------|----------------------|
| `/cart/` | `CART`, `FOOTER`, `LEGAL_LINKS` | `CHECKOUT` on same view — ERROR |
| `/checkout/` | `CHECKOUT`, `PAYMENT`, `FOOTER`, `LEGAL_LINKS` | `LEAD_FORM` primary — ERROR |

---

## SAFE UNKNOWN

- `THANK_YOU_PAGE` block matrix — **FUTURE**
- Per-block severity overrides in project charter — **HITL only**

---

*Page Type Validation Matrix version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
