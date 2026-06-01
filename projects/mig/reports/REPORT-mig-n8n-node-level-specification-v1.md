# REPORT — MIG n8n Node-Level Specification v1

**Status:** Specification only — no workflow JSON, no n8n import, no deployment.  
**Source of truth:** [REPORT-mig-runtime-design-metabot-patterns-v1.md](REPORT-mig-runtime-design-metabot-patterns-v1.md); MetaBOT v14 exports under `incoming/metabot/seo-writer-workflows/`; MIG spine `projects/mig/lib/session-spine/`; monolith reference `projects/mig/workflows/n8n/mig-research-session-v0.1.json`.  
**Date:** 2026-05-31  
**Lane:** A — MIG n8n Node-Level Specification

---

## Executive Summary

Спецификация описывает **точную последовательность n8n-узлов** для первого production-oriented семейства MIG workflow: **MIG Intake v0.1**, **MIG Worker v0.1**, **MIG Admin v0.1**. Связь — **Webhook → Webhook** (не `Execute Workflow`). Intake — единственная точка Telegram; Worker — исполнитель spine + артефакты; Admin — ops без pipeline.

Phase 1 Worker: маршруты `serp`, `get`, `status` (read-only); SERP через **fallback/manual/provider stub** из существующего spine; **без** live SERP API, competitors, landing, OpenRouter enrichment (только deterministic draft pack).

Документ готов для следующего шага: генерация/импорт n8n JSON по этим node maps.

---

## Telegram Command Surface

### Namespace

Все команды с префиксом **`/mig`**. Telegram передаёт полный текст сообщения; парсер Intake извлекает подкоманду после `/mig`.

**Синтаксис общий:** пробел после `/mig`, затем подкоманда; параметры — через пробел, `ключ=значение`, или флаги `--flag`.

### Routing matrix

| Command | Handler | Lock required? | Dispatch target |
|---------|---------|----------------|-----------------|
| `/mig` | Intake (local) | No | — |
| `/mig help` | Intake (local) | No | — |
| `/mig serp …` | Intake → Worker | Yes | Worker webhook |
| `/mig run …` | Intake → Worker | Yes | Worker (Phase 1: stub reply «Phase 2») |
| `/mig get …` | Intake → Worker | No | Worker (retrieval-only) |
| `/mig status` | Intake → Worker | No | Worker (retrieval-only) |
| `/mig cancel …` | Intake → Admin | No | Admin webhook |
| `/mig locks` | Intake → Admin | No | Admin webhook |
| `/mig health` | Intake → Admin | No | Admin webhook |
| `/mig stop-all` | Intake → Admin | No | Admin webhook |

### Exact syntax per command

#### `/mig` (no subcommand)

**Input:** `/mig`  
**Reply (Intake):** welcome + ссылка на `/mig help`.

#### `/mig help`

**Input:** `/mig help` или `/mig help serp` (optional topic — Phase 2)  
**Reply (Intake):** список команд Phase 1 (см. ниже).

#### `/mig serp` — Phase 1 primary route

**Minimal (defaults applied):**

```text
/mig serp ниша=аренда манипулятора город=Краснодар регион=Краснодарский край запросы="аренда манипулятора краснодар; кран манипулятор краснодар"
```

**Field parsing rules (Code node `Detect MIG Command`):**

| Token | Required | Default if omitted |
|-------|----------|-------------------|
| `ниша=` / `niche=` | Yes | — (validation error in Worker) |
| `регион=` / `region=` | Yes | — |
| `город=` / `city=` | No | `null` |
| `запросы=` / `queries=` / `seed_queries=` | Yes | — |
| `тип=` / `business_type=` | No | `local_service` |
| `поиск=` / `search_engine=` | No | `yandex` |
| `устройство=` / `device=` | No | `mobile` |

**Queries delimiter:** semicolon `;` inside quoted string, or comma if unquoted.  
**Flags:** `--strict`, `--from-session {session_id}` (Phase 2 resume).  
**Optional manual SERP (Phase 1):** reply to message with JSON attachment or inline `manual_serp=` — Worker only; Intake passes raw text in `task_raw`.

#### `/mig run` — Phase 2 placeholder in v0.1

```text
/mig run ниша=… регион=… запросы="…"
```

Phase 1: Intake dispatches to Worker; Worker route returns «`/mig run` — Phase 2, используйте `/mig serp`».

#### `/mig get`

```text
/mig get mig-20260531-a1b2c3
/mig get session_id=mig-20260531-a1b2c3
```

No lock. Retrieval-only envelope (`lock: null`).

#### `/mig status`

