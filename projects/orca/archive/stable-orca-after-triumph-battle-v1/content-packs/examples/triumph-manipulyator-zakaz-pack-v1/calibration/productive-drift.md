# Calibration — Productive drift

**Source:** `projects/orca/visual-semantics/triumph-calibration/productive-drift-findings-v1.md`  
**Definition:** improves hierarchy, clarity, honesty without breaking PPC locks.

## P1 — Inline hero form

- G0 scroll-to-CTA → `hero__aside` form
- Fields: `cta_priority: form`, `hero_layout_mode: grid_form_aside`

## P2 — Compact capability list

- 6 paragraphs → 5 icon spec lines
- Fields: `compactness_level: compact`, `hero_priority: capability_first`

## P3 — v5 visual system

- `first-screen` bg + gradient — reduced `visual_noise_risk` vs G0

## P4 — Cargo cards

- Interactive task CTAs — accept with mobile cap

## P5 — Lower band zoning

- `hero__lower` proof + cargo — enables zoned high density

## P6 — Fleet / fake price removal

- G0 destructive signals removed — `one_machine` restored

## P7 — Operational proof strip

- vs blueprint social strip — hot intent alignment

## P8 — Reviews below fold

- social layer preserved in trust section

## Pack encoding

```yaml
drift_acceptance:
  productive:
    - inline_hero_form
    - compact_spec_list
    - v5_bg_overlay
    - cargo_cards_v5
    - hero_lower_zoning
    - fleet_fake_price_removed
    - operational_hero_proof
```

**ORCA lesson:** Factory drift can be **more correct** than blueprint text if calibration captures it.
