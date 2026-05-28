# Semantic-to-Visual Translation v0

Maps ORCA **semantic artifacts** → **visual semantic fields** for Factory.

## Inputs (existing ORCA)

| Artifact | Typical semantic content |
|----------|---------------------------|
| Landing blueprint | H1, bullets, trust strip, chips, qualification |
| PPC instance JSON | `semantic_intent`, call-first, callouts, ads |
| Content pack (cousin) | Section copy, locks |
| Doctrine / MODE 1 | One machine, no fake price |

## Translation table

| Semantic artifact fragment | Visual semantic field(s) | Triumph observation |
|----------------------------|--------------------------|---------------------|
| 5 capability bullets | `hero_priority: capability_first`, `compactness_level: compact` | v5 spec list |
| «4.9 ★ Яндекс и Авито» | `trust_mode: social_proof`, `proof_visibility: prominent` | **Not implemented** in hero — ops strip instead |
| Qualification line | `qualification_mode: hero_notice`, `mobile_critical` + notice | **Removed** in v5 |
| «Узнать стоимость» CTA | `cta_priority: form`, `cta_weight: primary_dominant` | Label → «Рассчитать» (lexical neutral) |
| Use-case chips (6) | `visual_density: high`, `semantic_focus: use_case_fit` | Became 6 cargo cards + micro-CTAs |
| call-first in instance | `cta_priority: call`, `mobile_critical: call` | Hero form-dominant — **gap** |
| Anti-fleet doctrine | `semantic_focus: one_machine`, forbid `legacy_clutter` | v4 G0 violated |
| Pricing «по задаче» | No hero rate; `conversion_intent_weight: hot` | Fake rate removed (productive) |
| Denied tasks (section) | `qualification_mode: tasks_section_only` | Weaker than hero notice |
| Reviews section | `proof_priority: below_fold` | P3 trust — OK if `trust_mode` explicit |

## Translation procedure (operator / ORCA author)

1. Read blueprint **and** PPC instance slice for route.
2. Fill canonical fields in [schemas/visual-semantics-schema-v0.md](schemas/visual-semantics-schema-v0.md).
3. Classify expected Factory deviations as productive / destructive / ambiguous **before** build.
4. Attach visual semantics block to handoff (vNext: content pack front-matter).

## Failure mode: «copy-complete» handoff

5-ton handoff is structurally complete for **words**; zakaz had **no handoff**. Factory used blueprint + 5-ton patterns. Visual semantics were inferred ad hoc — causing ambiguous trust drift and destructive qualification loss.

**Rule:** Handoff is not complete without visual semantics bundle.

## Example snippet (target shape)

```yaml
visual_semantics:
  version: v0
  route: master_hot
  fields:
    trust_mode: hybrid_proof  # operator chose vs as-built operational_only
    qualification_mode: hero_lower_band
    visual_density: high
    visual_noise_risk: medium  # after capping cargo to 4
  drift_acceptance:
    productive: [inline_form, cargo_cards, bg_overlay]
    destructive: []  # must be empty for approval
```

## SAFE UNKNOWN

Automated translation from blueprint markdown to YAML — **not implemented** in v0.
