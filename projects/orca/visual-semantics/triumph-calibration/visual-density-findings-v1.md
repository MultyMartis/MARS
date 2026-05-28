# Visual Density Findings v1

**Source:** `visual-density-observations-v1.md`

## Hero density map (G2)

| Zone | Elements | Tier |
|------|----------|------|
| Main | H1, lead, 5 specs, form (5 fields) | high |
| Proof | 4 icons | medium |
| Cargo | 6×(title+desc+CTA) | high |

**~20+ messages before scroll** → `visual_density: high`

## What works

- Dark overlay compresses photo noise
- `clamp()` typography
- Single-line spec items
- Form column anchors desktop eye

## What strains

- 6 secondary cargo CTAs
- Duplicate «мин. заказ» (specs + proof)
- Multiple red focal points (geo span + buttons)

## Specs section (screen 2)

- Large portrait + 5-row dl + CTA — effective for «покажите машину»
- Heavy on mobile — stacks image above table

## Pack hints (from calibration)

```yaml
visual_density: high
cargo_cards_max: 6
cargo_cards_max_mobile: 4
proof_strip_mode: operational  # social | ops | hybrid
compactness_level: compact
```

## Productive vs destructive density

| Type | Triumph example |
|------|-----------------|
| Productive | master hot must qualify fast — some density intentional |
| Destructive | G0 everything in one zone without hierarchy |
| Borderline | 6 cargo CTAs without outline style |
