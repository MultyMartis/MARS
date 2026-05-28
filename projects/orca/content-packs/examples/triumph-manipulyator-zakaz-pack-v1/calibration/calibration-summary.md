# Calibration summary — first real Triumph implementation

**Route:** master hot · Аренда манипулятора в Краснодаре  
**As-built:** `triumph-manipulator-landing-v5` zakaz partials

## What ORCA learned

### 1. Semantic content alone is insufficient

Blueprint copy was correct; **visual hierarchy and zoning** determined whether users could use it. G0 failed with right-ish words in wrong layout.

### 2. Visual hierarchy matters

`hero_priority: capability_first` required **layout**, not just bullets in prose. Grid + aside form + lower band = implementation of priority.

### 3. Trust mode matters

Choosing `operational_proof` vs `social_proof` in hero is a **PPC decision**, not decoration. Pack must encode `trust_mode` explicitly.

### 4. Density matters

`visual_density: high` can be **productive** when zoned; **destructive** when flat (G0).

### 5. Hero zoning matters

`hero__main` vs `hero__lower` separation is a first-class semantic field (`hero_layout_mode`).

### 6. Productive drift exists

Factory improved on blueprint in form placement, fleet removal, ops proof — **must be whitelisted** or cleanup reverts wins.

### 7. Destructive drift is often PPC-design

D2 H1 mismatch is not fixed by CSS — needs pack + ads strategy.

### 8. Content packs must carry visual semantics

5-ton pack copy-only gaps listed in `semantic-pack-gaps-v1.md` — this v1 pack closes that for master hot.

### 9. Calibration must diff repo vs docs

D1 notice: calibration doc lag vs partial — **as-built wins** until docs updated.

### 10. Ack flags are honesty

`intent_continuity_ack: false` is correct until operator signs — do not fake in pack gates.

## Feedback loop (new)

```text
workspace src + reports
  → orca/calibration/
  → content-pack (this artifact)
  → factory handoff vNext
```

## Scaling

Use this pack as template for 11 sibling routes — swap `group_id`, partial folder, visual bundle deltas per route calibration.

## Not learned (no data in repo)

- Conversion rates
- Call vs form split
- Live SLA for «30 минут»

See [SAFE-UNKNOWN.md](../SAFE-UNKNOWN.md).
