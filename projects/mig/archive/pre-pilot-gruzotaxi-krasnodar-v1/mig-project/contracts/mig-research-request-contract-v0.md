# MIG Research Request Contract v0

**Status:** **documented** — domain-level Source of Truth for MIG intake.  
**Not:** workflow spec, adapter implementation, JSON Schema registry, transport protocol, or runtime product.

**Supersedes:** Telegram-first, webhook-first, and task-file-first intake thinking.  
**Primary upstream (intended):** [../reports/REPORT-mig-request-architecture-v1.md](../reports/REPORT-mig-request-architecture-v1.md) — **SAFE UNKNOWN:** file not present in repo at contract authoring time; this contract consolidates approved principles from task charter + evidenced v0.1 spine + runtime design reports.

**Consumers (future, by reference only):** MIG Intake adapters, MIG Worker, MIG Admin, ORCA integration, MARS runtime integration.

---

## 1. Purpose

### What Research Request is

**Research Request** is the **canonical domain object** that declares operator intent to acquire market groundtruth under MIG (R1).

It is the **single normalized intake shape** that all transport surfaces must converge to **before** MIG executes acquisition work. Every adapter reads transport-specific input and produces (or updates) one Research Request.

```text
Research Request
    ↓
Research Session
    ↓
Research Pack
    ↓
ORCA (R2)
```

| Layer | Role |
|-------|------|
| **Research Request** | Declares *what* to research, *who* requested it, *how* (type), and intake metadata. **No** artifacts, **no** SERP body, **no** pack content. |
| **Research Session** | Bounded execution unit bound to a `session_id`; owns manifest, normalized SERP, draft pack, snapshots. Created **after** request acceptance. |
| **Research Pack** | Versioned session artifact with lifecycle `draft → review → approved → consumed → archived`. **Output** of session work — **not** the request. |
| **ORCA** | Consumes **approved** pack + manifest via human handoff. **Interprets** reality; does **not** own intake. |

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

### What Research Request is not

| Anti-pattern | Why excluded |
|--------------|--------------|
| Telegram command text | Transport only — parsed by Telegram Adapter |
| Webhook HTTP body | Transport envelope — parsed by Webhook Adapter |
| Task file on disk | Human/agent artifact — parsed by Task File Adapter |
| MARS Bridge stub payload | Cross-system envelope — parsed by MARS Bridge Adapter |
| OpenRouter / LLM payload | Synthesis transport — **never** intake |
| `session_manifest.json` | Session state — created **after** request is session-bound |
| Research Pack (any state) | Session **output**, not intake |
| ORCA analysis task | Downstream interpretation — separate domain |
| MARS Task envelope (orchestration) | May **reference** a Research Request; **not** interchangeable with it |

### Relationship to MARS Task

A **MARS Task** (future runtime / operator task file) may **carry** or **point to** a Research Request (by `request_id`, embedded JSON, or file path). The task envelope describes *orchestration context* (lane, HITL, deadlines). The Research Request describes *research intent*. Adapters must **extract** the Research Request; they must **not** treat the task wrapper as canonical intake.

### Relationship to intake adapters

Adapters are **transport-only**. Each adapter:

1. Accepts surface-specific input.
2. Normalizes to this contract (Research Request).
3. Hands off to MIG validation / acceptance / session binding.

**Approved adapter surfaces (non-exhaustive):**

| Adapter | Transport | Produces Research Request |
|---------|-----------|---------------------------|
| Webhook Adapter | HTTP POST body | Yes |
| Task File Adapter | JSON/YAML task file | Yes |
| MARS Bridge Adapter | Bridge envelope → nested payload | Yes |
| Telegram Adapter | `/mig …` command parse | Yes |
| CLI Adapter | stdin / file arg to spine | Yes (legacy flat map) |
| Cursor Adapter | Agent-authored JSON in repo task scope | Yes |
| API Adapter | Future REST/gRPC (not implemented) | Yes |

Adapters **must not** bypass validation. Adapters **must not** assign `session_id` unless explicitly running in **legacy v0.1 spine-compat** mode (see §10).

---

## 2. Request types

Each request carries exactly one `request_type`. Types define **intent**, **supported MIG phase**, and **lifecycle expectations**.

