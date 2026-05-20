# Heuristic Expiration Template v1

## Boundary

Use this template for human expiration review. Expiration review does not run automatically and does not erase historical evidence.

## Metadata

- `heuristic_id`:
- `reviewer`:
- `review_date`:
- `previous_expiration_review_date`:
- `next_expiration_review_date`:

## Current State

- `current_status`:
- `current_confidence`:
- `current_stability`:
- `freshness`:
- `volatility`:
- `regional_applicability`:
- `niche_applicability`:
- `device_applicability`:
- `seasonal_applicability`:

## Expiration Inputs

- `oldest_supporting_evidence_date`:
- `latest_supporting_evidence_date`:
- `stale_records`:
- `expired_records`:
- `open_contradictions`:
- `seasonal_mismatch`:
- `region_or_niche_mismatch`:
- `serp_or_market_changes`:

## Decision

- `expiration_decision`: renew / watch / needs_refresh / expired / retired
- `decision_reason`:
- `confidence_impact`:
- `stability_impact`:
- `required_refresh_evidence`:
- `safe_unknowns`:

## Required Discipline

Expired evidence should not support current confidence. A heuristic may be historically useful and still unsuitable for present strategic use.
