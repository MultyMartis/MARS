# REPORT — ISEO Sales Manager Bot — current card status sync fix v1

## 1. Verdict

**CARD STATUS SYNC LIVE PASS — SPAM/PROCESSED UPDATE THE CLICKED CURRENT CARD**

## 2. Operator-visible defect

Spam ack appeared (`Лид отмечен как спам.`) while the original card stayed Pending with active Spam/Processed buttons.

## 3. Callback execution

Incident Admin.dev exec **`36629`** (`2026-08-21T05:50:31Z`): action `spam`, ADMIN_A, early ack + full mutate path completed.

## 4. Authoritative state result

Class **A**: CLEAN update ×1, LEAD_EVENTS ×1 (`manager_marked_spam`), status `spam`. Transition committed.

## 5. Clicked message

`callback_chat_id_h8=3fbe2132`, `callback_message_id_h8=216da54b`.

## 6. Selected edit target

Same chat/message (`message_ref_source=callback_initiator`, contract `iseo-authoritative-card-instance-v1.2`). **Not** a stale-instance miss.

## 7. Telegram edit result

`Edit Lead Card Message` → `Bad Request: can't parse InlineKeyboardButton: Text buttons are unallowed in the inline keyboard`. Aggregate `card_sync_ok=0` + sync warning; semantic reply still spam.

## 8. Exact root cause

Edit nodes always attached `🟢 Полная карточка` with `$json.telegram_callback_full_card`. That field is set only for digest `queue_open`/`full_card`. On Spam/Processed/Reopen it is empty → Telegram rejects the keyboard → UI sync fails.

## 9. Repair

Conditional full_card row on `Edit Lead Card Message` and `Edit Lead Card Message Pending` (include only when callback non-empty). Digest preserved. No callback redesign.

## 10. Spam live acceptance

Exec **`36654`**: applied, status spam, edit_ok, `card_sync_ok=1`, matched clicked, Spam label present, Pending absent, event ×1.

## 11. Processed acceptance

Exec **`36657`**: applied, status processed, edit_ok, `card_sync_ok=1`, matched clicked, Processed label present, Pending absent, event ×1.

## 12. Idempotency

- Spam `36665` applied (1 event) → `36666` idempotent (0 events).
- Processed `36658` idempotent (0 events).
- Idempotent re-edit may surface Telegram `message is not modified` (benign; distinct from empty-button failure).

## 13. Test routing

ADMIN_A only. Moderator/customer messages = 0. Real customer leads modified = 0. AI = 0.

## 14. Reminder acceptance impact

Patch before the planned ≥10:20 Europe/Moscow natural window; reminder code untouched. **That natural window may still be used** after this patch. Do not manual-fire reminder. Soak still blocked until reminder + digest click also PASS.

## 15. Backups

Private under `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\card-status-sync-20260821-local\backups\`. Manifests: PRE `FCA650F738960D19`, POST `238248E76B845C7E`.

## 16. Git

Clean worktree `agent/iseo-smb-card-status-sync` from `origin/mars/canonical-post-recovery`. Scope: `projects/iseo-sales-manager-bot/**` evidence/report/implementation note.

## 17. Remaining stabilization gates

- Natural reminder live PASS (window after patch OK to use)
- Operator actionable digest click PASS
- Then start 48h soak (this production patch resets soak baseline)
- Deferred: ACCESS/DELIVERY split, DND, `/announce`, `/admin`, legacy synth cleanup, PG/Google auth modernization, AI ON

---

## Counters

| Counter | Value |
|---------|------:|
| callback actions inspected | ≥1 incident + live waves |
| status transitions committed (incident) | 1 |
| lifecycle events created (incident) | 1 |
| clicked message_id matched selected edit target | YES (incident + live) |
| Telegram edit attempts (incident) | 1 |
| Telegram edit successes (incident) | 0 |
| Telegram edit successes (post-repair Spam/Processed) | 2 |
| stale/wrong card edit attempts (incident) | 0 |
| Spam live tests | PASS (`36654`, idem `36665/36666`) |
| Processed live tests | PASS (`36657`, idem `36658`) |
| duplicate lifecycle events (idempotent repeats) | 0 |
| moderator test messages | 0 |
| customer test messages | 0 |
| real customer leads modified | 0 |
| workflows modified | 1 (Admin.dev) |
| AI calls | 0 |

## Evidence index

`projects/iseo-sales-manager-bot/evidence/current-stabilization/card-status-sync/`
