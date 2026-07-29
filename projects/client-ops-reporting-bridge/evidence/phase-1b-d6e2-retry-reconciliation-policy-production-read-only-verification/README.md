# README — Phase 1B-D6E2 evidence

Retry and Reconciliation Policy Production Read-Only Verification.

## Tokens (summary)

| Token | Status |
|-------|--------|
| `D6E2_CANONICAL_BASELINE_RECONFIRMED` | PASS |
| `D6E2_ACCEPTED_D6E_SOURCE_REVALIDATED` | PASS (54/54 + 10/10 + Python 10/10) |
| `D6E2_LIVE_BASELINE_RECONFIRMED` | PASS |
| `D6E2_RUNTIME_BASELINE_RECONFIRMED` | PASS (HEAD/scheduler/process; porcelain pre-existing foreign WIP) |
| `D6E2_READ_ONLY_SURFACE_DECLARED` | PASS |
| `D6E2_READ_ONLY_CHARTER_READY` | PASS |
| `D6E2_READ_ONLY_INVARIANT_ARMED` | PASS |
| `D6E2_SECURITY_GATE_PASS` | PASS |
| `D6E2_RECONCILIATION_IS_READ_ONLY` | PASS |
| Historical PENDING / SENT policy | PASS — both prohibit blind retry |
| Zero side effects | PASS |
| A/B/C/E regressions | PASS |
| `MAIN_INDEX_UNTOUCHED_BY_D6E2` | PASS |

## Runner

```text
node n8n/runners/run-client-ops-d6e2-retry-reconciliation-policy-production-read-only-verification.mjs
```

Transport: `n8n/runners/lib/client-ops-d6e2-readonly-transport.mjs` (GET-only allowlist).

## Readiness

`READY_FOR_D6E2_EVIDENCE_BASELINE_COMMIT`

Next (not started): Phase 1B-D6E2B — Retry and Reconciliation Policy Production Evidence Baseline Commit

Do not create REPORT as a repository file.
