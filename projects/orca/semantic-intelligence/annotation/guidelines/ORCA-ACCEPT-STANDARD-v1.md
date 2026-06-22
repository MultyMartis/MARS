# ORCA ACCEPT Standard v1

**Standard ID:** `orca-accept-standard`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Defines when `commercial_eligibility.decision` may be set to **ACCEPT** — admission of a phrase to the approved semantic core path (subject to review gates). ACCEPT is the **highest-evidence** positive gate outcome; it requires satisfying **all seven requirements** below.

Aligns with P0-B: 27 primary intents, commercial eligibility taxonomy, record invariants 1–2, 4, 9, 15, 18.

---

## Seven requirements for ACCEPT

Every ACCEPT record must satisfy **all seven**. Failure of any single requirement → ABSTAIN or REJECT, never partial ACCEPT.

### R1 — Positive commercial evidence

At least one **STRONG** or **EXPLICIT** commercial signal path is present and documented in `signals[]` with `evidence_span`.

- Permitted signal families: `PROVIDER_HIRE`, `IMPLEMENTATION`, `CONFIGURATION`, `MODIFICATION`, `INTEGRATION`, `SUPPORT`, `RECOVERY`, `AUDIT_DIAGNOSTIC`, `MIGRATION`, `MAINTENANCE`, or validated problem+provider cluster per problem adjudication.
- **Forbidden:** ACCEPT on WEAK/MEDIUM topical match alone (invariant 1–2).

### R2 — Eligible primary intent

`primary_intent` must be compatible with commercial service admission:

- Commercial family: `HIRE_SERVICE`, `REQUEST_*` (implementation, configuration, modification, integration, migration, maintenance, support, recovery, audit, quote where hire path confirmed), or `PROBLEM_UNRESOLVED` only with `STRONG_PAID_SERVICE_PROBLEM_INTENT`.
- `may_support_accept: true` on assigned intent **or** explicit operator seed override with audit.
- **Forbidden:** ACCEPT when dominant intent is protected stratum (`EDUCATIONAL`, `CAREER_EMPLOYMENT`, `DIY_HOW_TO`, `REGULATORY` info-only, `NAVIGATIONAL`, `DOWNLOAD_RESOURCE`) unless operator override.

### R3 — No unresolved mandatory ambiguity

None of the following may remain unresolved at eligibility boundary:

- `PROVIDER_VS_DIY`
- `PRODUCT_VS_SERVICE`
- `CAREER_VS_PROVIDER`
- `SUPPORT_VS_INFORMATION`
- `SHORT_HEAD_TERM` (HIGH/CRITICAL)
- `MULTIPLE`

→ Otherwise **ABSTAIN** (invariant 4).

### R4 — Protected strata adjudicated

Conflicting protected signals must be resolved with documented dominance. Unresolved protected conflict → **ABSTAIN** `PROTECTED_SIGNAL_CONFLICT` (invariant 3).

### R5 — Valid ACCEPT reason_code

`commercial_eligibility.reason_code` must be exactly one ACCEPT family code:

| reason_code | Typical path |
|-------------|--------------|
| `EXPLICIT_PROVIDER_REQUEST` | Explicit hire/provider |
| `EXPLICIT_SERVICE_REQUEST` | Commercial service verb + object |
| `EXPLICIT_IMPLEMENTATION_CONFIGURATION_MODIFICATION` | Scoped paid work |
| `EXPLICIT_SUPPORT_RECOVERY_REQUEST` | Support/recovery engagement |
| `STRONG_PAID_SERVICE_PROBLEM_INTENT` | Problem + provider path |
| `STRONG_GEOGRAPHY_PLUS_SERVICE_INTENT` | Geo + commercial task |
| `VALIDATED_OPERATOR_SEED` | Operator-prevalidated |

### R6 — Confidence and provenance

| Field | Requirement |
|-------|-------------|
| `commercial_eligibility.confidence` | Meets `threshold_profile`; not below automated ACCEPT floor |
| `provenance_status` | Not `MISSING` (invariant 7) |
| `versioning` | rule/model/prompt versions recorded for automated decisions (invariant 8) |

### R7 — Phrase-specific rationale

