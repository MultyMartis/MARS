# Pattern Reliability Scoring v1

## Purpose

Defines a practical scoring method for ORCA pattern reliability. The score is a human-reviewed summary of evidence support, not an automated truth measure.

ORCA observes reality. ORCA does not define reality. Pattern reliability remains contextual, revisable, and bounded by evidence quality.

## Scoring Inputs

- evidence strength;
- repeatability;
- source reliability;
- evidence freshness;
- SERP stability;
- market volatility;
- contradiction frequency;
- regional certainty;
- seasonal certainty;
- human validation status.

## Reliability Bands

- `low_reliability` - weak evidence, isolated signal, missing context, stale source, or open contradiction.
- `moderate_reliability` - repeated evidence in a limited context with some uncertainty.
- `high_reliability` - repeated current evidence with bounded contradictions and clear context.
- `very_high_reliability` - multi-case, multi-source, time-aware evidence with low volatility and human-reviewed reuse.

## Penalties

- open contradiction;
- unstable SERP;
- high market volatility;
- missing region;
- missing timestamp;
- missing device context when relevant;
- stale or expired evidence;
- single-source repetition;
- seasonal mismatch;
- unsupported regional transfer.

## Rules

- Reliability cannot exceed evidence strength.
- Reliability cannot exceed confidence governance limits.
- Unsupported abstractions are forbidden.
- Synthetic summaries do not raise reliability.
- Repeated evidence may raise reliability only when comparable.
- Contradictory evidence must remain visible in the score rationale.
- Human review is required before high or very high reliability is used strategically.

## Output Format

```yaml
pattern_reliability:
  pattern_id:
  reliability_band:
  confidence_level:
  evidence_strength:
  repeatability:
  penalties:
  contradictions:
  regional_scope:
  seasonal_scope:
  freshness:
  human_reviewer:
  safe_unknown:
```

## Boundary

This scoring model is a research aid. It is not a runtime scoring engine, telemetry system, autonomous market intelligence model, or campaign optimization system.
