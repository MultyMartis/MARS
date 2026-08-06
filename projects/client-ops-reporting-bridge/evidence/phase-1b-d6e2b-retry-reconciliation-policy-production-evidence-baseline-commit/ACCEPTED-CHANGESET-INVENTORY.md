# ACCEPTED-CHANGESET-INVENTORY — D6E2B

## Isolation verdict

`D6E2B_ACCEPTED_CHANGESET_ISOLATED`

## Classification of Client Ops porcelain (A–I)

| Class | Meaning | Action | Approx count |
|-------|---------|--------|--------------|
| A | Accepted D6E implementation (retry/concurrency/reconciliation libs + Python binding) | INCLUDE | 7 |
| B | Accepted D6E tests/harness | INCLUDE | 2 |
| C | Accepted D6E phase doc + evidence pack | INCLUDE | 1 + 32 |
| D | Accepted D6E2 read-only tooling (transport + runner) | INCLUDE | 2 |
| E | Accepted D6E2 production read-only phase + evidence | INCLUDE | 1 + 34 |
| F | D6E2B baseline phase + evidence (this pack) | INCLUDE | 1 + ~30 |
| G | Previously committed A/B/C material appearing as inverse-cache `D` / WT mirrors | EXCLUDE | many |
| H | Unrelated/newer Client Ops WIP (D5R-MONCLEAN/MOND/MONRESTORE; fixture/producer MM; etc.) | EXCLUDE | many |
| I | Unknown | none in allowlist | 0 |

## Include paths (A+B+C+D+E+F)

### A — D6E implementation
- `n8n/runners/lib/client-ops-retry-policy.mjs`
- `n8n/runners/lib/client-ops-retry-reason-codes.mjs`
- `n8n/runners/lib/client-ops-reconciliation-planner.mjs`
- `n8n/runners/lib/client-ops-retry-charter.mjs`
- `n8n/runners/lib/client-ops-concurrency-policy.mjs`
- `src/client_ops_reporting_bridge/retry_policy_binding.py`

### B — D6E tests/harness
- `n8n/harness/d6e-retry-concurrency-policy-harness.mjs`
- `tests/test_retry_policy_d6e.py`

### C — D6E docs/evidence
- `PHASE-1B-D6E-RETRY-AND-CONCURRENCY-POLICY-BINDING.md`
- `evidence/phase-1b-d6e-retry-and-concurrency-policy-binding/**` (all accepted artifacts)

### D — D6E2 tooling
- `n8n/runners/lib/client-ops-d6e2-readonly-transport.mjs`
- `n8n/runners/run-client-ops-d6e2-retry-reconciliation-policy-production-read-only-verification.mjs`

### E — D6E2 evidence
- `PHASE-1B-D6E2-RETRY-AND-RECONCILIATION-POLICY-PRODUCTION-READ-ONLY-VERIFICATION.md`
- `evidence/phase-1b-d6e2-retry-reconciliation-policy-production-read-only-verification/**`

### F — D6E2B
- `PHASE-1B-D6E2B-RETRY-AND-RECONCILIATION-POLICY-PRODUCTION-EVIDENCE-BASELINE-COMMIT.md`
- `evidence/phase-1b-d6e2b-retry-reconciliation-policy-production-evidence-baseline-commit/**`

## Explicit exclusions

- SITE-002 source under `projects/ocpilot/sites/site-002/` → **0**
- MetaBOT / iSEO / FP-0002 → **0**
- Workstream A/B/C inverse-cache paths → **0** (already committed)
- MONCLEAN / MOND / MONRESTORE → **0**
- Workstream D → **0** (not started)
