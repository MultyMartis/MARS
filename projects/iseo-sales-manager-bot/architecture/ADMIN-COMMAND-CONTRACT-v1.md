# ADMIN COMMAND CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Workflow:** Admin.dev  
**Status:** documented command surface

---

## 1. Authorization

1. Resolve Telegram `user_id` from update.
2. Load `admin_user_ids` from CONFIG (`string_list`).
3. If CONFIG unreadable → deny writes; reply that config is unavailable.
4. If user not in list → short deny: `Доступ запрещён.`
5. Do not reveal other admin IDs.

---

## 1b. Optional aliases (normalize → canonical)

| Alias | Canonical |
|-------|-----------|
| `/aistatus` | `/ai_status` |
| `/lasterror` | `/last_error` |
| `/aion` | `/ai_on` |
| `/aioff` | `/ai_off` |
| `/foobarunknown` | `/foobar_unknown` |

Canonical forms remain the router contract. Do not replace canonical help text with aliases.

**Phase 3D.2.1:** readiness / Help / operator notices must advertise **only** canonical forms. Aliases remain accepted by Normalize Command but must not appear in operator-facing instruction lists.

## 2. Unknown command

Exact response:

```
Неизвестная команда. Используйте /help.
```

---

## 3. Command matrix (v1)

| Command | Mode | Effect | Response |
|---------|------|--------|----------|
| `/start` | read | Contour + AI mode greeting | Dynamic start panel |
| `/help` | read | List commands + short purpose | Static help |
| `/status` | read | environment, ai_enabled, last_success_at, last_processed_lead_id, last_error_at | Snapshot |
| `/ai_status` | read | ai_enabled, ai_model, health_ai_probe_enabled | AI snapshot |
| `/ai_on` | **write** | Set `ai_enabled=true`; audit event | Confirm ON + model |
| `/ai_off` | **write** | Set `ai_enabled=false`; audit | Confirm OFF |
| `/health` | read | Run healthcheck contract | Pass/fail lines |
| `/stats` | read | Rollup last N days (`stats_days_default` or arg) | Counts |
| `/test_lead` | write (sandbox) | Inject/run synthetic fixture — **no real Gmail** | Result summary |
| `/last_error` | read | Latest ERRORS row | Code + stage + time |
| `/config` | read | Allowlisted non-secret keys summary | Russian operator labels |
| `/leads` | read | Recent CLEAN leads (default 5; accepts `3`\|`5`\|`10`; rejects other counts) | Archive cards, read-only, no lifecycle buttons |

### Phase 3B.3 operator-facing `/config` shape

```
Сводка CONFIG
Контур: разработка
Режим ИИ: выключен
Версия парсера: sm-parser-v3.2
Версия сообщений: sm-msg-v2.1
Администраторов в allowlist: 1
Менеджеров с доступом к кнопкам: 2
(секреты и идентификаторы скрыты)
```

Do not expose raw key tokens such as `environment:`, `aienabled:`, `parserversion:` in operator replies.

### `/start` (Phase 3D.2 / 3D.2.1 / 3D.4)

**Admin** (`admin_user_ids`) authorized response shape:

```
Sales Manager Admin запущен.

Контур: рабочий
Режим ИИ: выключен

Используйте /help, чтобы посмотреть доступные команды.
```

**Manager only** (`manager_action_user_ids`, not admin) — Phase 3D.4 role-aware shape:

```
Sales Manager — менеджерский режим

Вы можете отмечать лиды кнопками под карточкой:
✅ Обработанным · 🚫 Спам

Карточки приходят в рабочий чат менеджеров.
Admin-команды (/status, /leads, …) вам недоступны.

/help — краткая памятка по работе с карточками.
```

- `production` → `рабочий`; otherwise → `разработка`
- `ai_enabled=true` → `включён`; else → `выключен`
- `/start@bot_username` normalizes to `/start`
- Unauthorized → `Доступ запрещён.` (no config leak)

### `/status` (Phase 3D.2.1)

Production snapshot must read authoritative CONFIG:

- `last_poll_success_at` → «Последний опрос Gmail»
- `last_lead_success_at` (fallback `last_success_at`) → «Последний обработанный лид»

Operational must write `last_lead_success_at` from **Telegram Result Gate** success context after Gmail finalize — not from the Gmail API stub alone.

### Failure behavior (all)

- Catch errors → reply short Russian failure + `error_code` if safe.
- Log ERRORS / LEAD_EVENTS.
- Never include credentials or stack traces.

### Audit logging

- Writes (`/ai_on`, `/ai_off`, `/test_lead`): mandatory `LEAD_EVENTS` (or `ADMIN_AUDIT`) with actor telegram id.
- Reads: optional debug; not required for v1.

---

## 4. Command details

### `/help`

**Admin path:** lists canonical commands with one-line Russian descriptions, including `/start` under «Начало». Omits deferred `/test_lead`. Mentions: AI default OFF; bot never writes to clients.

