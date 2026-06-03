# MIG — Task File Intake Drop Zone

**Purpose:** First production intake path for MIG — human, agent, ORCA, Website Factory, or future MARS runtime submit **Research Requests** as JSON files.

**Status:** v0.1 operational drop zone + human-invoked processor. **Not** a daemon, **not** Telegram, **not** MARS Bridge.

**Canonical intake object:** Research Request per [projects/mig/contracts/mig-research-request-contract-v0.md](../../projects/mig/contracts/mig-research-request-contract-v0.md).

**Processor:** [projects/mig/lib/task-file-adapter/](../../projects/mig/lib/task-file-adapter/) — run via [projects/mig/tools/run-task-file-adapter.ps1](../../projects/mig/tools/run-task-file-adapter.ps1).

---

## Folder map

| Path | Operational state | Meaning |
|------|-------------------|---------|
| `requests/` | `received` | Drop new `request-<request_id>.json` here |
| `processing/` | `processing` | Adapter claimed file; Runtime MVP running |
| `completed/` | `completed` | Terminal success + `*.outcome.json` sidecar |
| `failed/` | `failed` / `rejected` | Terminal failure + `*.error.json` sidecar |
| `archive/` | `archived` | Operator-retained copies after review |
| `registry/` | — | `request-index.json` — request ↔ session linkage |

---

## Operator rules

1. **One request per file** — filename `request-<request_id>.json` where `request_id` matches the `request_id` field inside the file (or omit field; adapter generates before processing).
2. **Do not edit** files in `processing/`, `completed/`, or `failed/` — adapter owns moves.
3. **Examples** — files prefixed `example-` are never processed automatically.
4. **Run processor** after drop: `.\projects\mig\tools\run-task-file-adapter.ps1` (human-supervised).
5. **No secrets** in request files — credentials belong in env / n8n only.

---

## Flow

```text
requests/request-<id>.json
        ↓  (normalize → validate)
processing/request-<id>.json
        ↓  (runMigSession — Runtime MVP)
projects/mig/sessions/{session_id}/
        ↓  session_manifest.json v0.2 + research_pack.draft.md
completed/request-<id>.json + request-<id>.outcome.json
```

---

## Related

- Adapter spec: [projects/mig/contracts/mig-task-file-adapter-spec-v0.1.md](../../projects/mig/contracts/mig-task-file-adapter-spec-v0.1.md)
- Example request: [requests/example-request-serp-capture-v0.1.json](requests/example-request-serp-capture-v0.1.json)
- ORCA submission example: [projects/mig/examples/orca-research-request-submission-v0.1.json](../../projects/mig/examples/orca-research-request-submission-v0.1.json)
