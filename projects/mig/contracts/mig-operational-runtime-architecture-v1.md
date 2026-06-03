# MIG Operational Runtime Architecture v1

**Status:** **documented** — first operational runtime model for MIG inside MARS.  
**Not:** implementation, deployment, n8n workflow export, VPS provisioning, OpenRouter setup, MARS Bridge production wiring, ORCA redesign, Website Factory redesign, Deep Research runtime, Keyword runtime, or Wordstat implementation.

**Upstream:** [mig-runtime-assembly-v1.md](mig-runtime-assembly-v1.md); [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md); [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md); [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md); [mig-task-file-adapter-spec-v0.1.md](mig-task-file-adapter-spec-v0.1.md); [../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md); [../reports/REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md).  
**Evidence (runtime):** `projects/mig/lib/runtime/run-mig-session.js`; `projects/mig/schemas/session-manifest-v0.2.schema.json`; `incoming/mig/` drop zone; `incoming/mars-bridge/mars-bridge-workflow.json` (stub).

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

---

## 1. Operational Runtime — definition

### 1.1 What Operational Runtime is

| Aspect | Definition |
|--------|------------|
| **Operational Runtime** | The **human-supervised** combination of **where MIG runs**, **how sessions are triggered and stored**, **how operators review and approve**, and **how approved outputs reach ORCA** — without claiming autonomous orchestration |
| **Scope** | One bounded **Research Session** from intake transport through **pack lifecycle** (`draft` → … → `archived`) |
| **SoT split** | **Filesystem** = session artifacts + manifest; **Research Pack** = domain product (lifecycle independent of `session_manifest.stage`) |
| **Authority** | **Human operator** owns approval, handoff, and consumption ack; automation **never** auto-approves |

Operational Runtime **wraps** the existing **Runtime MVP** (`runMigSession`) with **MARS-operable** intake paths, storage discipline, registry mirrors, and phased deployment — it does **not** replace acquisition logic.

### 1.2 What Operational Runtime is not

| Anti-pattern | Why excluded |
|--------------|--------------|
| Runtime MVP itself | MVP = **capability** (P0–P6 JS pipeline); Operational Runtime = **how MARS runs and governs** that capability |
| MARS multi-agent orchestration product | No in-repo orchestration engine; docs describe **human-operated** patterns only |
| n8n as acquisition engine | n8n **orchestrates and notifies**; heavy fetch/parse stays in **Node modules** |
| ORCA analysis runtime | ORCA consumes **approved** packs only — see handoff contract |
| Website Factory production | Factory path: MIG → ORCA → strategy → Factory |
| Background daemon / auto-poll without charter | Task File Adapter v0.1 is **invoke-on-demand** |
| Proof of VPS or n8n production deployment | Design references `n8n.ai-metacode.com`; **live cutover not evidenced in-repo** |

### 1.3 Relationship map

