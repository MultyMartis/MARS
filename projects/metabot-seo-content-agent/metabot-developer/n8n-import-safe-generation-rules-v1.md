# n8n Import-Safe Generation Rules v1

**Status:** documented discipline for MetaBOT Developer synthetic workflow JSON  
**Source evidence:** `projects/metabot-seo-content-agent/exports/live-v14-evidence/2026-07-10/`  
**Classification:** LIVE_API_EXPORT · SANITIZED · SAFE_TO_COMMIT  
**Export date:** 2026-07-10  
**Derived from:** observed live v14 Intake / Worker / Admin API exports

**Companion:** [n8n-workflow-json-grammar-v1.md](n8n-workflow-json-grammar-v1.md) · [n8n-node-type-catalog-v14.md](n8n-node-type-catalog-v14.md)

---

## 1. Purpose

These rules prevent broken import/display when MetaBOT Developer generates n8n workflow JSON. They encode lessons from historical Web-GPT failures and the 2026-07-10 live export grammar pass.

---

## 2. Include vs omit checklist

### 2.1 Always include (minimal importable workflow)

```json
{
  "name": "Workflow Name",
  "nodes": [ /* see node checklist */ ],
  "connections": { /* name-keyed graph */ },
  "settings": { "executionOrder": "v1" }
}
```

### 2.2 Include when matching live export fidelity

| Field | When |
|-------|------|
| `active` | `false` for draft imports; never assume deploy |
| `meta` | `{ "templateCredsSetupCompleted": true }` optional |
| `tags` | When operator uses i-SEO / MetaBOT tags |

### 2.3 Always omit in synthetic JSON

| Field | Reason |
|-------|--------|
| `id`, `versionId`, `activeVersionId` | n8n assigns / version history |
| `createdAt`, `updatedAt`, `triggerCount`, `versionCounter` | n8n-managed |
| `pinData` | Debug-only; causes stale execution state |
| `shared`, `activeVersion`, `workflowPublishHistory` | API export artifacts |
| `staticData` with live user data | Runtime state — Intake export contained legacy jobs |
| Literal secrets in any field | Security policy |

---

## 3. Credentials

| Rule | Detail |
|------|--------|
| **Never** embed tokens, OAuth secrets, or API keys | Use n8n credential types |
| In committed JSON | Omit `credentials` or document `"credentials": "<bind in UI>"` in companion note — do not copy `REDACTED_CREDENTIAL` into import files intended for live use |
| Shape in live exports | `{ "telegramApi": { "id": "...", "name": "..." } }` — operator re-selects after import |
| OpenRouter | HTTP Request Authorization header bound via credential or expression — redacted in sanitizer |
| Google Sheets | `googleSheetsOAuth2Api` credential reference on every Sheets node |

**After import:** operator opens each node with credential warning and selects existing credential.

---

## 4. webhookId

| Node types | Rule |
|------------|------|
| `telegramTrigger`, `telegram`, `webhook` | **Omit** in synthetic JSON |
| On import | n8n generates new webhookId on save/activate |
| Risk | Duplicated webhookId across workflows breaks Telegram/webhook routing |

If copying a node verbatim from export for **local diff only**, strip `webhookId` before import.

---

## 5. Node IDs

| Approach | Guidance |
|----------|----------|
| Fresh workflow | Omit `id` — n8n assigns UUIDs |
| Partial fragment merge | Generate new UUID v4 per node to avoid collisions |
| Copy-paste from export | IDs may be kept if importing into **new** workflow on same instance — **SAFE UNKNOWN** collision behavior; prefer new IDs |

Connections use **names**, not IDs — node `id` changes are safe if names stable.

---

## 6. versionId and timestamps

Omit all version/timestamp fields. n8n sets them on save. Including stale `versionId` from export may confuse version history — not observed as import blocker but unnecessary.

---

## 7. Connections validity

1. Every connection key must match a `nodes[].name` exactly (case-sensitive).  
2. Every `node` target in connections must exist in `nodes`.  
3. IF nodes: provide **two** `main` branches (use `[]` for empty branch).  
4. Switch nodes: `main.length` === `rules.values.length`.  
5. Only `"main"` output channel used in v14 — do not invent `"error"` channels unless node type requires it.  
6. Target `index` is usually `0`.  

**Validation script (local):**

```bash
node -e "
const w = require('./workflow.json');
const names = new Set(w.nodes.map(n => n.name));
for (const [src, outs] of Object.entries(w.connections)) {
  if (!names.has(src)) console.error('Missing source:', src);
  for (const branch of outs.main || [])
    for (const t of branch)
      if (!names.has(t.node)) console.error('Missing target:', t.node, 'from', src);
}
"
```

---

## 8. Canvas layout (position)

| Rule | Detail |
|------|--------|
| Format | `[x, y]` integers |
| v14 Intake | Large coordinates (~10000, ~23500) — legacy canvas offset |
| v14 Worker | Negative coordinates (~-6000, ~-700) |
| New nodes | Place relative to neighbors; ±220px horizontal, ±180px vertical spacing |
| Avoid | All nodes at `[0,0]` — import works but unreadable canvas |

MetaBOT Developer should preserve relative layout when modifying existing exports.

---

## 9. typeVersion compatibility

Copy `typeVersion` from [n8n-node-type-catalog-v14.md](n8n-node-type-catalog-v14.md). Wrong version causes:

- missing parameter fields in UI  
- import validation errors  
- silent parameter drops  

After n8n upgrade, re-export one workflow and diff typeVersions before bulk generation.

---

## 10. Expression syntax safety

