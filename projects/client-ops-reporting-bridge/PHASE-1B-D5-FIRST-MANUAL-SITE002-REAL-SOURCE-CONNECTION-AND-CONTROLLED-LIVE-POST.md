# Phase 1B-D5 — First Manual SITE-002 Real-Source Connection and Controlled Live POST

**Status:** PARTIAL — Part A DONE; Part B LIVE POST NOT EXECUTED  
**Pre-live readiness:** `NOT_READY_FOR_ONE_MANUAL_REAL_SOURCE_POST`  
**Readiness:** `NOT_READY_FOR_FIRST_MANUAL_REAL_SOURCE_CONNECTION_BASELINE_COMMIT`  
**Preview verdict:** `REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST`  
**Final verdict:** `PARTIAL — MANUAL SITE-002 REAL-SOURCE CONNECTION NOT STARTED; PRE-LIVE GATE BLOCKED`  
**Task HEAD:** `f92ba003c981bb7ba6025865998f439b0f4ce756`  
**Client Ops ancestor OK:** `fe3a1b64`  
**Branch:** `mars/canonical-post-recovery`  
**Evidence:** [evidence/phase-1b-d5-first-manual-site002-real-source-connection/](evidence/phase-1b-d5-first-manual-site002-real-source-connection/)

## Purpose

Authorize and execute **one** manual SITE-002 real-source controlled live POST under Pattern B:

```
explicit completed SITE-002 monitor artifact
  → D4 adapter preview (formal full adapter)
  → operator / live gate
  → temporary n8n activate
  → one bounded HTTPS POST (max HTTP=1)
  → correlate
  → deactivate
```

## Pattern

**Pattern B only.** Explicit completed run directory. No latest/watch/auto-discovery. No scheduler connection.

## Parts

| Part | Scope | Result |
|------|-------|--------|
| **A** | D5 modules, gates, CLI, phrases, marker, transport reuse, tests | DONE |
| **B** | Pre-live source safety → approve one source → controlled live POST | BLOCKED — not executed |

## Part A — Implementation (DONE)

| Item | Value |
|------|-------|
| Modules | `producer_d5.py`, `producer_d5_gates.py` |
| CLI | `site002-controlled-live` |
| Marker | `mars-client-ops-site002-real-source-d5` |
| Max HTTP | 1 |
| Concurrency | 1 |
| Retries | 0 |
| Transport | `create_d5_live_transport` reuses D3 HTTPS allowlist/TLS |
| D3 charter | remains CONSUMED (cannot authorize D5 source) |
| D4 live | remains BLOCKED |
| Charter local path | `local/client-ops-reporting-bridge/bzpm.ru/runs/d5-manual-real-source/` (UNUSED; `real_http_requests=0`) |

### Exact D5 phrases

1. `ENABLE ONE MANUAL SITE002 REAL SOURCE D5 BZPM`
2. `ACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`
3. `SEND ONE MANUAL SITE002 REAL SOURCE EVENT D5 BZPM`
4. `DEACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`
5. `EMERGENCY DEACTIVATE CLIENT OPS MANUAL REAL SOURCE D5 BZPM`

Environment: `manual_real_source_controlled` only. Requires `--apply` plus enable + send phrases for live.

## Part B — Pre-live source inspection (BLOCKED)

Canonical artifact root class (sanitized): `STORAGE/ocpilot/.../scheduled-monitors/post-1c/`

| Metric | Value |
|--------|-------|
| Candidates inspected (formal full adapter) | 3 |
| Authoritative JSON files read | 9 (3 per candidate) + limited classification-pair probes |
| Raw logs read | 0 |
| Storage mutations | 0 |
| Monitor executions | 0 |
| Live POST | NOT EXECUTED |
| Network calls (producer/n8n/Telegram) | 0 |

All three candidates **REJECTED**. Pre-live source safety blocked live.

### Candidate summary

