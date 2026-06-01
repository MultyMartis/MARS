# MIG Runtime Assembly v1

**Status:** **documented** — canonical end-to-end runtime architecture (assembly contract).  
**Not:** implementation, deployment, n8n workflow export, JSON Schema registry engine, provider setup, OpenRouter setup, ORCA redesign, or Website Factory redesign.

**Supersedes:** Ad-hoc «phase» language scattered across subsystem contracts without a single session lifecycle.  
**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md); subsystem contracts (competitor, multi-query, website, landing, keyword, deep research, research pack); [../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md); [../reports/REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md).  
**Downstream:** Future `session-manifest-v0.2.schema.json`; Worker route design; spine orchestration backlog.

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

---

## 1. Purpose

### 1.1 Problem statement

MIG capabilities (Research Request, SERP capture, Competitor Discovery, Multi-Query Discovery, Website Acquisition, Landing Analysis, Keyword Intelligence, Deep Research, Research Pack) exist as **designed subsystems** and **partial libraries**. There is **no** single documented contract for how a **complete research session** executes from intake to **approved** Research Pack.

This document defines **MIG Runtime Assembly** — the canonical lifecycle, phase graph, artifact flow, session manifest model, orchestration boundaries, failure semantics, approval gates, session outputs, MVP honesty, and phased roadmap.

### 1.2 What Runtime Assembly is

| Aspect | Definition |
|--------|------------|
| **Runtime Assembly** | The ordered composition of intake, acquisition passes, pack projection, and HITL approval for one `session_id` |
| **Research Session** | Bounded execution unit; filesystem folder under `{MIG_SESSION_ROOT}/{session_id}/` |
| **Session Spine** | Minimal orchestrator that **must** run for every session — intake validation, manifest SoT, terminal artifact registration |
| **Passes** | Unit-testable Node modules (competitor, website, landing, keyword, deep research) invoked by spine or Worker **after** upstream artifacts exist |
| **Research Pack** | Logical output product; **projected** from artifacts + manifest; lifecycle **independent** from `session_manifest.stage` |

### 1.3 What Runtime Assembly is not

- Not a new acquisition subsystem
- Not proof of production n8n/Telegram deployment
- Not automated approval or ORCA transport
- Not MARS runtime orchestration product

---

## 2. Canonical runtime lifecycle

### 2.1 End-to-end flow (normative)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  TRANSPORT (adapters — not session-internal)                                 │
│  Task File · Telegram · Webhook · CLI · MARS Bridge                          │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  P0  REQUEST INTAKE          Research Request validated & session-bound      │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  P1  SEARCH ACQUISITION      serp_result.json (+ optional serp_index bundle) │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  P2  COMPETITOR DISCOVERY    competitors.json (derived from SERP)           │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    ▼
                    ┌───────────────┴───────────────┐
                    │  P3  WEBSITE ACQUISITION       │  (optional by profile)
                    │  website_snapshots.json      │
                    └───────────────┬───────────────┘
                                    ▼
                    ┌───────────────┴───────────────┐
                    │  P4  LANDING ANALYSIS          │  (optional; needs P3)
                    │  landing_observations.json     │
                    └───────────────┬───────────────┘
          ┌─────────────────────────┴─────────────────────────┐
          │  P-K  KEYWORD INTELLIGENCE (parallel optional)     │
          │  keyword_registry.json / wordstat / suggestions    │
          └─────────────────────────┬─────────────────────────┘
                                    ▼
                    ┌───────────────┴───────────────┐
                    │  P5  DEEP RESEARCH             │  (optional; needs min bundle)
                    │  research_findings.json        │
                    └───────────────┬───────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  P6  RESEARCH PACK ASSEMBLY  research_pack.draft.md (+ future .json)        │
│       pack_state: draft · session stage: draft_complete                      │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  P7  APPROVAL (HITL)         review → approved → published                   │
│       pack_state independent · human Approved By mandatory for ORCA          │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  P8  CONSUMPTION / ARCHIVE   consumed (ORCA ack) → archived                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Terminal success definitions

| Terminal | `session_manifest.stage` | `pack_state` | ORCA-eligible |
|----------|--------------------------|--------------|---------------|
| **Draft session complete** | `draft_complete` | `draft` | **No** |
| **Approved pack** | `draft_complete` or `assembly_complete` | `approved` | **Yes** (after human handoff bundle) |
| **Published handoff** | unchanged | `published` | **Yes** (pickup marker) |
| **Consumed** | optional `handoff_complete` | `consumed` | Historical |
| **Partial session** | `partial_complete` | `draft` or `failed` | **No** |
| **Failed session** | `failed` | `failed` | **No** |

**Rule:** Research Request `completed` means **session pipeline finished** (including `draft_complete`). It does **not** mean pack `approved`.

### 2.3 Request type → runtime profile

