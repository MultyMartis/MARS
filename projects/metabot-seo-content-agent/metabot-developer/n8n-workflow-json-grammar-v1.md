# n8n Workflow JSON Grammar v1

**Status:** REPO_EVIDENCED reference grammar for MetaBOT Developer  
**Source evidence:** `projects/metabot-seo-content-agent/exports/live-v14-evidence/2026-07-10/`  
**Classification:** LIVE_API_EXPORT · SANITIZED · SAFE_TO_COMMIT (operator review required)  
**Export date:** 2026-07-10  
**Live workflow names:**

- `SEO Content Agent Beta.v14 - Intake`
- `SEO Content Agent Beta.v14 - Worker`
- `SEO Content Agent Beta.v14 - Admin`

**Limits:** Sanitized exports redact credentials, tokens, webhook IDs/URLs, sheet IDs, personal IDs, pinData, and some execution metadata. Grammar shapes are authoritative; secret values and live credential bindings are not.

**n8n version:** **SAFE UNKNOWN** — exact server version not present in export JSON. See [n8n-import-safe-generation-rules-v1.md](n8n-import-safe-generation-rules-v1.md).

**Companion docs:** [n8n-node-type-catalog-v14.md](n8n-node-type-catalog-v14.md) · [n8n-import-safe-generation-rules-v1.md](n8n-import-safe-generation-rules-v1.md)

---

## 1. Purpose

This document formalizes the observed n8n workflow JSON structure from live v14 exports so MetaBOT Developer can generate or modify importable workflow JSON without repeating historical Web-GPT import/display failures.

Use this as **reference grammar**, not execution truth. Live n8n remains authoritative.

---

## 2. Top-level workflow JSON grammar

Observed top-level keys are **identical across Intake, Worker, and Admin** (21 keys each).

| Field | Type (observed) | In I/W/A | Import role | MetaBOT generate? | Notes |
|-------|-----------------|----------|-------------|-------------------|-------|
| `name` | string | all | **required** | yes | Exact live names include `Beta.v14` suffix |
| `nodes` | array | all | **required** | yes | Core graph |
| `connections` | object | all | **required** | yes | Keys = source **node names** |
| `settings` | object | all | **required** | yes | Always includes `executionOrder: "v1"` |
| `active` | boolean | all | optional | omit or `false` for drafts | Live exports are `true` |
| `id` | string | all | optional on fresh import | omit for new workflows | n8n assigns on create |
| `versionId` | string (UUID) | all | omit for synthetic JSON | omit | n8n version history |
| `activeVersionId` | string (UUID) | all | omit | omit | API export artifact |
| `versionCounter` | number | all | omit | omit | API export artifact |
| `createdAt` | ISO string | all | omit | omit | n8n-managed |
| `updatedAt` | ISO string | all | omit | omit | n8n-managed |
| `triggerCount` | number | all | omit | omit | Derived by n8n |
| `description` | null/string | all | optional | omit or null | Observed `null` |
| `isArchived` | boolean | all | omit | omit | Observed `false` |
| `meta` | object | all | optional | optional | Observed `{ templateCredsSetupCompleted: true }` |
| `tags` | array | Intake, Admin | optional | optional | Worker export had `[]` |
| `staticData` | object/null | Intake only | optional | omit unless needed | Intake had legacy `global.seo_active_jobs`; Worker/Admin `null` |
| `pinData` | object/string | all | **omit** in generated JSON | omit | Sanitized to `REDACTED_PINNED_DATA` |
| `shared` | array | all | omit | omit | API ownership metadata |
| `activeVersion` | object | all | omit | omit | Nested full workflow copy + publish history from API export |

### 2.1 Settings shape (observed)

```json
{
  "executionOrder": "v1",
  "binaryMode": "separate",
  "availableInMCP": false
}
```

Intake includes `availableInMCP`; Worker/Admin omit it. Safe default: `{ "executionOrder": "v1" }`.

### 2.2 API export nesting (`activeVersion`)

Live API exports embed a full duplicate under `activeVersion` (nodes, connections, authors, `workflowPublishHistory`). This is **not** required for manual import UI paste and should **not** be synthesized by MetaBOT Developer.

---

## 3. Node object grammar

Every node in v14 exports includes at minimum:

