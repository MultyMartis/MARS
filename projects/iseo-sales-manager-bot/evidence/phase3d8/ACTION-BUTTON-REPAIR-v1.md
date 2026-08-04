# ACTION BUTTON REPAIR v1

**Phase:** 3D.8  
**Workflow IDs unchanged:** Operational `xSnXPy8cEHoZw6xG` · Admin `wLrLp4WQHm1VJmxz`  
**Workflows created:** 0  
**AI / OpenRouter:** OFF / disabled  
**Sales-Manager-v2:** inactive

## Triple root cause

1. **Format routing gap** — Format set `telegram_reply_markup` but never `telegram_has_buttons` or `telegram_callback_*`. `IF Lead Has Action Buttons` required `telegram_has_buttons === true`, so cards always went to plain `Send Telegram Lead Card`.
2. **Send parameter nesting** — On the With-Buttons node, `replyMarkup` + `inlineKeyboard` lived under `additionalFields`. n8n `addReplyMarkup()` reads them as **top-level** parameters; nested values were Object.assigned into the Telegram body and ignored. API returned message text **without** `reply_markup`.
3. **Admin token algorithm drift** — Format used FNV dual-hash tokens; Admin `Handle Callback Action` used `sha256hex(lead_id).slice(0,12)`. CLEAN has no stored `telegram_action_token` (written before Format), so lookup failed → `manager_action_unauthorized`.

## Repairs

| Wave | Target | Change |
|------|--------|--------|
| 3D.8 Format | OPS Format Telegram Lead Card | Add `telegram_has_buttons`, `telegram_callback_processed`, `telegram_callback_spam`; keep `telegram_reply_markup` |
| 3D.8.1 Send | OPS Send Telegram Lead Card With Buttons | Lift `replyMarkup` + `inlineKeyboard` to top-level parameters |
| 3D.8.2 Token | Admin Handle Callback Action | Lead token = Format FNV dual-hash; `actorHash` remains sha256 |

## Post-repair verification

- Local harness: **30/30 PASS**
- Live synthetic fixture delivered to **2 recipients** (active admin + active moderator).
- Both Telegram API sends returned `reply_markup.inline_keyboard` with both buttons and `sm:p:` / `sm:s:` callbacks.
- No duplicate sends appeared in the short poll window.
- After token sync: callback `pending → processed`; `Edit Lead Card Message` succeeded and removed buttons from the edited copy.
- `Expand Card Sync` found **1** copy in harness. **ATTENTION:** visually verify the second moderator copy.
- `Answer Callback Query` fails for the synthetic query id as expected; real Telegram clicks carry real query ids.
- Gmail `PROCESSED` fails for the synthetic fixture as expected because it has no real Gmail id.

## Final workflow state

- Operational `xSnXPy8cEHoZw6xG`: active, 45 nodes.
- Admin `wLrLp4WQHm1VJmxz`: active, 57 nodes.
- Sales-Manager-v2 `h8I2Tl2yl4uzhUnB`: inactive.
- OpenRouter disabled; AI OFF.

## Non-changes

- Parser runtime unchanged (`sm-parser-v3.2`)
- Semantic classification unchanged
- No AI enablement
- Olya / Nikita not restored
- No new workflows
