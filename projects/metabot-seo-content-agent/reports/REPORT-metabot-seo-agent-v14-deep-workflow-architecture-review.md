# REPORT — MetaBOT SEO Agent v14 Deep Workflow Architecture Review

**Date:** 2026-07-10  
**Classification:** READ-ONLY architecture review · LIVE_API_EXPORT evidence  
**Scope:** `SEO Content Agent Beta.v14` — Intake, Worker, Admin  
**Evidence pack:** `projects/metabot-seo-content-agent/exports/live-v14-evidence/2026-07-10/`  
**Reviewer:** Cursor agent (MARS lane B)

---

## 1. Executive Summary

MetaBOT SEO Agent v14 — это **трёхслойная внешняя n8n-система** (Intake / Worker / Admin) с Telegram как UX-шлюзом, Google Sheets как операционным state store и OpenRouter как LLM backend. Санитизированный live-export от **2026-07-10** подтверждает активные workflow:

| Workflow | ID | Nodes |
|----------|-----|-------|
| SEO Content Agent Beta.v14 - Intake | `x8EbTGKNdlBprLvk` | 20 |
| SEO Content Agent Beta.v14 - Worker | `p4mqb4VuPcemIDlC` | 91 |
| SEO Content Agent Beta.v14 - Admin | `AR6QxGt8ZKH0xG2T` | 15 |

**Ключевые выводы (evidence-backed):**

1. **Handoff Intake → Worker / Admin** — синхронный **HTTP POST** на n8n webhook (`Send To Worker`, `Send To Admin`); Worker принимает на path `seo-content-agent-worker`, Admin — `seo-content-agent-admin`. Это **не** executeWorkflow и **не** sheet-polling.
2. **Concurrency** — per-chat lock в листе `seo_active_jobs` с TTL **30 минут** (`expires_at`), статус `active`, `task_id` при создании = `pending`.
3. **Worker routing** — пять маршрутов: `local`, `single`, `run`, `get`, `reuse` (поле `route` в `Route Command`).
4. **Run pipeline** — многоэтапный конвейер: outline → strategy → text → cleanup/repair/score → seoqa → factcheck → format; с детерминированными JS-слоями (Content Score, Strict Risk Scanner, Table Sanity Check) и несколькими LLM-проходами.
5. **Memory** — лист `memory`; append после local/single/run; `/get` читает memory без lock; `reuse` подтягивает prior task и идёт в single-контур.
6. **Admin** — `/stop-all-flow` помечает active locks как `cancelled` в Sheets; **не** прерывает уже запущенные OpenRouter HTTP-вызовы.
7. **Документационный drift** — пакет `mega-map.md` / `OPERATIONAL-INDEX.md` всё ещё описывает **v13** и помечает handoff как SAFE UNKNOWN; v14 evidence закрывает часть пробелов, но полная parity docs ↔ live **не подтверждена**.

**Статус обзора:** COMPLETE для committed sanitized v14 evidence. Live runtime parity, модели по всем веткам, error branches и полная Sheets schema — частично SAFE UNKNOWN.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Staged changes | empty ✓ |
| Foreign WIP | preserved (unrelated `M` / `??` not touched) ✓ |
| Live API calls | none ✓ |
| Files modified | one new report only ✓ |

---

## 3. Source Evidence

### 3.1 Documentation pack (read)

- `OPERATIONAL-INDEX.md`, `README.md`, `workflow-map.md`, `mega-map.md`
- `lock-system.md`, `task-lifecycle.md`, `memory-and-task-reuse.md`
- `seoqa-and-factcheck.md`, `cleanup-rewrite-layer.md`
- `telegram-commands.md`, `admin-operations.md`, `known-issues.md`
- `metabot-developer/n8n-workflow-json-grammar-v1.md`
- `metabot-developer/n8n-node-type-catalog-v14.md`
- `metabot-developer/n8n-import-safe-generation-rules-v1.md`

### 3.2 Live v14 evidence (read)

- `EXPORT-MANIFEST.md`, `SANITIZATION-REPORT.md`, `WORKFLOW-MAP-v14.md`
- `NODE-INVENTORY-v14.md`, `PROMPT-AND-CODE-NODE-INDEX-v14.md`, `RISK-AND-UNKNOWN-REGISTER-v14.md`
- `SEO-Content-Agent-Beta-v14-Intake.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Worker.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Admin.sanitized.json`

