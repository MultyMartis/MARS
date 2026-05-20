# Semantic Observation Rules v1

## Purpose

Defines how ORCA pilot cases record semantic observations: query intent, ambiguity, commercial strength, local modifiers, and contamination risks. Semantic observations require human validation before they affect campaign architecture.

## What To Observe

- core service intent;
- urgent intent;
- local intent;
- price intent;
- comparison intent;
- branded or competitor intent;
- informational contamination;
- adjacent-service contamination;
- negative keyword candidates;
- query-to-landing fit;
- policy-sensitive terms.

## Required Fields

- query or query group;
- niche;
- region;
- device when relevant;
- intent label;
- commercial strength;
- ambiguity level;
- landing fit;
- negative keyword risk;
- confidence level;
- SAFE UNKNOWN.

## Interpretation Rules

- Classify intent from observed language and SERP context, not from assumptions.
- Treat local modifiers differently by region.
- Separate high-volume language from high-commercial-intent language.
- Do not automatically approve keywords.
- Do not automatically generate negatives without human review.
- Record semantic ambiguity instead of forcing a clean cluster.

## Common Risks

- broad service terms hiding informational intent;
- competitor names causing policy or brand risk;
- geo terms changing meaning by region;
- emergency modifiers attracting irrelevant traffic;
- price terms attracting low-quality or comparison traffic;
- service-adjacent terms contaminating clusters.

## SAFE UNKNOWN Examples

- whether query demand is stable;
- whether searcher intent differs by device;
- whether local slang changes intent;
- whether competitor brand terms are allowed;
- whether a landing page can satisfy the query.

## Boundary

Semantic observations support PPC research and QA. They do not authorize automatic keyword upload, automatic negative keyword changes, or autonomous campaign restructuring.
