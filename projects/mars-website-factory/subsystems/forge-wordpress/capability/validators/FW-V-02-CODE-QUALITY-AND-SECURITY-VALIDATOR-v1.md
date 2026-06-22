# FW-V-02 — Code Quality and Security Validator v1

**Validator ID:** FW-V-02  
**Independence:** **Required** — implementer must not self-approve

## Input artifacts
- All PHP files in theme and functionality plugin
- PHPCS output
- Implementation spec
- FW-S-07 coding standard

## Checks
| ID | Check | Blocking |
|----|-------|----------|
| Q-01 | PHPCS run — no blocking errors | Yes |
| Q-02 | Output escaping in templates | Yes |
| Q-03 | Input sanitization on save | Yes |
| Q-04 | Nonces on forms/AJAX | Yes |
| Q-05 | Capability checks on admin actions | Yes |
| Q-06 | No hardcoded secrets | Yes |
| Q-07 | No `eval`, unsafe `include`, direct SQL | Yes |
| Q-08 | Prepared statements if custom DB (discouraged) | Yes |
| Q-09 | ABSPATH guard in PHP files | Yes |

## Blocking findings
Any Q-01–Q-09 fail → **FAIL**

## Non-blocking findings
PHPCS warnings, missing docblocks, minor WPCS style

## Independence requirement
Security pass **must not** be issued by same pass that wrote the code.

## Report format
```text
# REPORT — FW-V-02 Code Quality and Security — <project>
## PHPCS summary
## Security checklist
## Verdict
```

## Pass/fail rules
- **PASS:** No blocking security/quality issues
- **FAIL:** Any blocking issue

## Human escalation
Security FAIL → STOP release; operator review mandatory
