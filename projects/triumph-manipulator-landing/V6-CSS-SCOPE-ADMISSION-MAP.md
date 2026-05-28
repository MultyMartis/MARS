# V6 CSS Scope Admission Map

Purpose: track which routes are admitted into canonical route-scoped CSS, and flag rollout risks early.

## Admission table

| Route | `body[data-page-type]` | Status | Admitted selectors | Notes |
|---|---|---|---|---|
| zakaz | `ppc-zakaz-manip` | Canonical baseline | `_v5-machine-showcase.scss` explicit route scope groups; shared `body[data-page-type^='ppc-']` groups | Source-of-truth baseline route |
| 5-tonn | `ppc-5-tonn` | Admitted (calibration) | `_v5-machine-showcase.scss` explicit route scope groups for ops-grid/showcase blocks | Added after calibration mismatch |

## Current explicit route-scoped selector groups (audit)

From current V6 SCSS audit in `workspaces/triumph-manipulator-landing-v6/src/scss/sections/`:

- `_v5-machine-showcase.scss` contains explicit grouped scopes:
  - `body[data-page-type='ppc-zakaz-manip'], body[data-page-type='ppc-5-tonn'] { ... }`
  - Repeated for machine-showcase / machine-transport responsive and section variants.
- Shared selectors with `body[data-page-type^='ppc-']` exist in:
  - `_v5-hero-extensions.scss`
  - `_v5-page01-overrides.scss`
  - These are generic PPC scopes (not per-route admission lists).

## Future rollout risk

- Any canonical style still scoped only to `ppc-zakaz-manip` is a rollout risk and requires explicit admission for each new route.
- HTML parity is insufficient when CSS admission is incomplete; route rollout must include selector-group admission checks.
- This map is a tracking artifact only; do not mass-admit future routes until each route is actively in rollout.
