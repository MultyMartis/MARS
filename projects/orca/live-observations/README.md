# ORCA Live Observations

## Purpose

Defines the ORCA Live Observation Workflow v1 for human-reviewed real-world SERP and competitor landing observations.

This layer supports operational PPC research intake. It does not create autonomous scraping, browser automation, live telemetry, self-updating intelligence, runtime orchestration, automatic SERP analysis, or autonomous market intelligence.

## Scope

Use this section for:

- live SERP reviews performed by a human reviewer;
- mobile and desktop SERP comparison;
- local pack review;
- competitor landing review;
- CTA, trust, pricing, urgency, and aggregator observations;
- contradiction detection;
- evidence validation;
- confidence update inputs.

## Required Discipline

- Observations are time-bound.
- SERPs are volatile.
- Screenshots can become outdated.
- Regional variation matters.
- Conclusions remain revisable.
- All findings require human review.
- ORCA does not autonomously observe markets.
- No browser automation exists in this workflow.

## Directory Guide

- `live-observation-workflow-v1.md` - end-to-end intake flow.
- `*-review-method-v1.md` - practical review methods.
- `observation-validation-rules-v1.md` - required validation fields and rejection rules.
- `observation-update-rules-v1.md` - stale evidence, replacement, contradiction, and confidence handling.
- `templates/` - forms for structured observation intake.
- `checklists/` - reviewer checklists for operational use.
- `examples/` - fictional demonstrations only, not production evidence.

## Boundary

This is a human-supervised observation discipline. It is not scraping infrastructure, telemetry, browser automation, monitoring, deployment code, analytics dashboards, or runtime intelligence.
