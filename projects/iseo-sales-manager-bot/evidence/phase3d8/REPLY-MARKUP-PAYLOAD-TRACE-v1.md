# REPLY-MARKUP PAYLOAD TRACE v1

Sanitized structural/live trace for new `🟢 Новый лид` cards; `/leads` archive cards are outside this actionable path.

## Stage table

| Stage | Pre-repair observation | Repair / post-repair fact | Acceptance |
|---|---|---|---|
| OPS Format Telegram Lead Card | `telegram_reply_markup` existed; `telegram_has_buttons` and `telegram_callback_*` absent | Sets `telegram_has_buttons`, `telegram_callback_processed`, `telegram_callback_spam`; retains `telegram_reply_markup` | Harness PASS |
| Expand Delivery Recipients | Lead payload spread to eligible recipients | Action fields preserved for 2 recipients | 2 eligible copies |
| Prepare Delivery Claims | Delivery items prepared with lead payload | Action fields preserved | 2 claims |
| Upsert LEAD_DELIVERIES Claim | Sparse Sheets output does not carry full action payload | Expected; restore stage uses prepared items | No contract regression |
| Restore Claimed Delivery Items | Restores original prepared lead item | Buttons/callback fields restored | Harness PASS |
| IF Lead Has Action Buttons | Missing boolean forced false/plain path | `telegram_has_buttons=true` selects With-Buttons path | true=2, false=0 |
| OPS Send Telegram Lead Card With Buttons | `replyMarkup` + `inlineKeyboard` nested in `additionalFields`; API response lacked `reply_markup` | Both parameters lifted to top-level, as required by n8n `addReplyMarkup()` | API returned markup on 2/2 sends |
| Telegram API result | Text only | `reply_markup.inline_keyboard` contains both buttons and `sm:p:` / `sm:s:` callbacks | PASS |
| Admin Handle Callback Action | sha256 lead token did not match Format FNV token; `manager_action_unauthorized` | Lead token synchronized to FNV dual-hash; actor hashes remain sha256 | pending→processed applied |
| Edit Lead Card Message | Not reachable through failed callback | Edited card successfully and removed buttons | PASS for found copy |
| Expand Card Sync | Not accepted | Harness found 1 card copy | ATTENTION: visually verify second moderator copy |
| Answer Callback Query | Synthetic query id cannot be acknowledged | Expected synthetic-fixture failure; real clicks provide real query ids | Expected limitation |
| Gmail PROCESSED | Synthetic fixture has no real Gmail id | Expected synthetic-fixture failure | Expected limitation |

## Payload facts

- `telegram_reply_markup` is an object with `inline_keyboard`, not a JSON string.
- The live sender uses top-level `replyMarkup` / `inlineKeyboard`.
- Both live sends returned `reply_markup` with processed and spam actions.
- Callback values use the existing `sm:p:` and `sm:s:` prefixes.
- Pending actionable cards have buttons; non-pending and archive cards remain buttonless.
- The same With-Buttons node serves both eligible recipients.