| Field | Type | Required | Generate? | Classification |
|-------|------|----------|-----------|----------------|
| `name` | string | **yes** | yes | Must be unique within workflow; used as connection key |
| `type` | string | **yes** | yes | e.g. `n8n-nodes-base.code` |
| `typeVersion` | number | **yes** | yes — match catalog | Wrong version breaks import/UI |
| `position` | `[x, y]` | **yes** | yes | Canvas layout |
| `parameters` | object | **yes** | yes | Node-specific |
| `id` | string (UUID) | present in exports | optional | n8n can assign; use UUID v4 if generating |
| `credentials` | object | conditional | **reference only** | Sanitized to `REDACTED_CREDENTIAL`; operator binds in UI |
| `webhookId` | string | conditional | **omit** on synthetic | On Telegram, Webhook nodes; n8n assigns on activate |
| `disabled` | boolean | not observed | omit unless needed | — |
| `notes` | string | not observed | optional | — |
| `retryOnFail` | boolean | not observed | omit | — |
| `continueOnFail` | boolean | Worker (5 nodes) | optional | Used on some Google Sheets append nodes |
| `alwaysOutputData` | boolean | Intake (2), Admin (3) | optional | Sheets lookup paths |
| `onError` | string | Admin (2) | optional | Observed on error-tolerant Admin nodes |
| `executeOnce` | boolean | not observed | omit | — |

### 3.1 Field frequency by workflow

| Field | Intake (20 nodes) | Worker (91) | Admin (15) |
|-------|-------------------|-------------|------------|
| `webhookId` | 5 | 15 | 3 |
| `credentials` | 8 | 21 | 7 |
| `continueOnFail` | 0 | 5 | 0 |
| `alwaysOutputData` | 2 | 0 | 3 |

---

## 4. Connections grammar

### 4.1 Structure

```json
"connections": {
  "Source Node Name": {
    "main": [
      [ { "node": "Target Node Name", "type": "main", "index": 0 } ],
      [ { "node": "Other Target", "type": "main", "index": 0 } ]
    ]
  }
}
```

| Rule | Detail |
|------|--------|
| Source key | **Node `name` string**, not `id` |
| Output channel | Only `"main"` observed in v14 |
| Nesting | `main[outputBranchIndex][targetIndex]` |
| Target object | `{ node, type: "main", index: 0 }` — `index` is target input index |
| Single output | `main: [ [ {...} ] ]` — one branch, one target |
| IF node | `main[0]` = true branch, `main[1]` = false branch |
| Switch node | `main[0..n-1]` = rule order (matches `rules.values` order) |

### 4.2 Observed branch counts

| Workflow | Source nodes in connections | Max branches per source |
|----------|----------------------------|-------------------------|
| Intake | 15 | 2 (IF nodes) |
| Worker | 84 | 5 (Switch Route) |
| Admin | 13 | 2 (IF nodes) |

### 4.3 Safe IF example (from Intake)

```json
"IF Busy": {
  "main": [
    [ { "node": "Send Busy Message", "type": "main", "index": 0 } ],
    [ { "node": "Create Lock Row", "type": "main", "index": 0 } ]
  ]
}
```

### 4.4 Switch Route branch map (Worker)

| Branch index | Output key | Target |
|--------------|------------|--------|
| 0 | local | Format Local Response |
| 1 | single | Status Single |
| 2 | run | Status Outline |
| 3 | get | Lookup Memory Get |
| 4 | reuse | Lookup Memory Reuse |

### 4.5 Common connection errors to avoid

1. Using node `id` instead of `name` as connection key  
2. Mismatched node name spelling (case-sensitive)  
3. Missing second branch array on IF nodes (empty branch = `[]`)  
4. Switch branch order not matching `rules.values` order  
5. Orphan nodes (in `nodes` but not reachable — import may work, logic breaks)  
6. Duplicate node names within one workflow  

---

## 5. Expressions grammar

n8n parameter fields use a leading `=` to enable expressions.

### 5.1 Delimiters

| Form | Usage |
|------|-------|
| `={{ expression }}` | Standard inline expression |
| `={{ ... multiline ... }}` | Complex JSON/body expressions |
| `=literal text` | Static string with optional embedded `{{ }}` for interpolation |
| `={{ $('Node Name').first().json.field }}` | Cross-node reference in parameters |

### 5.2 Observed patterns (64 unique expression strings in v14)

**Current item:**

- `={{ $json.route }}`
- `={{ String($json.is_busy) }}`
- `={{ Boolean($json.task_id) }}`

**Cross-node (parameter expressions):**

