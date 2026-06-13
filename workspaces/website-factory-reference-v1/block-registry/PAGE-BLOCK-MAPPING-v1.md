# Website Factory — Page Block Mapping v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** authoritative REQUIRED / OPTIONAL / FORBIDDEN per `page_type`  
**Связь:** [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md), [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [CORE-PAGE-ARCHITECTURES-v1.md](../page-architecture/CORE-PAGE-ARCHITECTURES-v1.md)

**Не является:** page composer, block order automation, design layout spec

**Легенда:**

| Code | Meaning |
|------|---------|
| **REQUIRED** | Must appear on this page type when page exists in Blueprint |
| **OPTIONAL** | Allowed from allow-list; document in project IA |
| **FORBIDDEN** | Incompatible on this page type — reclassification or HITL |

**Notes:**

- Global `FOOTER` + `LEGAL_LINKS` REQUIRED on all marketing page types when Legal Pack applies.
- ECOMMERCE utility routes (`/cart/`, `/checkout/`) use page roles documented in Blueprint — not separate page_type in v1 minimum registry.
- `block_id` keys — authoritative from BLOCK-REGISTRY-v1.

---

## Summary matrix

| block_id | HOME | LANDING | SERVICE | CATEGORY | PRODUCT | ABOUT | CONTACT | FAQ | REVIEWS | LEGAL |
|----------|------|---------|---------|----------|---------|-------|---------|-----|---------|-------|
| HERO | REQ | REQ | REQ | REQ | OPT | REQ | OPT | OPT | REQ | FORB |
| BENEFITS | OPT | REQ | OPT | FORB | OPT | OPT | FORB | FORB | FORB | FORB |
| FEATURES | OPT | OPT | OPT | FORB | OPT | FORB | FORB | FORB | FORB | FORB |
| SERVICES | REQ* | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB |
| PROCESS | OPT | REQ | OPT | FORB | FORB | FORB | FORB | FORB | FORB | FORB |
| PRICING | OPT | OPT | OPT | FORB | OPT | FORB | FORB | FORB | FORB | FORB |
| CASES | OPT | OPT | OPT | FORB | FORB | OPT | FORB | FORB | OPT | FORB |
| TRUST | OPT | REQ | OPT | OPT | REQ | OPT | FORB | FORB | OPT | FORB |
| TESTIMONIALS | OPT | OPT | OPT | OPT | OPT | OPT | FORB | FORB | REQ | FORB |
| REVIEWS | OPT | FORB | OPT | FORB | OPT** | FORB | FORB | FORB | REQ | FORB |
| CERTIFICATES | OPT | OPT | OPT | OPT | OPT | OPT | FORB | FORB | FORB | FORB |
| CATEGORIES | REQ† | FORB | FORB | OPT | FORB | FORB | FORB | FORB | FORB | FORB |
| CATEGORY_GRID | OPT | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB |
| PRODUCT_GRID | OPT | FORB | FORB | REQ | FORB | FORB | FORB | FORB | FORB | FORB |
| PRODUCT_CARD | FORB | FORB | FORB | FORB | REQ | FORB | FORB | FORB | FORB | FORB |
| FAQ | OPT | REQ | REQ | OPT | OPT | FORB | FORB | REQ | FORB | FORB |
| CTA | REQ | REQ | REQ | OPT | REQ | OPT | FORB | OPT | OPT | FORB |
| LEAD_FORM | OPT | REQ | REQ | FORB | OPT‡ | FORB | OPT | FORB | FORB | FORB |
| CONTACTS | REQ | REQ | OPT | OPT | OPT | FORB | REQ | FORB | FORB | FORB |
| MAP | OPT | OPT | FORB | OPT | FORB | FORB | OPT | FORB | FORB | FORB |
| TEAM | FORB | FORB | FORB | FORB | FORB | OPT | FORB | FORB | FORB | FORB |
| ABOUT | FORB | FORB | FORB | FORB | FORB | REQ | FORB | FORB | FORB | FORB |
| PARTNERS | OPT | FORB | FORB | FORB | FORB | OPT | FORB | FORB | FORB | FORB |
| DELIVERY | FORB | FORB | FORB | FORB | OPT§ | FORB | FORB | FORB | FORB | FORB |
| PAYMENT | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB |
| CART | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB |
| CHECKOUT | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB | FORB |
| LEGAL_LINKS | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ | FORB |
| FOOTER | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ | FORB |

\* `SERVICES` REQUIRED on PROMO/CORPORATE `HOME_PAGE`; FORBIDDEN on LANDING, CATALOG, ECOMMERCE home.  
† `CATEGORIES` REQUIRED on CATALOG/ECOMMERCE `HOME_PAGE`; OPTIONAL on CORPORATE catalog subtree.  
‡ CATALOG `PRODUCT_PAGE`: RFQ via `LEAD_FORM` OPTIONAL; ECOMMERCE: FORBIDDEN as primary.  
§ `DELIVERY` on ECOMMERCE PDP optional info strip only.  
\*\* `REVIEWS` REQUIRED on ECOMMERCE `PRODUCT_PAGE` when reviews enabled; OPTIONAL on CATALOG PDP.

---

## HOME_PAGE

**Allowed site types:** PROMO, CATALOG, ECOMMERCE, CORPORATE

| block_id | Stance | Notes |
|----------|--------|-------|
| HERO | REQUIRED | Brand / shop entry |
| SERVICES | REQUIRED (PROMO, CORPORATE) | Solutions hub |
| CATEGORIES | REQUIRED (CATALOG, ECOMMERCE) | Taxonomy entry |
| CATEGORY_GRID | OPTIONAL (CATALOG, ECOMMERCE) | Visual category tiles on shop home |
| PRODUCT_GRID | OPTIONAL (CATALOG, ECOMMERCE) | Featured products |
| CTA | REQUIRED (PROMO, CORPORATE) | Segment CTA |
| CONTACTS | REQUIRED | NAP or teaser to CONTACT_PAGE |
| TRUST | OPTIONAL | Home proof strip |
| BENEFITS, PROCESS, FAQ, CASES, PARTNERS | OPTIONAL | Per Blueprint |
| CART, CHECKOUT, PAYMENT | FORBIDDEN | Utility routes only |
| LEAD_FORM | OPTIONAL | Not primary on multi-page home |

---

## LANDING_PAGE

**Allowed site types:** LANDING (required); PROMO, CORPORATE (optional campaign)

| block_id | Stance | Notes |
|----------|--------|-------|
| HERO | REQUIRED | First viewport |
| BENEFITS | REQUIRED | Value props |
| PROCESS | REQUIRED | How it works |
| TRUST or TESTIMONIALS | REQUIRED | Social proof |
| FAQ | REQUIRED | Objection handling |
| LEAD_FORM | REQUIRED | Primary conversion |
| CTA | REQUIRED | Band + sticky mobile variant |
| CONTACTS | REQUIRED | Contact zone |
| FOOTER, LEGAL_LINKS | REQUIRED | Production legal |
| PRICING, FEATURES, CASES, CERTIFICATES, MAP | OPTIONAL | Context-dependent |
| CATEGORIES, PRODUCT_GRID, PRODUCT_CARD, CATEGORY_GRID | FORBIDDEN | → CATALOG |
| SERVICES, ABOUT, TEAM, PARTNERS | FORBIDDEN | Multi-page → PROMO/CORPORATE |
| CART, CHECKOUT, PAYMENT, REVIEWS | FORBIDDEN | Commerce / UGC hub |

---

## SERVICE_PAGE

**Allowed site types:** PROMO, CORPORATE

| block_id | Stance | Notes |
|----------|--------|-------|
| HERO | REQUIRED | Money page header |
| BENEFITS or FEATURES | REQUIRED (one or both) | Scope / capabilities |
| FAQ | REQUIRED | Service objections |
| LEAD_FORM | REQUIRED | Primary conversion |
| CTA | REQUIRED | Contextual action |
| TRUST, CASES, PROCESS | OPTIONAL | Proof stack |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| PRODUCT_GRID, CATEGORIES, CART, CHECKOUT | FORBIDDEN | Catalog/commerce |

---

## CATEGORY_PAGE

**Allowed site types:** CATALOG, ECOMMERCE, CORPORATE (subtree)

| block_id | Stance | Notes |
|----------|--------|-------|
| HERO | REQUIRED | Category intro (compact allowed) |
| PRODUCT_GRID | REQUIRED | PLP grid |
| CTA | OPTIONAL (CATALOG: recommended RFQ/contact) | |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| CATEGORIES | OPTIONAL | Subcategory nav |
| TRUST, FAQ, CERTIFICATES | OPTIONAL | |
| LEAD_FORM | OPTIONAL | RFQ on PLP — document CTA type |
| BENEFITS, PROCESS, SERVICES, LEAD_FORM primary | FORBIDDEN | Marketing funnel blocks |
| CART, CHECKOUT | FORBIDDEN | Not on PLP |

---

## PRODUCT_PAGE

**Allowed site types:** CATALOG, ECOMMERCE, CORPORATE (subtree)

| block_id | Stance | Notes |
|----------|--------|-------|
| PRODUCT_CARD | REQUIRED | PDP layout host |
| TRUST | REQUIRED | Spec / brand credibility |
| CTA | REQUIRED | RFQ / contact / ATC |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| FEATURES, BENEFITS | OPTIONAL | Spec highlights |
| FAQ | OPTIONAL | Product support |
| REVIEWS | OPTIONAL (CATALOG) / REQUIRED (ECOMMERCE when reviews on) | UGC ratings |
| TESTIMONIALS | OPTIONAL | Curated quotes |
| LEAD_FORM | OPTIONAL (CATALOG RFQ) | FORBIDDEN as ECOMMERCE primary |
| DELIVERY | OPTIONAL (ECOMMERCE) | Shipping summary |
| CART, CHECKOUT on PDP body | FORBIDDEN | Mini-cart / ATC within PRODUCT_CARD only |

---

## ABOUT_PAGE

**Allowed site types:** PROMO, CORPORATE

| block_id | Stance | Notes |
|----------|--------|-------|
| HERO | REQUIRED | |
| ABOUT | REQUIRED | Company narrative |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| TEAM, TRUST, CERTIFICATES, CASES, PARTNERS | OPTIONAL | |
| CTA | OPTIONAL | Soft conversion |
| LEAD_FORM as primary | FORBIDDEN | Unless project charter |
| Commerce blocks | FORBIDDEN | |

---

## CONTACT_PAGE

**Allowed site types:** PROMO, CATALOG, ECOMMERCE, CORPORATE

| block_id | Stance | Notes |
|----------|--------|-------|
| CONTACTS | REQUIRED | **requires** Contact Channel / Legal Entity NAP |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| MAP | OPTIONAL | Geo |
| LEAD_FORM | OPTIONAL | Consent Rule applies |
| HERO | OPTIONAL | Compact intro |

---

## FAQ_PAGE

**Allowed site types:** PROMO, CATALOG, ECOMMERCE, CORPORATE

| block_id | Stance | Notes |
|----------|--------|-------|
| FAQ | REQUIRED | Hub content |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| HERO | OPTIONAL | Page intro |
| CTA | OPTIONAL | Support escalation |

---

## REVIEWS_PAGE

**Allowed site types:** PROMO, CORPORATE (optional CATALOG/ECOMMERCE)

| block_id | Stance | Notes |
|----------|--------|-------|
| TESTIMONIALS and/or REVIEWS | REQUIRED | At least one trust block |
| HERO | REQUIRED | Intro |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| CASES, CTA | OPTIONAL | |
| LEAD_FORM | OPTIONAL | Secondary |

---

## LEGAL_PAGE

**Allowed site types:** All Core (production)

| block_id | Stance | Notes |
|----------|--------|-------|
| All marketing blocks (HERO, LEAD_FORM, CTA, …) | FORBIDDEN | Semantic legal body only |
| LEGAL_LINKS in global FOOTER on other routes | REQUIRED elsewhere | Not duplicated as marketing stack on L1–L4 |

Authoritative legal page rules: [LEGAL-PAGE-CONTRACT-v1.md](../page-architecture/LEGAL-PAGE-CONTRACT-v1.md).

---

## ECOMMERCE utility routes (reference)

Not separate page_types in v1 minimum registry; block stance when routes exist:

| Route role | REQUIRED | OPTIONAL | FORBIDDEN |
|------------|----------|----------|-----------|
| `/cart/` | CART, FOOTER, LEGAL_LINKS | CTA | CHECKOUT on same view |
| `/checkout/` | CHECKOUT, PAYMENT, FOOTER, LEGAL_LINKS | DELIVERY | LEAD_FORM as primary |

---

## SAFE UNKNOWN

- Automated page ↔ block validator — **not implemented**
- Thank-you page block mapping — **FUTURE** (`THANK_YOU_PAGE` not in v1 registry)

---

*Page Block Mapping version: v1. Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
