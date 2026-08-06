# PHASE 1B-D6D — Unattended Monitor-to-Client-Ops Integration Contract

**Mode:** OFFLINE ONLY
**D6D_UNATTENDED_PRODUCTION_ENABLED:** NO
**D6D_RUNTIME_DEPLOYMENT_AUTHORIZED:** NO
**D6D_SCHEDULER_CREATION_AUTHORIZED:** NO

## Roadmap

A → B → C → E → **D** (this phase)

## Purpose

Deterministic fail-closed integration layer that can later connect completed SITE-002 monitor artifacts to Client Ops without operator hand-building each envelope.

**Unattended means:** a separately scheduled and bounded producer evaluates completed artifacts (`D6D_UNATTENDED_MEANS_BOUNDED_SCHEDULED_PRODUCER`).

It does **not** mean always-on workflow, blind POST, retry loops, filesystem watchers, dirty MAIN execution, or bypass of A/B/C/E gates.

## Implementation (offline)

| Layer | Path |
|-------|------|
| Constants / exit codes / gate order | `n8n/runners/lib/client-ops-d6d-constants.mjs` |
| Kill switch | `n8n/runners/lib/client-ops-d6d-kill-switch.mjs` |
| Producer singleton lock | `n8n/runners/lib/client-ops-d6d-producer-lock.mjs` |
| Cursor | `n8n/runners/lib/client-ops-d6d-cursor.mjs` |
| Artifact discovery/stabilize/identity | `n8n/runners/lib/client-ops-d6d-artifact.mjs` |
| Receipt | `n8n/runners/lib/client-ops-d6d-receipt.mjs` |
| Runtime/scheduler gates | `n8n/runners/lib/client-ops-d6d-runtime-gates.mjs` |
| Orchestrator | `n8n/runners/lib/client-ops-d6d-unattended-producer.mjs` |
| Harness D1–D60 + DS1–DS10 | `n8n/harness/d6d-unattended-integration-harness.mjs` |
| Python language boundary | `src/client_ops_reporting_bridge/unattended_d6d.py` |
| Python tests | `tests/test_unattended_d6d.py` |

Composes existing Workstream B freshness, C lifecycle, and E retry policy modules without semantic drift.

## Authoritative source

Completed scheduled run directory under:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\<run_id>\`

Required machine-readable files: `run-summary.json`, `monitor-classification.json`, `changed-summary.json`, plus D6D completion marker `run-complete.marker`.

## Evidence

`evidence/phase-1b-d6d-unattended-monitor-to-client-ops-integration-contract/`

## Next (not started)

Phase 1B-D6D2 — Unattended Producer Controlled Runtime Deployment and Dry-Run Verification

Requires D6D baseline commit before runtime deployment if process model demands committed baseline.
