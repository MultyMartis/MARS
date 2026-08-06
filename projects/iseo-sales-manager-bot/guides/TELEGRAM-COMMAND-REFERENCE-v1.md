# Telegram Command Reference v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3G.2.1 (silent `/help` `/start` `/config` repair on top of 3G.2 profiles + text contract)  
**Audience:** operators / Admin / moderators  
**Safety:** never paste Telegram user IDs, secrets, workbook IDs, emails, or phones into operator chat logs.

**Contour (current):** Operational.dev active (45 nodes) · Admin.dev active (**85**) · Sales-Manager-v2 inactive · AI OFF · reminders **ON** 10:00 Europe/Moscow · no auto-send to customers.

**Phase 3H.4:** `/reminder_status` Admin SyntaxError repaired; `/status` uses poll heartbeat + `last_production_processed_*`; `/health` Gmail probe ≠ poll heartbeat.

**Response contract:** recognized commands must never go silent — valid reply, permission/validation reply, or safe internal-error fallback.

---

## Legend

| Column | Meaning |
|--------|---------|
| **Who** | Who may run the command |
| **Mut** | `R` = read-only · `W` = mutates durable state |
| **Safety** | Operator notes |

Roles (Russian labels in bot UI): **Администратор** · **Модератор** · public / pending / revoked / blocked as status labels.

---

## 1. Public / personal

| Command | Who | Syntax | Example | Purpose | Mut | Safety |
|---------|-----|--------|---------|---------|-----|--------|
| `/start` | public+staff | `/start` | `/start` | Greeting; Admin AI/reminders; moderator shows approved reply name | R | Role-aware; no config leak to unauthorized |
| `/help` | public+staff | `/help` | `/help` | Role-aware help (explicit Admin vs moderator templates) | R | Never silent; rebuild templates only — never substring-patch |
| `/my_status` | public+staff (incl. blocked exception) | `/my_status` | `/my_status` | Personal ACCESS_CONTROL status for caller only | R | No other users’ data |

---

## 2. Admin runtime / AI / health

| Command | Who | Syntax | Example | Purpose | Mut | Safety |
|---------|-----|--------|---------|---------|-----|--------|
| `/status` | Admin | `/status` | `/status` | Environment, AI, last poll/lead success | R | Poll line = scheduled heartbeat; production lead = `last_production_processed_*` (3H.4) |
| `/health` | Admin | `/health` | `/health` | Healthcheck contract | R | On-demand probes; Gmail ≠ scheduled poll heartbeat (3H.4) |
| `/ai_status` | Admin | `/ai_status` | `/ai_status` | AI flags snapshot | R | Production stays OFF unless chartered |
| `/ai_on` | Admin | `/ai_on` | `/ai_on` | Enable AI flag | W | Does not call provider by itself; audit required; **do not enable casually** |
| `/ai_off` | Admin | `/ai_off` | `/ai_off` | Disable AI flag | W | Preferred production posture |
| `/stats` | Admin | `/stats [days]` | `/stats` · `/stats 30` | Bounded rollup from authoritative `LEADS` epoch **05.08.2026** Europe/Moscow | R | Business vs technical counts; no PII dumps |
| `/last_error` | Admin | `/last_error` | `/last_error` | Latest safe error summary | R | No stack/credentials |
| `/config` | Admin | `/config` | `/config` | Safe contour summary (epoch, source, versions, AI/reminders, reporting sync, recipients) | R | Never show API keys / IDs / workbook IDs; unavailable → `не задано` |

**Deferred / not advertised:** `/test_lead` (sandbox inject — omit from help until chartered).

---

## 3. Leads archive / history / pending / reminders

| Command | Who | Syntax | Example | Purpose | Mut | Safety |
|---------|-----|--------|---------|---------|-----|--------|
| `/leads` | Admin + active moderator | `/leads [3\|5\|10]` | `/leads 5` | Archive cards (no lifecycle buttons) | R | Invalid counts rejected |
| `/lead_history` | Admin + active moderator | `/lead_history <номер>` | `/lead_history 1` | Human event history for archive index | R | Human labels only (no raw event codes) |
| `/pending_count` | Admin + active moderator | `/pending_count` | `/pending_count` | Count pending business leads | R | Tests excluded from prod posture |
| `/pending_leads` | Admin + active moderator | `/pending_leads [page]` | `/pending_leads` | List pending (oldest-first) | R | Read-only view |
| `/pending_leads_test` | Admin | `/pending_leads_test` | `/pending_leads_test` | Pending view including test fixtures | R | Admin-only |
| `/reminder_status` | Admin + active moderator | `/reminder_status` | `/reminder_status` | Reminder engine status | R | Production: enabled=false |
| `/reminder_on` | Admin | `/reminder_on` | `/reminder_on` | Enable daily reminders | W | **Explicit operator activation only** |
| `/reminder_off` | Admin | `/reminder_off` | `/reminder_off` | Disable reminders | W | Safe default |
| `/reminder_time` | Admin | `/reminder_time HH:MM` | `/reminder_time 10:00` | Local send time | W | Europe/Moscow default TZ |
| `/reminder_timezone` | Admin | `/reminder_timezone <IANA>` | `/reminder_timezone Europe/Moscow` | Reminder TZ | W | Validate IANA |
| `/reminder_min` | Admin | `/reminder_min <n>` | `/reminder_min 1` | Minimum pending before send | W | Fail-closed if below min |

---

## 4. Delivery / moderators