**Manager path (Phase 3D.4):** short памятка — card emoji meanings, copy blocks, processed/spam buttons, no Admin commands, contact operator on failure. Does **not** list `/status`, `/leads`, `/config`, or AI toggles.

### `/status`

Fields: `environment`, AI on/off, `last_success_at`, `last_processed_at`, `last_processed_lead_id`, `last_error_code`, workflow label `Operational.dev` freshness if known.

### `/ai_on` / `/ai_off`

- Idempotent.
- Update CONFIG `updated_at` / `updated_by`.
- Response confirms new state.
- Does not call OpenRouter.

### `/health`

See [HEALTHCHECK-CONTRACT-v1.md](HEALTHCHECK-CONTRACT-v1.md).

### `/stats`

Default window from CONFIG. Optional `/stats 30`. Sources: bounded CLEAN aggregate — **avoid full unbounded reads**.

**Phase 3D.1 production shape (business vs technical):**

```text
Статистика за N дней

Уникальных заявок: N
Новых: N
Повторных: N
Возможных повторов: N
Повторных обработок сообщений: N

Технических повторных попыток: N
Карточек доставлено: N
Ошибок обработки: N

Без ИИ: N
С ИИ: N
Использован шаблон: N
```

Unique identity = `gmail_message_id` || `source_message_id` || `lead_id`. Technical retries must not inflate unique business lead totals.

### `/last_error`

Error lifecycle (read-path): `open` | `resolved` | `controlled_test`.  
When no open production error:

```text
Активных рабочих ошибок нет.

Последняя устранённая ошибка:
<summary> · <stage> · <time>
```

Do not erase ERRORS history. `/status` must not present a stale timestamp alone as an active failure; authoritative lifecycle is `/last_error`.

### `/test_lead`

- Accepts optional fixture name: `/test_lead audit_named`.
- Default fixture: phone-only unnamed audit.
- Writes to **sandbox** RAW/CLEAN only when `environment=dev` **or** explicit `test_mode` key.
- If `environment=prod`: refuse unless separate `allow_prod_synthetic=true` (default false).
- Must not touch unread production Gmail labels.

### `/config`

Show: ai_enabled, ai_model, environment, message_format_version, reply_template_version, parser_version, health_ai_probe_enabled, stats_days_default.  
**Hide:** raw admin id list may be shown as count only (`admins: 3`) to reduce leak surface — operator choice; default **count only**.

---

## 5. Deferred from v1

| Command idea | Status |
|--------------|--------|
| `/set_status <lead> <status>` | Deferred — Sheets lifecycle enough |
| `/assign` | Deferred |
| `/broadcast` | Forbidden |
| `/stop-all-flow` (MetaBOT) | Not applicable / deferred |
| `/raw_replay` production Gmail | Forbidden without charter |
| Inline button callbacks | **Delivered Phase 3D.3** — see §7 |

---

## 6. Routing pattern (MetaBOT-aligned)

```
Trigger → Normalize (/cmd lower) → Auth → Switch → Handler → Telegram reply
                                      └ unknown → fixed string
```

Explicit unknown-command node — do not silent-drop.

---

## 7. Phase 3D.3 — callback routing, `/leads`, and allowlists

### 7.1 Callback routing (inline lead actions)

Inline lifecycle buttons on manager cards route through the **same Admin Telegram Trigger** as text commands (Trigger update types: `message` + `callback_query`; no separate webhook/workflow):

```
Admin Telegram Trigger → Normalize Command (detect callback_query vs text)
   → Read Authorization Config → Check Manager Action Authorization
        → Resolve Lead by Token → State Machine (pending→processed|spam)
             → Update CLEAN Lifecycle (Sheets) → Append LEAD_EVENTS Callback
                  → Edit Lead Card Message (clear keyboard) → Answer Callback Query
```

- Allowed transitions: `pending→processed`, `pending→spam`.
- Same action repeated on an already-applied lead: **idempotent** — answered, no duplicate Sheets mutation, no duplicate `LEAD_EVENTS` row.
- Cross transition after settle (`processed↔spam`): **conflict** — `LEAD_EVENTS` records the conflict attempt; **no** Sheets status change; answer explains the lead already has a different status.
- Unauthorized caller: **no** Sheets mutation, answer `Доступ запрещён.` (same deny wording as command path).
- On successful mutation the source card message is edited (keyboard cleared); if the edit call itself fails, the Sheets mutation is **kept** and an operator-facing notice path (`Callback Edit Result`) records the edit failure separately — the lifecycle change is not rolled back.

### 7.2 `/leads` command detail

- Default count: **5**. Accepted explicit counts: **exact tokens** `3`, `5`, `10` only (`/leads 03`, `/leads 1`, `/leads 7`, `/leads 10 extra` rejected). Invalid reply:

```
⚠️ Укажите количество: 3, 5 или 10.
Например: /leads 5
```

