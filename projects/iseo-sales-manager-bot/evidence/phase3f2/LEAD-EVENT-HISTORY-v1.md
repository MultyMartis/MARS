# LEAD EVENT HISTORY v1 — Phase 3F.2

## Model

`LEAD_EVENTS` is append-only, per [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md) §4: `event_id`, `ts`, `lead_id` (nullable), `event_type`, `actor`, `detail`. Phase 3F.2 does not change this model — it adds one new `event_type` value for the reconciliation flow.

## Expected event trail for Клиент A

| Step | `event_type` | `actor` | Notes |
|---|---|---|---|
| Intake | `raw_logged` / `processed` (existing vocabulary) | `operational` | Original Ops execution (exec `23273`) |
| Telegram delivery | `telegram_sent` | `operational` | 2 recipients stamped |
| Failed moderator callback | *(no event — write never reached this stage)* | — | `append_lead_event=false` on the failed attempt itself, per [CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md](CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md) — this is expected and correct: a failed lookup must not fabricate an event record |
| Reconciliation | `lifecycle_changed` (or `reconciled`) | `admin:<sanitized>` or `moderator:<sanitized>` — no raw Telegram numeric ID in this document | `detail` should reference `source=telegram_callback_reconciliation`; see [EVGENIY-LIFECYCLE-RECONCILIATION-v1.md](EVGENIY-LIFECYCLE-RECONCILIATION-v1.md) |

## PII discipline for this tab

- `actor` values in `LEAD_EVENTS` are stored in the live sheet as `admin:<telegram_id>` per the documented format (§4) — that raw numeric id is **never** reproduced in this evidence file or any Phase 3F.2 markdown; actors are referred to here only by role/sanctioned label (Мопс, moderator).
- `detail` must stay short and free of contact data, per the existing `ERRORS`/`LEAD_EVENTS` "no secrets" convention already documented for the `ERRORS` tab.

## Status

| Item | Status |
|---|---|
| Event model (unchanged) | **CONFIRMED** — no schema change needed |
| New `lifecycle_changed`/`reconciled` event type adopted | **IMPLEMENTED** (contract-level) |
| Live `LEAD_EVENTS` row for Клиент A's reconciliation confirmed present | **SAFE UNKNOWN** — not independently re-read in this evidence pass |

*Related: [CLEAN-BACKEND-SCHEMA-v1.md](CLEAN-BACKEND-SCHEMA-v1.md), [EVGENIY-LIFECYCLE-RECONCILIATION-v1.md](EVGENIY-LIFECYCLE-RECONCILIATION-v1.md).*
