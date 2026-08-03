# MY-STATUS LIVE NON-ADMIN ACCEPTANCE v1

**Date:** 2026-08-04  
**Operator approval:** explicit Phase 3D.6 live acceptance closeout  
**Subject:** real non-Admin test account (opaque ref `u:518CC34C4C0F`)  
**Evidence type:** operator-confirmed Telegram UI text (no screenshot / raw IDs committed)

## Confirmed PASS

### 1. Revoked state (`/my_status`)

Operator-confirmed reply:

```text
Ваш статус

Роль: бывший модератор
Рабочие права: отозваны

Публичные команды остаются доступны.
Для восстановления прав обратитесь к администратору.
```

### 2. Moderator/active state after restoration (`/my_status`)

Operator-confirmed reply:

```text
Ваш статус

Роль: модератор
Статус: активен

Доступно:
— работа с карточками лидов;
— отметка «Обработан»;
— отметка «Спам».

Административные настройки недоступны.
```

## Proven facts

- `/my_status` responds for a real non-Admin user after hotfix `3d6b-my-status-code-mode`
- revoked state is read from ACCESS_CONTROL
- moderator/active state is read from ACCESS_CONTROL after re-approval
- no Admin capabilities are exposed to the test account
- public commands remain available after revocation
- role changes take effect without workflow edits
- exactly one response per observed `/my_status` (operator visual confirmation)
- final test-account role at acceptance: **moderator / active**
- Оля remained **moderator / active**
- Андрей remained sole **admin / active**

## Not included in Git

Raw Telegram user id, chat id, username handle, screenshot, and raw execution payloads are excluded from this receipt.
