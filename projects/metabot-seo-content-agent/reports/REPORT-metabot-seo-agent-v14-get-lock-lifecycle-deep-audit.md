# REPORT — MetaBOT SEO Agent v14 /get and Lock Lifecycle Deep Audit

**Date:** 2026-07-10  
**Classification:** READ-ONLY deep audit · no live API calls · no workflow modifications  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Intake / Worker / Admin  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Evidence pack:** `exports/live-v14-evidence/2026-07-10/`  
**Issue matrix anchor:** commit `61bb6019`  
**Checkpoint commits verified:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`

**Constraints honored:** No live n8n / Telegram / OpenRouter / Sheets calls. No workflow modifications. No staging. No commit. Foreign WIP preserved.

---

## 1. Executive Summary

This audit reconstructs **exact node-level paths** for `/get`, `from:task_id` / reuse, and the **lock lifecycle** in v14 sanitized evidence, cross-checked against the deep architecture review (`84dd9b07`) and issue backlog (`61bb6019`).

| Area | Primary finding | Risk |
|------|-----------------|------|
| **`/get`** | Two-stage memory lookup (Intake `Lookup From Task` → Worker `Lookup Memory Get` + `Find Memory Get Row`); **no lock**; **no immediate Telegram ack** before Worker | Silent failure if Worker handoff or Telegram send fails |
| **`IF From Task Exists`** | Condition is `Boolean($json.task_id)` — **not** explicit memory-row match; behavior on empty lookup depends on Sheets `alwaysOutputData` passthrough | Medium — may route missing tasks to Worker instead of Intake `Send NOT-FOUND` |
| **Reuse** | Intake **lock path** (not retrieval); Worker `reuse` → single OpenRouter pipeline; missing source still proceeds with `MEMORY_LOOKUP_FAILED` prefix | Orphan lock + wasted LLM if source missing |
| **Lock lifecycle** | Per-`chat_id` lock in `seo_active_jobs`; TTL 30 min; `task_id=pending` at create; **only single path promotes `task_id`** in jobs sheet | `pending` desync on `/run`; stale `active` after expiry |
| **`/stop-all-flow`** | Sheets-only cancel for **requesting chat's** active locks; does not stop in-flight Worker/LLM | Misleading command name; cost continues |

**Evidence confidence:** High for node names, connections, and code-node logic from sanitized JSON. Medium for live runtime edge cases (Sheets empty-result passthrough, error branches). **SAFE UNKNOWN** for production ACL, full column schemas, and automated expiry cleanup.

**Final assessment:** Audit **complete** for committed evidence. Live trace validation still recommended for silent-failure reproduction.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Checkpoint `6263815c` | exists ✓ |
| Checkpoint `1b954990` | exists ✓ |
| Checkpoint `84dd9b07` | exists ✓ |
| Checkpoint `af6fc35d` | exists ✓ |
| Checkpoint `61bb6019` | exists ✓ |
| Staged changes | empty ✓ |
| Live API calls | none ✓ |
| Foreign WIP | preserved, not touched ✓ |

**Note:** `HEAD` (`61bb6019`) is ahead of `origin/mars/canonical-post-recovery` (`49ffdafe`). Per charter: no commit/push.

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Signal |
|-------------|--------|
| `projects/iseo-report-hub/` | not read |
| Smart Reporter docs | not read |
| Website Factory report demo | `M projects/mars-website-factory/...` — foreign WIP |
| WordPress report hub | `M workspaces/website-factory-operations/...` — foreign WIP |
| `workspaces/fp-0002-*` | foreign WIP |
| `projects/ocpilot/` | foreign WIP |
| `.recovery-temp/`, `.restore-test-temp/` | untracked foreign WIP |

---

## 4. Source Evidence

### 4.1 Governance and product docs (read)

| Source | Role |
|--------|------|
| `AGENTS.md`, `.cursorrules` | MARS boundaries, preflight |
| `README.md`, `OPERATIONAL-INDEX.md` | Product identity (v13 worker ref — drift) |
| `known-issues.md`, `telegram-commands.md` | `/get` silence, lock/job desync |
| `task-lifecycle.md`, `lock-system.md`, `memory-and-task-reuse.md` | Conceptual semantics |
| `admin-operations.md` | Ops duties |

### 4.2 v14 analysis (read)

| Source | Role |
|--------|------|
| `reports/REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md` | Synthesized I/W/A architecture |
| `reports/REPORT-metabot-seo-agent-vnext-lane-reanchor-and-plan.md` | B01–B18 backlog seed |
| `reports/REPORT-metabot-seo-agent-v14-issue-backlog-and-test-matrix.md` | IB-xx / TC-xx / TR-xx IDs |

### 4.3 MetaBOT Developer discipline (read)

| Source | Role |
|--------|------|
| `metabot-developer/n8n-workflow-json-grammar-v1.md` | JSON grammar |
| `metabot-developer/n8n-node-type-catalog-v14.md` | 126 nodes |
| `metabot-developer/n8n-import-safe-generation-rules-v1.md` | Import-safe rules |

### 4.4 Live v14 evidence (read + JSON parse)

| Source | Role |
|--------|------|
| `WORKFLOW-MAP-v14.md` | Node index (handoff auto-index stale — superseded by architecture review) |
| `NODE-INVENTORY-v14.md` | No dedicated error-handler nodes |
| `PROMPT-AND-CODE-NODE-INDEX-v14.md` | Code node sizes |
| `RISK-AND-UNKNOWN-REGISTER-v14.md` | Unknowns |
| `SEO-Content-Agent-Beta-v14-Intake.sanitized.json` | Intake graph + code |
| `SEO-Content-Agent-Beta-v14-Worker.sanitized.json` | Worker graph + code |
| `SEO-Content-Agent-Beta-v14-Admin.sanitized.json` | Admin graph + code |

### 4.5 Authority hierarchy

1. **Live n8n** — execution truth (not accessed)
2. **v14 sanitized export** — best repo graph evidence (**this audit's base**)
3. **v14 architecture review** — synthesized behavior
4. **mega-map / OPERATIONAL-INDEX (v13)** — semantics with drift risk

---

## 5. /get Path Audit

### 5.1 Intake detection

**Node:** `Detect Local Command` (Code)

| Step | Logic |
|------|-------|
| Command parse | `command = /^\/([a-zA-Z0-9_-]+)/` → lowercase |
| `/get` task_id | `task_id = /^\/get\s+([a-zA-Z0-9_-]+)/i` capture group 1 |
| Retrieval flag | `is_retrieval_command = (command === 'get')` |
| Design note (in-code) | `--from` / `from:task_id` **do not** use retrieval branch |

**Branch routing after detect:**

```
Telegram Trigger
  → Detect Local Command
  → IF Local Command
       true  → Send Local Intake Message
       false → IF Admin Command
                  true  → Send To Admin
                  false → Route Retrieval Command
                             true  → /get path
                             false → lock path (Build User Lock Key …)
