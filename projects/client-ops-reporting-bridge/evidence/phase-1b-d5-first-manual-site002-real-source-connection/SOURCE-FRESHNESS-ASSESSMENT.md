# SOURCE-FRESHNESS-ASSESSMENT

**STALE_AFTER_SECONDS:** 93600 (26 hours)  
**Root class:** `STORAGE/ocpilot/.../scheduled-monitors/post-1c/`  
**Monitor executions authorized:** 0

## Candidate 1 — fresh, CONFLICT

| Field | Value |
|-------|-------|
| Label | `site002-post-1c-run/2026-07-26_12-30-02` |
| Observed | 2026-07-26T05:33:06Z |
| Age | ~hours — within stale window (fresh) |
| Monitor class | ONBOARDING_REQUIRED |
| Run-summary class | NO_ACTION_REQUIRED |
| Adapter | SOURCE_ARTIFACT_CONFLICT → BLOCKED |
| Live-safe | NO |

## Candidate 2 — MATCH quiet, STALE

| Field | Value |
|-------|-------|
| Label | `site002-post-1c-run/2026-07-20_22-32-43` |
| Observed | 2026-07-20T15:33:03Z |
| Age | ~6 days — **>** 26h threshold |
| Classes | NO_ACTION_REQUIRED / NO_ACTION_REQUIRED (MATCH) |
| Metrics | baseline=1737 current=1737 added=0 removed=0 onboarding=0 |
| Adapter | SOURCE_REPORT_STALE → BLOCKED |
| Live-safe | NO (client-facing BLOCKED/stale wording misleading for historically OK quiet run) |

## Candidate 3 — MATCH onboarding, STALE

| Field | Value |
|-------|-------|
| Label | `site002-post-1c-run/2026-07-20_12-45-01` |
| Observed | 2026-07-20T06:10:33Z |
| Age | stale under 93600 |
| Classes | ONBOARDING_REQUIRED / ONBOARDING_REQUIRED (MATCH) |
| Adapter | SOURCE_REPORT_STALE → BLOCKED |
| Live-safe | NO |

## Systemic note

Recent scheduled runs (≈21–26 Jul): monitor vs run-summary classification **CONFLICT**. Older MATCH runs are **STALE**. No authorized monitor execution to mint a fresh MATCH run. Pre-live source safety therefore blocks all live candidates.