### 3.3 Sanitization posture

- **SAFE_TO_COMMIT** per `SANITIZATION-REPORT.md`; operator review still required.
- Redacted: credentials, tokens, webhook URLs/IDs, sheet IDs, personal IDs, pinData.
- Residual **REVIEW_LABEL_ONLY** labels on all three workflows.

---

## 4. Current System Map

```
Telegram user (@seo_content_agent_bot — OPERATOR_CLARIFICATION)
        │
        ▼
┌───────────────────────────────────────────────────────────┐
│  INTAKE (Telegram Trigger)                                 │
│  Detect command → local | admin | retrieval | content+lock   │
└───────┬───────────────────────────────┬───────────────────┘
        │ HTTP POST worker_payload      │ HTTP POST admin body
        ▼                               ▼
┌───────────────────────┐       ┌───────────────────────┐
│  WORKER (Webhook)     │       │  ADMIN (Webhook)      │
│  seo-content-agent-   │       │  seo-content-agent-   │
│  worker               │       │  admin                │
│  Route → 5 branches   │       │  stop / locks / health│
└───────┬───────────────┘       └───────────┬───────────┘
        │                                   │
        ├──────── OpenRouter (chat/completions)
        ├──────── Google Sheets (seo_active_jobs, memory)
        └──────── Telegram (status + final output)
```

### 4.1 Triggers

| Workflow | Trigger node | Type |
|----------|--------------|------|
| Intake | Telegram Trigger | `telegramTrigger` |
| Worker | Webhook | POST `seo-content-agent-worker` |
| Admin | Webhook | POST `seo-content-agent-admin` |

### 4.2 Handoff (evidenced)

| From | To | Node | Mechanism |
|------|-----|------|-----------|
| Intake | Worker | `Send To Worker` | HTTP POST, body = `$json.worker_payload` |
| Intake | Admin | `Send To Admin` | HTTP POST, body with `message`, `admin_command`, chat/user ids |
| Worker | Telegram | multiple `Send Telegram *` / `Status *` | Bot API |
| Worker | Sheets | append/update nodes | Google Sheets API |
| Admin | Sheets | lookup/update | Google Sheets API |
| Admin | Telegram | `Send Admin Telegram`, `Send Stop All Flow Success` | Bot API |

### 4.3 State stores

| Store | Sheet name (evidenced) | Role |
|-------|------------------------|------|
| Active jobs / locks | `seo_active_jobs` (gid redacted) | Lock rows, health, admin cancel |
| Memory | `memory` | Task artifacts, get/reuse |
| Intake staticData | `global.seo_active_jobs` (legacy snapshot in export) | **Historical** — not Worker truth |

### 4.4 Quality subgraphs (Worker, run path)

`Outline → Strategy → Text → AutoFix/Polish → FAQ/Commercial → Cleanup → TextRepair → StrictCleanup → TableSanity → StrictRisk → ContentScore → SEO QA → Factcheck → Postcheck → Normalize → Format → Telegram`

---

## 5. Intake Workflow

**Nodes:** 20 · **Trigger:** Telegram Trigger only.

### 5.1 Command detection (`Detect Local Command`)

Parsed from Telegram `message.text`:

| Category | Commands | Intake branch |
|----------|----------|---------------|
| **local** | `/start`, unknown slash commands | `IF Local Command` → `Send Local Intake Message` (static `response_text`) |
| **admin** | `/help`, `/examples`, `/locks`, `/health`, `/stop-all-flow` | `IF Admin Command` → `Send To Admin` |
| **retrieval** | `/get task_id` only | `Route Retrieval Command` → `Lookup From Task` (memory sheet) |
| **content** | `/run`, `/outline`, `/text`, `/seoqa`, `/factcheck` (+ `from:` / `--from` for reuse) | Lock path → Worker |

**Important design note (code comment):** `--from` / `from:task_id` **не** идут через retrieval branch; это **новая** задача и проходят lock-ветку.

Flags parsed: `--strict`, `--from`, `from:`, `task_id:` variants.

### 5.2 Lock path (content commands)

