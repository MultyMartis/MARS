# D5R2A Delivery Facts

## Charter

NEW one-shot charter → **CONSUMED**

Limits respected: activation changes max=2; POST max=1; retries=0; replays=0; concurrency=1.

## Activation lifecycle

`active=false` → `active=true` → `active=false`

Activation changes: **2**

Workflow: `MARS Client Ops Bridge — bzpm.ru` / `tkM4H0G0gM3q9Foi`
Nodes: 17
Version ID unchanged: `3d2fd6fc-bc17-4e0f-b9e5-086c959afd29`
Workflow content/config mutations: **0**

## One request result

| Field | Value |
|-------|-------|
| Producer requests | 1 |
| Retries / replays | 0 / 0 |
| Duplicate proof | NOT PERFORMED |
| Producer | `site002-controlled-live` |
| Producer stdout JSON parse | **FAILED** |
| Authoritative intake | HTTP **202** / `intake_state=FIRST_SEEN` via GET-only recovery |

## n8n execution

Executions: 31 → **32**
Selected: **3416** / status=`success` / finished=`true` / mode=`webhook` / path=`FIRST_SEEN`
Telegram node reached: `Telegram Notify Accepted`

## Data Table

Table: `MARS Client Ops Dedupe — bzpm.ru` / `H6VYhwz7RXZCBMmu`
rows: 2 → **3**
selected event rows: 0 → **1**
event_id: `c84e29bf-79b1-5aea-98c4-9dc8d651fc96`
intake_state: `FIRST_SEEN`
event_status: `ATTENTION`
delivery_state: may remain `PENDING` (durable SENT ledger DEFERRED)

## Telegram

Attempted: 1 / Delivered: 1 / sanitized `message_id`: **7**
Direct Telegram API calls: 0

## Final containment

`active=false` after mandatory deactivation.
