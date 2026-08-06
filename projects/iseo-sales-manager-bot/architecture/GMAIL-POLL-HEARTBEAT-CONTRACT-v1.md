# GMAIL POLL HEARTBEAT CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3H.4  
**Owner workflow:** Operational.dev (`xSnXPy8cEHoZw6xG`)  
**Version stamp:** `iseo-gmail-poll-heartbeat-v1.0`

---

## 1. Purpose

Scheduled Gmail polling must advance operator-visible poll freshness even when the inbox is **empty**. Pre-3H.4, empty runs returned no CONFIG write and `/status` showed a frozen poll timestamp while polling continued.

---

## 2. Write obligation

On **every successful** completion of the scheduled poll path (including Intake Gate **empty** route):

1. Write compact JSON to CONFIG key `gmail_poll_heartbeat`
2. Mirror ISO timestamp to `last_poll_success_at`
3. Set `last_poll_heartbeat_version=iseo-gmail-poll-heartbeat-v1.0`

---

## 3. Heartbeat JSON (minimum fields)

| Field | Type | Meaning |
|---|---|---|
| `version` | string | `iseo-gmail-poll-heartbeat-v1.0` |
| `at` | ISO-8601 | Wall-clock completion time |
| `empty_run` | boolean | true when zero messages entered processing |
| `messages_fetched` | number | Count from fetch step (0 allowed) |

---

## 4. Non-goals

- Does **not** replace `/health` on-demand Gmail probe
- Does **not** imply a lead was processed when `empty_run=true`
- Does **not** write production lead stamps on empty runs

---

## 5. Production lead stamps (separate)

On **non-test** successful lead processing only:

- `last_production_processed_at`
- `last_production_processed_lead_id`

These keys feed `/status` production line — see `OPERATIONAL-STATUS-TRUTH-CONTRACT-v1.md`.

---

## 6. Implementation reference

`implementation/SCHEDULED-POLL-OBSERVABILITY-v1.md` · Evidence: `evidence/phase3h4/GMAIL-POLL-HEARTBEAT-v1.md`