| `request_type` | Phases executed (minimum) | Notes |
|----------------|---------------------------|-------|
| `serp_capture` | P0 → P1 → P2 → P6 | v0.1 spine default |
| `groundtruth_run` | P0 → P1 → P2 → (P3,P4 opt) → P6 | Multi-query when `capture_profile` requires |
| `competitor_discovery` | P0 → P1 → P2 → P6 | Emphasis on P2; still needs SERP |
| `landing_analysis` | P0 → P1 → P2 → P3 → P4 → P6 | Website pass mandatory |
| `deep_research` | Full stack through P5 → P6 | P5 gated on upstream bundle |
| `session_resume` | From last `manifest.phase` checkpoint | Re-run failed/skipped passes only |
| `pack_retrieval` | **None** (read-only) | No new artifacts |

---

## 3. Runtime phases (final lifecycle)

### 3.1 Phase evaluation (charter phases → assembly phases)

| Charter # | Charter name | **Assembly ID** | Verdict |
|-----------|--------------|-----------------|---------|
| 1 | Request Intake | **P0** | **Mandatory** — always first; adapter + spine validation |
| 2 | Search Acquisition | **P1** | **Mandatory** for all capture types — `serp_result.json` SoT |
| 3 | Competitor Discovery | **P2** | **Mandatory** for `groundtruth_run` and above; **default-on** in spine v0.1 after P1 (may yield `empty`) |
| 4 | Website Acquisition | **P3** | **Optional** — `capture_profile` / `request_type` |
| 5 | Landing Analysis | **P4** | **Optional** — requires P3 success for structured landing SoT |
| 6 | Deep Research | **P5** | **Optional** — synthesis only; never substitutes acquisition |
| 7 | Research Pack | **P6** | **Mandatory** — projection pass; may re-run after any pass |
| 8 | Approval | **P7** | **Mandatory for ORCA** — never automated in MVP |
| — | Keyword Intelligence | **P-K** | **Optional parallel** — not numbered in spine order; see §3.3 |

**Dropped as separate runtime phase:** «Multi-Query Discovery» is **not** a standalone phase — it is a **mode of P1** (multiple SERP artifacts + `serp_index.json`) feeding **P2**.

### 3.2 Phase specifications

#### P0 — Request Intake

| Attribute | Value |
|-----------|-------|
| **Inputs** | Research Request (adapter-normalized) |
| **Outputs** | Session folder created; `session_manifest.json` initial (`stage=intake_complete`) |
| **SoT** | Research Request fields copied to manifest `scope`, `queries` — request file is **not** session SoT |
| **Failure** | Validation error → no session dir; request → `failed` in drop zone |
| **Implementation** | Task File Adapter + `validate-intake.js` — **implemented** |

#### P1 — Search Acquisition

| Attribute | Value |
|-----------|-------|
| **Inputs** | Seeds, scope, optional `manual_serp` / provider response |
| **Outputs** | `serp_result.json`; optional `serp_index.json` + `serp_results/{query_id}.json` |
| **Manifest** | `serp.mode`, `serp.captured_at`; `stage` via `acquiring_serp` → `serp_complete` |
| **Failure** | Provider fail → `fallback` + SAFE UNKNOWN — session **continues** (v0.1 proven) |
| **Implementation** | `normalize-serp.js` in spine — **implemented**; live provider — **not** |

#### P2 — Competitor Discovery

| Attribute | Value |
|-----------|-------|
| **Inputs** | `serp_result.json` or multi-query bundle |
| **Outputs** | `competitors.json` |
| **Manifest** | `competitor_discovery.status` ∈ `complete` \| `empty` \| `skipped` |
| **Failure** | Empty SERP → `empty` + SAFE UNKNOWN — **not** session-fatal |
| **Implementation** | `discover-from-serp` + `write-competitors-artifact` in spine — **implemented**; multi-query loop in spine — **partial** (library supports bundle; spine single-query) |

#### P3 — Website Acquisition

| Attribute | Value |
|-----------|-------|
| **Inputs** | `competitors.json`, URL plan rules |
| **Outputs** | `website_snapshots.json`, `snapshots/sites/{snapshot_id}/*` |
| **Manifest** | `website_acquisition` block; `stage` `acquiring_sites` → `sites_complete` |
| **Failure** | Per-URL `failed`/`skipped`; session may be `partial_complete` |
| **Implementation** | `lib/website-acquisition/*` + verify script — **implemented**; **not** wired to spine |

#### P4 — Landing Analysis

| Attribute | Value |
|-----------|-------|
| **Inputs** | `website_snapshots.json` + snapshot HTML |
| **Outputs** | `landing_observations.json`, `landings/{landing_id}/landing_observation.json` |
| **Manifest** | `landing_analysis` block |
| **Failure** | No snapshots → pass `skipped` + SAFE UNKNOWN |
| **Implementation** | `lib/landing-analysis/*` + verify script — **implemented**; **not** wired to spine; OPERATIONAL-INDEX stale on this point |

