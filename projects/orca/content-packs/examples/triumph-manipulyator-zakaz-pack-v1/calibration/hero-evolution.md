# Calibration — Hero evolution

**Sources:** `calibration/.../hero-drift-analysis-v1.md`, `ux-observations/hero-evolution-v1.md`

## Three generations

| Gen | Artifact | Character |
|-----|----------|-----------|
| G0 | v4 `sections/screen-01-hero.html` | Fleet, fake rate, clutter — **broken** |
| G1 | v4 `v5-ppc/zakaz/screen-01-hero.html` | PPC copy + form + notice |
| G2 | v5 `v5-ppc/zakaz/screen-01-hero.html` | `hero--v5` + lower band — **current** |

## Why G0 failed

- Visual clutter, semantic overload, image competition
- Fake pricing, wrong tonnage, fleet framing
- Weak CTA — no inline form

## Why G2 works

- Focus: H1 → lead → specs → form
- Capability-first <5 sec
- Honest pricing
- Zoned lower band (proof + cargo + notice)

## G1 → G2 changes

| Change | Class |
|--------|-------|
| `hero__lower` zoning | productive |
| Cargo micro-CTAs | productive |
| Notice | present in current repo — verify visibility |
| Proof label simplification | neutral |

## Remaining weaknesses

- Lower band still dense (4+6+notice)
- Six cargo CTAs vs one primary
- Mobile form fold — **UNKNOWN** QA

## ORCA lesson

**Blueprint was right; first Factory hero was wrong.** Calibration must read **workspace as-built**, not only blueprint.
