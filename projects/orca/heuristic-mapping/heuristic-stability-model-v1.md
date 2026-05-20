# Heuristic Stability Model v1

## Purpose

Classifies heuristic stability for human review. Stability describes how durable a heuristic appears within its evidence boundaries. It is not a predictive score.

Heuristics can decay, conflict, or become unusable when evidence ages, markets shift, or contradictions increase.

## Inputs

Classify stability using:

- evidence age;
- contradiction density;
- repeatability;
- regional consistency;
- niche consistency;
- device consistency;
- seasonal consistency;
- volatility exposure;
- freshness state;
- reviewer confidence.

## Stability Levels

### UNSTABLE

Use when:

- evidence is early, stale, or single-context;
- contradictions are open or severe;
- SERP or competitor behavior is highly volatile;
- regional or niche fit is unclear;
- repeatability is weak;
- freshness is unknown.

Operational meaning: do not reuse broadly. Treat as hypothesis or refresh candidate.

### FRAGILE

Use when:

- evidence repeats but only in narrow context;
- contradictions exist but may be bounded;
- volatility is moderate or rising;
- regional transfer is unvalidated;
- seasonal fit is uncertain;
- confidence is capped.

Operational meaning: usable only with explicit boundaries and active review.

### MODERATE

Use when:

- evidence repeats across comparable contexts;
- contradictions are bounded;
- freshness is current or recent;
- regional and niche limits are clear;
- volatility is present but understood;
- seasonal fit is reviewed.

Operational meaning: usable as bounded strategic guidance after human review.

### STABLE

Use when:

- evidence is current, repeated, and traceable;
- contradictions are low, resolved, or tightly bounded;
- regional and niche consistency are demonstrated;
- seasonal behavior is understood;
- volatility exposure is low or monitored by review cadence;
- reviewer confidence is high within stated boundaries.

Operational meaning: reliable within limits, never universal.

## Downgrade Conditions

Downgrade stability when:

- evidence becomes stale;
- contradiction density increases;
- repeatability weakens;
- region or niche behavior diverges;
- seasonal assumptions fail;
- SERP volatility increases;
- reviewer cannot verify supporting records.

## Boundary

This stability model supports human judgment. It is not an automated scoring algorithm, telemetry system, prediction model, or autonomous strategy engine.
