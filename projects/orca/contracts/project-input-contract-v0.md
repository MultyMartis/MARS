# Project Input Contract v0

## Purpose

Defines the minimum project brief required before ORCA can begin PPC research and campaign architecture work.

## Required Fields

- `project_name` - working name of the PPC project.
- `business_type` - product or service category.
- `offer_summary` - what is being promoted.
- `target_geography` - regions or cities for research and campaign planning.
- `target_language` - campaign language.
- `platform_intent` - intended platform, such as Yandex.Direct or Google Ads.
- `landing_pages` - URLs or SAFE UNKNOWN.
- `human_owner` - person responsible for final decisions.
- `hard_exclusions` - products, regions, claims, or keywords to avoid.

## Optional Fields

- `known_competitors`.
- `seed_keywords`.
- `brand_tone`.
- `budget_notes`.
- `tracking_requirements`.
- `regulatory_constraints`.
- `preferred_campaign_structure`.

## Validation Notes

- Budget notes are informational only and do not authorize bidding decisions.
- Missing landing pages must be marked SAFE UNKNOWN.
- Platform intent does not authorize upload, activation, or optimization.
- Human owner must be known before final approval.

## Example

```yaml
project_name: clinic_search_phase_1
business_type: private medical clinic
offer_summary: paid diagnostics appointments
target_geography: Moscow
target_language: ru
platform_intent: Yandex.Direct
landing_pages:
  - https://example.com/diagnostics
human_owner: marketing_lead
hard_exclusions:
  - emergency claims
  - guaranteed cure wording
seed_keywords:
  - diagnostics clinic
```

## SAFE UNKNOWN Fields

- Unknown landing pages.
- Unknown legal restrictions.
- Unknown tracking requirements.
- Unknown competitor relevance.
- Unknown final platform settings.
