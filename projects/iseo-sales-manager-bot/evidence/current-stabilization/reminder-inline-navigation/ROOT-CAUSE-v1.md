# ROOT CAUSE v1

## Exact cause

**C / D hybrid (schema formatting):**  
Renderer produced a correct keyboard, but the Telegram send node bound `inlineKeyboard` as a **whole-object expression**. n8n silently omitted `reply_markup` from the outbound Telegram payload. No API error was raised.

Not:

- A alone (send “dropped” a correctly bound keyboard) — binding never resolved into Telegram’s fixedCollection shape
- B (renderer never produced keyboard) — false for natural path 40019
- E (wrong branch without keyboard UI) — false; same digest path had UI
- empty callback rejection — not observed on natural send (message succeeded without markup)

## Proof ladder

1. Exec 40019: UI present → Telegram result without `reply_markup`
2. Probe: whole-object expression → message OK, no markup
3. Probe: static fixedCollection → markup present
4. Probe: static + per-field expressions → markup present
5. Live deploy of flatten + field-expression Send Reminder / Safe Telegram KB bands
6. ADMIN_A acceptance: digest/group/lead all `has_reply_markup: true`

## Repair class

Field-expression static keyboards + flatten helpers. No schedule/claims/ACCESS changes.
