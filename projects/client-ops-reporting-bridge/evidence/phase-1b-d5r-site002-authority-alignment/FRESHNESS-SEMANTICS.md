# FRESHNESS-SEMANTICS

## Decision

`FRESHNESS_STATUS_SEMANTICS_REQUIRES_SEPARATE_REPAIR`

## Current behavior (unchanged in D5R)

- `STALE_AFTER_SECONDS = 93600` (~26h)
- `age_seconds > threshold` → `SOURCE_REPORT_STALE` → client-facing `BLOCKED`
- Phase 0A / REPORT-CONTRACT freeze: `freshness.stale=true` forces BLOCKED site status

## Problem observed in D5

Matching historical quiet/onboarding runs are truthful source observations, but delivery maps them to client-facing BLOCKED, which can misrepresent “scheduler/review failure” instead of “historical OK/ATTENTION not eligible to send.”

## Preferred future separation (not implemented in D5R)

| Field | Meaning |
|-------|---------|
| `source_status` / factual monitor result | OK / ATTENTION / FAILED from consistent authorities |
| `delivery_eligibility` | `FRESH` \| `STALE_REVIEW_REQUIRED` \| `NOT_SAFE_TO_SEND` |

Stale ⇒ do not send; do not falsify original monitor status in the factual layer.

## Why not repaired in D5R

1. Primary blocker is emitter classification corruption (`MONITOR_ARTIFACT_GENERATION_BUG`).
2. Client Ops adapter changes are authorized in D5R only when emitter is coherent and no SITE-002 repair is required.
3. Freshness/delivery split is a contract-visible change touching normalizer + envelope semantics; requires its own charter after (or coordinated with) monitor repair.

Threshold `93600` may remain as delivery eligibility threshold unless a later charter retunes it.
