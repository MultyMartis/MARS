# Contradiction Tracking Model v1

## Purpose

Defines how ORCA records and preserves contradictory commercial observations. Contradictions are evidence, not noise. They prevent false confidence, premature generalization, and unsupported market rules.

ORCA observes reality. ORCA does not define reality. Contradictory evidence must remain visible and revisable.

## Contradiction Types

- contradictory findings;
- regional contradictions;
- seasonal contradictions;
- niche contradictions;
- device contradictions;
- SERP instability;
- source reliability conflict;
- evolving market behavior;
- stale versus current evidence conflict.

## Required Fields

- `contradiction_id`;
- `linked_observations`;
- `contradiction_type`;
- `region`;
- `niche`;
- `device_context`;
- `observation_timestamps`;
- `conflicting_findings`;
- `possible_explanation`;
- `confidence_impact`;
- `resolution_status`;
- `human_reviewer`;
- `safe_unknown`.

## Resolution Status

- `open` - contradiction exists and needs more evidence.
- `bounded` - contradiction is explained by region, season, device, niche, or source limits.
- `unstable` - SERP or market volatility prevents resolution.
- `superseded` - newer evidence reduces older evidence reliability without deleting it.
- `resolved` - human-reviewed explanation is documented.
- `SAFE_UNKNOWN` - insufficient evidence to classify.

## Rules

- Do not delete contradictory evidence.
- Do not hide unstable findings.
- Do not convert hypotheses into rules too early.
- Do not average contradictions into a cleaner conclusion.
- Link contradictions to confidence penalties.
- Preserve region, niche, device, and timestamp context.
- Require human review before marking a contradiction resolved.

## Boundary

This model is a documentation discipline for human research. It is not automated conflict resolution, telemetry, monitoring, scraping, or self-learning intelligence.
