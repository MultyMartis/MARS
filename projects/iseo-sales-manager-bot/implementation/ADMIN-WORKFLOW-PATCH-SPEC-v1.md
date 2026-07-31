# ADMIN WORKFLOW PATCH SPEC v1

**Target workflow name:** `i-SEO Sales Manager - Admin.dev`  
**Phase:** 3A — specification only  
**Pattern source:** MetaBOT Admin sanitized baseline (see ADMIN-SOURCE-SELECTION-v1) — **not copied yet**  
**Forbidden:** operational Gmail lead processing; client messaging; OpenRouter except optional health probe when both AI ON and probe enabled

---

## 1. Target node list

Placeholders: `<TELEGRAM_CREDENTIAL>` · `<GOOGLE_SHEETS_CREDENTIAL>` · `<ADMIN_CHAT_ID>` · `<CLEAN_WORKBOOK_ID>`  
Sandbox: Telegram send may be disabled until synthetic admin chat approved.

| # | Stable name | Source | type (expected) | typeVersion | Responsibility | Input | Output | Error behavior | Side effects | Credential | Sandbox disabled | Connection targets |
|---|-------------|--------|-----------------|-------------|----------------|-------|--------|----------------|--------------|------------|------------------|-------------------|
| 1 | Telegram Trigger | **new**/adapt | `n8n-nodes-base.telegramTrigger` (or webhook) | 1.1 / 2.1 | Admin entry | update | message | ignore non-text | Telegram receive | `<TELEGRAM_CREDENTIAL>` | false | → Normalize Command |
| 2 | Normalize Command | **new** | `n8n-nodes-base.code` | 2 | `/cmd` lower, trim args, user_id | update | cmd object | → Admin Error Handler | none | — | false | → Read Authorization Config |
| 3 | Read Authorization Config | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | Read CONFIG keys | cmd | cmd+config | deny writes; reply unavailable | Sheets read | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Check User Authorization |
| 4 | Check User Authorization | **new** | `n8n-nodes-base.if` | 2.2 | Allowlist `admin_user_ids` | cmd+config | true/false | false → deny reply | none | — | false | true→Route Command; false→Safe Telegram Reply (deny) |
| 5 | Route Command | **new** | `n8n-nodes-base.switch` | 3.2 | Route 10 cmds + unknown | authorized | branch | unknown branch | none | — | false | → handlers 6–16 |
| 6 | Help | **new** | `n8n-nodes-base.code` | 2 | Static Russian help | — | text | → Error Handler | none | — | false | → Safe Telegram Reply |
| 7 | Status | **new** | `n8n-nodes-base.code` (+ Sheets if needed) | 2 | environment, AI, last_* ops | config | text | → Error Handler | Sheets read | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 8 | AI Status | **new** | `n8n-nodes-base.code` | 2 | ai_enabled, model, probe flag | config | text | → Error Handler | none | — | false | → Safe Telegram Reply |
| 9 | AI On | **new** | Sheets update + Code | 4.5+ / 2 | Set `ai_enabled=true` | config | confirm | → Error Handler | CONFIG write + audit | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Audit Config Change → Safe Telegram Reply |
| 10 | AI Off | **new** | Sheets update + Code | 4.5+ / 2 | Set `ai_enabled=false` | config | confirm | → Error Handler | CONFIG write + audit | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Audit Config Change → Safe Telegram Reply |
| 11 | Health | **new** | Code + bounded Sheets | 2 | HEALTHCHECK-CONTRACT | config | text | FAIL lines | read-only probes; optional admin ping | sheets/tg | probe nodes gated | → Safe Telegram Reply |
| 12 | Stats | **new** | Code + bounded Sheets | 2 | Windowed counts | config/arg | text | → Error Handler | Sheets read bounded | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 13 | Synthetic Test Lead | **new** | Code + Sheets | 2 | Fixture inject sandbox only | args | summary | refuse if prod | sandbox RAW/CLEAN write | `<GOOGLE_SHEETS_CREDENTIAL>` | **true** until approved | → Audit Config Change → Safe Telegram Reply |
| 14 | Last Error | **new** | Sheets read + Code | 4.5+ / 2 | Latest ERRORS row | — | text | empty → «нет ошибок» | Sheets read | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 15 | Config Summary | **new** | Code | 2 | Allowlisted non-secret keys; admins as count | config | text | → Error Handler | none | — | false | → Safe Telegram Reply |
| 16 | Unknown Command | **new** | `n8n-nodes-base.code` | 2 | Fixed Russian string | — | text | — | none | — | false | → Safe Telegram Reply |
| 17 | Audit Config Change | **new** | `n8n-nodes-base.googleSheets` | 4.5+ | LEAD_EVENTS admin_* | write cmds | same | warn | Sheets append | `<GOOGLE_SHEETS_CREDENTIAL>` | false | → Safe Telegram Reply |
| 18 | Safe Telegram Reply | pattern | `n8n-nodes-base.telegram` | 1.2 | Reply to admin user/chat | text | sent | → Admin Error Handler | Telegram send | `<TELEGRAM_CREDENTIAL>` | optional | (end / success) |
| 19 | Admin Error Handler | **new** | Code + ERRORS append + Telegram | 2 | Short Russian + error_code | any | reply | last resort | ERRORS write | sheets/tg | false | → Safe Telegram Reply |

