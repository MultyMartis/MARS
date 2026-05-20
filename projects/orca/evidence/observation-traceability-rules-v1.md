# Observation Traceability Rules v1

## Purpose

Defines how ORCA keeps every commercial observation traceable to its evidence context. Traceability prevents fake patterns, premature generalization, and confidence accumulation without support.

ORCA observes reality. ORCA does not define reality. If an observation cannot be traced, it cannot support a conclusion.

## Required Trace Fields

- `observation_id` - stable identifier.
- `evidence_id` - linked evidence record.
- `source_type` - SERP, landing page, competitor page, local pack, client input, operator note, or SAFE UNKNOWN.
- `timestamp` - observation time or SAFE UNKNOWN.
- `region` - observed market boundary.
- `niche` - service or commercial category.
- `query_or_case_ref` - exact query, case, or review target.
- `device_context` - desktop, mobile, mixed, or SAFE UNKNOWN.
- `serp_conditions` - visible layout and volatility notes when relevant.
- `human_reviewer` - reviewer or role.
- `interpretation_status` - raw, interpreted, contradicted, superseded, or retired.
- `linked_contradictions` - contradictory observations that limit the finding.

## Traceability Rules

- Every interpretation must link back to one or more observations.
- Every reusable pattern must link back to repeated observations.
- Every confidence increase must cite evidence that caused the increase.
- Every confidence decrease must preserve the cause: contradiction, volatility, age, region mismatch, or source weakness.
- Observation timestamps must not be removed when evidence ages.
- Region, niche, and device context must travel with the observation.
- SAFE UNKNOWN must be used instead of filling missing trace fields.

## Unsupported Pattern Controls

- Do not merge unlike observations only because they sound similar.
- Do not reuse a pattern outside its observed region without new evidence.
- Do not treat one SERP snapshot as a stable market structure.
- Do not hide contradictory or unstable evidence during summary.
- Do not rewrite old observations to match newer interpretations.

## Boundary

These rules create human-readable traceability. They are not telemetry, a database schema, browser automation, scraping infrastructure, or autonomous evidence collection.
