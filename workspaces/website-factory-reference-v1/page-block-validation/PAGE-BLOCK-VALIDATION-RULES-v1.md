# Website Factory — Page Block Validation Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** каноническая validation logic — **documentation only**  
**Связь:** [VALIDATION-CONTRACT-v1.md](VALIDATION-CONTRACT-v1.md), [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md)

**Не является:** executable rules engine, linter config, CI policy

---

## Назначение

Правила ниже определяют, как из `required_blocks`, `optional_blocks`, `forbidden_blocks` и **actual stack** получается `status` = PASS | PASS_WITH_WARNINGS | FAIL.

**Authority order (conflict resolution):**

1. [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md) — per `page_type`
2. [BLUEPRINT-BLOCK-MAPPING-v1.md](../block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md) — site-wide FORBIDDEN
3. [CORE-PAGE-ARCHITECTURES-v1.md](../page-architecture/CORE-PAGE-ARCHITECTURES-v1.md) — recommended / OR-groups
4. Project Page Contract — **cannot weaken** 1–3

---

## Core rules

### Rule 1 — REQUIRED blocks must exist

**Statement:** Every `block_id` marked REQUIRED for the target `page_type` (after OR-group resolution) **must** appear in the actual stack.

| Outcome | Condition |
|---------|-----------|
| **PASS contribution** | All REQUIRED present |
| **FAIL** | Any REQUIRED missing at severity ERROR or CRITICAL |

**Severity:** per [VALIDATION-SEVERITY-SYSTEM-v1.md](VALIDATION-SEVERITY-SYSTEM-v1.md) and [PAGE-TYPE-VALIDATION-MATRIX-v1.md](PAGE-TYPE-VALIDATION-MATRIX-v1.md).

---

### Rule 2 — FORBIDDEN blocks must not exist

**Statement:** Any `block_id` marked FORBIDDEN for the target `page_type` **must not** appear in the actual stack.

| Outcome | Condition |
|---------|-----------|
| **PASS contribution** | Zero FORBIDDEN present |
| **FAIL** | Any FORBIDDEN present — typically CRITICAL for commerce blocks on wrong type |

**Operator action:** FORBIDDEN commerce blocks (`CART`, `CHECKOUT`, `PAYMENT`) on LANDING/CATALOG → **halt** + reclassify Blueprint.

---

### Rule 3 — OPTIONAL blocks do not affect PASS/FAIL

**Statement:** Presence or absence of OPTIONAL blocks **does not** change PASS/FAIL.

| Outcome | Condition |
|---------|-----------|
| **PASS** | OPTIONAL absent — allowed |
| **PASS_WITH_WARNINGS** | OPTIONAL absent but **recommended** in CORE-PAGE-ARCHITECTURES — emit WARNING |
| **No FAIL** | OPTIONAL alone never causes FAIL |

**Exception:** OPTIONAL block that is **also** FORBIDDEN on another grounds (wrong page_type) → Rule 2 applies if present.

---

### Rule 4 — Unknown block_id

**Statement:** Any `block_id` in actual stack **not** in [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) → `unexpected_blocks` with severity **ERROR**.

---

### Rule 5 — OR-group satisfaction

**Statement:** When mapping requires **one of** several blocks, at least **one** member must be present.

| Group | page_type | Members | Min satisfied |
|-------|-----------|---------|---------------|
| Social proof | `LANDING_PAGE` | `TRUST`, `TESTIMONIALS` | 1 |
| Value scope | `SERVICE_PAGE` | `BENEFITS`, `FEATURES` | 1 |
| Reviews hub | `REVIEWS_PAGE` | `TESTIMONIALS`, `REVIEWS` | 1 |

**Failure:** list as `missing_blocks` entry with `block_id: "<GROUP_ID>"` or enumerate absent members; severity **ERROR** unless matrix says WARNING.

---

### Rule 6 — LEGAL_LINKS placement

**Statement:**

- On all marketing `page_type` routes when Legal Pack applies: `LEGAL_LINKS` **REQUIRED** (typically within `FOOTER`).
- On `LEGAL_PAGE`: marketing blocks **FORBIDDEN**; validate absence of `HERO`, `LEAD_FORM`, `CTA`, etc.
- `LEGAL_LINKS` on **other** routes satisfies production gate; not duplicated as marketing stack on legal body.

