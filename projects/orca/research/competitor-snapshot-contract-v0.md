# ORCA Competitor Snapshot Contract v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — structured capture format for human-operated competitor research.

**Not** a crawler. **Not** a SERP API product. Future collectors must honor this schema.

## Purpose

Normalize one competitor observation into a reusable snapshot — comparable across sessions and linkable to [research-session-snapshot-contract-v0.md](research-session-snapshot-contract-v0.md).

## Storage

```
projects/orca/projects/<project-id>/competitors/snapshots/<competitor_id>-<date>.md
```

Or JSON equivalent alongside screenshots in `competitors/screenshots/`.

## Snapshot Fields

| Field | Required | Description |
|-------|----------|-------------|
| `competitor_id` | yes | Stable slug (domain or brand shorthand) |
| `source` | yes | `manual_serp` \| `manual_visit` \| `ads_transparency` \| `operator_note` \| `other` |
| `query` | yes | Query that surfaced this competitor |
| `geo` | yes | City / region context |
| `date` | yes | Observation date (ISO) |
| `URL` | if known | Landing or ad destination |
| `SERP_position` | if known | Numeric or `SAFE UNKNOWN` |
| `ad_copy` | if SERP | Headlines + text as captured |
| `landing_headline` | if visited | H1 or hero headline |
| `offer` | if visible | Price / scope / terms signals |
| `CTA` | if visible | Primary call to action |
| `price_signals` | optional | "from X", hourly, hidden pricing |
| `trust_blocks` | optional | Reviews, licenses, fleet proof |
| `weaknesses` | optional | Operator-assessed gaps (evidence-based) |
| `screenshots` | recommended | Paths under `competitors/` or `serp/` |
| `evidence_level` | yes | Per [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md) |
| `SAFE UNKNOWN` | optional | Unverified fields listed explicitly |

## Evidence Discipline

- `weaknesses` require observation support — not invented psychology.
- `price_signals` without screenshot or live capture → `evidence_level: unverified` or SAFE UNKNOWN.
- Do not store credentials, personal data, or scraped private content.

## Downstream Use

| Consumer | Use |
|----------|-----|
| Strategy docs | Positioning gaps, hook candidates |
| Negative keywords | Contamination patterns from competitor SERP |
| Landing briefs | Differentiation — not copy-paste |
| Project memory | `winning_structures` / competitor pressure notes |

## Related Documents

- [orca-research-layer-v0.md](orca-research-layer-v0.md)
- [research-session-snapshot-contract-v0.md](research-session-snapshot-contract-v0.md)
- [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md)

## Boundary

Contract for human-operated capture only. No automated competitor monitoring claimed.
