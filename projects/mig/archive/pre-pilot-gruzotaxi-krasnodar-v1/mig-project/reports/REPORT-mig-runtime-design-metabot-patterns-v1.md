# REPORT — MIG Runtime Design Based On MetaBOT Patterns

**Status:** Design only — no implementation, no workflow exports, no deployment.  
**Source of truth:** [MIG n8n Infrastructure Discovery](91daad8c-fcd9-4002-acd2-d09b92ee02e2) (agent transcript); exports under `incoming/metabot/seo-writer-workflows/`; MIG v0.1 session spine in `projects/mig/lib/session-spine/`.  
**Date:** 2026-05-31  
**Lane:** A — MIG Runtime Design

---

## Executive Summary

Первый production-oriented **MIG runtime** должен быть **гибридом (вариант C из discovery)**: те же VPS, тот же self-hosted n8n (`n8n.ai-metacode.com`), тот же оператор, те же экосистемы **Telegram**, **OpenRouter** и **Google Sheets** — но **отдельное семейство workflow** с namespaced webhook-путями `mig/*`, без встраивания в SEO Content Agent graphs.

Минимальное семейство workflow — **три** (Intake / Worker / Admin), как у MetaBOT v14. Связь — **Webhook → Webhook**, не `Execute Workflow`. Черновик `MIG — Research Session v0.1` (монолитный webhook + filesystem) остаётся **библиотекой spine**, но **не** целевой production-формой: его логика переезжает в **MIG Worker**; Intake получает Telegram; Admin — ops-слой.

**Primary output:** Research Pack как системный объект с жизненным циклом `draft → review → approved → consumed → archived`.  
**Storage:** filesystem — источник истины для артефактов сессии; Google Sheets — реестр сессий, locks, operator-visible history (адаптация `seo_active_jobs` / `memory`, не слепое копирование).  
**OpenRouter:** только в Worker, только на этапах синтеза/обогащения — не на сыром SERP capture в Phase 1.  
**ORCA:** контрактный human handoff — approved pack + manifest; ORCA **никогда** не пишет в MIG storage и не запускает capture.

Discovery зафиксировал **SECURITY RISK** (inline OpenRouter key в SEO Worker export). MIG design **требует** n8n credentials / `$env`, не повторяет anti-pattern.

---

## Recommended Workflow Family

### Решение: три workflow + опциональный четвёртый позже

| Workflow | Phase 1 | Обоснование |
|----------|---------|-------------|
| **MIG Intake** | **Да** | MetaBOT v14: единственная точка Telegram, lock gate, fire-and-forget dispatch. Без Intake оператор теряет проверенный UX (busy, ack, routing). |
| **MIG Worker** | **Да** | Вся тяжёлая работа: SERP spine, draft pack, OpenRouter, Sheets updates, status edits, chunk delivery. |
| **MIG Admin** | **Да** | Battle-tested ops: locks, health, stop/cancel. MIG sessions дольше и дороже SEO run — ops surface обязателен. |
| **MIG Export / File** | **Нет в Phase 1** | MetaBOT docs упоминают future File Export workflow. Для MIG Phase 1 достаточно Telegram + filesystem paths; export workflow — Phase 4+. |

### Почему не меньше двух

- **Monolith webhook** (текущий v0.1) не даёт async UX, lock per chat, admin isolation — всё это доказано в MetaBOT production.
- Слияние Admin в Worker **увеличивает** blast radius и усложняет health checks (MetaBOT держит Admin отдельно).

### Почему не больше трёх в Phase 1

- Discovery: `Execute Workflow` **не используется** — лишние workflow без отдельного trigger/path только добавляют drift.
- SERP provider, competitor, landing — **маршруты внутри Worker** (`Route Command` pattern), не отдельные n8n workflow.

### Именование и webhook convention (design)

| Workflow | Trigger | Outbound webhook path (design) |
|----------|---------|--------------------------------|
| MIG Intake | Telegram Trigger (`message`) | → `POST …/webhook/mig-worker` |
| MIG Worker | Webhook `POST mig-worker` | Telegram, Sheets, FS, OpenRouter |
| MIG Admin | Webhook `POST mig-admin` | ← Intake admin commands |