| `request_type` | Description | Phase | Implementation status | Lifecycle notes |
|----------------|-------------|-------|----------------------|-----------------|
| `serp_capture` | Single-query SERP groundtruth capture → normalized SERP + draft pack | Phase 1 | **v0.1 implemented** (Session Spine, `/mig serp`, monolith webhook) | Full path through `executing` → `completed` at `draft_complete` today |
| `groundtruth_run` | Multi-step groundtruth pipeline (queries + extended capture scope) | Phase 2 | **v0.2 planned** | Superset of `serp_capture`; Worker route `run` |
| `competitor_discovery` | Competitor set observation + snapshots | Phase 2 | **v0.2 planned** | Requires snapshot discipline; extends manifest |
| `landing_analysis` | Landing / CTA / trust surface capture | Phase 3 | **future** | Additional Worker sub-pipeline |
| `deep_research` | Long-running, multi-query, memory-backed research | Phase 4 | **future** | Extended TTL, optional `mig_session_memory` |
| `session_resume` | Continue interrupted session from prior `session_id` | Phase 2 | **v0.2 planned** | Requires `resume_from_session`; may reuse `parent_request_id` |
| `pack_retrieval` | Read-only fetch of session summary / pack pointer | Phase 1 | **v0.1 partial** (`/mig get`, `/mig status`) | Terminal at `completed` without new session artifacts; **no** new capture |

### Status by implementation wave

| Wave | Types |
|------|-------|
| **v0.1 implemented** | `serp_capture`; partial `pack_retrieval` |
| **v0.2 planned** | `groundtruth_run`, `competitor_discovery`, `session_resume`; full `pack_retrieval` |
| **future** | `landing_analysis`, `deep_research` |

### Default type resolution (adapters)

| Surface signal | Default `request_type` |
|----------------|------------------------|
| `/mig serp …`, spine test payload, serp webhook route | `serp_capture` |
| `/mig run …` | `groundtruth_run` (Phase 2; Phase 1 → reject or stub) |
| `/mig get …`, `/mig status …` | `pack_retrieval` |
| `--from-session` / `resume_from_session` | `session_resume` |

---

## 3. Required fields

Canonical Research Request object (logical JSON shape). Field paths use dot notation for nested keys.

| Field | Required | Meaning | Validation rule |
|-------|----------|---------|-----------------|
| `schema_version` | **Yes** | Contract version for this object | Must be `"0"`. Adapters reject unknown major versions. |
| `request_id` | **Yes** | Stable identifier for this intake attempt | Non-empty string; max 128 chars; pattern `{adapter}-{date}-{suffix}` recommended (e.g. `req-20260601-a1b2c3`). Must be unique among **active** requests (not yet terminal). Adapters generate if absent **before** submit. |
| `request_type` | **Yes** | Intent classifier (§2) | Must be one of defined enum values. v0.1 Worker **accepts** only `serp_capture` and read-only types (`pack_retrieval`); others → `rejected` or deferred stub. |
| `scope.niche` | **Yes** | Market vertical / service niche | Non-empty string after trim; max 500 chars. |
| `scope.region` | **Yes** | Geographic or locale scope | Non-empty string after trim. |
| `scope.business_type` | **Yes** | Business model class for capture context | Non-empty string; default adapter value `local_service` if omitted **only** at adapter layer before validation. |
| `scope.search_engine` | **Yes** | Target search engine | Non-empty string; normalized lowercase (e.g. `yandex`, `google`). |
| `scope.device` | **Yes** | Device context for SERP | Non-empty string; normalized lowercase (e.g. `mobile`, `desktop`). |
| `queries.seed_queries` | **Yes** | Seed query list | Non-empty array of non-empty strings after trim; v0.1 execution uses **first element only** (`query_used`). |
| `operator_id` | **Yes** | Human or service account owning the request | Non-empty string after trim. |
| `created_at` | **Yes** | Request creation timestamp | ISO-8601 UTC with timezone (`Z` or offset). |
| `source` | **Yes** | Intake provenance | Object; see §3.1. |

### 3.1 Required sub-object: `source`

| Subfield | Required | Meaning | Validation |
|----------|----------|---------|------------|
| `source.adapter` | **Yes** | Which adapter normalized this request | Enum: `webhook`, `task_file`, `mars_bridge`, `telegram`, `cli`, `cursor`, `api`, `unknown`. |
| `source.adapter_version` | **Yes** | Adapter semver or spine tag | Non-empty string (e.g. `"0.1"`). |
| `source.transport_ref` | No | Opaque handle to raw transport (message id, webhook id, task path) | String or null; **no secrets**. |

---

## 4. Optional fields

