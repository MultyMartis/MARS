# Heuristic Evidence Requirements v1

## Purpose

Defines minimum evidence expectations before ORCA heuristics can be reused as strategic guidance. Evidence requirements protect against universal claims, stale assumptions, and unsupported recommendations.

## Minimum Evidence

A reusable heuristic requires:

- repeated observations in comparable contexts;
- traceable source records;
- human-reviewed pilot findings or validated observation records;
- region, niche, device, and timestamp context;
- contradiction review;
- evidence freshness review;
- explicit SAFE UNKNOWN notes.

## Repeated Observation Rules

- One observation can suggest a hypothesis, not a reusable heuristic.
- Repetition must come from comparable commercial contexts.
- Repetition from one unstable SERP does not establish reliability.
- Repetition across region, device, or season must preserve those boundaries.

## Regional Confirmation

- Regional evidence supports only the observed region unless validated elsewhere.
- City-level local service evidence should not be generalized to broad national markets.
- Regional transfer requires fresh human review.
- Missing regional context caps confidence.

## Evidence Quality Thresholds

Higher quality evidence includes:

- current screenshots or traceable manual review;
- consistent pilot case findings;
- visible SERP or landing evidence;
- bounded contradictions;
- clear reviewer notes.

Lower quality evidence includes:

- stale screenshots;
- synthetic-only summaries;
- unclear region or device context;
- single-source repetition;
- unreviewed assumptions.

## Penalties

Apply penalties for:

- SERP volatility;
- high market volatility;
- stale evidence;
- open contradictions;
- missing timestamp;
- missing region;
- missing device context;
- seasonal mismatch;
- unsupported regional transfer.

## Insufficient Evidence Handling

- Mark as `hypothesis` when evidence is promising but thin.
- Use `SAFE_UNKNOWN` when key context is missing.
- Do not raise confidence to support a preferred recommendation.
- Do not convert pilot-only evidence into universal strategy.

## Boundary

These requirements guide human evidence review. They are not automated validation, telemetry, self-learning intelligence, or an optimization system.
