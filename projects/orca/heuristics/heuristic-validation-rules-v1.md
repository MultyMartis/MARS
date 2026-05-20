# Heuristic Validation Rules v1

## Purpose

Defines how ORCA heuristics are validated before reuse in strategic PPC guidance. Validation is human-supervised and evidence-sensitive.

## Validation Required

Human validation is required before:

- using a heuristic in campaign segmentation recommendations;
- applying a heuristic to a new niche;
- applying a heuristic to a new region;
- raising confidence;
- resolving contradictions;
- treating an urgent-intent or mobile-first pattern as current;
- using aggregator-pressure guidance in a launch plan.

## Required Checks

- human review;
- evidence traceability;
- contradiction checks;
- confidence review;
- volatility review;
- regional review;
- seasonal review;
- device review when mobile behavior matters;
- SAFE UNKNOWN review.

## Validation Outcomes

- `accepted` - usable within stated limits.
- `accepted_with_limits` - usable only with explicit region, niche, device, or time boundaries.
- `hypothesis` - promising but insufficiently supported.
- `contradicted` - conflicts with evidence and must be tracked.
- `expired` - evidence is too old for current use.
- `rejected` - unsupported, overgeneralized, or synthetic-only.

## Rules

- Validation does not make a heuristic universal truth.
- Contradictions must remain attached to the heuristic.
- Heuristics may conflict across niches, regions, devices, or seasons.
- Current evidence matters more than clean theory.
- Human interpretation is required before operational use.
- ORCA does not autonomously make strategy decisions.

## Boundary

These rules define manual validation discipline. They are not autonomous strategy generation, campaign control, automated optimization, telemetry, or runtime orchestration.
