# Heuristic Confidence Rules v1

## Purpose

Defines how ORCA assigns and updates confidence for strategic heuristics. Confidence is a human-reviewed estimate of evidence support, not an automated score or decision authority.

## Confidence Levels

- `LOW` - weak, early, stale, or single-context evidence.
- `MEDIUM` - repeated evidence within clear limits.
- `HIGH` - repeated current evidence with bounded contradictions.
- `VERY_HIGH` - multi-case, multi-source, current evidence with low volatility and strong human review.

## Increase Rules

Confidence can increase only when:

- evidence is repeated and traceable;
- region and niche fit are clear;
- contradictions are reviewed;
- evidence is current;
- volatility is low or bounded;
- human reviewer approves the change.

## Decrease Rules

Confidence must decrease or be capped when:

- evidence becomes stale;
- SERP or market volatility increases;
- contradictions appear;
- regional transfer is unvalidated;
- seasonal conditions change;
- device behavior changes;
- supporting screenshots or observations are outdated.

## Confidence Caps

Use a cap when:

- evidence is strong but region-limited;
- mobile evidence is applied to desktop or desktop to mobile;
- aggregator pressure is visible but not repeated;
- trust or CTA patterns are observed but landing performance is unknown;
- urgency behavior is plausible but not validated.

## SAFE UNKNOWN

Use SAFE UNKNOWN for:

- unknown conversion performance;
- unknown CPC impact;
- unknown lead quality;
- unknown competitor intent;
- unknown stability over time;
- unknown regional representativeness.

## Boundary

These confidence rules support human strategic review. They are not an automated scoring engine, bidding system, optimization system, or self-learning model.
