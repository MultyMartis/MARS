# PHASE 1B-D1 — Durable Dedupe Design and Inactive Sandbox Implementation

**Status:** COMPLETE (inactive sandbox retained)
**Date:** 2026-07-24
**Branch:** `mars/canonical-post-recovery`
**Readiness:** `READY_FOR_DURABLE_DEDUPE_BASELINE_COMMIT`
**Concurrency class:** `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN`

## Summary

Installed n8n Data Table API and workflow node (`n8n-nodes-base.dataTable` @ 1.1) were proven adequate for **sequential** durable dedupe. Dedicated table `MARS Client Ops Dedupe — bzpm.ru` was created and retained. Workflow gained a 7-node dedupe gate **before** Respond Accepted / Telegram.

Controlled tests:

| Case | Exec | HTTP | Telegram |
|------|------|------|----------|
| FIRST_SEEN | 3411 | 202 ACCEPTED / FIRST_SEEN | 1 |
| EXACT_REPLAY | 3412 | 200 DUPLICATE_SUPPRESSED | 0 |
| EVENT_ID_CONFLICT | 3413 | 409 EVENT_ID_CONFLICT | 0 |

## Fingerprint

`canonical_json_v1` — SHA-256 via `require('crypto')` is **disallowed** on this n8n Code host (failed execution 3410). Canonical JSON equality is the installed-safe fingerprint.

## Baseline adjustment

Original charter expected executions 25→28. Attempt-1 error 3410 forced rollback; successful retest used post-rollback baseline 26→29. Functional caps (3 POSTs / 1 Telegram) held on the successful attempt.

## Deferred

- Post-Telegram `delivery_state=SENT` update
- duplicate_count / conflict_count durable increments
- Concurrent atomicity proof

## Next

Phase 1B-D1B — Durable Dedupe Evidence Baseline Commit (this wave). After commit: Phase 1B-D2 Sequential Runtime Producer Design (offline; do not begin without charter).

Evidence: `n8n/evidence/phase-1b-d1-durable-dedupe/`
