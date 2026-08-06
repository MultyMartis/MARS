# PHASE-1B-D6B2B — Freshness Semantics Production Evidence Baseline Commit

**Status:** COMPLETE (on successful commit)
**Date (UTC):** 2026-07-26
**Mode:** OFFLINE EVIDENCE BASELINE / GIT COMMIT ONLY
**No-live rule:** enforced (0 n8n mutations, 0 activation, 0 webhook, 0 Telegram, 0 Data Table mutations, 0 producer byte deployments)

## Purpose

Canonically commit accepted Workstream B baseline proving:

1. factual `source_status` is independent from evaluation-time freshness;
2. accepted status mapping (NO_ACTION_REQUIRED→OK, ONBOARDING/HYGIENE→ATTENTION, FAILURE_REVIEW_REQUIRED→FAILED, true authority defect→BLOCKED);
3. delivery eligibility: FRESH_AND_ELIGIBLE / STALE_REVIEW_REQUIRED / NOT_SAFE_TO_SEND;
4. stale valid sources preserve factual status + STALE_REVIEW_REQUIRED;
5. true authority defect remains BLOCKED + NOT_SAFE_TO_SEND;
6. STALE_AFTER_SECONDS=93600 with operator `age > 93600` (93600 fresh; 93601 stale);
7. event identity is freshness-clock independent;
8. new source run creates new deterministic event identity;
9. stale/blocked fail closed before Client Ops intake;
10. Workstream A durable ledger unchanged; retries=0; concurrency=1; Client Ops contained.

## Accepted prior phases

| Phase | State |
|-------|-------|
| 1B-D6A / D6A2 / D6A2B | COMPLETE — Workstream A durable ledger COMMITTED/DEPLOYED @ `12e4c6ad…` |
| 1B-D6B | COMPLETE — offline freshness/eligibility separation |
| 1B-D6B2 | COMPLETE — effective producer-path verification (PRODUCER_ONLY; byte mutations=0) |
| Readiness entering D6B2B | `READY_FOR_D6B2_EVIDENCE_BASELINE_COMMIT` |

## D6B2 production-surface nuance (load-bearing)

`D6B2_PRODUCTION_SURFACE_PRODUCER_ONLY`

D6B2 did **not** perform a separate source→runtime producer byte deployment. Accepted D6B working-tree producer implementation was already the effective producer code surface. D6B2 performed producer path hash lock + formal production-surface declaration + deployed/effective-path semantic verification. Producer bytes mutated during D6B2: **0**. n8n content mutations: **0**. Activation changes: **0**.

## Commit subject (exact)

`feat(client-ops): separate freshness delivery eligibility`

## Scope

- Allowed: `projects/client-ops-reporting-bridge/` accepted D6B / D6B2 / D6B2B paths only
- Forbidden: SITE-002 source/runtime mutations; n8n mutations; MAIN index mutations; push; live verification replay; Workstream C/E/D

## Evidence pack

`projects/client-ops-reporting-bridge/evidence/phase-1b-d6b2b-freshness-semantics-production-evidence-baseline-commit/`

## Production readiness preserved

| Flag | Value |
|------|-------|
| CLIENT_OPS_UNATTENDED_PRODUCTION_READY | NO |
| CLIENT_OPS_AUTOMATIC_SITE002_CONNECTION_AUTHORIZED | NO |
| D6C_NOT_STARTED | YES |
| D6E_NOT_STARTED | YES |
| D6D_NOT_STARTED | YES |
| HISTORICAL_D5R2A_ROW_RECONCILIATION_AUTHORIZED | NO |

## Next (do not begin automatically)

**Phase 1B-D6C — Controlled Activation Lifecycle Contract** (offline / architecture+implementation first)
