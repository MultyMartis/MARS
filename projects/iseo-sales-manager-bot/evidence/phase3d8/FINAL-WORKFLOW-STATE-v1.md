# FINAL WORKFLOW STATE v1

| Workflow | ID | Active | Nodes |
|----------|----|--------|------:|
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | false | 19 |
| i-SEO Sales Manager - Operational.dev | xSnXPy8cEHoZw6xG | true | 45 |
| i-SEO Sales Manager - Admin.dev | wLrLp4WQHm1VJmxz | true | 57 |

## Operational.dev highlights

- Sole Gmail intake preserved
- Claim-before-send path preserved
- Format button bridge fields present
- Send With Buttons: top-level `replyMarkup=inlineKeyboard`
- OpenRouter disabled
- AI OFF

## Admin.dev highlights

- Telegram message + callback_query trigger
- ACCESS_CONTROL SoT
- `/my_status`, `/delivery_status`, `/delivery_users`
- Handle Callback lead token = FNV (synced with Format)
- Actor hash remains sha256

## ACCESS_CONTROL

- active admins = 1
- active moderators = 1
- revoked moderators = 2
- revocation is intentional; Olya/Nikita were not restored

## Safety counters (this phase)

- AI provider calls = 0
- Automatic client messages = 0
- Workflows created = 0
- Parser runtime changes = 0
- Semantic-classification runtime changes = 0

## Verdict

`COMPLETE — BASELINE AND BACKUP READY; LIVE BUTTON CONFIRMATION PENDING`

API evidence proves both button payloads. Operator visual confirmation of both Telegram clients remains pending because `Expand Card Sync` found 1 copy in the harness.