| Field | Meaning | Validation | Usage |
|-------|---------|------------|-------|
| `scope.city` | City-level localization | String or null after trim | Local pack / geo-sensitive capture |
| `capture_profile` | Named capture preset (provider params, depth) | String enum — **SAFE UNKNOWN** until v0.2 registry | Worker route selection |
| `manual_serp` | Operator-supplied SERP observation object | Non-null object when present; structure per manual SERP discipline | Bypasses provider; v0.1 supported |
| `provider_response` | Raw SERP provider payload (stub) | Object; field name **`provider_response`** canonical; legacy spine alias `serp_provider_response` | Normalized by Worker; not stored in request after session bind |
| `priority` | Operator priority hint | Enum: `low`, `normal`, `high` — default `normal` | Queue ordering (future); v0.1 ignored |
| `deadline` | Soft deadline for completion | ISO-8601 datetime | Reporting only in v0.1 |
| `downstream_context` | Opaque passthrough for operator notes (not ORCA semantics) | Object or string; max 8 KB | Must not contain interpreted clusters |
| `signals` | Structured hints (competitor URLs, known domains) | Array of strings or objects | Phase 2+; v0.1 stored in manifest if present |
| `parent_request_id` | Prior request in chain | Valid `request_id` | Resume, re-run, audit trail |
| `strict` | Fail closed on validation warnings | Boolean; default `false` | When `true`, warnings → `rejected` |
| `resume_from_session` | Existing `session_id` to continue | Pattern `^mig-[0-9]{8}-[a-f0-9]{6}$` | Required for `session_resume` |
| `status` | Request lifecycle state (§5) | Enum | Set by MIG/Worker; omitted → `draft` or `submitted` per adapter |
| `session_id` | Bound session | Pattern `^mig-[0-9]{8}-[a-f0-9]{6}$` | Set at `session_bound`; must be absent before acceptance in strict mode |
| `validation_errors` | Human-readable validation list | Array of strings | Set on `rejected` / failed validation |
| `request_status_message` | Operator-facing status line | String | UX adapters only |

---

## 5. Lifecycle

### Canonical request states

```text
draft
  ↓
submitted          ← adapter finished normalization
  ↓
validated          ← schema + business rules OK
  ↓
accepted           ← MIG acknowledged; lock/registry if applicable
  ↓
session_bound      ← session_id assigned; manifest initialized
  ↓
executing          ← capture / normalize / draft in progress
  ↓
completed          ← terminal success (capture types)
```

**Terminal branches:**

| State | Meaning |
|-------|---------|
| `failed` | Unrecoverable error (`validation_errors` or `failure_reason`) |
| `cancelled` | Operator or Admin cancel |
| `rejected` | Validation or policy gate failed before execution |

### State definitions

| State | Entry condition | Exit |
|-------|-----------------|------|
| `draft` | Adapter constructing object | `submitted` |
| `submitted` | Adapter handoff to MIG Intake/Worker | `validated` or `rejected` |
| `validated` | All required fields + rules pass | `accepted` or `rejected` |
| `accepted` | Concurrency + policy checks pass | `session_bound` or `cancelled` |
| `session_bound` | `session_id` written; session dir created | `executing` |
| `executing` | Worker pipeline active | `completed`, `failed`, or `cancelled` |
| `completed` | Pipeline terminal success | — |
| `failed` / `cancelled` / `rejected` | Terminal | — |

### Ownership transition (summary)

| Transition | From owner | To owner | Artifact |
|------------|------------|----------|----------|
| `draft` → `submitted` | Operator / Agent | Adapter | Research Request |
| `submitted` → `validated` | Adapter | MIG (validation) | Research Request |
| `validated` → `accepted` | MIG | MIG Intake / Admin (locks) | Research Request |
| `accepted` → `session_bound` | MIG | MIG Worker | Request + `session_id` |
| `session_bound` → `executing` | MIG Worker | MIG Worker | Session manifest |
| `executing` → `completed` | MIG Worker | Operator (review) | Session artifacts |
| `*` → `cancelled` | Operator / Admin | MIG Admin | Request + registry |
| Pack `approved` → ORCA | Operator (HITL) | ORCA (human handoff) | Approved pack — **outside** request lifecycle |

### v0.1 spine mapping (compatibility)

v0.1 **does not** persist Research Request as a separate file. It collapses:

```text
submitted → validated → session_bound → executing → completed
```

in one `validateIntake()` + `runSessionSpine()` call. Explicit `request_id`, `draft`, and `accepted` states are **contract targets** for v0.2+ adapters.

---

## 6. Ownership

