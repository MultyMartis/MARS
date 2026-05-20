# Drift Detection Rules v1

## Purpose

Defines how ORCA reviewers identify operational drift: growth that weakens usefulness, evidence discipline, commercial realism, or human usability.

Drift detection is a human review practice. It is not autonomous monitoring or telemetry.

## Drift Types

### Methodology Bloat

The method adds steps, fields, or categories without improving review decisions.

### Useless Abstraction Growth

Language becomes more theoretical while practical PPC usefulness declines.

### Duplicated Systems

Multiple documents solve the same review problem with different names and no clear boundary.

### Operational Irrelevance

Outputs no longer help with real evidence review, local-service strategy, campaign QA, or commercial decisions.

### Stale Heuristics

Heuristics continue to be reused after evidence becomes stale, contradicted, or region-mismatched.

### Stale Patterns

Old SERP, CTA, aggregator, or local-pack patterns are treated as current without refresh.

### Evidence Decay

Evidence loses relevance because time, region, device behavior, competition, or seasonality changed.

### Over-Engineering

Review work becomes too complex for human operators to perform consistently.

### Review Fatigue

Reviewers fill templates mechanically, skip contradictions, or stop using review outputs.

## Detection Questions

- Does this artifact still change decisions?
- Is the same review repeated elsewhere?
- Are stale patterns being reused as current?
- Are contradictions becoming harder to see?
- Is reviewer effort proportional to value?
- Does commercial reality still lead the method?

## Review Actions

- simplify;
- merge duplicated areas;
- mark stale;
- retire low-use artifacts;
- refresh evidence;
- downgrade confidence;
- preserve drift notes for future review.

## Boundary

These rules support human drift detection. They are not telemetry, automated governance, runtime monitoring, or autonomous cleanup.
