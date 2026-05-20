# Export Package Contract v0

## Purpose

Defines the expected contents of a human-reviewed export package for manual use with advertising platform tools.

## Required Fields

- `project_name`.
- `platform_intent`.
- `export_date`.
- `prepared_by`.
- `campaign_table`.
- `ad_group_table`.
- `keyword_table`.
- `negative_keyword_table`.
- `ad_copy_table`.
- `format_assumptions`.
- `human_import_checklist`.
- `safe_unknown`.

## Optional Fields

- `extension_table`.
- `utm_table`.
- `tracking_notes`.
- `account_notes`.
- `version_notes`.
- `qa_report_ref`.

## Validation Notes

- Export tables are draft artifacts until a human approves them.
- This contract does not connect to Yandex.Direct, Google Ads, or any live account.
- Missing platform-specific columns must be marked SAFE UNKNOWN.
- Import must be performed manually by an authorized human operator.

## Example

```yaml
project_name: clinic_search_phase_1
platform_intent: Yandex.Direct
export_date: 2026-05-18
prepared_by: ORCA documentation workflow
campaign_table: campaigns.csv
ad_group_table: ad_groups.csv
keyword_table: keywords.csv
negative_keyword_table: negatives.csv
ad_copy_table: ads.csv
format_assumptions:
  - Direct Commander style tabular import
human_import_checklist:
  - review required columns
  - confirm URLs and tracking
  - approve campaign activation manually
safe_unknown:
  - exact account import template
```

## SAFE UNKNOWN Fields

- Exact account import template.
- Required platform columns.
- Final tracking parameters.
- Final campaign activation setting.
- Account-level restrictions.
