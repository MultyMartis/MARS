# CORVONERO RUN 004 — PHASE 3 CANARY REVIEW PACKAGE v1

**Run ID:** `corv-semantic-v2-20260626-004`  
**Verdict:** `FAILED`

## Verdict distribution

- **ACCEPT:** 32 (26.7%)
- **REJECT:** 59 (49.2%)
- **ABSTAIN:** 29 (24.2%)

## Error-family analysis

### platform_mismatch
- Affected: 0
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### generic_erp_ambiguity
- Affected: 8
- Unexpected vs pre-auth: 2
- Severity: non_blocking_review
- Recommendation: Monitor — no broad pattern detected

### product_license_vs_service
- Affected: 12
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### product_plus_service_bundles
- Affected: 3
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### informational_self_service
- Affected: 12
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### ambiguous_diy_problems
- Affected: 0
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### direct_problem_demand
- Affected: 15
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### integrations
- Affected: 10
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### marking_chestny_znak
- Affected: 8
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### ts_piot
- Affected: 5
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### careers_training
- Affected: 8
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected

### geography
- Affected: 16
- Unexpected vs pre-auth: 0
- Severity: none
- Recommendation: Monitor — no broad pattern detected


## Operator decisions required

1. Review PSR-AMB-01 family ACCEPT instances (if any).
2. Review 0 false accepts and 12 false rejects on pre-authorized items.
3. Authorize or deny Phase 4 full-corpus task separately.

**Wave 5, strategy, Campaign Architecture, Commander, import, launch: BLOCKED**
