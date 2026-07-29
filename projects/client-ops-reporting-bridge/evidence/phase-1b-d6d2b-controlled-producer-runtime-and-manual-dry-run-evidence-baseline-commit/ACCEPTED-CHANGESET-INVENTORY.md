# ACCEPTED-CHANGESET-INVENTORY — D6D2B

Uncommitted paths under `projects/client-ops-reporting-bridge/` classified:

| Class | Meaning | Count | Commit? |
|-------|---------|------:|:-------:|
| A | Accepted D6D2 phase document | 1 | YES |
| B | Accepted D6D2 sanitized evidence | 30 | YES |
| C | Accepted D6D2 deployment manifest and policy evidence | 12 | YES |
| D | D6D2B baseline docs/evidence | (this pack + phase doc) | YES |
| E | Previously committed A/B/C/E/D inverse-cache differences | 808 | NO |
| F | Unrelated/newer Client Ops WIP (incl. D5R deletions etc.) | 220 | NO |
| G | Runtime-state / runtime checkout material | 0 | NO |
| H | SITE-002 runtime/source changes unrelated to D6D2B | 0 | NO |
| I | Foreign systems | 0 | NO |
| J | Unknown | 0 | NO |

## Class A (1)

- `PHASE-1B-D6D2-UNATTENDED-PRODUCER-CONTROLLED-RUNTIME-DEPLOYMENT-AND-DRY-RUN-VERIFICATION.md`

## Class C (12) — deployment/policy subset of D6D2 evidence

- `PRODUCER-RUNTIME-DEPLOYMENT-MANIFEST.json`
- `PRODUCER-RUNTIME-CLEANLINESS.md`
- `KILL-SWITCH-DRY-RUN.json`
- `BOOTSTRAP-BOUNDARY.json`
- `MARKER-DEPLOYMENT-DECISION.md`
- `HISTORICAL-FALLBACK-STABILIZATION.md`
- `RUNTIME-STATE-BOUNDARIES.md`
- `SCHEDULER-BOUNDARY.md`
- `SECRET-BOUNDARY.md`
- `DRY-RUN-DELIVERY-PROHIBITION.md`
- `DRY-RUN-GATE-ORDER.md`
- `DRY-RUN-SAFETY-SELF-CHECK.md`

## Class B (30)

Remaining files under `evidence/phase-1b-d6d2-unattended-producer-controlled-runtime-deployment-and-dry-run-verification/` not listed in C.

## Class D

- `PHASE-1B-D6D2B-CONTROLLED-PRODUCER-RUNTIME-AND-MANUAL-DRY-RUN-EVIDENCE-BASELINE-COMMIT.md`
- `evidence/phase-1b-d6d2b-controlled-producer-runtime-and-manual-dry-run-evidence-baseline-commit/*`

Commit candidates: **A+B+C+D only**.