- Admin allowlist only (`admin_user_ids`) — not the manager-action allowlist.
- Returns **up to N distinct** recent CLEAN business leads as **separate Telegram archive cards** (one message per card + optional notice), newest first, ordinals `1 из N` … `N из N` after unique-lead selection. If fewer unique leads exist than requested, return the available count honestly with a notice.
- Cards are read-only: current lifecycle line (`🕓 Ожидает обработки` / `✅ Обработан` / `🚫 Спам`), copy-friendly fields, **no** inline lifecycle buttons.
- One bounded `lead_card_recovered` LEAD_EVENTS append per command (not per card).
- Synthetic / technical-retry-only rows excluded. Invalid Sheets contacts (`#ERROR!`, formula text, `UNKNOWN`, …) are omitted (optional corrupt-contact warning) — never shown as a phone/email.

### 7.2.1 Phase 3D.3.1 repair note

Pre-fix defect: `Capture Admin Reply` collapsed multi-item `/leads` output to `$input.first()`, so Telegram delivered only «карточка 1 из N». Fixed by passthrough of all items. See `evidence/phase3d31/`.

### 7.3 Manager vs admin allowlists

| CONFIG key | Purpose | Phase 3D.4 state |
|------------|---------|------------------|
| `admin_user_ids` | Text-command authorization (`/status`, `/leads`, `/ai_on`, …) | **1** — operator only (hash 3FBE21323E22BFC1) |
| `manager_action_user_ids` | Inline lead-action callback authorization; role-aware manager `/start`/`/help` | **2** — operator + Olya (hash E6714550214106BA); **no fallback** when populated |

Olya is enrolled in **`manager_action_user_ids` only** — not in `admin_user_ids`. She may use lifecycle buttons and receives manager `/start`/`/help`; she may **not** run Admin commands.

---

*Related: CONFIGURATION-MODEL-v1 · HEALTHCHECK-CONTRACT-v1 · TWO-WORKFLOW-ARCHITECTURE-v1 · TELEGRAM-UX-CONTRACT-v1 §8.*


### Phase 3B.4 stats shape

`/stats` returns bounded 7-day SYNTHETIC_TEST counts (not placeholder text). Runtime success appears on `/status` via CONFIG ops keys. `/last_error` maps `telegram_send` → «отправка карточки в Telegram».

### Phase 3B.5 operator-facing polish

- Timestamps in Telegram: `DD.MM.YYYY HH:mm МСК` (Europe/Moscow); UTC storage unchanged.
- Dev `/status`: тестовый успех/ошибка; no raw error codes; process on/off lines.
- `/ai_status` / `/ai_on` / `/ai_off`: Russian ИИ wording (see evidence/phase3b5).
- `/stats` filter note: dev «Учитываются только тестовые заявки.» / prod «Тестовые заявки исключены.»
- `/test_lead`: **deferred** — removed from `/help`; reply «Команда временно недоступна до запуска рабочего контура.»


---

## Phase 3D.5 — Public access + moderator registry

Authorization order:
1. Read ACCESS_CONTROL (SoT).
2. Bootstrap from `admin_user_ids` if no row (emergency).
3. Legacy `manager_action_user_ids` only if no ACCESS_CONTROL row.

Public commands: `/start`, `/help`.  
Staff-only denial: `Команда доступна только сотрудникам с рабочими правами.`  
Unknown: `Команда не найдена. Используйте /help.`  
Blocked: `Доступ к боту ограничен.`

Admin registry commands:
- `/moderators`
- `/moderator_pending`
- `/moderator_info <code>`
- `/moderator_add <code>`
- `/moderator_remove <code>`

Never display raw Telegram user IDs. Opaque codes only.


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.

## Phase 3D.5.2 — Guaranteed response + zero-item hazard

- Never let a Sheets read (empty or error) terminate routing with zero Telegram replies.
- Preserve command context across registry lookup (`chat_id` / `user_id` / `message_id` / `command`).
- One-response invariant for every text command.
- Admin bootstrap (`admin_user_ids`) is recovery-only for `/start` `/help` `/status` `/health` `/config` `/moderators` `/moderator_pending` when ACCESS_CONTROL is technically unreadable.
- Unknown command text: `Команда не найдена. Используйте /help.`
- Registry technical failure (non-bootstrap): `Сервис временно недоступен. Попробуйте позже.`
- Webhook ownership: exactly one active Telegram Trigger for the Sales Manager bot (Admin.dev).

## Phase 3D.6 — Personal status and role notifications
- `/my_status` is public and resolves only the caller through ACCESS_CONTROL by `telegram_user_id`.
- Explicit active Admin/moderator, pending, revoked and blocked states have separate safe replies; blocked callers may use only this status exception.
- Help exposes `/my_status` to public, moderator and Admin with HTML `<code>` formatting.
- A non-idempotent `/moderator_add` or `/moderator_remove` mutates ACCESS_CONTROL first, then sends the canonical role notification.
- Notification delivery failure does not roll back the access mutation; Admin receives `Права изменены, но уведомление пользователю доставить не удалось.`
- Delivery audit events: `personal_status_viewed`, `moderator_grant_notification_sent/failed`, `moderator_revoke_notification_sent/failed`.
- Repeated add/remove sends no notification.
