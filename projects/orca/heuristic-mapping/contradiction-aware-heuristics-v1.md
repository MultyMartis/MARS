# Contradiction-Aware Heuristics v1

## Purpose

Defines how ORCA keeps strategic heuristics contradiction-aware. A heuristic may remain useful while still carrying visible conflicts, limits, and unresolved unknowns.

Contradictions do not disappear because a heuristic is convenient. They must remain linked, reviewed, and reflected in confidence.

## Supported Conflict Types

Record conflicts involving:

- conflicting regions;
- conflicting niche behavior;
- conflicting mobile versus desktop behavior;
- conflicting CTA behavior;
- conflicting call-first versus form-first behavior;
- seasonal conflicts;
- unstable SERP patterns;
- changing aggregator pressure;
- changed local pack behavior;
- landing evidence that conflicts with SERP evidence.

## Contradiction Status

- `open` - conflict exists and cause is not resolved.
- `bounded` - conflict is explained by region, device, season, niche, or context.
- `volatile` - conflict may be caused by unstable SERP or market movement.
- `superseded` - newer evidence replaced older support after human review.
- `unresolved_safe_unknown` - cause remains unknown and must cap confidence.

## Confidence Impact

Contradictions should:

- prevent `VERY_HIGH` confidence when unresolved;
- downgrade confidence when repeated or severe;
- narrow regional, niche, device, or seasonal applicability;
- trigger expiration review when evidence may no longer represent current conditions;
- require reviewer notes before confidence is restored.

## Handling Examples

- A mobile CTA pattern that performs as call-first in one city but WhatsApp-first in another should be region-bounded, not averaged.
- A seasonal spike that supports urgency messaging in peak months should not become year-round guidance without off-season evidence.
- A SERP pattern contradicted by newer screenshots should be marked stale or volatile until refreshed.

## Preservation Rule

Do not delete old contradictory evidence just because new evidence is stronger. Preserve it with timestamp, context, confidence impact, and reviewer decision.

## Boundary

This layer documents contradiction governance for human reviewers. It is not automated conflict resolution, self-learning revision, telemetry monitoring, or an autonomous market intelligence system.