- `={{ $('Build User Lock Key').first().json.chat_id }}`
- `={{ $('Detect Local Command').first().json.task_id }}`

**Functions:**

- `={{ new Date().toISOString() }}`
- `={{ JSON.stringify($json.openrouter_payload) }}`

**String cleanup (Telegram):**

- `={{ String($json.telegram_text || '').replace(/_/g, '-').replace(/\*/g, '').replace(/`/g, "'") }}`

**Ternary / multiline:**

- Task-accepted message uses nested ternary on command === 'run'

### 5.3 `$items()` usage

Observed **only in Code nodes**, not in parameter expressions:

```javascript
$items('Compute Content Score', 0, 0)?.[0]?.json || {}
```

Used by restore nodes to merge pipeline state from earlier branches.

### 5.4 Code node vs parameter expressions

| Context | Syntax | Access prior nodes |
|---------|--------|-------------------|
| Parameter field | `={{ ... }}` | `$json`, `$('Name').first().json` |
| Code node JS | plain JavaScript | `$json`, `$input`, `items`, `$('Name').first()`, `$items('Name', 0, 0)` |

**Pitfall:** Using `$node["Name"]` — **not observed** in v14; prefer `$('Node Name')`.

**Pitfall:** Forgetting `String()` wrapper when IF conditions compare booleans as strings (`String($json.is_busy)` equals `"true"`).

---

## 6. Code node grammar

| Attribute | Observed value |
|-----------|----------------|
| `type` | `n8n-nodes-base.code` |
| `typeVersion` | `2` (all 62 instances) |
| Parameter key | `parameters.jsCode` (string) |
| Language setting | not present — default JavaScript |

### 6.1 Input conventions

- `$json` — current item JSON
- `items` — all incoming items array
- `$('Node Name').first().json` — read specific upstream node output
- `$items('Node Name', 0, 0)` — random-access to prior node output in merge/restore paths

### 6.2 Output conventions

Always return array of items:

```javascript
return [{ json: { ...fields } }];
```

Minimal passthrough:

```javascript
return [items[0]];
```

Spread pattern (preserve upstream fields):

```javascript
return [{ json: { ...$json, new_field: value } }];
```

### 6.3 Role categories in v14

| Role | Example nodes | Pattern |
|------|---------------|---------|
| Routing | `Route Command`, `Detect Local Command` | Parse command → set `route`, flags, booleans |
| Payload build | `Build Outline Payload`, `Build SEOQA Payload` | Construct `openrouter_payload` object |
| Extract | `Run Extract Outline`, `Run Extract SEO QA` | Parse HTTP response → structured fields |
| Restore | `Restore Route Data`, `Restore Content Score Data` | Merge `$json` with `$items(...)` |
| Lock/state | `Build User Lock Key`, `Check Active Lock` | Lock key, busy detection |
| Quality | `Compute Content Score`, `Strict Risk Scanner` | Deterministic post-LLM checks |
| Format/output | `Format Run Pipeline`, `Normalize Run Output` | Telegram chunking, final text assembly |

### 6.4 Safe generation rules

- Return `[{ json: {...} }]` — never bare object  
- Use optional chaining when reading upstream (`?.`)  
- Keep node name references in `$('Exact Node Name')` matching `name` field exactly  
- Do not embed API keys — build payload objects for HTTP Request nodes  

### 6.5 Risky anti-patterns

- Hardcoded credentials in `jsCode`  
- `$node["Name"]` without verifying n8n version support  
- Returning wrong shape (object instead of array)  
- Minified one-liners without doc cross-reference  

---

## 7. HTTP Request node grammar

| Attribute | Observed |
|-----------|----------|
| `typeVersion` | `4` (9 nodes), `4.4` (2 nodes — Intake handoff) |
| Methods | `POST` |

### 7.1 OpenRouter pattern (Worker)

```json
{
  "method": "POST",
  "url": "https://openrouter.ai/api/v1/chat/completions",
  "sendHeaders": true,
  "headerParameters": {
    "parameters": [
      { "name": "Authorization", "value": "=REDACTED_TOKEN" },
      { "name": "Content-Type", "value": "application/json" }
    ]
  },
  "sendBody": true,
  "specifyBody": "json",
  "jsonBody": "={{ JSON.stringify($json.openrouter_payload) }}",
  "options": { "timeout": 120000 }
}
```

**Generation rule:** Authorization must use n8n credential or expression reference — never literal key in repo JSON.

### 7.2 Intake → Worker handoff

```json
{
  "method": "POST",
  "url": "REDACTED_WEBHOOK_URL",
  "sendBody": true,
  "specifyBody": "json",
  "jsonBody": "={{\n  $json.worker_payload\n}}",
  "options": {}
}
```

Worker webhook path (observed): `seo-content-agent-worker` (POST). Admin: `seo-content-agent-admin`.

Payload built upstream in `Build Worker Payload` Code node.

### 7.3 Sensitive fields — never hardcode

- Authorization headers / API keys  
- Full webhook production URLs  
- OAuth tokens  

---

## 8. Telegram node grammar

### 8.1 Telegram Trigger

```json
{
  "type": "n8n-nodes-base.telegramTrigger",
  "typeVersion": 1,
  "parameters": {
    "updates": ["message"],
    "additionalFields": {}
  },
  "webhookId": "REDACTED_WEBHOOK_ID",
  "credentials": "REDACTED_CREDENTIAL"
}
```

### 8.2 Send message (Telegram node)

| Parameter | Pattern |
|-----------|---------|
| `chatId` | Static in export (redacted) — live uses expression or dynamic from `$json.chat_id` |
| `text` | Expression or static; chunking done in Code nodes upstream |
| `additionalFields.appendAttribution` | `false` |
| `additionalFields.parse_mode` | `"HTML"` on formatted messages |

**typeVersion:** `1.2` (6 nodes) or `1` (13 nodes) — both present; prefer `1.2` for new nodes matching Intake pattern.

### 8.3 Status messages (Worker)

Worker uses `editMessageText` operation on status Telegram nodes for pipeline progress (Outline → Strategy → Text → SEO QA → Factcheck → Final).

### 8.4 Dynamic fields that must stay dynamic

- `chatId` — per-user  
- `text` — from `$json.telegram_text`, `$json.response_text`, etc.  
- Message IDs for edit operations — from prior Telegram responses  

---

## 9. Google Sheets node grammar

| Attribute | Observed |
|-----------|----------|
| `typeVersion` | `4.7` (11 nodes), `4` (5 nodes) |
| Credential | always present (sanitized) |

### 9.1 Document/tab selection shape

```json
{
  "documentId": {
    "__rl": true,
    "value": "REDACTED_SHEET_ID",
    "mode": "id"
  },
  "sheetName": {
    "__rl": true,
    "value": 2116752312,
    "mode": "list",
    "cachedResultName": "seo_active_jobs",
    "cachedResultUrl": "https://docs.google.com/spreadsheets/d/REDACTED_SHEET_ID/edit#gid=2116752312"
  }
}
```

**Tabs observed:** `seo_active_jobs`, `memory`

### 9.2 Operations by role

| Operation | Nodes | Tab |
|-----------|-------|-----|
| append | Create Lock Row; Append Memory * | seo_active_jobs / memory |
| update | Finish Lock, Close Lock*, Cancel Active Locks | seo_active_jobs |
| read/lookup | Lookup Active Locks, Lookup Memory*, Health Check* | both tabs |

### 9.3 Column mapping (update example)

```json
{
  "mappingMode": "defineBelow",
  "value": {
    "status": "done",
    "finished_at": "={{ new Date().toISOString() }}",
    "lock_key": "={{ $json.worker_lock_key || $('Store Worker Meta').first().json.worker_lock_key }}"
  },
  "matchingColumns": ["lock_key"]
}
```

Append nodes include full `schema` array with column id/displayName/type — large but import-safe when copied from export.

### 9.4 Redaction limits

Sheet IDs and gid numbers are redacted. Tab **names** preserved. Operator must supply real document ID in n8n UI after import.

---

## 10. Routing nodes (IF / Switch)

### 10.1 IF node (typeVersion 2 or 2.3)

Structure:

```json
{
  "conditions": {
    "options": {
      "caseSensitive": true,
      "leftValue": "",
      "typeValidation": "strict",
      "version": 1
    },
    "conditions": [{
      "id": "unique-id",
      "leftValue": "={{ String($json.is_busy) }}",
      "rightValue": "true",
      "operator": { "type": "string", "operation": "equals" }
    }],
    "combinator": "and"
  },
  "options": {}
}
```

typeVersion `2.3` adds `operator.name` (e.g. `"filter.operator.equals"`). Both work in v14 exports.

### 10.2 Switch node (typeVersion 3.2)

Uses `parameters.rules.values[]` with per-rule `conditions`, `renameOutput: true`, and `outputKey` (local/single/run/get/reuse).

Connection branch index matches `values` array order.

### 10.3 Intake routing flow

```
Telegram Trigger → Detect Local Command
  → IF Local Command → Send Local Intake Message
  → IF Admin Command → Send To Admin (HTTP)
  → Route Retrieval Command (IF) → Lookup From Task → ...
  → lock path → IF Busy → ...
  → Build Worker Payload → Send To Worker (HTTP)
