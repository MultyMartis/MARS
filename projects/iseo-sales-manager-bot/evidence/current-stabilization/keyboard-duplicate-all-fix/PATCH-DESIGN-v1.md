# PATCH-DESIGN-v1

## Goals

1. `COUNT(logical filter = all) = 1` on main reminder keyboard.
2. Keep field-expression Telegram binding (do not restore whole-object `inlineKeyboard`).
3. Touch Admin.dev only; leave Operational.dev, schedule, claims, CLEAN/DEDUP, ACCESS untouched.

## Changes

### A. `flattenInlineKeyboardUi` (Reminder Build Claims + Prepare Callback Answer)

- Unused slots → empty `text` / empty `cb`.
- Pad with All **only** when there are zero real buttons (safety fallback for empty digest).
- Stop `flat[i-1] || { text: padT, cb: padC }` reuse of All for every missing index.

### B. Exact-size send path (Send Reminder)

- Add Switch `Switch Reminder Keyboard Size` on `rm_kb_n` ∈ {1..8}.
- Add `Send Reminder Telegram KB1`…`KB8` with packed fixedCollection truncated to N rows/buttons.
- Archive disable previous fixed-8 node as `Send Reminder Telegram (ARCHIVED fixed-8)`.
- Downstream: each KB* → `Reminder Stamp` (ledger unchanged).

### C. Exact-size callback replies

- `rm_kb_band = rm_kb_n` (exact), not rounded 4/8/12/14.
- Expand `Switch Reply Keyboard Band` to 1..14 → `Safe Telegram Reply KB1`…`KB14`.

## Non-goals

- No reminder schedule / window / claim / `last_window` edits.
- No ACCESS writes.
- No Operational.dev edits.
- No group-filter selector redesign.

## Deploy stamp

`2026-08-27T14-56-02-910Z` → Admin.dev `updatedAt` `2026-08-27T14:56:04.027Z`.