```text
/mig status
/mig status mig-20260531-a1b2c3
```

No args → last active session for `chat_id` from registry. With `session_id` → that session.

#### `/mig cancel`

```text
/mig cancel mig-20260531-a1b2c3
```

Intake → Admin. Admin sets lock `cancelled`, registry `status=cancelled`.

#### `/mig locks`, `/mig health`, `/mig stop-all`

```text
/mig locks
/mig health
/mig stop-all
```

Intake → Admin webhook with `admin_command` = subcommand name.

### Help text template (Intake local)

```text
MIG — Market Intelligence Gateway

/mig serp — SERP-сессия и draft Research Pack
  ниша=… регион=… [город=…] запросы="q1; q2"

/mig get {session_id} — сводка и путь к pack
/mig status [session_id] — текущий этап

/mig locks — активные locks (admin)
/mig health — проверка подсистем
/mig cancel {session_id} — отмена сессии
/mig stop-all — отмена всех active locks

/mig help — эта справка
```

---

## MIG Intake Node Spec

**Workflow name:** `MIG Intake v0.1`  
**Trigger:** Telegram Trigger (`message` updates only)  
**Outbound webhooks (design):**

- Worker: `POST {N8N_BASE_URL}/webhook/mig-worker`
- Admin: `POST {N8N_BASE_URL}/webhook/mig-admin`

**Env vars (design):** `MIG_WORKER_WEBHOOK_URL`, `MIG_ADMIN_WEBHOOK_URL`, `MIG_SPREADSHEET_ID`, `MIG_LOCK_TTL_MINUTES` (default 90).

### Node sequence (execution order)

| # | Node name | Node type | Purpose |
|---|-----------|-----------|---------|
| 1 | Telegram Trigger | `n8n-nodes-base.telegramTrigger` | Receive operator messages |
| 2 | Detect MIG Command | `n8n-nodes-base.code` | Parse `/mig` subcommand, flags, key=value fields |
| 3 | IF Not MIG Command | `n8n-nodes-base.if` | Ignore non-`/mig` messages (no reply) |
| 4 | Build User Lock Key | `n8n-nodes-base.code` | Extract chat_id, user_id, username; build lock_key |
| 5 | IF Local Command | `n8n-nodes-base.if` | Branch: start/help → local reply |
| 6 | Send Local Intake Message | `n8n-nodes-base.telegram` | Welcome / help text |
| 7 | IF Admin Command | `n8n-nodes-base.if` | Branch: locks/health/cancel/stop-all → Admin |
| 8 | Build Admin Payload | `n8n-nodes-base.code` | Admin envelope (no lock) |
| 9 | Send To Admin | `n8n-nodes-base.httpRequest` | POST Admin webhook; fire-and-forget |
| 10 | IF Retrieval Command | `n8n-nodes-base.if` | Branch: get/status → Worker without lock |
| 11 | Lookup Active Locks | `n8n-nodes-base.googleSheets` | Read `mig_active_sessions` (filter by chat_id in Code) |
| 12 | Check Active Lock | `n8n-nodes-base.code` | Determine is_busy, active_lock |
| 13 | IF Busy | `n8n-nodes-base.if` | Branch on is_busy |
| 14 | Send Busy Message | `n8n-nodes-base.telegram` | «⏳ У вас уже выполняется сессия…» |
| 15 | Create Lock Row | `n8n-nodes-base.googleSheets` | Append lock to `mig_active_sessions` |
| 16 | Send Task Accepted | `n8n-nodes-base.telegram` | Immediate ack; captures status_message |
| 17 | Build Worker Payload | `n8n-nodes-base.code` | Full envelope for Worker |
| 18 | Send To Worker | `n8n-nodes-base.httpRequest` | POST Worker webhook |
| 19 | IF Worker Dispatch Failed | `n8n-nodes-base.if` | HTTP error branch |
| 20 | Rollback Lock Row | `n8n-nodes-base.googleSheets` | Update lock status=cancelled, cancel_reason=dispatch_failed |
| 21 | Send Dispatch Error | `n8n-nodes-base.telegram` | «⚠️ Не удалось запустить сессию» |

**Retrieval path (get/status):** nodes 10 → 17 → 18 (skip 11–16 lock path; `lock: null` in payload).

**Admin path:** nodes 7 → 8 → 9 (skip lock entirely).

### Per-node detail

#### 1. Telegram Trigger

| Field | Value |
|-------|-------|
| **Input** | Telegram Bot API update |
| **Output** | `{ message: { text, chat, from, message_id, … } }` |
| **Error** | n8n retry; no custom handler |
| **Credential** | MIG Telegram bot (separate or shared — operator choice) |

