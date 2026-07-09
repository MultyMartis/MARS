# n8n Node Type Catalog v14

**Status:** REPO_EVIDENCED reference catalog  
**Source evidence:** `projects/metabot-seo-content-agent/exports/live-v14-evidence/2026-07-10/*.sanitized.json`  
**Classification:** LIVE_API_EXPORT · SANITIZED · SAFE_TO_COMMIT  
**Export date:** 2026-07-10  
**Workflows:** Intake (20 nodes) · Worker (91 nodes) · Admin (15 nodes) · **Total: 126 nodes**

**Limits:** Credential objects, webhook IDs, and sheet document IDs are redacted in source JSON. Parameter **shapes** below are authoritative; live values require operator binding.

**Companion:** [n8n-workflow-json-grammar-v1.md](n8n-workflow-json-grammar-v1.md)

---

## Summary table

| Node type | Count | Workflows | typeVersion(s) |
|-----------|-------|-----------|----------------|
| `n8n-nodes-base.code` | 62 | I, W, A | 2 |
| `n8n-nodes-base.telegram` | 19 | I, W, A | 1, 1.2 |
| `n8n-nodes-base.googleSheets` | 16 | I, W, A | 4, 4.7 |
| `n8n-nodes-base.httpRequest` | 11 | I, W | 4, 4.4 |
| `n8n-nodes-base.if` | 9 | I, W, A | 2, 2.3 |
| `n8n-nodes-base.switch` | 4 | W | 3, 3.2 |
| `n8n-nodes-base.webhook` | 2 | W, A | 2.1 |
| `n8n-nodes-base.telegramTrigger` | 1 | I | 1 |
| `n8n-nodes-base.set` | 1 | W | 2 |
| `n8n-nodes-base.wait` | 1 | W | 1.1 |

---

## n8n-nodes-base.telegramTrigger

| Attribute | Value |
|-----------|-------|
| Workflows | Intake only |
| Count | 1 |
| typeVersion | **1** |
| Role | Primary entry — Telegram message updates |

**Key parameters:**

```json
{
  "updates": ["message"],
  "additionalFields": {}
}
```

**Required:** `updates`, credentials (Telegram API), `webhookId` (assigned by n8n)  
**Sensitive:** bot token (via credentials only)  
**Import notes:** Must be workflow trigger; only one per Intake graph  

**Generation guidance:** Do not fabricate `webhookId`. Include credentials placeholder comment in companion doc; operator binds Telegram credential in UI. Copy `typeVersion: 1` exactly.

---

## n8n-nodes-base.telegram

| Attribute | Value |
|-----------|-------|
| Workflows | Intake (5), Worker (12), Admin (2) |
| Count | 19 |
| typeVersion | **1.2** (6), **1** (13) |
| Role | Send messages, edit status messages, user feedback |

**Send message shape:**

```json
{
  "chatId": "REDACTED_PERSONAL_ID",
  "text": "={{ $json.response_text }}",
  "additionalFields": {
    "appendAttribution": false,
    "parse_mode": "HTML"
  }
}
```

**Edit status shape (Worker pipeline):**

```json
{
  "operation": "editMessageText",
  "chatId": "...",
  "messageId": "={{ $json.status_message_id }}",
  "text": "={{ $json.status_text }}"
}
```

**Required:** `chatId`, `text` (or operation-specific fields)  
**Risky:** hardcoded chat IDs in repo  
**Dynamic fields:** `chatId`, `text`, `messageId` — use expressions in generated JSON  

**Generation guidance:** Prefer `typeVersion: 1.2` with `parse_mode: HTML` for new send nodes matching Intake. Upstream Code nodes should produce `telegram_text` / `response_text`; apply markdown cleanup expression before send when needed.

---

## n8n-nodes-base.webhook

| Attribute | Value |
|-----------|-------|
| Workflows | Worker, Admin |
| Count | 2 |
| typeVersion | **2.1** |
| Role | Cross-workflow HTTP entry (Intake handoff) |

**Observed paths:**

| Workflow | path | httpMethod |
|----------|------|------------|
| Worker | `seo-content-agent-worker` | POST |
| Admin | `seo-content-agent-admin` | POST |

**Parameter shape:**

```json
{
  "httpMethod": "POST",
  "path": "seo-content-agent-worker",
  "options": {
    "responseCode": { "values": {} },
    "responseData": "{\"ok\": true}"
  }
}
```

**Required:** `path`, `httpMethod`  
**Risky:** colliding path with other workflows on same n8n instance  
**Import notes:** `webhookId` assigned on activation; omit in synthetic JSON  

**Generation guidance:** Use namespaced paths (`seo-content-agent-*`). Document full production URL in operator runbook, not in committed JSON.

---

## n8n-nodes-base.httpRequest

| Attribute | Value |
|-----------|-------|
| Workflows | Intake (2), Worker (9) |
| Count | 11 |
| typeVersion | **4.4** (Intake handoff), **4** (Worker OpenRouter) |
| Role | OpenRouter LLM calls; Intake→Worker/Admin webhook POST |

**OpenRouter call (required params):**

- `method`: POST  
- `url`: `https://openrouter.ai/api/v1/chat/completions`  
- `sendHeaders`: true  
- `headerParameters`: Authorization + Content-Type  
- `sendBody`: true  
- `specifyBody`: `"json"`  
- `jsonBody`: `={{ JSON.stringify($json.openrouter_payload) }}`  
- `options.timeout`: 120000 (Worker LLM nodes)

**Handoff call (Intake):**

- `jsonBody`: `={{ $json.worker_payload }}`  
- `url`: production webhook URL (operator-provided)