```

### 5.2 Intake nodes involved (`/get`)

| Order | Node | Type | Role |
|-------|------|------|------|
| 1 | `Detect Local Command` | Code | Parse `/get task_id`, set `is_retrieval_command` |
| 2 | `IF Local Command` | IF | Bypass for `/start` / unknown |
| 3 | `IF Admin Command` | IF | Bypass admin commands |
| 4 | `Route Retrieval Command` | IF | `is_retrieval_command === true` |
| 5 | `Lookup From Task` | Google Sheets | Filter `memory.task_id` = Detect task_id; **`alwaysOutputData: true`** |
| 6 | `IF From Task Exists` | IF | `Boolean($json.task_id)` |
| 7a | `Build Worker Payload` | Code | `lock: null` for `/get` |
| 7b | `Send NOT-FOUND Message` | Telegram | Intake not-found (false branch) |
| 8 | `Send To Worker` | HTTP POST | Body = `$json.worker_payload` |

### 5.3 Does `/get` create a lock?

**No.** Evidence:

- Retrieval branch skips `Build User Lock Key` → `Create Lock Row`.
- `Build Worker Payload` sets `isRetrievalOnly = (command === 'get')` → `lock: null`.

### 5.4 Payload to Worker

**Node:** `Build Worker Payload`

```json
{
  "worker_payload": {
    "message": { "...telegram message..." },
    "lock": null,
    "status_message": {
      "chat_id": "<chat_id>",
      "message_id": null
    }
  }
}
```

**Handoff:** `Send To Worker` — HTTP POST, `jsonBody: $json.worker_payload`. Webhook path `seo-content-agent-worker` (redacted in export).

**No `Task Accepted` message** on `/get` path — user receives no immediate feedback until Worker responds.

### 5.5 Expected Worker payload fields

| Field | Source | Required for get |
|-------|--------|------------------|
| `body.message` | Telegram message | Yes — `Route Command` reads `task_raw` from message text |
| `body.lock` | null | Yes — no lock close on get path |
| `body.status_message` | chat_id + message_id | Optional — get path has no prior status message |

### 5.6 Worker routing to `get`

**Entry chain:**

```
Webhook → Wait (3) → Store Worker Meta → Set Raw Input → Route Command → Switch Route [output: get]
```

**Node:** `Route Command` (Code)

| Field | Value for `/get seoXXXX` |
|-------|--------------------------|
| `mode` | `get` |
| `from_task_id` | parsed from `/get` second token |
| `route` | `get` when `mode === 'get' && commandValid && !isDemo` |
| `task_id` | **new** `seo{timestamp}{rand}` generated (not the requested id) |

**Node:** `Switch Route` — output key `get` when `route === 'get'`

### 5.7 Worker memory lookup nodes

| Order | Node | Operation | Notes |
|-------|------|-----------|-------|
| 1 | `Lookup Memory Get` | Read `memory` sheet (full tab, **no filter in node**) | `continueOnFail: true` |
| 2 | `Find Memory Get Row` | Code filter: `row.task_id === route.from_task_id` | Sets `memory_found` |
| 3 | `Format Memory Get` | Code: build text + `splitMessage(3600)` | Handles not-found in-band |
| 4 | `Send Telegram Memory Get` | Telegram send per chunk | Strips `_`, `` ` ``, `*` |

### 5.8 When task exists

1. Intake: `Lookup From Task` finds row → `IF From Task Exists` true → `Send To Worker`
2. Worker: `Find Memory Get Row` → `memory_found: true` → `Format Memory Get` formats input/output
3. Telegram: chunked via `Send Telegram Memory Get`