**Не смешивать** с `seo-content-agent-worker` / `seo-content-agent-admin`. Общий только **host + credential store**.

### Связь с v0.1 spine

`projects/mig/lib/session-spine/*` — **shared library** (Code nodes в Worker, тот же контракт `session_manifest.json` / `serp_result.json` / `research_pack.draft.md`). Монолитный export `mig-research-session-v0.1.json` — **deprecated as production shape** после внедрения трёхслойной схемы.

---

## MIG Intake Design

### Purpose

Telegram-шлюз оператора: парсинг команд, concurrency lock, немедленный UX (ack / busy / help), dispatch в Worker или Admin через HTTP POST. **Не** выполняет SERP, **не** вызывает OpenRouter.

### Inputs

| Source | Content |
|--------|---------|
| Telegram | `message` (text commands, optional brief body) |
| Google Sheets | Active lock lookup (`mig_active_sessions`) |
| Operator context | `chat_id`, `user_id`, `username`, names |

### Outputs

| Target | Content |
|--------|---------|
| Worker webhook | Payload envelope (см. ниже) |
| Admin webhook | Admin envelope |
| Telegram | Instant replies: start, help, busy, accepted |
| Google Sheets | Lock row create (before Worker) |

**Worker payload envelope (reuse MetaBOT shape):**

```json
{
  "message": { },
  "lock": { "lock_key", "session_id", "chat_id", "user_id", "username", ... } | null,
  "status_message": { "chat_id", "message_id" }
}
```

Дополнительно для MIG: `intake_parsed` — ниша, регион, seed query, flags (`--strict`, `--from-session`, …) после Code node `Detect MIG Command`.

### External services

- Telegram Bot API (MIG bot — **отдельный** от SEO bot или shared bot с namespace команд — **SAFE UNKNOWN**, operator choice; design prefers **dedicated `/mig` command prefix** to avoid collision with `/run`).
- Google Sheets — lock registry only (Intake).
- HTTP — same-host webhook POST.

### Human interaction

- Operator sends commands; Intake never blocks on Worker completion.
- Local commands (`/mig start`, `/mig help`) answered in Intake.
- Research commands (`/mig serp`, `/mig run`, `/mig status`) → Worker.

### Storage interaction

- **Sheets:** append lock `status=active`, `session_id=pending|assigned`, `expires_at=+TTL`.
- **Filesystem:** none in Intake.

### Failure handling

| Failure | Behavior |
|---------|----------|
| Busy lock | «⏳ У вас уже выполняется сессия» (reuse MetaBOT copy pattern) |
| Sheets unreachable | Fail closed — do not dispatch Worker; Telegram error |
| Worker webhook HTTP fail | Telegram: «⚠️ Не удалось запустить сессию»; Intake attempts lock rollback (**design gap fix** — MetaBOT export unclear on rollback) |
| Invalid command | Unknown command template in Intake |

---

## MIG Worker Design

### Purpose

Единственный исполнитель research session: validate intake → manifest → capture/normalize SERP → draft Research Pack → optional OpenRouter enrichment → persist artifacts → update Sheets registry → Telegram progress + result.

### Inputs

| Source | Content |
|--------|---------|
| Worker webhook | Intake envelope + `intake_parsed` |
| Filesystem | Existing session dir for resume/`--from` |
| SERP provider / manual / fallback | Per phase (Phase 1: fallback + manual stub) |
| Google Sheets | Session registry row, prior memory (Phase 2+) |

### Outputs

| Artifact | Location |
|----------|----------|
| `session_manifest.json` | `{MIG_SESSION_ROOT}/{session_id}/` |
| `serp_result.json` | same |
| `research_pack.draft.md` | same |
| `research_pack.review.md` | optional human edit target |
| `research_pack.approved.md` | after human approval |
| Sheets row | status, stage, paths, timestamps |
| Telegram | status edits + chunked summary / pack pointer |

### External services

