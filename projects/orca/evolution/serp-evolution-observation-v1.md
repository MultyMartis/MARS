# SERP Evolution Observation v1

## Purpose

Defines how ORCA records changes in SERP structure over time. SERP evolution observations help humans understand volatility, not automate monitoring or claim permanent market structure.

ORCA observes reality. ORCA does not define reality. SERP findings are contextual, volatile, and revisable.

## Observable SERP Changes

- ad block density changes;
- local pack appearance, disappearance, or dominance;
- aggregator and marketplace position changes;
- organic result composition changes;
- review snippet visibility changes;
- map result prominence;
- mobile layout differences;
- CTA and offer message changes;
- informational versus commercial result mix.

## Required Fields

- `serp_evolution_id`;
- `search_engine`;
- `region`;
- `niche`;
- `query_set`;
- `device_context`;
- `baseline_snapshot_ref`;
- `comparison_snapshot_ref`;
- `observation_timestamps`;
- `change_summary`;
- `serp_stability`;
- `personalization_risk`;
- `seasonality_notes`;
- `contradictions`;
- `confidence`;
- `safe_unknown`.

## Rules

- Never treat a single SERP change as stable market evolution.
- Repeated observations matter more than isolated findings.
- Mobile and desktop SERPs must not be merged without evidence.
- Regional SERP differences must be preserved.
- Unstable SERPs reduce confidence and may cap conclusions at LOW or MEDIUM.
- Contradictory snapshots must remain linked.
- Human review is required before using SERP evolution in strategy.

## Boundary

This document supports manual SERP research discipline. It is not scraping infrastructure, browser automation, telemetry, alerting, or live SERP monitoring.