#### P-K — Keyword Intelligence (optional)

| Attribute | Value |
|-----------|-------|
| **When** | After P1 or in parallel with P3; never before SERP for seed anchoring |
| **Outputs** | `keyword_registry.json`, optional Wordstat/suggestion snapshots |
| **Rule** | Phrases as **captured surfaces** — no clustering (ORCA) |
| **Implementation** | Architecture only — [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) |

#### P5 — Deep Research

| Attribute | Value |
|-----------|-------|
| **Inputs** | Minimum bundle per [mig-deep-research-architecture-v1.md](mig-deep-research-architecture-v1.md) §2.2 |
| **Outputs** | `research_findings.json` |
| **Gate** | Missing `serp_result.json` or `competitors.json` → **fail closed** |
| **Implementation** | Architecture only |

#### P6 — Research Pack Assembly

| Attribute | Value |
|-----------|-------|
| **Inputs** | All completed pass artifacts + manifest |
| **Outputs** | `research_pack.draft.md` (v0.1); future `research_pack.json` |
| **Manifest** | `stage=draft_complete`, `mig_phase` = highest represented phase (1–4) |
| **Rule** | Pack **projects** artifacts — does not invent SERP/landing facts |
| **Re-run** | After any pass completes, operator or Worker may re-invoke assembly only |
| **Implementation** | `build-research-pack.js` in spine — **implemented** for P1+P2; partial projection for P3/P4/P5 |

#### P7 — Approval

| Attribute | Value |
|-----------|-------|
| **Inputs** | Draft pack + artifact registry |
| **Outputs** | `research_pack.review.md` (optional edit), `research_pack.approved.md`, manifest `pack_state`, `approved_by`, `approved_at` |
| **Authority** | **Human operator only** — Worker forbidden from `approved` |
| **Implementation** | Contract only — [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) §6 |

#### P8 — Consumption / Archive

| Attribute | Value |
|-----------|-------|
| **Trigger** | ORCA operator acknowledges intake |
| **Outputs** | `pack_state=consumed` → `archived`; optional `handoff_bundle.json` checksum manifest |
| **Implementation** | Not implemented |

### 3.3 `session_manifest.stage` vocabulary (target v0.2)

| Stage | Phase | Notes |
|-------|-------|-------|
| `intake_complete` | P0 done | v0.1 exists |
| `acquiring_serp` | P1 in progress | v0.2 target |
| `serp_complete` | P1 done | v0.2 target |
| `discovering_competitors` | P2 in progress | v0.2 target |
| `competitors_complete` | P2 done | v0.2 target |
| `acquiring_sites` | P3 in progress | per website contract |
| `sites_complete` | P3 done | |
| `analyzing_landings` | P4 in progress | |
| `landings_complete` | P4 done | |
| `acquiring_keywords` | P-K in progress | optional |
| `synthesizing` | P5 in progress | |
| `synthesis_complete` | P5 done | |
| `assembling_pack` | P6 in progress | |
| `draft_complete` | P6 terminal (draft) | **v0.1 terminal today** |
| `partial_complete` | Mixed pass outcomes | explicit partial |
| `failed` | Unrecoverable | |
| `handoff_complete` | P8 marker | optional |

**v0.1 reality:** only `intake_complete` → `draft_complete` (atomic jump in `finalizeManifest`).

### 3.4 `session_manifest.phase` (cursor for resume)

String enum mirroring highest **started** assembly phase: `intake` | `search` | `competitors` | `websites` | `landings` | `keywords` | `deep_research` | `pack` | `approval` | `handoff`.

Distinct from `mig_phase` (1–4 pack depth) in Research Pack contract.

---

## 4. Artifact flow

### 4.1 Principle

**Artifacts remain Source of Truth.** Research Pack and markdown representations are **projections**. Deep Research findings reference artifacts — do not replace them.

### 4.2 Relationship diagram

```text
Research Request (intake — external to session folder until bound)
    │
    │  request_id, scope, queries, request_type, capture_profile
    ▼
session_manifest.json ◄────────────────────────────────────────────┐
    │ registers paths, stages, pack_state, safe_unknown[], coverage │
    │                                                                │
    ├──► serp_result.json ◄── P1 Search Acquisition                 │
    │         │                                                    │
    │         ├──► (optional) serp_index.json + serp_results/*    │
    │         │                                                    │
    │         ▼                                                    │
    ├──► competitors.json ◄── P2 Competitor Discovery (derived)     │
    │         │                                                    │
    │         ├──────────────────┐                                 │
    │         ▼                  ▼                                 │
    ├──► website_snapshots.json   keyword_registry.json (optional) │
    │         │                  │                                 │
    │         ▼                  │                                 │
    ├──► snapshots/sites/*        │                                 │
    │         │                  │                                 │
    │         ▼                  │                                 │
    ├──► landing_observations.json                                │
    │         │                                                    │
    │         ▼                                                    │
    ├──► landings/*/landing_observation.json                      │
    │         │                                                    │
    │         ├──────────────────┘                                 │
    │         ▼                                                    │
    ├──► research_findings.json ◄── P5 Deep Research (optional)    │
    │         │                                                    │
    │         ▼                                                    │
    └──► research_pack.draft.md ──► .review.md ──► .approved.md    │
              (P6 projection)              (P7 HITL)                │
```

