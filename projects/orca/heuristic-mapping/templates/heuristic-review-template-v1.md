# Heuristic Review Template v1

## Boundary

Use this template for human review of an existing heuristic mapping. It is not an automated confidence update or autonomous validation process.

## Review Metadata

- `heuristic_id`:
- `review_type`: scheduled / contradiction / expiration / volatility / transfer / evidence_refresh
- `reviewer`:
- `review_date`:
- `previous_confidence`:
- `previous_stability`:
- `previous_status`:

## Review Inputs

- `new_evidence_records`:
- `new_pilot_findings`:
- `new_observations`:
- `new_contradictions`:
- `expired_or_stale_records`:
- `region_niche_device_season_changes`:

## Evidence Check

- `minimum_evidence_met`: yes / no / partial
- `repeatability_confirmed`: yes / no / partial
- `region_fit_confirmed`: yes / no / partial
- `niche_fit_confirmed`: yes / no / partial
- `freshness_confirmed`: yes / no / partial
- `contradictions_reviewed`: yes / no / partial

## Decision

- `new_confidence`:
- `new_stability`:
- `new_status`:
- `confidence_change_reason`:
- `stability_change_reason`:
- `applicability_changes`:
- `expiration_review_date`:
- `safe_unknowns`:

## Required Discipline

Do not increase confidence unless evidence is traceable, current, repeatable, bounded, and human-reviewed. Contradictions and unknowns must remain visible.
