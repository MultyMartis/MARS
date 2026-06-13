# Website Factory — Content Signal Validation Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** validation expectations for content signals — **documentation only**  
**Authority:** [BLOCK-CONTENT-CONTRACTS-v1.md](../content-contracts/BLOCK-CONTENT-CONTRACTS-v1.md), [PAGE-CONTENT-CONTRACTS-v1.md](../content-contracts/PAGE-CONTENT-CONTRACTS-v1.md), [SITE-TYPE-CONTENT-MAPPING-v1.md](../content-contracts/SITE-TYPE-CONTENT-MAPPING-v1.md)

**Scope:** Core 5 `site_type_code` · 10 `page_type` · 29 `block_id` · 28 `signal_id`

**Не является:** copy matrix, CMS field map, automated test suite.

---

## How to read this matrix

| Symbol | Meaning |
|--------|---------|
| **R** | Required when block/page is in stack and REQUIRED by page-block validation |
| **O** | Optional — absence → PASS; recommended absence → WARNING per site type |
| **F** | Forbidden — presence → FAIL (severity in Outcome column) |
| **—** | Not applicable (block not used on page type / site type) |
| **PASS** | All R satisfiable; no F present |
| **PWW** | PASS_WITH_WARNINGS — optional gaps only |
| **FAIL** | Missing R or present F at ERROR+ |

**Validation applies only when:** (1) Page Block Validation not FAIL; (2) `block_id` on stack; (3) `page_type` allowed for `site_type_code`.

---

## Part A — Site type overlays (Core 5)

Forbidden **patterns** (cross-page) — additive to block/page forbidden columns.

| site_type_code | Extra forbidden (architecture) | Trust/conversion emphasis |
|----------------|-------------------------------|----------------------------|
| `LANDING` | Catalog `service_scope` as primary IA; `payment`; fabricated `review` | Single `cta` path; `proof` before hard `cta` |
| `PROMO` | Ecommerce `payment` on non-checkout routes | `service_scope` on money pages; entity trust |
| `CATALOG` | `payment`, `cart` checkout signals site-wide | RFQ `cta`; no listed `price` without stance |
| `ECOMMERCE` | RFQ-only PDP without charter | `payment`+`delivery` on checkout path |
| `CORPORATE` | Campaign `urgency` site-wide | Subtree inherits CATALOG/ECOMMERCE commerce rules |

**Source:** [SITE-TYPE-CONTENT-MAPPING-v1.md](../content-contracts/SITE-TYPE-CONTENT-MAPPING-v1.md)

---

## Part B — Page-level signal matrix (10 page types)

Page-level signals **in addition to** block contracts. Authority: PAGE-CONTENT-CONTRACTS-v1.

| page_type | Required (R) | Optional (O) | Forbidden (F) | Expected if page-block PASS |
|-----------|--------------|--------------|---------------|----------------------------|
| `HOME_PAGE` | offer, entity_identity, service_scope, cta | benefit, proof, trust, review, case, location, contact | consent*, payment, process, legal_disclosure (body), urgency | PASS / PWW |
| `LANDING_PAGE` | offer, benefit, proof, objection, cta, contact | process, price, guarantee, faq, urgency† | service_scope, comparison, payment, delivery, review‡, legal_disclosure (body) | PASS strict; PWW if optional proof deferred |
| `SERVICE_PAGE` | offer, service_scope, benefit, proof, objection, cta | process, case, price, faq, contact, guarantee | payment, delivery, comparison§, urgency†, entity_identity (dup) | PASS |
| `CATEGORY_PAGE` | service_scope | benefit, proof, cta, price | offer, process, objection, consent, payment, urgency, review | PASS |
| `PRODUCT_PAGE` | offer, benefit, cta | price, availability, proof, review, guarantee, delivery, comparison, objection, contact | brand_narrative, urgency†, legal_disclosure (body), entity_identity (primary) | PASS / PWW |
| `ABOUT_PAGE` | brand_narrative, entity_identity, experience | proof, case, certificate, cta, contact | price, payment, offer, urgency, comparison, consent, review | PASS |
| `CONTACT_PAGE` | contact, location, entity_identity | cta, service_scope, consent* | offer, benefit, proof, price, urgency, review, comparison | PASS |
| `FAQ_PAGE` | faq, question, answer, objection | cta, contact, guarantee, delivery, process | offer, price, urgency, review, payment, legal_disclosure (body) | PASS |
| `REVIEWS_PAGE` | review, proof, trust | case, cta, entity_identity | offer, price, urgency, comparison, payment, legal_disclosure (body), fabricated review | PASS / FAIL if fake review |
| `LEGAL_PAGE` | legal_disclosure, entity_identity | contact | offer, benefit, cta, proof, trust, review, case, price, urgency, comparison, objection, payment | PASS or CRITICAL FAIL if marketing |

