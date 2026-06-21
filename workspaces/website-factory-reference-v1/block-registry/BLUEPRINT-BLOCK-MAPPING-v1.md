# Website Factory — Blueprint Block Mapping v1

**Версия:** v1.1 *(WF-R01.2 Gate 2 — structural stances additive)*  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** authoritative REQUIRED / OPTIONAL / FORBIDDEN per Core Blueprint  
**Связь:** [BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md), [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md)

**Scope:** Core Blueprints only — `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`.

**Легенда:** REQUIRED · OPTIONAL · FORBIDDEN (same as PAGE-BLOCK-MAPPING-v1)

Blueprint-level stance applies **site-wide** across all pages in the Blueprint unless page mapping overrides placement.

---

## Summary matrix

| block_id | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|----------|---------|-------|---------|-----------|-----------|
| HEADER_NAV | OPT* | REQ | REQ | REQ | REQ |
| SEARCH | FORB | OPT | REQ | REQ | OPT |
| FILTERS | FORB | FORB | REQ | REQ | OPT† |
| HERO | REQ | REQ | OPT | OPT | REQ |
| BENEFITS | REQ | OPT | FORB | FORB | OPT |
| FEATURES | OPT | OPT | OPT | OPT | OPT |
| SERVICES | FORB | REQ | FORB | FORB | REQ |
| PROCESS | REQ | OPT | FORB | FORB | OPT |
| PRICING | OPT | OPT | FORB | OPT | OPT |
| CASES | OPT | OPT | FORB | FORB | OPT |
| TRUST | REQ | OPT | OPT | OPT | REQ |
| TESTIMONIALS | OPT | OPT | OPT | OPT | OPT |
| REVIEWS | FORB | OPT | OPT | OPT | OPT |
| CERTIFICATES | OPT | OPT | OPT | OPT | OPT |
| CATEGORIES | FORB | FORB | REQ | REQ | OPT |
| CATEGORY_GRID | FORB | FORB | OPT | OPT | OPT |
| PRODUCT_GRID | FORB | FORB | REQ | REQ | OPT |
| PRODUCT_CARD | FORB | FORB | REQ | REQ | OPT |
| FAQ | REQ | OPT | OPT | OPT | OPT |
| CTA | REQ | OPT | FORB* | OPT | OPT |
| LEAD_FORM | REQ | OPT | OPT | FORB | OPT |
| CONTACTS | REQ | REQ | REQ | REQ | REQ |
| MAP | OPT | OPT | OPT | OPT | OPT |
| TEAM | FORB | OPT | FORB | FORB | OPT |
| ABOUT | FORB | REQ | FORB | FORB | REQ |
| PARTNERS | FORB | FORB | FORB | FORB | OPT |
| DELIVERY | FORB | FORB | FORB | OPT | OPT |
| PAYMENT | FORB | FORB | FORB | REQ | OPT |
| CHECKOUT | FORB | FORB | FORB | REQ | OPT |
| CART | FORB | FORB | FORB | REQ | OPT |
| LEGAL_LINKS | REQ | REQ | REQ | REQ | REQ |
| FOOTER | REQ | REQ | REQ | REQ | REQ |

\* CATALOG: CTA allowed as RFQ/contact on PLP/PDP — not PPC sticky pattern.

\* LANDING: `HEADER_NAV` OPTIONAL minimal — not catalog chrome.  
† CORPORATE: `FILTERS` OPTIONAL catalog subtree only.

---

## LANDING Blueprint

**Blueprint:** [LANDING-BLUEPRINT-v1.md](../blueprints/LANDING-BLUEPRINT-v1.md)  
**site_type_code:** `LANDING`

### REQUIRED

`HERO` · `BENEFITS` · `PROCESS` · `TRUST` · `FAQ` · `LEAD_FORM` · `CTA` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS`

### OPTIONAL

`PRICING` · `FEATURES` · `CASES` · `TESTIMONIALS` · `CERTIFICATES` · `MAP` · `HEADER_NAV` (minimal shell)

### FORBIDDEN

`SERVICES` · `ABOUT` · `TEAM` · `PARTNERS` · `CATEGORIES` · `CATEGORY_GRID` · `PRODUCT_GRID` · `PRODUCT_CARD` · `REVIEWS` · `CART` · `CHECKOUT` · `PAYMENT` · `DELIVERY` · `FILTERS` · `SEARCH`

**Operator rule:** cart or checkout on LANDING production → **halt** + reclassify ECOMMERCE.

---

## PROMO Blueprint

**Blueprint:** [PROMO-BLUEPRINT-v1.md](../blueprints/PROMO-BLUEPRINT-v1.md)  
**site_type_code:** `PROMO`

### REQUIRED

`HERO` · `SERVICES` · `ABOUT` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS` · `HEADER_NAV`

