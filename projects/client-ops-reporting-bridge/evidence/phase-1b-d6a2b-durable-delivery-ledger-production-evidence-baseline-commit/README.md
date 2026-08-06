# Evidence — Phase 1B-D6A2B Durable Delivery Ledger Production Evidence Baseline Commit

**Mode:** offline evidence baseline / Git commit only
**Live mutations by this phase:** 0

## Key tokens

| Token | Result |
|-------|--------|
| `D6A2B_LIVE_BASELINE_RECONFIRMED` | PASS (GET-only) |
| `D6A2B_ACCEPTED_CHANGESET_ISOLATED` | PASS |
| `D6A2B_SECURITY_CLEAN` | PASS |
| `CLEAN_GIT_SYNC_WORKTREE_READY` | PASS |
| `CLEAN_WORKTREE_ACCEPTED_FILE_PARITY=PASS` | PASS (recorded at materialization) |
| `MAIN_INDEX_UNTOUCHED_BY_D6A2B` | PASS |
| `D6A2B_POSTCOMMIT_LIVE_BASELINE_MATCH` | recorded post-commit |
| `D6A2B_POSTCOMMIT_REGRESSION_PASS` | recorded post-commit |
| Readiness | `READY_FOR_D6B_FRESHNESS_SEMANTICS_CHARTER` |

## Pack contents

| File | Role |
|------|------|
| `D6A2B-CHARTER.json` | Phase charter machine evidence |
| `D6A2B-DECISION.json` | Final decision tokens |
| `LIVE-RECONFIRMATION.md` | GET-only Client Ops reconfirmation |
| `RUNTIME-RECONFIRMATION.md` | SITE-002 runtime / scheduler |
| `ACCEPTED-CHANGESET-INVENTORY.md` | Isolation allowlist |
| `D6-ARCHITECTURE-BASELINE.md` | A→B→C→E→D |
| `D6A-OFFLINE-LEDGER-BASELINE.md` | Offline ledger state machine |
| `D6A2-PRODUCTION-LEDGER-BASELINE.md` | Production apply facts |
| `SENT-PRODUCTION-PROOF.md` | Synthetic SENT proof |
| `DUPLICATE-PRODUCTION-PROOF.md` | Duplicate suppression |
| `FAILED-PATH-LIMITATION.md` | Production FAILED deferred |
| `HISTORICAL-REAL-EVENT-STATE.md` | Real row remains PENDING |
| `WORKFLOW-CONTAINMENT.md` | active=false / 20 nodes / 34 exec |
| `SECURITY-REVIEW.md` | Secret scan |
| `TEST-RESULTS.md` | Offline suites |
| `GIT-SAFETY.md` | Worktree / MAIN index rules |

## Secrets

No raw n8n API keys, Telegram bot tokens, webhook secrets, Authorization headers, `.env` values, raw Telegram API responses, or raw execution payloads are stored in this pack. Operational sandbox `chat_id` may appear only as previously accepted Client Ops operational identity (same baseline as D0/D1/D3/D6A2).