### 4.3 Artifact dependency matrix

| Artifact | Produced by | Requires | Referenced by |
|----------|-------------|----------|---------------|
| `session_manifest.json` | P0 spine | Research Request | All passes, pack, ORCA handoff |
| `serp_result.json` | P1 | P0 | P2, P6, P5 |
| `serp_index.json` | P1 (multi) | P0 | P2 multi mode |
| `competitors.json` | P2 | P1 | P3, P6, P5 |
| `website_snapshots.json` | P3 | P2 (URLs) | P4, P6, P5 |
| `snapshots/sites/*` | P3 | P2 | P4, evidence refs |
| `landing_observations.json` | P4 | P3 | P6, P5 |
| `landings/*` | P4 | P3 | P6, P5 |
| `keyword_registry.json` | P-K | P1 | P5, P6 |
| `research_findings.json` | P5 | P1+P2 (+ conditional P3/P4) | P6 |
| `research_pack.*.md` | P6 / P7 | All applicable upstream | ORCA handoff |

### 4.4 Provenance rules

1. **Downstream may summarize upstream** — never overwrite upstream JSON.
2. **IDs are stable** within session (`competitor_id`, `snapshot_id`, `landing_id`, `finding_id`).
3. **SAFE UNKNOWN** propagates: union of pass-level + manifest + pack section at approval.
4. **Orphan artifacts** (file exists but manifest registry missing) → session `partial_complete` + validation warning.

---

## 5. Session manifest model

### 5.1 Role

`session_manifest.json` is the **session execution Source of Truth**: identity, runtime cursor, artifact registry, coverage, errors, SAFE UNKNOWN aggregate, approval state, and operational metadata.

It is **not** the Research Pack object — see [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md).

### 5.2 Schema versioning

| Version | Status |
|---------|--------|
| **v0.1** | **Implemented** — [session-manifest-v0.1.schema.json](../schemas/session-manifest-v0.1.schema.json); stages `intake_complete`, `draft_complete` only |
| **v0.2** | **Target** — additive fields below; proposed `session-manifest-v0.2.schema.json` (not implemented) |

### 5.3 Canonical `session_manifest.json` (v0.2 target shape)

```json
{
  "schema_version": "0.2",
  "session_id": "mig-20260601-ce1557",
  "request_id": "req-20260601-smoke01",
  "created_at": "2026-06-01T06:22:57.391Z",
  "updated_at": "2026-06-01T07:15:00.000Z",

  "stage": "draft_complete",
  "phase": "pack",
  "runtime_profile": "groundtruth_run",

  "operator_id": "op-test-001",
  "request_type": "serp_capture",
  "capture_profile": {
    "multi_query": false,
    "website_pass": false,
    "landing_pass": false,
    "keyword_pass": false,
    "deep_research_pass": false
  },

  "scope": {
    "niche": "…",
    "region": "…",
    "city": null,
    "business_type": "local_service",
    "search_engine": "yandex",
    "device": "mobile"
  },

  "queries": {
    "seed_queries": ["…"],
    "query_used": "…",
    "query_set": [],
    "queries_executed": []
  },

  "serp": {
    "mode": "fallback",
    "captured_at": "2026-06-01T06:22:57.392Z",
    "result_file": "serp_result.json",
    "discovery_mode": "single"
  },

  "competitor_discovery": {
    "status": "empty",
    "competitor_count": 0,
    "discovery_mode": "single",
    "query_coverage": "complete",
    "generated_at": "…",
    "artifact_file": "competitors.json"
  },

  "website_acquisition": {
    "status": "skipped",
    "snapshots_planned": 0,
    "snapshots_success": 0,
    "artifact_file": "website_snapshots.json"
  },

  "landing_analysis": {
    "status": "skipped",
    "landings_analyzed": 0,
    "artifact_file": "landing_observations.json"
  },

  "keyword_intelligence": {
    "status": "skipped",
    "artifact_file": "keyword_registry.json"
  },

  "deep_research": {
    "status": "skipped",
    "artifact_file": "research_findings.json"
  },

  "pack": {
    "pack_state": "draft",
    "mig_phase": "2",
    "draft_file": "research_pack.draft.md",
    "approved_file": null,
    "approved_by": null,
    "approved_at": null,
    "published_at": null,
    "consumed_at": null
  },

  "artifacts": {
    "session_manifest": "session_manifest.json",
    "serp_result": "serp_result.json",
    "serp_index": null,
    "competitors": "competitors.json",
    "website_snapshots": null,
    "landing_observations": null,
    "keyword_registry": null,
    "research_findings": null,
    "research_pack_draft": "research_pack.draft.md"
  },

  "coverage": {
    "session_grade": "D",
    "phases_completed": ["intake", "search", "competitors", "pack"],
    "phases_skipped": ["websites", "landings", "keywords", "deep_research"],
    "phases_failed": [],
    "partial": true
  },

  "errors": [],
  "safe_unknown": [
    "SERP provider unavailable — fallback mode"
  ],

  "runtime_metadata": {
    "spine_version": "0.1",
    "session_root": "{MIG_SESSION_ROOT}",
    "last_pass": "competitor_discovery",
    "orchestrator": "session_spine",
    "n8n_execution_id": null
  }
}
```

