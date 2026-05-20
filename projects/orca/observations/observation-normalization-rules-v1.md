# Observation Normalization Rules v1

## Purpose

Defines how ORCA pilot observations are converted into reusable records. Normalization improves comparison across cases while preserving context and human interpretation.

## Normalization Principles

- Keep original context attached to every observation.
- Use consistent observation types.
- Separate evidence from interpretation.
- Record region, niche, device, and timestamp.
- Preserve uncertainty instead of forcing a conclusion.
- Update confidence only after human review.

## Required Normalization Steps

1. Assign an observation type.
2. Link the observation to a pilot case.
3. Record source, region, niche, device, and time.
4. Rewrite the finding as a factual statement.
5. Add interpretation only if the operator can justify it.
6. Score evidence strength.
7. Score repeatability.
8. Score volatility and recency.
9. Assign strategic importance.
10. Record SAFE UNKNOWN.

## Factual Finding Rules

Good findings:

- describe visible evidence;
- avoid strategy claims;
- avoid hidden metrics;
- avoid permanent language;
- include context.

Bad findings:

- "Competitor has a better bid strategy."
- "The market is saturated."
- "Users prefer aggregators."
- "This campaign should increase budget."

Improved findings:

- "Four ads were visible above organic results for the observed mobile query."
- "Two aggregators appeared in top organic positions for three observed queries."
- "Most visible competitors used price-from messaging in the observed region."

## Confidence Constraints

- A single SERP snapshot cannot exceed MEDIUM confidence unless supported by independent evidence.
- Stale evidence reduces confidence.
- Contradictory evidence must be recorded before raising confidence.
- Region-specific evidence must not be generalized without new validation.
- Unstable SERP layouts require volatility notes.

## Reuse Rules

An observation can be reused only when the report includes:

- original case source;
- applicable region or reuse boundary;
- niche applicability;
- confidence level;
- known distortions;
- human validation note.

## Boundary

Normalization supports PPC research discipline. It does not automate conclusions, create optimization rules, control campaigns, or replace human strategic judgment.
