# Руководство Оли — работа с лидами (v1)

> Phase 3D.8 access note: intended guide recipient is currently **revoked by operator choice**. This remains a future moderator guide; do not restore access from this document.

Новые заявки приходят в **личный чат** с ботом Sales Manager.

1. Откройте карточку лида.
2. Прочитайте комментарий клиента и блок **Интерес** — готовый ответ должен звучать как обычное сообщение менеджера (Human Reply Style v1; пакет примеров: `evidence/phase3e2-2/ACTUAL-HUMAN-COPY-PACKET-v1.md`).
3. Скопируйте контакт и при необходимости блок **✉️ Ответ клиенту** (бот сам клиенту не пишет).
4. Если ответа нет и есть предупреждение про контакт — сначала проверьте способ связи; не отправляйте клиенту системные формулировки.
5. После связи с клиентом нажмите **✅ Обработано** или **🚫 Спам**.
6. Статус **общий** для всей команды: повторный клик не перезапишет чужой статус.
7. Кнопки на всех копиях карточки синхронизируются.

Команды: `/start`, `/help`, `/my_status`.

## Phase 3E.2.3 note

Human Reply Style is already operator-accepted and is not being redesigned. During the inactive quiet window no new cards should arrive from Operational.dev. After reactivation, repeated identical cards must be reported to the operator; do not process both copies and do not ask for access restoration from this guide.

## Phase 3F.1 note

A new read-only overview (`/pending_count`, `/pending_leads`) and an optional daily reminder now exist for active moderators/Admin. These do not change how you process a card — you still copy the reply and press **✅ Обработано** / **🚫 Спам** as before. Reminders are currently **switched off** in production; this guide will be updated separately if/when reminders are activated and if access is ever restored.


## Архив и история (3F.2.1)

- `/leads` — архивные карточки (без кнопок статуса)
- `/lead_history <номер>` — история по номеру из `/leads`
- Источник для форм сайта отображается как «Сайт i-seo.su»

## Phase 3F.2.2 note

В `/help` для модератора доступны `/leads`, `/lead_history`, `/pending_count`, `/pending_leads`, `/reminder_status`. Настройки ИИ и напоминаний — только у администратора. История лида показывает человеческие формулировки событий (без машинных кодов).

## Phase 3G.1 note

First-contact drafts become INTLSEO approved templates with the manager's approved client-facing name. Still: copy manually, never assume auto-send. Guidance under the tip block is for you, not the client. Access remains revoked for this guide's intended recipient unless separately restored — this phase does not restore access.

## Phase 3G.2 note

- Имя в ответе клиенту задаёт только администратор (по **номеру профиля**), не по Telegram-нику.
- Для модератора из профильных команд доступна только `/my_reply_profile` — посмотреть своё имя в ответе.
- Если в карточке предупреждение, что имя не задано — напишите администратору; не подставляйте ник вручную в текст клиенту.
- Доступ (права модератора) **не** меняется командами имени. Напоминания и ИИ по-прежнему выключены, пока оператор не включит отдельно.
