# ROOT-CAUSE-v1 — Duplicate «Все» on natural reminder keyboard

## Classification

`UNUSED_SLOT_DEFAULTS_TO_ALL`

## Proven first divergence

Admin.dev workflow `wLrLp4WQHm1VJmxz`, Code node **Reminder Build Claims**, helper `flattenInlineKeyboardUi`.

Call site (digest send path):

```js
...flattenInlineKeyboardUi(digest.telegram_inline_keyboard_ui, 8, '📋 Все', 'sm:g:all')
```

Pre-fix helper behavior:

- Flattens real UI buttons into `flat[]`.
- Sets `rm_kb_n = min(flat.length, slots)`.
- For every slot `i = 1..slots`, if `flat[i-1]` is missing, **pads with** `{ text: padT, cb: padC }` where defaults are `📋 Все` / `sm:g:all`.

Same helper + pad pattern existed in **Prepare Callback Answer** (pads to rounded band 4/8/12/14).

## Natural evidence (execution 41719)

- Window: `pending-reminder:2026-08-27:10:00:Europe/Moscow`
- Renderer real buttons: **5** (`digest_button_count=5`, `rm_kb_n=5`)
- Slots 1–5: Audit / SEO / Other / Older / All (legitimate)
- Slots 6–8: pad `📋 Все` / `sm:g:all` (duplicates)
- Telegram `reply_markup.inline_keyboard` contained the real set **plus three extra All buttons**

## Why field-expression architecture stayed

Whole-object `inlineKeyboard` was previously dropped by n8n. FixedCollection field expressions (`rm_bN_text` / `rm_bN_cb`) remain required. The bug is **slot emission content**, not the binding mechanism.

## Rejected alternate classes

| Class | Why rejected |
|-------|----------------|
| `LAST_BUTTON_REUSED` | Pad text is always All, not last category |
| `STATIC_FIXEDCOLLECTION_SLOT_LEAK` | Expressions read JSON fields; fields were actively padded |
| `BUTTON_COUNT_BRANCH_MISMATCH` | Send Reminder was a single fixed-8 node (no branch yet) |
| `KEYBOARD_PACKER_DUPLICATES_ALL` | Digest builder adds All once; duplicates appear only after flatten pad |

## Repair direction

1. Stop padding unused slots with All (empty unused fields).
2. Route Telegram send/reply nodes by **exact** `rm_kb_n` / `rm_kb_band` so empty slots are never sent.
