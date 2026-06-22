# FW-V-07 — Release and Handoff Validator v1

**Validator ID:** FW-V-07

## Input artifacts
- Release manifest
- Package contents listing
- Validation report bundle
- FW-C-03 handoff draft
- Plugin register

## Checks
| ID | Check | Blocking |
|----|-------|----------|
| R-01 | All validation blockers closed or waived | Yes |
| R-02 | WV6 operator approval on record | Yes |
| R-03 | Package excludes core/vendor/uploads/secrets | Yes |
| R-04 | Manifest matches package | Yes |
| R-05 | Plugin dependencies listed | Yes |
| R-06 | FW-C-03 handoff fields complete | Yes |
| R-07 | Install/rollback notes present | Yes |
| R-08 | No production credentials in package | Yes |

## Blocking findings
Any R-01–R-08 fail → **FAIL**

## Non-blocking findings
Missing optional README sections

## Independence requirement
Separate pass from implementer before handoff submission.

## Report format
```text
# REPORT — FW-V-07 Release and Handoff — <project>
## Manifest audit
## Handoff contract checklist
## Verdict
```

## Pass/fail rules
- **PASS:** All blocking checks pass
- **FAIL:** Any blocking check fails

## Human escalation
Handoff FAIL → operator; WPilot reviewer for acceptance (separate from R-06)