#### 2. Detect MIG Command

| Field | Value |
|-------|-------|
| **Input** | `$json.message` |
| **Output** | `{ command, subcommand, task_raw, chat_id, user_id, username, first_name, last_name, session_id, flags[], scope: { niche, region, city, … }, seed_queries[], is_known, route: 'local'|'admin'|'worker'|'ignore' }` |
| **Expressions** | Match `^/mig(?:\\s+([a-z0-9_-]+))?` for subcommand; parse `ключ=значение` and quoted strings; map RU/EN keys |
| **Error** | Unknown `/mig foo` → `route=local`, command=unknown → node 6 sends help hint |

**Important:** subcommand `serp` sets `command=serp`, `needs_lock=true`. Subcommands `get`, `status` set `needs_lock=false`.

#### 4. Build User Lock Key

| Field | Value |
|-------|-------|
| **Input** | Detect output + Telegram message |
| **Output** | `{ chat_id, user_id, username, first_name, last_name, base_lock_key, lock_key }` |
| **Expressions** | `base_lock_key = mig:chat:{chatId}`; `lock_key = mig:chat:{chatId}:{Date.now()}` |
| **Pattern** | REUSE MetaBOT `Build User Lock Key` with `mig:` prefix |

#### 11. Lookup Active Locks

| Field | Value |
|-------|-------|
| **Input** | Build User Lock Key |
| **Operation** | Read rows from sheet `mig_active_sessions` |
| **Output** | All rows (filter in node 12) |
| **Error** | Fail closed → Send Sheets Error Telegram; do not dispatch Worker |

#### 12. Check Active Lock

| Field | Value |
|-------|-------|
| **Input** | Sheet rows + start context |
| **Output** | `{ is_busy, active_lock, active_session_id, lock_debug[] }` |
| **Logic** | REUSE MetaBOT: match `chat_id`, `status=active`, `expires_at > now` |
| **Error** | Treat empty sheet as not busy |

#### 15. Create Lock Row

| Field | Value |
|-------|-------|
| **Operation** | Append row |
| **Columns** | See Google Sheets section |
| **Values** | `session_id=pending`, `status=active`, `expires_at=now+TTL`, `command`, `scope` summary |
| **Error** | Fail closed; Telegram «Sheets недоступен»; no Worker dispatch |

#### 16. Send Task Accepted

| Field | Value |
|-------|-------|
| **Output** | Telegram message; capture `message_id` as status_message |
| **Text** | `✅ Сессия принята · ожидайте status…` (session_id assigned in Worker) |
| **parse_mode** | HTML |

#### 17. Build Worker Payload

| Field | Value |
|-------|-------|
| **Input** | Telegram, Build Lock, Detect, Send Task Accepted (for status_message) |
| **Output** | Envelope per Payload Contracts |
| **Logic** | REUSE MetaBOT `Build Worker Payload`; add `intake_parsed`; `lock=null` for get/status |

#### 18. Send To Worker

| Field | Value |
|-------|-------|
| **Method** | POST |
| **Body** | JSON from node 17 |
| **Options** | `neverError: false`; timeout 10s |
| **Error** | Route to rollback branch (nodes 19–21) |

---

## MIG Worker Node Spec

**Workflow name:** `MIG Worker v0.1`  
**Trigger:** Webhook `POST /webhook/mig-worker`  
**Response mode:** `responseNode` or immediate 200 for async (MetaBOT pattern: respond fast, work continues).

### Node sequence

