# D6A Evidence Pack — Durable Post-Telegram Delivery Ledger

**Phase:** 1B-D6A
**Live apply:** false
**Harness:** `D6A_OFFLINE_LEDGER_HARNESS_PASS` (11/11)

## Contents

| File | Purpose |
|------|---------|
| D6A-CHARTER.json | Charter bounds |
| LIVE-BASELINE-GET-ONLY.md | GET-only live reconfirm |
| CURRENT-DATA-TABLE-SCHEMA.md | 15-column inventory |
| CURRENT-DELIVERY-STATE-MACHINE.md | Pre-D6A lifecycle |
| TARGET-DELIVERY-STATE-MACHINE.md | Target transitions |
| SCHEMA-DECISION.md | Schema sufficiency |
| FINALIZER-CONTRACT.md | Narrow finalizer contract |
| FINALIZER-UPDATE-MODEL.md | Update model classification |
| TELEGRAM-SUCCESS-AUTHORITY.md | Success signals |
| TELEGRAM-FAILURE-SEMANTICS.md | Failure vs ambiguous |
| POST-TELEGRAM-LEDGER-WRITE-FAILURE.md | No-resend policy |
| DUPLICATE-SAFETY.md | Duplicate suppression |
| WORKFLOW-FINALIZATION-PLACEMENT.md | Topology choice B |
| OFFLINE-WORKFLOW-IMPLEMENTATION.md | Source vs production |
| OFFLINE-SCHEMA-MODEL.md | Offline schema model |
| FIXTURE-MATRIX.md | Cases 1–8 (+extras) |
| TEST-RESULTS.md | Harness + validator |
| REGRESSION-RESULTS.md | Historical suites |
| SECURITY-REVIEW.md | Data minimization |
| D6A-DECISION.json | Machine-readable decision |

## Helper scripts (GET-only / export)

- `_get-precheck.mjs` — live GET-only baseline
- `_export-offline-workflow.mjs` — sanitized 17-node fixture export
- `_get-postcheck.mjs` — live GET-only postcheck (created with postcheck wave)
