# CARD STATUS SYNC — empty full_card keyboard repair

**Date:** 2026-08-21  
**Contour:** Admin.dev  
**Evidence:** `evidence/current-stabilization/card-status-sync/`

## Defect

Status callbacks committed CLEAN/LEAD_EVENTS, selected the clicked message, then `editMessageText` failed because Edit nodes always included `🟢 Полная карточка` with empty `telegram_callback_full_card` on non-digest paths.

## Repair

Conditional inclusion of the full_card button in:

- `Edit Lead Card Message`
- `Edit Lead Card Message Pending`

## Live

Spam exec `36654` and Processed exec `36657`: `card_sync_ok=1`, clicked==selected, terminal labels correct.
