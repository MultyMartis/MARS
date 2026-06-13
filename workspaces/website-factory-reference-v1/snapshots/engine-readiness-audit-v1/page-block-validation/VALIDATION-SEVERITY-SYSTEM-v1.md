# Website Factory — Validation Severity System v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** canonical severity taxonomy — **documentation only**  
**Связь:** [PAGE-BLOCK-VALIDATION-RULES-v1.md](PAGE-BLOCK-VALIDATION-RULES-v1.md), [VALIDATION-CONTRACT-v1.md](VALIDATION-CONTRACT-v1.md)

---

## Назначение

Severity System v1 классифицирует каждое отклонение validation run. Severity определяет, блокирует ли issue production gate и как operator prioritizes correction.

---

## Severity levels

| Level | Code | Gate impact | Operator action |
|-------|------|-------------|-----------------|
| **INFO** | `INFO` | None | Log; optional improvement |
| **WARNING** | `WARNING` | None alone — may yield PASS_WITH_WARNINGS | Document; fix before launch if strict |
| **ERROR** | `ERROR` | **FAIL** | Fix before Design/Frontend |
| **CRITICAL** | `CRITICAL` | **FAIL** + likely reclassification | Halt; Blueprint/site type review |

---

## Level definitions

### INFO

**Definition:** Observation that does not indicate contract violation. Optional or recommended element absent; cosmetic IA note.

**Examples:**

- Missing optional `MAP` on `CONTACT_PAGE`
- Missing optional `HERO` on `FAQ_PAGE`
- Recommended `TRUST` absent on PROMO `HOME_PAGE` when not REQUIRED

**status impact:** PASS (may be noted in `warnings` with severity INFO)

---

### WARNING

**Definition:** Contract soft gap — recommended block missing, OR-group borderline, registry drift item. Does **not** alone fail strict PASS but flags risk.

**Examples:**

- Missing `FAQ` on `HOME_PAGE` (optional but recommended for PROMO)
- Missing `FAQ` on strict `LANDING_PAGE` review (operator may escalate to ERROR)
- Mobile sticky `CTA` variant absent — WARNING (VF-015); legacy label `STICKY_CTA` maps to `CTA`
- CORPORATE subtree route group undocumented

**status impact:** PASS_WITH_WARNINGS

---

### ERROR

**Definition:** Required block missing or forbidden block present at page level (non-commerce-critical). Breaks page contract; must fix before downstream work.

**Examples:**

- Missing `LEAD_FORM` on `LANDING_PAGE` or `SERVICE_PAGE`
- Missing `LEGAL_LINKS` on marketing page when Legal Pack applies
- Missing `CTA` on money page
- Missing `BENEFITS` **and** `FEATURES` on `SERVICE_PAGE` (OR-group fail)
- Unknown `block_id` in stack

**status impact:** FAIL

---

### CRITICAL

**Definition:** Structural or Blueprint-level violation. Wrong site model, commerce on wrong type, missing identity/conversion anchor.

**Examples:**

- Missing `HERO` on `LANDING_PAGE` or primary conversion page
- Missing `PRODUCT_GRID` on `CATEGORY_PAGE`
- Missing `PRODUCT_CARD` on `PRODUCT_PAGE`
- Missing `ABOUT` block on `ABOUT_PAGE`
- Missing `CONTACTS` on `CONTACT_PAGE`
- `CART` / `CHECKOUT` / `PAYMENT` on LANDING or CATALOG PLP
- `HOME_PAGE` on `LANDING` site type
- `CATEGORY_PAGE` with `CHECKOUT`

**status impact:** FAIL + operator reclassification review

---

## Canonical examples (task reference)

| Scenario | Severity | Rationale |
|----------|----------|-----------|
| Missing FAQ (optional context) | WARNING | OPTIONAL on many page types |
| Missing FAQ on LANDING primary | ERROR | REQUIRED in mapping for LANDING_PAGE |
| Missing LEAD_FORM on LANDING | ERROR | Primary conversion block |
| Missing HERO on LANDING | CRITICAL | First viewport / identity anchor |
| Missing LEGAL_LINKS on marketing page | ERROR | Legal Pack production gate |
| CART on LANDING | CRITICAL | Blueprint misclassification |
| CHECKOUT on CATEGORY_PAGE | CRITICAL | Forbidden placement |

---

## Severity assignment rules

1. **FORBIDDEN commerce blocks** on wrong Blueprint → default **CRITICAL**
2. **Missing REQUIRED** from PAGE-BLOCK-MAPPING → default **ERROR**; escalate to **CRITICAL** if block is identity/transaction anchor (HERO on LANDING, PRODUCT_GRID on PLP, PRODUCT_CARD on PDP, CONTACTS on CONTACT_PAGE)
3. **Missing OPTIONAL** → **INFO** or **WARNING** if CORE-PAGE-ARCHITECTURES says recommended
4. **page_type FORBIDDEN** for site_type → **CRITICAL**
5. **Mobile sticky `CTA` variant** → **WARNING** if absent on LANDING (VF-015). Embedded video — out of block validation scope (not `block_id`).

---

## Aggregation reference

```
CRITICAL anywhere in missing_blocks or unexpected_blocks → FAIL
ERROR anywhere (and no CRITICAL) → FAIL
Only WARNING / INFO → PASS_WITH_WARNINGS or PASS
```

Full logic: [PAGE-BLOCK-VALIDATION-RULES-v1.md](PAGE-BLOCK-VALIDATION-RULES-v1.md) § Status aggregation

---

## SAFE UNKNOWN

- Per-project severity override table — **HITL only**; not in v1 automation
- Severity → CI exit code mapping — **FUTURE**

---

*Validation Severity System version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
