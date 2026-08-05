# PENDING LEAD REMINDER SPEC v1 — DRAFT

**Статус: DRAFT / NOT IMPLEMENTED в Phase 3D.8.**

> **Обновление (Phase 3F.1):** v1 этой спецификации **реализован** в Phase 3F.1 — см. [architecture/PENDING-REMINDER-v1.md](../architecture/PENDING-REMINDER-v1.md) (архитектура), [implementation/REMINDER-CONFIG-COMMANDS-v1.md](../implementation/REMINDER-CONFIG-COMMANDS-v1.md) (implementation) и `evidence/phase3f1/` (acceptance). Активация в production остаётся отдельным решением оператора — `pending_reminders_enabled=false` по умолчанию. Этот черновик сохранён как исходный замысел; авторитетным источником текущего поведения являются документы Phase 3F.1 выше.

## Schedule и eligibility

Один запуск ежедневно в `10:00` по настраиваемой timezone клиента. Получатели: только active Admin и active moderator из ACCESS_CONTROL с пригодным private delivery target. Public, pending, revoked и blocked исключаются.

## Selection и dedupe

Только лиды с lifecycle `pending`. Не более одного reminder на получателя в одном reminder window. Нужен durable ключ вида `pending-reminder:<window>:<recipient-ref>` без PII. Исторические окна не переотправляются после downtime.

## Сообщение

Компактная сводка: количество pending, возраст самого старого, несколько первых карточек/ссылок и безопасная пагинация. Предлагаемый русский текст (точная charter-формулировка не предоставлена — требует операторского утверждения):

> Напоминание: есть необработанные лиды — {count}. Самый ранний ожидает с {time}. Используйте /pending_leads для просмотра.

## Команды

- `/pending_count` — число pending без PII.
- `/pending_leads` — paginated read-only list; default page size и допустимые аргументы фиксируются harness.
- Карточки команды не создают новый lifecycle send и не должны обходить existing action-token contract.

## Acceptance

Timezone/DST, one-per-window, recipient revocation, empty set, pagination boundaries, restart, delayed schedule и no historical resend. Никаких client messages и AI calls.