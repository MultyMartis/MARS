# LEAD CARD INSTANCE REGISTRY — v1

## Phase 3H.7.3.1 (2026-08-10)
- Verdict baseline: acceptance-card canonicalization + authoritative instance v1.1
- Root cause: callback status sync used reduced `buildFinalCard`; fixed to full canonical body
- Contract: `iseo-authoritative-card-instance-v1.1`
- Soak: new final 48h restarted (does not reuse 3H.7.3 T+0); Phase 3I.1 blocked; AI OFF
- Evidence: `evidence/phase3h731/`

Contract id: `iseo-lead-card-instance-registry-v1`

## Model

Each **business lead** may have multiple Telegram **card instances**.

Multiple instances ≠ multiple business leads.

## Instance fields

| Field | Meaning |
|-------|---------|
| lead_id / stable_lead_ref | business identity |
| recipient_ref | staff recipient |
| chat reference | telegram chat id (required for sync) |
| message reference | telegram message id |
| delivery_type | `initial` \| `operator_resurface` \| other approved |
| created_at / delivered_at | timestamps |
| active/superseded state | current vs historical |
| last_sync_at / last_sync_status | sync bookkeeping |

## Authoritative rule

When an operator resurfaces a lead:

1. Newly resurfaced card per recipient becomes **authoritative current**.
2. Older initial cards may be treated as **superseded** for active sync.
3. Status sync edits authoritative current cards only (expected 4/4).
4. Stale/superseded historical edit failures must not replace semantic callback acknowledgements.

## Implementation

Admin node **Expand Card Sync Copies** selects one authoritative instance per recipient (prefer latest `operator_resurface`).

Deployed Phase 3H.7.3.



## v1.1 selection

See `iseo-authoritative-card-instance-v1.1` / `implementation/AUTHORITATIVE-CARD-SELECTION-CORRECTION-v1.md`. Case-normalized recipient keys; acceptance_canonical preferred; superseded excluded from current sync accounting.

