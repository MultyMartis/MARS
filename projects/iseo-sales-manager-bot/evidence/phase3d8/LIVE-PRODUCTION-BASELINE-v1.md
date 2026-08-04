# LIVE PRODUCTION BASELINE v1

**Captured:** Phase 3D.8 (post button repairs)

| Workflow | ID | Active | Nodes |
|----------|----|--------|------:|
| Operational.dev | xSnXPy8cEHoZw6xG | true | 45 |
| Admin.dev | wLrLp4WQHm1VJmxz | true | 57 |
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | 19 |

## Versions

- environment=production
- ai_enabled=false
- parser_version=sm-parser-v3.2
- message_format_version=sm-msg-v2.2

## Access (counts only)

- active admins: 1
- active moderators: 1
- revoked moderators: 2

## Delivery

- sole Gmail intake
- multi-recipient fan-out
- claim-before-send + LEAD_DELIVERIES
- Admin-anchor Gmail finalization preserved
- original pending cards: inline action buttons restored (Format bridge + Send top-level keyboard + Admin FNV token sync)

## Repair and acceptance facts

- OPS Format sets `telegram_has_buttons`, `telegram_callback_processed`, `telegram_callback_spam` and retains `telegram_reply_markup`.
- OPS Send With Buttons exposes `replyMarkup` and `inlineKeyboard` as top-level parameters.
- Admin lead lookup uses Format-compatible FNV dual-hash; actor hashes remain sha256.
- Local harness: 30/30 PASS; both live synthetic recipient sends returned both buttons.
- No duplicate sends were observed in the short poll window.
- OpenRouter is disabled; AI OFF.
- Revoked roles remain intentional; Olya/Nikita were not restored.