```text
                    ┌─────────────────────────────────────────┐
                    │              MARS (repo)                 │
                    │  contracts · drop zones · spine lib      │
                    └────────────────────┬────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         │                               │                               │
         ▼                               ▼                               ▼
┌─────────────────┐           ┌─────────────────┐           ┌─────────────────┐
│  Runtime MVP    │           │ Operational     │           │  MARS Bridge    │
│  runMigSession  │◄──────────│ Runtime (this   │──────────►│  (stub export)  │
│  manifest v0.2  │  wraps    │  document)      │  future   │  cross-system   │
└────────┬────────┘           └────────┬────────┘           └────────┬────────┘
         │                             │                             │
         │                             ▼                             │
         │                   ┌─────────────────┐                       │
         │                   │ n8n (VPS)       │◄── MetaBOT patterns │
         │                   │ Intake/Worker/  │    separate webhooks  │
         │                   │ Admin (design)  │    `mig/*` not SEO    │
         │                   └────────┬────────┘                       │
         │                            │                               │
         ▼                            ▼                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  Session storage: {MIG_SESSION_ROOT}/{session_id}/                           │
│  Intake registry: incoming/mig/registry/request-index.json                   │
└─────────────────────────────────────────────────────────────────────────────┘
         │
         │  approved pack + human handoff
         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│      ORCA       │────►│ Website Factory │     │      NOVA       │
│  interprets R2  │     │  R3 (downstream)│     │  no direct MIG  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

| System | Relationship to Operational Runtime |
|--------|-------------------------------------|
| **Runtime MVP** | **Core executor** — `runMigSession` implements P0→P2→optional P3/P4→P6; Operational Runtime defines **when/where/who** invokes it |
| **n8n** | **Phase 2+ orchestration substrate** on existing VPS (`n8n.ai-metacode.com` per runtime design report) — locks, Telegram UX, webhooks; **not** DOM/fetch logic |
| **ORCA** | **Downstream consumer** — human handoff of **approved** pack; never writes MIG storage |
| **MARS Bridge** | **Future transport** — envelope → Research Request; today **stub only** (`incoming/mars-bridge/mars-bridge-workflow.json`, `mode: bridge_stub`) |
| **Website Factory** | **No direct** MIG session consumption; chain via ORCA strategy |
| **NOVA** | **No MIG coupling** in repo — mobile factory methodology parallel to Website Factory; market groundtruth for mobile products would follow same **MIG → ORCA → …** pattern if chartered later |
| **MetaBOT** | **Pattern donor only** (Intake/Worker/Admin, Sheets locks) — **separate** workflow family; MIG must not embed in SEO Content Agent graphs |

---

## 2. Where MIG lives

### 2.1 Logical placement in MARS

| Layer | Location | Role |
|-------|----------|------|
| **Contracts & architecture** | `projects/mig/contracts/` | Normative behavior |
| **Runtime libraries** | `projects/mig/lib/` (`session-spine/`, `runtime/`, passes) | Executable logic (Node) |
| **Session artifact SoT** | `{MIG_SESSION_ROOT}/{session_id}/` | Default dev: `projects/mig/sessions/` per [env.example](../config/env.example) |
| **Intake drop zone** | `incoming/mig/` | Request files + `registry/request-index.json` |
| **n8n exports (design)** | `projects/mig/workflows/n8n/` | Not proof of production |
| **Bridge stub** | `incoming/mars-bridge/` | Cross-lane envelope experiments |

MIG **does not** live inside ORCA, Website Factory, or MetaBOT repos. It **may** be **invoked from** n8n on the **same VPS** as MetaBOT with **isolated** webhooks and credentials.

### 2.2 Deployment topology evaluation

| Topology | Fit | Role |
|----------|-----|------|
| **Local workstation** | **Operational MVP primary** | Cursor-supervised dev; `node` / PowerShell verify; Task File drop zone on repo disk |
| **Cursor execution** | **Operational MVP primary** | Agent/human runs adapter or `runMigSession`; no hidden automation |
| **VPS execution** | **Phase 2 primary** | `MIG_SESSION_ROOT` on Linux path; n8n Code nodes `require()` spine; backup/permissions operator-owned |
| **n8n execution** | **Phase 2 orchestration** | Webhooks, Telegram, Sheets registry — **not** replacement for `runMigSession` |
| **Hybrid** | **Long-term target** | Intake on VPS (Telegram/Bridge); heavy passes in Node; optional local resume for debug |

### 2.3 Phased deployment decision

| Phase | Execution home | Intake | Storage |
|-------|----------------|--------|---------|
| **Operational MVP** | Operator workstation + repo paths | Task File (`incoming/mig/`) + manual `runMigSession` / verify CLI | Filesystem SoT; registry JSON mirror |
| **Operational Phase 2** | VPS + n8n Worker calling same lib | MIG Intake (Telegram) + Task File + Bridge webhook (chartered) | Filesystem SoT on VPS; Google Sheets **registry mirror** |
| **Operational Phase 3** | Hybrid stable | All chartered transports + optional read API | Filesystem SoT + DB index optional; Sheets optional retire of wide columns |

**Normative:** Production `MIG_SESSION_ROOT` is **operator-configured** — never hardcode `C:\AI MARS\...` in n8n nodes (Windows dev vs Linux VPS mismatch is a **known high risk** from runtime design report).

---

## 3. How MIG is executed

### 3.1 Execution stack (normative)

```text
Transport adapter (Task File · CLI · future Bridge · future n8n Intake)
        ↓
Research Request validation (canonical contract)
        ↓
runMigSession (Runtime MVP — canonical intake path)
        ↓
{MIG_SESSION_ROOT}/{session_id}/  artifacts + session_manifest.json v0.2
        ↓
Operator HITL (review → approve → publish)
        ↓
ORCA handoff (human)
```

| Executor | Invokes | When |
|----------|---------|------|
| **Task File Adapter** | `runMigSession` | Drop zone + `run-task-file-adapter.ps1` |
| **`run-mig-session.js`** | Full Runtime MVP | Verify script, direct CLI, future Worker |
| **n8n MIG Worker (design)** | `require(runMigSession)` or HTTP to local helper | Phase 2 async sessions |
| **Cursor agent** | Supervised CLI only | Dev/fixture — **not** production scheduler |

### 3.2 Concurrency and locks

| Concern | Operational MVP | Phase 2 |
|---------|-------------------|---------|
| Per-operator session | Human discipline | Google Sheets `mig_active_sessions` lock (MetaBOT pattern) |
| Parallel sessions | Allowed with distinct `session_id` | Lock per `chat_id` in Intake |
| Crash mid-run | Re-run pass or new request; manifest `phase` for resume (target) | Worker marks manifest `failed`; Admin cancel |

---

## 4. Session storage model

### 4.1 Evaluation

| Store | Verdict | Role |
|-------|---------|------|
| **Filesystem** | **SoT — required** | All session artifacts, HTML snapshots, manifest, pack representations |
| **Google Sheets** | **Mirror — Phase 2** | Session registry, locks, operator-visible index — **not** full pack body |
| **Database** | **Optional Phase 3** | Searchable index, audit API — **not** SoT for blobs/HTML |
| **Hybrid** | **Long-term** | FS SoT + DB/Sheets indexes |

### 4.2 Source of truth hierarchy

| Priority | Artifact / index | Location |
|----------|------------------|----------|
| 1 | Session artifacts (`serp_result.json`, snapshots, `research_pack.*.md`) | `{MIG_SESSION_ROOT}/{session_id}/` |
| 2 | `session_manifest.json` v0.2 | Same folder — execution + `pack_state` (when set) |
| 3 | Research Pack (logical) | Projected from manifest + files; `pack_state` per [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) |
| 4 | `incoming/mig/registry/request-index.json` | Request ↔ session linkage (intake transport only) |
| 5 | Google Sheets row | Mirror — **manifest wins** on conflict |

### 4.3 Session folder layout (evidenced + target)

```text
{MIG_SESSION_ROOT}/{session_id}/
  session_manifest.json
  serp_result.json
  competitors.json
  website_snapshots.json
  snapshots/sites/{snapshot_id}/...
  landing_observations.json
  landings/{landing_id}/landing_observation.json
  research_pack.draft.md
  research_pack.review.md          (operator, Phase 2 ops)
  research_pack.approved.md        (after HITL)
  handoff/                         (optional published bundle, Phase 2)
```

### 4.4 Retention and archive

| Model | Rule |
|-------|------|
| **Active** | Default — sessions under `MIG_SESSION_ROOT` until operator archives |
| **Intake archive** | `incoming/mig/archive/` — operator copies of **request files**, not session SoT |
| **Pack `archived`** | Lifecycle state + optional move to cold path (`MIG_ARCHIVE_ROOT` — **operator-defined**, not in repo) |
| **Retention policy** | Human-operated; no automated purge in Operational MVP |
| **Deletion** | **Explicit human instruction only** — aligns with MARS file rules |

---

## 5. Operator workflow

### 5.1 Canonical workflow

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ 1. CREATE RESEARCH REQUEST                                                │
│    · Task File: incoming/mig/requests/request-<request_id>.json          │
│    · OR: fixture / CLI body / future Telegram / Bridge                    │
└───────────────────────────────┬──────────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ 2. RUN SESSION                                                            │
│    · MVP: run-task-file-adapter.ps1  OR  node run-mig-session.js          │
│    · Outcome: session dir + research_pack.draft.md + pack_state=draft     │
└───────────────────────────────┬──────────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ 3. REVIEW DRAFT PACK (HITL)                                               │
│    · Operator reads draft + artifacts + SAFE UNKNOWN                      │
│    · Promote pack_state: draft → review (manifest + optional .review.md)  │
└───────────────────────────────┬──────────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ 4. APPROVE                                                                │
│    · Record approved_by, approved_at                                      │
│    · pack_state: approved · write research_pack.approved.md               │
└───────────────────────────────┬──────────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ 5. PUBLISH (handoff ready)                                                │
│    · pack_state: published · optional handoff/ bundle                     │
└───────────────────────────────┬──────────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ 6. DELIVER TO ORCA                                                        │
│    · Human handoff — filesystem bundle or agreed channel                  │
│    · ORCA validates Approved By + required fields                         │
└───────────────────────────────┬──────────────────────────────────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────────────────┐
│ 7. CONSUME → ARCHIVE                                                      │
│    · ORCA operator ack → pack_state consumed                              │
│    · Retention → archived                                                │
└──────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Operator responsibilities

| Responsibility | Owner | Automation |
|----------------|-------|------------|
| Author valid Research Request | Operator / upstream system | Adapter validates schema |
| Invoke processor | **Human** (MVP) | Phase 2: n8n dispatch after lock |
| Evidence review | **Human** | None |
| Approve pack | **Human only** | **Forbidden** for Worker/runtime |
| Deliver to ORCA | **Human** | None in v1 |
| ORCA consumption ack | ORCA operator | Operator writes `consumed` in manifest |
| Registry hygiene | Operator | Adapter updates `request-index.json` on success |

### 5.3 Automation boundaries

| Automated (allowed) | Never automated (MVP–Phase 2) |
|---------------------|----------------------------------|
| Intake normalize + validate | `approved`, `published`, `consumed` transitions |
| SERP normalize (incl. fallback) | ORCA interpretation |
| Competitor / website / landing passes per profile | Deleting SAFE UNKNOWN without audit |
| Draft pack assembly | Website Factory blueprint generation |
| Manifest stage updates inside `runMigSession` | Cross-session approval on behalf of operator |

---

## 6. Runtime entrypoints

### 6.1 Evaluation matrix

| Entrypoint | MVP | Phase 2 | Phase 3 | Notes |
|------------|-----|---------|---------|-------|
| **Task File** (`incoming/mig/`) | **Primary** | Supported | Supported | Evidenced: adapter + registry |
| **CLI** (`run-mig-session.js`, verify scripts) | **Primary** | Dev/ops | Dev/ops | Evidenced |
| **Manual execution** (Cursor / PowerShell) | **Primary** | Supervised | Supervised | Human-supervised norm |
| **MARS Bridge** | Stub only | Chartered webhook | Stable envelope | `mars-bridge-workflow.json` = stub |
| **n8n Webhook** (`mig-worker`) | Export exists, not production | **Primary async** | Primary | Monolith v0.1 export **not** production shape |
| **Telegram (MIG Intake)** | No | **Primary UX** | Primary UX | Design per MetaBOT report |
| **Future HTTP API** | No | No | Optional read/status | **Not** acquisition API in Phase 3 unless chartered |

### 6.2 Entrypoint routing (target)

```text
Task File ──────┐
Telegram Intake ├──► normalize Research Request ──► runMigSession ──► session dir
Bridge webhook ─┤
CLI / fixture ──┘
```

**Task File Adapter** today calls **session spine v0.1**, not `runMigSession` — **Operational Phase 2 backlog:** unify adapter to Runtime MVP orchestrator.

---

## 7. n8n role

### 7.1 What n8n should do

| Function | Rationale |
|----------|-----------|
| **Intake webhook / Telegram trigger** | Proven MetaBOT UX; instant ack / busy |
| **Concurrency locks** (Sheets) | Prevent duplicate sessions per operator |
| **Fire-and-forget dispatch** to Worker | Async long sessions |
| **Status notifications** | `editMessageText`, chunked summaries |
| **Simple HTTP** to SERP provider (Phase 2+) | Credential store |
| **Thin Code node** | `require()` → `runMigSession` with env `MIG_SESSION_ROOT` |
| **Admin routes** | Cancel, health, lock clear |
| **Registry mirror updates** | `stage`, `pack_state`, `folder_path` columns |

### 7.2 What n8n must not do

| Anti-pattern | Why |
|--------------|-----|
| Monolith single-webhook session (v0.1 export as production) | No locks, no admin isolation |
| Playwright / heavy DOM in Code nodes | Timeouts, RAM, untestable |
| Pack approval logic | Violates HITL contract |
| ORCA analysis or Factory generation | Boundary violation |
| Embed inside `seo-content-agent-*` workflows | Blast radius + naming collision |
| Filesystem as **only** registry without manifest discipline | Sheets is mirror, not SoT |
| Inline API keys in exports | MetaBOT SECURITY RISK lesson |

### 7.3 What stays in JS runtime

| Module class | Examples |
|--------------|----------|
| Session orchestration | `run-mig-session.js`, manifest helpers |
| Acquisition passes | `competitor-discovery/`, `website-acquisition/`, `landing-analysis/` |
| Pack projection | `build-research-pack.js` |
| Unit verification | `verify-runtime-mvp-v0.mjs` |

**Pattern (normative):** MetaBOT **orchestrates**; MIG **lib acquires** — same as data acquisition architecture report.

### 7.4 Workflow family (Phase 2 target)

| Workflow | Webhook path (design) |
|----------|----------------------|
| MIG Intake | Telegram → `POST …/webhook/mig-worker` |
| MIG Worker | `POST mig-worker` |
| MIG Admin | `POST mig-admin` |

**Connection rule:** Webhook → Webhook only — **no** `Execute Workflow` between MIG workflows (MetaBOT discipline).

---

## 8. Approval operations

### 8.1 Lifecycle states (canonical)

Aligned with [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) §6:

```text
draft → review → approved → published → consumed → archived
         ↑___________|
              revoked (from approved)
```

| State | Meaning | ORCA-eligible |
|-------|---------|---------------|
| `draft` | Worker finished P6 | **No** |
| `review` | Operator HITL | **No** |
| `approved` | `Approved By` recorded | **Yes** (after handoff) |
| `published` | Bundle released for pickup | **Yes** |
| `consumed` | ORCA ack | Historical |
| `archived` | Retention | Read-only |

### 8.2 Ownership and auditability

| Transition | Authority | Audit artifact |
|------------|-----------|----------------|
| → `review` | Operator | Manifest `pack_state`; optional `research_pack.review.md` |
| → `approved` | Operator | `approval.approved_by`, `approved_at` in manifest; `research_pack.approved.md` |
| → `published` | Operator | `handoff/` bundle manifest; Telegram notice (Phase 2) |
| → `consumed` | Operator + ORCA ack | `consumption.*` in manifest |
| → `revoked` | Admin / approver | Audit reason in manifest |
| → `archived` | Admin / policy | Manifest + optional cold storage move |

**SoT for `pack_state`:** `session_manifest.pack_state` (v0.2 schema); Sheets mirror second; filename hint third.

**v0.1 gap (honest):** Approval transitions are **contract-defined** but **not implemented** in automation — operator performs file/manifest edits manually until Phase 2 Admin commands.

### 8.3 Artifact transitions

| Event | Files touched |
|-------|---------------|
| Draft complete | `research_pack.draft.md` created; `pack_state=draft` |
| Enter review | Copy or edit → `research_pack.review.md` (optional) |
| Approve | `research_pack.approved.md`; manifest approval block |
| Publish | `handoff/pack-bundle.json` + pointers (design); notify ORCA operator |
| Consume | Manifest consumption block only — **artifacts immutable** |

---

## 9. ORCA handoff operations

### 9.1 Evaluation

| Mechanism | MVP | Phase 2 | Long-term |
|-----------|-----|---------|-----------|
| **Filesystem bundle** | **Canonical** | **Canonical** | SoT remains FS |
| **MARS Bridge** | Stub | Envelope + path refs | Not pack body transport alone |
| **Task handoff** | Human copies paths | Same + checklist | Optional ticket id |
| **Artifact package** | `handoff/` subfolder | Standardized manifest | Versioned bundle schema |
| **Future API** | No | No | Read-only status optional |

### 9.2 Canonical approach (normative)

**Primary:** Operator delivers **approved Research Pack** as:

1. **Logical object** — satisfies [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) required fields  
2. **Representation bundle** — directory or zip under session:
   - `research_pack.approved.md` (or approved export)
   - `session_manifest.json`
   - Pointers to `serp_result.json`, `competitors.json`, snapshots as needed
   - Explicit **SAFE UNKNOWN** section
   - **Approved By** mandatory

**Transport:** **Human handoff only** — channel agnostic (shared drive, chat, ORCA inbox folder). No mandated API in Operational MVP.

**MARS Bridge (future):** Carries **envelope + references** (`session_id`, `folder_path`, checksums) — Bridge **does not** replace human approval or ORCA methodology.

**Forbidden:**

- ORCA pulling unapproved `research_pack.draft.md` as production input  
- Automated ORCA write-back into `MIG_SESSION_ROOT`  
- Website Factory reading raw session folders  

---

## 10. Reality assessment

### 10.1 Operationalizable immediately (human-supervised)

| Item | Evidence |
|------|----------|
| End-to-end Runtime MVP (`runMigSession`) | `lib/runtime/run-mig-session.js`; `verify-runtime-mvp-v0.mjs` |
| Manifest v0.2 schema | `schemas/session-manifest-v0.2.schema.json` |
| Task File drop zone + registry | `incoming/mig/`; adapter → `runMigSession`; verify: `verify-adapter-runtime-or09.mjs` |
| Session storage on repo disk | `MIG_SESSION_ROOT` default in env.example |
| Draft pack generation | Runtime MVP test folders |
| Operator workflow **as procedure** | This doc + existing pack/ORCA contracts |
| CLI verification / local runs | `test/run-spine-test.ps1`, verify scripts |

### 10.2 Requires implementation (not deployment)

| Item | Gap |
|------|-----|
| Task File Adapter → `runMigSession` | **Implemented (OR-09)** — adapter uses Runtime MVP |
| Approval state machine automation | Manifest transitions manual |
| `handoff/` bundle generator | Design only |
| MARS Bridge → Research Request adapter | Stub workflow only |
| n8n Intake/Worker/Admin family | Design + monolith export only |
| Sheets registry mirror | Not wired |
| Unified `update-manifest-pass` across passes | Noted gap in runtime assembly |
| Live SERP provider | Not implemented |

### 10.3 Requires infrastructure (operator / VPS)

| Item | Notes |
|------|-------|
| Linux `MIG_SESSION_ROOT` on VPS | Permissions, backup |
| n8n import + `mig/*` webhooks | Live inventory vs repo exports — **UNKNOWN** |
| Telegram bot for MIG | Operator choice: dedicated bot vs `/mig` prefix |
| Google Sheets tabs | `mig_active_sessions`, registry |
| OpenRouter credentials in n8n env | Phase 2+ enrichment only — **out of this charter** |
| VPS RAM for future Playwright | **UNKNOWN** — measure on host |

### 10.4 Remains conceptual

| Item |
|------|
| MARS autonomous runtime dispatch |
| ORCA automated intake API |
| Production MIG HTTP API |
| Database SoT for sessions |
| NOVA-specific MIG intake |
| Deep Research / Keyword / Wordstat **operational** lanes (explicitly out of scope) |

---

## 11. Roadmap

### 11.1 Operational MVP (target: now)

**Goal:** Repeatable human-operated sessions inside MARS repo without VPS dependency.

| Deliverable | Type |
|-------------|------|
| Task File + CLI/`runMigSession` as dual entry (adapter unification = small impl task) | Procedure + backlog |
| Filesystem SoT + `request-index.json` | **Exists** |
| Draft-only packs; manual approval files | **Exists / manual** |
| ORCA handoff checklist + filesystem bundle | Procedure |
| Operator runbook section in [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) | Doc |

**Out of scope:** n8n deploy, Bridge production, Sheets, Telegram, approval automation.

### 11.2 Operational Phase 2

**Goal:** VPS-hosted async operations with MetaBOT patterns.

| Deliverable | Type |
|-------------|------|
| MIG Intake / Worker / Admin on `n8n.ai-metacode.com` | Infra + n8n |
| `MIG_SESSION_ROOT` on VPS | Infra |
| Sheets registry + locks | n8n + Sheets |
| Telegram status UX | n8n |
| Bridge webhook → Research Request | Impl |
| Manifest-driven `pack_state` updates via Admin | Impl |
| Task File adapter calls `runMigSession` | Impl |

**Out of scope:** Deep Research runtime, Keyword runtime, Wordstat, OpenRouter-heavy synthesis as default.

### 11.3 Operational Phase 3

**Goal:** Stable hybrid ops + observability without scope creep.

| Deliverable | Type |
|-------------|------|
| Optional DB/session index API (read-mostly) | Impl |
| Standardized `handoff/` bundle + checksums | Impl |
| Bridge + ORCA folder drop automation (still HITL approve) | Impl |
| Archive/cold storage policy | Ops |
| Live SERP provider in Worker | Impl |

**Still out of scope:** Autonomous approval; ORCA capture ownership; Factory direct MIG reads.

---

## 12. Architecture decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| **OR-01** | **Operational Runtime ≠ Runtime MVP** | Separates capability from MARS operations |
| **OR-02** | **Filesystem SoT** for all capture artifacts | Evidenced; HTML/snapshots ill-suited for Sheets |
| **OR-03** | **Operational MVP = workstation + Task File + CLI** | Matches repo evidence; lowest infra risk |
| **OR-04** | **Phase 2 = VPS hybrid + n8n three-workflow family** | MetaBOT-proven; avoids monolith webhook |
| **OR-05** | **n8n orchestrates; Node acquires** | Testability + timeout safety |
| **OR-06** | **Human-only approval chain** | Pack + ORCA contracts |
| **OR-07** | **ORCA handoff = filesystem bundle + human transport** | Matches handoff v0; no fake API |
| **OR-08** | **MARS Bridge = envelope future, stub today** | `bridge_stub` in export |
| **OR-09** | **Unify Task File → `runMigSession`** before n8n cutover | Single pipeline truth |
| **OR-10** | **Explicit exclusion** of Deep Research / Keyword / Wordstat operational lanes in this roadmap | User charter boundary |

---

## 13. Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| OPERATIONAL-INDEX stale vs Runtime MVP | Medium | Sync index after implementation tasks |
| Task File uses spine v0.1 not `runMigSession` | High | OR-09 backlog before VPS |
| Windows vs Linux `MIG_SESSION_ROOT` | High | Env-only paths |
| n8n assumed production without evidence | Medium | Status honesty in reports |
| Auto-approve drift in Worker design | High | Forbidden transitions in contracts |
| Sheets/manifest `pack_state` conflict | Medium | Manifest wins |
| OpenRouter inline keys (MetaBOT legacy) | **SECURITY** | n8n credentials / `$env` only |
| Monolith `mig-research-session-v0.1.json` mistaken for prod | Medium | Deprecate in ops docs |

---

## 14. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Live n8n workflow IDs and active webhooks on VPS | **UNKNOWN** — operator inventory |
| Production `MIG_SESSION_ROOT` Linux path | **UNKNOWN** — operator config |
| MIG Telegram bot strategy (dedicated vs shared) | **UNKNOWN** — operator choice |
| VPS RAM headroom for Playwright | **UNKNOWN** |
| Whether Task File adapter will merge with `runMigSession` before Phase 2 | **Planned** — not done |
| ORCA physical inbox folder convention | **UNKNOWN** — ORCA operator |
| MARS Bridge production contract version | **UNKNOWN** — stub only |

---

## 15. Related documents

| Document | Link |
|----------|------|
| Runtime Assembly | [mig-runtime-assembly-v1.md](mig-runtime-assembly-v1.md) |
| Research Pack | [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) |
| ORCA Handoff | [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) |
| Task File Adapter | [mig-task-file-adapter-spec-v0.1.md](mig-task-file-adapter-spec-v0.1.md) |
| MetaBOT patterns report | [../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) |
| Drop zone | [../../../incoming/mig/README.md](../../../incoming/mig/README.md) |
| Boundaries | [../boundaries.md](../boundaries.md) |

---

## 16. Recommended next step

1. **Operator charter (HITL):** adopt Operational MVP workflow using `runMigSession` + Task File for one real request; manual approve → filesystem bundle → ORCA.  
2. **Implementation task (separate):** wire Task File Adapter to `runMigSession` (OR-09).  
3. **Before VPS:** operator defines `MIG_SESSION_ROOT`, Telegram/Sheets names, live n8n inventory (read-only).  
4. **Do not** import monolith n8n v0.1 as production — plan Intake/Worker/Admin skeleton per Phase 2.
