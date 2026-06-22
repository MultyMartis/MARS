# FW-V-06 — Admin UX Validator v1

**Validator ID:** FW-V-06

## Input artifacts
- Admin UX map
- ACF field groups (JSON + admin screenshots if available)
- Options page config
- CPT admin labels

## Checks
| ID | Check | Blocking |
|----|-------|----------|
| U-01 | All editable regions reachable in admin | Yes |
| U-02 | Field labels human-readable | Non-blocking |
| U-03 | Field order matches visual top-to-bottom | Non-blocking |
| U-04 | No exposed technical keys to editor | Non-blocking |
| U-05 | Options vs page fields correctly separated | Yes |
| U-06 | Featured image usage documented | Non-blocking |

## Blocking findings
U-01, U-05 fail → **FAIL**

## Non-blocking findings
U-02–U-04, U-06

## Independence requirement
Operator or designated editor review for U-02–U-03.

## Report format
```text
# REPORT — FW-V-06 Admin UX — <project>
## Editor workflow checklist
## Verdict
```

## Pass/fail rules
- **PASS:** Blocking checks pass
- **FAIL:** Editor cannot reach required content

## Human escalation
Editor confusion → FW-SK-08 revision
