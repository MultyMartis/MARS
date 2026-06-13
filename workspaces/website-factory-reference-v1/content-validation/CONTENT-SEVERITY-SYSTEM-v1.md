# Website Factory — Content Severity System v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** canonical severity taxonomy for content validation — **documentation only**  
**Связь:** [CONTENT-VALIDATION-RULES-v1.md](CONTENT-VALIDATION-RULES-v1.md), [CONTENT-VALIDATION-CONTRACT-v1.md](CONTENT-VALIDATION-CONTRACT-v1.md)

**Aligned with (separate layer):** [page-block-validation/VALIDATION-SEVERITY-SYSTEM-v1.md](../page-block-validation/VALIDATION-SEVERITY-SYSTEM-v1.md) — block presence vs signal architecture.

---

## Назначение

Content Severity System v1 классифицирует каждое отклонение **content signal** validation run. Severity определяет `status` (PASS / PASS_WITH_WARNINGS / FAIL) и приоритет исправления operator.

---

## Severity levels

| Level | Code | Gate impact | Operator action |
|-------|------|-------------|-----------------|
| **INFO** | `INFO` | None | Log; optional completeness |
| **WARNING** | `WARNING` | None alone — may yield PASS_WITH_WARNINGS | Document; fix before strict launch |
| **ERROR** | `ERROR` | **FAIL** | Fix architecture before Frontend |
| **CRITICAL** | `CRITICAL` | **FAIL** + Blueprint/legal review | Halt; reclassify or remove signals |

---

## Level definitions

### INFO

**Definition:** Observation without contract violation. Optional signal absent where not required; documentation note.

**Examples:**

| Scenario | Severity |
|----------|----------|
| Missing optional `proof` on `HERO` when not site-type mandated | INFO |
| Missing optional `urgency` on `CTA` | INFO |
| `experience` not used on ABOUT when optional only | INFO |

**status impact:** PASS (may appear in `warnings` with severity INFO)

---

### WARNING

**Definition:** Soft gap — recommended signal absent, evidence plan not yet attached, site-type profile recommends stronger trust.

**Examples:**

| Scenario | Severity |
|----------|----------|
| Missing optional `proof` on `LANDING_PAGE` `HERO` (recommended for LANDING) | WARNING |
| Missing optional `faq` page-level when inline FAQ block present | WARNING |
| `guarantee` optional on PDP not declared | WARNING |
| Design `VF_*` cross-check not performed | WARNING |

**status impact:** PASS_WITH_WARNINGS

---

### ERROR

**Definition:** Required signal missing; forbidden signal at ERROR tier; placeholder leakage; conversion/trust architecture break (non-legal-fraud).

**Examples:**

| Scenario | Severity |
|----------|----------|
| Missing required `offer` in `HERO` | ERROR |
| Missing required `cta` in `HERO` | ERROR |
| Missing `consent` on `LEAD_FORM` architecture | ERROR |
| Missing required `contact` on `CONTACTS` | ERROR |
| Placeholder leakage in bound slot | ERROR |
| Unsupported `signal_id` in declaration | ERROR |
| Missing `service_scope` on `CATEGORY_PAGE` | ERROR |

**status impact:** FAIL

---

### CRITICAL

**Definition:** Legal violation, fabricated proof/review architecture, commerce model violation, marketing on LEGAL_PAGE, fake evidence pattern.

**Examples:**

| Scenario | Severity |
|----------|----------|
| Fake `review` signal (no UGC_AUTHENTIC plan) | CRITICAL |
| Fake `proof` / invented statistics without evidence | CRITICAL |
| `legal_disclosure` missing on `LEGAL_PAGE` | CRITICAL |
| Marketing `offer` / `cta` primary on `LEGAL_PAGE` | CRITICAL |
| `payment` on CATALOG primary path | CRITICAL |
| `consent` missing on `CHECKOUT` | CRITICAL |
| Contradictory commerce signals (checkout on LANDING) | CRITICAL |
| Legal Pack violation (wrong document binding) | CRITICAL |

**status impact:** FAIL + halt

---

## Severity → status mapping

| Highest severity in run | `status` |
|-------------------------|----------|
| None | PASS |
| INFO only | PASS |
| WARNING only (no ERROR/CRITICAL) | PASS_WITH_WARNINGS |
| ≥1 ERROR | FAIL |
| ≥1 CRITICAL | FAIL |

---

## Cross-reference: common signal gaps

| Gap | Typical severity |
|-----|------------------|
| Missing optional signal | WARNING |
| Missing required `offer` | ERROR |
| Missing required `cta` | ERROR |
| Missing required `consent` (form) | CRITICAL |
| Fake review | CRITICAL |
| Fake proof | CRITICAL |
| Legal violation | CRITICAL |
| Missing `legal_disclosure` on LEGAL_PAGE | CRITICAL |
| Missing required trust on TRUST block | ERROR |
| Placeholder leakage | ERROR |

---

## SAFE UNKNOWN

- Whether strict LANDING elevates missing optional `proof` from WARNING to ERROR — **operator policy**; default WARNING in v1.

---

*Content Severity System version: v1.*
