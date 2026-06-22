# FW-V-03 — WordPress Correctness Validator v1

**Validator ID:** FW-V-03

## Input artifacts
- Theme files (style.css header, templates)
- Plugin bootstrap
- CPT/taxonomy registration
- ACF JSON sync path
- Local WP instance (when available)

## Checks
| ID | Check | Blocking |
|----|-------|----------|
| W-01 | `style.css` theme header valid | Yes |
| W-02 | Template hierarchy files exist per map | Yes |
| W-03 | CPT registers on `init` — correct args | Yes |
| W-04 | ACF JSON loads/syncs | Yes (if ACF used) |
| W-05 | Enqueue handles — no duplicate conflicts | Non-blocking |
| W-06 | Text domain consistent | Non-blocking |
| W-07 | Permalink flush noted in handoff | Non-blocking |
| W-08 | No PHP fatals on front page load | Yes (when env up) |

## Blocking findings
W-01–W-04, W-08 fail → **FAIL**

## Non-blocking findings
W-05–W-07

## Independence requirement
Separate pass recommended; implementer self-check allowed for W-01–W-04 only.

## Report format
```text
# REPORT — FW-V-03 WordPress Correctness — <project>
## Template/CPT/ACF checks
## Runtime smoke (if available)
## Verdict
```

## Pass/fail rules
- **PASS:** Blocking checks pass; W-08 PASS or SAFE UNKNOWN with env note
- **FAIL:** Blocking check fails

## Human escalation
W-08 SAFE UNKNOWN when no local env → FW-05 dependency