### 5.4 Field groups (normative)

| Group | Purpose |
|-------|---------|
| **Session identity** | `session_id`, `request_id`, timestamps |
| **Status** | `stage`, `phase`, `runtime_profile` |
| **Scope & queries** | Copied from accepted request — session-bound |
| **Pass blocks** | `serp`, `competitor_discovery`, `website_acquisition`, `landing_analysis`, `keyword_intelligence`, `deep_research` — each with `status` |
| **Pack block** | `pack_state`, `mig_phase`, file pointers, approval fields |
| **artifacts** | Map of **relative paths** — null = not produced |
| **coverage** | `session_grade`, phase lists, `partial` flag |
| **errors** | Structured pass failures (code, pass, message, recoverable) |
| **safe_unknown** | Aggregated gap register — **must** sync to pack at approval |
| **runtime_metadata** | Non-domain operational hints — not ORCA input |

### 5.5 `pack_state` on manifest (target)

Per Research Pack contract §6.4 — manifest is **primary SoT** for `pack_state`. v0.1 infers `draft` when `research_pack.draft.md` exists.

### 5.6 Backward compatibility

v0.2 consumers **must** read v0.1 manifests: missing pass blocks imply `skipped`; missing `pack.pack_state` implies `draft`.

---

## 6. Execution orchestration

### 6.1 Session Spine (always runs)

| Responsibility | Module (evidenced) |
|----------------|-------------------|
| Intake validation | `validate-intake.js` |
| Manifest create/finalize | `create-manifest.js` |
| SERP normalize | `normalize-serp.js` |
| Competitor pass (inline) | `discover-from-serp`, `write-competitors-artifact` |
| Pack draft | `build-research-pack.js` |
| Atomic write | `write-artifacts.js` |
| Entry | `run-session-spine.js`, Task File Adapter |

**Spine v0.1 executes:** P0 + P1 + P2 + P6 in **one synchronous call** — no mid-session checkpoint.

### 6.2 Passes (invoked after spine or by extended orchestrator)

| Pass | CLI / module pattern | Invoked by |
|------|----------------------|------------|
| Website | `run-website-pass.js {sessionDir}` | Worker route / future `run-runtime.js` |
| Landing | `run-landing-pass.js {sessionDir}` | After website |
| Keyword | (planned) | Worker optional route |
| Deep Research | (planned) | Worker after min bundle |
| Pack re-assembly | `build-research-pack` only | After any pass |

Passes **must** update manifest via shared `update-manifest-pass.js` (backlog) — today passes used only in verify scripts may write artifacts without manifest sync (**gap**).

### 6.3 Optional phases (may skip)

| Phase | Skip when |
|-------|-----------|
| P3 Website | `capture_profile.website_pass=false` or `serp_capture` only |
| P4 Landing | No successful snapshots or profile off |
| P-K Keyword | Not chartered; no operator seeds for Wordstat |
| P5 Deep Research | `request_type` < deep_research; missing upstream |
| P7 Approval | Never skipped for ORCA — may be **deferred** indefinitely while draft exists |

### 6.4 Must never skip

| Requirement | Rationale |
|-------------|-----------|
| P0 Intake validation | No orphan sessions |
| P1 SERP artifact | P2 and pack SERP section require file (fallback allowed) |
| P6 Pack assembly | Session without pack is incomplete product |
| SAFE UNKNOWN section in pack | Contract §6 — even if empty array with explicit «none» only when truly complete |
| Human `approved` before ORCA | Handoff contract |

**P2 Competitor pass:** spine **always runs** discovery; `empty` is valid — do not skip writing `competitors.json`.

### 6.5 Orchestration surfaces (design — not implemented as unified runtime)

