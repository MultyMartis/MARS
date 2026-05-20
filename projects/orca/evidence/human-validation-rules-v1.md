# Human Validation Rules v1

## Purpose

Defines when ORCA evidence and interpretations require human validation. Human validation prevents false confidence, premature generalization, unsupported strategy, and AI-generated fake patterns.

ORCA observes reality. ORCA does not define reality. All conclusions remain human-supervised and revisable.

## Validation Required

Human validation is required before:

- raising confidence to HIGH or VERY HIGH;
- converting observations into reusable patterns;
- using evidence in campaign architecture;
- applying regional evidence to a new region;
- treating seasonal evidence as non-seasonal;
- resolving contradictions;
- retiring or downgrading stale evidence;
- using client input as commercial market evidence;
- using AI-generated synthesis in a research deliverable.

## Reviewer Checks

The reviewer must check:

- source exists and is traceable;
- timestamp is present or SAFE UNKNOWN is explicit;
- region, niche, and device context are recorded;
- SERP conditions and volatility are noted where relevant;
- contradictions are preserved;
- confidence matches evidence strength;
- evidence freshness is appropriate for the intended use;
- strategic impact does not exceed evidence support.

## Validation Outcomes

- `accepted` - evidence is usable within stated limits.
- `accepted_with_limits` - evidence is usable only with explicit boundaries.
- `needs_more_evidence` - evidence is too thin for conclusion.
- `contradicted` - evidence conflicts with another observation and must be tracked.
- `stale` - evidence is too old for current confidence.
- `rejected` - source is unreliable, unsupported, or synthetic-only.

## Rules

- Human validation does not make an observation absolute truth.
- Repeated evidence matters more than isolated findings.
- Unstable SERPs reduce confidence even when findings are commercially interesting.
- Contradictory evidence must remain visible after validation.
- SAFE UNKNOWN is valid when evidence is missing or unstable.

## Boundary

These rules describe review discipline. They are not autonomous QA, runtime validation, telemetry, scraping, or self-learning market intelligence.