### 5.9 When task is missing

**Intake path (false branch):**

- `IF From Task Exists` false → `Send NOT-FOUND Message`
- Text: `Task not found: {{ Detect Local Command.task_id }}` + memory guidance

**Caveat:** IF condition is `Boolean($json.task_id)` after lookup, **not** `memory_found`. With `Lookup From Task.alwaysOutputData=true`, if empty lookup **passthrough preserves parsed task_id**, false branch may **not** fire → Worker handles not-found instead.

**Worker path (always reachable if Intake sends):**

- `Format Memory Get` emits explicit `Task not found: {fromId}` when `!memory_found || !output`

### 5.10 When lookup fails (Sheets error)

| Location | Behavior | User impact |
|----------|----------|-------------|
| Intake `Lookup From Task` | No `continueOnFail` evidenced | **SAFE UNKNOWN** — may halt Intake execution |
| Worker `Lookup Memory Get` | `continueOnFail: true` | May pass error item; `Find Memory Get Row` likely sets `memory_found=false` → "Task not found" (misleading) or downstream crash |

### 5.11 Telegram outputs

| Stage | Node | When |
|-------|------|------|
| Intake | `Send NOT-FOUND Message` | IF false branch (missing/empty task_id after lookup) |
| Worker | `Send Telegram Memory Get` | Success, not-found, or missing-id messages from `Format Memory Get` |

**No** `Task Accepted`, **no** progress status messages on get path.

### 5.12 Silent failure points (ranked)

| # | Point | Mechanism | Evidence confidence |
|---|-------|-----------|---------------------|
| 1 | `Send To Worker` HTTP failure | No error branch; no Intake Telegram fallback; no lock path ack | **High** |
| 2 | Worker execution error before `Format Memory Get` | No error-handler subgraph in NODE-INVENTORY | **High** |
| 3 | `Send Telegram Memory Get` failure | No `continueOnFail`; no error Telegram | **High** |
| 4 | `Lookup Memory Get` returns 0 items (non-error) | `Find Memory Get Row` never runs | **Medium** |
| 5 | Intake `Lookup From Task` Sheets error | No continueOnFail | **Medium** |
| 6 | Full-sheet `Lookup Memory Get` timeout on large `memory` tab | Quota/timeout → continueOnFail path | **Medium** |
| 7 | User perception delay | No immediate ack — long Worker wait feels like silence | **High** (UX) |

### 5.13 Patch candidate nodes (later)

| Node | Workflow | Patch type |
|------|----------|------------|
| `IF From Task Exists` | Intake | Check `memory_found` or row `output` column, not parsed `task_id` |
| `Lookup From Task` | Intake | Add `continueOnFail` + error Telegram branch |
| `Send To Worker` | Intake | Error branch + user notice; optional retry |
| `Lookup Memory Get` | Worker | Filter by `task_id` in Sheets node; stop full-tab read |
| `Find Memory Get Row` | Worker | Guard when `items.length===0` — still emit format item |
| `Format Memory Get` | Worker | Distinct "lookup error" vs "not found" messages |
| `Send Telegram Memory Get` | Worker | Error branch / retry |
| New node | Intake | Immediate "⏳ retrieving…" ack for `/get` |

### 5.14 Tests without production changes

| Test ID | What to verify | Environment |
|---------|----------------|-------------|
| TC-I11 | `/get` existing task_id — full Intake→Worker trace | Sandbox clone or historical n8n execution replay |
| TC-I12 | `/get seoMISSING` — which branch sends not-found | Sandbox |
| TR-12 | Sheets failure on get lookup | Sandbox inject |
| TC-W04 | Worker `get` route direct webhook | Sandbox only |
| Code review | `IF From Task Exists` condition vs `alwaysOutputData` | Repo evidence (done) |

---

## 6. from:task_id / Reuse Path Audit

### 6.1 Detection

**Intake — `Detect Local Command`:**

| Pattern | Regex / logic |
|---------|---------------|
| `--from ID` | `/--from\s+([a-zA-Z0-9_-]+)/i` |
| `from:ID` | `/(?:^|\s)from\s*:\s*([a-zA-Z0-9_-]+)/i` |
| `task_id:ID` | `/(?:^|\s)task[_-]?id\s*:\s*([a-zA-Z0-9_-]+)/i` |

**Not** `is_retrieval_command` — reuse uses **content/lock branch**.

**Worker — `Route Command`:** same `fromTaskId` patterns + direct `/text|seoqa|factcheck ID` arg.

### 6.2 Intake branch: retrieval vs lock

| Command pattern | Branch |
|-----------------|--------|
| `/get task_id` | Retrieval (`Route Retrieval Command` true) |
| `/text from:ID`, `/seoqa from:ID`, etc. | **Lock path** (`Route Retrieval Command` false → `Build User Lock Key` …) |

### 6.3 Does reuse create a lock?

**Yes.** Same path as `/run`, `/text`, etc.:

```
Build User Lock Key → Lookup Active Locks → Check Active Lock → IF Busy
  → Create Lock Row (task_id=pending, status=active, TTL 30m)
  → Send Task Accepted → Build Worker Payload (lock object) → Send To Worker
```

### 6.4 Payload to Worker (reuse)