| # | Node name | Node type | Purpose |
|---|-----------|-----------|---------|
| 1 | Webhook | `n8n-nodes-base.webhook` | Receive Intake envelope |
| 2 | Store Worker Meta | `n8n-nodes-base.code` | Extract lock, chat, status_message, operator |
| 3 | Route Command | `n8n-nodes-base.code` | Map command → mode: serp/get/status/run/local |
| 4 | Switch Route | `n8n-nodes-base.switch` | Branch by mode |
| **Route: local** | | | |
| 5a | Format Local Response | Code | Phase 1 stub for run |
| 6a | Send Telegram Local | Telegram | Reply to chat |
| **Route: get / status** | | | |
| 5b | Lookup Session Registry | Google Sheets | Read `mig_session_registry` |
| 6b | Load Manifest From FS | Code | Read `session_manifest.json` if folder_path known |
| 7b | Format Get Response | Code | Summary + pack pointer |
| 8b | Sanitize Telegram HTML | Code | REUSE MetaBOT `Parse Mode` pattern |
| 9b | Send Telegram Get | Telegram | Chunked if needed |
| **Route: serp (Phase 1 spine)** | | | |
| 5c | Assign Session ID | Code | If lock.session_id=pending → generate `mig-YYYYMMDD-xxxxxx` |
| 6c | Update Lock Session ID | Google Sheets | Update `mig_active_sessions.session_id` |
| 7c | Status Intake Validated | Telegram | editMessageText on status_message |
| 8c | Build Spine Intake Body | Code | Map intake_parsed → validateIntake body |
| 9c | Validate Intake | Code | REUSE `session-spine-n8n-snippets.validateIntake` |
| 10c | IF Validation Error | IF | Branch error path |
| 11c | Send Validation Error | Telegram | Explicit failure message |
| 12c | Create Manifest | Code | snippet `createManifest` |
| 13c | Create Session Folder | Code | snippet `createSessionFolder` |
| 14c | Status Collecting | Telegram | editMessageText |
| 15c | SERP Input | Code | snippet `serpInput` |
| 16c | Normalize SERP | Code | snippet `normalizeSerp` |
| 17c | Status Normalizing | Telegram | editMessageText |
| 18c | Research Pack Draft | Code | snippet `researchPackDraft` |
| 19c | Status Drafting | Telegram | editMessageText |
| 20c | Finalize Manifest | Code | snippet `finalizeManifest` (writes artifacts) |
| 21c | Append Session Registry | Google Sheets | Append/update `mig_session_registry` |
| 22c | Status Complete | Telegram | editMessageText «Ready for review» |
| 23c | Format Result Summary | Code | splitMessage, summary text |
| 24c | Sanitize Telegram HTML | Code | HTML escape |
| 25c | Send Telegram Result | Telegram | Chunk loop |
| 26c | Finish Lock | Google Sheets | Update lock `status=done`, `finished_at` |
| **Error path (shared)** | | | |
| E1 | Format Pipeline Error | Code | reason, session_id |
| E2 | Update Registry Failed | Google Sheets | `status=failed`, `error_message` |
| E3 | Status Failed | Telegram | editMessageText ✗ |
| E4 | Send Failure Notice | Telegram | «❌ Сессия остановлена…» |
| E5 | Finish Lock Failed | Google Sheets | `status=failed` or leave active for Admin |

### Key node details

#### 2. Store Worker Meta

| Field | Value |
|-------|-------|
| **Input** | Webhook body |
| **Output** | `{ worker_lock_key, worker_chat_id, worker_user_id, worker_username, status_chat_id, status_message_id, intake_parsed, message, lock }` |
| **Pattern** | REUSE MetaBOT `Store Worker Meta` |

#### 3. Route Command

| Field | Value |
|-------|-------|
| **Output** | `{ mode: 'serp'|'get'|'status'|'run'|'local', session_id, task_raw, … }` |
| **Mapping** | `serp→serp`, `get→get`, `status→status`, `run→run`, unknown→local |

#### 5c. Assign Session ID

| Field | Value |
|-------|-------|
| **Logic** | Use spine `generateSessionId()` — format `mig-YYYYMMDD-{6hex}` |
| **Output** | Propagate to lock update + spine body |

#### 8c. Build Spine Intake Body

| Field | Value |
|-------|-------|
| **Output** | Object matching `validate-intake.js` REQUIRED_FIELDS |
| **Mapping** | `operator_id` ← `user_id` or username; `seed_queries` from intake_parsed; optional `manual_serp`, `serp_provider_response` from payload extensions |

**Note:** spine generates its own session_id inside validateIntake — Worker node **must pass pre-assigned session_id** via spine extension (implementation task: add optional `session_id` override to validateIntake or set after validation in Worker Code).

#### 9c–20c. Session spine chain

| Field | Value |
|-------|-------|
| **Source** | `projects/mig/workflows/n8n/session-spine-n8n-snippets.js` |
| **Requires** | `MIG_LIB_ROOT`, `MIG_SESSION_ROOT`, n8n fs permissions |
| **Output terminal** | `{ status:'ok', session_id, folder_path, stage, serp_mode, files }` |
| **stage** | v0.1 spine: `draft_complete` (maps to lifecycle `draft_complete`) |

#### 21c. Append Session Registry

| Field | Value |
|-------|-------|
| **Operation** | Append or update by session_id |
| **continueOnFail** | true (FS is SoT) |
| **Columns** | See Sheets spec |

#### 26c. Finish Lock

| Field | Value |
|-------|-------|
| **Operation** | Update by `lock_key` |
| **Values** | `status=done`, `finished_at=now`, `session_id`, `stage=draft_complete` |
| **Pattern** | REUSE MetaBOT `Finish Lock` |

