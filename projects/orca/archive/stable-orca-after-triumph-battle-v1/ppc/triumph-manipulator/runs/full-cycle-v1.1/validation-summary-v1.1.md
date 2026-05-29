# Validation Summary v1.1

**CLI:** `tools/validation-cli` (Hardening v0.1)  
**Input:** `schema/instances/triumph-s-tier-draft-v1.json`  
**Report:** `tools/validation-cli/output/validation-report.output.json`

## Result

| Metric | v1 | v1.1 |
|--------|-----|------|
| Status | passed | **passed** |
| export_allowed | true | **true** |
| Blocking errors | 0 | **0** |
| Warnings | 0 | **0** |
| Rule evaluations | 276 pass | **345 pass** |
| launch_allowed | null | null |

## Delta vs v1

- +2 groups, +4 ads, +13 keywords → additional structural/semantic/landing rule coverage.
- Initial draft used `master_hot` / `medium` cross_intent_risk — corrected to schema enums (`hot_general`, `low`) before export.

## Operator note

Validation proves **export prep survivability**, not Commander import success or live campaign performance.