```json
{
  "worker_payload": {
    "message": { "...includes /text from:seoXXX ..." },
    "lock": {
      "lock_key": "chat:{chat_id}:{timestamp}",
      "chat_id", "user_id", "username", "first_name", "last_name"
    },
    "status_message": { "chat_id", "message_id" }
  }
}
```

### 6.5 Worker routing to `reuse`

**`Route Command` conditions:**

```
route = 'reuse' when:
  fromTaskId is set
  AND mode ∈ {text, seoqa, factcheck}
  AND commandValid
  AND !isDemo
```

**`Switch Route`** → output `reuse` → `Lookup Memory Reuse` → `Find Memory Reuse Row` → `Prepare Memory Reuse` → `Build Single Payload` → **single OpenRouter path** (same as `/text` single mode).

### 6.6 Memory lookup (reuse)

| Node | Behavior |
|------|----------|
| `Lookup Memory Reuse` | Read `memory` sheet; `continueOnFail: true` |
| `Find Memory Reuse Row` | Code match on `route.from_task_id` |
| `Prepare Memory Reuse` | Builds `task_input` with `MEMORY_FROM_TASK_ID` block or `MEMORY_LOOKUP_FAILED` prefix |

### 6.7 Source task exists

- `memory_found: true` → `task_input` includes stored input/output + current user addition
- Inherits `--strict` and tables policy from route flags and stored input
- New `task_id` generated in `Route Command`
- Pipeline: `Status Single` → OpenRouter → format → **`Close Single Lock Before Sending`** (promotes `task_id`) → Telegram → **`Append Memory Single`**

### 6.8 Source task missing

- `Prepare Memory Reuse` sets `task_input = "MEMORY_LOOKUP_FAILED\nTask not found: …"` but **still continues**
- No dedicated IF halt before `Build Single Payload`
- LLM runs on failure stub → user may get confusing output
- Lock still created at Intake → **orphan risk** if pipeline errors

### 6.9 Route after reuse

**Single-mode OpenRouter path** (not full `/run` pipeline):

`Build Single Payload` → `OpenRouter Single Mode` → optional `Run Single Text Repair` → `Format Single Mode Message` → memory append → lock close → Telegram.

### 6.10 Lock close (reuse)

**Node:** `Close Single Lock Before Sending`

| Field updated | Value |
|---------------|-------|
| `status` | `done` |
| `finished_at` | ISO now |
| `lock_key` | from `Store Worker Meta` |
| `task_id` | **`$('Route Command').first().json.task_id`** (promoted) |
| user metadata | username, user_id, first_name, last_name |

### 6.11 Memory append (reuse)

**Nodes:** `Prepare Memory Row Single` → `Append Memory Single` (`continueOnFail: true`)

Columns: `timestamp`, `task_id`, `mode`, `chat_id`, `input`, `output`, `chunk_count`, `status`, user fields. Input/output truncated to 50k in prepare nodes (per architecture review).

### 6.12 Failure points

| # | Point | Impact |
|---|-------|--------|
| 1 | Missing source not blocked | Wasted LLM + confusing output |
| 2 | Lock created before source validation | Orphan `active` lock on failure |
| 3 | `Lookup Memory Reuse` full-sheet read | Quota / latency |
| 4 | `continueOnFail` on append | User has Telegram output but `/get` later fails |
| 5 | User expects no new task_id | UX surprise (IB-16) |

### 6.13 Priority tests

| Test ID | Scenario |
|---------|----------|
| TC-I13–I15 | reuse valid source (text/seoqa/factcheck) |
| TC-I16 | `/text from:seoINVALID` — lock + error behavior |
| TC-W05 | Worker reuse direct webhook |
| TR-13 | reuse missing source — lock + Telegram |
| IB-16 | UX documentation for new task_id |

---

## 7. Lock Lifecycle Audit

### 7.1 Step-by-step register