### Phase 1 exclusions (Worker)

- No OpenRouter HTTP nodes
- No competitor/landing sub-pipelines
- No `mig_session_memory` writes
- Live SERP API only if `serp_provider_response` supplied in payload (spine already supports)

---

## MIG Admin Node Spec

**Workflow name:** `MIG Admin v0.1`  
**Trigger:** Webhook `POST /webhook/mig-admin`

### Node sequence

| # | Node name | Node type | Purpose |
|---|-----------|-----------|---------|
| 1 | Webhook | webhook | Receive Admin envelope |
| 2 | Route Admin Command | switch | Branch by admin_command |
| **locks** | | | |
| 3a | Lookup Active Locks | Google Sheets | Read `mig_active_sessions` |
| 4a | Format Locks Response | Code | Filter active, non-expired |
| **health** | | | |
| 3b | Health Check Active Sessions | Google Sheets | Read tab |
| 3c | Health Check Registry | Google Sheets | Read tab |
| 3d | Health Check Session Root | Code | fs.access writable on MIG_SESSION_ROOT |
| 4b | Format Health Response | Code | Aggregate OK/DEGRADED/FAIL |
| **cancel** | | | |
| 3e | Lookup Session By ID | Google Sheets | registry + active locks |
| 4c | Prepare Cancel Row | Code | status=cancelled |
| 5c | Cancel Lock Row | Google Sheets | Update active lock |
| 6c | Cancel Registry Row | Google Sheets | Update registry |
| **stop-all** | | | |
| 3f | Lookup All Active Locks | Google Sheets | |
| 4d | Prepare Cancelled Locks | Code | REUSE MetaBOT stop-all |
| 5d | Cancel Active Locks | Google Sheets | Batch update |
| **send** | | | |
| 7 | Build Admin Response | Code | splitMessage chunks |
| 8 | Send Admin Telegram | Telegram | HTML reply to chat_id |

### Per-command operations

#### `/mig locks`

| Aspect | Spec |
|--------|------|
| **Input** | `{ admin_command: "locks", chat_id, user_id, username }` |
| **Sheets** | Read `mig_active_sessions`; filter `status=active` AND `expires_at > now` |
| **FS** | None |
| **Telegram** | List: lock_key, session_id, command, created_at, expires_at, stage |

#### `/mig health`

| Aspect | Spec |
|--------|------|
| **Input** | `{ admin_command: "health", … }` |
| **Sheets** | Probe read both tabs; `onError: continueRegularOutput` per sub-check |
| **FS** | `fs.access(MIG_SESSION_ROOT, W_OK)`; list newest session dir (optional) |
| **Telegram** | Structured report (see Error spec template) |

#### `/mig cancel {session_id}`

| Aspect | Spec |
|--------|------|
| **Input** | `{ admin_command: "cancel", session_id, … }` |
| **Sheets** | Update lock row matching session_id → `status=cancelled`, `cancel_reason=admin_cancel`; registry → `status=cancelled` |
| **FS** | Optional: write `{session_dir}/session.cancelled` flag file (Phase 1 optional; Sheets-only acceptable) |
| **Telegram** | «Сессия {id} отменена» or NOT FOUND |

#### `/mig stop-all`

| Aspect | Spec |
|--------|------|
| **Input** | `{ admin_command: "stop-all", … }` |
| **Sheets** | All active locks → cancelled (REUSE MetaBOT `stop-all-flow`) |
| **FS** | None |
| **Telegram** | Count of cancelled locks |

---

## Google Sheets Specification

**Document:** operator-configured (`MIG_SPREADSHEET_ID`). **Separate tabs from SEO** — never write to `seo_active_jobs` / `memory`.

### Tab: `mig_active_sessions`

**Role:** Concurrency locks (adapt MetaBOT `seo_active_jobs`).

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| lock_key | string | yes | PK for updates; `mig:chat:{chatId}:{ts}` |
| chat_id | string | yes | Telegram chat |
| user_id | string | yes | Telegram user |
| username | string | no | |
| first_name | string | no | |
| last_name | string | no | |
| session_id | string | yes | `pending` until Worker assigns |
| command | string | yes | serp, run, … |
| scope | string | no | JSON or summary: niche/region |
| status | string | yes | `active`, `done`, `failed`, `cancelled` |
| stage | string | no | Worker updates |
| created_at | ISO8601 | yes | |
| updated_at | ISO8601 | no | |
| expires_at | ISO8601 | yes | default +90 min |
| finished_at | ISO8601 | no | |
| cancel_reason | string | no | dispatch_failed, admin_cancel, … |
| error_message | string | no | |