| Surface | Role |
|---------|------|
| **Session Spine** | MVP single-shot pipeline |
| **Task File Adapter** | Intake + invoke spine |
| **MIG Worker (n8n)** | Future: phase loop, pass dispatch, Telegram status |
| **MIG Intake / Admin** | Locks, approval commands — per runtime design report |
| **Human CLI** | `run-website-pass`, verify scripts — today |

### 6.6 Recommended orchestration sequence (full profile)

```text
1. adapter → validate → create session dir
2. manifest.stage = intake_complete
3. P1 SERP → serp_complete
4. P2 competitors → competitors_complete
5. [optional] P3 websites → sites_complete
6. [optional] P4 landings → landings_complete
7. [optional] P-K keywords
8. [optional] P5 deep research → synthesis_complete
9. P6 assemble_pack → draft_complete
10. operator P7 approval (out of band)
11. P8 consume/archive (out of band)
```

---

## 7. Failure model

### 7.1 Failure taxonomy

| Class | `errors[].code` example | Session outcome | Pack rule |
|-------|-------------------------|-----------------|-----------|
| **Fatal intake** | `INTAKE_INVALID` | No session / request failed | No pack |
| **SERP failed (no fallback)** | `SERP_UNAVAILABLE` | `failed` | No pack or `failed` |
| **SERP degraded** | `SERP_FALLBACK` | Continue | Draft with grade D + SAFE UNKNOWN |
| **Competitor empty** | — | Continue | `empty` status — not failure |
| **Website partial** | `WEBSITE_PARTIAL` | `partial_complete` | Draft allowed; sections X + SAFE UNKNOWN |
| **Landing unavailable** | `LANDING_SKIPPED` | Continue | «Landing Analysis pass not executed» |
| **Deep Research unavailable** | `DEEP_RESEARCH_SKIPPED` | Continue | `mig_phase` < 4; findings absent |
| **Pack assembly error** | `PACK_ASSEMBLY_FAILED` | `failed` | `pack_state=failed` |
| **LLM synthesis fail** | `DEEP_RESEARCH_LLM_FAILED` | `partial_complete` | No fabricated findings |

### 7.2 Recovery rules

| Scenario | Recovery |
|----------|----------|
| SERP fallback | Operator may supply `manual_serp` + `session_resume` |
| Website URL blocked | Skip URL; continue plan; record per-snapshot `failed` |
| Pass crashed mid-session | `session_resume` from `manifest.phase` + re-run pass only |
| Bad draft pack | Operator `review` → regenerate P6 from artifacts (not re-capture) |
| Approved pack revoked | `pack_state=revoked` → `review` — artifacts immutable |

### 7.3 Fallback rules

1. **SERP:** manual import > provider > fallback stub (v0.1).
2. **Website:** static HTTP only in MVP — no Playwright unless flagged.
3. **Deep Research:** if LLM unavailable, omit `research_findings.json` — do **not** fill pack with LLM prose.

### 7.4 SAFE UNKNOWN behavior

| Event | Action |
|-------|--------|
| Any pass skips | Append manifest `safe_unknown[]` with pass-specific string |
| Pack assembly | Merge manifest + pass unknowns into pack §SAFE UNKNOWN |
| Approval | Operator **may add** — must not delete without audit note |
| ORCA | Must preserve all entries |

### 7.5 Pack generation rules (partial session)

| Condition | Allow `research_pack.draft.md`? |
|-----------|--------------------------------|
| `serp_result.json` exists | **Yes** (minimum) |
| P3 skipped by profile | **Yes** — landing sections SAFE UNKNOWN |
| P3 failed all URLs | **Yes** — `partial_complete` |
| P5 skipped | **Yes** — `mig_phase` < 4 |
| No `serp_result.json` | **No** — `failed` |

**Normative:** Partial ≠ unapproved. ORCA still rejects non-`approved` packs.

---

## 8. Approval model

### 8.1 Pack states (from Research Pack contract)

```text
draft → review → approved → published → consumed → archived
         ↓                    ↓
       failed              revoked → review
```

### 8.2 State definitions (runtime assembly view)

| State | Artifact representation | Session manifest |
|-------|----------------------|------------------|
| **Draft Pack** | `research_pack.draft.md` | `pack_state=draft`, `stage=draft_complete` |
| **Review** | Optional `research_pack.review.md` (operator edit) | `pack_state=review` |
| **Approved Pack** | `research_pack.approved.md` | `pack_state=approved`, `approved_by`, `approved_at` |
| **Published** | Same approved file + handoff marker | `pack_state=published`, `published_at` |
| **Consumed Pack** | Immutable approved snapshot | `pack_state=consumed`, `consumed_at` |
| **Archived Pack** | Session moved/read-only policy | `pack_state=archived` |

### 8.3 Ownership model

