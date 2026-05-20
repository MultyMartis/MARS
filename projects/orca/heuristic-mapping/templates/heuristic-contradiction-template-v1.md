# Heuristic Contradiction Template v1

## Boundary

Use this template to preserve conflicts affecting a heuristic. The goal is not to force resolution, but to keep contradictions visible for human review.

## Contradiction Metadata

- `contradiction_id`:
- `heuristic_id`:
- `reported_by`:
- `reported_at`:
- `status`: `open` / `bounded` / `volatile` / `superseded` / `unresolved_safe_unknown`

## Conflict Type

- `region_conflict`:
- `niche_conflict`:
- `device_conflict`:
- `cta_conflict`:
- `seasonal_conflict`:
- `serp_pattern_conflict`:
- `landing_serp_conflict`:
- `other_conflict`:

## Linked Evidence

- `supporting_records`:
- `conflicting_records`:
- `pilot_cases`:
- `observation_records`:
- `screenshots_or_review_notes`:

## Review Notes

- `possible_explanation`:
- `confidence_impact`:
- `stability_impact`:
- `applicability_impact`:
- `required_refresh_evidence`:
- `safe_unknowns`:
- `reviewer`:
- `review_date`:

## Required Discipline

Do not hide, delete, or average away contradictions. If the conflict cause is unclear, record `SAFE_UNKNOWN` and cap confidence until human review resolves or bounds it.