### Tab: `mig_session_registry`

**Role:** Session index / history (adapt MetaBOT `memory` index, not full pack body).

| Column | Type | Required | Notes |
|--------|------|----------|-------|
| session_id | string | yes | PK |
| lock_key | string | no | originating lock |
| chat_id | string | yes | |
| user_id | string | yes | |
| username | string | no | |
| command | string | yes | |
| status | string | yes | `running`, `draft_complete`, `failed`, `cancelled` |
| stage | string | yes | lifecycle stage |
| pack_state | string | yes | `draft`, `review`, … |
| scope | string | no | JSON: niche, region, city, business_type |
| query_used | string | no | primary seed query |
| folder_path | string | yes | absolute session dir |
| serp_mode | string | no | fallback, manual, provider |
| created_at | ISO8601 | yes | |
| updated_at | ISO8601 | yes | |
| finished_at | ISO8601 | no | |
| expires_at | ISO8601 | no | lock TTL mirror |
| error_message | string | no | |

### Tab: `mig_session_memory` (optional Phase 2)

| Column | Type | Notes |
|--------|------|-------|
| timestamp | ISO8601 | |
| session_id | string | |
| chat_id | string | |
| input | string | ≤50000 chars task summary |
| output | string | ≤50000 chars result summary |
| chunk_count | string | |
| status | string | |

---

## Payload Contracts

Schema-level only. All objects JSON.

### Intake → Worker

```json
{
  "message": {
    "message_id": "number",
    "chat": { "id": "string|number" },
    "from": { "id": "number", "username": "string", "first_name": "string" },
    "text": "string",
    "date": "number"
  },
  "lock": {
    "lock_key": "string",
    "session_id": "string",
    "chat_id": "string",
    "user_id": "string",
    "username": "string",
    "status": "active",
    "expires_at": "ISO8601"
  },
  "status_message": {
    "chat_id": "string",
    "message_id": "number"
  },
  "intake_parsed": {
    "command": "serp|get|status|run",
    "session_id": "string|null",
    "flags": ["string"],
    "scope": {
      "niche": "string",
      "region": "string",
      "city": "string|null",
      "business_type": "string",
      "search_engine": "string",
      "device": "string"
    },
    "seed_queries": ["string"],
    "task_raw": "string",
    "manual_serp": "object|null",
    "serp_provider_response": "object|null"
  }
}
```

**Retrieval-only:** `"lock": null`, `"status_message": null` allowed for get/status.

### Intake → Admin

```json
{
  "message": { },
  "admin_command": "locks|health|cancel|stop-all",
  "session_id": "string|null",
  "chat_id": "string",
  "user_id": "string",
  "username": "string",
  "task_raw": "string"
}
```

### Worker → internal spine (validateIntake body)

```json
{
  "session_id": "string",
  "niche": "string",
  "region": "string",
  "city": "string|null",
  "business_type": "string",
  "seed_queries": ["string"],
  "search_engine": "string",
  "device": "string",
  "operator_id": "string",
  "manual_serp": "object|null",
  "serp_provider_response": "object|null"
}
```

**Spine success output:**

```json
{
  "status": "ok",
  "session_id": "string",
  "folder_path": "string",
  "stage": "draft_complete",
  "serp_mode": "fallback|manual|provider",
  "files": {
    "session_manifest": "string",
    "serp_result": "string",
    "research_pack_draft": "string"
  },
  "session_root": "string"
}
```

**Spine error output:**

```json
{
  "status": "error",
  "code": "VALIDATION_ERROR|SESSION_SPINE_ERROR",
  "message": "string",
  "details": ["string"] | null
}
```

### Worker → Telegram result

Internal formatted object (before Send):

```json
{
  "telegram_text": "string",
  "telegram_text_safe": "string",
  "chunk_count": "number",
  "chunks": ["string"],
  "session_id": "string",
  "folder_path": "string",
  "pack_state": "draft"
}
```

### Worker → Sheets registry row

```json
{
  "session_id": "string",
  "lock_key": "string",
  "chat_id": "string",
  "user_id": "string",
  "username": "string",
  "command": "serp",
  "status": "draft_complete",
  "stage": "draft_complete",
  "pack_state": "draft",
  "scope": "{\"niche\":\"…\",\"region\":\"…\"}",
  "query_used": "string",
  "folder_path": "string",
  "serp_mode": "fallback",
  "created_at": "ISO8601",
  "updated_at": "ISO8601",
  "finished_at": "ISO8601",
  "error_message": ""
}
```

