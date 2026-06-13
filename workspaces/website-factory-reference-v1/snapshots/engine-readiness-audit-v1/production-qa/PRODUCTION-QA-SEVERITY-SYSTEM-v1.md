# Website Factory — Production Severity System v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** canonical severity taxonomy for production QA — **documentation only**  
**Связь:** [PRODUCTION-QA-CONTRACT-v1.md](PRODUCTION-QA-CONTRACT-v1.md), [PRODUCTION-QA-FAILURE-LIBRARY-v1.md](PRODUCTION-QA-FAILURE-LIBRARY-v1.md)

**Aligned with (separate layers):** [page-block-validation/VALIDATION-SEVERITY-SYSTEM-v1.md](../page-block-validation/VALIDATION-SEVERITY-SYSTEM-v1.md), [content-validation/CONTENT-SEVERITY-SYSTEM-v1.md](../content-validation/CONTENT-SEVERITY-SYSTEM-v1.md) — layer-specific; Production QA **aggregates** upstream severities.

---

## Назначение

Production Severity System v1 классифицирует каждое finding production QA run. Severity определяет contract `status` и приоритет исправления operator.

**v1 adds:** `BLOCKER` — prerequisite or process violation that prevents meaningful QA evaluation.

---

## Severity levels

| Level | Code | Gate impact | Contract status impact |
|-------|------|-------------|------------------------|
| **INFO** | `INFO` | None | May appear in `warnings`; alone → `PASS` |
| **WARNING** | `WARNING` | None alone | May yield `PASS_WITH_WARNINGS` |
| **ERROR** | `ERROR` | Relevant gate → FAIL | Contributes to `FAIL` |
| **CRITICAL** | `CRITICAL` | Relevant gate → FAIL | Contributes to `FAIL` |
| **BLOCKER** | `BLOCKER` | QA cannot complete | `BLOCKED` |

---

## Level definitions

### INFO

**Definition:** Observation without production QA contract violation. Documentation note; optional completeness.

**Examples:**

| Scenario | Severity |
|----------|----------|
| Optional page type in blueprint not yet instantiated | INFO |
| Recommended signal not declared (optional tier) | INFO |
| Matrix cell marked C not used in this project | INFO |

**Status impact:** `PASS` (record in `warnings` if logged)

---

### WARNING

**Definition:** Soft gap — should fix before strict handoff; does not alone block architecture pass if operator waives.

**Examples:**

| Scenario | Severity |
|----------|----------|
| PQF-016 superseded doc reference fixed in next pass | WARNING |
| PASS_WITH_WARNINGS on upstream validation with documented waiver | WARNING |
| Design cross-check not performed (recommended) | WARNING |
| Extended documentation pin missing (non-blocking) | WARNING |

**Status impact:** `PASS_WITH_WARNINGS` when no ERROR/CRITICAL/BLOCKER

**Waiver rule:** Operator must document `waiver_eligible: true` finding + rationale + owner in contract `notes`.

---

### ERROR

**Definition:** Required architecture artefact missing or inconsistent; blocks honest PASS.

**Examples:**

| Scenario | Severity |
|----------|----------|
| PQF-003 missing page contract | ERROR |
| PQF-007 missing validation | ERROR |
| PQF-011 missing SEO profile | ERROR |
| PQF-014 placeholder leakage | ERROR |
| Upstream validation ERROR propagated | ERROR |

**Status impact:** `FAIL`

---

### CRITICAL

**Definition:** Legal/compliance architecture break or aggregate integrity failure; halt handoff.

**Examples:**

| Scenario | Severity |
|----------|----------|
| PQF-005 missing Legal Pack | CRITICAL |
| PQF-006 missing Entity Card when required | CRITICAL |
| PQF-015 unresolved upstream CRITICAL/FAIL | CRITICAL |
| Legal route required but LEGAL_PAGE contract absent | CRITICAL |

**Status impact:** `FAIL` (treat as non-waivable for handoff unless explicit legal operator charter)

---

### BLOCKER

**Definition:** Cannot run or complete Production QA — missing layer, wrong prerequisites, process violation.

**Examples:**

| Scenario | Severity |
|----------|----------|
| PQF-001 missing architecture layer | BLOCKER |
| PQF-002 missing blueprint | BLOCKER |
| PQF-009 generation before readiness | BLOCKER |
| PQF-010 handoff before QA | BLOCKER |
| PQF-017 Extended type without charter | BLOCKER |
| `required_inputs` any status ≠ READY | BLOCKER |

**Status impact:** `BLOCKED`

---

## Severity → contract status mapping

| Highest severity in run | Required gates state | Contract `status` |
|-------------------------|----------------------|-------------------|
| — (none) | All PASS | `PASS` |
| INFO only | All PASS | `PASS` |
| WARNING only | All PASS | `PASS_WITH_WARNINGS` |
| ERROR | Any | `FAIL` |
| CRITICAL | Any | `FAIL` |
| BLOCKER | Any | `BLOCKED` |

**Mixed severities:** contract status = **most severe** applicable per table above.

**Upstream propagation:**

| Upstream contract status | Production QA default treatment |
|--------------------------|--------------------------------|
| Upstream `FAIL` | At least ERROR; often CRITICAL if legal |
| Upstream `CRITICAL` | CRITICAL in production QA |
| Upstream `PASS_WITH_WARNINGS` | WARNING in production QA unless waived |
| Missing upstream run | BLOCKER |

---

## Severity → gate status mapping

| Severity | Gate `status` |
|----------|---------------|
| INFO | `PASS` |
| WARNING | `PASS` or `PASS_WITH_WARNINGS` |
| ERROR | `FAIL` |
| CRITICAL | `FAIL` |
| BLOCKER | `BLOCKED` |

---

## Frontend Handoff rules

| Contract status | `GATE_FRONTEND_HANDOFF_APPROVED` |
|-----------------|----------------------------------|
| `PASS` | Allowed after operator sign-off |
| `PASS_WITH_WARNINGS` | Allowed with documented waivers |
| `FAIL` | **Forbidden** |
| `BLOCKED` | **Forbidden** |

**Explicit exclusion:** PASS status **does not** authorize production deployment, runtime release, or browser QA — architecture handoff only.

---

*Production Severity System v1 — five-level taxonomy for architectural QA.*
