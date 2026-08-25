# NATURAL REMINDER SEND PATH v1

Date: 2026-08-25  
Workflow: `wLrLp4WQHm1VJmxz` (Admin.dev)  
Execution inspected: **40019**

## Window

- Business window: `pending-reminder:2026-08-25:10:00:Europe/Moscow`
- Pending count snapshot: **19**
- Digest contract: `iseo-pending-digest-renderer-v1.1`
- Recipient: ADMIN_A only (ACCESS unchanged)

## Path observed

1. Reminder Schedule Trigger → gate/claims → Reminder Build Claims  
2. Digest renderer produced text + `telegram_inline_keyboard_ui` (`telegram_has_buttons: true`)  
3. Merge Reminder Send Payload carried keyboard UI object  
4. **Send Reminder Telegram** sent message successfully (`message_id` present)  
5. Telegram API result: **no `reply_markup`**

## Divergence

First divergence: keyboard present in renderer/merge → **absent at Telegram provider result**.

## Delivery/dedupe note

Natural window showed one reminder for the logical window with no recovery duplicate observed in this inspection.

`DELIVERY/DEDUPE LIVE STABLE` (text delivery only; does **not** imply inline navigation acceptance).

## PII

No customer PII stored in this evidence file.
