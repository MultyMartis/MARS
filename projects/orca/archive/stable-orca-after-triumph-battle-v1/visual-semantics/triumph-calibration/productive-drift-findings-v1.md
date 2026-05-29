# Productive Drift Findings v1

**Definition:** Factory or operator changes that **improve** hierarchy, clarity, compactness, or honesty without breaking PPC locks.

**ORCA must encode** these in `drift_acceptance.productive` so cleanup passes do not revert them.

## P1 — Inline hero form

- **Was:** scroll-to-CTA pattern (G0)
- **Now:** `hero__aside` form
- **Fields:** `cta_priority: form`, `hero_layout_mode: grid_form_aside`

## P2 — Capability bullets as compact list

- **Was:** 6 paragraph features
- **Now:** 5 icon/line specs
- **Fields:** `compactness_level: compact`, `hero_priority: capability_first`

## P3 — v5 visual system (bg + overlay)

- **Was:** busy composite, competing visual note
- **Now:** `first-screen` bg img + gradient
- **Fields:** reduced `visual_noise_risk` vs G0

## P4 — Cargo cards with micro-CTA

- **Was:** static chips (blueprint)
- **Now:** 6 interactive cards «Заказать перевозку»
- **Fields:** `semantic_focus: use_case_fit` — accept with `cargo_cards_max` cap

## P5 — Lower band zoning

- **Was:** single competing block
- **Now:** `hero__lower` proof + cargo
- **Fields:** enables `visual_density: high` without `critical`

## P6 — Fleet / fake price removal

- **Was:** G0 destructive signals
- **Now:** absent
- **Fields:** `semantic_focus: one_machine` restored

## P7 — Operational proof strip

- **Was:** blueprint social strip not implemented
- **Now:** ops facts above fold
- **Fields:** `trust_mode: operational_proof` — **ambiguous** vs blueprint but **productive** for hot intent (operator may reclassify to `hybrid_proof`)

## P8 — Reviews preserved below fold

- **Fields:** `proof_priority: below_fold` for social layer — locks preserved

## Pack template

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
