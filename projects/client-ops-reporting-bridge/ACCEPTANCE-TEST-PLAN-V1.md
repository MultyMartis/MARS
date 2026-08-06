# Acceptance Test Plan v1

**Status:** DESIGN ONLY / PHASE 0B  
**Execution:** Phase 0B executes **none** of these tests  
**Purpose:** Deterministic acceptance specification for future Phase 1 implementation

---

## 1. Test scope

| In scope | Out of scope |
|----------|--------------|
| Offline fixture normalization | Live production Telegram as first step |
| Exporter dry-run / isolated publish | SITE-002 production mutation tests |
| n8n sandbox intake and approved test chat | Client routing tests |
| Security / dedupe / retry / rollback proofs | Hub Gateway runtime tests |
| No-production-mutation proofs | Real credential values in Git |

---

## 2. Test levels

| Level | Name | Goal |
|-------|------|------|
| **L0** | Documentation and schema review | Contract + design coherence |
| **L1** | Offline fixture normalization | Algorithm determinism |
| **L2** | Exporter dry-run against copied fixtures | validate-only / build-envelope |
| **L3** | Atomic publication in isolated test Storage folder | by-run + latest protocol |
| **L4** | n8n sandbox intake without Telegram send | validation + dedupe |
| **L5** | n8n sandbox Telegram to approved internal test chat | SIMPLE delivery |
| **L6** | One controlled production workflow activation | HITL |
| **L7** | Multi-day observation | Stability / stale / OK policy |

---

## 3. Fixture validation

Each fixture in `TEST-FIXTURES-SPEC-V1.md` must declare expected:

- `site_status` / `summary_code` / `action.code`
- `event_id` stability class
- SIMPLE message shape
- publication allowed? (security)

---

## 4. Exporter unit-level acceptance

- Discover completed vs in-progress correctly.
- Read-only (no source writes).
- Missing metric ≠ zero.
- Conflict → BLOCKED.
- Stale → BLOCKED with `SOURCE_REPORT_STALE`.
- Security reject → no publish.

---

## 5. Normalization acceptance

- Order matches `NORMALIZATION-ALGORITHM-V1.md`.
- Identical inputs → identical envelope identity fields + `event_id`.

---

## 6. Promoted artifact acceptance

- Temp never exposed as final.
- by-run immutable.
- latest replaced only after by-run success.
- failure does not clobber latest.

---

## 7. n8n sandbox acceptance

- Independent schema/security gates.
- Dedupe statuses correct.
- No raw artifact reread required.

---

## 8. Telegram sandbox acceptance

- Approved test chat only.
- Counts match envelope.
- FAILED/BLOCKED not suppressed.
- OK sends during validation period.
- Parse-mode safe.

---

## 9. Failure / retry acceptance

- Same `event_id` on retry.
- No duplicate after confirmed SENT.
- Telegram failure leaves `site_status` unchanged.

---

## 10. Security acceptance

Reject publication / send when:

- `contains_secrets != false`
- `redacted != true`
- absolute/UNC paths in public fields
- credentialed URIs / token markers / raw stacks / raw logs

---

## 11. No-production-mutation acceptance

Evidence must show zero:

- SITE-002 production writes
- monitor code/scheduler/baseline changes
- Storage source-run mutations

---

## 12. Rollback acceptance

- Disable workflow restores quiet state.
- Source monitor still intact.
- Last envelope preserved.

---

## 13. Phase 1 exit criteria

- L0–L5 pass for selected profile.
- L6 HITL complete.
- L7 observation started with documented window.
- Remaining operator gates closed.

---

## 14. Test matrix

