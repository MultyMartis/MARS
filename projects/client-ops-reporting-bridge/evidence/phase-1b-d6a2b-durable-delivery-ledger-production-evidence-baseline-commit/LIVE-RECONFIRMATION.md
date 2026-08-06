# LIVE-RECONFIRMATION — D6A2B (GET-only)

**Method:** GET-only n8n workflow + Data Table reconfirmation
**Mutations:** 0
**Verdict:** `D6A2B_LIVE_BASELINE_RECONFIRMED`

## Workflow — MARS Client Ops Bridge — bzpm.ru

| Field | Expected | Observed |
|-------|----------|----------|
| id | `tkM4H0G0gM3q9Foi` | match |
| active | `false` | `false` |
| nodes | `20` | `20` |
| executions | `34` | `34` |
| running | `0` | `0` |
| versionId | `dc8746bf-df9c-425d-9b3f-4ace452ac5ef` | match |

Ledger nodes present: `Classify Telegram Delivery Outcome`, `IF Delivery Finalize`, `Delivery Ledger Finalize Update`.

## Data Table — `H6VYhwz7RXZCBMmu`

| Field | Expected | Observed |
|-------|----------|----------|
| columns | `15` | `15` |
| rows | `4` | `4` |

## Historical real event

| Field | Value |
|-------|-------|
| event_id | `c84e29bf-79b1-5aea-98c4-9dc8d651fc96` |
| intake_state | `FIRST_SEEN` |
| event_status | `ATTENTION` |
| delivery_state | `PENDING` |

## Synthetic D6A2 event

| Field | Value |
|-------|-------|
| event_id | `d6a2a001-27d6-4a2e-bd6a-000000000001` |
| intake_state | `FIRST_SEEN` |
| event_status | `OK` |
| delivery_state | `SENT` |

## Pre/post D6A2 contrast (accepted facts)

| | Pre-D6A2 | Post-D6A2 / D6A2B |
|--|----------|-------------------|
| nodes | 17 | 20 |
| executions | 32 | 34 |
| active | false | false |
| Data Table rows | 3 | 4 |
