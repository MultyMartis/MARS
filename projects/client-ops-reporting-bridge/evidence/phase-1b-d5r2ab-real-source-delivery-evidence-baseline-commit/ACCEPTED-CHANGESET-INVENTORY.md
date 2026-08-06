# Accepted Change Inventory

## Isolation verdict

`D5R2AB_ACCEPTED_CHANGESET_ISOLATED`

## Classification of Client Ops porcelain

| Class | Content | Action |
|-------|---------|--------|
| A | D5R2 phase + evidence | INCLUDE |
| B | D5R2A phase + evidence | INCLUDE |
| C | older already-committed Client Ops | N/A (not dirty for this wave) |
| D | foreign Client Ops WIP (MONSYNC deletions, MONCLEAN/MOND/MONRESTORE) | EXCLUDE |
| E | unknown | none observed in allowlist |

## Exact allowlist (paths relative to repo root)

### Phase docs (3)

1. `projects/client-ops-reporting-bridge/PHASE-1B-D5R2-CONTROLLED-D5-MANUAL-REAL-SOURCE-RETRY-WITH-REVALIDATED-FRESH-CANDIDATE.md`
2. `projects/client-ops-reporting-bridge/PHASE-1B-D5R2A-CONTROLLED-REAL-SOURCE-DELIVERY-WITH-TEMPORARY-N8N-ACTIVATION-AND-IMMEDIATE-RE-CONTAINMENT.md`
3. `projects/client-ops-reporting-bridge/PHASE-1B-D5R2AB-TEMPORARY-ACTIVATION-REAL-SOURCE-DELIVERY-EVIDENCE-BASELINE-COMMIT.md`

### D5R2 evidence (20)

All files under `projects/client-ops-reporting-bridge/evidence/phase-1b-d5r2-controlled-real-source-retry/`

### D5R2A evidence (35)

All files under `projects/client-ops-reporting-bridge/evidence/phase-1b-d5r2a-temporary-activation-one-shot/`

### D5R2AB evidence (this pack)

All files under `projects/client-ops-reporting-bridge/evidence/phase-1b-d5r2ab-real-source-delivery-evidence-baseline-commit/`

## Explicit exclusions

- SITE-002 source under `projects/ocpilot/sites/site-002/` → **0**
- MetaBOT → **0**
- runtime checkout contents → **0**
- MONSYNC / MONCLEAN / MOND / MONRESTORE Client Ops WIP → excluded
- unrelated iSEO / WP Forge / Website Factory / FP-0002 → excluded