```
Build User Lock Key
  → Lookup Active Locks (chat_id + status=active)
  → Check Active Lock (expires_at > now)
  → Debug Lock State
  → IF Busy
       true  → Send Busy Message
       false → Create Lock Row → Send Task Accepted → Build Worker Payload → Send To Worker
```

**Lock key:** `chat:{chat_id}:{timestamp}`  
**TTL:** `expires_at = now + 30 minutes`  
**Create Lock Row columns:** `lock_key`, `chat_id`, `user_id`, `username`, `first_name`, `last_name`, `task_id=pending`, `created_at`, `expires_at`, `status=active`

**Busy check:** active row for same `chat_id`, `status=active`, non-expired `expires_at`.

### 5.3 Retrieval path (`/get`)

```
Route Retrieval Command (get only)
  → Lookup From Task (memory, filter task_id)
  → IF From Task Exists
       true  → Build Worker Payload (lock=null)
       false → Send NOT-FOUND Message
```

### 5.4 Worker payload (`Build Worker Payload`)

```json
{
  "message": { ...telegram message... },
  "lock": { lock_key, chat_id, user_id, ... } | null,
  "status_message": { chat_id, message_id }
}
```

- `lock=null` for `/get` (retrieval-only).
- `status_message` carries Task Accepted message id for Worker status updates.

### 5.5 Telegram immediate responses

| Node | When |
|------|------|
| Send Local Intake Message | `/start`, unknown command |
| Send Busy Message | active lock |
| Send Task Accepted | lock created (mode-specific text for `/run`) |
| Send NOT-FOUND Message | `/get` task missing |

### 5.6 Risks / unknowns

| Item | Status |
|------|--------|
| HTTP failure after lock create | SAFE UNKNOWN — orphan lock risk |
| Worker webhook error handling | SAFE UNKNOWN |
| Whether `task_id` in lock row updates from `pending` | SAFE UNKNOWN in Intake export |
| Admin ACL (who can run admin commands) | SAFE UNKNOWN |

---

## 6. Worker Workflow

**Nodes:** 91 · **Trigger:** Webhook POST.

### 6.1 Entry chain

```
Webhook → Wait (3 units) → Store Worker Meta → Set Raw Input → Route Command → Switch Route
```

- **Wait:** likely debounce/race mitigation before processing (exact unit — n8n wait node `amount: 3`).
- **Store Worker Meta:** extracts lock, user, status_message from `body`.

### 6.2 Route model (`Route Command`)

Field **`route`** (not `route_type` in export):

| route | Condition |
|-------|-----------|
| `local` | invalid command, `/help`, `/start`, `/demo` |
| `get` | `/get` with valid command |
| `reuse` | `from_task_id` + mode ∈ {text, seoqa, factcheck} |
| `run` | `/run` |
| `single` | default for outline/text/seoqa/factcheck without run |

Also emits: `task_id` (`seo{timestamp}{rand}`), flags (`strict`, `no_factcheck`, `outline_only`, `text_only`, `tables_policy`), cleaned `task_input`.

### 6.3 Branch summaries

#### local
`Format Local Response` → `Send Telegram Local` + `Append Memory Local`

#### get
`Lookup Memory Get` → `Find Memory Get Row` → `Format Memory Get` → `Send Telegram Memory Get`  
Chunking: `splitMessage` max **3600** chars.

#### reuse
`Lookup Memory Reuse` → `Find Memory Reuse Row` → `Prepare Memory Reuse` → `Build Single Payload` → single OpenRouter path.

#### single
`Status Single` → `Build Single Payload` → `OpenRouter Single Mode` → optional `Run Single Text Repair` → format → memory → **Close Single Lock Before Sending** → Telegram.

#### run (full pipeline)
See §6.4.

### 6.4 Run pipeline order (evidenced chain)