| Command | Who | Syntax | Example | Purpose | Mut | Safety |
|---------|-----|--------|---------|---------|-----|--------|
| `/delivery_status` | Admin | `/delivery_status` | `/delivery_status` | Delivery health counts | R | No IDs / PII |
| `/delivery_users` | Admin | `/delivery_users` | `/delivery_users` | Eligible recipients summary | R | Names/roles only — no raw Telegram IDs |
| `/moderators` | Admin | `/moderators` | `/moderators` | Active moderators | R | Active-only |
| `/moderator_pending` | Admin | `/moderator_pending` | `/moderator_pending` | Pending + revoked former moderators (stable codes) | R | Opaque codes; no raw IDs |
| `/moderator_info` | Admin | `/moderator_info <code>` | `/moderator_info AB12` | Detail by opaque code | R | Code only |
| `/moderator_add` | Admin | `/moderator_add <code>` | `/moderator_add AB12` | Grant moderator | W | Access mutation ≠ reply-name mutation |
| `/moderator_remove` | Admin | `/moderator_remove <code>` | `/moderator_remove AB12` | Revoke moderator | W | Does not renumber reply profiles |

---

## 5. Reply profiles (Phase 3G.2 — number-based)

Stable address is **`reply_profile_number`** (immutable 1–4 for current seed). **Do not** address mutations by username, display name, Telegram ID, or row order.

| Command | Who | Syntax | Example | Purpose | Mut | Safety |
|---------|-----|--------|---------|---------|-----|--------|
| `/reply_profiles` | Admin | `/reply_profiles [page]` | `/reply_profiles` | List profiles by number | R | Shows display label + client name + flags |
| `/reply_profile` | Admin | `/reply_profile <N>` | `/reply_profile 3` | One profile card by number | R | Unknown N → point to list |
| `/reply_name_set` | Admin | `/reply_name_set <N> <имя>` | `/reply_name_set 3 Михаил` | Set client-facing first name | W | Validates name; **does not change access role/status**; does not auto-enable |
| `/reply_name_enable` | Admin | `/reply_name_enable <N>` | `/reply_name_enable 3` | Enable personalization | W | Requires valid name + active card recipient; revoked stay blocked |
| `/reply_name_disable` | Admin | `/reply_name_disable <N>` | `/reply_name_disable 3` | Disable personalization | W | Access unchanged |
| `/my_reply_profile` | Admin + moderator | `/my_reply_profile` | `/my_reply_profile` | Caller’s own profile | R | Moderators: **only** profile command in help |

**Moderator mutations** of reply names → deny: «Эта команда доступна только администратору.»

### Seeded numbers (sanitized evidence labels)

| № | Internal display (sanitized) | Client name | Enabled | Access | Label |
|---|------------------------------|-------------|---------|--------|-------|
| 1 | Андрей | Андрей | да | active | ADMIN_A |
| 2 | Ola4seo | Оля | нет | revoked | MOD_B_REVOKED |
| 3 | Мопс | Михаил | да | active | MOD_A |
| 4 | Никита | Никита | нет | revoked | MOD_C_REVOKED |

Client-facing text uses **only** `reply_sender_name` (never «Мопс», never Telegram username).

---

## 6. Inline lifecycle (not slash commands)

| Action | Who | Purpose | Mut | Safety |
|--------|-----|---------|-----|--------|
| ✅ Обработано | active Admin/moderator | Mark lead processed | W | Shared lifecycle; multi-copy sync |
| 🚫 Спам | active Admin/moderator | Mark spam | W | Same |
| Archive cards | `/leads` | No buttons | — | Intentional |

Callbacks: `sm:p:<token12>` / `sm:s:<token12>`. Immediate ack `Обрабатываю…`.

---

## 7. Unknown / deny

| Situation | Reply (Russian) |
|-----------|-----------------|
| Unknown command | `Команда не найдена. Используйте /help.` |
| Staff-only for non-staff | `Команда доступна только сотрудникам с рабочими правами.` |
| Unauthorized | `Доступ запрещён.` |
| Blocked (non-status) | `Доступ к боту ограничен.` |
| Registry technical failure | `Сервис временно недоступен. Попробуйте позже.` |

---

## Related

- [TELEGRAM-TEXT-CONTRACT-v2.md](../architecture/TELEGRAM-TEXT-CONTRACT-v2.md)
- [REPLY-PROFILE-NUMBERING-v1.md](../architecture/REPLY-PROFILE-NUMBERING-v1.md)
- [UNIFIED-REPLY-PROFILE-RESOLVER-v1.md](../architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md) — Phase 3G.2.2
- [REPLY-PROFILE-ADMIN-COMMANDS-v2.md](../implementation/REPLY-PROFILE-ADMIN-COMMANDS-v2.md)
- [ROLE-AWARE-HELP-BUILDER-v2.md](../implementation/ROLE-AWARE-HELP-BUILDER-v2.md)
- Evidence stubs: `evidence/phase3g2/` · `evidence/phase3g2-2/`

## Phase 3G.2.2 note

`/reply_profiles`, `/reply_profile <N>`, `/my_reply_profile`, and the `/start` reply-name line now auto-rehydrate a previously wiped row before responding — see `evidence/phase3g2-2/`. `/config` displays the live parser version and an added resolver-version line; reporting-sync state is shown honestly rather than omitted.

## Phase 3H.6

`/reminder_status` Admin long-form includes `Получателей:` from live ACCESS (fallback CONFIG cache). Expected production value: **4**.