**Sensitive:** Authorization header, webhook URLs  
**Generation guidance:** Build payloads in Code nodes; HTTP node only serializes. Use `typeVersion: 4` for OpenRouter, `4.4` if matching Intake handoff nodes exactly.

---

## n8n-nodes-base.googleSheets

| Attribute | Value |
|-----------|-------|
| Workflows | Intake (3), Worker (8), Admin (5) |
| Count | 16 |
| typeVersion | **4.7** (11), **4** (5) |
| Role | Locks (`seo_active_jobs`), memory (`memory`), health checks |

**Tabs used:**

| Tab name | Purpose |
|----------|---------|
| `seo_active_jobs` | Active/done locks, cancel, health |
| `memory` | Task results, get/reuse lookups |

**Operations:**

| operation | Example nodes |
|-----------|---------------|
| append | Create Lock Row, Append Memory Local/Single/Run |
| update | Finish Lock, Close Lock*, Cancel Active Locks |
| (read) | Lookup Active Locks, Lookup Memory Get, Health Check Memory |

**Required parameters:**

- `documentId` with `__rl: true`, `mode: "id"`  
- `sheetName` with `__rl: true`, `mode: "list"`, `cachedResultName`  
- For append/update: `columns` with `mappingMode`, `value`, often `schema`  

**Redacted:** `documentId.value`, full URLs  
**Generation guidance:** Copy column `schema` blocks from export when modifying append nodes. Use `typeVersion: 4.7` for lock/update nodes, `4` for memory append if matching Worker. Operator replaces `REDACTED_SHEET_ID`.

---

## n8n-nodes-base.code

| Attribute | Value |
|-----------|-------|
| Workflows | Intake (5), Worker (54), Admin (3) |
| Count | 62 |
| typeVersion | **2** (uniform) |
| Role | Routing, payload build, extract, restore, quality, formatting |

**Parameter shape:**

```json
{
  "jsCode": "// JavaScript string\nreturn [{ json: { ... } }];"
}
```

**Representative nodes by role:**

| Role | Examples |
|------|----------|
| Routing | Detect Local Command, Route Command |
| Payload | Build Outline Payload, Build Factcheck Payload |
| Extract | Run Extract Text, Run Extract SEO QA |
| Restore | Restore Route Data, Restore Content Score Data |
| Quality | Compute Content Score, Strict Risk Scanner, Table Sanity Check |
| Lock | Build User Lock Key, Check Active Lock |
| Output | Format Run Pipeline, Normalize Run Output |

**Required:** `jsCode`  
**Generation guidance:** Always `typeVersion: 2`. Return `[{ json }]`. Reference nodes by exact `name`. See grammar doc §6.

---

## n8n-nodes-base.if

| Attribute | Value |
|-----------|-------|
| Workflows | Intake (5), Worker (1), Admin (3) |
| Count | 9 |
| typeVersion | **2** (1), **2.3** (8) |
| Role | Boolean routing — busy lock, local/admin/retrieval commands |

**Key parameters:** `conditions.options`, `conditions.conditions[]`, `conditions.combinator`  
**Required:** at least one condition with `leftValue`, `rightValue`, `operator`  
**Connection rule:** output 0 = true, output 1 = false  

**Generation guidance:** Prefer `typeVersion: 2.3` with `operator.name` for new nodes. Wrap boolean JSON fields with `String()` for string comparison.

---

## n8n-nodes-base.switch

| Attribute | Value |
|-----------|-------|
| Workflows | Worker only |
| Count | 4 |
| typeVersion | **3.2** (1 — Switch Route), **3** (3 — run pipeline switches) |
| Role | Multi-way route by `$json.route` or boolean flags |

**Switch Route output keys:** local, single, run, get, reuse

**Required:** `rules.values[]` with conditions + `outputKey` when `renameOutput: true`  
**Connection rule:** `main[i]` ↔ `values[i]`

**Generation guidance:** Use `typeVersion: 3.2` for new multi-route switches. Keep output key names stable — downstream documentation references them.

---

## n8n-nodes-base.set

| Attribute | Value |
|-----------|-------|
| Workflows | Worker |
| Count | 1 (`Set Raw Input`) |
| typeVersion | **2** |
| Role | Normalize webhook JSON into pipeline fields |

**Generation guidance:** Prefer Code node for complex normalization in new work; keep Set only when matching existing Worker entry pattern.

---

## n8n-nodes-base.wait

| Attribute | Value |
|-----------|-------|
| Workflows | Worker |
| Count | 1 |
| typeVersion | **1.1** |
| Role | Timing between status updates / API pacing |

**Generation guidance:** Copy parameters from export if adding wait; do not invent duration without operator spec.

---

## Nodes not present in v14

The following were checked but **not observed** in v14 exports:

- `n8n-nodes-base.merge`  
- `n8n-nodes-base.noOp`  
- `n8n-nodes-base.respondToWebhook`  
- `n8n-nodes-base.executeWorkflow`  

**SAFE UNKNOWN** whether older MetaBOT versions used these types.

---

## typeVersion compatibility matrix

When generating JSON for this operator instance, use these exact versions unless a fresh export proves an upgrade:

| Node type | Preferred typeVersion |
|-----------|----------------------|
| telegramTrigger | 1 |
| telegram | 1.2 (send) / 1 (legacy Worker sends) |
| webhook | 2.1 |
| httpRequest | 4 (OpenRouter) / 4.4 (handoff) |
| googleSheets | 4.7 (locks) / 4 (memory append) |
| code | 2 |
| if | 2.3 |
| switch | 3.2 (route) / 3 (pipeline) |
| set | 2 |
| wait | 1.1 |

---

*MetaBOT Developer · node catalog from live v14 sanitized exports · 2026-07-10*
