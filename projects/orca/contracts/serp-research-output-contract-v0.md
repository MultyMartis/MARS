# SERP Research Output Contract v0

## Purpose

Defines the expected output of SERP research before semantic collection and campaign architecture.

## Required Fields

- `project_name`.
- `research_date`.
- `target_geography`.
- `queries_reviewed`.
- `observed_competitors`.
- `paid_result_patterns`.
- `organic_result_patterns`.
- `intent_notes`.
- `risk_notes`.
- `safe_unknown`.

## Optional Fields

- `example_ad_messages`.
- `offer_patterns`.
- `common_objections`.
- `localization_notes`.
- `screenshots_or_source_refs`.

## Validation Notes

- Competitor data must be described as visible observation, not verified strategy.
- Search result personalization and localization limits must be noted.
- SERP research does not prove volume, conversion rate, bid level, or account performance.
- Results require human review before being used in PPC planning.

## Example

```yaml
project_name: clinic_search_phase_1
research_date: 2026-05-18
target_geography: Moscow
queries_reviewed:
  - diagnostics clinic
observed_competitors:
  - name: competitor_a
    evidence: visible ad result for reviewed query
paid_result_patterns:
  - appointment-focused headlines
organic_result_patterns:
  - service category landing pages
intent_notes:
  - commercial local intent
risk_notes:
  - medical claim sensitivity
safe_unknown:
  - exact competitor bids
```

## SAFE UNKNOWN Fields

- Exact competitor budgets.
- Exact competitor bids.
- Search volume when no reliable source is available.
- Personalized result differences.
- Whether a visible ad is part of a stable campaign.
