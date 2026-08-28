# REMINDER-EXACT-LEAD-FORENSIC-v1

## Root cause (proven)

`queue_open` branch in **Handle Callback Action** used a compact renderer and set `answer_text: 'Лид'` instead of delegating to `buildFinalCard` with pending action keyboard.

## Post-patch behavior (acceptance @ 2026-08-28T12:04:51Z)

- Route: `sm:q:` from `/leads` pending synth token
- `answer_text`: **Карточка**
- `edit_keyboard_mode`: **pending_actions**
- `has_actions`: true
- `standalone_lid`: 0
- **pass:** true

## Fix artifact

`implementation/patches/HandleCallbackAction.canonical-card-unification.js` — deployed Admin.dev @ 2026-08-28T11:09:44Z.
