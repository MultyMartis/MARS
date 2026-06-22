# FW-SK-01 — Frontend Package Inspection v1

**Skill ID:** FW-SK-01  
**Stage:** FW-04 capability

## Purpose
Verify approved Website Factory frontend package completeness before WordPress work begins.

## When to use
- First task on any Forge WordPress project
- After frontend revision — re-inspection required
- Before WAD or content model

## Prerequisites
- Operator-declared frontend approval
- FW-C-01 handoff contract loaded

## Inputs
- Handoff manifest
- Frontend build output (`dist/` or equivalent)
- Block/section inventory if available
- Asset manifest

## Outputs
- Inspection checklist (pass/fail per FW-C-01 requirement)
- Missing artifact list
- Block inventory summary
- STOP/BLOCK recommendation if incomplete

## Procedure
1. Load FW-C-01 and handoff template requirements.
2. Verify manifest exists and matches frontend path.
3. List pages, templates, global partials (header/footer).
4. Verify assets: CSS, JS, fonts, images, SVG — no placeholder policy per Factory rules.
5. Record responsive evidence (desktop/mobile breakpoints present in source).
6. Check production_mode if declared in passport.
7. Produce checklist with PASS / FAIL / PARTIAL per section.
8. If FAIL on blocking item — **STOP**; do not proceed to architecture.

## Standards used
- FW-C-01 Website Factory to Forge WordPress Handoff
- FW-T frontend handoff template

## Allowed tools
- Read filesystem, `npm run build` (read-only verify), grep, list directories
- No frontend edits

## Forbidden actions
- Editing frontend source
- Assuming approval without operator record
- Skipping manifest check

## Validation
- Every FW-C-01 mandatory field addressed in checklist
- Missing items listed as SAFE UNKNOWN with verification path

## Human gate
Operator confirms frontend approval status if not explicit in intake.

## Stop conditions
- No handoff manifest
- Frontend path missing or empty build
- Operator has not approved frontend

## Report format
```text
# REPORT — Forge WordPress Frontend Package Inspection
## Handoff checklist
## Block inventory
## Missing / blocking items
## Recommendation: PROCEED | STOP
```
