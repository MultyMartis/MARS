# MIG Task File Adapter — Specification v0.1

**Status:** **implemented** (human-invoked Node.js processor).  
**Not:** Telegram intake, MARS Bridge, n8n workflow, API server, or background daemon.

**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md)  
**Implementation:** [../lib/task-file-adapter/](../lib/task-file-adapter/)  
**Drop zone:** [../../../incoming/mig/README.md](../../../incoming/mig/README.md)

---

## 1. Purpose

The Task File Adapter is the **first production intake path** for MIG. Any submitter drops a JSON file; a human-supervised processor normalizes it to a **canonical Research Request**, runs **`runMigSession` (Runtime MVP)**, and records linkage in the inbox registry.

```text
request file (transport)
    → normalize → validate
    → Research Request (canonical)
    → runMigSession (Runtime MVP)
    → projects/mig/sessions/{session_id}/
    → completed + outcome sidecar + registry
```

---

## 2. Responsibilities

| Step | Owner | Action |
|------|-------|--------|
| Watch / poll | Operator + `process-inbox.js` | v0.1: **single-pass scan** on invoke; no OS watcher |
| Read file | Adapter | UTF-8 JSON from `incoming/mig/requests/` |
| Validate schema | Adapter | Canonical contract + filename ↔ `request_id` |
| Normalize | Adapter | Canonical or legacy flat → Research Request; `source.adapter=task_file` |
| Claim file | Adapter | Move to `processing/` |
| Run runtime | Adapter | Canonical Research Request → `runMigSession()` |
| Write outputs | Runtime MVP | `session_manifest.json` **v0.2**, `serp_result.json`, `competitors.json`, `research_pack.draft.md` |
| Terminal move | Adapter | `completed/` or `failed/` + sidecar |
| Manifest / registry | Adapter | `incoming/mig/registry/request-index.json` |

---

## 3. Folder structure

| Path | State(s) |
|------|----------|
| `incoming/mig/requests/` | `received` |
| `incoming/mig/processing/` | `processing` |
| `incoming/mig/completed/` | `completed` |
| `incoming/mig/failed/` | `failed`, `rejected` |
| `incoming/mig/archive/` | `archived` (operator manual) |
| `incoming/mig/registry/` | index (not a lifecycle folder) |

---

## 4. Naming rules

**Normative filename:** `request-<request_id>.json`

| Pattern | Verdict |
|---------|---------|
| `request-<request_id>.json` | **Required** for auto-processing |
| `request-<timestamp>.json` | **Reject** unless timestamp equals `request_id` |
| `request-<slug>.json` | **Accept** if slug equals `request_id` |
| `example-*.json` | **Excluded** from scan |

`request_id` pattern: start alphanumeric; max 128 chars; recommended `req-YYYYMMDD-{hex6}`.

---

## 5. Request lifecycle

### Contract states (logical)

`draft` → `submitted` → `validated` → `accepted` → `session_bound` → `executing` → `completed`

v0.1 adapter **collapses** acceptance and binding into one `runMigSession()` call (Runtime MVP per Research Request contract §10).

### Operational states (filesystem)

| Operational | Folder | Contract mapping |
|-------------|--------|------------------|
| `received` | `requests/` | `submitted` (file dropped) |
| `processing` | `processing/` | `validated` → `executing` |
| `completed` | `completed/` | `completed` |
| `failed` | `failed/` | `failed` or `rejected` |
| `archived` | `archive/` | operator archive |

---

## 6. Failure model

| Failure | Code | File move | Operator visibility |
|---------|------|-----------|------------------------|
| Invalid JSON | `INVALID_JSON` | → `failed/` | `request-<id>.error.json` |
| Unrecognized shape | `UNRECOGNIZED_SHAPE` | → `failed/` | error sidecar |
| Validation | `VALIDATION_ERROR` | → `failed/` | error sidecar + `details[]` |
| Filename mismatch | `FILENAME_MISMATCH` | → `failed/` | error sidecar |
| Duplicate `request_id` | `DUPLICATE_REQUEST` | → `failed/` | error sidecar + registry entry |
| Unsupported type | `VALIDATION_ERROR` | → `failed/` | only `serp_capture` and `groundtruth_run` in v0.1 |
| Spine failure | `VALIDATION_ERROR` / `RUNTIME_SESSION_FAILED` | → `failed/` | error sidecar |
| Filesystem error | `ADAPTER_ERROR` | best-effort | stderr JSON |

**No automatic retry** in v0.1 — operator fixes file or clears registry entry under human charter, then re-drops.

---

## 7. Execution model (v0.1 decision)

| Option | v0.1 |
|--------|------|
| A. Pure Node.js one-shot | **Selected** — `node process-inbox.js` / PowerShell wrapper |
| B. n8n polling | Build Later |
| C. n8n webhook + helper | Build Later |
| D. Hybrid | **Target** — A now; B on VPS when operator schedules |

**Rationale:** Runtime MVP is already Node.js; MARS repo work is human-supervised; Windows-friendly; matches OCPilot/ORCA **drop + human gate** pattern without requiring always-on watcher.

---

## 8. Filesystem contract

### Request file

- Canonical Research Request JSON (`schema_version: "0"`) **or** legacy flat (spine fields).
- Written by submitter; adapter never mutates source in `requests/` except move.

### Supported `request_type` values (v0.1)

| Type | Adapter | Runtime MVP |
|------|---------|-------------|
| `serp_capture` | **Accepted** | Single-query SERP capture → draft pack |
| `groundtruth_run` | **Accepted** | Website + landing passes when `capture_profile` requires |

Other contract types (`pack_retrieval`, `session_resume`, `competitor_discovery`, …) remain **unsupported** by the Task File Adapter in v0.1 → `VALIDATION_ERROR`.

### Session folder

`{MIG_SESSION_ROOT}/{session_id}/`:

- `session_manifest.json`
- `serp_result.json`
- `research_pack.draft.md`

### Adapter artifacts

| Artifact | Location |
|----------|----------|
| Completed request copy | `completed/request-<id>.json` |
| Outcome sidecar | `completed/request-<id>.outcome.json` |
| Canonical snapshot | `completed/<request_id>.canonical.json` |
| Error sidecar | `failed/request-<id>.error.json` |
| Registry entry | `registry/request-index.json` → `entries[request_id]` |

### Linkage

```json
{
  "request_id": "req-20260601-a1b2c3",
  "session_id": "mig-20260601-abcdef",
  "folder_path": "C:\\AI MARS\\projects\\mig\\sessions\\mig-20260601-abcdef",
  "status": "completed"
}
```

---

## 9. ORCA compatibility

ORCA (or any upstream) **only** drops the same JSON into `incoming/mig/requests/` with optional `downstream_context.orca_project_id`. Adapter code **unchanged**. See [../examples/orca-research-request-submission-v0.1.json](../examples/orca-research-request-submission-v0.1.json).

ORCA still consumes **approved** packs per handoff contract — not Research Requests.

---

## 10. Build Now vs Build Later

### Build Now

- Drop-zone tree + README
- Adapter spec (this document)
- `normalize-request`, `validate-canonical`, `process-inbox`
- Registry index file
- PowerShell runner
- Example + ORCA demo JSON

### Build Later

- fs.watch / scheduled daemon
- n8n Intake poll branch
- Separate request persistence file per session
- `accepted` / lock registry (Sheets)
- YAML support
- Auto-archive retention job
- MARS Bridge adapter

---

## Related

- [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md)
- [REPORT-mig-task-file-adapter-v0.1.md](../reports/REPORT-mig-task-file-adapter-v0.1.md)