Deny path from node 4 may jump directly to Safe Telegram Reply with `Доступ запрещён.` without Route Command.

---

## 2. Command router outcomes

| Command | Handler | Write? |
|---------|---------|--------|
| `/start` | Start | no |
| `/help` | Help | no |
| `/status` | Status | no |
| `/ai_status` | AI Status | no |
| `/ai_on` | AI On + Audit | yes |
| `/ai_off` | AI Off + Audit | yes |
| `/health` | Health | no (optional admin ping) |
| `/stats` | Stats | no |
| `/test_lead` | Synthetic Test Lead + Audit | sandbox write |
| `/last_error` | Last Error | no |
| `/config` | Config Summary | no |
| other | Unknown Command | no |

---

## 3. Explicit non-goals

- No Gmail fetch / label mutate.  
- No production unread lead processing.  
- No auto client reply.  
- No SEO locks / stop-all-flow.  
- No Execute Workflow to Operational unless later charter.

---

## 4. `/test_lead` policy

- Default fixture: unnamed Audit phone-only.  
- Optional arg: fixture id from TEST-HARNESS-SPEC.  
- Allowed when `environment=dev` or explicit test flag.  
- Prod: refuse unless `allow_prod_synthetic=true` (default false).

---

## 5. SAFE UNKNOWN

Telegram Trigger vs Webhook; shared bot with manager cards vs separate admin bot; exact Switch typeVersion on instance.

---

*Related: ADMIN-SOURCE-SELECTION-v1 · ADMIN-COMMAND-CONTRACT-v1 · HEALTHCHECK-CONTRACT-v1.*


## Phase 3B.4 patch notes

- Enable Telegram Trigger (`disabled=false`) for acceptance windows only; final active=false.
- Stats: Route → Read CLEAN for Stats → Stats (bounded SYNTHETIC_TEST).
- AI on/off: AI On/Off → Prepare Config Write → Apply CONFIG Write (appendOrUpdate) → Restore Reply → Capture → Safe Telegram Reply.
- Normalize Command accepts Telegram Trigger root updates and webhook `body` wrappers.


## Phase 3B.4.1 patch notes

- Keep Telegram Trigger `disabled=false` for future controlled acceptance windows; Admin final active=false.
- Normalize Command: trim, lowercase, strip `@bot`, map optional aliases to canonical commands; args excluded from privileged matching.

## Phase 3C.1 patch notes

- `/health` → Gmail Health Probe (bounded production incoming-label query) → Health formatter.
- Production wording: `Gmail: доступен, запрос выполнен` + `Найдено подходящих писем: N`.
- `/status` production lines: последний опрос Gmail / последний обработанный лид / последняя ошибка.
- `/last_error` stage vocabulary includes `gmail_read` / `schedule_trigger`.

## Phase 3B.5 patch notes

- Admin.dev may remain **active** after polish.
- Safe patch: deactivate → code-only PUT → reactivate; restore backup if Trigger registration fails.
- Operator UX: Moscow time render; Russian terminology; synthetic/production status separation.
- `/test_lead`: deferred reply; omit from `/help` until Operational synthetic entry is chartered.
- `/start` (Phase 3D.2): authorized greeting with dynamic contour + AI wording; unauthorized → `Доступ запрещён.`
- Phase 3D.2.1: all Telegram send nodes must set `additionalFields.appendAttribution=false`; Help/readiness advertise canonical commands only; no Admin update-id idempotency table (duplicate `/start` was harness overlap).