| Stage / concern | Owner | Responsibilities |
|-----------------|-------|------------------|
| Request authoring | **Operator** (or delegated agent under human charter) | Correct scope, queries, business context |
| Adapter normalization | **Adapter** (transport) | Map transport → canonical object; set `source`; generate `request_id` |
| Validation | **MIG** (validation layer / Worker entry) | Required fields, enums, strict mode |
| Acceptance + locks | **MIG Intake** (+ Sheets registry in runtime design) | Concurrency, ack UX, dispatch |
| Session binding + execution | **MIG Worker** | `session_id`, manifest, SERP, draft pack |
| Cancel / health / locks | **MIG Admin** | Operational control; no capture |
| Pack review + approval | **Operator** (human) | HITL; `Approved By` |
| ORCA intake | **ORCA operator** | Interpret approved pack only |
| Future MARS runtime | **MARS runtime** (experimental) | May **submit** requests via adapters; **must not** replace MIG validation or approve packs |

**ORCA never owns:** request validation, session execution, SERP capture, or pack approval.

---

## 7. Approval gates

| Gate | Auto-accept allowed? | Authority | Notes |
|------|----------------------|-----------|-------|
| Schema + required fields | **Yes** | MIG validation | Fails → `rejected` |
| `serp_capture` scope sanity | **Yes** (v0.1) | MIG Worker | Warnings unless `strict: true` |
| Concurrency lock | **Yes** if no active lock | MIG Intake | Else busy / defer |
| `groundtruth_run`, `competitor_discovery`, `landing_analysis`, `deep_research` | **No** (v0.1) | Human charter + Worker route availability | Stub or reject until phase |
| Session start (filesystem write) | **Yes** after `validated` | MIG Worker | Creates session dir |
| Draft pack promotion to `review` | **No** | Operator | Manual / Phase 2 UX |
| Pack `approved` | **No** | **Human operator only** | Mandatory `Approved By` per ORCA handoff |
| ORCA consumption | **No** | ORCA operator + human handoff | Approved pack required |
| Semantic / campaign decisions | **Never auto** | — | **ORCA can never approve** MIG intake or substitute missing groundtruth |

**ORCA can never approve:**

- Research Request acceptance (capture intent)
- Session execution start
- Draft pack as production input
- Filling SAFE UNKNOWN without human sign-off

---

## 8. Adapter mapping

All adapters produce the **same canonical object** (§3–4). Normalization path:

```text
Transport input
  → parse surface-specific
  → map fields to canonical paths
  → set source.adapter / source.adapter_version
  → assign request_id (if missing)
  → set request_type (explicit or inferred)
  → status: submitted
  → MIG validate → …
```

### 8.1 Webhook Adapter

| Transport | Normalization |
|-----------|---------------|
| HTTP POST JSON body | Body may be flat (legacy) or canonical. Extract `body` wrapper if present (n8n pattern). Map flat keys → `scope.*`, `queries.seed_queries`. Set `source.adapter=webhook`, `transport_ref=webhook_execution_id`. |

### 8.2 Task File Adapter

| Transport | Normalization |
|-----------|---------------|
| JSON/YAML file in task scope | Read file → canonical object. `source.adapter=task_file`, `transport_ref=relative path`. |

### 8.3 MARS Bridge Adapter

| Transport | Normalization |
|-----------|---------------|
| Bridge envelope `{ task_id, run_id, payload, … }` | Extract nested `payload` (or agreed key) as intake body. Map to canonical. `source.adapter=mars_bridge`, `transport_ref=task_id`. **Do not** treat bridge stub fields as scope. |

### 8.4 Telegram Adapter

| Transport | Normalization |
|-----------|---------------|
| `/mig serp …` parsed tokens | Map `ниша=`/`niche=` → `scope.niche`, etc. (see n8n node spec). `request_type=serp_capture`. `source.adapter=telegram`, `transport_ref=chat_id:message_id`. **Command text is not stored** as canonical — only parsed fields. |

### 8.5 CLI Adapter

| Transport | Normalization |
|-----------|---------------|
| File arg or stdin JSON | v0.1 **legacy flat** keys (`niche`, `region`, …) accepted. Adapter wraps into canonical shape before spine OR spine-compat layer flattens for `validateIntake()`. `source.adapter=cli`. |

### 8.6 Cursor Adapter

| Transport | Normalization |
|-----------|---------------|
| Agent-produced JSON in repo | Same as Task File; `source.adapter=cursor`, `transport_ref=task or chat ref`. |

### Legacy flat → canonical map (v0.1 spine compat)

