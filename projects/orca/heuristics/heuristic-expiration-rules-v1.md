# Heuristic Expiration Rules v1

## Purpose

Defines when ORCA strategic heuristics must be reviewed, downgraded, expired, or refreshed. Heuristic reliability can degrade as markets, SERPs, competitors, devices, and seasons change.

## Expiration Triggers

- evidence age exceeds the review window;
- SERP layout changes;
- aggregator visibility changes;
- local pack behavior changes;
- seasonal demand changes;
- regional expansion is proposed;
- device behavior changes;
- landing patterns shift;
- contradictions appear;
- pilot evidence is superseded.

## Evidence Aging Rules

- Stale evidence cannot support high confidence.
- Old screenshots should be treated as historical evidence.
- Time-bound urgent-intent patterns need frequent review.
- Mobile behavior may expire faster than broad strategic guidance.
- Aggregator-pressure evidence should be refreshed when SERPs change.

## Expiration Outcomes

- `active` - current and usable within limits.
- `review_due` - usable with caution until human review.
- `confidence_reduced` - still relevant but weaker.
- `expired` - not usable for current strategy without fresh evidence.
- `superseded` - replaced by newer evidence while old rationale remains visible.

## Refresh Requirements

Refresh requires:

- new timestamped evidence;
- human reviewer;
- region and device confirmation;
- contradiction review;
- confidence review;
- updated SAFE UNKNOWN notes.

## Boundary

These rules manage documentation freshness. They are not automated monitoring, telemetry, scraping, self-updating intelligence, or campaign optimization.
