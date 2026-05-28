# Visual Semantic Fields for Content Pack v1

**Target:** bind v0 fields to `projects/orca/content-packs/` front-matter.

## Proposed pack front-matter block

```yaml
visual_semantics:
  $ref: projects/orca/visual-semantics/schemas/visual-semantics-schema-v0.md
  fields: { ... }
  drift_acceptance: { ... }
```

## Fields to add in v1

| Field | Purpose |
|-------|---------|
| `cargo_cards_max` | desktop cap |
| `cargo_cards_max_mobile` | mobile cap |
| `mobile_hero_cta_order` | stack order |
| `primary_ad_variant` | H1 ↔ ad continuity |
| `trust_hero_social` | hybrid/social copy lock |
| `trust_hero_operational` | ops strip lines |
| `density_override` | operator sign-off for high density |

## First pack candidates

1. `triumph-manipulyator-zakaz-pack-v0` — **does not exist**; required for master hot
2. Extend `triumph-manipulyator-5-tonn-pack-v0` with visual block as pattern donor only

## Migration rule

5-ton pack = **structural donor**, not SoT for zakaz H1 or visual fields.

## Blockers

- No zakaz handoff today (`handoff-gaps-v1.md`)
- validation-cli does not validate visual fields — human QA only

## SAFE UNKNOWN

Automated pack linter for visual semantics — not planned in v0.
