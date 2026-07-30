# ADMIN COMMAND CONTRACT v1

**Product:** i-SEO Sales Manager Bot  
**Workflow:** Admin.dev  
**Status:** documented command surface

---

## 1. Authorization

1. Resolve Telegram `user_id` from update.
2. Load `admin_user_ids` from CONFIG (`string_list`).
3. If CONFIG unreadable → deny writes; reply that config is unavailable.
4. If user not in list → short deny: `Недостаточно прав.`
5. Do not reveal other admin IDs.

---

## 2. Unknown command

Exact response:

```
Неизвестная команда. Используйте /help.
```

---

## 3. Command matrix (v1)

| Command | Mode | Effect | Response |
|---------|------|--------|----------|
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

### Phase 3B.3 operator-facing `/config` shape

```
Сводка CONFIG
Контур: разработка
Режим ИИ: выключен
Версия парсера: sm-parser-v3
Версия сообщений: sm-msg-v1
Администраторов в allowlist: 1
(секреты и идентификаторы скрыты)
```

Do not expose raw key tokens such as `environment:`, `aienabled:`, `parserversion:` in operator replies.

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

Lists the ten commands above with one-line Russian descriptions. Mentions: AI default OFF; bot never writes to clients.

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

Default window from CONFIG. Optional `/stats 30`. Sources: `STATS_DAILY` and/or bounded CLEAN aggregate — **avoid full unbounded reads**.

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
| Inline button callbacks | Deferred |

---

## 6. Routing pattern (MetaBOT-aligned)

```
Trigger → Normalize (/cmd lower) → Auth → Switch → Handler → Telegram reply
                                      └ unknown → fixed string
```

Explicit unknown-command node — do not silent-drop.

---

*Related: CONFIGURATION-MODEL-v1 · HEALTHCHECK-CONTRACT-v1 · TWO-WORKFLOW-ARCHITECTURE-v1.*


### Phase 3B.4 stats shape

`/stats` returns bounded 7-day SYNTHETIC_TEST counts (not placeholder text). Runtime success appears on `/status` via CONFIG ops keys. `/last_error` maps `telegram_send` → «отправка карточки в Telegram».
