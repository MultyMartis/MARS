# Heuristic Link Record Template v1

## Boundary

Template for human-reviewed heuristic mapping. Do not treat completion of this template as automated validation, strategy approval, or proof of universal truth.

## Record

- `heuristic_id`:
- `heuristic_title`:
- `current_statement`:
- `status`: `hypothesis` / `active_bounded` / `needs_refresh` / `contradicted` / `expired` / `retired`
- `reviewer`:
- `last_reviewed_at`:
- `expiration_review_date`:

## Linked Sources

- `linked_evidence_records`:
- `linked_pilot_cases`:
- `linked_confidence_reviews`:
- `linked_contradiction_records`:
- `linked_observations`:

## Applicability

- `regional_applicability`:
- `niche_applicability`:
- `device_applicability`:
- `seasonal_applicability`:
- `non_applicable_contexts`:

## Evidence Summary

- `supporting_observations`:
- `conflicting_observations`:
- `minimum_evidence_met`: yes / no / partial
- `repeatability_notes`:
- `evidence_quality_notes`:
- `stale_evidence_penalties`:
- `weak_evidence_penalties`:

## Review Decision

- `confidence_level`: `LOW` / `MEDIUM` / `HIGH` / `VERY_HIGH`
- `stability_level`: `UNSTABLE` / `FRAGILE` / `MODERATE` / `STABLE`
- `volatility`:
- `freshness`: `current` / `recent` / `stale` / `expired` / `unknown`
- `safe_unknowns`:
- `reviewer_decision`:

## Required Discipline

- Heuristics are revisable.
- Evidence quality matters.
- Contradictions must be preserved.
- Human review is required for all updates.
- ORCA does not autonomously evolve this record.