| # | Label | Adapter outcome | Why rejected |
|---|-------|-----------------|--------------|
| 1 | `site002-post-1c-run/2026-07-26_12-30-02` | `SOURCE_ARTIFACT_CONFLICT` → BLOCKED | Fresh; monitor ONBOARDING_REQUIRED vs run-summary NO_ACTION_REQUIRED |
| 2 | `site002-post-1c-run/2026-07-20_22-32-43` | `SOURCE_REPORT_STALE` → BLOCKED | MATCH quiet run but age > STALE_AFTER_SECONDS=93600; Telegram would mislead |
| 3 | `site002-post-1c-run/2026-07-20_12-45-01` | `SOURCE_REPORT_STALE` → BLOCKED | MATCH ONBOARDING_REQUIRED but stale; message would mislead |

**Primary inspected (documentation):** Candidate 1 — fresh real source, rejected.  
**Selected for live:** none.

### Systemic note (sanitized)

Recent scheduled runs (≈21–26 Jul) show monitor vs run-summary classification **CONFLICT**. Older **MATCH** runs are **STALE** under `STALE_AFTER_SECONDS=93600`. No monitor execution was authorized to mint a fresh MATCH run.

### D5R authority follow-up (historical D5 unchanged)

D5 historical verdict remains:

`PARTIAL — MANUAL SITE-002 REAL-SOURCE CONNECTION NOT STARTED; PRE-LIVE GATE BLOCKED`

**D5R (later analysis, Client Ops evidence only):** root cause confirmed as `MONITOR_ARTIFACT_GENERATION_BUG` in SITE-002 runner `Finish-Summary` overwrite of `run-summary.classification` after Python exported matching values. Client Ops fail-closed conflict behavior in D5 was **correct** and must not be papered over. SITE-002 repair is required before a truthful D5 live retry. See [PHASE-1B-D5R…](PHASE-1B-D5R-SITE002-MONITOR-CLASSIFICATION-AUTHORITY-ALIGNMENT-AND-FRESH-SAFE-SOURCE-REASSESSMENT.md).

## Caps and containment

- Max real HTTP requests: **1**
- Concurrency: **1**
- Retries: **0**
- Workflow activation: temporary only under D5 phrases (never activated in Part B)
- Scheduler: **NO**
- Monitor execution: **NO**
- Workflow PUT / graph change: **NO**
- Data Table admin mutation: **NO**

## Expected Client Ops pre-state (charter baseline)

Live GET for D5 pre-state was **not** performed (`prelive_get_performed=false`). Values below are the expected pre-D5 baseline from prior charter evidence:

| Field | Expected |
|-------|----------|
| Workflow | `tkM4H0G0gM3q9Foi` |
| versionId | `3d2fd6fc-bc17-4e0f-b9e5-086c959afd29` |
| active | false |
| nodes | 17 |
| executions | 31 |
| running | 0 |
| Data Table | `H6VYhwz7RXZCBMmu` rows=2 |

`live_state_verified`: false / UNKNOWN for this D5 evidence pack.

## Non-goals / forbidden in D5

- Scheduler connection or recommendation
- Unattended / automatic source pick
- Monitor execution to mint fresh artifacts (without a separate repair charter)
- Second real-source POST
- Reuse of D3 synthetic charter for real source
- Absolute Storage paths or secrets in Git evidence

## Readiness labels

| Label | Value |
|-------|-------|
| Preview | `REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST` |
| Pre-live | `NOT_READY_FOR_ONE_MANUAL_REAL_SOURCE_POST` |
| Baseline commit readiness | `NOT_READY_FOR_FIRST_MANUAL_REAL_SOURCE_CONNECTION_BASELINE_COMMIT` |
| Verdict | `PARTIAL — MANUAL SITE-002 REAL-SOURCE CONNECTION NOT STARTED; PRE-LIVE GATE BLOCKED` |

## Next recommendation

**Phase 1B-D5R — SITE-002 Monitor Classification Authority Alignment and Fresh Safe-Source Reassessment**

Do **not** recommend scheduler. Repair classification authority conflict and reassess for a fresh safe MATCH source before any live POST.
