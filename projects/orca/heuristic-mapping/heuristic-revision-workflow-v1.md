# Heuristic Revision Workflow v1

## Purpose

Defines the human-reviewed workflow for revising heuristic mappings when evidence changes, contradictions appear, confidence decays, or expiration review is due.

Revision is controlled documentation maintenance. ORCA does not autonomously update, evolve, retire, or promote heuristics.

## Review Triggers

Start review when:

- new pilot findings support or challenge a heuristic;
- new evidence records are added;
- confidence review changes;
- stability classification changes;
- region, niche, device, or season transfer is proposed;
- reviewer identifies missing context.

## Contradiction Triggers

Start contradiction review when:

- regions show different behavior;
- mobile and desktop behavior diverge;
- CTA evidence conflicts;
- seasonal evidence conflicts with current use;
- SERP screenshots or local pack behavior change;
- competitor or aggregator pressure changes;
- observation quality is disputed.

## Expiration and Volatility Triggers

Start expiration review when:

- expiration review date arrives;
- evidence becomes stale or unknown;
- market volatility increases;
- SERP layout changes;
- seasonal period ends;
- a high-pressure competitor pattern changes;
- freshness cannot be verified.

## Confidence Downgrade Rules

Downgrade or cap confidence when:

- evidence is stale;
- contradictions are open;
- region or niche transfer is unvalidated;
- repeatability is weak;
- volatility is high;
- supporting records cannot be traced;
- reviewer notes are missing.

Do not raise confidence to support a preferred recommendation.

## Evidence Refresh Workflow

1. Identify the heuristic and affected mapping fields.
2. List current supporting and conflicting evidence.
3. Check freshness, region, niche, device, and season boundaries.
4. Add new evidence records or observation summaries.
5. Preserve contradictions and explain any bounded conflicts.
6. Update confidence and stability only by human reviewer decision.
7. Record reviewer, date, SAFE UNKNOWN, and next expiration review date.

## Stale Heuristic Workflow

When evidence is stale:

- mark the mapping `needs_refresh` or `expired`;
- cap confidence until fresh evidence exists;
- keep historical evidence visible;
- define required refresh evidence;
- avoid applying the heuristic outside the last validated context;
- record human reviewer decision.

## Boundary

This workflow is human-operated documentation discipline. It is not runtime orchestration, an automated lifecycle engine, telemetry analytics, or autonomous strategic learning.
