# Pilot Execution Flow v1

## Purpose

Defines a repeatable, human-supervised flow for running ORCA PPC pilot cases. The flow accumulates observations and intelligence without introducing scraping, browser automation, live optimization, or autonomous campaign control.

## Flow

1. Define pilot case scope.
2. Capture niche, region, device, search engine, and business context.
3. Collect manual or human-directed SERP snapshots.
4. Record competitor, local pack, aggregator, offer, CTA, trust, and landing observations.
5. Normalize observations using the observation model.
6. Identify semantic, landing, QA, and campaign architecture implications.
7. Assign confidence using the pattern confidence model.
8. Produce a pilot report.
9. Extract reusable intelligence only after human review.
10. Archive SAFE UNKNOWN and follow-up questions.

## Required Inputs

- Business or niche description.
- Target region and service area.
- Device context.
- Search engine context.
- Seed queries.
- Landing page or landing type.
- Known exclusions and constraints.
- Human operator.

## Required Outputs

- Completed pilot case record.
- Normalized observations.
- Confidence notes.
- SAFE UNKNOWN list.
- Pilot report.
- Reusable intelligence candidates.

## Human Review Gates

- Scope approval before observations begin.
- Evidence review before confidence scoring.
- Strategic review before intelligence reuse.
- QA review before any campaign architecture recommendation is reused.

## Evidence Discipline

- Treat SERP data as time-bound.
- Treat region as a major behavior factor.
- Separate observation from interpretation.
- Record contradictions instead of hiding them.
- Use SAFE UNKNOWN when evidence is missing.
- Avoid market conclusions from single snapshots.

## Prohibited Actions

- Automatic campaign edits.
- Automatic bidding or budget decisions.
- Automatic keyword upload.
- Automatic negative keyword upload.
- Automatic landing page changes.
- Autonomous competitor conclusions.
- Scraping or browser automation.
- Live monitoring claims.

## Completion Criteria

A pilot case is complete when the operator has recorded the evidence, normalized the observations, assigned confidence, listed unknowns, and produced a reviewed report. Completion does not mean the market has been fully understood or that a campaign should be automatically changed.
