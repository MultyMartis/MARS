# Website Factory — Block Content Contracts v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** authoritative `block_id` → content signals map — **architecture only**  
**Связь:** [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md), [CONTENT-SIGNAL-REGISTRY-v1.md](CONTENT-SIGNAL-REGISTRY-v1.md), [CONTENT-CONTRACT-v1.md](CONTENT-CONTRACT-v1.md)

**Не является:** block copy templates, component props, HTML partial content.

---

## Легенда

| Column | Meaning |
|--------|---------|
| **required** | Signals that **must** be satisfiable when block is REQUIRED on page |
| **optional** | Signals encouraged per Blueprint / site type |
| **forbidden** | Signals that **must not** appear in this block scope |

`conversion_role` / `trust_role` — from Block Registry unless noted.

---

## CONTENT blocks

### HERO — `CC_BLOCK_HERO`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | SECONDARY_CONVERSION |
| **trust_role** | SUPPORTING_TRUST (when proof present) |
| **required** | `offer`, `benefit`, `cta` |
| **optional** | `proof`, `trust`, `experience`, `urgency`, `service_scope`, `location` |
| **forbidden** | `legal_disclosure` (body), `consent`, `payment`, `comparison` (without catalog context) |

---

### BENEFITS — `CC_BLOCK_BENEFITS`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `benefit` |
| **optional** | `objection`, `comparison`, `proof` |
| **forbidden** | `price` (use PRICING), `payment`, `legal_disclosure`, `consent` |

---

### FEATURES — `CC_BLOCK_FEATURES`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `benefit` (capability framing) |
| **optional** | `comparison`, `service_scope`, `proof` |
| **forbidden** | `urgency`, `consent`, `legal_disclosure` |

---

### PROCESS — `CC_BLOCK_PROCESS`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `process` |
| **optional** | `objection`, `cta`, `delivery` |
| **forbidden** | `review` (use TESTIMONIALS/REVIEWS), `legal_disclosure` |

---

### FAQ — `CC_BLOCK_FAQ`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `question`, `answer`, `objection` |
| **optional** | `faq`, `guarantee`, `delivery`, `price` (stance-only) |
| **forbidden** | `urgency`, `offer` (as FAQ headline substitute), fabricated `review` |

---

### PRICING — `CC_BLOCK_PRICING`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | SECONDARY_CONVERSION |
| **trust_role** | SUPPORTING_TRUST |
| **required** | `price`, `cta` |
| **optional** | `offer`, `benefit`, `comparison`, `guarantee`, `objection` |
| **forbidden** | `urgency` (without SOURCE_DOCUMENTED), `legal_disclosure` (body) |

---

## COMPANY blocks

### SERVICES — `CC_BLOCK_SERVICES`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `service_scope`, `cta` |
| **optional** | `benefit`, `proof`, `case` |
| **forbidden** | `payment`, `checkout` signals, `consent` |

---

### CASES — `CC_BLOCK_CASES`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | SOCIAL_PROOF |
| **required** | `case`, `proof` |
| **optional** | `benefit`, `cta`, `service_scope` |
| **forbidden** | `price`, `urgency`, `comparison` (unless case is comparative study) |

---

### ABOUT — `CC_BLOCK_ABOUT`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | ENTITY_IDENTITY |
| **required** | `brand_narrative`, `entity_identity` |
| **optional** | `experience`, `proof`, `cta` |
| **forbidden** | `price`, `payment`, `urgency`, `offer` as primary substitute |

---

### TEAM — `CC_BLOCK_TEAM`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | PRIMARY_TRUST |
| **required** | `proof` (role/credential slots per person) |
| **optional** | `experience`, `brand_narrative` |
| **forbidden** | `price`, `cta` (primary), `urgency` |

---

### PARTNERS — `CC_BLOCK_PARTNERS`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | SOCIAL_PROOF |
| **required** | `proof` |
| **optional** | `cta`, `service_scope` |
| **forbidden** | `offer`, `price`, `urgency` |

---

## CATALOG blocks

### CATEGORIES — `CC_BLOCK_CATEGORIES`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `service_scope` (taxonomy scope) |
| **optional** | `cta`, `benefit` (category intro) |
| **forbidden** | `offer` (campaign), `urgency`, `process` (timeline) |

---

### CATEGORY_GRID — `CC_BLOCK_CATEGORY_GRID`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `service_scope` |
| **optional** | `cta`, `proof` |
| **forbidden** | `price` (grid cell), `lead_form`/`consent` in tile |

---

### PRODUCT_GRID — `CC_BLOCK_PRODUCT_GRID`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `service_scope` |
| **optional** | `price` (if listed), `availability`, `cta` |
| **forbidden** | `objection` (page-level), `legal_disclosure` |

---

### PRODUCT_CARD — `CC_BLOCK_PRODUCT_CARD`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | SUPPORTING_TRUST |
| **required** | `offer` (SKU/service unit), `cta` |
| **optional** | `price`, `availability`, `benefit`, `proof`, `guarantee`, `delivery`, `review` |
| **forbidden** | `urgency` (without source), `entity_identity` (footer scope) |

---

## TRUST blocks

