# Heuristic Expiration Review v1

## Purpose

Defines how ORCA reviews heuristic mappings for expiration, decay, and continued applicability.

Expiration review prevents old evidence from being treated as current truth. It does not delete history and does not run automatically.

## Expiration Inputs

Review:

- last evidence timestamp;
- latest pilot case reference;
- freshness state;
- contradiction references;
- volatility exposure;
- regional and niche applicability;
- device and seasonal applicability;
- confidence level;
- stability level;
- last reviewer notes.

## Review States

- `current` - evidence remains usable within stated context.
- `watch` - usable with caution because volatility, seasonality, or contradictions are increasing.
- `needs_refresh` - cannot support current strategic use until refreshed.
- `expired` - should not support confidence without new evidence.
- `retired` - no longer used as guidance, preserved for history.

## Expiration Rules

- Stale evidence cannot support `VERY_HIGH` confidence.
- Expired evidence cannot support current recommendations.
- High-volatility markets require shorter review intervals.
- Seasonal heuristics must be reviewed before reuse outside their season.
- Region-sensitive heuristics must be reviewed before transfer.
- Contradicted heuristics must not silently renew.
- Human reviewer approval is required for reactivation.

## Seasonal Review

Seasonal review should record:

- original season or demand cycle;
- whether current use matches that season;
- evidence from comparable prior seasons;
- off-season contradictions;
- required refresh observations.

## Output

Every expiration review should record:

- review decision;
- reason for renewal, downgrade, expiration, or retirement;
- confidence impact;
- stability impact;
- required evidence refresh;
- SAFE UNKNOWN;
- reviewer and date;
- next expiration review date.

## Boundary

Expiration review is documentation maintenance. It is not telemetry, monitoring, automatic expiration, autonomous validation, or market surveillance.
