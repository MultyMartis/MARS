# DEDUPE HISTORY RENDERING v1

Internal Sheets/dedupe values remain technical. Telegram rendering maps:

| match type | Human text |
|------------|------------|
| same_message | Это повторная обработка того же сообщения. |
| phone | Ранее уже была заявка с этого телефона. |
| email | Ранее уже была заявка с этого email. |
| messenger | Ранее уже была заявка из этого мессенджера. |
| site_only | Ранее была другая заявка с этого сайта. |
| multi_evidence | Найдена предыдущая заявка с совпадающими контактами. |

Safe previous timestamps render as `дд.мм.гггг чч:мм`.

Forbidden in cards: match keys, lead IDs, dedupe keys, technical enums.

Fixtures: H03/H04/H05 · live TG4/TG5/TG6.
