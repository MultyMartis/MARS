# GLOSSARY v1

- **Operational.dev** — активный workflow единственного Gmail intake и доставки лидов.
- **Admin.dev** — активный workflow Telegram-команд и callbacks.
- **Rollback workflow** — неактивный Sales-Manager-v2 для recovery reference.
- **ACCESS_CONTROL** — durable source of truth для staff roles/status.
- **Claim-before-send** — резервирование recipient delivery до Telegram send.
- **LEAD_DELIVERIES** — ledger получательских доставок и карточек.
- **Lifecycle** — `pending → processed|spam`; первая валидная смена побеждает.
- **Action token** — непрозрачный 12-символьный token в callback `sm:p:`/`sm:s:`.
- **Archive card** — read-only карточка из `/leads`, без кнопок.
- **Parser version** — версия извлечения полей; сейчас `sm-parser-v3.2`.
- **Message format version** — версия Telegram presentation; сейчас `sm-msg-v2.2`.
- **Shared core** — планируемая общая логика без client secrets/config.
- **Client profile** — планируемая изолированная конфигурация клиента.
- **SAFE UNKNOWN** — факт без достаточного evidence, который нельзя утверждать.