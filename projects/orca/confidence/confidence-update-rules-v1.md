# Confidence Update Rules v1

## Purpose

Defines how ORCA updates confidence when new evidence, contradictions, volatility, or decay appears. Updates must be traceable and human-reviewed.

ORCA observes reality. ORCA does not define reality. Confidence changes must explain why reliability changed.

## Required Update Fields

- `confidence_update_id`;
- `pattern_or_observation_ref`;
- `previous_confidence`;
- `new_confidence`;
- `update_reason`;
- `new_evidence_refs`;
- `contradiction_refs`;
- `volatility_notes`;
- `evidence_age`;
- `region_niche_device_scope`;
- `human_reviewer`;
- `safe_unknown`.

## Increase Rules

- LOW to MEDIUM requires repeated evidence in a defined context.
- MEDIUM to HIGH requires repeated, current, traceable evidence with bounded contradictions.
- HIGH to VERY HIGH requires multi-case, multi-source, time-aware validation and clear context boundaries.
- Confidence cannot increase from synthetic synthesis alone.
- Repetition from one unstable source does not justify a major increase.

## Decrease Rules

- New contradiction requires downgrade or explicit confidence cap.
- Stale evidence requires downgrade unless refreshed.
- Unstable SERPs require a volatility penalty.
- Missing region, niche, timestamp, or device context requires downgrade.
- Regional transfer without validation requires downgrade.
- Seasonal mismatch requires downgrade or pattern splitting.

## Insufficient Evidence Handling

- Use LOW when evidence exists but is weak.
- Use SAFE UNKNOWN when required context is missing.
- Do not force a confidence level to make a deliverable look complete.
- Do not hide downgrade reasons.

## Boundary

These rules define manual confidence discipline. They are not an automated model, scoring engine, telemetry pipeline, or self-learning system.