---

## Filesystem Specification

### Env vars

| Variable | Purpose | Example (dev) | Example (VPS — recommended) |
|----------|---------|---------------|----------------------------|
| `MIG_SESSION_ROOT` | Session folders SoT | `C:\AI MARS\projects\mig\sessions` | `/var/lib/mig/sessions` |
| `MIG_LIB_ROOT` | Spine library path (Code nodes) | `C:\AI MARS\projects\mig\lib\session-spine` | `/opt/mig/lib/session-spine` |
| `MIG_SPREADSHEET_ID` | Google Sheet document ID | operator-set | same |
| `MIG_WORKER_WEBHOOK_URL` | Intake → Worker | `http://localhost:5678/webhook/mig-worker` | `https://n8n.ai-metacode.com/webhook/mig-worker` |
| `MIG_ADMIN_WEBHOOK_URL` | Intake → Admin | `http://localhost:5678/webhook/mig-admin` | `https://n8n.ai-metacode.com/webhook/mig-admin` |
| `MIG_LOCK_TTL_MINUTES` | Lock expiry | `90` | `90` |

**n8n host env (required for Code + fs):**

- `NODE_FUNCTION_ALLOW_BUILTIN=fs,path,crypto`
- `NODE_FUNCTION_ALLOW_EXTERNAL=*` (or scoped to spine path)
- `N8N_BLOCK_ENV_ACCESS_IN_NODE=false`

### Path strategy

```text
{MIG_SESSION_ROOT}/{session_id}/
  session_manifest.json
  serp_result.json
  research_pack.draft.md
  session.cancelled          ← optional Admin cancel flag
  safe_unknown.log           ← optional Phase 2
```

**session_id format (Phase 1 spine):** `mig-YYYYMMDD-{6hex}` — matches `session-manifest-v0.1.schema.json`.

### Permissions

| Environment | Owner | Permissions |
|-------------|-------|-------------|
| Local dev (Windows) | n8n process user | Read/write on `MIG_SESSION_ROOT` |
| VPS (Linux) | n8n service user (e.g. `n8n`) | `0750` on root dir; `0640` files; no world-readable if packs sensitive |

### What gets written (Phase 1 Worker `serp` route)

| File | Writer | When |
|------|--------|------|
| `session_manifest.json` | spine `writeArtifacts` | After finalize |
| `serp_result.json` | spine | After normalize |
| `research_pack.draft.md` | spine | After buildResearchPackDraft |
| Session directory | spine `mkdirSync` | Before writes |

Intake and Admin **do not** write FS in Phase 1.

---

## Error And Recovery Specification

| Failure | Detection | Operator UX | System action | Lock | Registry |
|---------|-----------|-------------|---------------|------|----------|
| **Validation failure** | spine `status=error`, code VALIDATION_ERROR | Telegram: «❌ Ошибка параметров: …» | No FS artifacts; no registry append | Finish `failed` or `cancelled` | optional row `failed` |
| **Busy lock** | Intake Check Active Lock | «⏳ У вас уже выполняется сессия `{session_id}`» | No Worker dispatch | unchanged | unchanged |
| **Sheets unreachable (Intake)** | Google Sheets node error | «⚠️ Реестр недоступен, сессия не запущена» | Fail closed; no dispatch | no create | — |
| **Worker dispatch HTTP fail** | HTTP 4xx/5xx/timeout | «⚠️ Не удалось запустить сессию» | **Rollback lock** → cancelled, reason=dispatch_failed | cancelled | — |
| **Worker pipeline failure** | spine error or uncaught exception | edit status ✗ + «❌ Сессия `{id}` остановлена: {reason}» | Partial FS may exist — do not mark draft_complete | `failed` | `status=failed`, error_message |
| **Filesystem write failure** | Code throw on write | Same as pipeline failure | stage not draft_complete | `failed` | `failed` |
| **Spine failure** | `{ status:'error', code, message }` | Explicit Telegram (MetaBOT gap fix) | No false success message | close failed | failed |
| **Telegram send failure** | Telegram node error | Log in n8n; optional retry once | Pipeline may complete; operator checks `/mig get` | still finish lock done | updated |
| **Sheets update failure (Worker)** | `continueOnFail` on registry/lock | FS SoT — session still usable via path | Log warning | attempt Finish Lock separately | may desync — Admin `/mig health` |

### Health report template (Admin)

```text
MIG Health
Sheets (locks): OK | FAIL — {reason}
Sheets (registry): OK | FAIL — {reason}
Session root: OK | FAIL — {path}, writable={bool}
Last session: {session_id} @ {created_at}
Active locks: {n}
OpenRouter: SKIP (Phase 1)
Overall: OK | DEGRADED | FAIL
```

