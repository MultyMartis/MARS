# TELEGRAM TEXT CONTRACT v2

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3G.2 (+ 3G.2.1 response-guard addendum)  
**Status:** current authority for user-visible Telegram **text** tone, labels, and formats  
**Supersedes for text surfaces:** parts of [TELEGRAM-UX-CONTRACT-v1.md](TELEGRAM-UX-CONTRACT-v1.md) that describe wording/tone (card **layout blocks** remain in v1)

---

## 1. Purpose

Единый контракт всех **пользовательских** текстов Telegram: команды, `/start`/`/help`, статусы, профили ответа, карточки лидов, напоминания, ошибки. Цель — русский человеческий тон, без техжаргона и без утечки идентификаторов.

---

## 2. Tone

- Спокойный, деловой, короткий.
- Русский для оператора и менеджера.
- Без Markdown-акцентов как основного формата (риск parse errors) — prefer plain text или аккуратный HTML (`<b>`, `<code>`, `<pre>`).
- Без сырых enum (`active`, `revoked`, `ai_off`) в UI — только русские ярлыки.
- Без Telegram user ID, workbook ID, секретов, сырых JSON, stack traces.

---

## 3. Role and status labels (Russian)

| Internal | UI label |
|----------|----------|
| `admin` | Администратор |
| `moderator` | Модератор |
| `public` | Публичный |
| `blocked` (role) | Заблокирован |
| `active` | Активен / Доступ: Активен |
| `revoked` | Отозван / Доступ отозван |
| `pending` | Ожидает |
| `blocked` (status) | Заблокирован |

Card eligibility line: `Получает карточки: да|нет`.

Personalization flag: `Персональный ответ: включён|выключен`.

---

## 4. Reply profile surfaces

- Header list: `👤 Профили ответов клиентам`
- One profile: `👤 Профиль ответа клиенту №N` (when number known)
- Self: `👤 Мой профиль ответа клиенту`
- Fields order: Пользователь → Имя в ответе → Персональный ответ → Роль → Доступ → Получает карточки → optional Пример представления
- Intro example only when name valid: `"Меня зовут <имя>, компания INTLSEO."`
- Missing name warning (manager card): `⚠️ Не задано имя для ответа клиенту. Обратитесь к администратору.`
- Admin-only deny: `Эта команда доступна только администратору.`
- Invalid name hint points to number syntax: `/reply_name_set <N> <Имя>`

**Client name source:** ONLY `reply_sender_name`. Never display_name, username, actor, role, or nickname «Мопс» in customer `<pre>` copy.

---

## 5. Help / start

- **Admin** and **moderator** help are **separate explicit templates** (Phase 3G.2 / [ROLE-AWARE-HELP-BUILDER-v2.md](../implementation/ROLE-AWARE-HELP-BUILDER-v2.md)).
- Never substring-patch an existing help string to insert a command.
- HTML: wrap only slash-command tokens in `<code>` via `cmdHtml`; placeholders like `<номер>` render as `&lt;номер&gt;` **outside** code tags.
- Admin help **must** include reply-profile section (list/get/set/enable/disable + `/my_reply_profile`).
- Moderator help among profile commands: **only** `/my_reply_profile`.
- Moderator `/start` must show `Имя в ответах: <approved reply_sender_name>` (or `не задано`).
- **No-silent recognized-command invariant (3G.2.1):** every recognized command path must emit a valid reply, permission/validation reply, or safe internal-error fallback — never terminate without Telegram output.
- Fallback: `Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.`
- `/help` may split into ≤3 deterministic parts only if length would exceed Telegram 4096; current Admin help fits in one message.

---

## 6. Card / first-contact copy (unchanged hard rules)

- Customer block inside `<pre>` / copy fence only.
- Disclaimer outside: `Ответ клиенту автоматически не отправляется.`
- Company default: `INTLSEO`.
- Greeting: `Добрый день!`
- No auto-send. AI OFF default. Reminders OFF until explicit activation.
- Layout block order for lead cards: still [TELEGRAM-UX-CONTRACT-v1.md](TELEGRAM-UX-CONTRACT-v1.md) §2.

---

## 7. Warnings and fail-closed text

| Situation | Operator-facing text (pattern) |
|-----------|--------------------------------|
| Profile number missing | `Укажите номер профиля.` + example |
| Number not integer / not positive | `Номер профиля должен быть целым положительным числом.` |
| Number not found | `Профиль с таким номером не найден. Посмотрите доступные номера командой /reply_profiles.` |
| Enable without name | `Нельзя включить персональные ответы: сначала задайте имя командой /reply_name_set.` |
| Enable while revoked | Name kept; explain access revoked — cards not sent |
| Name set while revoked | `Имя сохранено, но пользователь не получает карточки.` |
| Name set, disabled | Suggest `/reply_name_enable` |

Access role/status **must not** change as a side effect of reply-name commands.

---

## 8. Stats / config / reminders (wording posture)

- Stats: human Russian counts; epoch display **05.08.2026** (Europe/Moscow); authoritative table `LEADS`; events in `LEAD_EVENTS`.
- Config (Admin): contour; stats start date; source display; parser version; template standard version; personalization version; **resolver version**; AI state; reminder state; reporting synchronization state; active recipient count. Unavailable → `не задано`. Never workbook IDs, Telegram IDs, credentials, raw CONFIG secrets.
- Reminder status: clearly show enabled/disabled; production **ON** since Phase 3H.3 (10:00 Europe/Moscow).
- **Phase 3H.4:** `/status` poll line uses scheduled heartbeat keys; production last-lead line uses `last_production_processed_*`; `/health` probe text must not imply poll heartbeat. See `OPERATIONAL-STATUS-TRUTH-CONTRACT-v1.md`.
- **Phase 3G.2.2:** `/config` must display the **live** parser version (source: `Parse Lead` stamp), not a stale cached CONFIG key; reporting-sync state must be stated honestly (e.g. «выключена») rather than omitted when no sync node is active. See `evidence/phase3g2-2/CONFIG-TRUTH-FORENSIC-v1.md` / `CONFIG-HUMAN-DISPLAY-v1.md`.

---

## 9. Related registry

- [USER-VISIBLE-TEXT-REGISTRY-v1.md](../implementation/USER-VISIBLE-TEXT-REGISTRY-v1.md)
- [REPLY-PROFILE-NUMBERING-v1.md](REPLY-PROFILE-NUMBERING-v1.md)
- [UNIFIED-REPLY-PROFILE-RESOLVER-v1.md](UNIFIED-REPLY-PROFILE-RESOLVER-v1.md) — Phase 3G.2.2
- Evidence: `evidence/phase3g2/TEXT-CONTRACT-COVERAGE-v1.md` (stub) · `evidence/phase3g2-2/CONFIG-HUMAN-DISPLAY-v1.md`
