# REGRESSION

## Suite

`projects/client-ops-reporting-bridge/tests/test_d6g_event_driven_import.py`

Result: **7 tests OK** (local worktree / runtime sources).

## Focused gate mapping (R1–R24)

| ID | Result | Notes |
|----|--------|-------|
| R1 | PASS | Scheduled gateway + admin enqueue call same wrapper |
| R2 | PASS (contract) | Shared lock returns «Импорт уже выполняется» |
| R3 | PASS (contract) | Same lock for SCHEDULED |
| R4 | PASS (contract) | Stale lock requires inactive process proof |
| R5–R7 | PASS (live) | Admin login + permission + POST + user_token |
| R8 | PASS (live) | Async launch ~298 ms |
| R9 | PASS (live) | Status poll to terminal |
| R10–R12 | PASS (unit + live R11) | Terminal statuses; live = ATTENTION_OFFERS_INPUT_MISSING |
| R13 | PASS (live) | Dispatcher targeted exact run_id |
| R14 | PASS (live) | Redispatch → ALREADY_DISPATCHED |
| R15 | PASS (design) | Event_id includes run_id |
| R16 | PASS | Producer task no longer backlog-sends normal reports |
| R17–R19 | PASS (watchdog script) | Distinct daily event; skip if delivered/running |
| R20 | PASS (live Telegram) | Russian D6F1B UX |
| R21 | PASS | Workflow active, 20 nodes |
| R22 | PASS | Final task model applied |
| R23 | PASS | Automatic retries remain disabled |
| R24 | PASS | No secrets in admin HTML; evidence sanitized |

## Gate

`D6G_REGRESSION_PASS` — PASS (with live coverage for critical path; unit suite for contract helpers)
