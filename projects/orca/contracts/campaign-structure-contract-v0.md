# Campaign Structure Contract v0

## Purpose

Defines a draft campaign and ad group structure produced from reviewed semantic clusters.

## Required Fields

- `project_name`.
- `platform_intent`.
- `campaign_id`.
- `campaign_name`.
- `campaign_goal_note`.
- `target_geography`.
- `ad_groups`.
- `landing_page_mapping`.
- `exclusions`.
- `human_decisions_required`.
- `safe_unknown`.

## Optional Fields

- `naming_convention`.
- `audience_notes`.
- `schedule_notes`.
- `utm_notes`.
- `budget_notes`.
- `bid_notes`.
- `copy_requirements`.

## Validation Notes

- Budget and bid notes are placeholders for human decisions only.
- The contract does not authorize upload, activation, or live edits.
- Each ad group must map to a semantic cluster.
- Missing settings must remain SAFE UNKNOWN rather than guessed.

## Example

```yaml
project_name: clinic_search_phase_1
platform_intent: Yandex.Direct
campaign_id: cmp_001
campaign_name: search_moscow_diagnostics
campaign_goal_note: draft search campaign for diagnostics demand
target_geography: Moscow
ad_groups:
  - ad_group_id: ag_001
    ad_group_name: diagnostics_general
    cluster_id: cl_001
landing_page_mapping:
  ag_001: https://example.com/diagnostics
exclusions:
  - free
human_decisions_required:
  - final budget
  - final bid strategy
safe_unknown:
  - account schedule settings
```

## SAFE UNKNOWN Fields

- Final budget.
- Final bid strategy.
- Account-level targeting settings.
- Schedule settings.
- Tracking template.
- Compliance approval.
