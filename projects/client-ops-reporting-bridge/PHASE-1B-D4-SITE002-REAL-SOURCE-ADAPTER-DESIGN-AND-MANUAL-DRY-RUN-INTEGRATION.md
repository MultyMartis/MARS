# Phase 1B-D4 — SITE-002 Real-Source Adapter Design and Manual Dry-Run Integration

**Status:** COMPLETE (offline); D4B offline evidence baseline COMMITTED (not pushed)
**D4 readiness (historical decision artifact):** `READY_FOR_REAL_SOURCE_ADAPTER_OFFLINE_BASELINE_COMMIT`
**Post-D4B readiness:** `READY_FOR_FIRST_MANUAL_REAL_SOURCE_CONNECTION_CHARTER`
**Client Ops baseline ancestor:** `1390a3850309ee5513463fdc98fdf93d69c79fb2`
**Evidence:** [evidence/phase-1b-d4-site002-real-source-adapter/](evidence/phase-1b-d4-site002-real-source-adapter/)

## Purpose

Design and implement the real-source adapter boundary:

```
SITE-002 monitor/report
  → real-source adapter / normalization
  → Client Ops producer
  → authenticated webhook
  → n8n durable dedupe
  → Telegram
```

D4 proves this **offline** with sanitized accepted SITE-002 artifacts. No monitor execution. No real HTTP. No scheduler.

## Source authority

**SOURCE_AUTHORITY_CONFIRMED** from repository evidence (Storage reads = 0).

Authoritative artifact family: per-run directory with:

- `monitor-classification.json` (primary **action** classification)
- `changed-summary.json` (metrics)
- `run-summary.json` (run_id / timing / exit; `classification` is an **intended duplicate** of monitor-classification, not an independent health layer)

**D5R clarification (no D4 behavior change):** when `run-summary.classification` disagrees with `monitor-classification.classification`, Client Ops must continue to fail closed (`SOURCE_ARTIFACT_CONFLICT`). D5R traced disagreement to SITE-002 runner merge overwrite (`MONITOR_ARTIFACT_GENERATION_BUG`), not to expected different semantic layers. See Phase 1B-D5R evidence pack.

## Implementation

| Module | Role |
|--------|------|
| `site002_adapter.py` | parse → firewall → normalize → producer offline |
| `site002_adapter_firewall.py` | SITE-002 allowlist / reject / strip |
| `site002_adapter_constants.py` | contract version, mapping, live-block token |
| CLI `site002-adapter-dry-run` | manual explicit `--source` only |

Live attempts (`--live`, `--apply`, `--transport http`, D3 phrases) → `REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4`.

D3 synthetic runner rejects D4 real-source fixtures (consumed charter isolation).

## Fixtures

`fixtures/site-002-real-source-adapter/` — sanitized, marked `SANITIZED_FROM_ACCEPTED_SITE002_EVIDENCE`.

## Next pattern (not executed)

**B:** explicit completed monitor artifact → manual adapter → preview → operator gate → temporary n8n activate → one POST → correlate → deactivate.

## Restrictions after D4

- SITE-002 monitor connected: NO
- real SITE-002 live POST: NO
- scheduler: NO
- D3 charter: CONSUMED (cannot authorize D4 source)
- D4 real-source live: BLOCKED
- SENT ledger: DEFERRED

## Next recommendation

Phase 1B-D5 — First Manual SITE-002 Real-Source Connection Charter and Controlled Live POST

Pattern B only (explicit completed artifact → adapter preview → operator/live gate → temporary n8n activation → one bounded POST → evidence → deactivation). Do not begin D5 without a separate charter.