| Concern | Owner |
|---------|-------|
| Draft content generation | MIG Worker / spine |
| Review edits | **Operator** |
| Approval (`Approved By`) | **Operator** — mandatory for ORCA |
| Publish handoff | **Operator** |
| Consumption ack | **ORCA operator** (flag); **MIG operator** writes manifest |
| Artifact SoT | **MIG** filesystem |
| Semantic interpretation | **ORCA** only |

### 8.4 Forbidden

- Worker → `approved`
- ORCA → write MIG session files
- `draft` → ORCA production input

---

## 9. Runtime outputs

### 9.1 Session folder layout (full profile target)

```text
{MIG_SESSION_ROOT}/{session_id}/
  session_manifest.json          [required]
  serp_result.json               [required]
  competitors.json               [required — may be empty array]
  research_pack.draft.md         [required at draft_complete]
  website_snapshots.json         [optional]
  snapshots/sites/…              [optional]
  landing_observations.json      [optional]
  landings/…                     [optional]
  research_findings.json         [optional]
  research_pack.review.md        [optional]
  research_pack.approved.md      [required for ORCA]
  serp_index.json                [optional multi-query]
  serp_results/                  [optional]
  handoff_bundle.manifest.json   [optional Phase 2+]
```

### 9.2 Required vs optional at `draft_complete`

| File | MVP spine today | Full runtime target |
|------|-----------------|---------------------|
| `session_manifest.json` | **Required** | **Required** |
| `serp_result.json` | **Required** | **Required** |
| `competitors.json` | **Required** | **Required** |
| `research_pack.draft.md` | **Required** | **Required** |
| Website / landing / findings | — | Per profile |

### 9.3 Approval bundle (ORCA handoff)

Minimum human-delivered bundle per [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md):

| Item | Required |
|------|----------|
| `research_pack.approved.md` | **Yes** |
| `session_manifest.json` (`pack_state=approved`) | **Yes** |
| `serp_result.json` | **Yes** |
| `competitors.json` | **Yes** when Phase 2 represented |
| `snapshots/`, landing JSON, `research_findings.json` | When pack `mig_phase` claims them |
| SAFE UNKNOWN (manifest + pack) | **Yes** |
| Evidence grades | **Yes** |
| Approved By metadata | **Yes** |

### 9.4 What goes to ORCA

- **Delivered:** approval bundle (human transport — path copy, archive zip, shared drive).
- **Not delivered:** drop-zone request files, processing logs, n8n execution internals.
- **ORCA produces:** analysis artifacts in ORCA workspace only.

---

## 10. MVP runtime assessment (brutally honest)

### 10.1 What can be assembled today

| Capability | Evidence | End-to-end? |
|------------|----------|-------------|
| Task File → spine → session folder | `incoming/mig/completed/*`, `lib/task-file-adapter/` | **Yes** (human runs adapter) |
| P0+P1+P2+P6 single shot | `run-session-spine.js` | **Yes** |
| Fallback SERP + draft pack | test payloads, sessions | **Yes** |
| Competitor discovery (may be empty) | wired in spine | **Yes** |
| Website pass | `lib/website-acquisition/`, verify script | **No** — manual pass per session dir |
| Landing pass | `lib/landing-analysis/`, verify script | **No** — not in spine |
| Multi-query SERP loop | design + partial lib | **No** in spine |
| Deep research | contract only | **No** |
| Keyword intelligence | contract only | **No** |
| Approval workflow | contract only | **No** — manual file rename possible, no manifest fields |
| n8n production Worker | export exists | **Not proven** deployed |
| ORCA automated handoff | contract | **No** |

**Honest MVP runtime today:** **Research Request → Session Spine (SERP fallback + competitor pass + draft pack)** under human-supervised CLI or Task File Adapter. That is **one atomic runtime**, not a multi-phase resumable orchestrator.

### 10.2 Architecture-only (documented, not assembled)

- Unified `run-runtime.js` phase loop
- Manifest v0.2 stages and `pack_state`
- MIG Worker Intake/Admin three-workflow family
- Live SERP provider
- Deep Research + `research_findings.json`
- Keyword Intelligence passes
- Approval + published/consumed automation
- `handoff_bundle.manifest.json`

### 10.3 Implementation backlog (priority order)

1. **Manifest v0.2** + `update-manifest-pass` helper used by all passes  
2. **Wire website + landing passes** into orchestrator after P2  
3. **Extend `build-research-pack`** for P3/P4 artifact projection  
4. **`pack_state` + approval CLI** (human commands, no auto-approve)  
5. **Multi-query P1 loop** in spine or Worker  
6. **SERP provider** integration (one vendor)  
7. **Deep Research pass** module  
8. **Worker n8n** routes per runtime design report  

### 10.4 Documentation drift warnings

