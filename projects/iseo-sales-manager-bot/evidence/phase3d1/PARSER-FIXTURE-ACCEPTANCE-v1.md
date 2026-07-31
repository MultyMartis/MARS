# PARSER-FIXTURE-ACCEPTANCE-v1

**Phase:** 3D.1  
**Harness:** `implementation/parser-fixtures/run-fixture-suite.mjs`  
**Library:** `implementation/parser-fixtures/parse-lead-lib.mjs`

## Results

| ID | Title | Pass |
|----|-------|------|
| F-AF01 | multiline audit form with phone | PASS |
| F-AF02 | collapsed single-line audit form with phone | PASS |
| F-AF03 | audit form with email | PASS |
| F-AF04 | audit form with Telegram | PASS |
| F-AF05 | optional spaces / NBSP | PASS |
| F-AF06 | reordered optional fields | PASS |
| F-AF07 | missing name but valid phone/site | PASS |
| F-AF08 | valid name/contact missing site | PASS |
| F-AF09 | malformed contact | PASS |
| F-AF10 | previous accepted lead format regression | PASS |
| F-AF11 | special characters | PASS |
| F-AF12 | duplicated quoted email content | PASS |

**Score:** 12 / 12 PASS

## Gates

- No greedy end-of-message field capture across next labels
- No field value includes the next field label
- Pre-parsed synthetic fields still honored (regression)

Machine result copy: `evidence/phase3d1/PARSER-FIXTURE-RESULTS.json`
