# FW-SK-11 — WordPress Validation v1

**Skill ID:** FW-SK-11  
**Stage:** FW-04 capability

## Purpose
Execute structural and functional validation chain on WordPress implementation.

## When to use
- After FW-SK-10 implementation complete
- Before release packaging

## Prerequisites
- Implementation artifacts present
- Validation plan from FW-SK-09
- Validator profiles FW-V-01–04 available

## Inputs
- Theme and plugin code
- Validation plan
- Local WordPress URL (when env available)

## Outputs
- Validation report(s) per FW-T
- Pass/fail per WV level attempted
- Blocker list

## Procedure
1. Load validation plan and FW-S-08.
2. Run architecture validator (FW-V-01) — independent pass preferred.
3. Run code quality/security validator (FW-V-02).
4. Run WordPress correctness validator (FW-V-03).
5. Run functional validator (FW-V-04) — menus, forms, CPT archives.
6. Record evidence paths (command output, screenshots).
7. Do **not** self-approve WV6 — defer to FW-SK-12.
8. Escalate blockers per independence policy.

## Standards used
- FW-S-08 Validation Standard
- Validation runner architecture (design)
- Validator independence policy

## Allowed tools
- PHPCS, PHPStan if configured, WP-CLI read-only checks
- Local HTTP fetch for smoke tests
- Playwright if configured (FW-05+)

## Forbidden actions
- Marking WV6 pass without operator
- Rewriting code during validation pass
- Production URL testing

## Validation
- All planned WV levels attempted or marked SAFE UNKNOWN with reason
- Independent pass documented

## Human gate
Operator reviews blocker resolution.

## Stop conditions
- Blocking validator failure unresolved
- Local env unavailable when required — report PARTIAL

## Report format
```text
# REPORT — Forge WordPress Validation Pass
## Per-validator verdicts
## Blockers
## WV6 status: DEFERRED to FW-SK-12
```