```

---

## 11. Quality pipeline grammar (Worker)

| Stage | Node types | Flow pattern |
|-------|------------|--------------|
| **SEO QA** | Code `Build SEOQA Payload` → HTTP `Run SEO QA` → Code `Run Extract SEO QA` | OpenRouter call + extract structured `seoqa` |
| **Factcheck** | Code `Build Factcheck Payload` → HTTP `Run Factcheck` → Code `Run Extract Factcheck` → Switch `Switch Run Factcheck` | Branch on strict/normal |
| **Content Score** | Code `Compute Content Score` | Deterministic scoring on text + outline |
| **Strict Risk Scanner** | Code `Strict Risk Scanner` | Scans for risky claims (strict mode) |
| **Table Sanity Check** | Code `Table Sanity Check` | Validates table markup/structure |
| **Postcheck Strict Claims** | Code `Postcheck Strict Claims` | Post-LLM strict claim validation |
| **Text Repair** | Code `Build Text Repair Payload` → HTTP `Run Text Repair` → Code `Extract Text Repair` | LLM repair pass |
| **Auto Polish** | Code `Auto Polish Text` → HTTP `Run Auto Polish Text` → Code `Extract Auto Polish Text` | LLM polish pass |
| **Cleanup chain** | `Auto Fix Text` → `Ensure FAQ Text` → `Commercial Layer Text` → `Final Text Cleanup` → `Strict Cleanup` → `Hard Final Cleanup` | Code-only transforms |
| **Normalize output** | Code `Normalize Run Output` | Final Telegram-safe formatting/chunking |

**Restore pattern:** After parallel/branching steps, `Restore * Data` Code nodes merge state via `$items('Upstream Node', 0, 0)`.

**Switch routing after pipeline stages:** `Switch Run After Outline`, `Switch Run After Text`, `Switch Run Factcheck` control run-mode continuation.

---

## 12. Lock / state / memory grammar

### 12.1 Lock table (`seo_active_jobs`)

| Workflow | Nodes |
|----------|-------|
| Intake | Build User Lock Key → Lookup Active Locks → Check Active Lock → IF Busy → Create Lock Row |
| Worker | Store Worker Meta → Close Lock Before Sending / Close Single Lock → Finish Lock |
| Admin | Lookup Active Locks → Cancel Active Locks; Lookup Locks; Health Check Active Jobs |

**Lock key pattern:** `chat:{chatId}:{timestamp}` built in Code.

**Status values observed:** `active`, `done` (update operations).

### 12.2 Memory table (`memory`)

| Operation | Nodes |
|-----------|-------|
| append | Prepare Memory Row * → Append Memory Local/Single/Run |
| lookup | Lookup Memory Get, Lookup Memory Reuse, Lookup From Task (Intake) |
| find row | Find Memory Get Row, Find Memory Reuse Row (Code) |

**Reuse pattern:** `--from task-id` / `from:task_id` parsed in Intake/Worker Code nodes; retrieval via Sheets lookup then fed into generation pipeline.

### 12.3 Cross-workflow handoff

- Intake → Worker: HTTP POST to Worker webhook with `worker_payload` (**REPO_EVIDENCED** path shape; URL redacted)
- Intake → Admin: HTTP POST to Admin webhook with admin command envelope
- **SAFE UNKNOWN:** whether Execute Workflow node exists elsewhere — not in v14 exports

---

## 13. Other observed node types

| Type | Count | Notes |
|------|-------|-------|
| `n8n-nodes-base.set` | 1 | `Set Raw Input` — normalizes webhook body |
| `n8n-nodes-base.wait` | 1 | Rate-limit / sequencing in Worker |
| `n8n-nodes-base.webhook` | 2 | Worker + Admin entry points |

No `merge`, `noOp`, or `respondToWebhook` nodes observed in v14 exports.

---

*MetaBOT Developer · grammar derived from sanitized live v14 evidence · 2026-07-10*