### MetaBOT lessons applied

1. **Lock rollback on dispatch fail** — explicit in Intake (MetaBOT export unclear).
2. **Failure Telegram** — mandatory on Worker errors (MetaBOT silent-failure gap).
3. **Sheets non-blocking** — registry append `continueOnFail`; manifest wins on conflict.
4. **No inline API keys** — credentials only.

---

## Implementation Order

Exact build order for next Cursor task (small steps):

| Step | Deliverable | Validates |
|------|-------------|-----------|
| 1 | Create Google Sheet tabs + column headers per spec | Manual sheet inspection |
| 2 | Import **MIG Admin v0.1** skeleton (Webhook + health + locks) | curl POST `/webhook/mig-admin` |
| 3 | Import **MIG Worker v0.1** skeleton (Webhook + Route + get/status stubs) | curl POST with test envelope |
| 4 | Add Worker **serp route** — full spine chain from snippets | Match v0.1 monolith output |
| 5 | Import **MIG Intake v0.1** skeleton (Telegram + local help) | Bot responds /mig help |
| 6 | Wire Intake lock + dispatch to Worker/Admin | End-to-end Telegram serp |
| 7 | Local n8n import/test (localhost webhooks) | Full Phase 1 loop |
| 8 | Live n8n import/test (supervised, same host as MetaBOT) | Operator HITL sign-off |

**Do not** activate monolith `mig-research-session-v0.1` in parallel after cutover.

---

## What To Build First

1. **Google Sheets tabs** — zero code dependency; unblocks all workflows.
2. **Worker serp spine path** — reuses proven library; highest risk is fs path/env.
3. **Intake lock + dispatch** — UX-critical; depends on Sheets + Worker webhook URL.
4. **Admin health/locks** — ops safety net before live operator traffic.

---

## What To Delay

| Item | Phase |
|------|-------|
| OpenRouter enrichment nodes | 2+ |
| Live SERP provider HTTP | 2+ |
| `/mig run` full pipeline | 2+ |
| `/mig approve`, resume, history | 2+ |
| `mig_session_memory` tab | 2+ |
| MIG Export workflow | 4+ |
| ORCA consumption automation | 5+ |
| Expired-lock sweeper cron | 2+ (optional) |
| Dedicated Telegram bot vs shared | operator decision |

---

## SAFE UNKNOWN

- Dedicated MIG Telegram bot vs shared bot with `/mig` prefix.
- Production `MIG_SESSION_ROOT` on VPS (exact path, backup policy).
- Google Spreadsheet: new document vs new tabs in existing MetaBOT spreadsheet.
- Live n8n webhook IDs after import (`mig-worker`, `mig-admin` path confirmation).
- Whether Worker passes pre-assigned `session_id` into spine or spine continues to generate (requires small lib change).
- Admin ACL: who may run `/mig stop-all`.
- Phase 1 optional OpenRouter draft enrichment vs deterministic template-only pack.
- Auto cleanup of expired locks (TTL expiry without Worker finish).
- `session_id` in lock row: update timing Intake `pending` vs Worker assign (specified above; implementation detail).

---

## Recommended Next Step

**Operator decision gate (HITL):** confirm Telegram bot strategy, `MIG_SESSION_ROOT` on VPS, `MIG_SPREADSHEET_ID`, and webhook base URL.

Then next Cursor task:

> **Implement Step 1–4:** create Sheets tabs, export/import **MIG Worker v0.1** JSON with spine chain + **MIG Admin v0.1** skeleton JSON — still no production deploy until local curl tests pass.

---

## References

| Artifact | Path |
|----------|------|
| Runtime design | [REPORT-mig-runtime-design-metabot-patterns-v1.md](REPORT-mig-runtime-design-metabot-patterns-v1.md) |
| MetaBOT Intake | `incoming/metabot/seo-writer-workflows/SEO Content Agent Beta.v14 - Intake.json` |
| MetaBOT Worker | `incoming/metabot/seo-writer-workflows/SEO Content Agent Beta.v14 - Worker.json` |
| MetaBOT Admin | `incoming/metabot/seo-writer-workflows/SEO Content Agent Beta.v14 - Admin.json` |
| MIG monolith v0.1 | `projects/mig/workflows/n8n/mig-research-session-v0.1.json` |
| Spine snippets | `projects/mig/workflows/n8n/session-spine-n8n-snippets.js` |
| Env example | `projects/mig/config/env.example` |

---

*Specification only. No workflow JSON. No git commit.*
