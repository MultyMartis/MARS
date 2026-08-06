# Phase 1B-D1 — Durable Dedupe Evidence Pack

**Status:** COMPLETE (inactive sandbox; sequential proof)
**Readiness:** READY_FOR_DURABLE_DEDUPE_BASELINE_COMMIT
**Concurrency:** DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN

## Baseline note

First apply attempt failed because n8n Code disallows `require('crypto')` (execution 3410). Workflow and table were rolled back. Fingerprint switched to canonical JSON. Second apply succeeded against post-rollback baseline executions=26 / versionId `fc6c6801-...`. Final executions=29 (26+3).

## Artifacts

See JSON/MD files in this directory.