\* `consent` when form block on page  
† `urgency` only with SOURCE_DOCUMENTED  
‡ fabricated UGC  
§ comparison without comparables

---

## Part C — Block-level signal matrix (29 block IDs)

Authority: BLOCK-CONTENT-CONTRACTS-v1. **Outcome** = when block is REQUIRED on page.

| block_id | Required (R) | Optional (O) | Forbidden (F) | Outcome if R signals missing | Outcome if F present |
|----------|--------------|--------------|---------------|------------------------------|----------------------|
| `HERO` | offer, benefit, cta | proof, trust, experience, urgency, service_scope, location | legal_disclosure, consent, payment, comparison | FAIL (ERROR) | FAIL (CRITICAL payment) |
| `BENEFITS` | benefit | objection, comparison, proof | price, payment, legal_disclosure, consent | FAIL | FAIL |
| `FEATURES` | benefit | comparison, service_scope, proof | urgency, consent, legal_disclosure | FAIL | FAIL |
| `SERVICES` | service_scope, cta | benefit, proof, case | payment, consent | FAIL | FAIL |
| `CATEGORIES` | service_scope | cta, benefit | offer, urgency, process | FAIL | FAIL |
| `CATEGORY_GRID` | service_scope | cta, proof | price, consent | FAIL | FAIL |
| `PRODUCT_GRID` | service_scope | price, availability, cta | objection, legal_disclosure | FAIL | FAIL |
| `PRODUCT_CARD` | offer, cta | price, availability, benefit, proof, guarantee, delivery, review | urgency†, entity_identity | FAIL | FAIL |
| `PRICING` | price, cta | offer, benefit, comparison, guarantee, objection | urgency†, legal_disclosure (body) | FAIL | FAIL |
| `PROCESS` | process | objection, cta, delivery | review, legal_disclosure | FAIL | FAIL |
| `CASES` | case, proof | benefit, cta, service_scope | price, urgency, comparison | FAIL | FAIL |
| `TESTIMONIALS` | proof, trust | review, case | fabricated review, price, urgency | FAIL | CRITICAL if fake review |
| `REVIEWS` | review, proof, trust | case, cta | fabricated review, offer, urgency | FAIL | CRITICAL if fake review |
| `TRUST` | proof, trust | certificate, experience, guarantee | price, cta (primary), legal_disclosure (body) | FAIL | FAIL |
| `CERTIFICATES` | certificate, trust | proof, entity_identity | urgency, offer, price | FAIL | FAIL |
| `TEAM` | proof | experience, brand_narrative | price, cta (primary), urgency | FAIL | FAIL |
| `ABOUT` | brand_narrative, entity_identity | experience, proof, cta | price, payment, urgency, offer | FAIL | FAIL |
| `FAQ` | question, answer, objection | faq, guarantee, delivery, price | urgency, offer, fabricated review | FAIL | FAIL |
| `CTA` | cta | offer, urgency† | legal_disclosure, review, faq | FAIL | FAIL |
| `LEAD_FORM` | cta, contact, consent | offer, objection, service_scope | urgency, review, price | CRITICAL if no consent | FAIL |
| `CHECKOUT` | cta, process, payment, delivery, consent | guarantee, trust, contact | offer, benefit, urgency, review | CRITICAL if no consent | FAIL |
| `CART` | cta, price | delivery, guarantee, trust | offer, process, legal_disclosure | FAIL | FAIL |
| `CONTACTS` | contact, location | cta, entity_identity, service_scope | offer, price, urgency, review | FAIL | FAIL |
| `MAP` | location | contact | offer, cta (primary), price, review | FAIL | FAIL |
| `PARTNERS` | proof | cta, service_scope | offer, price, urgency | FAIL | FAIL |
| `DELIVERY` | delivery | location, guarantee, objection | offer, urgency, review | FAIL | FAIL |
| `PAYMENT` | payment, trust | guarantee, entity_identity | offer, benefit, urgency, review | FAIL | FAIL |
| `LEGAL_LINKS` | legal_disclosure | entity_identity | offer, cta (primary), benefit, urgency, review | ERROR | CRITICAL |
| `FOOTER` | entity_identity, contact, legal_disclosure | location, service_scope | offer, urgency, price | ERROR | FAIL |

