# Website Factory — Site Type Content Mapping v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** Core 5 content profiles — **documentation only**  
**Scope:** `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

**Связь:** [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md), [blueprints/](../blueprints/), [SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md), [SITE-TYPE-DESIGN-MAPPING-v1.md](../design-system/SITE-TYPE-DESIGN-MAPPING-v1.md)

**Не является:** tone-of-voice guide, industry copy packs, content calendar.

**Extended types:** SAAS, WEB_APPLICATION, MARKETPLACE — **not expanded** (see [CONTENT-GAPS-v1.md](CONTENT-GAPS-v1.md)).

---

## Легенда

| Term | Meaning |
|------|---------|
| **content priorities** | Ordered semantic goals (signals emphasis) |
| **trust priorities** | Ordered proof/entity obligations |
| **conversion priorities** | Ordered action path goals |
| **forbidden content patterns** | Cross-page signal misuse banned for type |

---

## LANDING

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **content priorities** | 1) `offer` clarity 2) `benefit` + `objection` resolution 3) `proof` before `cta` 4) `process` (if complex offer) 5) `faq` inline |
| **trust priorities** | 1) `proof` / `trust` 2) `certificate` (if regulated) 3) `experience` (verifiable) 4) **no** fabricated `review` |
| **conversion priorities** | 1) Single `cta` path 2) `contact` alternate 3) `consent` on form 4) Sticky `cta` (block-level) |
| **forbidden content patterns** | Catalog `service_scope` as primary IA · `comparison` tables without context · `payment` / `delivery` ecommerce signals · Multi-primary `cta` · `urgency` without source · Placeholder entity/contact · Invented statistics |

**Alignment:** `LANDING_PAGE` only primary conversion surface; SEO MINIMAL depth.

---

## PROMO

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **content priorities** | 1) Per-route `service_scope` on money pages 2) `brand_narrative` on ABOUT 3) `benefit` on SERVICE_PAGE 4) Hub `faq` / `review` without competing primary `offer` on every route |
| **trust priorities** | 1) `case` + `proof` on services 2) `review` / `testimonial` (authentic) 3) `team` / `experience` 4) `entity_identity` sitewide |
| **conversion priorities** | 1) SERVICE_PAGE `cta` / form 2) Contextual `contact` 3) HOME hub secondary `cta` 4) FAQ escalation optional |
| **forbidden content patterns** | Checkout/cart signals on marketing routes · Catalog-primary `service_scope` on home · Campaign `urgency` on ABOUT/LEGAL · Fake `review` · RFQ and ATC mixed without page-level stance |

**Alignment:** SEO STANDARD; multi-page organic architecture.

---

## CATALOG

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **content priorities** | 1) Taxonomy `service_scope` 2) PDP `offer` + specs (`benefit` / features) 3) RFQ `cta` 4) `availability` / `price` only when sourced |
| **trust priorities** | 1) `proof` on PDP 2) `certificate` (industry) 3) `guarantee` (policy-linked) 4) `review` when authentic UGC enabled |
| **conversion priorities** | 1) Browse → PDP 2) RFQ / `contact` on PDP 3) Dealer/locator `location` (optional) 4) **no** cart/checkout signals |
| **forbidden content patterns** | `payment` / checkout `process` · Tier `pricing` block as site-wide required · LANDING-style single `offer` as entire site · `urgency` on PLP · Invented `availability` |

**Alignment:** SEO DEEP catalog; RFQ commerce path only.

---

## ECOMMERCE

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **content priorities** | 1) PDP `offer` + `price` + `availability` 2) `delivery` + `payment` on transaction path 3) `guarantee` / returns reference 4) `review` on PDP when enabled |
| **trust priorities** | 1) `trust` on PDP and checkout 2) `payment` security 3) `review` (UGC) 4) `certificate` (regulated categories) |
| **conversion priorities** | 1) ATC `cta` on PDP 2) Cart → checkout `process` 3) `consent` at checkout 4) Order confirmation utility (page extension — FUTURE) |
| **forbidden content patterns** | RFQ-only PDP when type is ECOMMERCE · Lead-form as PDP primary · LANDING linear `objection` stack on checkout · SEO/marketing `benefit` grids on checkout · False `urgency` · Unsupported `guarantee` |

**Alignment:** Transactional SEO; utility funnel simplicity on cart/checkout.

---

## CORPORATE

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **content priorities** | 1) `entity_identity` + `brand_narrative` 2) Subtree-appropriate `service_scope` (promo/catalog/ecommerce arms) 3) B2B `case` / `partners` 4) Section-specific signals per Blueprint arm |
| **trust priorities** | 1) `entity_identity` 2) `case` / `certificate` 3) `team` / `partners` 4) `experience` (verifiable) |
| **conversion priorities** | 1) Arm-specific primary (RFQ vs ATC per subtree) 2) `contact` / partner routes 3) Soft `cta` on ABOUT 4) Compliance-first on LEGAL |
| **forbidden content patterns** | Single global `offer` overriding subtree models · Commerce signals on non-commerce arms · Mixed cart + RFQ without page stance · Enterprise claims without HITL · Marketing signals on LEGAL routes |

**Alignment:** Composite IA — content profile follows active Blueprint subtree per route.

---

## Cross-type forbidden patterns (global)

| Pattern | Applies to |
|---------|------------|
| Invented facts, statistics, awards | All Core 5 |
| Fake `review` / testimonial | All Core 5 |
| Placeholder leakage (`lorem`, `TBD`, template tokens) | All Core 5 |
| Unsupported superlatives without evidence | All Core 5 |
| `legal_disclosure` marketing substitution | All Core 5 |
| `entity_identity` contradicting Legal Entity Card | All Core 5 |

---

## SAFE UNKNOWN

- Extended type content profiles — **FUTURE**
- Per-industry mandatory `certificate` sets — **FUTURE** (Industry Packs gap)

---

*Site Type Content Mapping version: v1.*
