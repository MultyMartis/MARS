# Visual Density Schema v0

## `visual_density`

| Value | Hero message budget (all zones) |
|-------|--------------------------------|
| `low` | ≤8 |
| `medium` | 9–14 |
| `high` | 15–20 |
| `overloaded` | 21+ without zoning plan |

## `visual_noise_risk`

| Value | Condition |
|-------|-----------|
| `low` | Single focal red CTA |
| `medium` | 2 focal areas |
| `high` | proof + cargo + form accents |
| `critical` | fake price + fleet + 6 features (G0) |

## `cargo_cards_max` (vNext optional)

| Context | Calibration proposal |
|---------|---------------------|
| desktop | 6 |
| mobile | 4 |

## Density warning trigger

Set `visual_noise_risk: high` or `critical` when:

- `cargo_cards` > 4 **and** `hero_proof` > 3 **and** inline form **and** 5 specs

Triumph zakaz: `visual_density: high`, `visual_noise_risk: high`.

## Operator override

```yaml
visual_density: high
density_override:
  reason: "master_hot broad qualification"
  signed_by: "<operator>"
```

## SAFE UNKNOWN

Automated element counting — not implemented.