| Step | Workflow | Node | Sheet | Fields | Confidence | Failure risk |
|------|----------|------|-------|--------|------------|--------------|
| **Lock key construction** | Intake | `Build User Lock Key` | — | `lock_key = chat:{chat_id}:{Date.now()}` | High | Low |
| **Active lock lookup** | Intake | `Lookup Active Locks` | `seo_active_jobs` | filter `chat_id` + `status=active` | High | Sheets quota / race |
| **TTL evaluation** | Intake | `Check Active Lock` | — | `expires_at > now`, `status===active` | High | **Expired rows with status=active not auto-cleaned** |
| **Busy decision** | Intake | `IF Busy` | — | `is_busy === 'true'` (string compare) | High | Stale lock → false busy |
| **Busy message** | Intake | `Send Busy Message` | — | static HTML text | High | Low |
| **Create lock row** | Intake | `Create Lock Row` | `seo_active_jobs` | append: `lock_key`, `chat_id`, `user_id`, `username`, `first_name`, `last_name`, `task_id=pending`, `created_at`, `expires_at=now+30m`, `status=active` | High | Orphan if Worker handoff fails |
| **Task accepted** | Intake | `Send Task Accepted` | — | mode-specific text for `/run` | High | Low |
| **Worker handoff** | Intake | `Send To Worker` | — | HTTP POST `worker_payload` | High | **Orphan lock, no compensation** |
| **Worker meta store** | Worker | `Store Worker Meta` | — | extracts `worker_lock_key`, status_message ids | High | Low |
| **Real task_id assignment** | Worker | `Route Command` | — | `task_id = seo{utcStamp}{rand}` | High | Not written to jobs sheet on run path |
| **Run: close before send** | Worker | `Close Lock Before Sending` | `seo_active_jobs` | update by `lock_key`: `status=done`, `finished_at` — **no task_id** | High | `pending` remains |
| **Run: telegram send** | Worker | `Send Telegram Run` | — | chunked output | High | Lock already `done` before send |
| **Run: finish lock** | Worker | `Finish Lock` | `seo_active_jobs` | duplicate `status=done`, `finished_at` | High | Redundant close |
| **Single/reuse: close** | Worker | `Close Single Lock Before Sending` | `seo_active_jobs` | `status=done`, `finished_at`, **`task_id` promoted** | High | Low |
| **Single: telegram** | Worker | `Send Telegram Single` | — | after lock close | High | User may get msg after lock closed |
| **Memory append** | Worker | `Append Memory Run/Single/Local` | `memory` | new row; `continueOnFail: true` | High | Silent memory loss |
| **Admin cancel** | Admin | `Cancel Active Locks` | `seo_active_jobs` | `status=cancelled`, `finished_at`, `cancel_reason=admin_stop_all_flow` | High | Does not stop Worker |
| **Health probe** | Admin | `Health Check Active Jobs` | `seo_active_jobs` | read; `alwaysOutputData: true` | High | Quota |

### 7.2 Status values (evidenced)

| status | Set by |
|--------|--------|
| `active` | `Create Lock Row` |
| `done` | `Close Lock Before Sending`, `Finish Lock`, `Close Single Lock Before Sending` |
| `cancelled` | Admin `Prepare Cancelled Locks` → `Cancel Active Locks` |

### 7.3 Orphan lock scenarios

1. `Create Lock Row` succeeds → `Send To Worker` fails (IB-04)
2. Worker OpenRouter/early crash after lock create — **no evidenced lock cleanup on error** (TR-05 SAFE UNKNOWN)
3. Admin cancel during run — sheet `cancelled` but Worker continues — new completion may still close lock as `done` (**race — SAFE UNKNOWN**)
4. Expired `active` row never transitioned — blocks chat until manual cleanup (IB-02)

### 7.4 task_id promotion summary

| Path | Jobs sheet `task_id` after success |
|------|-----------------------------------|
| **single** | Updated to real `seo…` id in `Close Single Lock Before Sending` |
| **reuse** | Same as single |
| **run** | **Stays `pending`** — close nodes do not map `task_id` |
| **get** | No lock row |

### 7.5 Cancellation path

- User: no `/cancel` command evidenced
- Admin: `/stop-all-flow` → per-chat active lock cancel in Sheets only
- Worker: no check for `cancelled` status mid-pipeline evidenced

### 7.6 Health / admin path

`/locks` → Admin `Lookup Locks` → `Format Locks Response` (filters `status=active` AND `expires_at > now`) → Telegram.

`/health` → `Health Check Active Jobs` + `Health Check Memory` → `Format Health Response`.

---

## 8. Admin /stop-all-flow Audit

### 8.1 Command reachability

```
Telegram → Intake: Detect Local Command (admin_command=stop-all-flow)
  → IF Admin Command true
  → Send To Admin (HTTP POST)
       body: { message, admin_command, chat_id, user_id, username }
  → Admin Webhook (seo-content-agent-admin)
```

### 8.2 Admin routing

```
Webhook → Route Stop All Flow (admin_command === 'stop-all-flow')
  true  → Lookup Active Locks → Prepare Cancelled Locks → Cancel Active Locks → Send Stop All Flow Success
  false → Route Locks → …
```

### 8.3 Google Sheets operation

| Node | Operation | Filter | Updates |
|------|-----------|--------|---------|
| `Lookup Active Locks` | read/lookup | `chat_id` = body.chat_id, `status=active` | — |
| `Prepare Cancelled Locks` | Code | — | `status=cancelled`, `finished_at`, `cancel_reason=admin_stop_all_flow` |
| `Cancel Active Locks` | update | match `lock_key` | per prepared row |

**Scope note:** Cancels **only the requesting chat's** active locks — not fleet-wide, despite command name.

### 8.4 Physical Worker stop?

**No.** Admin does not call Worker webhook, n8n execution cancel API, or OpenRouter abort. In-flight LLM HTTP (120s timeout) continues.

### 8.5 User notification

**Node:** `Send Stop All Flow Success`

> ✅ Активные задачи сброшены. Новые задачи можно запускать.

### 8.6 What remains running

- Current Worker n8n execution graph
- Active OpenRouter HTTP requests
- Pending Telegram sends from that execution
- Memory append operations

### 8.7 Lock impact

- Sheet rows: `active` → `cancelled`
- Worker may still run `Close Lock Before Sending` with `status=done` afterward — **overwrite race SAFE UNKNOWN**

### 8.8 Operator messaging (recommended later)

Describe `/stop-all-flow` as:

> **Logical lock reset for your chat in Google Sheets.** Does not abort running AI requests or in-flight Worker executions. You may still receive output from a run started before cancel. Use only when locks are stuck; prefer waiting for natural completion when possible.

