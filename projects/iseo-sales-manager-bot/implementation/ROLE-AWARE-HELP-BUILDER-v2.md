# ROLE-AWARE HELP BUILDER v2

**Phase:** 3G.2 (+ 3G.2.1 silent-repair)  
**Status:** current help-template contract  
**Extends:** [ADMIN-HELP-BUILDER-v1.md](ADMIN-HELP-BUILDER-v1.md) (HTML/`cmdHtml` rules remain)  
**Parse mode:** HTML

---

## 1. Hard rules

1. **Explicit templates** for Admin and moderator — separate full `helpReply(role)` bodies.
2. **Never** substring-patch an existing help line to insert a command (defect class: Phase 3F.2.1 `/ai_on` corruption).
3. `cmdHtml('/command')` wraps **only** the slash token; placeholders (`&lt;номер&gt;`, `&lt;имя&gt;`) stay outside `<code>`.
4. Public/unauthorized paths keep short deny/help — do not leak Admin command inventory.
5. **Never ship a syntax-broken shared module splice** (defect class: Phase 3G.2 silent `/help` — orphan `}) {` after `startReply`). Validate Code-node parse before deploy.
6. If Admin help would exceed Telegram 4096, split deterministically into ≤3 parts (leads+profiles / reminders+system+AI / users+settings); current measured Admin help fits in one message (~2344).

---

## 2. Admin template — required sections (order)

1. Начало: `/start`, `/help`, `/my_status`
2. Контур / ИИ / здоровье: `/status`, `/health`, `/ai_status`, `/ai_on`, `/ai_off`, `/stats`, `/last_error`, `/config`
3. Лиды: `/leads`, `/lead_history`, `/pending_count`, `/pending_leads`, `/pending_leads_test`
4. Напоминания: `/reminder_status` + Admin-only config (`/reminder_on|off|time|timezone|min`) under **Только для администратора**
5. Доставка / модераторы: `/delivery_status`, `/delivery_users`, `/moderators`, `/moderator_pending`, add/remove/info
6. **Профили ответов клиентам (обязательная секция 3G.2):**
   - `/reply_profiles` — профили ответов клиентам
   - `/reply_profile &lt;номер&gt;` — профиль ответа по номеру
   - `/reply_name_set &lt;номер&gt; &lt;имя&gt;` — задать имя для клиента
   - `/reply_name_enable &lt;номер&gt;` — включить персональный ответ
   - `/reply_name_disable &lt;номер&gt;` — выключить персональный ответ
   - `/my_reply_profile` — мой профиль ответа
7. Footer notes: ИИ по умолчанию выключен; ответ клиенту автоматически не отправляется; напоминания выключены до явной активации.

Omit deferred `/test_lead`.

---

## 3. Moderator template — required shape

Include staff-safe lead ops:

- Card usage tip (copy reply; ✅ Обработано / 🚫 Спам; shared status)
- `/start`, `/help`, `/my_status`
- `/leads`, `/lead_history`, `/pending_count`, `/pending_leads`, `/reminder_status`
- **Profile commands:** only `/my_reply_profile` — мой профиль ответа клиенту

**Must not advertise:** `/config`, AI toggles, moderator-management, reminder configuration, `/reply_profiles`, `/reply_profile`, `/reply_name_set`, `/reply_name_enable`, `/reply_name_disable`, `/delivery_*` Admin diagnostics (unless separately chartered as staff-read — default: Admin-only).

---

## 4. Acceptance checks (Phase 3G.2)

| Check | Expect |
|-------|--------|
| Admin `/help` | Contains full reply-profile section with `<номер>` placeholders |
| Moderator `/help` | Contains `/my_reply_profile`; zero Admin profile mutation commands |
| No substring patch | `/ai_on` line intact; no glued tokens |
| Role branch | Separate templates, not one string with conditional inserts mid-line |

Evidence stubs: `evidence/phase3g2/ADMIN-HELP-ACCEPTANCE-v1.md`, `MODERATOR-HELP-ACCEPTANCE-v1.md`.

---

## 5. Related

- [TELEGRAM-TEXT-CONTRACT-v2.md](../architecture/TELEGRAM-TEXT-CONTRACT-v2.md)
- [TELEGRAM-COMMAND-REFERENCE-v1.md](../guides/TELEGRAM-COMMAND-REFERENCE-v1.md)
- [REPLY-PROFILE-ADMIN-COMMANDS-v2.md](REPLY-PROFILE-ADMIN-COMMANDS-v2.md)