- **Filesystem** (primary) — via session-spine library; VPS path aligned with `MIG_SESSION_ROOT` (discovery: v0.1 uses `C:/AI MARS/projects/mig/sessions` — production path **operator-configured**, not hardcoded in design).
- **Google Sheets** — session registry + optional memory index (not full pack body).
- **OpenRouter** — selective stages (see OpenRouter Architecture).
- **Telegram** — `editMessageText` on `status_message_id`, final chunked delivery.
- **SERP provider** — Phase 2+ HTTP; Phase 1 spine only.

### Human interaction

- Async: operator watches status line (Collecting → Normalizing → Drafting → …).
- `/mig get {session_id}` — retrieval route inside Worker (MetaBOT `/get` pattern).
- Approval **не** в Worker auto — transitions to `review` / `approved` via explicit operator command or Admin-assisted flow (Phase 1: manual file + command).

### Storage interaction

- Create session dir early (after validation).
- Write artifacts atomically per spine `writeArtifacts`.
- Update manifest `stage` field on each transition.
- Sheets: update `stage`, `finished_at`, `pack_state`, `folder_path`.

### Failure handling

| Failure | Behavior |
|---------|----------|
| Validation error | Respond error JSON if sync caller; else Telegram + no lock close |
| SERP provider fail | Fallback mode + `safe_unknown[]` in manifest (v0.1 proven) |
| OpenRouter fail | Stage `failed_llm`; Telegram explicit error; manifest records failure (**design improvement** over MetaBOT gap) |
| Partial write | Do not mark `draft_complete`; lock remains until Admin cancel |
| Memory/Sheets append | `continueOnFail` pattern (reuse MetaBOT Worker) — FS is SoT |

**Route types (Worker internal Switch — adapt MetaBOT `Route Command`):**

| Route | Phase | Description |
|-------|-------|-------------|
| `local` | 1 | help, ping |
| `serp` | 1 | single-query SERP session (v0.1 parity) |
| `run` | 2+ | multi-step pipeline |
| `get` | 1 | fetch session summary / pack pointer |
| `approve` | 2 | mark pack approved (HITL) |
| `resume` | 2 | continue interrupted session |

---

## MIG Admin Design

### Purpose

Operational control plane без Telegram trigger: locks, health, forced cancel, storage/OpenRouter probes, session listing. **Не** запускает research pipeline.

### Inputs

| Source | Content |
|--------|---------|
| Admin webhook | `{ message, admin_command, chat_id, user_id, username }` |
| Google Sheets | `mig_active_sessions`, registry |
| Optional HTTP | HEAD/check SERP provider, OpenRouter models endpoint |

### Outputs

- Telegram formatted admin replies (HTML, chunked).
- Sheets mutations: cancel locks, mark `status=cancelled`.
- No Research Pack writes.

### External services

- Google Sheets (primary for admin reads).
- Telegram.
- Optional: filesystem list dir check, OpenRouter health (credentials-based).

### Human interaction

Admin-only commands (operator ACL — **SAFE UNKNOWN** in discovery):

| Command | Action |
|---------|--------|
| `/mig locks` | List active locks / sessions |
| `/mig health` | Sheets reachable, session root writable, webhook self-check |
| `/mig stop-all` | Cancel all active locks (reuse `stop-all-flow` semantics) |
| `/mig cancel {session_id}` | Single session cancel |
| `/mig storage` | Disk/session root stats |
| `/mig openrouter` | Credential present + minimal probe (no key in export) |

### Storage interaction

- Read/write Sheets only.
- Filesystem: read-only checks (dir exists, last session).

### Failure handling

- `onError: continueRegularOutput` on health sub-checks (reuse Admin pattern).
- Aggregate health report: OK / DEGRADED / FAIL per subsystem.

---

## Telegram UX Design

### Command namespace

**Префикс `/mig`** (или dedicated bot) — avoids collision with SEO `/run`, `/outline`, etc.

| Command | Handler | Operator experience |
|---------|---------|----------------------|
| `/mig start` | Intake | Welcome + capability summary |
| `/mig help` | Intake | Command list |
| `/mig serp {query}` | Intake → Worker | Quick Phase 1 SERP session |
| `/mig run` + body | Intake → Worker | Full session with brief (Phase 2+) |
| `/mig status` | Intake → Worker `get` | Current stage + session_id |
| `/mig get {session_id}` | Intake → Worker | Summary + pack location |
| `/mig history` | Intake → Worker/Sheets | Last N sessions for chat |
| `/mig approve {session_id}` | Intake → Worker | HITL approval gate (Phase 2) |
| `/mig locks` | Intake → Admin | Active sessions |
| `/mig health` | Intake → Admin | Subsystem health |
| `/mig stop-all` | Intake → Admin | Emergency cancel |

