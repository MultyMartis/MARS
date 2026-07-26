# WORKSTREAM E — Retry / Concurrency Policy

`D6_WORKSTREAM_E_ANALYZED`

## Current proven safe producer mode

- `concurrency=1`
- `max_retries=0`
- `automatic_retry=false`
- Enforced in D5 gates (`producer_d5_gates.py`)

## Current maturity

`PARTIALLY_PROVEN` (safe zero-retry mode proven; production-grade retry **not** accepted)

## Failure-class policy (design)

| # | Failure | Auto retry today | Safe next action |
|---|---------|------------------|------------------|
| 1 | Connection failure before request sent | unsafe as auto | Future: may retry after confirm no execution; today operator |
| 2 | Ambiguous timeout after request may have reached server | **unsafe** | GET-only reconcile DT + executions; no automatic POST |
| 3 | HTTP 4xx (auth/validation) | unsafe | Terminal failure / fix config; no retry of same bad request |
| 4 | HTTP 5xx before dedupe persistence | conditional future | GET-only first; retry only if no row + no execution claim |
| 5 | HTTP 5xx after dedupe persistence | **unsafe** for Telegram path | Reconcile delivery_state; never blind POST |
| 6 | Workflow accepted but Telegram failed | unsafe without ledger | Persist FAILED; operator / future retryable only if SENT ledger exists |
| 7 | Telegram succeeded but SENT persistence failed | **unsafe** to re-send | GET-only Telegram/execution reconcile; repair ledger; **no** second customer message |
| 8 | Activation failed | n/a POST | Do not POST; abort; operator |
| 9 | Deactivation failed | n/a | Emergency deactivate + alert; do not start new activate window |

## Why retries are blocked today

Without durable SENT vs PENDING reconciliation, any automatic retry of the same `event_id` can produce a **duplicate customer Telegram** if the first attempt already delivered.

## Concurrency

`D6_MAX_SAFE_CONCURRENCY_TODAY=1`

Data Table claim is sequential-safe only under single producer (accepted: `DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN`). No evidence supports >1.

## Prerequisite

`D6_RETRY_POLICY_PREREQUISITE=durable_SENT_ledger_plus_GET_only_reconciliation_plus_freshness_separation`

Order: implement **A**, repair **B**, then define retry matrix as code/policy; only then consider non-zero retries under charter.

## Upstream / downstream

- Upstream: **A** (hard), **B** (hard for stale retries)
- Downstream: **D**
