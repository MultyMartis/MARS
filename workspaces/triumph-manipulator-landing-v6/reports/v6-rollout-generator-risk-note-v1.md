# V6 Rollout Generator Risk Note (v1)

## Status

`tools/generate-ppc-rollout.mjs` is present but not approved as production rollout source.

## Why this is risky now

- Generator content still reflects legacy assumptions from earlier rollout phases.
- It can reintroduce forbidden patterns (`.hero__notice`, legacy partial structures).
- It can leak non-production ORCA/internal operational language into landing copy.
- It does not enforce current V6 admission/parity gates.

## Current source of truth

- `projects/triumph-manipulator-landing/V6-ROUTE-ROLLOUT-CHECKLIST.md`
- `projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md` (hardening section)
- `projects/triumph-manipulator-landing/V6-CSS-SCOPE-ADMISSION-MAP.md`

## Operational note

Use manual, route-by-route rollout with parity and CSS scope admission checks until generator hardening is explicitly completed and approved.
