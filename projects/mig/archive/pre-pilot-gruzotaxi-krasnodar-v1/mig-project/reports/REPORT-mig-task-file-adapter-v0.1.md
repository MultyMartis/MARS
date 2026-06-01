# REPORT — MIG Task File Adapter v0.1

**Date:** 2026-06-01  
**Lane:** A — MIG Intake  
**Status:** Architecture + v0.1 implementation (human-invoked processor). **Not** committed per task charter.

---

## Executive Summary

**Task File Adapter** утверждён как **первый production intake path** для MIG: оператор, агент, ORCA, Website Factory или будущий MARS runtime кладут JSON в `incoming/mig/requests/`, затем запускают `run-task-file-adapter.ps1`. Адаптер нормализует файл в **canonical Research Request**, валидирует, прогоняет **Session Spine v0.1**, пишет сессию в `projects/mig/sessions/{session_id}/` и фиксирует связку `request_id` ↔ `session_id` в `incoming/mig/registry/request-index.json`.

Рекомендованная модель исполнения для текущей реальности MARS: **вариант A (Node.js one-shot)** сейчас, **гибрид D** позже (n8n poll на VPS). Telegram, MARS Bridge, OpenRouter и n8n workflow generation **вне scope**.

---

## Recommended Architecture

```text
Submitter (human / ORCA / agent / future runtime)
        │
        ▼
incoming/mig/requests/request-<request_id>.json
        │
        ▼
┌───────────────────────────────┐
│  MIG Task File Adapter v0.1   │
│  normalize → validate         │
│  duplicate check → registry   │
└───────────────┬───────────────┘
                ▼
        Canonical Research Request
                ▼
        canonicalToSpineFlat()
                ▼
        runSessionSpine()  (existing lib)
                ▼
projects/mig/sessions/{session_id}/
  session_manifest.json
  serp_result.json
  research_pack.draft.md
                ▼
incoming/mig/completed/ + *.outcome.json
registry/request-index.json
```

**Принцип (утверждён):** Research Request = canonical intake; Task File = первый адаптер; транспорт не смешивается с сессией.

---

## Folder Structure

| Path | Purpose |
|------|---------|
| `incoming/mig/` | Root drop zone + [README](../../../incoming/mig/README.md) |
| `incoming/mig/requests/` | New submissions (`received`) |
| `incoming/mig/processing/` | Claimed in-flight |
| `incoming/mig/completed/` | Success + outcome sidecars |
| `incoming/mig/failed/` | Errors + `*.error.json` |
| `incoming/mig/archive/` | Operator retention (manual) |
| `incoming/mig/registry/` | `request-index.json` |

Структура **валидирована** против паттернов `incoming/orca-*` и OCPilot quarantine — временная зона, human gate, не SoT для артефактов исследования (SoT = session folder).

---

## Naming Rules

**Выбор: `request-<request_id>.json`**

| Вариант | Оценка |
|---------|--------|
| `request-<request_id>.json` | **Best** — idempotency, registry key, audit, соответствие контракту |
| `request-<timestamp>.json` | Плохо — коллизии, слабая связь с логами |
| `request-<slug>.json` | Допустимо только если slug **равен** `request_id` |

Дополнительно:

- Префикс `example-` — **никогда** не обрабатывается сканером.
- Имя файла **обязано** совпадать с полем `request_id` (иначе `FILENAME_MISMATCH`).

Рекомендуемый `request_id`: `req-YYYYMMDD-{hex6}` (генерируется адаптером, если поле отсутствует — но тогда оператор должен переименовать файл перед drop или указать id заранее).

---

## Request Lifecycle

### Logical (Research Request contract)

`submitted` → `validated` → (`session_bound` + `executing` collapsed) → `completed`  
Ветки: `failed`, `rejected` (валидация / duplicate / unsupported type).

### Operational (folders)

| Phase | Folder | Exit |
|-------|--------|------|
| Drop | `requests/` | Adapter claim → `processing/` |
| Execute | `processing/` | Spine OK → `completed/`; else → `failed/` |
| Review | `completed/` | Operator → `archive/` (manual) |

**Archive strategy:** v0.1 — только ручное перемещение в `archive/` после проверки outcome/manifest; автоматический TTL — Build Later.

**Duplicate handling:** registry entry **или** одноимённый файл в `processing`/`completed`/`failed` → `DUPLICATE_REQUEST`, файл в `failed/`.

---

## Adapter Responsibilities

См. [mig-task-file-adapter-spec-v0.1.md](../contracts/mig-task-file-adapter-spec-v0.1.md) и реализацию [../lib/task-file-adapter/](../lib/task-file-adapter/).

Кратко:

1. Scan `requests/request-*.json`
2. Parse → normalize (canonical или legacy flat)
3. Validate contract + filename
4. Duplicate check
5. Move → `processing/`
6. `runSessionSpine(canonicalToSpineFlat())`
7. Move → `completed/` + `*.outcome.json` + `.canonical.json`
8. Update `request-index.json`

---

## Failure Model

| Class | Code | Destination | Visibility |
|-------|------|-------------|------------|
| Invalid JSON | `INVALID_JSON` | `failed/` | `*.error.json` |
| Bad shape | `UNRECOGNIZED_SHAPE` | `failed/` | sidecar |
| Contract | `VALIDATION_ERROR` | `failed/` | sidecar + `details` |
| Filename | `FILENAME_MISMATCH` | `failed/` | sidecar |
| Duplicate | `DUPLICATE_REQUEST` | `failed/` | sidecar + registry |
| Spine | `VALIDATION_ERROR` / `SESSION_SPINE_ERROR` | `failed/` | sidecar |
| FS | `ADAPTER_ERROR` | best-effort | stderr |

