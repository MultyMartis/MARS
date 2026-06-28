# CORVONERO RUN 004 — CANARY ATTEMPT 1 FAILURE ACCEPTANCE v1

**Run ID:** `corv-semantic-v2-20260626-004`  
**Attempt ID:** `corv-run004-phase3-canary-attempt-001`  
**Operator decision:** ACCEPTED (harness failure)

## Failure accepted as harness failure

Attempt 1 failed with `CANARY_CLASSIFIER_EXPECTATION_POLICY_FAILURE`. The canary support layer (family classifier and expectation-policy assignment) incorrectly marked career, education, and informational phrases as `direct_commercial_1c_service` with `expected_verdict: ACCEPT`. ORCA correctly rejected these phrases.

## ORCA regression

**NOT CONFIRMED.** No evidence of ORCA production regression. Failure is isolated to the canary harness expectation policy.

## Full corpus

**Remains BLOCKED.** Full-corpus processing is not authorized pending successful Attempt 2 and operator review.

## Attempt 2

**Required.** Operator authorized classifier repair and deterministic Attempt 2 with 120 newly selected phrases.

## Attempt 1 immutability

Attempt 1 outputs remain immutable evidence:

- `CORVONERO-RUN-004-PHASE-3-CANARY-SELECTION-v1.json`
- `CORVONERO-RUN-004-PHASE-3-CANARY-RESULT-v1.json`
- `CORVONERO-RUN-004-PHASE-3-CANARY-REVIEW-PACKAGE-v1.json`
- `REPORT-corvonero-run-004-phase-3-canary-v1.md`

Do not overwrite, change verdict, change selection, or reinterpret labels as canonical truth.
