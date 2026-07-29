# ACCEPTED-CHANGESET-INVENTORY — D6DB

`D6DB_ACCEPTED_CHANGESET_ISOLATED`

| Class | Meaning | Action | Count |
|-------|---------|--------|-------|
| A | Accepted D6D Client Ops implementation | INCLUDE | 10 |
| B | Accepted D6D tests/harness | INCLUDE | 2 |
| C | Accepted D6D docs/evidence | INCLUDE | 1 + 43 |
| D | Accepted minimal SITE-002 completion-marker source | INCLUDE | 2 |
| E | D6DB baseline docs/evidence | INCLUDE | 1 + pack |
| F | Previously committed A/B/C/E inverse-cache differences | EXCLUDE | many |
| G | Unrelated/newer Client Ops WIP | EXCLUDE | many |
| H | Unrelated SITE-002 WIP (README, lari tools, baseline-mix in WT monitor) | EXCLUDE | many |
| I | Runtime-only foreign WIP | EXCLUDE | 1+ |
| J | Unknown | none in allowlist | 0 |

## A — implementation
- `n8n/runners/lib/client-ops-d6d-constants.mjs`
- `n8n/runners/lib/client-ops-d6d-kill-switch.mjs`
- `n8n/runners/lib/client-ops-d6d-producer-lock.mjs`
- `n8n/runners/lib/client-ops-d6d-cursor.mjs`
- `n8n/runners/lib/client-ops-d6d-artifact.mjs`
- `n8n/runners/lib/client-ops-d6d-receipt.mjs`
- `n8n/runners/lib/client-ops-d6d-runtime-gates.mjs`
- `n8n/runners/lib/client-ops-d6d-unattended-producer.mjs`
- `n8n/runners/lib/client-ops-acquisition-lifecycle-shim.mjs`
- `src/client_ops_reporting_bridge/unattended_d6d.py`

## B — tests/harness
- `n8n/harness/d6d-unattended-integration-harness.mjs`
- `tests/test_unattended_d6d.py`

## C — D6D docs/evidence
- `PHASE-1B-D6D-UNATTENDED-MONITOR-TO-CLIENT-OPS-INTEGRATION-CONTRACT.md`
- `evidence/phase-1b-d6d-unattended-monitor-to-client-ops-integration-contract/**`

## D — SITE-002 marker (minimal)
- `projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py` (marker-only bytes; foreign WT baseline hunks excluded)
- `projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner.ps1` (additive marker after Finish-Summary JSON write)

## E — D6DB
- `PHASE-1B-D6DB-UNATTENDED-MONITOR-TO-CLIENT-OPS-INTEGRATION-CONTRACT-BASELINE-COMMIT.md`
- `evidence/phase-1b-d6db-unattended-monitor-to-client-ops-integration-contract-baseline-commit/**`