### Status messages

Reuse MetaBOT pattern:

1. Intake: «✅ Сессия принята · `{session_id}`» immediately.
2. Worker: create status message → `editMessageText` chain:

```text
MIG · {session_id}
◌ Intake validated
◌ Collecting SERP
◌ Normalizing
◌ Draft pack
◌ Ready for review
```

Use `◌` / `✓` / `✗` consistent with HTML `parse_mode`.

### Progress updates

- Edit same `status_message_id` (proven).
- Long operations: optional 3s Wait before Sheets meta write (MetaBOT timing buffer) — **ADAPT** for MIG.

### Result delivery

- Phase 1: chunk summary (≤3600) + «Pack: `{folder_path}` / session_id».
- Do not paste full `research_pack.draft.md` in Telegram if > limit — operator uses path or `/mig get`.
- `splitMessage()` + markup sanitizer node (reuse Worker `Parse Mode` node **name is misleading** — it's Telegram HTML sanitizer).

### Failure messages

**Explicit design requirement** (MetaBOT gap): Worker must send «❌ Сессия `{id}` остановлена: {reason}» on pipeline failure; update status message to failed state; Sheets `status=failed`.

### Research retrieval

- `/mig get {session_id}` — metadata + first N lines of draft or link to files.
- `/mig history` — Sheets-backed list (session_id, niche, stage, date).

### History access

- **Sheets registry** = index (operator-visible, cross-device).
- **Filesystem** = authoritative artifacts.
- No separate database.

### Reuse matrix (UX)

| Pattern | Reuse |
|---------|-------|
| Intake/Worker split | REUSE |
| Acceptance + busy messages | REUSE |
| Status `editMessageText` | REUSE |
| Chunk splitter | REUSE |
| Inline callbacks / keyboards | AVOID (not in exports) |

---

## Research Session Lifecycle

### Validated lifecycle (replaces example-only draft)

Стадии выровнены с `session_manifest.stage` + Sheets `stage` column + pack state:

```text
requested          ← Telegram command received (Intake)
    ↓
accepted           ← Lock acquired, Worker webhook fired
    ↓
intake_validated   ← validateIntake OK (maps v0.1)
    ↓
collecting         ← SERP provider / manual / fallback active
    ↓
normalizing        ← serp_result.json written
    ↓
drafting           ← research_pack.draft.md generation
    ↓
draft_complete     ← artifacts on disk (v0.1 terminal today)
    ↓
review             ← operator HITL (optional file edit)
    ↓
approved           ← Approved By recorded in manifest
    ↓
published          ← handoff marker for ORCA pickup (human)
    ↓
consumed           ← ORCA acknowledged intake (manual flag Phase 5)
    ↓
archived           ← retention / cold storage
```

**Failure / cancel branches:**

- `failed` — unrecoverable error (with `failure_reason`).
- `cancelled` — Admin or operator cancel.
- `stale` — lock TTL expired without completion (**SAFE UNKNOWN** if auto-cleanup job exists live).

### Mapping to v0.1

| v0.1 stage | New runtime |
|------------|-------------|
| `intake_complete` | `intake_validated` |
| `draft_complete` | `draft_complete` |

v0.1 does not implement `review` → `approved` — Phase 2 HITL.

---

## Storage Architecture

### Principle: hybrid SoT (from discovery recommendation C)

| Layer | Role | SoT for |
|-------|------|---------|
| **Filesystem** (`MIG_SESSION_ROOT/{session_id}/`) | Artifacts, snapshots, packs, manifest | Research Pack content, SERP JSON, evidence files |
| **Google Sheets** (`mig_session_registry`, `mig_active_sessions`) | Operator index, locks, history | Concurrency, cross-session lookup, audit index |
| **Telegram** | UX | Ephemeral — not storage |
| **Database** | **Avoid** | Not evidenced in ecosystem; not required Phase 1–4 |

### Filesystem layout (per session)

```text
{session_id}/
  session_manifest.json      ← spine SoT for stage + metadata
  serp_result.json
  research_pack.draft.md
  research_pack.review.md    ← optional
  research_pack.approved.md  ← ORCA handoff file
  snapshots/                 ← Phase 2+
  safe_unknown.log           ← optional append-only
```

### Google Sheets roles (new tabs — separate from SEO sheets)

**Do not write MIG rows into `seo_active_jobs` / `memory`.** Same spreadsheet **document** acceptable if operator prefers one doc; **separate sheet tabs** mandatory.

| Sheet | Role |
|-------|------|
| `mig_active_sessions` | Lock registry (adapt `seo_active_jobs`): `lock_key`, `chat_id`, `session_id`, `status`, `expires_at`, `stage` |
| `mig_session_registry` | Append/update index: `session_id`, `niche`, `region`, `query_used`, `stage`, `pack_state`, `folder_path`, `operator_id`, timestamps |
| `mig_session_memory` | Optional Phase 2: lightweight input/output summary for `/mig get` (≤50k fields pattern from MetaBOT) — **not** full pack |

### Research Pack role

- System object (see next section), not «just a file» — filename reflects `pack_state`.
- Draft generated by Worker; approved copy is ORCA intake artifact.

### Session registry role

- Sheets = **index**; manifest = **session truth**.
- On conflict: **filesystem manifest wins**.

### Locks role

- Per-chat mutex (reuse 30min TTL pattern — **ADAPT** to MIG session duration, suggest 60–120 min).
- `lock_key`: `mig:chat:{chatId}:{timestamp}`.
- `session_id`: `mig{YYYYMMDDHHmmss}{random6}` (parallel SEO format, different prefix).

### History role

- `mig_session_registry` filtered by `chat_id` / `operator_id`.
- No separate history DB.

---

## OpenRouter Architecture

### Where OpenRouter belongs

| Location | OpenRouter? |
|----------|-------------|
| MIG Intake | **No** |
| MIG Admin | **Probe only** (health check, no generation) |
| MIG Worker | **Yes** — selected routes only |

### Which workflow calls it

**MIG Worker only**, via Code `Build * Payload` → HTTP `POST https://openrouter.ai/api/v1/chat/completions` (same endpoint pattern as MetaBOT).

### Stages that SHOULD use OpenRouter

| Stage | Phase | Purpose |
|-------|-------|---------|
| Draft pack enrichment | 1 (optional) | Turn normalized SERP JSON into structured narrative sections in `research_pack.draft.md` |
| Evidence summarization | 2 | Competitor / landing notes compression |
| SAFE UNKNOWN expansion | 2 | Structured gap list from raw notes |
| Review assistant | 3 | Suggest review checklist — **HITL**, not auto-approve |

### Stages that MUST NOT use OpenRouter

| Stage | Reason |
|-------|--------|
| SERP raw capture | Groundtruth must be provider/human observation — not LLM hallucination |
| Lock / registry writes | Deterministic |
| Approval transition | Human authority only |
| Manifest stage transitions | Code/deterministic rules |
| ORCA handoff | No LLM in MIG at consumption boundary |

### Architectural rules

1. **Credentials:** n8n OpenRouter credential or `$env` — **never** inline in export.
2. **Payload pattern:** REUSE `openrouter_payload` + `extractContent` + `parseJsonLoose` + `safeParse`.
3. **JSON mode:** structured steps only; markdown pack body may be non-JSON.
4. **Timeout:** 120000 ms (proven); **retry:** design explicit 1–2 retries (MetaBOT lacks — MIG adds).
5. **Cost control:** Phase 2+ — model map per route; default small model for enrichment.
6. **Failure:** stage `failed_llm`, manifest `safe_unknown`, Telegram notify.

---

## Research Pack System Object

### Definition

**Research Pack** — версионируемый артефакт сессии, связывающий manifest, SERP, observations, evidence grades, и SAFE UNKNOWN, с явным lifecycle state independent from `session_manifest.stage`.

### States (validated)

| `pack_state` | Meaning | Writable by |
|--------------|---------|-------------|
| `draft` | Auto-generated `research_pack.draft.md` | Worker |
| `review` | Operator editing / HITL | Human (file or future UX) |
| `approved` | `research_pack.approved.md` + manifest `approved_by` | Human only |
| `consumed` | ORCA acknowledged | Human/ORCA operator flag |
| `archived` | Retention | Admin or cron (future) |

### Lifecycle

```text
(none) → draft → review → approved → consumed → archived
           ↓                 ↓
        failed            revoked (admin, back to review)
```

### Ownership

| Concern | Owner |
|---------|-------|
| Content truth | MIG filesystem |
| Approval authority | Human operator |
| Interpretation | ORCA (after approved) |
| pack_state SoT | `session_manifest.pack_state` + Sheets column mirror |

### Storage

- Files per state (see filesystem layout).
- Manifest fields: `pack_state`, `approved_by`, `approved_at`, `consumed_at`, `artifact_paths`.

### Consumption

- **ORCA** reads `research_pack.approved.md` + manifest + `serp_result.json` + snapshots (Phase 2+).
- **Website Factory** — no direct consumption.
- **MetaBOT** — no consumption.

---

## ORCA Integration Contract

### Contract level only (no transport)

Aligns with [contracts/mig-orca-handoff-contract-v0.md](../contracts/mig-orca-handoff-contract-v0.md).

### What ORCA receives (exactly)

| Deliverable | Description |
|-------------|-------------|
| **Approved Research Pack** | `research_pack.approved.md` (human-finalized) |
| **Session manifest** | `session_manifest.json` with `pack_state=approved`, `approved_by`, dates |
| **SERP artifact** | `serp_result.json` (normalized observations) |
| **Snapshots** | Files under `snapshots/` when present |
| **SAFE UNKNOWN list** | From manifest + pack |
| **Evidence grades** | Per contract required fields |

**Delivery mechanism:** **Human handoff only** — operator copies path, archive, or shared drive; Phase 5 may add optional notification, **not** auto webhook to ORCA in Phase 1–4.

### What ORCA must NEVER do

| Prohibition | Reason |
|-------------|--------|
| Write into MIG session folders | Preserve capture integrity |
| Trigger MIG Worker / Intake webhooks | MIG owns acquisition |
| Mutate `serp_result` or draft packs | Groundtruth contamination |
| Auto-approve packs | Human authority |
| Infer missing fields silently | Contract requires SAFE UNKNOWN |
| Semantic clustering during intake | ORCA owns interpretation |
| Use unapproved draft as production input | Boundary |

### Phase 5: consumption signal

- Operator sets `pack_state=consumed` in manifest after ORCA confirms — **manual** registry update; no automated ORCA→MIG bus without explicit future charter.

---

## Admin Operations

### Minimum viable admin surface (Phase 1)

| Operation | Command | Priority |
|-----------|---------|----------|
| Health | `/mig health` | P0 |
| Active locks | `/mig locks` | P0 |
| Cancel one | `/mig cancel {id}` | P0 |
| Stop all | `/mig stop-all` | P0 |
| Storage check | `/mig storage` | P1 |
| OpenRouter check | `/mig openrouter` | P1 |
| Resume | `/mig resume {id}` | P2 (Phase 2) |

### Health report structure (design)

```text
MIG Health
Sheets: OK | FAIL
Session root: OK | FAIL (path, writable)
Last session: {id} @ {date}
Active locks: {n}
OpenRouter: OK | SKIP | FAIL
```

### Sessions admin

- List from `mig_session_registry` (not FS scan alone).
- Filter: active / failed / stale.

### Locks admin

- Same semantics as MetaBOT Admin cancel → `status=cancelled`.
- **Design add:** optional expired-lock sweeper (not in MetaBOT export).

### Cancel / resume

- **Cancel:** Worker cooperative flag file `session.cancelled` or Sheets status — Worker checks between stages.
- **Resume:** reload manifest `stage`, continue from last incomplete step — Phase 2.

---

## Evolution Path

### Phase 1 — SERP + Research Pack (MVP runtime)

- Deploy Intake / Worker / Admin skeleton on same n8n.
- Worker route `serp` — v0.1 spine parity (fallback/manual).
- Filesystem artifacts + Sheets registry/locks.
- Telegram UX: accept, status, get, fail messages.
- Pack lifecycle ends at `draft` → manual promote to `review`/`approved`.
- **No** live SERP provider required.

### Phase 2 — Competitor Discovery

- Worker route `run` multi-step.
- `snapshots/` + competitor observation fields in manifest.
- OpenRouter: summarization only post-capture.
- `/mig approve`, resume, history.

### Phase 3 — Landing Analysis

- Additional Worker sub-pipeline + snapshot captures.
- Pack sections for landing/CTA/trust.
- Extended `safe_unknown` discipline.

### Phase 4 — Deep Research

- Long-running sessions, multi-query, optional `mig_session_memory`.
- Optional Export workflow (file bundle to operator).
- Retention / `archived` automation.

### Phase 5 — ORCA Consumption

- Formal `consumed` state + operator checklist.
- Optional: read-only ORCA workspace mirror — **still human-mediated**.
- No reverse automation without new contract version.

---

## Architecture Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Inline API keys copied from SEO Worker | **High** | Credentials-only; redacted exports |
| n8n FS path mismatch (Windows vs Linux VPS) | **High** | `MIG_SESSION_ROOT` env; no hardcoded `C:/` in production nodes |
| Command collision with SEO bot | **Medium** | `/mig` prefix or separate bot |
| Sheets/FS desync | **Medium** | Manifest wins; reconciliation admin command |
| LLM contamination of SERP groundtruth | **High** | OpenRouter ban on capture stages |
| MetaBOT error visibility gaps copied | **Medium** | Explicit failure Telegram messages (design mandate) |
| Lock TTL too short for research | **Medium** | Tune TTL; status in Sheets |
| Governance drift («MIG owns n8n») | **Low** | Docs: n8n is execution substrate; MARS repo remains contracts + spine lib |
| v0.1 monolith left active parallel to v14-style | **Medium** | Deprecate single-webhook after cutover |
| Live n8n ≠ repo exports | **Medium** | Operator live inventory before cutover |

---

## SAFE UNKNOWN

- Dedicated Telegram bot vs shared bot with `/mig` namespace.
- Production `MIG_SESSION_ROOT` on VPS (Linux path, permissions, backup).
- Whether MIG shares OpenRouter credential with SEO or separate budget cap.
- Google Spreadsheet: new doc vs new tabs in existing MetaBOT doc.
- Live n8n workflow IDs and exact webhook paths after import.
- SERP provider vendor and API shape (Phase 2).
- Admin ACL (who may `/mig stop-all`).
- Auto cleanup of expired locks.
- Worker behavior on partial OpenRouter JSON (beyond MetaBOT `safeParse` pattern).
- Whether Phase 1 includes optional OpenRouter draft enrichment or deterministic template only.
- ORCA operator workflow for `consumed` acknowledgment.

---

## Recommended Next Step

1. **Operator decision gate (HITL):** Telegram bot strategy + `MIG_SESSION_ROOT` on VPS + Sheets tab names.
2. **Sanitize & rotate** OpenRouter keys in live n8n before cloning HTTP nodes for MIG.
3. **Author workflow design spec v2** — node-level map for Intake/Worker/Admin only after this runtime design approval (still not JSON export until chartered).
4. **Migrate v0.1 spine** into Worker Code node library; mark monolith webhook deprecated.
5. **Implement Phase 1 failure notifications** — do not copy MetaBOT silent-failure gap.
6. **Live inventory** — reconcile exports with active n8n workflows (read-only, supervised).

---

## References

| Artifact | Path |
|----------|------|
| Discovery report | Agent transcript `91daad8c-fcd9-4002-acd2-d09b92ee02e2` |
| MetaBOT exports | `incoming/metabot/seo-writer-workflows/` |
| MIG v0.1 workflow | `projects/mig/workflows/n8n/mig-research-session-v0.1.json` |
| Session spine | `projects/mig/lib/session-spine/` |
| ORCA handoff contract | `projects/mig/contracts/mig-orca-handoff-contract-v0.md` |
| Boundaries | `projects/mig/boundaries.md` |

---

*Design only. No git commit. No implementation.*
