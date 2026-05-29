# Compactness Schema v0

## `compactness_level`

| Value | ORCA output style | Factory pattern |
|-------|-------------------|-----------------|
| `airy` | Short hero, fewer bullets | Large type, whitespace |
| `standard` | Default blueprint | Mixed |
| `compact` | Icon spec lines, tight lead | v5 spec list |
| `dense` | Many chips/cards in lower band | `hero__lower` cargo grid |

## Route guidance (Triumph scaling)

| Route type | Typical |
|------------|---------|
| master_hot | `compact` main + `dense` lower |
| use_case | `compact` |
| b2b | `standard` — more legal copy |

## Mobile downgrade

Unless pack overrides: on ≤760px treat `dense` as `high` `visual_noise_risk`.

## Triumph

```yaml
compactness_level: compact  # hero__main
# implicit dense in hero__lower — document via visual_density: high
```