1. **Status Outline** → Build Outline Payload → Run Outline → Extract
2. **Switch Run After Outline** — skip strategy if `outline_only`
3. **Status Strategy** → Build SEO Strategy Payload → Run SEO Strategy → Extract
4. **Status Text** → Build Text Payload → Run Text → Extract
5. **Auto Fix Text** → **Auto Polish Text** (code builds payload) → Run Auto Polish Text
6. **Ensure FAQ Text** → **Commercial Layer Text** → **Final Text Cleanup** → **Hard Final Cleanup**
7. **Build Text Repair Payload** → Run Text Repair → Extract → **Strict Cleanup** → **Table Sanity Check** → **Strict Risk Scanner** → **Compute Content Score**
8. **Switch Run After Text** — may short-circuit to format
9. **Status SEO QA** → Build SEOQA Payload → Run SEO QA → Extract
10. **Switch Run Factcheck** — skip if `no_factcheck`
11. **Status Factcheck** → Build Factcheck Payload → Run Factcheck → Extract → **Postcheck Strict Claims**
12. **Status Final** → Restore → **Normalize Run Output** → **Format Run Pipeline**
13. **Close Lock Before Sending** → **Parse Mode** → **Send Telegram Run** → **Finish Lock**
14. **Append Memory Run**

### 6.5 OpenRouter call structure

- **Endpoint:** `https://openrouter.ai/api/v1/chat/completions`
- **Auth:** `Authorization` header (redacted in export)
- **Body:** `JSON.stringify($json.openrouter_payload)` or `cleanup_payload`
- **Default model (evidenced):** `openai/gpt-4.1-mini` via `route.model || 'openai/gpt-4.1-mini'` in payload builders
- **Timeouts:** 120000 ms on HTTP nodes
- **JSON stages:** outline, strategy, text, seoqa, factcheck use `response_format: { type: 'json_object' }`; text repair returns raw markdown

### 6.6 Lock close paths

| Path | Node | Timing |
|------|------|--------|
| run | Close Lock Before Sending | Before Telegram send |
| run | Finish Lock | After send (via Restore Lock Context) |
| single | Close Single Lock Before Sending | Before final status + send |

**SAFE UNKNOWN:** exact update columns for close/finish nodes (redacted sheet mappings).

### 6.7 Failure / retry

No dedicated error-handler subgraphs visible in NODE-INVENTORY. **SAFE UNKNOWN** for retries, dead-letter, Telegram error replies.

---

## 7. Admin Workflow

**Nodes:** 15 · **Trigger:** Webhook POST `seo-content-agent-admin`.

### 7.1 Routing (`Route Stop All Flow` → `Route Locks` → `Route Health`)

| Command | Path |
|---------|------|
| `stop-all-flow` | Lookup Active Locks → Prepare Cancelled Locks → Cancel Active Locks → Send Stop All Flow Success |
| `locks` | Lookup Locks → Format Locks Response → Send Admin Telegram |
| `health` | Health Check Active Jobs → Health Check Memory → Format Health Response → Send Admin Telegram |
| `help`, `examples` | Build Admin Response → Send Admin Telegram |

### 7.2 Stop-all-flow semantics

`Prepare Cancelled Locks` sets per row:
- `status: cancelled`
- `finished_at: now`
- `cancel_reason: admin_stop_all_flow`

**Cannot stop:** in-flight Worker execution, active OpenRouter requests, already-queued n8n items.

### 7.3 Health check

Reads both `seo_active_jobs` and `memory`; `Format Health Response` inspects node outputs for errors / rate-limit messages.

### 7.4 Recovery strength

| Can do | Cannot do |
|--------|-----------|
| List active locks | Kill running LLM calls |
| Cancel lock rows in Sheets | Guarantee Worker stops mid-graph |
| Probe Sheets connectivity | Fix pending/job mismatch automatically |
| Send help/examples/locks text | **SAFE UNKNOWN** user-level ACL |

---

## 8. Task Lifecycle

```
1. Telegram command
2. Intake: classify (local / admin / get / content)
3a. local/admin → immediate Telegram or Admin webhook (no lock)
3b. get → memory lookup → Worker get branch OR not-found
3c. content → lock lookup → busy OR create lock (pending task_id)
4. Send Task Accepted + POST Worker
5. Worker: assign real task_id, route, execute pipeline
6. Status Telegram messages per stage (run path)
7. Quality layers + formatting
8. Close lock → Telegram delivery
9. Append memory (input/output truncated to 50k chars)
10. Finish lock / cancelled (admin)
```

### Reuse lifecycle

Prior `task_id` loaded from memory → new Worker `task_id` generated → single-mode LLM with restored context.

### Known inconsistency (docs + export staticData)

- Lock may close while `seo_active_jobs.task_id` still `pending` — aligns with `known-issues.md`.
- Intake `staticData.global.seo_active_jobs` shows legacy `task_id: pending` entry — operational drift signal.

