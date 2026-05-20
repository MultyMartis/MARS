# Live Observation Workflow v1

## Purpose

Defines how ORCA collects, validates, normalizes, and integrates human-reviewed live SERP and landing observations into intelligence records.

Live observation means a human reviewer manually inspects current search results or landing pages and records evidence. ORCA does not autonomously observe markets, run browsers, scrape pages, monitor SERPs, or update intelligence without review.

## Workflow Stages

1. Prepare review context.
2. Capture visible evidence.
3. Normalize observations.
4. Validate evidence.
5. Check contradictions.
6. Update confidence when justified.
7. Integrate into ORCA records with boundaries.

## 1. Prepare Review Context

Record before interpretation:

- reviewer;
- timestamp and timezone;
- region and localization notes;
- device type;
- search engine;
- exact query;
- niche or service category;
- personalization risk;
- screenshot reference or manual evidence source.

If any required context is missing, mark it as `SAFE UNKNOWN` and cap confidence.

## 2. Capture Visible Evidence

Record what is visible before making conclusions:

- ad block presence and count;
- local pack presence;
- organic overlap with paid results;
- aggregator or directory presence;
- CTA patterns;
- trust patterns;
- pricing visibility;
- urgency signals;
- landing page links or visible destination types;
- mobile versus desktop differences when both are reviewed.

Do not infer bids, budgets, conversion rates, targeting strategy, account maturity, or competitor intent from result order alone.

## 3. Normalize Observations

Convert notes into bounded statements:

- `observed`: directly visible in evidence;
- `inferred_with_limits`: reasonable interpretation with explicit basis;
- `contradicted`: conflicts with another observation;
- `stale_risk`: likely to age quickly;
- `SAFE_UNKNOWN`: not supported by current evidence.

Every normalized observation must keep timestamp, region, device, query, evidence source, and reviewer.

## 4. Validate Evidence

Validation requires:

- timestamp;
- reviewer;
- evidence source;
- region;
- device;
- query or landing URL;
- screenshot reference where available;
- contradiction notes;
- SAFE UNKNOWN notes;
- volatility review;
- confidence review.

Unsupported notes remain research notes, not ORCA intelligence.

## 5. Check Contradictions

Compare the observation against:

- prior ORCA observations;
- mobile versus desktop findings;
- regional differences;
- seasonal or time-of-day effects;
- landing claims versus SERP claims;
- local pack signals versus landing trust claims;
- aggregator pressure in current versus prior reviews.

Contradictions must be preserved, not averaged away.

## 6. Update Confidence

Confidence can increase only when evidence is current, traceable, repeated, and human-reviewed.

Confidence must decrease or be capped when:

- evidence is stale;
- SERP volatility is high;
- region or device context is missing;
- screenshots are outdated;
- contradictions remain open;
- seasonal or regional transfer is unvalidated.

## 7. Integrate Safely

When integrated into ORCA intelligence records, include:

- observation summary;
- evidence references;
- confidence impact;
- contradiction impact;
- age and volatility notes;
- regional and device boundaries;
- next review trigger.

## Boundary

This workflow is operational discipline for human-supervised PPC observation. It is not autonomous scraping, browser automation, telemetry, live monitoring, automatic SERP analysis, or self-updating intelligence.
