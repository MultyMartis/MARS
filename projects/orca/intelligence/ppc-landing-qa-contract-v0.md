# ORCA PPC Landing QA Contract v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — human QA checklist for landings built from ORCA → Website Factory.

Not automated Lighthouse gate. Not a substitute for platform ad policy review.

## Purpose

Verify continuity between approved ads/briefs and implemented landing pages **before** assigning URLs in Commander or marking `approved_for_ads`.

## When to Run

After Factory implementation reaches reviewable build (staging or dist), **before** updating [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md) status.

## Checks

| # | Check | Pass criterion |
|---|-------|----------------|
| 1 | Search intent continuity | Hero + first screen match query intent tier from brief |
| 2 | Ad headline ↔ hero H1 | Approved ad headline aligns with H1 (semantic, not necessarily byte-equal) |
| 3 | CTA consistency | Primary CTA matches brief (call / form / messenger priority) |
| 4 | Offer consistency | Price framing, tonnage, scope match approved brief |
| 5 | Trust consistency | Review sources, ratings, legal refs match approved claims |
| 6 | No fake claims | No invented stats, fleet, or guarantees |
| 7 | Qualification blocks | Anti-junk / anti-broad filters present where brief requires |
| 8 | Mobile CTA visibility | Primary CTA visible without excessive scroll on mobile |
| 9 | Form simplicity | Fields match brief; no surprise required fields |
| 10 | Region consistency | Geo text matches campaign geo |
| 11 | Route consistency | Built `slug` matches registry `route_id` / `slug` |
| 12 | Semantic lock compliance | MODE 1: no unauthorized copy changes per [orca-website-factory-semantic-lock-v0.md](orca-website-factory-semantic-lock-v0.md) |

## QA Statuses

| Status | Meaning |
|--------|---------|
| `draft` | Implementation in progress; QA not started |
| `needs_fix` | Failures logged; Factory or copy fix required |
| `approved_for_ads` | Human sign-off — URL may enter ads / registry |
| `approved_for_launch` | Launch gate satisfied (with [approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)) |

## Output

Recommended: `projects/orca/projects/<project-id>/artifacts/qa/landing-qa-<route_id>-<date>.md`

Minimum content:

- `route_id`
- checker name / date
- pass/fail per check
- findings (max practical detail)
- final status

## SAFE UNKNOWN

- Analytics not yet available — do not infer performance
- A/B variant not in brief
- Third-party widget behavior unverified

## Related Documents

- [landing-route-registry-contract-v0.md](landing-route-registry-contract-v0.md)
- [orca-factory-bridge-index-v0.md](orca-factory-bridge-index-v0.md)
- [approval-gates-contract-v0.md](../artifacts/approval-gates-contract-v0.md)
- Triumph: `ppc/triumph-manipulator/validation/landing-continuity-rules-v1.md` (pack-specific rules, complementary)

## Boundary

Human-operated QA contract. AI may assist checklist drafting; **human** sets `approved_for_ads`.
