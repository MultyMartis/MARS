# Ad Relevance QA v1

## Purpose

Checks whether draft ad copy is relevant, supported, and safe enough for human review in search PPC.

## Checks

- Keyword and ad group intent is reflected in headline and description.
- CTA matches user intent: call, calculate, book, request quote, order.
- Claims are supported by landing page or business evidence.
- Urgency wording is operationally true.
- Local wording matches actual service area.
- B2B/B2C audience is not mixed.
- Competitor or brand references are separately reviewed.
- Platform character limits are checked where known.

## Yandex.Direct Notes

- Ad copy should align tightly with query intent and landing content.
- Medical, financial, legal, repair, emergency, and guarantee claims need extra review.
- Human approval is mandatory before upload or import.

## Failure Signals

- Generic copy for highly specific clusters.
- Price promise without visible price proof.
- Urgent CTA without operational capability.
- Local claim without local trust signal.
- Informational query receiving hard-sell copy.

## Boundary

Ad relevance QA reviews drafts only. It does not publish ads, run A/B tests, automate copy optimization, or manage live account performance.
