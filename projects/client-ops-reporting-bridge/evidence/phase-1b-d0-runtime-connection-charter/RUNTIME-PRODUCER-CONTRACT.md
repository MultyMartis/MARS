# Runtime Producer Contract — Phase 1B-D0

**Status:** CONTRACT for future R1 producer (not implemented)
**Preferred pattern:** R1 — Exporter as producer
**Fallback pattern:** R3 — File/report pickup adapter

## Local exporter assessment (CURRENT / PROVEN)

| Topic | Finding |
|-------|---------|
| Paths | `projects/client-ops-reporting-bridge/src/client_ops_reporting_bridge/` (+ fixtures/tests) |
| Input contract | Required: `monitor-classification.json`, `changed-summary.json`, `run-summary.json`; optional `run.log` |
| Envelope | `mars.client_ops.report` / `1.0` / `site.post_1c_monitor` / SITE-002 |
| Network POST | **Absent**; `push-webhook` not implemented; tests assert no `urlopen` |
| Intentional block | **Yes** — Phase 1A offline-only |
| Dry-run | `validate-only` (no write); `build-envelope` writes only approved local paths |
| Secret loading | **None** in exporter core today |
| Retry/replay controls | **None** |
| Suitability as first controlled runtime producer | **Yes, after** durable dedupe + POST capability + secrets/endpoint profile |
| Required changes before webhook call | Add authenticated POST mode; load ignored secrets; timeouts; retry policy respecting same `event_id`; local evidence writer; refuse dirty-main scheduled use |

**Do not modify exporter in D0.**

## SITE-002 monitor assessment (CURRENT)

| Topic | Finding |
|-------|---------|
| Source | Post-1C catalog onboarding monitor (`monitor-02` lineage) under OCPilot SITE-002 tools |
| Report root | Storage scheduled-monitors `post-1c/YYYY-MM-DD_HH-mm-ss/` (operational path; not for envelope) |
| Invocation | Manual supported; Windows Task `MARS_SITE_002_Post_1C_Catalog_Monitor` exists |
| Output | JSON/MD artifacts including classification, changed-summary, run-summary, logs |
| Stable event ID | Monitor does **not** emit Client Ops `event_id`; exporter computes it |
| OK/ATTENTION/FAILED/BLOCKED | Via Client Ops normalization mapping (proven offline) |
| Sensitive data | Absolute paths, raw logs, possible secrets references — must be sanitized by exporter |
| Direct monitor→n8n | **Not appropriate** (R2 rejected) |
| Adapter/exporter boundary | **Required** (R1/R3) |

**Do not run or modify monitor in D0.**

## First producer obligations (REQUIRED BEFORE RUNTIME CONNECTION)

1. Emit distributable envelope only when security gate passes.
2. Reuse `event_id` on retries.
3. Consult durable dedupe outcome semantics after HTTP response (and locally if fallback ledger used).
4. Never log secret values or full webhook URL to Git.
5. Write sanitized producer evidence (run id, event id, HTTP status, elapsed, failure class).

## Forbidden without new charter

- Connecting SITE-002 monitor directly to webhook.
- Scheduling producer from dirty `X:\AI MARS`.
- Enabling automatic unbounded retries.
- Production activation.