---

## 9. Lock Model

| Aspect | Evidence |
|--------|----------|
| Granularity | **Per chat_id** |
| Key format | `chat:{chat_id}:{timestamp}` |
| Storage | `seo_active_jobs` sheet |
| Active lookup | `chat_id` + `status=active` + `expires_at > now` |
| Create | append row, TTL 30 min |
| Close (Worker) | update before send + Finish Lock |
| Close (single) | Close Single Lock Before Sending |
| Admin cancel | status → `cancelled` |
| Expired cleanup | **Not evidenced** as automated job |
| Stale lock risk | **High** — documented in known-issues |

---

## 10. Memory Model

| Aspect | Evidence |
|--------|----------|
| Sheet | `memory` |
| Append triggers | After local, single, run completions |
| Columns | `timestamp`, `task_id`, `mode`, `chat_id`, `user_id`, `username`, `first_name`, `last_name`, `input`, `output`, `chunk_count`, `status` |
| `/get` | Lookup by `task_id`, format output, chunk to Telegram |
| `reuse` | Lookup prior row, inject into `Build Single Payload` |
| Truncation | input/output sliced to 50000 chars |
| PII | User metadata stored — retention policy **SAFE UNKNOWN** |

---

## 11. Prompt Architecture

Prompts live in **Code nodes** (payload builders), not in standalone prompt files. Pattern: `openrouter_payload.messages[]` with `system` + `user` roles.

### 11.1 Prompt families

| Family | Builder node | OpenRouter node | Output | Temp (evidenced) |
|--------|--------------|-----------------|--------|------------------|
| **outline** | Build Outline Payload | Run Outline | JSON outline schema | 0.2 |
| **strategy** | Build SEO Strategy Payload | Run SEO Strategy | JSON SEO Strategy v10 | 0.15 |
| **text** | Build Text Payload | Run Text | JSON w/ content_markdown | 0.3 |
| **single** | Build Single Payload | OpenRouter Single Mode | JSON per mode | varies |
| **auto polish** | Auto Polish Text | Run Auto Polish Text | edited markdown | 0.15 |
| **text repair (run)** | Build Text Repair Payload | Run Text Repair | markdown | 0.05 |
| **text repair (single)** | Build Single Text Repair Payload | Run Single Text Repair | JSON cleanup | 0.15 |
| **SEO QA** | Build SEOQA Payload | Run SEO QA | JSON verdict/score | 0.03 |
| **factcheck** | Build Factcheck Payload | Run Factcheck | JSON verdict/claims | 0 |
| **SEO QA context** | — | — | Reads content_score, strict_risk_scan, table_sanity_check | — |

### 11.2 System prompt themes (summary)

- **Universal niche adaptation** — no hardcoded niche entities
- **Strict / SAFE CLAIMS** — forbidden promise patterns (рост, гарантии, влияет, помогает, …)
- **JSON-only** for structured stages; repair stages return markdown
- **Deterministic pre-checks** fed into SEO QA prompt (content_score, strict_risk_scan, table_sanity_check)
- **Separation:** factcheck ≠ SEO QA (different prompts and extractors)

### 11.3 Extraction nodes

`Run Extract Outline/Text/SEO QA/Factcheck`, `Extract SEO Strategy`, `Extract Auto Polish Text`, `Extract Text Repair`, `Extract Single Text Repair` — parse OpenRouter JSON, safe fallbacks on parse errors.

### 11.4 Quality risks

- Prompt duplication across single vs run vs repair
- Text Repair may reintroduce forbidden markers (documented known issue)
- Distributed strict policy across prompts + JS scanners — drift risk between branches

---

## 12. Code Node Architecture

### 12.1 Families

