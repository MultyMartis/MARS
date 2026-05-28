# Hero v2 Requirements — master hot (calibration output)

**Status:** Requirements only — **not** a build charter.  
**Triggers:** After master hot handoff approved OR operator accepts calibration findings.

## Goals

1. Close destructive drift (qualification, multi-ad H1 policy)
2. Preserve productive v5 structure (grid + inline form + bg layer)
3. Encode decisions in content pack — not ad-hoc SCSS

## Layout (retain)

| Zone | Requirement |
|------|-------------|
| `first-screen` | bg `<img>` + overlay (keep) |
| `hero__main` | 2-col desktop; stack mobile per `mobile_hero_cta_order` |
| `hero__aside` | Inline form — keep |
| `hero__lower` | Proof + cargo OR proof + notice + cargo (reordered) |

## Copy locks (from doctrine)

- Specs: 5 т / 3 т / 14 м / 6.2×2.2 / 2 ч — unchanged
- No fleet / no fake rate
- Geo in H1

## v2 changes (required)

| ID | Change | Priority |
|----|--------|----------|
| H2-1 | Restore **qualification line** in `hero__lower` above cargo | P0 |
| H2-2 | Pack-driven **H1** aligned to `primary_ad_variant` | P0 |
| H2-3 | Define `trust_hero_mode`: recommend **hybrid** — 4.9 ★ compact + 2 ops items max | P1 |
| H2-4 | Cap cargo cards at **4** on mobile, 6 desktop OR 4 all | P1 |
| H2-5 | `mobile_hero_cta_order`: `call` then `form` when instance call-first | P0 |
| H2-6 | Single primary red CTA — cargo uses outline/ghost style | P2 |

## Optional experiments (operator-only)

- Sticky mobile bar (tel + form)
- Collapse proof strip into 2 items
- Move reviews snippet into hero (one line, no invented text)

## Acceptance checks

- [ ] A1 and A2 ads each have documented H1 continuity strategy
- [ ] Qualification visible without scrolling on 390px **or** sticky notice
- [ ] No placeholder form handler on production
- [ ] Semantic lock fields in pack match HTML

## Do not

- Reintroduce v4 fleet hero
- Add hero hourly price
- Add second H1
