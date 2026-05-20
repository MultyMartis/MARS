# Heuristic Mapping Model v1

## Purpose

Defines the required record model for linking strategic heuristics to evidence, pilot cases, observations, contradictions, confidence reviews, and expiration review.

A mapping record does not prove a heuristic is universally true. It records why a human reviewer currently treats a heuristic as usable within bounded conditions.

## Required Fields

- `heuristic_id` - stable identifier for the heuristic being mapped.
- `heuristic_title` - short human-readable name.
- `current_statement` - bounded statement of the heuristic.
- `linked_evidence_records` - evidence IDs, observation IDs, screenshots, or review notes supporting the heuristic.
- `linked_pilot_cases` - pilot case IDs or paths that produced relevant findings.
- `contradiction_references` - linked contradiction records, open conflicts, or bounded exceptions.
- `supporting_observations` - repeated observations that support the heuristic.
- `conflicting_observations` - observations that weaken, limit, or contradict the heuristic.
- `confidence_level` - `LOW`, `MEDIUM`, `HIGH`, or `VERY_HIGH` by human review.
- `stability_level` - `UNSTABLE`, `FRAGILE`, `MODERATE`, or `STABLE`.
- `volatility` - market, SERP, seasonal, device, or offer volatility that may affect use.
- `freshness` - `current`, `recent`, `stale`, `expired`, or `unknown`.
- `regional_applicability` - regions where evidence is directly supported.
- `niche_applicability` - niches where evidence is directly supported.
- `device_applicability` - mobile, desktop, or mixed evidence boundary.
- `seasonal_applicability` - season, demand cycle, or time-sensitive condition.
- `expiration_review_date` - date when evidence must be refreshed or downgraded.
- `reviewer` - human reviewer responsible for the latest mapping decision.
- `last_reviewed_at` - date of latest human review.
- `safe_unknowns` - unknowns that must remain visible.

## Mapping Rules

- Every heuristic must link to traceable evidence or remain a hypothesis.
- Contradictions must be linked even when they are inconvenient.
- Supporting and conflicting observations must not be merged into a cleaner claim.
- Freshness and volatility must influence confidence.
- Regional, niche, device, and seasonal boundaries must stay explicit.
- Human review is required before changing confidence, stability, applicability, or expiration.

## Status Semantics

- `active_bounded` - usable within stated limits after human review.
- `hypothesis` - promising but not sufficiently supported.
- `needs_refresh` - evidence is stale, region-mismatched, or volatility-sensitive.
- `contradicted` - open contradictions prevent broad reuse.
- `expired` - should not support current strategy without refreshed evidence.
- `retired` - preserved for history but no longer used as guidance.

## Boundary

This model is a documentation schema for human-supervised traceability. It is not an automated knowledge graph, scoring engine, strategy engine, telemetry system, or self-updating heuristic store.
