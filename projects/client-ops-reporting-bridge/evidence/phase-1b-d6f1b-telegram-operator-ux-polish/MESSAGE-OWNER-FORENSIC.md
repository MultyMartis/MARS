# Message Owner Forensic

## Defect ownership (D6F1A gallery)

| Defect | Owner |
|--------|-------|
| English titles / ATTENTION / OK enums | Gallery `buildMessage` |
| UTC timestamps | Gallery + n8n production fallback |
| Underscore→hyphen filename distortion | Gallery `safe()` replace `_`→`-` |
| Synthetic `offers0-N.xml` | Gallery scenario copy |
| Field dump / empty impact | Gallery structure |
| Production path still English-ish status header | n8n Telegram expression |

## D6F1B owner

Single authoritative formatter:

- JS: `n8n/runners/lib/client-ops-telegram-operator-message.mjs`
- Python twin: `src/client_ops_reporting_bridge/telegram_operator_message.py`

n8n Telegram node: pass-through full operator bodies; HTML parse_mode so `offers0_*.xml` is not entity-parsed (wrapped in `<code>`).

Token: `D6F1B_MESSAGE_FORMATTING_OWNER_PROVEN`
