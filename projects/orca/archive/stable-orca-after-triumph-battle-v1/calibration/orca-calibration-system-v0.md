# ORCA Calibration System v0

## Status

**Documentation only** — first loop anchored on Triumph master hot landing (`Аренда манипулятора в Краснодаре`).

## Purpose

Calibration closes the gap between:

1. **ORCA research** — intent tiers, blueprints, campaign instance
2. **ORCA semantic packs** — section contracts, locks, factory notes
3. **PPC continuity** — ad headlines, callouts, display paths
4. **Website Factory** — HTML partials, SCSS, build reports
5. **Operational review** — human QA, drift classification, next pack requirements

Without calibration, each lane optimizes locally (copy vs layout vs ads) and **semantic debt** accumulates in production.

## Calibration loop (v0)

```text
ORCA blueprint / pack
        ↓
   handoff (if exists)
        ↓
   Factory build (workspace)
        ↓
   CALIBRATION PASS  ← this layer
        ↓
   findings → pack vNext / hero v2 / scaling rules
```

## Outputs per pass

| Output type | Example location |
|-------------|------------------|
| As-built state | `current-state/` |
| Drift analysis | `drift-analysis/` |
| UX observations | `ux-observations/` |
| Factory lessons | `implementation-findings/` |
| PPC alignment | `ppc-alignment/` |
| Evolution requirements | `next-evolution/` |

## Drift philosophy

Not all implementation change is error.

| Class | Meaning |
|-------|---------|
| **Productive evolution** | Factory improved UX / conversion path while preserving intent locks |
| **Destructive drift** | Lost PPC continuity, broke semantic lock, invented claims |
| **Neutral presentation** | Layout/typography within allowed Factory layer |

See [semantic-drift-rules-v0.md](semantic-drift-rules-v0.md).

## Relationship to semantic lock

[orca-website-factory-semantic-lock-v0.md](../intelligence/orca-website-factory-semantic-lock-v0.md) defines **what must not change** in MODE 1.

Calibration records **what actually changed** after production — including allowed presentation moves that still affect PPC feel (hero density, trust placement, CTA weight).

## Non-goals

- Automated diff bots as product
- Conversion rate claims without measured data
- Replacing `approved_for_ads` human sign-off

## First canonical case

**Triumph — master hot / group 12** — see [triumph-manipulator/README.md](triumph-manipulator/README.md).

Evidence date for v0 pass: **2026-05-28** (repo snapshot).