| Family | Examples | Workflows |
|--------|----------|-----------|
| **Command parsing** | Detect Local Command, Route Command | Intake, Worker |
| **Lock helpers** | Build User Lock Key, Check Active Lock, Restore Lock Context | Intake, Worker |
| **Payload builders** | Build * Payload (7 nodes) | Worker |
| **Response extractors** | Run Extract *, Extract * | Worker |
| **Formatters** | Format Run Pipeline (11.7k chars), Format Single Mode Message (9.7k), Normalize Run Output | Worker |
| **Memory builders** | Prepare Memory Row *, Prepare Memory Reuse, Find Memory * Row | Worker |
| **Deterministic QA** | Compute Content Score, Strict Risk Scanner, Table Sanity Check, Postcheck Strict Claims, Strict Cleanup | Worker |
| **Cleanup** | Auto Fix Text, Final/Hard Cleanup, Ensure FAQ, Commercial Layer | Worker |
| **Context restore** | Restore Route/Outline/Strategy/ContentScore/Postcheck/Format* | Worker |
| **Telegram chunking** | Parse Mode, splitMessage in Format Memory Get | Worker, Admin |
| **Admin formatters** | Build Admin Response, Format Locks/Health Response, Prepare Cancelled Locks | Admin |

### 12.2 Technical debt signals

- Large monolithic formatters (`Format Run Pipeline` ~11.7k chars)
- Many near-duplicate `Restore *` one-liners — graph complexity vs readability
- `safeNodeJson` pattern in Intake — defensive against unexecuted nodes
- Duplicate workflow bodies inside API export (`activeVersion` nesting) — import/generation hazard documented in grammar v1

### 12.3 Reusable patterns (for future MetaBOT Developer)

- Payload builder → HTTP → Extract trilogy
- Deterministic scanner → LLM QA with enforced verdict caps
- Lock close **before** Telegram send (single/run)
- `splitMessage(3600)` chunking convention

---

## 13. Quality Layers

| Layer | Position (run path) | Type | Protects against | Does NOT protect |
|-------|---------------------|------|------------------|------------------|
| **Auto Fix Text** | After text extract | Code | trivial fixes | semantic errors |
| **Auto Polish (LLM)** | Post text | LLM | grammar, template smell | factual hallucination |
| **Final / Hard Cleanup** | Pre repair | Code | formatting/markers | strict compliance alone |
| **Text Repair (LLM)** | Mid pipeline | LLM | grammar/strict markers | may reintroduce banned phrases |
| **Strict Cleanup** | Post repair | Code | strict markers | nuanced SEO issues |
| **Table Sanity Check** | Pre score | Code | broken tables | content quality |
| **Strict Risk Scanner** | Pre score | Code | risky claims lexicon | context-aware factcheck |
| **Content Score** | Pre SEO QA | Code | deterministic issues | narrative flow |
| **SEO QA** | Late | LLM | brief/outline alignment | external fact verification |
| **Factcheck** | Late | LLM | unsafe claims | SEO structure |
| **Postcheck Strict Claims** | After factcheck | Code | regex strict markers | — |
| **Operator review** | External | Human | final production sign-off | — |

### Failure modes (documented + structural)

- LLM JSON parse failures → safeParse fallback objects with `reject` verdicts
- Text Repair vs prior cleanup conflict
- `--no-factcheck` / `outline_only` / `text_only` flags short-circuit stages — behavior divergence
- Strict only when `--strict` flag set — not inherited by `/run` by default

---

## 14. Google Sheets Model

| Tab | Operations | Nodes |
|-----|------------|-------|
| **seo_active_jobs** | lookup, append, update | Intake, Worker, Admin |
| **memory** | lookup, append | Intake (get lookup), Worker |

### 14.1 seo_active_jobs columns (partial, evidenced)

`lock_key`, `chat_id`, `user_id`, `username`, `first_name`, `last_name`, `task_id`, `created_at`, `expires_at`, `status`, (`finished_at`, `cancel_reason` on admin cancel)

### 14.2 Bottlenecks

- Every lock check = Sheets read
- Health = multiple reads across tabs
- No transactions → race under concurrent commands
- Rate limits documented for `/health`

### 14.3 Schema gaps

- Full column list for memory beyond append mapping — **SAFE UNKNOWN**
- Whether `task_id` updated from `pending` to final id in jobs sheet — **SAFE UNKNOWN**
- Indexes / filtering performance — **SAFE UNKNOWN**

---

## 15. Telegram UX Model

### 15.1 Command surface (evidenced)

**User:** `/start`, `/run`, `/outline`, `/text`, `/seoqa`, `/factcheck`, `/get task_id`  
**Admin-routed:** `/help`, `/examples`, `/locks`, `/health`, `/stop-all-flow`  
**Flags:** `--strict`, `--no-factcheck`, `--outline-only`, `--text-only`, `--tables yes|no|auto`, `--from`, `from:`

