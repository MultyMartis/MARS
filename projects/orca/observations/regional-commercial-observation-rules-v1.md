# Regional Commercial Observation Rules v1

## Purpose

Defines how ORCA pilot cases record region-specific commercial observations. Regional evidence is critical for PPC research because SERP behavior, competition, trust expectations, and local service demand can vary strongly by geography.

## What To Observe

- local competition density;
- local pack dominance;
- aggregator pressure;
- brand dominance;
- visible price sensitivity;
- urgency pressure;
- trust signal expectations;
- local terminology;
- service-area cues;
- regional landing availability;
- ad density differences by region.

## Required Fields

- region;
- niche;
- device;
- query or query group;
- observed commercial signal;
- source;
- confidence level;
- repeatability;
- volatility;
- regional reuse limit;
- SAFE UNKNOWN.

## Interpretation Rules

- Do not generalize one region to another by default.
- Record whether the observation is city-specific, oblast-specific, or country-level.
- Treat local pack and aggregator pressure as region-sensitive.
- Separate regional commercial behavior from platform mechanics.
- Mark seasonal or event-driven demand when suspected.
- Require human validation before reuse outside the original region.

## Regional Distortion Examples

- capital city results may overstate brand and aggregator pressure;
- smaller cities may show lower ad density but higher local pack sensitivity;
- resort or seasonal regions may distort urgency and price signals;
- border or multilingual regions may change query language and intent;
- rural service areas may create landing and targeting mismatch.

## SAFE UNKNOWN Examples

- whether regional results persist over time;
- whether operator location affected SERP;
- whether competitor density is complete;
- whether local terminology is representative;
- whether seasonality is distorting demand.

## Boundary

Regional commercial observations support human-supervised PPC intelligence. They do not create automatic regional strategy, budget allocation, bid adjustment, or market conclusions.