| Legacy (flat) | Canonical |
|---------------|-----------|
| `niche` | `scope.niche` |
| `region` | `scope.region` |
| `city` | `scope.city` |
| `business_type` | `scope.business_type` |
| `search_engine` | `scope.search_engine` |
| `device` | `scope.device` |
| `seed_queries` | `queries.seed_queries` |
| `operator_id` | `operator_id` |
| `manual_serp` | `manual_serp` |
| `serp_provider_response` | `provider_response` |

---

## 9. Session binding

### Relationship

- **One Research Request** (capture types) binds to **at most one primary Research Session** per acceptance.
- **`request_id`** identifies the intake attempt across transport and logs.
- **`session_id`** identifies the filesystem session folder and manifest (pattern `mig-YYYYMMDD-{hex6}`).

### Can they differ?

**Yes — by design.**

| Identifier | When assigned | Purpose |
|------------|---------------|---------|
| `request_id` | At adapter submit (before or at validation) | Audit, idempotency, parent chains |
| `session_id` | At `session_bound` (v0.1: inside `validateIntake()`) | Artifact paths, manifest SoT |

v0.1 spine generates `session_id` **inside** `validateIntake()` immediately — it does **not** yet separate request persistence from session creation. v0.2+ should assign `request_id` first, then bind `session_id` at `session_bound`.

### Lifecycle interaction

| Request state | Session state (manifest `stage`) |
|---------------|----------------------------------|
| `session_bound` | `intake_complete` (v0.1) / `intake_validated` (runtime design) |
| `executing` | `collecting` → `normalizing` → `drafting` |
| `completed` | `draft_complete` (v0.1 terminal) |
| `failed` / `cancelled` | Session may be partial; manifest records failure |

### Read-only types

`pack_retrieval` may **reference** existing `session_id` via `resume_from_session` or adapter argument **without** creating a new session. Request completes at `completed` with retrieval payload only.

### Resume

`session_resume` requires `resume_from_session` = existing `session_id`. New `request_id`; same `session_id`. Parent link via `parent_request_id` optional.

---

## 10. Compatibility

### MIG v0.1 Session Spine

| Aspect | Compatibility |
|--------|---------------|
| `validate-intake.js` | Validates **legacy flat** required fields: `niche`, `region`, `business_type`, `seed_queries`, `search_engine`, `device`, `operator_id`. Maps to canonical §3 via §8.6. |
| `run-session-spine.js` | Assumes validated intake → immediate session creation. Equivalent to `serp_capture` fast-path. |
| `session_manifest.json` | Session artifact; **not** a Research Request. Scope/queries mirror accepted request fields. |
| Monolith webhook | Webhook Adapter → flat body → spine (unchanged until adapter layer inserted). |

### Research Pack lifecycle

Request **`completed`** does **not** mean pack **`approved`**. Pack lifecycle remains independent — [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md).

### ORCA handoff contract

ORCA receives **approved pack + manifest**, not Research Request. Request fields inform scope in manifest; handoff minimum per [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md).

### Future MARS runtime

Runtime may enqueue Research Requests through adapters. **Must** reference this contract version (`schema_version: "0"`). **Must not** claim execution without MIG Worker evidence. No automated ORCA approval.

---

## 11. Explicit non-goals

This contract is **not**:

- A workflow or n8n node graph
- A Telegram message format specification (see adapter mapping only)
- A transport protocol (HTTP, webhook paths, Telegram API)
- An OpenRouter or LLM request schema
- A Research Pack schema or template
- An ORCA task or R2 analysis envelope
- A MARS Task replacement
- An automated approval or policy engine
- A JSON Schema file (may be added later; **not** part of v0)
- Proof that all adapters are implemented

---

## Related

| Document | Path |
|----------|------|
| Research Pack | [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) |
| Competitor Discovery | [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) |
| ORCA handoff | [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) |
| Boundaries | [../boundaries.md](../boundaries.md) |
| Session spine | [../lib/session-spine/](../lib/session-spine/) |
| Intake validation (v0.1) | [../lib/session-spine/validate-intake.js](../lib/session-spine/validate-intake.js) |
| Session manifest schema | [../schemas/session-manifest-v0.1.schema.json](../schemas/session-manifest-v0.1.schema.json) |
| Runtime design | [../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) |
| n8n node spec | [../reports/REPORT-mig-n8n-node-level-specification-v1.md](../reports/REPORT-mig-n8n-node-level-specification-v1.md) |

---

*Contract v0 — documentation only. No adapter implementation. No git commit by default.*