`phrase_explanation` (or equivalent narrative) must meet [`ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md) — all six elements, no generic templates.

---

## ACCEPT evidence types

### Type E — Explicit commercial

**Definition:** EXPLICIT commercial signal + identifiable task object in the phrase.

| Marker | Example (RU) | reason_code |
|--------|--------------|-------------|
| Hire verb | «заказать внедрение crm под ключ» | `EXPLICIT_PROVIDER_REQUEST` |
| Implementation | «внедрение 1с erp на предприятии» | `EXPLICIT_SERVICE_REQUEST` |
| Configuration outsource | «настроить 1с специалистом» | `EXPLICIT_IMPLEMENTATION_CONFIGURATION_MODIFICATION` |
| Support/recovery | «вызвать специалиста 1с срочно» | `EXPLICIT_SUPPORT_RECOVERY_REQUEST` |

**Requirements:** No EXPLICIT opposing protected signal. Task object scoped to campaign service domain.

### Type I — Implicit commercial (strict)

**Definition:** No single EXPLICIT hire verb, but **multiple STRONG** commercial signals form an unambiguous paid-service task.

| Pattern | Example (RU) | Notes |
|---------|--------------|-------|
| STRONG implementation + geo | «монтаж вентиляции москва под ключ» | DIY must be ruled out |
| STRONG problem + provider | «1с не проводит документ вызвать мастера» | Problem adjudication |
| STRONG service collocation | «аудит 1с на предприятии стоимость работ» | Not quote-only |

**Requirements:**

- At least **two** STRONG commercial signals **or** one STRONG + supporting MEDIUM cluster
- Implicit ACCEPT **never** on head terms or single MEDIUM token
- reason_code typically `STRONG_PAID_SERVICE_PROBLEM_INTENT` or `STRONG_GEOGRAPHY_PLUS_SERVICE_INTENT`

**Forbidden implicit patterns:**

- «внедрение crm» alone without provider context when DIY plausible → ABSTAIN
- «стоимость работ» without task → informational

### Type O — Operator seed (`VALIDATED_OPERATOR_SEED`)

**Definition:** Phrase appears on operator-approved seed list with explicit audit linkage.

| Requirement | Detail |
|-------------|--------|
| Exact match | Normalized phrase matches seed entry |
| Seed record | ID, approval date, operator, scope |
| Campaign fit | Seed scope matches service catalog |
| Review | `reviewer_required` per seed policy |
| Rationale | Cite seed ID in element 6 of phrase rationale |

Operator seed **does not** bypass invariants 10–11 (no campaign/cluster fields in semantic record). It **does** satisfy R1 when seed charter declares prevalidated commercial evidence.

---

## ACCEPT vs primary_intent separation

Invariant 15: intent ≠ decision.

| primary_intent | decision | Valid? |
|----------------|----------|--------|
| `HIRE_SERVICE` | ACCEPT | Yes — typical |
| `HIRE_SERVICE` | ABSTAIN | Yes — insufficient evidence |
| `REQUEST_IMPLEMENTATION` | ACCEPT | Yes |
| `PROBLEM_UNRESOLVED` | ACCEPT | Yes — with R1 problem path |
| `INFORMATIONAL` | ACCEPT | **No** — dominant info |
| `UNKNOWN` | ACCEPT | **No** — invariant 18 |

---

## Service mapping boundary (invariant 9)

ACCEPT authorizes **candidate** service mapping (`mapping_status: CANDIDATE_ONLY`). Final `service_id` assignment occurs downstream — not at semantic eligibility without separate mapping gate.

---

## Reviewer_required norms

Set `commercial_eligibility.reviewer_required: true` when:

- Implicit commercial (Type I) ACCEPT
- High `risk` score
- Borderline confidence
- Operator seed with charter requirement
- Any ACCEPT on problem-shaped phrase

---

## Examples (RU)

| Query | Type | decision | reason_code |
|-------|------|----------|-------------|
| «заказать внедрение crm под ключ» | E | ACCEPT | `EXPLICIT_PROVIDER_REQUEST` |
| «доработать отчёт 1с под требования заказчика» | E | ACCEPT | `EXPLICIT_IMPLEMENTATION_CONFIGURATION_MODIFICATION` |
| «монтаж вентиляции спб под ключ» | I | ACCEPT | `STRONG_GEOGRAPHY_PLUS_SERVICE_INTENT` |
| «1с» | — | ABSTAIN | — (R3 fails) |
| «курс 1с» | — | REJECT | — (R2 fails) |
| «сколько стоит внедрение» | — | REJECT/ABSTAIN | — (no hire — R1 fails) |

---

## Anti-patterns

| Anti-pattern | Violation |
|--------------|-----------|
| ACCEPT on topic/domain only | R1, invariant 1 |
| ACCEPT with unresolved DIY conflict | R3 |
| ACCEPT `UNKNOWN` intent | R2, invariant 18 |
| Generic phrase_explanation | R7 |
| Missing reason_code | R5 |
| Final service_id at eligibility | Invariant 9 |

---

## Related documents

- [`ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md`](ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md)
- [`ORCA-REJECT-STANDARD-v1.md`](ORCA-REJECT-STANDARD-v1.md)
- [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
- [`ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md)
