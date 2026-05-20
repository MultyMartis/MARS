# Pattern Confidence Model v1

## Purpose

Defines confidence levels for ORCA pilot observations and repeated commercial patterns. Confidence indicates how cautiously a pattern may be reused in human-reviewed PPC research. It does not authorize automatic optimization or strategic decisions.

## Confidence Levels

## LOW

Use LOW when evidence is thin, unclear, stale, or strongly contextual.

Typical signals:

- single observation;
- one query only;
- uncertain region or device;
- weak source quality;
- high personalization risk;
- strong contradiction;
- missing timestamp.

Allowed use: note as a lead for follow-up research only.

## MEDIUM

Use MEDIUM when a pattern appears more than once but remains context-limited.

Typical signals:

- repeated within one pilot case;
- visible across several related queries;
- region and device are known;
- evidence is current;
- some volatility or contradiction remains.

Allowed use: inform human review, QA focus, and hypothesis building.

## HIGH

Use HIGH when a pattern is repeated, current, and supported by multiple sources or cases.

Typical signals:

- repeated across queries and SERP snapshots;
- consistent in the same region and niche;
- supported by landing or competitor review;
- low-to-medium volatility;
- contradictions are explained.

Allowed use: reusable intelligence candidate for similar cases with context limits.

## VERY HIGH

Use VERY HIGH only when a pattern is repeatedly validated across time, cases, and evidence types.

Typical signals:

- repeated across multiple pilot cases;
- stable across observation dates;
- supported by SERP, landing, competitor, and local evidence;
- clear regional boundary;
- low contradiction;
- human-reviewed reuse history.

Allowed use: strong reusable intelligence for human-supervised planning. It still does not become an automatic campaign rule.

## Repeated Observation Logic

Repeated observations increase confidence only when they are comparable:

- same or clearly related niche;
- defined region;
- similar device context;
- current timestamps;
- comparable query intent;
- independently reviewed evidence.

Repetition from the same unstable source should not be treated as strong evidence.

## Contradictory Evidence Handling

Contradictions must be recorded, not averaged away.

- If contradiction is unexplained, cap confidence at MEDIUM.
- If contradiction is region-specific, split the pattern by region.
- If contradiction is device-specific, split by device.
- If contradiction is seasonal, mark the pattern as season-bound.
- If contradiction is caused by weak evidence, keep SAFE UNKNOWN.

## Unstable SERP Risks

SERP layout, ads, local pack visibility, aggregator placement, and personalization can change quickly. High volatility lowers confidence and requires fresh validation before reuse.

## Seasonal Distortion Risks

Seasonal demand can distort urgency, price sensitivity, offer patterns, ad density, and local pack behavior. Mark observations as season-bound when timing may affect interpretation.

## Regional Distortion Risks

Region affects competitor density, aggregator strength, local trust signals, price sensitivity, and CTA behavior. Do not transfer confidence from one region to another without new evidence.

## Boundary

Confidence scoring is a research discipline. It is not a model for automatic bidding, automatic budget allocation, automatic keyword decisions, or autonomous strategic conclusions.
