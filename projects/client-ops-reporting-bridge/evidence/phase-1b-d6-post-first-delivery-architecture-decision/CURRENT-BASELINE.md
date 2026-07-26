# CURRENT BASELINE — Phase 1B-D6

## Accepted canonical baseline

| Field | Value |
|-------|-------|
| Commit | `e9c9be59f643e66970930e31339431acb8077b55` |
| Subject | feat(client-ops): record first verified site002 real-source delivery |
| Verdict | COMPLETE — FIRST VERIFIED SITE-002 REAL-SOURCE DELIVERY EVIDENCE COMMITTED; CLIENT OPS REMAINS CONTAINED |
| Readiness (prior) | READY_FOR_CLIENT_OPS_NEXT_CONTROLLED_ARCHITECTURE_PHASE |

## First verified real-source delivery

| Field | Value |
|-------|-------|
| run_id | `2026-07-26_17-48-38` |
| event_id | `c84e29bf-79b1-5aea-98c4-9dc8d651fc96` |
| source classification | ONBOARDING_REQUIRED |
| mapped status | ATTENTION |
| Acceptance | `D5R2A_FIRST_SEEN_DELIVERY_VERIFIED` |
| n8n execution | 3416 / success / webhook / FIRST_SEEN |
| Telegram sanitized message_id | 7 |
| activation changes | 2; final `active=false` |

## D6 GET-only live reconfirmation

Method: GET-only (`_get-precheck.mjs` + supplemental GET for row fields). Mutations: **0**.

| Check | Expected | Observed | Match |
|-------|----------|----------|-------|
| workflow active | false | false | YES |
| nodes | 17 | 17 | YES |
| versionId | `3d2fd6fc-bc17-4e0f-b9e5-086c959afd29` | same | YES |
| executions | 32 | 32 | YES |
| running | 0 | 0 | YES |
| latest execution | 3416 success | 3416 success | YES |
| Data Table columns | 15 | 15 | YES |
| Data Table rows | 3 | 3 | YES |
| selected event rows | 1 | 1 | YES |
| intake_state | FIRST_SEEN | FIRST_SEEN | YES |
| event_status | ATTENTION | ATTENTION | YES |
| delivery_state | PENDING (SENT not required) | PENDING | YES |

**Verdict:** `D6_BASELINE_RECONFIRMED`

Note: `_get-precheck.mjs` still embeds pre-D5R2A expected values (executions=31, rows=2). D6 evaluates against post-D5R2A / D5R2AB accepted containment, not that script’s outdated expected block.

## Runtime reconfirmation

| Check | Expected | Observed |
|-------|----------|----------|
| Path | `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo` | same |
| HEAD | `8bb6e8f0…` | exact match |
| porcelain | EMPTY | EMPTY |
| Scheduler `MARS_SITE_002_Post_1C_Catalog_Monitor` | Ready / not Running | Ready |

No monitor execution. No scheduler execution. No runtime modification.

## Containment (unchanged)

- Automatic monitor→producer: **NO**
- Unattended adapter: **NO**
- Watcher: **NO**
- Automatic retries: **NO**
- Generic producer live: **BLOCKED**
- Production activation: **NO**
- Durable SENT ledger: **DEFERRED**
- Freshness semantics repair: **DEFERRED**

## MAIN preflight notes (foreign WIP)

- Branch: `mars/canonical-post-recovery`
- HEAD: `e9c9be59…` (matches accepted baseline)
- Volume: `X:` / `AI WS`
- Pre-existing **staged** deletions (~76 paths) of prior Client Ops evidence/charters observed as foreign WIP — **not** created or modified by D6; **not** restored/cleaned/committed.
- D6 writes only new documentation under allowlisted Client Ops paths; **no** `git add` / commit / push.
- `MAIN_INDEX_UNTOUCHED_BY_D6` (task performs zero index mutations)
