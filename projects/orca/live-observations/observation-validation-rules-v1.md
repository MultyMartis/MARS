# Observation Validation Rules v1

## Purpose

Defines minimum validation rules for ORCA live observations. Validation is human-reviewed and evidence-first. It does not make an observation permanent or absolute.

## Required Validation Fields

- observation ID;
- reviewer;
- timestamp and timezone;
- evidence source;
- region;
- device;
- query or landing URL;
- screenshot reference;
- contradiction notes;
- SAFE UNKNOWN notes;
- confidence review;
- volatility review.

## Acceptance Rules

An observation can be accepted when:

- required context is present;
- the evidence source is traceable;
- visible claims are separated from interpretation;
- region, device, and query boundaries are clear;
- screenshot or manual evidence reference is recorded;
- contradictions are noted;
- confidence does not exceed evidence strength.

## Rejection or Limitation Rules

Mark as `needs_more_evidence`, `accepted_with_limits`, or `rejected` when:

- timestamp is missing;
- reviewer is missing;
- region is missing;
- source cannot be traced;
- screenshot reference is missing for visual claims;
- SERP volatility is high and not noted;
- conclusions exceed the evidence;
- findings are synthetic-only;
- automation, scraping, or telemetry is implied as source.

## Volatility Review

Reviewers must consider:

- result order instability;
- ad block changes;
- local pack appearance changes;
- device differences;
- regional variation;
- personalization risk;
- seasonal demand;
- screenshot aging.

## Confidence Review

Confidence must stay low or capped when:

- evidence is single-snapshot only;
- contradictions remain open;
- region or device transfer is unvalidated;
- screenshot evidence is old;
- live review cannot be repeated;
- SAFE UNKNOWN fields affect the conclusion.

## Boundary

These rules define manual evidence validation. They are not autonomous QA, runtime validation, scraping validation, telemetry validation, or self-learning intelligence.
