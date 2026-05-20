# Landing Analysis Framework v1

## Purpose

Defines how ORCA reviews landing pages for PPC relevance, local lead generation, and conversion readiness.

## Required Analysis Areas

- Offer clarity - user can immediately understand the service.
- CTA strength - call, form, quote, booking, or messenger action is visible.
- Trust architecture - reviews, cases, licenses, guarantees, photos, address, team, proof.
- Pricing transparency - prices, ranges, quote logic, or reason for no price.
- Urgency - same-day, emergency, schedule, availability, response time.
- Differentiation - why this provider over aggregators or competitors.
- Lead capture structure - friction, required fields, phone visibility, mobile forms.
- Mobile commercial quality - fast path to action on small screens.
- Local trust signals - city, district, address, map, local reviews, service area.
- Conversion friction - distractions, unclear navigation, slow steps, weak forms.

## QA Outcomes

- `landing_ready`.
- `landing_ready_with_warnings`.
- `landing_needs_revision`.
- `landing_mismatch`.
- `safe_unknown`.

## Practical Rules

- Do not send hot commercial traffic to weak generic pages.
- Do not use local queries without local proof.
- Do not use urgent ads if the landing does not support urgent action.
- Do not use price-focused copy without price context or quote logic.

## Boundary

Landing analysis is review guidance. It does not edit sites, run CRO automation, publish campaigns, optimize bids, or operate runtime workflows.
