# LEAD LIFECYCLE v1

> **Production supersession (2026-08-17):** Current lifecycle and Telegram action semantics are documented in [LEAD-LIFECYCLE-CURRENT.md](LEAD-LIFECYCLE-CURRENT.md).
> Canonical stable truth: [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md).
> This Phase 2 file remains historical design context where it conflicts with production baseline.

**Product:** i-SEO Sales Manager Bot  
**Status:** documented — simple manager lifecycle (**not** a CRM)

---

## 1. Purpose

Give Оля (PER-0010) and operators a **minimal** status vocabulary so leads are not stuck forever at `new`, without building CRM pipeline automation.

---

## 2. Status enum

| Status | Meaning (manager Russian label) |
|--------|----------------------------------|
| `new` | Новый — только что обработан ботом |
| `reviewing` | В разборе — менеджер смотрит карточку |
| `contacted` | Связались — первый контакт сделан |
| `waiting_client` | Ждём клиента |
| `qualified` | Целевой / квалифицирован |
| `not_target` | Не целевой |
| `closed` | Закрыт |
| `error` | Ошибка обработки (техническая) |

Telegram must show **Russian labels**, never raw enums.

---

## 3. Allowed transitions (v1)

```
new → reviewing | contacted | not_target | error | closed
reviewing → contacted | waiting_client | qualified | not_target | closed
contacted → waiting_client | qualified | not_target | closed
waiting_client → contacted | qualified | not_target | closed
qualified → closed | waiting_client
not_target → closed | reviewing
error → reviewing | closed
closed → reviewing   (reopen — rare; audit required)
```

Forbidden: skipping to `closed` without `close_reason` when moving from `qualified` / `contacted` (soft rule — warn in Admin if later commands exist).

---

## 4. Who changes status

| Actor | v1 mechanism | Notes |
|-------|--------------|-------|
| **Operational workflow** | Sets `manager_status=new` on first CLEAN write; sets `error` on hard process failure | Does not advance sales states |
| **Manager (Оля)** | **Sheets edit** of `manager_status` (+ notes/dates) for v1 | Primary path for Olya v1 |
| **Admin Telegram** | Status change commands | **NOT REQUIRED FOR V1** |
| **Telegram buttons / inline keyboards** | Callback updates | **NOT REQUIRED FOR V1** |

---

## 5. Required for Olya v1

1. Bot always creates CLEAN with `manager_status=new`.
2. Telegram card shows clear next step (`manager_recommendation`) so she knows what to do even if status stays `new`.
3. She may update status/notes in CLEAN sheet manually.
4. `first_reply_text` copy-paste to client channel of her choice — bot never sends to client.
5. Repeat/reprocessed distinction visible so she does not treat reprocess as new demand.

---

## 6. NOT REQUIRED FOR V1

- Assignment queues / `assigned_to` automation
- Follow-up reminders / `next_followup_at` jobs
- Telegram status buttons
- Admin `/set_status` commands
- SLA timers
- Pipeline forecasts
- Multi-manager routing
- Client portal sync

These fields may exist on CLEAN for future use but **must not block** Phase 3 sandbox.

---

## 7. Interaction with duplicates

| `duplicate_status` | Lifecycle effect |
|--------------------|------------------|
| `new` | `manager_status=new` |
| `reprocessed` | Keep existing lifecycle status if CLEAN updated; do not reset to `new` unless empty |
| `repeat` / `possible` | Still `new` card for attention, but recommendation references prior lead |

---

## 8. Close reasons (suggested vocabulary)

`won` · `lost` · `spam` · `duplicate_closed` · `not_target` · `no_response` · `other`

Stored in `close_reason` when `manager_status=closed`.

---

*Related: LEAD-DATA-MODEL-v1 · TELEGRAM-UX-CONTRACT-v1 · ADMIN-COMMAND-CONTRACT-v1.*
