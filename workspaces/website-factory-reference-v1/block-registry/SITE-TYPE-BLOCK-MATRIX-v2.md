# Website Factory — Site Type Block Matrix v2

**Версия:** v2.1 *(WF-R01.2 Gate 2 — structural rows additive)*  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** authoritative REQUIRED / OPTIONAL / FORBIDDEN matrix for Core site types  
**Связь:** [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [../registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md), [../blueprints/](../blueprints/)

**Scope:** **Core Types only** — `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`.

**Extended Types** (`SAAS`, `WEB_APPLICATION`, `MARKETPLACE`) — **out of scope** for this matrix.

**Легенда:**

| Code | Meaning |
|------|---------|
| **REQUIRED** | Must appear per Blueprint on specified pages |
| **OPTIONAL** | Allowed from Blueprint allow-list; document in project IA |
| **FORBIDDEN** | Incompatible — triggers reclassification review |

**Notes:**

- Page-level placement — per Blueprint `required_blocks` / `optional_blocks`.
- CORPORATE **subtrees** inherit CATALOG / ECOMMERCE rows for catalog/ecommerce route groups.
- Production legal — `LEGAL_LINKS` + `FOOTER` REQUIRED when Legal Pack applies.

---

## Summary matrix

| block_id | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|----------|---------|-------|---------|-----------|-----------|
| HERO | REQUIRED | REQUIRED | OPTIONAL | OPTIONAL | REQUIRED |
| BENEFITS | REQUIRED | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL |
| FEATURES | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| SERVICES | FORBIDDEN | REQUIRED | FORBIDDEN | FORBIDDEN | REQUIRED |
| CATEGORIES | FORBIDDEN | FORBIDDEN | REQUIRED | REQUIRED | OPTIONAL |
| CATEGORY_GRID | FORBIDDEN | FORBIDDEN | OPTIONAL | OPTIONAL | OPTIONAL |
| PRODUCT_GRID | FORBIDDEN | FORBIDDEN | REQUIRED | REQUIRED | OPTIONAL |
| PRODUCT_CARD | FORBIDDEN | FORBIDDEN | REQUIRED | REQUIRED | OPTIONAL |
| PRICING | OPTIONAL | OPTIONAL | FORBIDDEN | OPTIONAL | OPTIONAL |
| PROCESS | REQUIRED | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL |
| CASES | OPTIONAL | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL |
| TESTIMONIALS | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| REVIEWS | FORBIDDEN | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| TRUST | REQUIRED | OPTIONAL | OPTIONAL | OPTIONAL | REQUIRED |
| CERTIFICATES | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| TEAM | FORBIDDEN | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL |
| ABOUT | FORBIDDEN | REQUIRED | FORBIDDEN | FORBIDDEN | REQUIRED |
| FAQ | REQUIRED | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| CTA | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL | OPTIONAL |
| LEAD_FORM | REQUIRED | OPTIONAL | OPTIONAL | FORBIDDEN | OPTIONAL |
| CONTACTS | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| MAP | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| PARTNERS | FORBIDDEN | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL |
| DELIVERY | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | OPTIONAL |
| PAYMENT | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL |
| CHECKOUT | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL |
| CART | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL |
| LEGAL_LINKS | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| FOOTER | REQUIRED | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| HEADER_NAV | OPTIONAL* | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| SEARCH | FORBIDDEN | OPTIONAL | REQUIRED | REQUIRED | OPTIONAL |
| FILTERS | FORBIDDEN | FORBIDDEN | REQUIRED | REQUIRED | OPTIONAL† |

\* LANDING: optional **minimal** header chrome — not catalog SEARCH/FILTERS.  
† CORPORATE: optional in **catalog subtree** only — policy-dependent per route group.

---

## LANDING

**Blueprint:** [LANDING-BLUEPRINT-v1.md](../blueprints/LANDING-BLUEPRINT-v1.md)

| block_id | Status | Notes |
|----------|--------|-------|
| HERO | REQUIRED | Primary page `/` |
| BENEFITS | REQUIRED | Value props stack |
| PROCESS | REQUIRED | How it works |
| TRUST | REQUIRED | Social proof |
| FAQ | REQUIRED | Objection handling |
| LEAD_FORM | REQUIRED | Primary conversion |
| CTA | REQUIRED | Band + sticky mobile |
| CONTACTS | REQUIRED | Contact zone |
| FOOTER | REQUIRED | Legal footer shell |
| LEGAL_LINKS | REQUIRED | L1–L4 in production |
| PRICING | OPTIONAL | Tiered offers |
| FEATURES | OPTIONAL | Capability highlights |
| CASES | OPTIONAL | Extended proof |
| TESTIMONIALS | OPTIONAL | Quote variant of trust |
| REVIEWS | **FORBIDDEN** | UGC hub → PROMO/CORPORATE |
| CERTIFICATES | OPTIONAL | Regulated verticals |
| MAP | OPTIONAL | Local business |
| **CART** | **FORBIDDEN** | → ECOMMERCE |
| **CHECKOUT** | **FORBIDDEN** | → ECOMMERCE |
| **PAYMENT** | **FORBIDDEN** | → ECOMMERCE |
| **CATEGORIES** | **FORBIDDEN** | → CATALOG |
| **PRODUCT_GRID** | **FORBIDDEN** | → CATALOG |
| **PRODUCT_CARD** | **FORBIDDEN** | → CATALOG |
| **SERVICES** | **FORBIDDEN** | Multi-page → PROMO |
| **ABOUT** | **FORBIDDEN** | Dedicated about → PROMO |
| **PARTNERS** | **FORBIDDEN** | → CORPORATE |
| **HEADER_NAV** | OPTIONAL | Minimal shell — not catalog chrome |
| **SEARCH** | **FORBIDDEN** | → CATALOG |
| **FILTERS** | **FORBIDDEN** | → CATALOG |

---

## PROMO

**Blueprint:** [PROMO-BLUEPRINT-v1.md](../blueprints/PROMO-BLUEPRINT-v1.md)

| block_id | Status | Notes |
|----------|--------|-------|
| HERO | REQUIRED | Home + service pages |
| SERVICES | REQUIRED | Services index / overview |
| ABOUT | REQUIRED | `/about/` page |
| CONTACTS | REQUIRED | Contacts hub |
| FOOTER | REQUIRED | |
| LEGAL_LINKS | REQUIRED | |
| TRUST | OPTIONAL | Home proof |
| PROCESS | OPTIONAL | Service money pages |
| FAQ | OPTIONAL | Service / contacts |
| CTA | OPTIONAL | Contextual — not site-wide sticky |
| LEAD_FORM | OPTIONAL | Service money pages |
| CASES | OPTIONAL | Portfolio page |
| TEAM | OPTIONAL | About page |
| TESTIMONIALS | OPTIONAL | |
| PRICING | OPTIONAL | Ballpark pricing |
| MAP | OPTIONAL | Local business |
| CERTIFICATES | OPTIONAL | |
| **CART** | **FORBIDDEN** | → ECOMMERCE |
| **CHECKOUT** | **FORBIDDEN** | → ECOMMERCE |
| **PAYMENT** | **FORBIDDEN** | → ECOMMERCE |
| **CATEGORIES** | **FORBIDDEN** | Catalog scale → CATALOG |
| **PRODUCT_GRID** | **FORBIDDEN** | → CATALOG |
| **PRODUCT_CARD** | **FORBIDDEN** | → CATALOG |
| **CTA (sticky site-wide)** | **FORBIDDEN** | LANDING pattern |
| **BENEFITS** | OPTIONAL | Not required — PROMO uses SERVICES narrative |
| **HEADER_NAV** | REQUIRED | Global shell — multi-page IA |
| **SEARCH** | OPTIONAL | Discovery — not catalog-scale |
| **FILTERS** | **FORBIDDEN** | → CATALOG |

---

## CATALOG

**Blueprint:** [CATALOG-BLUEPRINT-v1.md](../blueprints/CATALOG-BLUEPRINT-v1.md)

| block_id | Status | Notes |
|----------|--------|-------|
| CATEGORIES | REQUIRED | Category tree |
| CATEGORY_GRID | OPTIONAL | Visual category tiles on home |
| PRODUCT_GRID | REQUIRED | PLP |
| PRODUCT_CARD | REQUIRED | PLP + PDP |
| CONTACTS | REQUIRED | Support / dealer |
| FOOTER | REQUIRED | |
| LEGAL_LINKS | REQUIRED | |
| TRUST | OPTIONAL | Brand strip |
| FAQ | OPTIONAL | Support |
| LEAD_FORM | OPTIONAL | RFQ on PDP |
| TESTIMONIALS | OPTIONAL | |
| REVIEWS | OPTIONAL | PDP / reviews hub |
| CERTIFICATES | OPTIONAL | Spec-heavy categories |
| MAP | OPTIONAL | Dealer locator |
| HERO | OPTIONAL | Category intro only |
| **CART** | **FORBIDDEN** | **Mandatory** — → ECOMMERCE |
| **CHECKOUT** | **FORBIDDEN** | **Mandatory** — → ECOMMERCE |
| **PAYMENT** | **FORBIDDEN** | → ECOMMERCE |
| **DELIVERY** | **FORBIDDEN** | Commerce policy — ECOMMERCE |
| **LEAD_FORM as primary purchase** | OPTIONAL | RFQ only — not checkout |
| **BENEFITS, PROCESS, SERVICES** | **FORBIDDEN** | Marketing stack → LANDING/PROMO |
| **CTA (PPC sticky)** | **FORBIDDEN** | LANDING pattern |
| **HEADER_NAV** | REQUIRED | Global shell |
| **SEARCH** | REQUIRED | Catalog discovery |
| **FILTERS** | REQUIRED | PLP refinement |

**Operator rule:** cart/checkout on production → **halt** + reclassify ECOMMERCE.

**Page-type host (G2-R3 A1):** `SEARCH_RESULTS_PAGE` is a registered page type (not a site type). CATALOG `SEARCH` · `PRODUCT_GRID` · `FILTERS` block stances apply on the search-results host per [PAGE-BLOCK-MAPPING-v1.md](PAGE-BLOCK-MAPPING-v1.md) § SEARCH_RESULTS_PAGE — **cross-reference only**; site-type matrix rows unchanged.

---

## ECOMMERCE

**Blueprint:** [ECOMMERCE-BLUEPRINT-v1.md](../blueprints/ECOMMERCE-BLUEPRINT-v1.md)

| block_id | Status | Notes |
|----------|--------|-------|
| CATEGORIES | REQUIRED | Shop taxonomy |
| CATEGORY_GRID | OPTIONAL | Shop home category tiles |
| PRODUCT_GRID | REQUIRED | PLP |
| PRODUCT_CARD | REQUIRED | PLP + PDP with ATC |
| CART | REQUIRED | `/cart/` |
| CHECKOUT | REQUIRED | `/checkout/` |
| PAYMENT | REQUIRED | Checkout context |
| CONTACTS | REQUIRED | Support |
| FOOTER | REQUIRED | |
| LEGAL_LINKS | REQUIRED | Checkout + site |
| TRUST | OPTIONAL | PDP badges |
| FAQ | OPTIONAL | |
| DELIVERY | OPTIONAL | Recommended |
| TESTIMONIALS | OPTIONAL | Reviews on PDP |
| REVIEWS | OPTIONAL | Recommended on PDP when UGC enabled |
| PRICING | OPTIONAL | Promos — PDP price primary |
| CTA | OPTIONAL | Promo banners |
| CERTIFICATES | OPTIONAL | |
| MAP | OPTIONAL | Pickup points |
| HERO | OPTIONAL | Shop home |
| **LEAD_FORM as primary conversion** | **FORBIDDEN** | Purchase path primary |
| **BENEFITS, PROCESS** | **FORBIDDEN** | Single-page funnel → LANDING |
| **HEADER_NAV** | REQUIRED | Global shell (+ utility composition in notes) |
| **SEARCH** | REQUIRED | Shop discovery |
| **FILTERS** | REQUIRED | PLP refinement |

---

## CORPORATE

**Blueprint:** [CORPORATE-BLUEPRINT-v1.md](../blueprints/CORPORATE-BLUEPRINT-v1.md)

| block_id | Status | Notes |
|----------|--------|-------|
| HERO | REQUIRED | Corporate home |
| SERVICES | REQUIRED | Solutions hub (or equivalent) |
| ABOUT | REQUIRED | Company narrative |
| TRUST | REQUIRED | Logos / cases on home |
| CONTACTS | REQUIRED | Global contact |
| FOOTER | REQUIRED | |
| LEGAL_LINKS | REQUIRED | |
| PARTNERS | OPTIONAL | Partner area |
| CASES | OPTIONAL | Proof |
| TEAM | OPTIONAL | Leadership |
| FAQ | OPTIONAL | |
| CTA | OPTIONAL | Segment-specific |
| LEAD_FORM | OPTIONAL | Per segment |
| TESTIMONIALS | OPTIONAL | |
| CERTIFICATES | OPTIONAL | |
| MAP | OPTIONAL | Locations |
| PRICING | OPTIONAL | |
| PROCESS | OPTIONAL | Solution pages |
| **CATALOG subtree** | OPTIONAL | Inherit CATALOG matrix |
| **ECOMMERCE subtree** | OPTIONAL | Inherit ECOMMERCE matrix |
| **BENEFITS** | OPTIONAL | Prefer SERVICES/solutions framing |
| **CART / CHECKOUT / PAYMENT** | OPTIONAL | **Only** in ecommerce subtree |
| **CTA (site-wide sticky PPC)** | **FORBIDDEN** | LANDING pattern |
| **HEADER_NAV** | REQUIRED | Mega/primary nav — mega_menu = HEADER_NAV variant |
| **SEARCH** | OPTIONAL | Optional catalog subtree |
| **FILTERS** | OPTIONAL | Catalog subtree only — policy per route group |

**Hybrid rule:** document subtree `site_type_code` per route group; matrix applies **within** subtree.

---

## Migration from SITE-TYPE-BLOCK-MAPPING-v1

| v1 concept | v2 mapping |
|------------|------------|
| Required / Recommended / Optional / Excluded | REQUIRED / OPTIONAL / FORBIDDEN |
| Block roles (hero, social proof) | Canonical `block_id` (HERO, TRUST) |
| Extended type rows | **Removed** — not in v2 |

Update project docs to reference **SITE-TYPE-BLOCK-MATRIX-v2** for compatibility checks.

---

## SAFE UNKNOWN

- Automated matrix validation — **not implemented**
- Waivers for REQUIRED blocks — **HITL only**, not in registry automation

---

*Matrix version: v2.1 (WF-R01.2 Gate 2 structural slice). Supersedes block compatibility detail in SITE-TYPE-BLOCK-MAPPING-v1 for Core types.*
