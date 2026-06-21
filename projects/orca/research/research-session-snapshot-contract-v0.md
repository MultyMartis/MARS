# ORCA Research Session Snapshot Contract v0

## Status

**PRE-IMPLEMENTATION FOUNDATION** — bounded capture of one human research session.

Not a session recorder product. Not continuous SERP monitoring.

## Purpose

Freeze **what was observed when** — so strategy later does not treat stale SERP as current truth.

## Storage

```
projects/orca/projects/<project-id>/research/sessions/<session_id>.md
```

Screenshots: `research/sessions/<session_id>/screenshots/`

## Snapshot Fields

| Field | Required | Description |
|-------|----------|-------------|
| `session_id` | yes | e.g. `rs-2026-05-21-mobile-krasnodar` |
| `project_id` | yes | Canonical project slug |
| `date_time` | yes | ISO datetime start (end optional) |
| `geo` | yes | Observation geography |
| `source_type` | yes | `mobile_serp` \| `desktop_serp` \| `competitor_visit` \| `mixed` |
| `queries` | yes | List of queries reviewed |
| `screenshots` | recommended | Paths relative to project |
| `extracted_findings` | yes | Bullet summary (operator-written) |
| `competitors_detected` | optional | List of `competitor_id` refs or names |
| `keyword_observations` | optional | Seeds, negatives, contamination notes |
| `landing_observations` | optional | Patterns from competitor landings |
| `confidence` | yes | `high` \| `medium` \| `low` — session-level |
| `stale_after` | recommended | Date after which re-run advised |
| `operator_notes` | optional | Friction, device, weather, market events |

## Child Snapshot Types (future / same session)

One session may spawn typed artifacts:

| Type | Contract |
|------|----------|
| SERP snapshot | This file + `serp/` captures |
| Competitor snapshot | [competitor-snapshot-contract-v0.md](competitor-snapshot-contract-v0.md) |
| Audit snapshot | Strategy / audit artifact refs |

Link child files via `session_id` in front-matter.

## Gate Link

Strategy citation requires `approved_for_research_use` or explicit operator override documented in `approvals/`.

## SAFE UNKNOWN

- Incomplete query set
- VPN / personalization effects unknown
- Competitor ad not seen in this session but assumed market-wide

## Related Documents

- [orca-research-layer-v0.md](orca-research-layer-v0.md)
- [competitor-snapshot-contract-v0.md](competitor-snapshot-contract-v0.md)
- [evidence-classification-system-v0.md](../evidence/evidence-classification-system-v0.md)

## Boundary

Human-operated snapshot contract. No crawler, no SERP API integration claimed.
