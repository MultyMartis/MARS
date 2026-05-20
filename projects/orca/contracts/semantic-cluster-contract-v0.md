# Semantic Cluster Contract v0

## Purpose

Defines the structure for reviewable PPC keyword clusters before campaign generation.

## Required Fields

- `project_name`.
- `cluster_id`.
- `cluster_name`.
- `primary_intent`.
- `keywords`.
- `negative_keyword_candidates`.
- `source_notes`.
- `landing_page`.
- `safe_unknown`.

## Optional Fields

- `secondary_intents`.
- `priority`.
- `match_type_suggestion`.
- `geo_modifier_notes`.
- `duplicate_warnings`.
- `policy_risk_notes`.

## Validation Notes

- Match type suggestions are draft notes, not final platform settings.
- Landing page must be confirmed or marked SAFE UNKNOWN.
- Each cluster should support one coherent ad message.
- Duplicate and near-duplicate keywords should be flagged for QA.

## Example

```yaml
project_name: clinic_search_phase_1
cluster_id: cl_001
cluster_name: diagnostics_general
primary_intent: commercial
keywords:
  - diagnostics clinic
  - paid diagnostics center
negative_keyword_candidates:
  - free
source_notes:
  - seed keyword plus SERP expansion
landing_page: https://example.com/diagnostics
safe_unknown:
  - search volume
```

## SAFE UNKNOWN Fields

- Search volume.
- Final match type.
- Landing page fit.
- Whether a term has regulated-claim risk.
- Whether a negative keyword may block useful traffic.
