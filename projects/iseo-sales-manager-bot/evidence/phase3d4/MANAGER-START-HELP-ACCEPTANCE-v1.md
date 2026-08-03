# MANAGER START HELP ACCEPTANCE v1

**Phase:** 3D.4  
**Scope:** role-aware `/start` and `/help` for manager-only users

---

## 1. Routing rule

| User | `/start` | `/help` |
|------|----------|---------|
| Admin (`admin_user_ids`) | Admin panel greeting (contour + AI mode) | Full Admin command list |
| Manager only (`manager_action_user_ids`, not admin) | Manager greeting | Manager help (buttons + copy blocks; no Admin commands) |
| Unauthorized | `Доступ запрещён.` | `Доступ запрещён.` |

---

## 2. Expected manager `/start` (synthetic shape)

```text
Sales Manager — менеджерский режим

Вы можете отмечать лиды кнопками под карточкой:
✅ Обработанным · 🚫 Спам

Карточки приходят в рабочий чат менеджеров.
Admin-команды (/status, /leads, …) вам недоступны.

/help — краткая памятка по работе с карточками.
```

- No contour/AI admin wording.
- No command list beyond pointer to `/help`.
- No secrets, IDs, or internal version strings.

---

## 3. Expected manager `/help` (synthetic shape)

```text
Памятка менеджера

Карточка лида:
• 🟢🟡🟠🔵 — тип лида (новый / повтор / …)
• 🕓 — ожидает обработки
• ✅ / 🚫 — уже отмечен

Кнопки под карточкой:
✅ Отметить обработанным — лид закрыт
🚫 Отметить как спам — не целевой лид

Копирование:
• Имя, телефон, email — нажмите на «капсулу»
• Ответ клиенту — скопируйте блок «Ответ клиенту»

Бот клиенту сам не пишет.
При сбое — напишите оператору (Андрей).
```

---

## 4. Acceptance matrix

| Check | Actor | Method | Result |
|-------|-------|--------|--------|
| Admin `/start` | operator hash 3FBE21323E22BFC1 | harness + live | **PASS** — Admin panel shape |
| Admin `/help` | operator | harness + live | **PASS** — full Admin list |
| Manager `/start` | Olya hash E6714550214106BA | **synthetic harness** | **PASS** — manager greeting shape |
| Manager `/help` | Olya hash E6714550214106BA | **synthetic harness** | **PASS** — manager help shape |
| Manager `/start` | Olya | **live human Telegram** | **PENDING** |
| Manager `/help` | Olya | **live human Telegram** | **PENDING** |
| Unauthorized `/start` | unknown user | harness | **PASS** — deny |

---

## 5. Regression guard

Manager `/start` and `/help` must **not** expose:

- `/status`, `/leads`, `/config`, `/ai_on`, `/ai_off`
- Admin contour/AI toggle wording
- Allowlist counts or other user identities

---

## 6. Notes

Synthetic harness validates routing and reply shape for the Olya hash without requiring a live second-user session during patch acceptance. Operator attestation for live Olya confirmation is a separate human gate documented in `PHASE3D4-ACCEPTANCE-RECEIPT-v1.md`.

---

*Related: ROLE-AUTHORIZATION-MODEL-v1 · guides/OLYA-LEAD-WORK-GUIDE-v1.md.*