| Test ID | Scenario | Input fixture | Expected site_status | Expected summary_code | Expected action.code | Expected publication | Expected Telegram send policy | Expected dedupe behavior | Evidence required |
|---------|----------|---------------|----------------------|-----------------------|----------------------|----------------------|-------------------------------|--------------------------|-------------------|
| AT-001 | valid OK | fixture-ok | OK | NO_ACTION_REQUIRED | NONE | yes | send (validation period) | NEW then DUPLICATE_ALREADY_SENT | envelope + SIMPLE |
| AT-002 | valid ATTENTION onboarding | fixture-attention-onboarding | ATTENTION | ONBOARDING_REQUIRED | REVIEW_ONBOARDING | yes | always send | NEW | envelope + SIMPLE |
| AT-003 | valid ATTENTION hygiene | fixture-attention-hygiene | ATTENTION | HYGIENE_REVIEW_REQUIRED | REVIEW_HYGIENE | yes | always send | NEW | envelope + SIMPLE |
| AT-004 | valid FAILED monitor | fixture-failed-execution | FAILED | SOURCE_EXECUTION_FAILED | REVIEW_SOURCE_FAILURE | yes | always send | NEW | envelope + SIMPLE |
| AT-005 | stale report | fixture-blocked-stale | BLOCKED | SOURCE_REPORT_STALE | REVIEW_SCHEDULER_AND_ARTIFACTS | yes | always send | NEW | age_seconds proof |
| AT-006 | missing monitor-classification | fixture-blocked-missing-artifact | BLOCKED | SOURCE_ARTIFACT_MISSING | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | missing-file evidence |
| AT-007 | missing changed-summary | fixture-blocked-missing-artifact | BLOCKED | SOURCE_ARTIFACT_MISSING | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | missing-file evidence |
| AT-008 | missing run-summary | fixture-blocked-missing-artifact | BLOCKED | SOURCE_ARTIFACT_MISSING | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | missing-file evidence |
| AT-009 | malformed classification JSON | fixture-blocked-malformed-json | BLOCKED | SOURCE_ARTIFACT_MALFORMED | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | parse error evidence |
| AT-010 | malformed metrics JSON | fixture-blocked-malformed-json | BLOCKED | SOURCE_ARTIFACT_MALFORMED | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | parse error evidence |
| AT-011 | malformed execution JSON | fixture-blocked-malformed-json | BLOCKED | SOURCE_ARTIFACT_MALFORMED | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | parse error evidence |
| AT-012 | classification conflict | fixture-blocked-classification-conflict | BLOCKED | SOURCE_ARTIFACT_CONFLICT | REVIEW_SOURCE_ARTIFACTS | yes | always send | NEW | conflict reasons |
| AT-013 | onboarding count conflict | fixture-blocked-classification-conflict | BLOCKED | SOURCE_ARTIFACT_CONFLICT | REVIEW_SOURCE_ARTIFACTS | yes | always send | NEW | reason codes |
| AT-014 | baseline/current/delta conflict | fixture-blocked-metric-conflict | BLOCKED | SOURCE_ARTIFACT_CONFLICT | REVIEW_SOURCE_ARTIFACTS | yes | always send | NEW | metric identity proof |
| AT-015 | missing baseline count | fixture-blocked-missing-baseline | BLOCKED | SOURCE_ARTIFACT_MISSING | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | no silent zero |
| AT-016 | missing current count | fixture-blocked-missing-baseline | BLOCKED | SOURCE_ARTIFACT_MISSING | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | no silent zero |
| AT-017 | explicit zero values | fixture-ok (zeros variant) | OK | NO_ACTION_REQUIRED | NONE | yes | send | NEW | zeros preserved |
| AT-018 | negative metrics | fixture-blocked-metric-conflict | BLOCKED | SOURCE_ARTIFACT_CONFLICT | REVIEW_SOURCE_ARTIFACTS | yes* | always send | NEW | negative evidence |
| AT-019 | unsupported schema major | fixture-blocked-unsupported-schema | BLOCKED | SOURCE_SCHEMA_UNSUPPORTED | REVIEW_SCHEMA_COMPATIBILITY | reject or blocked pub | no unsafe send | n/a | schema gate log |
| AT-020 | future observed_at | fixture-blocked-invalid-time | BLOCKED | SOURCE_TIME_INVALID | REVIEW_SOURCE_TIME | yes* | always send | NEW | skew proof |
| AT-021 | clock skew / invalid time | fixture-blocked-invalid-time | BLOCKED | SOURCE_TIME_INVALID | REVIEW_SOURCE_TIME | yes* | always send | NEW | clock evidence |
| AT-022 | duplicate already sent | fixture-dedupe-repeat | (unchanged facts) | (same) | (same) | n/a | **no second send** | DUPLICATE_ALREADY_SENT | dedupe record |
| AT-023 | duplicate after previous delivery failure | fixture-delivery-retry | (same) | (same) | (same) | n/a | retry send | RETRY_ALLOWED | attempt count |
| AT-024 | Telegram failure | fixture-ok | OK unchanged | NO_ACTION_REQUIRED | NONE | yes | attempt fail | delivery FAILED | delivery isolation |
| AT-025 | AI disabled | any valid | unchanged | unchanged | unchanged | yes | SIMPLE only | n/a | ai_status=DISABLED |
| AT-026 | AI failure fallback | (Phase 2) | unchanged | unchanged | unchanged | yes | SIMPLE remains | n/a | ai_status=FAILED |
| AT-027 | secret marker detected | fixture-security-secret-detected | distribution blocked | ENVELOPE_SECURITY_REJECTED | REVIEW_SOURCE_ARTIFACTS | **no** | **no** | n/a | reject evidence |
| AT-028 | redacted=false | fixture-security-secret-detected | distribution blocked | ENVELOPE_SECURITY_REJECTED | REVIEW_SOURCE_ARTIFACTS | **no** | **no** | n/a | flag evidence |
| AT-029 | contains_secrets=true | fixture-security-secret-detected | distribution blocked | ENVELOPE_SECURITY_REJECTED | REVIEW_SOURCE_ARTIFACTS | **no** | **no** | n/a | flag evidence |
| AT-030 | raw path in action text | fixture-security-secret-detected | distribution blocked | ENVELOPE_SECURITY_REJECTED | REVIEW_SOURCE_ARTIFACTS | **no** | **no** | n/a | path detect |
| AT-031 | oversized payload | synthetic large | reject intake | n/a | n/a | no | no | n/a | size gate |
| AT-032 | unknown source status | synthetic | BLOCKED | SOURCE_SCHEMA_UNSUPPORTED | REVIEW_SCHEMA_COMPATIBILITY | yes* | always send | NEW | vocabulary evidence |

\* “yes*” means a **BLOCKED** distributable envelope may publish when security passes; security failures never publish.

---

## 15. Evidence pack (future implementation)

Minimum:

- source fixture manifest
- normalized envelope
- validation result
- event_id calculation evidence
- atomic publication evidence
- dedupe decision
- formatted SIMPLE message
- Telegram response metadata (sanitized)
- delivery status
- workflow export (sanitized)
- credential references only
- rollback checkpoint
- production mutation count
- Git status
- no-secrets confirmation

No real token, chat ID, or sensitive raw API body may enter Git reports.
