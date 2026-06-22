# FW-V-01 — Architecture Validator v1

**Validator ID:** FW-V-01  
**Independence:** Required — separate from implementer for final pass

## Input artifacts
- WAD
- Theme architecture doc
- Content model
- Block-to-WP map
- Implementation spec
- Theme/plugin directory structure (if code exists)

## Checks
| ID | Check | Blocking |
|----|-------|----------|
| A-01 | WAD exists and approved | Yes |
| A-02 | Theme/plugin boundary matches WAD | Yes |
| A-03 | Template hierarchy covers all page types | Yes |
| A-04 | No business logic bloat in `functions.php` | Yes |
| A-05 | CPT design matches content model | Yes |
| A-06 | Plugin register aligns with WAD | Non-blocking if draft |
| A-07 | No scope creep vs intake | Yes |

## Blocking findings
Any A-01–A-05, A-07 fail → **FAIL**

## Non-blocking findings
Documentation gaps, minor naming inconsistencies

## Independence requirement
Implementer may not mark architecture PASS on own implementation without separate review pass.

## Report format
```text
# REPORT — FW-V-01 Architecture Validator — <project>
## Verdict: PASS | FAIL
## Findings table
```

## Pass/fail rules
- **PASS:** All blocking checks pass
- **FAIL:** Any blocking check fails

## Human escalation
Architecture FAIL → operator + WAD revision before further implementation