### TESTIMONIALS — `CC_BLOCK_TESTIMONIALS`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | SOCIAL_PROOF |
| **required** | `proof`, `trust` |
| **optional** | `review` (curated quote slot), `case` |
| **forbidden** | Fabricated `review`; `price`; `urgency` |

---

### REVIEWS — `CC_BLOCK_REVIEWS`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | SOCIAL_PROOF |
| **required** | `review`, `proof`, `trust` |
| **optional** | `case`, `cta` |
| **forbidden** | Fabricated `review`; `offer` as review body; `urgency` |

---

### TRUST — `CC_BLOCK_TRUST`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | PRIMARY_TRUST |
| **required** | `proof`, `trust` |
| **optional** | `certificate`, `experience`, `guarantee` |
| **forbidden** | `price`, `cta` (primary), `legal_disclosure` (full body) |

---

### CERTIFICATES — `CC_BLOCK_CERTIFICATES`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | PRIMARY_TRUST |
| **required** | `certificate`, `trust` |
| **optional** | `proof`, `entity_identity` |
| **forbidden** | `urgency`, `offer`, `price` |

---

## CONVERSION blocks

### CTA — `CC_BLOCK_CTA`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | PRIMARY_CONVERSION |
| **trust_role** | NONE |
| **required** | `cta` |
| **optional** | `offer` (reminder), `urgency` (documented only) |
| **forbidden** | `legal_disclosure`, `review`, `faq` (full FAQ in CTA band) |

---

### LEAD_FORM — `CC_BLOCK_LEAD_FORM`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | PRIMARY_CONVERSION |
| **trust_role** | NONE |
| **required** | `cta`, `contact`, `consent` |
| **optional** | `offer`, `objection`, `service_scope` |
| **forbidden** | `urgency` (manipulative), `review`, `price` (unless RFQ field architecture) |

---

### CHECKOUT — `CC_BLOCK_CHECKOUT`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | PRIMARY_CONVERSION |
| **trust_role** | SUPPORTING_TRUST |
| **required** | `cta`, `process`, `payment`, `delivery`, `consent` |
| **optional** | `guarantee`, `trust`, `contact` |
| **forbidden** | `offer` (campaign), `benefit` grid, `urgency`, `review` |

---

### CART — `CC_BLOCK_CART`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | SECONDARY_CONVERSION |
| **trust_role** | NONE |
| **required** | `cta`, `price` (line totals) |
| **optional** | `delivery`, `guarantee`, `trust` |
| **forbidden** | `offer` (hero), `process` (full timeline), `legal_disclosure` |

---

## CONTACT blocks

### CONTACTS — `CC_BLOCK_CONTACTS`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | SECONDARY_CONVERSION |
| **trust_role** | ENTITY_IDENTITY |
| **required** | `contact`, `location` |
| **optional** | `cta`, `entity_identity`, `service_scope` |
| **forbidden** | `offer`, `price`, `urgency`, `review` |

---

### MAP — `CC_BLOCK_MAP`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `location` |
| **optional** | `contact` |
| **forbidden** | `offer`, `cta` (primary), `price`, `review` |

---

## COMMERCE blocks

### DELIVERY — `CC_BLOCK_DELIVERY`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | INFORMATIONAL |
| **trust_role** | NONE |
| **required** | `delivery` |
| **optional** | `location`, `guarantee`, `objection` |
| **forbidden** | `offer`, `urgency`, `review` |

---

### PAYMENT — `CC_BLOCK_PAYMENT`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | TRUST_SUPPORT |
| **trust_role** | SUPPORTING_TRUST |
| **required** | `payment`, `trust` |
| **optional** | `guarantee`, `entity_identity` |
| **forbidden** | `offer`, `benefit`, `urgency`, `review` |

---

## LEGAL / SYSTEM blocks

### LEGAL_LINKS — `CC_BLOCK_LEGAL_LINKS`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | LEGAL |
| **trust_role** | COMPLIANCE |
| **required** | `legal_disclosure` (link targets per Legal Pack) |
| **optional** | `entity_identity` |
| **forbidden** | `offer`, `cta` (primary), `benefit`, `urgency`, `review` |

---

### FOOTER — `CC_BLOCK_FOOTER`

| Dimension | Value |
|-----------|-------|
| **conversion_role** | SYSTEM |
| **trust_role** | ENTITY_IDENTITY |
| **required** | `entity_identity`, `contact`, `legal_disclosure` (via LEGAL_LINKS slot) |
| **optional** | `location`, `service_scope` (nav) |
| **forbidden** | `offer` (hero substitute), `urgency`, `price` |

---

## Validation summary

| Check | Result |
|-------|--------|
| Block count | **29** — matches BLOCK-REGISTRY-v1 |
| New `block_id` | **None** |
| Marketing copy in contracts | **None** |
| Signal ids | All reference CONTENT-SIGNAL-REGISTRY-v1 |

---

## SAFE UNKNOWN

- Per-site-type signal overrides within same `block_id` — document in project IA; default table above is canonical v1.
- HEADER_NAV / FILTERS — **not** `block_id` in v1 — no block content contract.

---

*Block Content Contracts version: v1.*