### OPTIONAL

`TRUST` · `PROCESS` · `FAQ` · `CTA` · `LEAD_FORM` · `CASES` · `TEAM` · `TESTIMONIALS` · `REVIEWS` · `PRICING` · `FEATURES` · `MAP` · `CERTIFICATES` · `BENEFITS` · `SEARCH`

### FORBIDDEN

`CATEGORIES` · `CATEGORY_GRID` · `PRODUCT_GRID` · `PRODUCT_CARD` · `CART` · `CHECKOUT` · `PAYMENT` · `DELIVERY` · `FILTERS` · site-wide sticky CTA (LANDING pattern)

---

## CATALOG Blueprint

**Blueprint:** [CATALOG-BLUEPRINT-v1.md](../blueprints/CATALOG-BLUEPRINT-v1.md)  
**site_type_code:** `CATALOG`

### REQUIRED

`CATEGORIES` · `PRODUCT_GRID` · `PRODUCT_CARD` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS` · `HEADER_NAV` · `FILTERS` · `SEARCH`

### OPTIONAL

`HERO` · `CATEGORY_GRID` · `TRUST` · `FAQ` · `LEAD_FORM` · `TESTIMONIALS` · `REVIEWS` · `FEATURES` · `CERTIFICATES` · `MAP` · `CTA` (RFQ/contact)

### FORBIDDEN

`CART` · `CHECKOUT` · `PAYMENT` · `DELIVERY` · `BENEFITS` · `PROCESS` · `SERVICES` · PPC sticky `CTA`

**Operator rule:** add-to-cart or checkout path → **halt** + reclassify ECOMMERCE.

---

## ECOMMERCE Blueprint

**Blueprint:** [ECOMMERCE-BLUEPRINT-v1.md](../blueprints/ECOMMERCE-BLUEPRINT-v1.md)  
**site_type_code:** `ECOMMERCE`

### REQUIRED

`CATEGORIES` · `PRODUCT_GRID` · `PRODUCT_CARD` · `CART` · `CHECKOUT` · `PAYMENT` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS` · `HEADER_NAV` · `FILTERS` · `SEARCH`

### OPTIONAL

`HERO` · `CATEGORY_GRID` · `TRUST` · `FAQ` · `DELIVERY` · `TESTIMONIALS` · `REVIEWS` · `FEATURES` · `PRICING` · `CTA` · `CERTIFICATES` · `MAP`

### FORBIDDEN

`LEAD_FORM` as primary conversion · `BENEFITS` · `PROCESS` · single-page funnel stack

---

## CORPORATE Blueprint

**Blueprint:** [CORPORATE-BLUEPRINT-v1.md](../blueprints/CORPORATE-BLUEPRINT-v1.md)  
**site_type_code:** `CORPORATE`

### REQUIRED

`HERO` · `SERVICES` · `ABOUT` · `TRUST` · `CONTACTS` · `FOOTER` · `LEGAL_LINKS` · `HEADER_NAV`

### OPTIONAL

`PARTNERS` · `CASES` · `TEAM` · `FAQ` · `CTA` · `LEAD_FORM` · `TESTIMONIALS` · `REVIEWS` · `CERTIFICATES` · `MAP` · `PRICING` · `PROCESS` · `FEATURES` · `BENEFITS` · `SEARCH` · `FILTERS` (catalog subtree) · catalog/ecommerce subtree blocks (inherit CATALOG/ECOMMERCE rows)

### FORBIDDEN

Site-wide sticky PPC `CTA` (LANDING pattern)

### Subtree rules

| Subtree | Inherit matrix from |
|---------|---------------------|
| Catalog routes | CATALOG Blueprint block rows |
| Ecommerce routes | ECOMMERCE Blueprint block rows |

Document subtree `site_type_code` per route group in project IA.

---

## Alignment with SITE-TYPE-BLOCK-MATRIX-v2

This document and SITE-TYPE-BLOCK-MATRIX-v2 **must agree** on REQUIRED / OPTIONAL / FORBIDDEN for each `block_id` × Core site type. Discrepancies → fix in same pass + note in BLOCK-REGISTRY-GAPS-v1.

Page-level placement refinements — [PAGE-BLOCK-MAPPING-v1.md](PAGE-BLOCK-MAPPING-v1.md).

---

## SAFE UNKNOWN

- Extended Type blueprints (SAAS, WEB_APPLICATION, MARKETPLACE) — **out of scope**
- Blueprint JSON export — **not defined**

---

*Blueprint Block Mapping version: v1.1 (WF-R01.2 Gate 2 structural slice). Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