| Do | Don't |
|----|-------|
| `={{ $json.field }}` | `$json.field` without `=` prefix in expression fields |
| `={{ $('Node Name').first().json.x }}` | `$node["Node Name"]` (not used in v14) |
| `={{ String($json.flag) }}` for IF string compare | Compare boolean to string without coercion |
| `={{ JSON.stringify($json.payload) }}` for HTTP body | Raw object in `jsonBody` without stringify |
| Escape `\n` in JSON strings | Unescaped newlines breaking JSON |

**Code nodes:** plain JavaScript — no `={{ }}` wrapper inside `jsCode`.

---

## 11. Code node output

Required return shape:

```javascript
return [{ json: { key: value } }];
```

Multi-item:

```javascript
return items.map(item => ({ json: { ...item.json, extra: true } }));
```

Passthrough:

```javascript
return [items[0]];
```

---

## 12. Partial fragments vs full workflows

| Artifact type | Minimum contents | Use case |
|---------------|------------------|----------|
| **Full workflow** | name, nodes, connections, settings | New workflow import |
| **Subgraph fragment** | nodes[] + connections{} subset | Documentation / merge guide — **not** directly importable alone |
| **Single node patch** | one node object + connection deltas | Operator manual paste or merge tool |

For fragments: provide merge instructions listing anchor node names for connection rewiring.

**Cross-workflow edits:** Intake handoff URLs and Worker webhook paths must stay consistent — edit both or neither.

---

## 13. Pre-import testing

| Step | Action |
|------|--------|
| 1 | JSON.parse validation locally |
| 2 | Connection name reference check (script above) |
| 3 | Secret pattern scan (no `sk-`, Bearer tokens, bot tokens) |
| 4 | typeVersion catalog cross-check |
| 5 | Import into **inactive** workflow on n8n (operator) |
| 6 | Bind credentials without activating |
| 7 | Visual canvas inspection — all nodes wired |
| 8 | Single test execution with pinned sample payload (operator) |
| 9 | Compare node count / connection count to source export |

MetaBOT Developer stops at step 4 unless operator charters live import test.

---

## 14. n8n version / compatibility

| Signal | Observed |
|--------|----------|
| Exact n8n semver | **SAFE UNKNOWN** — not in export |
| `settings.executionOrder` | `"v1"` |
| IF condition schema version | 1 or 3 in options |
| Node typeVersions | See catalog — mixed 1.x–4.x suggests n8n 1.x era instance |
| API export shape | Includes `activeVersion`, `shared` — newer API format |

**Do not overclaim.** Verify after operator n8n upgrade with fresh `--report-only` export.

---

## 15. Future training corpus policy

### 15.1 When to export fresh examples

- Before any bulk JSON generation session  
- After n8n version upgrade  
- After operator deploys workflow changes to Intake/Worker/Admin  
- When import failure occurs — capture failing JSON + corrected export  

### 15.2 Sanitization

Use read-only exporter:

```bash
node projects/metabot-seo-content-agent/integrations/n8n-readonly-exporter/export-workflows.mjs --export --date YYYY-MM-DD
```

Review `SANITIZATION-REPORT.md` before commit. Never commit `raw/`.

### 15.3 Adding node grammar examples

1. Add row to `n8n-node-type-catalog-v14.md` with typeVersion + parameter shape  
2. Add cross-reference in `n8n-workflow-json-grammar-v1.md` if new pattern (connections, expressions)  
3. Update evidence folder `NODE-INVENTORY-v14.md` only via exporter manifest regen — do not hand-edit inventory unless exporter unavailable  

### 15.4 Recording import failures

Create operator-local note (or `projects/metabot-seo-content-agent/evidence/import-failures/YYYY-MM-DD-<summary>.md`):

- failing JSON excerpt (sanitized)  
- n8n error message  
- root cause (wrong typeVersion, connection name typo, etc.)  
- fix applied  

### 15.5 Generated vs exported diff

Before operator import approval:

1. Export current live workflow  
2. Diff node names, types, typeVersions, connections keys  
3. Flag unintended node renames or dropped branches  

### 15.6 Reference grammar maintenance

| File | Owner lane | Update trigger |
|------|------------|----------------|
| `metabot-developer/n8n-workflow-json-grammar-v1.md` | MetaBOT Developer | New cross-cutting pattern |
| `metabot-developer/n8n-node-type-catalog-v14.md` | MetaBOT Developer | New node type or typeVersion change |
| `metabot-developer/n8n-import-safe-generation-rules-v1.md` | MetaBOT Developer | Import failure lesson |
| `exports/live-v14-evidence/YYYY-MM-DD/` | Exporter tool | Scheduled / post-deploy export |

Bump `-v1` → `-v2` only on breaking grammar change (e.g. new required top-level field).

### 15.7 n8n upgrades

1. Operator upgrades n8n instance  
2. Run exporter dry-run + report-only  
3. Compare typeVersions and parameter shapes  
4. Update catalog matrix  
5. Re-test one import of sanitized JSON in staging  
6. Document **SAFE UNKNOWN** until verified  

---

## 16. Quick reference — generation DO / DON'T

| DO | DON'T |
|----|-------|
| Key connections by node name | Key by node id |
| Match catalog typeVersions | Use latest typeVersion from internet docs |
| Build LLM payloads in Code nodes | Embed prompts with API keys in HTTP node |
| Omit webhookId, pinData, secrets | Copy webhookId from old export |
| Use `$('Exact Name')` in expressions | Guess node names after rename |
| Provide operator credential binding checklist | Commit credential IDs as truth |
| Test JSON.parse + connection graph locally | Deploy unvalidated JSON to active workflow |

---

*MetaBOT Developer · import-safe generation rules · evidence 2026-07-10*
