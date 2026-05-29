# Factory — Allowed drift

Changes Factory or operator may make **without** pack version bump **if** semantics unchanged.

## Visual / layout

- Improved hero zoning (`hero__lower` rhythm, gaps)
- Compact specs presentation (icon size, grid)
- Productive visual hierarchy (proof before cargo or reverse within lower band)
- Proof relocation within hero lower band
- Density reduction (spacing, typography clamp)
- v5 bg overlay strength
- Cargo card ghost/outline styling
- Mobile: hide 2 cargo cards; collapse proof to 2 items
- Image swap with same operational meaning

## Copy-preserving UX

- `data-cta-source` additions for analytics
- Form endpoint wiring (production) — not copy change
- nbsp typography fixes per workspace reports

## Productive semantic-adjacent (document in pack changelog)

- Operational proof strip instead of ★ in hero (already as-built)
- «Рассчитать» vs blueprint «Узнать» — accepted lexical drift
- Interactive cargo cards vs static chips

## Encode in pack

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
    - hero_notice_retained_or_relocated_in_lower
```

## Requires pack amendment

- Any machine spec number change
- H1 strategy change
- New cargo type or denied rule
- New pricing claim
