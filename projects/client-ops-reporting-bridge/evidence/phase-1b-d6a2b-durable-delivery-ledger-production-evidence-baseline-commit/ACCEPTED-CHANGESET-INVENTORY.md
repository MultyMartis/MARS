# Accepted Change Inventory — D6A2B

## Isolation verdict

`D6A2B_ACCEPTED_CHANGESET_ISOLATED`

## Classification of Client Ops porcelain

| Class | Content | Action |
|-------|---------|--------|
| A | D6 architecture phase + evidence | INCLUDE |
| B | D6A offline implementation + evidence | INCLUDE |
| C | D6A2 production apply + evidence + activation phrases | INCLUDE |
| D | older already-committed Client Ops | N/A (not dirty for this wave) |
| E | foreign Client Ops WIP (MONSYNC deletions; MONCLEAN / MOND / MONRESTORE) | EXCLUDE |
| F | unknown | none observed in allowlist |

## Exact allowlist (paths relative to repo root)

### Phase docs (4)

1. `projects/client-ops-reporting-bridge/PHASE-1B-D6-CLIENT-OPS-POST-FIRST-DELIVERY-ARCHITECTURE-DECISION-CHARTER.md`
2. `projects/client-ops-reporting-bridge/PHASE-1B-D6A-DURABLE-POST-TELEGRAM-DELIVERY-LEDGER-DESIGN-AND-OFFLINE-IMPLEMENTATION.md`
3. `projects/client-ops-reporting-bridge/PHASE-1B-D6A2-CONTROLLED-DURABLE-DELIVERY-LEDGER-PRODUCTION-APPLY-AND-SYNTHETIC-VERIFICATION.md`
4. `projects/client-ops-reporting-bridge/PHASE-1B-D6A2B-DURABLE-DELIVERY-LEDGER-PRODUCTION-EVIDENCE-BASELINE-COMMIT.md`

### D6 evidence (15)

All files under `projects/client-ops-reporting-bridge/evidence/phase-1b-d6-post-first-delivery-architecture-decision/`

### D6A evidence (25)

All files under `projects/client-ops-reporting-bridge/evidence/phase-1b-d6a-durable-post-telegram-delivery-ledger/`

### D6A2 evidence (34)

All files under `projects/client-ops-reporting-bridge/evidence/phase-1b-d6a2-controlled-durable-delivery-ledger-production-apply/`

### D6A2B evidence (this pack)

All files under `projects/client-ops-reporting-bridge/evidence/phase-1b-d6a2b-durable-delivery-ledger-production-evidence-baseline-commit/`

### Implementation / tooling (7 path groups)

1. `projects/client-ops-reporting-bridge/n8n/runners/lib/client-ops-delivery-ledger.mjs`
2. `projects/client-ops-reporting-bridge/n8n/runners/lib/client-ops-delivery-ledger-compose.mjs`
3. `projects/client-ops-reporting-bridge/n8n/harness/delivery-ledger-harness.mjs`
4. `projects/client-ops-reporting-bridge/n8n/harness/delivery-ledger-cases/` (12 files)
5. `projects/client-ops-reporting-bridge/n8n/runners/validate-client-ops-d6a-delivery-ledger.mjs`
6. `projects/client-ops-reporting-bridge/n8n/runners/run-client-ops-d6a2-delivery-ledger-production-apply.mjs`
7. `projects/client-ops-reporting-bridge/n8n/runners/lib/client-ops-n8n-activation-client.mjs` (D6A2 confirmation phrases only)

## Explicit exclusions

- SITE-002 source under `projects/ocpilot/sites/site-002/` → **0**
- MetaBOT → **0**
- runtime checkout contents → **0**
- MONSYNC / MONCLEAN / MOND / MONRESTORE Client Ops WIP → excluded
- unrelated iSEO / WP Forge / Website Factory / FP-0002 → excluded
- D6B+ workstreams → not started / not included
