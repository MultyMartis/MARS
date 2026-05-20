# Observation Update Rules v1

## Purpose

Defines how ORCA handles updates to live observations when evidence ages, conflicts, or is replaced. Updates are human-reviewed and traceable.

## Update Triggers

- stale evidence;
- new screenshot or manual observation;
- contradiction with newer evidence;
- seasonal change;
- regional mismatch;
- mobile and desktop divergence;
- local pack change;
- landing page change;
- confidence review request.

## Stale Evidence Handling

- Mark old evidence as `stale_risk` when age may affect reliability.
- Do not delete stale evidence if it explains history or contradiction.
- Reduce confidence when stale evidence supports current conclusions.
- Require new human-reviewed observation before restoring confidence.

## Evidence Replacement

Replacement evidence must include:

- reviewer;
- timestamp;
- region;
- device;
- source;
- screenshot reference;
- reason for replacement;
- impact on prior conclusions.

Replacement does not erase older evidence. It supersedes it with visible reasoning.

## Contradiction Preservation

When new evidence conflicts with old evidence:

- keep both observations;
- record contradiction type;
- note region, device, timestamp, and query differences;
- explain confidence impact;
- use SAFE UNKNOWN when cause is unclear.

## Confidence Reduction

Reduce or cap confidence when:

- evidence is aging;
- screenshots no longer match current SERP;
- local pack layout changes;
- aggregator pressure changes;
- landing claims disappear;
- seasonal demand invalidates prior behavior;
- regional evidence is applied outside its observed region.

## Seasonal and Regional Invalidation

Seasonal invalidation applies when demand, urgency, pricing, or availability claims likely changed due to season.

Regional invalidation applies when evidence from one city, district, or service area is reused without local review.

Both require a fresh human review before confidence can increase.

## Boundary

These rules manage human-reviewed evidence updates. They are not self-updating intelligence, monitoring, telemetry, automation, scraping, or runtime orchestration.
