# Visual semantics — Hero (canonical bundle)

**Reference:** `projects/orca/visual-semantics/examples/triumph-zakaz-hero-visual-semantics-v1.md`

## Calibrated fields (as-built G2)

```yaml
hero_priority: capability_first
trust_mode: operational_proof
compactness_level: compact
visual_density: high
cta_priority: form
proof_priority: hero_strip
mobile_critical: [form_submit, capability_scan]
qualification_mode: hero_notice_plus_tasks
hero_layout_mode: grid_form_aside
visual_noise_risk: high
semantic_focus: [one_machine, use_case_fit]
conversion_intent_weight: hot
proof_visibility: prominent
cta_weight: primary_dominant
```

## Zone map

| Zone | CSS / region | Priority |
|------|--------------|----------|
| Capability | `.hero__content` | P0 |
| Conversion | `.hero__aside` | P0 |
| Ops proof | `.hero-proof--v5` | P1 |
| Task fit | `.hero__cargo` | P1 |
| Filter | `.hero__notice` | P1 |

## Scan path (desktop)

H1 → lead → 5 specs → form title → submit → proof strip → cargo → notice

## Background semantics

- Machine photo as **ambient** bg — reduces image competition vs G0 inline visual note
- `first-screen__overlay` — text legibility lock

## drift_acceptance (summary)

See `factory/allowed-drift.md` and `calibration/productive-drift.md`.
