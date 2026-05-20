# ORCA Heuristic Mapping System v1

## Purpose

Defines the ORCA Heuristic Mapping System v1: a documentation layer for linking pilot findings, evidence records, observations, contradictions, confidence reviews, and strategic heuristics.

This layer keeps heuristics evidence-backed, traceable, revisable, contradiction-aware, region-aware, and volatility-aware. It does not create, update, rank, or apply heuristics autonomously.

## Scope

Use this layer for:

- evidence-to-heuristic traceability;
- pilot-to-heuristic mapping;
- contradiction-aware heuristic review;
- confidence and stability review;
- expiration and freshness review;
- region, niche, device, and season boundary recording.

## Required Discipline

- Heuristics are revisable.
- Heuristics are not universal truth.
- Heuristics can decay.
- Heuristics can conflict.
- Evidence quality matters.
- Contradictions must be preserved, not hidden.
- Regional and niche transfer requires fresh human review.
- ORCA does not autonomously evolve heuristics.
- Human review is required for all updates.

## Directory Guide

- `heuristic-mapping-model-v1.md` - required mapping fields and record semantics.
- `evidence-to-heuristic-linking-v1.md` - evidence thresholds and linking rules.
- `contradiction-aware-heuristics-v1.md` - contradiction handling for heuristic records.
- `heuristic-revision-workflow-v1.md` - review, downgrade, refresh, and stale workflows.
- `heuristic-expiration-review-v1.md` - expiration review discipline.
- `heuristic-stability-model-v1.md` - UNSTABLE, FRAGILE, MODERATE, STABLE classification.
- `templates/` - human-filled record templates.
- `examples/` - fictional, non-production demonstrations.

## Boundary

This is heuristic traceability discipline and operational intelligence normalization. It is not self-learning AI, automatic heuristic generation, autonomous strategy, runtime orchestration, telemetry analytics, dashboards, scraping, browser automation, deployment tooling, or autonomous market intelligence.