### 8.9 Patch candidates

| Title | Type | Nodes |
|-------|------|-------|
| Honest stop semantics | DOC_ONLY / ADMIN_RUNBOOK | — |
| Rename or add `/stop-my-locks` | DOC_ONLY | `Build Admin Response` |
| Worker cancel-awareness | N8N_CODE_NODE_PATCH | `Store Worker Meta` + early check in `Route Command` |
| Fleet-wide stop (if intended) | N8N_NODE_PATCH + Operator approval | Admin `Lookup Active Locks` filter |
| n8n execution cancel research | SAFE_UNKNOWN | — |

---

## 9. Google Sheets Lock and Memory Model

### 9.1 `seo_active_jobs`

| Aspect | Detail |
|--------|--------|
| **Used by** | Intake: `Lookup Active Locks`, `Create Lock Row`; Worker: `Close Lock Before Sending`, `Close Single Lock Before Sending`, `Finish Lock`; Admin: `Lookup Active Locks`, `Cancel Active Locks`, `Lookup Locks`, `Health Check Active Jobs` |
| **Columns (evidenced)** | `lock_key`, `chat_id`, `user_id`, `username`, `first_name`, `last_name`, `task_id`, `created_at`, `expires_at`, `status`, `finished_at`, `cancel_reason`, `row_number` |
| **Read ops** | Lookup by `chat_id`+`status`; lookup by `lock_key` for update |
| **Write ops** | Append on create; update on close/cancel |
| **status values** | `active`, `done`, `cancelled` |
| **expires_at** | `now + 30 minutes` at create; checked in `Check Active Lock` and `Format Locks Response` |
| **cancel_reason** | `admin_stop_all_flow` on admin cancel |
| **task_id** | `pending` at create; promoted on **single/reuse close only** |
| **Missing schema** | Terminal `failed` status; `mode`; link to memory row — **SAFE UNKNOWN** |
| **Risks** | No transactions; stale `active`; `pending` desync on run; per-chat stop vs name |

### 9.2 `memory`

| Aspect | Detail |
|--------|--------|
| **Used by** | Intake: `Lookup From Task`; Worker: `Lookup Memory Get`, `Lookup Memory Reuse`, `Append Memory Local/Single/Run` |
| **Lookup** | Intake: filtered by `task_id`; Worker get/reuse: **full tab read** + code filter |
| **Append** | After local/single/run; `continueOnFail: true` |
| **Columns (append evidenced)** | `timestamp`, `task_id`, `mode`, `chat_id`, `user_id`, `username`, `first_name`, `last_name`, `input`, `output`, `chunk_count`, `status` |
| **get relation** | Read-only; formats `input` (first 3000) + full `output` |
| **reuse relation** | Injects stored input/output into new single-mode generation |
| **chunking** | `chunk_count` stored; Telegram split at 3600 chars |
| **Risks** | Full-sheet reads; append fail silent; retention/PII policy **SAFE UNKNOWN** |

---

## 10. Sequence Diagrams

### 10.1 Normal content request success

```
User          Intake              Sheets           Worker           OpenRouter      Telegram
  |              |                   |                |                 |              |
  |--/text------>|                   |                |                 |              |
  |              |--lookup locks---->|                |                 |              |
  |              |<--no active-------|                |                 |              |
  |              |--append lock----->| active/pending |                 |              |
  |              |--Task Accepted---------------------------------------->|              |
  |              |--HTTP POST worker_payload-------->|                 |              |
  |              |                   |                |--single/run--->|              |
  |              |                   |                |<--result-------|              |
  |              |                   |<-close lock----| status=done    |              |
  |              |                   |                |--append memory>|              |
  |              |                   |                |--result chunks----------------->|
```

### 10.2 Content request when active lock exists

```
User          Intake              Sheets           Worker
  |              |                   |                |
  |--/run------->|                   |                |
  |              |--lookup locks---->|                |
  |              |<--active row-------|                |
  |              |--Check Active Lock (not expired)   |
  |<--Busy msg---|                   |                |
  |              | (Worker NOT called)                |
```

### 10.3 `/get` existing task

```
User       Intake           Sheets(memory)     Worker           Sheets(memory)    Telegram
  |           |                  |                 |                  |              |
  |--/get id->|                  |                 |                  |              |
  |           |--lookup task_id->|                 |                  |              |
  |           |<--row found------|                 |                  |              |
  |           |--HTTP POST (lock=null)------------>|                  |              |
  |           |                  |                 |--read memory tab->|              |
  |           |                  |                 |--Find row--------|              |
  |           |                  |                 |--format chunks------------------>|
```

### 10.4 `/get` missing task

```
User       Intake           Sheets(memory)     Worker           Telegram
  |           |                  |                 |              |
  |--/get bad->|                  |                 |              |
  |           |--lookup task_id->|                 |              |
  |           |<--no row---------|                 |              |
  |           | IF task_id?      |                 |              |
  |           | [false branch]   |                 |              |
  |<--NOT-FOUND|                  |                 |              |
  |           |                  |                 |              |
  |  OR (if IF true on parsed id):                 |              |
  |           |--HTTP POST----------------------->|              |
  |           |                  |                 |--not found msg------------->|
```

