# MULTI-CARD-SEND-FIX-v1

## Defect

`Capture Admin Reply` jsCode:

```js
const j=$input.first().json; return [{ json: { ...j, ... } }];
```

Recent Leads emitted N cards + notice, but Capture collapsed to 1 → Telegram sent only «Архивная карточка 1 из N».

## Fix

Passthrough all items:

```js
return $input.all().map((item) => ({ json: { ...item.json, admin_reply_captured: true, reply_len: ... } }));
```

## Verification

Live acceptance: `/leads 3` → capture=4, telegramItems=4; `/leads 5` → 6/6; ordinals 1..N unique lead hashes.
