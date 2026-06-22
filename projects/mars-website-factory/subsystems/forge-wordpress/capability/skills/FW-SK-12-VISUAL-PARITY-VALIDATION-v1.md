# FW-SK-12 — Visual Parity Validation v1

**Skill ID:** FW-SK-12  
**Stage:** FW-04 capability

## Purpose
Compare local WordPress rendering against approved frontend baselines for visual parity.

## When to use
- After functional validation
- Before release candidate approval

## Prerequisites
- Local WordPress serving implementation
- Approved frontend baselines (screenshots or live static build)
- FW-V-05 validator profile

## Inputs
- Frontend reference URLs or screenshot set
- Local WP URLs per page template
- Viewport list: desktop + mobile minimum

## Outputs
- Visual comparison report
- Diff artifacts (screenshots, notes)
- Parity verdict: **recommendation only** — not final PASS

## Procedure
1. Define page list matching frontend inventory.
2. Capture or compare at agreed viewports (1024+, mobile ≤1024).
3. Compare: layout, typography, spacing, colors, assets.
4. Document every deviation with screenshot reference.
5. Classify: blocking | non-blocking | intentional (documented).
6. Run FW-V-05 independent review.
7. Submit to **operator for visual approval** — implementer must not mark PASS.

## Standards used
- Visual regression design doc
- FW-V-05 Visual Parity Validator
- Operator visual approval law (Factory)

## Allowed tools
- Playwright, manual screenshot, visual diff tools if configured

## Forbidden actions
- Implementer self-approving WV6
- Changing frontend source to "fix" WP
- Inventing design fixes without operator approval

## Validation
- All in-scope pages compared or marked SAFE UNKNOWN
- FW-V-05 report complete

## Human gate
**BLOCKING** — operator visual approval required for WV6 PASS.

## Stop conditions
- Local WP not available
- No frontend baseline
- Operator rejects parity

## Report format
```text
# REPORT — Forge WordPress Visual Parity Comparison
## Page comparison matrix
## Deviations
## Operator approval: PENDING | APPROVED | REJECTED
```
