# Validation Summary v1

**CLI:** `tools/validation-cli` (Hardening v0.1)  
**Input:** `schema/instances/triumph-s-tier-draft-v1.json`  
**Report:** `tools/validation-cli/output/validation-report.output.json`

## Result

| Metric | Value |
|--------|--------|
| Status | `passed` |
| export_allowed | `true` |
| Blocking errors | 0 |
| Warnings | 0 |
| Rule evaluations | 276 pass / 0 warn / 0 fail |
| launch_allowed | `null` (human-only by design) |

## Rules exercised (subset)

Structural: ST-01, ST-02  
Symbol: SY-01–SY-04 (headlines, description, fastlinks, callouts)  
Semantic: SE-05 (primary keyword in H1), SE-07, SE-08  
Landing: LM-01, LM-02  
Commercial: CM-02  
Survivability: SV-03, SV-04, SV-05  

## Schema

- Input: `orca-ppc-document-v1.schema.json` — valid  
- Output report: `validation-report-v1.schema.json` — valid  

## Operator note

Validation proves **export prep survivability**, not Commander import success or live campaign performance. Warnings policy: none triggered; no validator weakening applied.
