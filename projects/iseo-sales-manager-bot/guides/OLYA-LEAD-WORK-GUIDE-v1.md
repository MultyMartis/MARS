# Руководство Оли по работе с лидами (v1)

**Продукт:** i-SEO Sales Manager  
**Аудитория:** модератор (Оля)  
**Версия:** 1.4 · 2026-08-03 (Phase 3D.5 — роль модератора в реестре ACCESS_CONTROL)

Это рабочая инструкция без технических деталей. Бот помогает принимать заявки с сайта и готовить ответ; решение и отправку клиенту делает человек.

---

## 1. Ваша роль

- Вы — **модератор**, не администратор.
- Рабочие права выдаются индивидуально и хранятся в реестре доступа (не через правку кода).
- Вам доступны менеджерские `/start` и `/help`, карточки заявок и кнопки «Обработан» / «Спам».
- Команды администратора (`/config`, `/leads`, управление пользователями) вам недоступны — это нормально.

## 2. `/start` и `/help`

- **`/start`** — бот готов к работе с заявками; можно копировать контакт/ответ и отмечать статус.
- **`/help`** — памятка по значкам типа лида, блокам копирования и кнопкам. Статус в v1 нельзя обратить назад; при ошибке — к администратору.

## 3. Карточка и кнопки

- В карточке можно скопировать имя, контакт и готовый ответ.
- ✅ **Обработан** — вы связались с клиентом.
- 🚫 **Спам** — заявка нецелевая.
- Кнопки приходят только в рабочий менеджерский чат/назначение, не всем пользователям бота.

## 4. Если доступ отозвали

- Сообщение: рабочие права модератора отозваны.
- Кнопки перестанут приниматься сразу.
- `/start`/`/help` могут остаться только как справочные (без рабочих действий), пока администратор не выдаст права снова.

## 5. Чего бот не делает

- Не пишет клиенту сам.
- Не включает ИИ в обычном режиме.
- Не делает вас администратором.


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.
