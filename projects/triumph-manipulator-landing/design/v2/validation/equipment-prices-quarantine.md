# equipment-prices — EXPERIMENTAL / VALIDATION quarantine

**Status:** **NOT canonical** Triumph V2 homepage section (`design/v2/01.png` → `07.png`).  
**Human gate (2026-05-16):** remove from homepage flow — **APPROVED** and **applied** in `workspaces/triumph-manipulator-landing-v2/`.

## What stays true

- **Canonical homepage narrative** follows **`design/v2/`** only: **01** hero → **02** machine → **03** cases → **04** segments → **05** matrix → **06** consultation → **07** footer.
- **Partial + SCSS + assets** for `equipment-prices` remain on disk; **do not delete** without a separate operator decision.

## Where the block lives now

| Artifact | Path |
|----------|------|
| Isolated HTML page | `workspaces/triumph-manipulator-landing-v2/src/pages/validation-equipment-prices.html` |
| Section partial | `workspaces/triumph-manipulator-landing-v2/src/partials/sections/equipment-prices.html` |
| Styles | `workspaces/triumph-manipulator-landing-v2/src/scss/sections/_equipment-prices.scss` (still `@use`’d from `style.scss`) |
| Legacy mirror (non-V2 primary) | `workspaces/triumph-manipulator-landing/src/pages/validation-equipment-prices.html` — same quarantine role for the v1 workspace |

## Allowed uses

- Validation / fleet-mode experiments **off** the homepage.
- Visual or structural review without polluting Screen **01→07** rebuild tasks.
- Future operator decision: rewrite to a V2-backed slice **or** keep as non-homepage fleet concept.

## Forbidden

- Re-`@@include` on **`index.html`** without a **new** written operator gate.
- Treating fleet card copy as **locked** V2 homepage truth.
- Letting fleet semantics **drive** stub fill in `trust-cases-social-proof`, `machine-specs-transport-lists`, `consultation-lead-form`, or `site-footer-v2`.

## Navigation

- V2 **header** does not link to `#park-tehniki` on the homepage (unchanged).
- **Footer** (`footer.html` on `about` / `service`): link «Техника и цены» → `validation-equipment-prices.html` (not `index.html#park-tehniki`).

## Companion docs

- [V2-CLEANUP-DECISION-LOG.md](../../../V2-CLEANUP-DECISION-LOG.md)  
- [V2-SECTION-SOURCE-MATRIX.md](../../../V2-SECTION-SOURCE-MATRIX.md)  
- [V2-VISUAL-SOURCE-MATRIX.md](../../../V2-VISUAL-SOURCE-MATRIX.md)
