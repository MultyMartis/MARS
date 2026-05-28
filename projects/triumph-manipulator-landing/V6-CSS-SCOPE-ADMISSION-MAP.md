# V6 CSS Scope Admission Map

Purpose: track which routes are admitted into canonical route-scoped CSS, and flag rollout risks early.

## Admission table

| Route | `body[data-page-type]` | Status | Admitted selectors | Notes |
|---|---|---|---|---|
| zakaz | `ppc-zakaz-manip` | Canonical baseline | `_v5-machine-showcase.scss` explicit route scope groups; shared `body[data-page-type^='ppc-']` groups | Source-of-truth baseline route |
| 5-tonn | `ppc-5-tonn` | Admitted (calibration) | `_v5-machine-showcase.scss` explicit route scope groups for ops-grid/showcase blocks | Added after calibration mismatch |
| bytovki | `ppc-bytovki` | Admitted | `_v5-machine-showcase.scss` explicit route scope groups for `machine-showcase--ops-panel` and `machine-transport--ops-grid` (all responsive groups) | Added during second calibration rollout; no global scope broadening |
| konteynery | `ppc-konteynery` | admitted | `_v5-machine-showcase.scss` grouped route scope selectors for `machine-showcase--ops-panel` + `machine-transport--ops-grid` across base and responsive blocks | Added during V6 konteynery rollout; no global scope broadening |

## Current explicit route-scoped selector groups (audit)

From current V6 SCSS audit in `workspaces/triumph-manipulator-landing-v6/src/scss/sections/`:

- `_v5-machine-showcase.scss` contains explicit grouped scopes:
  - `body[data-page-type='ppc-zakaz-manip'], body[data-page-type='ppc-5-tonn'], body[data-page-type='ppc-bytovki'] { ... }`
  - Repeated for machine-showcase / machine-transport responsive and section variants.
- Shared selectors with `body[data-page-type^='ppc-']` exist in:
  - `_v5-hero-extensions.scss`
  - `_v5-page01-overrides.scss`
  - These are generic PPC scopes (not per-route admission lists).

## Future rollout risk

- Any canonical style still scoped only to `ppc-zakaz-manip` is a rollout risk and requires explicit admission for each new route.
- HTML parity is insufficient when CSS admission is incomplete; route rollout must include selector-group admission checks.
- This map is a tracking artifact only; do not mass-admit future routes until each route is actively in rollout.

## KNOWN HIGH-RISK AREA

- route-scoped selector groups
- any canonical selector scoped only to `ppc-zakaz-manip` is rollout-risk
- every new route requires explicit admission audit

## Bytovki calibration findings

- parity issue was CSS scope, not HTML structure
- grouped selector admission solved issue safely
