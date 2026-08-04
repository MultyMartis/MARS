# ACTION-BUTTON FORENSIC v1

## Defect

Original auto-delivered `🟢 Новый лид` cards showed text but no lifecycle buttons:
- `✅ Отметить обработанным`
- `🚫 Отметить как спам`

Archive `/leads` cards are buttonless by design and are out of scope.

## Method

- GET-only n8n workflow read (`X-N8N-API-KEY` from gitignored env)
- Structural inspection of Format / Expand / Restore / IF / Send nodes
- Live synthetic execution traces (sanitized)
- No parser changes; no AI; no Sales-Manager-v2 activation

## Findings

### A. Routing

`IF Lead Has Action Buttons` condition: `{{$json.telegram_has_buttons}} === true`.  
Pre-repair Format never set this flag → always plain Send.

### B. Keyboard assembly

`Send Telegram Lead Card With Buttons` stored `replyMarkup`/`inlineKeyboard` under `additionalFields`.  
n8n Telegram `addReplyMarkup()` requires top-level parameters → messages sent without keyboard even when IF routed correctly after Format bridge.

### C. Callback contract

Admin callback token algorithm (sha256) ≠ Format token algorithm (FNV).  
After buttons restored, synthetic callback still unauthorized until Admin FNV sync.

## Conclusion

Buttons missing was a **delivery payload / Telegram node configuration** defect chain, not a parser or archive issue. All three layers required repair for end-to-end lifecycle actions.