**Ref:** [LEGAL-PAGE-CONTRACT-v1.md](../page-architecture/LEGAL-PAGE-CONTRACT-v1.md)

---

### Rule 7 — Site type × page type gate (pre-block)

**Statement:** Before block rules, verify `page_type` is not FORBIDDEN for `site_type_code` per [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md).

**Failure:** `status` = FAIL, severity **CRITICAL**, message: reclassify site type or remove page.

---

### Rule 8 — Blueprint site-wide FORBIDDEN

**Statement:** Blocks FORBIDDEN at Blueprint level must not appear **anywhere** in the site IA unless page mapping explicitly allows (rare; document HITL).

**Example:** `CART` site-wide on CATALOG Blueprint → any page with `CART` → FAIL.

---

## Status aggregation

```
IF any unexpected_blocks with severity CRITICAL
   OR any missing_blocks with severity CRITICAL
   OR page_type FORBIDDEN for site_type
   → status = FAIL

ELSE IF any missing_blocks with severity ERROR
   OR any unexpected_blocks with severity ERROR
   OR any OR-group unsatisfied
   → status = FAIL

ELSE IF any warnings OR missing_blocks with severity WARNING only
   → status = PASS_WITH_WARNINGS

ELSE
   → status = PASS
```

---

## Examples

### Example PASS

**Target:** `LANDING` / `LANDING_PAGE`

**Actual stack:** `HERO`, `BENEFITS`, `PROCESS`, `TESTIMONIALS`, `FAQ`, `LEAD_FORM`, `CTA`, `CONTACTS`, `FOOTER`, `LEGAL_LINKS`

| Check | Result |
|-------|--------|
| REQUIRED | All present (TESTIMONIALS satisfies social proof OR-group) |
| FORBIDDEN | None |
| OPTIONAL | `PRICING` absent — OK |

**status:** PASS

---

### Example FAIL (missing conversion)

**Target:** `LANDING` / `LANDING_PAGE`

**Actual stack:** `HERO`, `BENEFITS`, `PROCESS`, `TRUST`, `FAQ`, `CTA`, `CONTACTS`, `FOOTER`, `LEGAL_LINKS`

| Check | Result |
|-------|--------|
| Missing | `LEAD_FORM` — ERROR |
| FORBIDDEN | None |

**status:** FAIL

---

### Example FAIL (FORBIDDEN block)

**Target:** `CATALOG` / `CATEGORY_PAGE`

**Actual stack:** `HERO`, `PRODUCT_GRID`, `CART`, `FOOTER`, `LEGAL_LINKS`

| Check | Result |
|-------|--------|
| Missing | None critical |
| FORBIDDEN | `CART` on PLP — CRITICAL |

**status:** FAIL — reclassify ECOMMERCE or remove CART from PLP

---

### Example PASS_WITH_WARNINGS

**Target:** `PROMO` / `HOME_PAGE`

**Actual stack:** `HERO`, `SERVICES`, `CTA`, `CONTACTS`, `FOOTER`, `LEGAL_LINKS`

| Check | Result |
|-------|--------|
| REQUIRED | Met |
| WARNING | `FAQ` recommended optional absent |
| WARNING | `TRUST` recommended absent |

**status:** PASS_WITH_WARNINGS

---

## Manual validation checklist

- [ ] Resolve `site_type_code` + `page_type` + Blueprint
- [ ] Confirm page_type allowed in SITE-TYPE-PAGE-MATRIX
- [ ] Load REQUIRED / OPTIONAL / FORBIDDEN from PAGE-BLOCK-MAPPING
- [ ] Expand OR-groups
- [ ] Collect actual stack from Page Contract / IA
- [ ] Apply Rules 1–8
- [ ] Assign severities
- [ ] Emit VALIDATION-CONTRACT fields
- [ ] Gate: FAIL → halt

---

## SAFE UNKNOWN

- Automated Rule 5 OR-group detection — **manual v1**
- Mobile sticky CTA — canonical `block_id` is `CTA`; reference partial `sticky_cta.html` is an implementation variant. If stack lists legacy label `STICKY_CTA`, map to `CTA`. If mobile sticky pattern absent on LANDING, emit WARNING (VF-015).

---

*Page Block Validation Rules version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