**Operator visibility:** JSON sidecars в `failed/` и stdout summary от `process-inbox.js`; registry всегда отражает последний терминальный статус.

---

## State Model

| Canonical (subset v0.1) | Operational folder | Notes |
|-------------------------|-------------------|-------|
| `submitted` | `requests/` | File waiting |
| `validated` | (transient) | In-process only |
| `executing` | `processing/` | Spine running |
| `completed` | `completed/` | Terminal OK |
| `failed` / `rejected` | `failed/` | Terminal error |
| `archived` | `archive/` | Manual |

Полные состояния `draft`, `accepted` отдельно от сессии — **Build Later** (v0.2+).

---

## Execution Model

| Option | Recommendation |
|--------|----------------|
| **A. Node.js one-shot** | **v0.1 — да** (`process-inbox.js`, PS1 wrapper) |
| B. n8n polling | Later — когда Intake workflow на VPS |
| C. n8n webhook + helper | Later — не нужен для repo-local drop |
| **D. Hybrid** | **Целевой:** A в dev/repo; B по cron на VPS |

**Обоснование:** Session Spine уже Node; операторский HITL; нет доказанного always-on watcher в MARS repo; MetaBOT pattern (Intake dispatch) применим позже без смены файлового контракта.

---

## Filesystem Contract

| Object | Location | Link |
|--------|----------|------|
| Request transport | `incoming/mig/requests/request-<id>.json` | `source.transport_ref` |
| Registry | `incoming/mig/registry/request-index.json` | `entries[request_id].session_id` |
| Session SoT | `{MIG_SESSION_ROOT}/<session_id>/` | `outcome.json` → `folder_path` |
| Draft pack | `.../research_pack.draft.md` | manifest `artifacts` |

**request_id ≠ session_id** by design (contract §9). Spine генерирует `session_id` внутри `validateIntake()`.

---

## ORCA Compatibility

ORCA (или скрипт фабрики) пишет **тот же** canonical JSON в `incoming/mig/requests/`:

- Допустим `downstream_context.orca_project_id` — адаптер игнорирует семантику, сохраняет в canonical snapshot при успехе.
- `source.adapter` принудительно `task_file` (не `orca` отдельным адаптером) — ORCA не получает отдельный код-путь.

Демо: [orca-research-request-submission-v0.1.json](../examples/orca-research-request-submission-v0.1.json) — копировать как `request-req-20260601-orca-demo.json` для прогона.

**Без изменения адаптера:** ORCA не вызывает spine напрямую; не утверждает pack.

---

## Build Now

| Deliverable | Path |
|-------------|------|
| Drop zone | `incoming/mig/**` |
| Adapter implementation | `projects/mig/lib/task-file-adapter/` |
| Spec | `projects/mig/contracts/mig-task-file-adapter-spec-v0.1.md` |
| Runner | `projects/mig/tools/run-task-file-adapter.ps1` |
| Examples | `incoming/mig/requests/example-*.json`, `projects/mig/examples/orca-*.json` |
| This report | `projects/mig/reports/REPORT-mig-task-file-adapter-v0.1.md` |
| OPERATIONAL-INDEX entry | updated |

---

## Build Later

- fs.watch / Windows scheduled task / VPS cron
- n8n «Poll MIG inbox» node in MIG Intake workflow
- Google Sheets lock registry (runtime design)
- Отдельный persisted `research_request.json` per session
- YAML intake
- MARS Bridge adapter (extract payload → same drop or direct normalize)
- Telegram Adapter
- Auto-archive retention
- Types: `groundtruth_run`, `session_resume`, …

---

## Risks

| Risk | Mitigation |
|------|------------|
| Operator forgets to run processor | Document in README + OPERATIONAL-INDEX; Later: n8n poll |
| Duplicate re-drop | Registry + filename collision → `failed/` |
| `request_id` / filename drift | Hard `FILENAME_MISMATCH` |
| Encoding in queries (Windows) | Existing spine risk; not introduced by adapter |
| Registry manual edit | Human charter; not automated repair |
| Scope creep to Bridge/Telegram | Explicit non-goals in charter |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Production `MIG_SESSION_ROOT` on VPS | Operator-configured; design uses env |
| n8n poll interval / credentials | Not implemented |
| JSON Schema registry file for Research Request | Contract v0 text only |
| Automated archive retention policy | Not defined |
| Whether Website Factory will use same path vs CI copy | Submitter convention only |

---

## Recommended Next Step

1. Operator: copy [example-request-serp-capture-v0.1.json](../../../incoming/mig/requests/example-request-serp-capture-v0.1.json) → `request-req-<newid>.json` (уникальный id).
2. Run: `.\projects\mig\tools\run-task-file-adapter.ps1`
3. Verify: `completed/*.outcome.json`, session folder, registry entry.
4. When VPS ready: add n8n poll branch **without** changing drop-zone contract (Hybrid D).

---

## Changed files (this task)

- `incoming/mig/**` (drop zone)
- `projects/mig/lib/task-file-adapter/**`
- `projects/mig/contracts/mig-task-file-adapter-spec-v0.1.md`
- `projects/mig/reports/REPORT-mig-task-file-adapter-v0.1.md`
- `projects/mig/tools/run-task-file-adapter.ps1`
- `projects/mig/examples/orca-research-request-submission-v0.1.json`
- `projects/mig/OPERATIONAL-INDEX.md` (entry)
