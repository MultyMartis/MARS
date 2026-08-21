# LIVE CALLBACK TRACE — card status sync regression

**Date:** 2026-08-21  
**Contour:** Admin.dev `wLrLp4WQHm1VJmxz`  
**Incident execution:** `36629`  
**Actor alias:** ADMIN_A  
**PII:** none (hashed refs only)

## Operator observation

Test lead card showed Pending (`🕓 Ожидает обработки`) with Spam/Processed/Raw buttons. Operator pressed `🚫 Спам`. Bot replied `Лид отмечен как спам.` Card UI did not update.

## Reconstructed callback (exec 36629)

| Field | Value |
|-------|-------|
| startedAt (UTC) | `2026-08-21T05:50:31.751Z` |
| stoppedAt (UTC) | `2026-08-21T05:50:38.222Z` |
| mode | webhook |
| status | success |
| callback_query_id_h8 | `758a39ac` |
| callback_chat_id_h8 | `3fbe2132` (ADMIN_A) |
| callback_message_id_h8 | `216da54b` |
| callback_data prefix | `sm:s:` |
| action | `spam` |
| lead_id_h8 | `9f78b00a` |
| prior_status | `pending` |
| new_status | `spam` |
| callback_outcome | applied (lifecycle path) |
| LEAD_EVENTS append | 1 (`manager_marked_spam`) |
| Update CLEAN Lifecycle | 1 |
| Expand Card Sync Copies | 1 item |
| Edit Lead Card Message | 1 attempt |
| Aggregate card_sync_ok | `0` |
| Aggregate warning | `Не все текущие копии карточки удалось обновить. [bad_request]` |
| Operator reply | `Лид отмечен как спам.` |

## Node path (ordered)

Telegram Trigger → Normalize → auth → Route → Prepare Early Callback Ack → Answer Callback Early → Read CLEAN → Resolve Callback Lead → Handle Callback Action → IF Callback Mutate → Update CLEAN Lifecycle → Append LEAD_EVENTS Callback → Read LEAD_DELIVERIES → Expand Card Sync Copies → IF Edit Lead Card → IF Pending Action Keyboard → **Edit Lead Card Message** → Aggregate Card Sync Result → Prepare Callback Answer → Safe Telegram Reply

## Classification

**A — state transition succeeded + visual card update failed.**
