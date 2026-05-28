# Visual Semantics Schema v0

Master bundle schema for ORCA handoff / future content pack front-matter.

## Root object

```yaml
visual_semantics:
  version: "v0"
  route_id: string          # e.g. master_hot, use_case_bytovka
  group_id: string | null   # e.g. grp_fc12_zakaz
  canonical_url: string
  fields: VisualSemanticsFields
  drift_acceptance:
    productive: string[]    # drift IDs or descriptions
    destructive: string[]   # must be empty for factory approval
    ambiguous: string[]     # requires operator note
  factory_hints:
    partial_paths: object   # section → path
    data_page_type: string
  operator:
    approved_by: string | null
    approved_at: date | null
```

## `VisualSemanticsFields` (required for Factory)

| Field | Type | Required |
|-------|------|----------|
| `hero_priority` | enum | yes |
| `proof_priority` | enum | yes |
| `cta_priority` | enum | yes |
| `visual_density` | enum | yes |
| `compactness_level` | enum | yes |
| `mobile_critical` | string[] | yes |
| `trust_mode` | enum | yes |
| `qualification_mode` | enum | yes |
| `hero_layout_mode` | enum | yes |
| `proof_visibility` | enum | yes |
| `cta_weight` | enum | yes |
| `semantic_focus` | string[] | yes |
| `conversion_intent_weight` | enum | yes |
| `visual_noise_risk` | enum | yes |
| `frontend_priority` | string[] | yes |

## Optional extensions (v1)

| Field | Type |
|-------|------|
| `cargo_cards_max` | int |
| `cargo_cards_max_mobile` | int |
| `mobile_hero_cta_order` | string[] |
| `trust_hero_social` | string |
| `trust_hero_operational` | string[] |
| `primary_ad_variant` | string |

## Validation rules (human-operated)

1. `destructive` array must be empty for `approved_for_factory: true`
2. `trust_mode: social_proof` requires `trust_hero_social` or blueprint lock text
3. `visual_density: overloaded` requires signed operator override
4. `hero_layout_mode: legacy_clutter` — **forbidden**

## Cross-refs

- [hero-priority-schema-v0.md](hero-priority-schema-v0.md)
- [trust-mode-schema-v0.md](trust-mode-schema-v0.md)
- [cta-priority-schema-v0.md](cta-priority-schema-v0.md)
- [compactness-schema-v0.md](compactness-schema-v0.md)
- [visual-density-schema-v0.md](visual-density-schema-v0.md)

## SAFE UNKNOWN

Machine validation CLI — **not in repo** for visual semantics v0.