| Doc | Issue |
|-----|-------|
| [README.md](../README.md) | Claims «No competitor capture» — **stale** vs spine |
| [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) | Claims landing «Not implemented» — **stale** vs `lib/landing-analysis/` (not spine-wired) |

---

## 11. Roadmap

### 11.1 Runtime MVP (assemble existing pieces)

**Goal:** One documented command path: intake → P1 → P2 → optional P3 → optional P4 → P6 → manual P7.

| Deliverable | Scope |
|-------------|-------|
| `run-mig-session.mjs` (name TBD) | Thin orchestrator calling existing passes |
| Manifest v0.2 | Stages, `pack_state`, pass blocks |
| Pack projection | Website + landing sections from artifacts |
| Operator approval script | Sets `approved_by` + copies approved md |
| Docs sync | README + OPERATIONAL-INDEX |

**Explicitly out of scope for Runtime MVP:** n8n deployment, OpenRouter, keyword APIs, deep research LLM, ORCA automation.

### 11.2 Runtime Phase 2

| Deliverable | Scope |
|-------------|-------|
| Multi-query P1 | `serp_index.json` + coverage in competitors |
| Live SERP provider | One integration + manual override |
| MIG Worker webhook | MetaBOT-pattern; spine as library |
| Google Sheets registry | Mirror manifest — FS remains SoT |
| Resume / partial_complete | Checkpoint by `manifest.phase` |

### 11.3 Runtime Phase 3

| Deliverable | Scope |
|-------------|-------|
| Deep Research pass | `research_findings.json` |
| Keyword Intelligence | Optional registry artifacts |
| Playwright selective fetch | Website pass enhancement |
| Consumed/archived automation | With ORCA ack discipline |
| Handoff bundle manifest | Checksums for approval bundle |

**Anti-scope-creep:** No ORCA methodology inside MIG; no Factory direct consumption; no query generation automation in MIG.

---

## 12. Architecture decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| **RA-01** | Artifacts are SoT; pack is projection | Prevents LLM drift; aligns all subsystem contracts |
| **RA-02** | `session_manifest.stage` ≠ `pack_state` | Execution vs product lifecycle |
| **RA-03** | Competitor discovery is derived pass after SERP, not separate acquisition API | Data acquisition architecture |
| **RA-04** | Multi-query is P1 mode, not its own phase | Reduces orchestration proliferation |
| **RA-05** | Keyword Intelligence is optional parallel P-K | Avoid blocking landing/website spine |
| **RA-06** | Spine v0.1 may remain single-shot; v0.2 adds checkpoints | Minimize breaking existing tests |
| **RA-07** | Partial sessions produce draft packs with SAFE UNKNOWN | Operator value vs fail-closed |
| **RA-08** | Approval never automated | Human authority protocol / ORCA handoff |
| **RA-09** | Filesystem SoT over Sheets | MetaBOT runtime design |
| **RA-10** | Deep Research fail-closed without SERP+competitors | Deep research architecture §2.2 |

---

## 13. Risks

| Risk | Mitigation |
|------|------------|
| Manifest/pass desync when passes run outside spine | Shared manifest updater; validation script |
| Operators treat `draft_complete` as ORCA-ready | Contract + manifest `pack_state` visibility |
| Stale README/INDEX mislead MVP scope | Doc sync in Runtime MVP backlog |
| Partial website capture overclaimed in pack | Coverage block + session_grade pessimistic |
| n8n assumed production without evidence | Status honesty in reports |
| LLM deep research invents facts | Findings JSON + citation refs only |

---

## 14. SAFE UNKNOWN (this document)

| Topic | Status |
|-------|--------|
| Production `MIG_SESSION_ROOT` on VPS | Operator-configured — design references env, not verified deployment |
| Dedicated MIG Telegram bot vs shared | Runtime design report — operator choice |
| Exact `session-manifest-v0.2` JSON Schema file | Specified herein — file not committed |
| `REPORT-mig-request-architecture-v1.md` | Referenced in Research Request contract — **not in repo** |

---

## 15. Related documents

| Document | Relationship |
|----------|----------------|
| [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) | Intake SoT |
| [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) | Output SoT |
| [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) | Downstream minimum bundle |
| [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) | P2 |
| [mig-multi-query-discovery-design-v0.md](mig-multi-query-discovery-design-v0.md) | P1 mode |
| [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) | P3 |
| [mig-landing-analysis-architecture-v1.md](mig-landing-analysis-architecture-v1.md) | P4 |
| [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) | P-K |
| [mig-deep-research-architecture-v1.md](mig-deep-research-architecture-v1.md) | P5 |
| [../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) | n8n Worker/Intake/Admin |
| [../OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) | Operator navigation |

---

## Document control

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Date | 2026-06-01 |
| Lane | A — MIG Runtime Assembly Architecture |
| Implementation | **None** by charter |