### 15.2 Feedback pattern

| Phase | UX |
|-------|-----|
| Immediate | local text, busy, task accepted, not-found |
| Progress (run) | Status Outline/Strategy/Text/SEO QA/Factcheck/Final/Complete |
| Final | Chunked Telegram messages (3600), ParseMode sanitization |
| get | Memory formatted output or explicit not-found guidance |

### 15.3 UX bottlenecks

- Long run = many status messages + large chunked output
- Silent `/get` failures (known issue) — no error branch evidenced
- No consistent "running" indicator tied to Sheets state
- HTML parse_mode on some Intake messages; Worker strips `_`, `` ` ``, `*` for safety

---

## 16. Architecture Strengths

1. **Clear three-workflow separation** — gateway vs compute vs ops.
2. **Webhook handoff** — simple, inspectable, scales with n8n activation model.
3. **Per-chat locking with TTL** — prevents concurrent conflicting runs per chat.
4. **Layered quality** — deterministic + LLM checks before delivery.
5. **Memory + reuse** — operational continuity for SEO team workflows.
6. **Explicit route switch** — five modes with documented conditions.
7. **Admin stop/locks/health** — minimal ops surface without touching Worker graph.
8. **MetaBOT Developer alignment** — v14 export enabled grammar + node catalog docs.
9. **Sanitized evidence in-repo** — closes major documentation gap from OPERATIONAL-INDEX work line 1.

---

## 17. Architecture Bottlenecks

1. **Google Sheets as SoT** — quota, latency, non-atomicity.
2. **Worker graph size** — 91 nodes, 50+ Code nodes, high cognitive load.
3. **Synchronous handoff** — Intake HTTP POST to Worker without evidenced queue/retry.
4. **No physical cancellation** — admin cancel is sheet-level only.
5. **Lock/job desync** — `pending` task_id vs closed lock.
6. **Distributed strict policy** — prompts + multiple JS scanners.
7. **Large formatter nodes** — change risk, test difficulty.
8. **Documentation drift** — v13 narrative vs v14 live names.
9. **Model coupling** — default `openai/gpt-4.1-mini` embedded in code nodes.
10. **Evidence gaps** — error branches, ACL, full schema, live URL parity.

---

## 18. Improvement Opportunity Register

| ID | Title | Class | Evidence | Why it matters | Study before action | Priority |
|----|-------|-------|----------|----------------|---------------------|----------|
| O1 | Sheets rate limit mitigation | OPS_RELIABILITY | known-issues, health nodes | System-wide slowdown | Quota metrics, read caching patterns | High |
| O2 | Stale lock / pending cleanup | OPS_RELIABILITY | known-issues, lock TTL | Users blocked, false busy | Operator logs, jobs sheet samples | High |
| O3 | `/get` silent failure | QUICK_FIX_CANDIDATE | known-issues, get branch | UX trust | Live execution traces | High |
| O4 | Text Repair reintroduces banned phrases | QUALITY_IMPROVEMENT | known-issues, repair nodes | Strict compliance | SEO team bad outputs | High |
| O5 | Centralize strict policy | QUALITY_IMPROVEMENT | distributed prompts/scanners | single vs run drift | Policy matrix from SEO team | Medium |
| O6 | Lock vs task_id sync | OPS_RELIABILITY | Create Lock `pending` | ops confusion | Live sheet update path | Medium |
| O7 | Worker error handling visibility | RESEARCH_REQUIRED | no error nodes in inventory | silent failures | n8n execution history | Medium |
| O8 | Admin ACL hardening | SECURITY_HARDENING | no ACL in export | anyone with bot access? | Operator Telegram allowlist | Medium |
| O9 | Documentation v14 sync | QUICK_FIX_CANDIDATE | mega-map v13 | planning errors | Doc owner review | Medium |
| O10 | MIG-lite research layer | MIG_PATTERN_CANDIDATE | OPERATIONAL-INDEX PLANNED | keyword/competitor gap | MIG reports, SEO charter | Low (research) |
| O11 | Model strategy per stage | RESEARCH_REQUIRED | single default model | cost/quality tradeoff | OpenRouter usage data | Medium |
| O12 | Formatter node decomposition | RESEARCH_REQUIRED | 11k+ char nodes | maintainability | Change frequency | Low |
| O13 | Physical cancellation | SAFE_UNKNOWN | known limitation | stop-all semantics | n8n capability study | Low |
| O14 | Wordstat / keyword API | SAFE_UNKNOWN | OPERATIONAL-INDEX | future acquisition | Product charter | Low |
| O15 | SEO team quality rubric | SEO_TEAM_FEEDBACK_REQUIRED | qa prompts | calibrate strict mode | Good/bad output corpus | High |

---

## 19. Questions for Operator / SEO Team

### Operator

1. Подтвердите production webhook URLs для Worker/Admin и совпадают ли они с redacted export?
2. Обновляется ли `task_id` в `seo_active_jobs` с `pending` на финальный `seo{timestamp}`?
3. Есть ли Telegram allowlist для admin-команд или доступен любой пользователь бота?
4. Какой фактический TTL busy-lock и есть ли cron/cleaner для expired rows?
5. Что происходит при HTTP ошибке `Send To Worker` после `Create Lock Row`?
6. Запущен ли в production **только** v14 Beta или параллельно v13?
7. Какие OpenRouter модели используются по стадиям в live (override `route.model`)?
8. Есть ли мониторинг Sheets quota и alerting?

### SEO specialists

1. Какие формулировки strict-режима всё ещё проходят в production?
2. Достаточно ли разделения `/run` vs явного `/seoqa --strict from:`?
3. Какие поля outline/strategy критичны в вашем ТЗ-шаблоне?
4. Нужны ли таблицы по умолчанию (`tables_policy=auto`) — типичные кейсы?
5. Примеры удачных/неудачных `/get` и `/reuse` сценариев?
6. Приемлем ли default model `gpt-4.1-mini` для text vs outline?

### Future research / external

1. MIG-lite: какие acquisition шаги должны предшествовать `/outline`?
2. Wordstat/Yandex API — в charter или out of scope?
3. ORCA — нужен ли interpretation lane для writer evolution?

### n8n live verification

1. Error workflow settings per workflow?
2. Execution timeout limits for 120s OpenRouter calls × many stages?
3. Wait node unit (3 seconds?) — зачем debounce?

### Google Sheets schema owner

1. Canonical schema doc for `seo_active_jobs` and `memory`?
2. Row growth / archival policy?

---

## 20. What Must Not Be Changed Yet

Until further evidence + operator charter:

- Live n8n workflows (Intake / Worker / Admin)
- Prompt text in payload builders
- Lock schema and TTL semantics
- Google Sheets tab/column layout
- Webhook paths (`seo-content-agent-worker`, `seo-content-agent-admin`)
- Full Worker graph refactor
- MIG integration / ORCA integration
- Wordstat API wiring
- Admin stop-all-flow semantics (without ops runbook)
- Sanitized evidence files in `exports/live-v14-evidence/`

---

## 21. SAFE UNKNOWN

| Topic | Notes |
|-------|-------|
| n8n server version | Not in export JSON |
| Production webhook base URLs | Redacted |
| Full OpenRouter model map per stage | Only default evidenced |
| Error / retry subgraphs | Not in node inventory |
| Worker physical stop on admin cancel | Not possible by design |
| `task_id` promotion in jobs sheet | Not traced in export |
| Telegram bot ACL | Not in repo |
| Execution frequency of known issues | No metrics |
| Whether File Export workflow exists | PLANNED only |
| Intake `staticData.seo_active_jobs` vs Sheets authority | Conflicting signals |
| Chunk merge order for multi-chunk outputs | Partial evidence |
| pinData operational use | Redacted |

---

## 22. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md` | **Created** (this report) |

No other files created or modified.

---

## 23. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** unchanged (e.g. `projects/mars-website-factory/...`, `workspaces/fp-0002-*`, `.recovery-temp/`)
- **Commit / push:** not performed (per task charter)

---

## 24. Final Status

**COMPLETE** — deep architecture review completed against committed sanitized live v14 evidence.

Residual shallow areas (error handling, ACL, full Sheets schema, live URL verification) are explicitly marked SAFE UNKNOWN and listed in §19 for operator follow-up.

---

Awaiting operator review.
