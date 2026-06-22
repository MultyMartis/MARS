# FW-V-04 — Functional Validator v1

**Validator ID:** FW-V-04

## Input artifacts
- Local WordPress URL
- Content model
- Menu locations plan
- Form configuration
- CPT archive URLs

## Checks
| ID | Check | Blocking |
|----|-------|----------|
| F-01 | Homepage renders | Yes |
| F-02 | All page templates reachable | Yes |
| F-03 | CPT archive and single work | Yes (if CPT) |
| F-04 | Menus assign and display | Yes |
| F-05 | Options page saves (ACF) | Yes (if options) |
| F-06 | Contact form submits locally | Non-blocking if stub |
| F-07 | FAQ accordion/interaction works | Non-blocking |
| F-08 | 404 template exists | Non-blocking |

## Blocking findings
F-01–F-05 fail (when feature in scope) → **FAIL**

## Non-blocking findings
F-06–F-08

## Independence requirement
Functional smoke by independent pass when possible.

## Report format
```text
# REPORT — FW-V-04 Functional Validator — <project>
## URL checklist
## Verdict
```

## Pass/fail rules
- **PASS:** All in-scope blocking features work
- **PARTIAL:** Env unavailable — document SAFE UNKNOWN

## Human escalation
Form/integration failures → operator decision on stub vs live
