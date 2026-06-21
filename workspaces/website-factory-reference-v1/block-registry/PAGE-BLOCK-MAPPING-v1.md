# Website Factory — Page Block Mapping v1

**Версия:** v1.1 *(WF-R01.2 Gate 2 — structural stances additive)*  
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
- Global `HEADER_NAV` REQUIRED on multi-page marketing types; OPTIONAL minimal on `LANDING_PAGE`.
- Structural blocks `HEADER_NAV`, `FILTERS`, `SEARCH` — WF-R01.2 Tier A; matrix: [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md).
- ECOMMERCE utility routes (`/cart/`, `/checkout/`) use page roles documented in Blueprint — not separate page_type in v1 minimum registry.
- `block_id` keys — authoritative from BLOCK-REGISTRY-v1.

---

## Summary matrix

| block_id | HOME | LANDING | SERVICE | CATEGORY | PRODUCT | ABOUT | CONTACT | FAQ | REVIEWS | LEGAL |
|----------|------|---------|---------|----------|---------|-------|---------|-----|---------|-------|
| HEADER_NAV | REQ | OPT¶ | REQ | REQ | REQ | REQ | REQ | REQ | REQ | REQ |
| FILTERS | OPT‖ | FORB | FORB | REQ | FORB | FORB | FORB | FORB | FORB | FORB |
| SEARCH | OPT | FORB | OPT | OPT | OPT | OPT | OPT | OPT | OPT | FORB |
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
¶ `HEADER_NAV` on `LANDING_PAGE`: OPTIONAL minimal shell — not catalog chrome.  
‖ `FILTERS` on `HOME_PAGE`: OPTIONAL when catalog hub exposes filterable grid (CATALOG/ECOMMERCE).  
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
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL (CATALOG, ECOMMERCE) | Discovery entry |
| FILTERS | OPTIONAL (CATALOG, ECOMMERCE) | When filterable grid on home |

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
| HEADER_NAV | OPTIONAL | Minimal shell — structural absence intentional on pure LANDING |
| FILTERS, SEARCH | FORBIDDEN | → CATALOG |
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
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL | Discovery |
| FILTERS | FORBIDDEN | Catalog-only |
| PRODUCT_GRID, CATEGORIES, CART, CHECKOUT | FORBIDDEN | Catalog/commerce |

---

## CATEGORY_PAGE

**Allowed site types:** CATALOG, ECOMMERCE, CORPORATE (subtree)

| block_id | Stance | Notes |
|----------|--------|-------|
| HERO | REQUIRED | Category intro (compact allowed) |
| PRODUCT_GRID | REQUIRED | PLP grid |
| FILTERS | REQUIRED | PLP refinement controls |
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL | PLP context |
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
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL | Discovery |
| FILTERS | FORBIDDEN | PLP-only — not on PDP |
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
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL | |
| FILTERS | FORBIDDEN | |
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
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL | |
| FILTERS | FORBIDDEN | |
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
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL | |
| FILTERS | FORBIDDEN | |
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
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | OPTIONAL | |
| FILTERS | FORBIDDEN | |
| FOOTER, LEGAL_LINKS | REQUIRED | |
| CASES, CTA | OPTIONAL | |
| LEAD_FORM | OPTIONAL | Secondary |

---

## LEGAL_PAGE

**Allowed site types:** All Core (production)

| block_id | Stance | Notes |
|----------|--------|-------|
| All marketing blocks (HERO, LEAD_FORM, CTA, …) | FORBIDDEN | Semantic legal body only |
| HEADER_NAV | REQUIRED | Global shell on legal routes |
| FILTERS, SEARCH | FORBIDDEN | |
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

## SEARCH_RESULTS_PAGE

**Allowed site types:** CATALOG, ECOMMERCE, CORPORATE (catalog subtree)

**Registry status:** **REGISTERED / UNSCAFFOLDED** (G2-R3 A1). Authority: [wf-r01-3-g2-r3-a1-search-results-registry-matrix-expansion-v1.md](../../../projects/mars-website-factory/wf-r01-3-g2-r3-a1-search-results-registry-matrix-expansion-v1.md).

| block_id / region | Stance | Notes |
|-------------------|--------|-------|
| HEADER_NAV | REQUIRED | Global shell |
| SEARCH | REQUIRED | Results-host query entry |
| PRODUCT_GRID | REQUIRED | Results listing surface |
| PRODUCT_CARD | REQUIRED | Implicit via PRODUCT_GRID composition |
| PAGINATION | REQUIRED | List surface paging (Tier B layout-component) |
| BREADCRUMBS | OPTIONAL | Query-aware shallow trail — POL |
| FILTERS | OPTIONAL | Refinement on results |
| FOOTER | REQUIRED | Global shell |
| LEGAL_LINKS | REQUIRED | Nested in FOOTER |
| Query identity region | SCAFFOLD-OWNED | Static fictional query — **no** `block_id` — A2/A3 authority |
| Result count / summary | SCAFFOLD-OWNED | Static count copy — **no** `block_id` |
| Sort controls | SCAFFOLD-OWNED | Presentation-only — **no** `block_id` |
| Empty / no-results state | SCAFFOLD-OWNED | Zero-hit variation — **no** `block_id` — A2 authority gap |
| HERO | FORBIDDEN | Not a marketing landing surface |
| LEAD_FORM as primary | FORBIDDEN | Not primary conversion on results host |

Route `/search/` documented in CATALOG Blueprint — now bound to registered `page_type`.

**Supersedes:** prior `SEARCH_RESULTS (planned — glossary)` section.

---

## SAFE UNKNOWN

- Automated page ↔ block validator — **not implemented**
- Thank-you page block mapping — **FUTURE** (`THANK_YOU_PAGE` not in v1 registry)

---

*Page Block Mapping version: v1.1 (WF-R01.2 Gate 2 structural slice). Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