### 10.5 `from:task_id` reuse success

```
User       Intake           Sheets(jobs)      Worker           Sheets(memory)    OpenRouter
  |           |                  |                |                  |              |
  |--/text from:ID-------------->|                |                  |              |
  |           |--create lock---->| active/pending |                  |              |
  |           |--Task Accepted-->|                |                  |              |
  |           |--HTTP POST+lock------------------>|                  |              |
  |           |                  |                |--read memory---->|              |
  |           |                  |                |--Prepare Reuse---|              |
  |           |                  |                |--single LLM------------------->|
  |           |                  |<-close+task_id-|                  |              |
  |           |                  |                |--append memory-->|              |
```

### 10.6 Worker OpenRouter failure after Intake lock creation

```
User       Intake           Sheets(jobs)      Worker           OpenRouter
  |           |                  |                |                 |
  |--/run----->|                  |                |                 |
  |           |--create lock---->| active/pending |                 |
  |           |--Task Accepted-->|                |                 |
  |           |--HTTP POST----------------------->|                 |
  |           |                  |                |--HTTP timeout--X|
  |           |                  |  (lock stays active — SAFE UNKNOWN cleanup)
  |  (no error Telegram evidenced)
```

### 10.7 Admin `/stop-all-flow` while Worker running

```
User       Intake      Admin        Sheets(jobs)     Worker       OpenRouter
  |           |           |              |              |             |
  | (run started earlier)  |              |              |--processing->|
  |--/stop-all-flow------>|              |              |             |
  |           |--HTTP---->|              |              |             |
  |           |           |--cancel rows>| cancelled    |             |
  |<--success-|           |              |              |             |
  |           |           |              |              |--may complete->|
  |<--result may still arrive from Worker----------------------------|
```

---

## 11. Failure Mode Register

| ID | Path | Failure condition | Current behavior | User impact | Lock impact | Memory impact | Detection | Patch type | Priority |
|----|------|-------------------|------------------|-------------|-------------|---------------|-----------|------------|----------|
| FM-01 | `/get` | `Send To Worker` HTTP fail | No evidenced error branch | Silence | None | None | n8n execution log | N8N_NODE_PATCH | P0 |
| FM-02 | `/get` | `Send Telegram Memory Get` fail | No error branch | Silence | None | None | n8n log | N8N_NODE_PATCH | P0 |
| FM-03 | `/get` | `Lookup Memory Get` 0 items | `Find Memory Get Row` may not run | Silence | None | None | Sandbox trace | N8N_CODE_NODE_PATCH | P0 |
| FM-04 | `/get` | Sheets lookup error at Intake | **SAFE UNKNOWN** | Silence or crash | None | None | n8n log | N8N_NODE_PATCH | P0 |
| FM-05 | `/get` | `IF From Task Exists` logic | Checks `task_id` not row match | Wrong routing | None | Read only | Code review | N8N_NODE_PATCH | P1 |
| FM-06 | reuse | Source missing | LLM runs on `MEMORY_LOOKUP_FAILED` stub | Confusing output | Orphan risk | Bad append possible | TC-I16 | N8N_CODE_NODE_PATCH | P0 |
| FM-07 | content | Worker unreachable post-lock | Orphan `active` lock | Task Accepted then silence | **active orphan** | None | TR-14 | N8N_NODE_PATCH | P0 |
| FM-08 | content | OpenRouter timeout 120s | **SAFE UNKNOWN** downstream | Silence after accepted | Stale active | None | TR-10 | N8N_NODE_PATCH | P0 |
| FM-09 | content | Telegram send fail mid-run | **SAFE UNKNOWN** | Partial/no output | May be `done` already | May append | TR-06 | N8N_NODE_PATCH | P1 |
| FM-10 | content | Memory append fail | `continueOnFail: true` | Has output; `/get` fails later | None | **row missing** | TR-11 | ADMIN_RUNBOOK | P1 |
| FM-11 | lock | Close lock fail | **SAFE UNKNOWN** | May still get output | Inconsistent | None | Sheets audit | GOOGLE_SHEETS_SCHEMA_PATCH | P1 |
| FM-12 | admin | Cancel during Worker | Sheet cancelled; Worker runs | Misleading stop | Race done/cancelled | May append | TR-07 | DOC_ONLY | P1 |
| FM-13 | lock | Expired `active` row | Still blocks if status not changed | False busy | **stale active** | None | TR-03 | N8N_CODE_NODE_PATCH | P0 |
| FM-14 | lock | `task_id` stays `pending` on `/run` | Evidenced — close omits task_id | `/locks` misleading | **pending** | memory has real id | IB-03 | N8N_NODE_PATCH | P0 |
| FM-15 | lock | Duplicate concurrent create | **SAFE UNKNOWN** race | Double run? | Duplicate rows? | Duplicate? | Concurrent test | GOOGLE_SHEETS_SCHEMA_PATCH | P1 |
| FM-16 | lookup | Lookup returns no rows | Intake NOT-FOUND or Worker not-found | Message or silence | None | None | TC-I12 | TEST_ONLY | P0 |
| FM-17 | lookup | Lookup node error | continueOnFail partial | Wrong not-found or silence | Varies | Varies | TR-08 | N8N_NODE_PATCH | P0 |
| FM-18 | infra | Sheets quota | Errors across paths | Intermittent silence | Stuck locks | Read fail | `/health` | ADMIN_RUNBOOK | P1 |

