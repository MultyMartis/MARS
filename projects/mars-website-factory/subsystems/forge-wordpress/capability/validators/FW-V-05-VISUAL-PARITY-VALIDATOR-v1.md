# FW-V-05 — Visual Parity Validator v1

**Validator ID:** FW-V-05  
**Independence:** **Required** — ties to WV6 operator gate

## Input artifacts
- FW-SK-12 visual comparison report
- Frontend baselines
- Local WP screenshots
- Documented deviations

## Checks
| ID | Check | Blocking |
|----|-------|----------|
| V-01 | All in-scope pages compared | Yes |
| V-02 | Desktop viewport compared | Yes |
| V-03 | Mobile viewport compared | Yes |
| V-04 | Blocking deviations resolved or waived | Yes |
| V-05 | Operator visual approval recorded | Yes |
| V-06 | No uninvented design elements | Yes |

## Blocking findings
V-01–V-06 fail → **FAIL**

## Non-blocking findings
Minor sub-pixel differences with operator waiver

## Independence requirement
Implementer **must not** approve V-05. Operator only.

## Report format
```text
# REPORT — FW-V-05 Visual Parity — <project>
## Comparison matrix
## Operator approval evidence
## Verdict: RECOMMEND PASS | FAIL (pending operator)
```

## Pass/fail rules
- **PASS:** V-05 operator APPROVED + no blocking deviations
- **FAIL:** Missing comparison or operator rejection

## Human escalation
Always — operator visual approval is mandatory for WV6
