# Website Factory — Page Content Contracts v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** authoritative `page_type` content profiles — **architecture only**  
**Связь:** [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md), [PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md), [BLOCK-CONTENT-CONTRACTS-v1.md](BLOCK-CONTENT-CONTRACTS-v1.md)

**Не является:** page copy, meta tags, URL slugs, sitemap content.

---

## Легенда

| Column | Meaning |
|--------|---------|
| **primary content role** | Dominant semantic job of the page |
| **conversion_role** | Page-level conversion stance (`PAGE_MIXED` = stack-derived) |
| **required / optional / forbidden** | Page-level signals **in addition to** block contracts |

Block-level signals still apply per REQUIRED `block_id` on the page stack.

---

## HOME_PAGE — `CC_PAGE_HOME_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Hub — orient visitor to money routes and entity credibility |
| **conversion_role** | PAGE_MIXED (secondary CTA; hub not sole primary funnel) |
| **required** | `offer` (site-level), `entity_identity`, `service_scope` (navigation scope), `cta` |
| **optional** | `benefit`, `proof`, `trust`, `review`, `case`, `location`, `contact` |
| **forbidden** | `consent` (unless form block present), `payment`, `process` (full checkout), `legal_disclosure` (body), `urgency` (site-wide false scarcity) |

---

## LANDING_PAGE — `CC_PAGE_LANDING_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Single-surface conversion narrative |
| **conversion_role** | PRIMARY_CONVERSION |
| **required** | `offer`, `benefit`, `proof`, `objection`, `cta`, `contact`, `consent` (when form) |
| **optional** | `process`, `price`, `guarantee`, `faq`, `urgency` (documented only) |
| **forbidden** | `service_scope` (catalog hub), `comparison` (PLP), `payment`, `delivery` (ecommerce), `review` (fabricated UGC), `legal_disclosure` (marketing body) |

---

## SERVICE_PAGE — `CC_PAGE_SERVICE_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Money page — service-specific conversion |
| **conversion_role** | PRIMARY_CONVERSION |
| **required** | `offer`, `service_scope`, `benefit`, `proof`, `objection`, `cta` |
| **optional** | `process`, `case`, `price`, `faq`, `contact`, `guarantee` |
| **forbidden** | `payment`, `delivery` (ecommerce), `comparison` (without service comparables), `urgency` (undocumented), `entity_identity` (duplicate footer-only) |

---

## CATEGORY_PAGE — `CC_PAGE_CATEGORY_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Catalog browse — taxonomy and discovery |
| **conversion_role** | INFORMATIONAL (micro-CTA to PDP) |
| **required** | `service_scope` |
| **optional** | `benefit` (category intro), `proof`, `cta`, `price` (if listed model) |
| **forbidden** | `offer` (campaign hero), `process`, `objection` (page-level), `consent`, `payment`, `urgency`, `review` (hub substitute) |

---

## PRODUCT_PAGE — `CC_PAGE_PRODUCT_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | PDP — unit decision and conversion path |
| **conversion_role** | PAGE_MIXED (RFQ primary on CATALOG; ATC on ECOMMERCE) |
| **required** | `offer`, `benefit`, `cta` |
| **optional** | `price`, `availability`, `proof`, `review`, `guarantee`, `delivery`, `comparison`, `objection`, `contact` |
| **forbidden** | `brand_narrative` (full about), `urgency` (undocumented), `legal_disclosure` (body), `entity_identity` (primary above fold) |

---

## ABOUT_PAGE — `CC_PAGE_ABOUT_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Entity trust — identity without direct commerce |
| **conversion_role** | TRUST_SUPPORT |
| **required** | `brand_narrative`, `entity_identity`, `experience` |
| **optional** | `proof`, `case`, `certificate`, `cta` (soft), `contact` |
| **forbidden** | `price`, `payment`, `offer` (primary), `urgency`, `comparison`, `consent` (no form), `review` (as commerce substitute) |

---

## CONTACT_PAGE — `CC_PAGE_CONTACT_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Reachability utility |
| **conversion_role** | SECONDARY_CONVERSION |
| **required** | `contact`, `location`, `entity_identity` |
| **optional** | `cta`, `service_scope`, `consent` (if form) |
| **forbidden** | `offer`, `benefit`, `proof` (campaign), `price`, `urgency`, `review`, `comparison` |

---

## FAQ_PAGE — `CC_PAGE_FAQ_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Centralized support / objection hub |
| **conversion_role** | INFORMATIONAL |
| **required** | `faq`, `question`, `answer`, `objection` |
| **optional** | `cta`, `contact`, `guarantee`, `delivery`, `process` |
| **forbidden** | `offer` (hero substitute), `price` (unless FAQ topic), `urgency`, `review`, `payment`, `legal_disclosure` (body) |

---

## REVIEWS_PAGE — `CC_PAGE_REVIEWS_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Aggregated social proof hub |
| **conversion_role** | TRUST_SUPPORT |
| **required** | `review`, `proof`, `trust` |
| **optional** | `case`, `cta`, `entity_identity` |
| **forbidden** | `offer`, `price`, `urgency`, `comparison`, `payment`, `legal_disclosure` (body), fabricated `review` |

---

## LEGAL_PAGE — `CC_PAGE_LEGAL_PAGE`

| Dimension | Value |
|-----------|-------|
| **primary content role** | Compliance document surface |
| **conversion_role** | LEGAL |
| **required** | `legal_disclosure`, `entity_identity` |
| **optional** | `contact` (controller reference) |
| **forbidden** | `offer`, `benefit`, `cta` (primary marketing), `proof`, `trust` (marketing band), `review`, `case`, `price`, `urgency`, `comparison`, `objection` (sales), `payment` (marketing) |

**Binding:** [LEGAL-PAGE-CONTRACT-v1.md](../page-architecture/LEGAL-PAGE-CONTRACT-v1.md) + Legal Pack v1 (FROZEN).

---

## Page type summary matrix

| page_type | Primary role | conversion_role |
|-----------|--------------|-----------------|
| HOME_PAGE | Hub | PAGE_MIXED |
| LANDING_PAGE | Conversion narrative | PRIMARY_CONVERSION |
| SERVICE_PAGE | Money page | PRIMARY_CONVERSION |
| CATEGORY_PAGE | Catalog browse | INFORMATIONAL |
| PRODUCT_PAGE | PDP | PAGE_MIXED |
| ABOUT_PAGE | Entity trust | TRUST_SUPPORT |
| CONTACT_PAGE | Reachability | SECONDARY_CONVERSION |
| FAQ_PAGE | Support hub | INFORMATIONAL |
| REVIEWS_PAGE | Social proof hub | TRUST_SUPPORT |
| LEGAL_PAGE | Compliance | LEGAL |

**Count:** 10 — matches PAGE-TYPE-REGISTRY-v1.

---

## SAFE UNKNOWN

- CART_PAGE / CHECKOUT_PAGE (ECOMMERCE extensions) — page profiles **FUTURE** — use block contracts on utility routes until chartered.

---

*Page Content Contracts version: v1.*