---

## 12. Safe Patch Candidates

| ID | Title | Class | Affected nodes | Expected benefit | Impl risk | Evidence before patch | Sandbox tests | Operator approval |
|----|-------|-------|----------------|------------------|-----------|----------------------|---------------|-------------------|
| PC-01 | Fix `IF From Task Exists` to check memory row | N8N_NODE_PATCH | `IF From Task Exists`, optionally `Lookup From Task` | Correct Intake NOT-FOUND; skip Worker on missing | Low | Confirm `alwaysOutputData` passthrough in live n8n | TC-I12 | Yes |
| PC-02 | `/get` immediate ack Telegram | N8N_NODE_PATCH | New node after `Route Retrieval Command` | UX — reduces perceived silence | Low | UX copy approval | TC-I11 | Yes |
| PC-03 | `Send To Worker` error branch + lock compensation | N8N_NODE_PATCH | `Send To Worker`, optional lock delete node | Prevent orphan locks | Medium | HTTP error taxonomy from logs | TR-14 | Yes |
| PC-04 | Filtered memory lookup on Worker get | N8N_NODE_PATCH | `Lookup Memory Get` | Quota/latency fix | Medium | Sheet column map | TC-W04 | Yes |
| PC-05 | Guard zero-item after memory lookup | N8N_CODE_NODE_PATCH | `Find Memory Get Row`, `Find Memory Reuse Row` | Prevent silent halt | Low | Sandbox | TR-12, TR-13 | No |
| PC-06 | Reuse halt on missing source | N8N_CODE_NODE_PATCH | `Prepare Memory Reuse` + IF | No LLM on missing; close lock with error | Medium | UX message approval | TC-I16 | Yes |
| PC-07 | Promote `task_id` on run close | N8N_NODE_PATCH | `Close Lock Before Sending` | Fix pending desync | Low | Column map | TR-01, IB-03 | Yes |
| PC-08 | Expired lock ignore in `Check Active Lock` | N8N_CODE_NODE_PATCH | `Check Active Lock` | Auto-recover after TTL | Medium | Operator TTL policy | TR-03 | Yes |
| PC-09 | Background stale-lock cleanup | N8N_NODE_PATCH + ADMIN_RUNBOOK | New scheduled workflow | Fleet hygiene | High | Cleanup policy charter | IB-02 | Yes |
| PC-10 | `/stop-all-flow` honest docs | DOC_ONLY / ADMIN_RUNBOOK | `admin-operations.md`, `Build Admin Response` | Operator trust | Low | None | IB-06 | No |
| PC-11 | Worker error subgraph template | N8N_NODE_PATCH | All Worker HTTP/Telegram nodes | Systematic error Telegram | High | Patch protocol | IB-07 | Yes |
| PC-12 | Safe Workflow Patch Protocol v1 | DOC_ONLY | — | Gate before any PC-01–11 | Low | None | IB-20 | No |
| PC-13 | Redacted Sheets sample for schema | SAFE_UNKNOWN | — | Close schema gaps | None | Operator export | IB-03 | Yes |

---

## 13. Recommended Next Action

**Pick: B — Create Safe Workflow Patch Protocol v1 first**

This audit identifies **multiple P0 patch candidates** (PC-01–07) touching live Intake/Worker graphs. Issue **IB-20** and grammar docs exist in fragments but there is **no unified safe-patch gate** in-repo. Before any n8n mutation:

1. Operator reviews this audit.
2. Author **Safe Workflow Patch Protocol v1** (sandbox export, diff, rollback, test matrix sign-off).
3. Then execute targeted patches (recommend order: PC-01 → PC-04 → PC-07 → PC-03) with sandbox runs of TC-I11, TC-I12, TR-14.

Optional parallel: **E** — request redacted `seo_active_jobs` / `memory` samples to close FM-14 and schema SAFE UNKNOWNs.

---

## 14. SAFE UNKNOWN

| Topic | Why it matters |
|-------|----------------|
| `Lookup From Task` empty-result item shape with `alwaysOutputData` | Determines Intake vs Worker not-found routing |
| Worker mid-pipeline lock cleanup on LLM/parse errors | Orphan lock frequency |
| `cancelled` vs `done` race when stop-all during run | Lock truth |
| Fleet-wide vs per-chat stop intent | Operator policy |
| Telegram admin ACL | Security of stop/health |
| Full `memory` column schema and indexes | Lookup performance |
| Production-only parallel v13 graphs | Test target uncertainty |
| Automated expiry job existence outside export | Stale lock remediation |
| n8n version-specific Sheets node behavior | Import/patch compatibility |

---

## 15. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-get-lock-lifecycle-deep-audit.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 16. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** `61bb601944699109c5af918fb1b34319ca2f1820`
- **origin/mars/canonical-post-recovery:** `49ffdafe68d634a7cfc4254a551c0e4862a67282` (HEAD ahead)
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** preserved (Website Factory, fp-0002 workspaces, `.recovery-temp/`, etc.)
- **Commit / push:** not performed

---

## 17. Final Status

**COMPLETE — /get and lock lifecycle audit completed**

---

Awaiting operator review.
