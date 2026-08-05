# PRODUCT ARCHITECTURE v1

## Исполняемая архитектура сейчас

1. Operational.dev — единственный Gmail intake; **Parser `sm-parser-v3.3`** + Lead Semantic Model v1; **First Reply `sm-reply-v2.1`** + **Human Reply Style `sm-human-v1.0`**; CLEAN/RAW; Format **`sm-msg-v2.4`**; recipient expansion; claim-before-send; **fail-closed ledger read**; Telegram delivery и Gmail finalization. Не изменялся в Phase 3F.1.
2. Admin.dev — единая Telegram ingress-точка для `message` и `callback_query`; ACCESS_CONTROL, команды, lifecycle transitions, синхронизация копий карточек и архив (stored reply drafts); **Phase 3F.1**: read-only pending-lead view (`/pending_count`, `/pending_leads`, `/pending_leads_test`) + daily reminder engine (`sm-pending-reminder-v1.0`) за внутренним 15-минутным Schedule Trigger.
3. Sheets — durable state и журналы; Telegram — операторский интерфейс; Gmail — источник и label lifecycle. **Phase 3F.1** добавляет additive-таб `REMINDER_DELIVERIES`.
4. Sales-Manager-v2 — неактивный rollback baseline.

## Инварианты

- AI OFF остаётся полностью рабочим и не вызывает AI provider (`ai_enabled=false`).
- Ответ клиенту только копируется менеджером вручную.
- Known-information guard: не запрашивать уже известные сайт/телефон/email/Telegram/задачу.
- ACCESS_CONTROL — источник полномочий; revoked имеет приоритет.
- Claim создаётся до send; повторный poll не должен повторять доставку.
- Archive `/leads` карточки не имеют lifecycle-кнопок и не перегенерируют draft.

## Semantic + reply layer (Phase 3E.1 / 3E.2)

- Authority: [LEAD-SEMANTIC-MODEL-v1.md](../architecture/LEAD-SEMANTIC-MODEL-v1.md), [PARSER-3.3-CONTRACT-v1.md](../architecture/PARSER-3.3-CONTRACT-v1.md), [FIRST-REPLY-ENGINE-v2.md](../architecture/FIRST-REPLY-ENGINE-v2.md), [HUMAN-REPLY-STYLE-v1.md](../architecture/HUMAN-REPLY-STYLE-v1.md), [KNOWN-INFORMATION-GUARD-v1.md](../architecture/KNOWN-INFORMATION-GUARD-v1.md), [DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](../architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md), [MANAGER-CARD-v2.4-CONTRACT-v1.md](../architecture/MANAGER-CARD-v2.4-CONTRACT-v1.md).
- Website states, intent precedence, comment boundary, quality и context-aware first reply — deterministic AI OFF path.

## Pending leads + daily reminder (Phase 3F.1)

- Authority: [PENDING-LEADS-VIEW-v1.md](../architecture/PENDING-LEADS-VIEW-v1.md), [PENDING-REMINDER-v1.md](../architecture/PENDING-REMINDER-v1.md), [REMINDER-DELIVERY-IDEMPOTENCY-v1.md](../architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md).
- Read-only view over existing `lead_clean_v2`; no new lifecycle; deduplicated by business key; oldest-first.
- Reminder engine живёт внутри Admin.dev (не отдельный workflow); fail-closed на каждом шаге (disabled/invalid config/zero pending/below minimum/already-completed window/ledger error/claim failure).
- Production: `pending_reminders_enabled=false` до явной активации оператором.

## Планируемая граница

Целевой reusable core отделяет общую логику от client config, bot/secrets, sources, storage и staff registry. Это архитектурное направление, а не существующий fleet runtime.