---

## Part D — Site type × page type applicability

Which page types receive page-level validation under each Core site type.

| site_type_code | Applicable page_types (v1) | Notes |
|----------------|---------------------------|-------|
| `LANDING` | `LANDING_PAGE`, `LEGAL_PAGE` | No `HOME_PAGE` |
| `PROMO` | `HOME_PAGE`, `LANDING_PAGE`*, `SERVICE_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`, `FAQ_PAGE`, `REVIEWS_PAGE`, `LEGAL_PAGE` | *optional campaign |
| `CATALOG` | `HOME_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `CONTACT_PAGE`, `FAQ_PAGE`, `LEGAL_PAGE` | No `payment` site-wide |
| `ECOMMERCE` | `HOME_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `CONTACT_PAGE`, `FAQ_PAGE`, `LEGAL_PAGE` | Checkout utility — block contracts on route |
| `CORPORATE` | All except `LANDING_PAGE` required | Subtree: CATALOG/ECOMMERCE pages inherit commerce columns |

**Count check:** 10 `page_type` codes — **no new types**.

---

## Part E — Validation outcome expectations (summary)

| Condition | Expected status | Typical severity |
|-----------|-----------------|------------------|
| All R present; no F; optional gaps only | PASS or PWW | WARNING for optional |
| Missing R on REQUIRED block | FAIL | ERROR |
| Missing `consent` on LEAD_FORM/CHECKOUT | FAIL | CRITICAL |
| Fake `review` / `proof` architecture | FAIL | CRITICAL |
| `LEGAL_PAGE` marketing signals | FAIL | CRITICAL |
| Placeholder in production-bound slot | FAIL | ERROR |
| Forbidden `payment` on LANDING/CATALOG | FAIL | CRITICAL |
| Page-block FAIL upstream | **Do not run** | — |

---

## Part F — Block × typical page_type (validation trigger)

When page-block validation marks block **REQUIRED**, run Part C for that `block_id`.

| page_type | Typical REQUIRED blocks (content validation trigger) |
|-----------|---------------------------------------------------|
| `LANDING_PAGE` | HERO, BENEFITS, PROCESS, TRUST\|TESTIMONIALS, FAQ, LEAD_FORM, CTA, CONTACTS, FOOTER, LEGAL_LINKS |
| `HOME_PAGE` | HERO, FOOTER, LEGAL_LINKS, CONTACTS, CTA + type-specific (SERVICES / CATEGORIES) |
| `SERVICE_PAGE` | HERO, SERVICES or FEATURES, LEAD_FORM, CTA, TRUST, FOOTER, LEGAL_LINKS |
| `CATEGORY_PAGE` | CATEGORIES or CATEGORY_GRID, PRODUCT_GRID (optional), FOOTER, LEGAL_LINKS |
| `PRODUCT_PAGE` | PRODUCT_CARD, TRUST, CTA, FOOTER, LEGAL_LINKS |
| `ABOUT_PAGE` | ABOUT, TEAM (optional), FOOTER, LEGAL_LINKS |
| `CONTACT_PAGE` | CONTACTS, MAP (optional), LEAD_FORM (optional), FOOTER, LEGAL_LINKS |
| `FAQ_PAGE` | FAQ, FOOTER, LEGAL_LINKS |
| `REVIEWS_PAGE` | REVIEWS or TESTIMONIALS, FOOTER, LEGAL_LINKS |
| `LEGAL_PAGE` | (no marketing blocks) — page-level LEGAL only |

Full block stance: [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md).

---

## Taxonomy verification

| Entity | v1 count | New in this workstream |
|--------|----------|------------------------|
| `site_type_code` (Core) | 5 | **None** |
| `page_type` | 10 | **None** |
| `block_id` | 29 | **None** |
| `signal_id` | 28 | **None** |

---

## SAFE UNKNOWN

- Per-project OR-group signal satisfaction (e.g. TRUST vs TESTIMONIALS proof) — manual documentation v1.
- CART_PAGE / CHECKOUT_PAGE page-level profiles — **FUTURE** (block contracts apply on utility routes).

---

*Content Signal Validation Matrix version: v1.*
