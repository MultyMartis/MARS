# PRODUCT ARCHITECTURE v1

## Исполняемая архитектура сейчас

1. Operational.dev — единственный Gmail intake; parsing, CLEAN/RAW, lifecycle-card formatting, recipient expansion, claim-before-send, Telegram delivery и Gmail finalization.
2. Admin.dev — единая Telegram ingress-точка для `message` и `callback_query`; ACCESS_CONTROL, команды, lifecycle transitions, синхронизация копий карточек и архив.
3. Sheets — durable state и журналы; Telegram — операторский интерфейс; Gmail — источник и label lifecycle.
4. Sales-Manager-v2 — неактивный rollback baseline.

## Инварианты

- AI OFF остаётся полностью рабочим и не вызывает AI provider.
- Ответ клиенту только копируется менеджером вручную.
- ACCESS_CONTROL — источник полномочий; revoked имеет приоритет.
- Claim создаётся до send; повторный poll не должен повторять доставку.
- Archive `/leads` карточки не имеют lifecycle-кнопок.

## Планируемая граница

Целевой reusable core отделяет общую логику от client config, bot/secrets, sources, storage и staff registry. Это архитектурное направление, а не существующий fleet runtime.