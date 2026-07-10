# REPORT — MetaBOT SEO Agent v14 PC-07 Production Proposal

**Task:** PC-07 — Production-apply proposal for `task_id` promotion on run-path lock close  
**Classification:** Proposal only — **no** live n8n mutation, **no** API calls, **no** workflow activation changes  
**Evidence baseline:** Sandbox evidence `e3dc9ef7`; proposal `6efd6afa`; v14 production export `exports/live-v14-evidence/2026-07-10/`  
**Date:** 2026-07-10  
**Lane:** MetaBOT SEO Content Agent (`@seo_content_agent_bot`) — Worker only  
**Checkpoint anchors:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`, `c1915bc8`, `6704b174`, `6efd6afa`, `e3dc9ef7`

---

## 1. Executive Summary

PC-07 addresses a documented path asymmetry in **IB-03** / **FM-14**: on successful `/run`, Worker node **`Close Lock Before Sending`** closes `seo_active_jobs` with `status=done` but leaves `task_id` at the Intake placeholder **`pending`**, while single/reuse paths already promote the real `seo…` id via **`Close Single Lock Before Sending`**.

**Static proposal** (`6efd6afa`) defined a minimal **R2** patch: add one Google Sheets field mapping mirroring the proven single-path expression. **Sandbox implementation** (`e3dc9ef7`) applied that patch to clone `kw1fHttu173lrkeW`, passed **PC07-01 through PC07-05**, and confirmed production workflows were untouched.

This report defines the **production-apply plan only**. No live apply is authorized by this document. Operator must complete a **fresh read-only production export** immediately before patch and grant explicit **Stage 13** approval per `safe-workflow-patch-protocol-v1.md`.

**Production decision:** `PC07_BLOCKED_PENDING_APPROVAL`  
**Task closeout:** `COMPLETE — PC-07 production proposal completed`

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Staged changes | Empty — **PASS** |
| Checkpoint `6263815c` | `docs(metabot): add foundation pack and live n8n evidence exporter` — **PASS** |
| Checkpoint `1b954990` | `docs(metabot): add n8n workflow grammar references` — **PASS** |
| Checkpoint `84dd9b07` | `docs(metabot): add seo agent v14 architecture review` — **PASS** |
| Checkpoint `af6fc35d` | `docs(metabot): add seo agent vnext reanchor plan` — **PASS** |
| Checkpoint `61bb6019` | `docs(metabot): add seo agent v14 issue backlog and test matrix` — **PASS** |
| Checkpoint `58c8f0b7` | `docs(metabot): add get and lock lifecycle audit` — **PASS** |
| Checkpoint `bc222072` | `docs(metabot): add safe workflow patch protocol` — **PASS** |
| Checkpoint `46fc6335` | `docs(metabot): add get success not-found verification plan` — **PASS** |
| Checkpoint `c1915bc8` | `docs(metabot): add sandbox get verification evidence` — **PASS** |
| Checkpoint `6704b174` | `docs(metabot): add get bridge hygiene and next selection` — **PASS** |
| Checkpoint `6efd6afa` | `docs(metabot): add pc07 task id promotion proposal` — **PASS** |
| Checkpoint `e3dc9ef7` | `docs(metabot): add pc07 sandbox evidence` — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `n8n-project-development-rules-v1.md`, `safe-workflow-patch-protocol-v1.md`, PC-07 proposal, PC-07 sandbox report, node diff, v14 production evidence pack.

**Parity note:** Committed production baseline export dated **2026-07-10**; workflow `updatedAt` in export is **2026-05-11T16:05:09.148Z**. Live parity at apply time is **PARTIAL** until operator performs fresh read-only export (mandatory pre-apply gate).

---

## 3. Out-of-Scope Preserved

Foreign WIP in git status — **`OUT_OF_SCOPE_PRESERVED`**. No read beyond status sampling, no stage, restore, delete, or modify.

| Lane | Status |
|------|--------|
| Smart Reporter | OUT_OF_SCOPE |
| I-SEO Report Hub | OUT_OF_SCOPE |
| Website Factory / FP-0002 | OUT_OF_SCOPE_PRESERVED |
| WordPress report hub | OUT_OF_SCOPE |
| OCPilot | OUT_OF_SCOPE_PRESERVED |
| Unrelated MARS systems | OUT_OF_SCOPE |
| `.recovery-temp/` | OUT_OF_SCOPE_PRESERVED |
| **PC-01** | **`PC01_MONITOR_NO_PATCH`** — preserved |

---

## 4. Production Patch Scope

### 4.1 Target

| Attribute | Value |
|-----------|-------|
| **Workflow name** | `SEO Content Agent Beta.v14 - Worker` |
| **Workflow ID** | `p4mqb4VuPcemIDlC` |
| **Node** | `Close Lock Before Sending` |
| **Node type** | `n8n-nodes-base.googleSheets` v4.7 |
| **Operation** | `update` on sheet `seo_active_jobs` |
| **Match key** | `lock_key` ← `{{ $('Store Worker Meta').first().json.worker_lock_key }}` |

### 4.2 Exact field change

**Add to `parameters.columns.value`:**

```text
task_id = {{ $('Route Command').first().json.task_id }}
```

**Schema change (if required by n8n UI):**

```text
parameters.columns.schema[] where id === "task_id" → removed: false
```

### 4.3 Production baseline (committed export)

**Before** — `Close Lock Before Sending` `columns.value`:

```json
{
  "status": "done",
  "finished_at": "={{ new Date().toISOString() }}",
  "lock_key": "={{ $('Store Worker Meta').first().json.worker_lock_key }}"
}
```

`task_id` schema entry: **`removed: true`**; not present in `columns.value`.

**After (desired):**

```json
{
  "status": "done",
  "finished_at": "={{ new Date().toISOString() }}",
  "lock_key": "={{ $('Store Worker Meta').first().json.worker_lock_key }}",
  "task_id": "={{ $('Route Command').first().json.task_id }}"
}
```

**Reference pattern** — `Close Single Lock Before Sending` already maps:

```text
task_id = {{ $('Route Command').first().json.task_id }}
```

### 4.4 Forbidden production changes

| Surface | Status |
|---------|--------|
| Intake (`x8EbTGKNdlBprLvk`) | **No change** |
| Admin (`AR6QxGt8ZKH0xG2T`) | **No change** |
| Telegram nodes | **No change** |
| OpenRouter HTTP nodes | **No change** |
| Memory append nodes (`Append Memory Run`, etc.) | **No change** |
| `/get` nodes | **No change** |
| `Close Single Lock Before Sending` | **No change** |
| `Finish Lock` | **No change** (PC-07 minimum) |
| Credentials | **No change** |
| Webhook paths | **No change** |
| Workflow activation state | **Preserve as-is** unless n8n UI requires temporary handling |

### 4.5 Risk classification

**R2 — LOW_LIVE_PATCH** per `safe-workflow-patch-protocol-v1.md`: single node, single field, proven expression elsewhere in same workflow.

---

## 5. Evidence Summary

### 5.1 Issue lineage

| ID | Role |
|----|------|
| **PC-07** | Patch candidate — promote `task_id` on run lock close |
| **IB-03** | P0 backlog — lock↔`task_id` sync |
| **FM-14** | Failure mode — `pending` remains on `/run` close |
| **TR-01**, **TR-04** | Test rules — promotion expectation at run close |

**Root cause:** Intake `Create Lock Row` sets `task_id: "pending"`. Worker `Route Command` generates real `seo{timestamp}{rand}`. Run path `Close Lock Before Sending` omits `task_id`; single path `Close Single Lock Before Sending` promotes it.

**Impact class:** Observability / ops consistency — `memory` already stores real `task_id`; `/get` unaffected; Admin `/locks` shows active rows only (mid-run may still show `pending` until close).

### 5.2 Static proposal evidence (`6efd6afa`)

- Confirmed omission from v14 sanitized Worker export.
- Defined minimal one-field patch mirroring single-path expression.
- Rated **R2**; gated sandbox before production.
- Recommended status at time: `PC07_READY_FOR_SANDBOX_PATCH`.

### 5.3 Sandbox implementation evidence (`e3dc9ef7`)

| Field | Value |
|-------|-------|
| Sandbox workflow | `SEO Content Agent Beta.v14 - Worker.sandbox-pc07` |
| Sandbox ID | `kw1fHttu173lrkeW` |
| Method | Approach B — harness webhook; OpenRouter/Telegram suppressed |
| Production touched | **No** — read-only GET only |
| Post-test sandbox state | **Inactive** (retained, not deleted) |

**Test matrix:**

| Test | Goal | Result |
|------|------|--------|
| **PC07-01** | Run close promotes real `task_id` | **PASS** — `row_task_id_promoted=true`, matches `Route Command` |
| **PC07-02** | Single close unchanged | **PASS** — static export comparison |
| **PC07-03** | `/get` unaffected | **PASS** — no GET node rewiring |
| **PC07-04** | Sheet history improves post-close | **PASS** — verified in PC07-01 |
| **PC07-05** | Failure path unchanged | **PASS** — static + harness scope |

### 5.4 Node diff evidence

File: `exports/sandbox-pc07/2026-07-10/pc07-close-lock-node-diff.json`

| Field | Before | After |
|-------|--------|-------|
| `status` | `done` | `done` (unchanged) |
| `finished_at` | `={{ new Date().toISOString() }}` | unchanged |
| `lock_key` | `={{ $('Store Worker Meta').first().json.worker_lock_key }}` | unchanged |
| `task_id` | **omitted** | `={{ $('Route Command').first().json.task_id }}` |

### 5.5 Production workflows untouched during sandbox

| Workflow | ID | Modified |
|----------|-----|----------|
| Intake | `x8EbTGKNdlBprLvk` | **No** |
| Worker | `p4mqb4VuPcemIDlC` | **No** |
| Admin | `AR6QxGt8ZKH0xG2T` | **No** |

Production Worker `updatedAt` unchanged across sandbox session (`2026-05-11T16:05:09.148Z`, 91 nodes).

---

## 6. Pre-Apply Requirements

**If any check below fails, live apply must STOP.**

| # | Requirement | Pass criteria |
|---|-------------|---------------|
| 1 | **Fresh read-only export** | Operator exports production Worker immediately before patch to gitignored `raw/` path; timestamp recorded |
| 2 | **Confirm workflow ID** | Export shows `id: p4mqb4VuPcemIDlC` |
| 3 | **Confirm workflow name** | Export shows `name: SEO Content Agent Beta.v14 - Worker` |
| 4 | **Confirm active state** | Record `active` flag; do not change unless n8n requires temporary deactivation for save (restore after) |
| 5 | **Baseline node match** | `Close Lock Before Sending` still has: `task_id` omitted or `removed: true`; `status`/`finished_at`/`lock_key` unchanged from expected baseline |
| 6 | **Reference node intact** | `Close Single Lock Before Sending` still has `task_id: {{ $('Route Command').first().json.task_id }}` |
| 7 | **No concurrent edits** | Operator confirms no other n8n edit session in progress on Worker |
| 8 | **Rollback export saved** | Pre-patch raw export stored locally; sanitized before-patch path planned under `exports/live-v14-evidence/` or task-chartered folder |
| 9 | **Explicit operator approval** | Stage 13 production approval recorded (dated note referencing PC-07) |

**Export freshness sub-gate:** Committed export is evidence baseline only. Apply requires **new** export at apply time — classify as `PC07_NEEDS_FRESH_EXPORT_FIRST` until step 1 completes.

---

## 7. Production Apply Plan

**Not executed in this task.** Operator or chartered follow-up task executes after gates pass.

| Step | Action |
|------|--------|
| 1 | Export production Worker raw to `projects/metabot-seo-content-agent/raw/` or `local/` (gitignored) |
| 2 | Sanitize before-patch export to evidence folder (e.g. `exports/live-v14-evidence/YYYY-MM-DD/` or `exports/production-pc07/YYYY-MM-DD/`) |
| 3 | Prepare minimal node-level mutation for `Close Lock Before Sending` only |
| 4 | Apply `task_id` mapping in n8n UI or selective import — **one field only** |
| 5 | Re-export production Worker after patch (raw, local) |
| 6 | Sanitize after-patch export to evidence folder |
| 7 | Generate node-level diff (compare `Close Lock Before Sending` `columns.value` + schema) |
| 8 | Verify diff matches sandbox `pc07-close-lock-node-diff.json` pattern — no other nodes/connections changed |
| 9 | Leave workflow active state as before apply |
| 10 | Record `updatedAt`, node count, n8n version metadata in apply report if safely available |

**Apply method preference:** n8n UI edit on `Close Lock Before Sending` Google Sheets node — lowest blast radius for R2 single-field change.

---

## 8. Smoke Test Plan

### PC07-PROD-01 — Minimal production verification (preferred if approved)

| Field | Detail |
|-------|--------|
| **Input** | One operator-approved `/run` with minimal brief (cost/risk acceptable) |
| **Expected output** | Pipeline completes; Telegram delivers normally |
| **Expected Sheets** | Matching `seo_active_jobs` row: `status=done`, `task_id` = real `seo…` (not `pending`), `finished_at` set |
| **Memory check** | `memory` row `task_id` matches promoted lock row `task_id` |
| **OpenRouter** | No model/config regression; generation completes |
| **Side effects** | One real content job; API cost incurred |
| **Operator involvement** | **Required** — approve test brief, monitor execution, inspect Sheets |
| **Stop conditions** | `task_id` still `pending`; empty `task_id`; wrong row updated; Telegram failure; pipeline error |

**Alternative (low-impact):** Operator-marked test request with minimal flags (`--outline-only` / `--text-only` if supported) — or defer full smoke and classify as **applied but unverified** (not recommended for R2 closeout).

### PC07-PROD-02 — `/get` unaffected

| Field | Detail |
|-------|--------|
| **Input** | Optional `/get {task_id}` for task from PC07-PROD-01 |
| **Expected** | Retrieval from `memory` succeeds; no lock created |
| **Sheets effect** | No new `seo_active_jobs` row |
| **Rerun required?** | **No** — patch touches run close only; prior GET evidence `c1915bc8` still valid |
| **Operator involvement** | Optional |
| **Stop conditions** | GET regression; unexpected lock row |

### PC07-PROD-03 — Rollback readiness

| Field | Detail |
|-------|--------|
| **Input** | Pre-apply export verification |
| **Expected** | Rollback export exists; reverse patch documented |
| **Sheets effect** | None (readiness check only) |
| **Operator involvement** | Confirm rollback file path before apply |
| **Stop conditions** | No rollback export → do not apply |

---

## 9. Rollback Plan

### 9.1 Rollback options

**Option A — Restore pre-patch workflow export**

1. Import pre-patch sanitized/raw export via n8n UI.
2. Confirm `Close Lock Before Sending` omits `task_id` mapping.
3. Verify active state restored.

**Option B — Reverse node field mapping**

1. Remove `columns.value.task_id` from `Close Lock Before Sending`.
2. Set `task_id` schema entry `removed: true` if n8n requires.
3. Save workflow.

### 9.2 Rollback triggers

- Production Worker fails to save after edit
- Node diff shows changes beyond `Close Lock Before Sending` / `task_id`
- PC07-PROD-01 smoke fails
- Telegram output fails post-patch
- `task_id` expression resolves empty
- Wrong `lock_key` row updated
- Unrelated nodes or connections changed

### 9.3 Post-rollback verification

Optional: one `/run` confirms `task_id` returns to `pending` on done rows (pre-patch behavior). No destructive Sheets cleanup required.

---

## 10. Risk Analysis

| Risk | Assessment | Mitigation |
|------|------------|------------|
| **R2 validity after sandbox PASS** | **Low** — sandbox confirmed promotion mechanics | Production smoke PC07-PROD-01 |
| **Production/live export drift** | **Medium** — export `updatedAt` 2026-05-11; apply may be months later | Mandatory fresh export (pre-apply #1) |
| **OpenRouter cost during smoke** | **Operational** — full `/run` triggers generation | Operator approves scope; use minimal flags or defer smoke |
| **Historical `pending` done rows** | **Low impact** — PC-07 does not backfill | Optional separate data hygiene charter |
| **`Finish Lock` omission** | **Low** — unmapped `task_id` should not erase promoted value | Monitor PC07-PROD-01; optional follow-up symmetry patch |
| **Mid-run `/locks` shows `pending`** | **By design** — promotion at close only | Document to ops; not PC-07 scope |
| **Unpushed branch / foreign WIP** | **Process** — unrelated changes in tree | Selective staging only; never `git add .` |
| **Inactive sandbox workflows on n8n** | **Low** — `kw1fHttu173lrkeW` inactive but retained | Operator may archive/delete after production verified |
| **Full `/run` not tested in sandbox** | **Medium** — Approach B isolated close node | PC07-PROD-01 recommended post-apply |
| **PC07-05 failure injection** | **Partial** — not fully exercised in sandbox | Acceptable for R2; monitor first production run |

---

## 11. Operator Approval Gate

Operator must explicitly approve before live apply:

- [ ] Production workflow ID **`p4mqb4VuPcemIDlC`**
- [ ] One-node / one-field patch scope (`Close Lock Before Sending` → `task_id` only)
- [ ] Fresh read-only pre-apply export (not committed raw secrets)
- [ ] Post-apply sanitized evidence capture path
- [ ] Whether to run live `/run` smoke (**PC07-PROD-01**) or accept **applied-but-unverified**
- [ ] Whether to leave sandbox workflow `kw1fHttu173lrkeW` inactive or archive later
- [ ] No git push unless separately authorized
- [ ] PC-01 remains **`PC01_MONITOR_NO_PATCH`**

**Protocol gates:** Stage 9 (planning) satisfied by prior proposal; Stage 11–12 satisfied by sandbox evidence; **Stage 13 (production apply) — PENDING**.

---

## 12. Production Decision

| Status | Applicable? |
|--------|-------------|
| `PC07_READY_FOR_LIVE_APPLY` | **No** — operator approval and fresh export not yet completed in this session |
| `PC07_NEEDS_FRESH_EXPORT_FIRST` | **Yes** — mandatory first action at apply time |
| **`PC07_BLOCKED_PENDING_APPROVAL`** | **Yes — selected** |
| `PC07_BLOCKED_RISK` | **No** — sandbox matrix passed; R2 bounded |
| `PC07_DEFER` | **No** — evidence supports proceed when gates clear |

**Rationale:** Sandbox evidence (`e3dc9ef7`) and static proposal (`6efd6afa`) are sufficient to authorize **planning** production apply. Live apply remains blocked until operator grants Stage 13 approval **and** completes fresh export immediately before patch. Technical sub-gate: `PC07_NEEDS_FRESH_EXPORT_FIRST`.

**Prior PC status:** `PC07_READY_FOR_PRODUCTION_PROPOSAL` → **fulfilled by this report**.

---

## 13. Recommended Next Prompt Outline

**Title:** MetaBOT SEO Agent PC-07 Production Apply — Promote `task_id` on Run Lock Close

**Goal:** After operator approval, perform fresh production Worker export, apply single-field patch to `Close Lock Before Sending`, capture before/after evidence, run PC07-PROD smoke tests.

**Allowed scope:**

- Read-only n8n GET for production Worker `p4mqb4VuPcemIDlC` (pre/post)
- n8n UI or chartered API patch on **one node field only**
- Sanitized exports to `exports/` per evidence rules
- Smoke test execution if operator approves
- Evidence report under `projects/metabot-seo-content-agent/reports/`

**Forbidden scope:**

- Intake, Admin, Telegram, OpenRouter, memory, `/get`, `Finish Lock`, `Close Single Lock Before Sending` edits
- Production apply without fresh export + Stage 13 approval
- Sandbox workflow activation without charter
- Commit/push unless explicitly requested
- Unrelated MARS lanes; PC-01 patch work

**Expected deliverable:** Production apply evidence report with node diff, smoke results, rollback confirmation.

**Final status labels (apply task):**

- `PC07_PRODUCTION_APPLIED_VERIFIED` — apply + smoke pass
- `PC07_PRODUCTION_APPLIED_UNVERIFIED` — apply without full smoke (operator choice)
- `PC07_APPLY_BLOCKED` — pre-apply gate failed
- `PC07_ROLLBACK_EXECUTED` — if rollback triggered

**Do not run full production-apply prompt until operator approves this proposal and confirms fresh-export window.**

---

## 14. SAFE UNKNOWN

| Item | Notes |
|------|-------|
| Live production Worker parity vs 2026-07-10 committed export | Requires fresh export at apply time |
| Full end-to-end `/run` without sandbox harness | Not tested; PC07-PROD-01 recommended |
| `Finish Lock` symmetry | Still omits `task_id`; likely harmless — not re-verified on full chain |
| Mid-run `/locks` display | Still `pending` until close — by design |
| Historical `done` rows with `pending` | Not auto-repaired |
| Empty `task_id` on malformed Worker input | Theoretically low; not evidenced |
| Sandbox synthetic row `sandbox-pc07:*` in live sheet | May remain; operator cleanup optional |
| Production Worker `updatedAt` at apply time | Unknown until fresh export |
| Whether n8n requires workflow deactivation to save | Operator resolves at apply time |

---

## 15. Files Created

| Path | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc07-production-proposal.md` | **Created** |

No other files modified.

---

## 16. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **Staged:** None
- **This task file:** Untracked until operator chooses to commit
- **Foreign WIP:** Preserved — `OUT_OF_SCOPE_PRESERVED` (FP-0002, Website Factory, OCPilot, `.recovery-temp/`, unrelated workspaces)
- **PC-01:** `PC01_MONITOR_NO_PATCH`
- **Commit / push:** Not performed

---

## 17. Final Status

**`COMPLETE — PC-07 production proposal completed`**

Sandbox evidence supports a minimal R2 production patch. Live apply is **not authorized** by this document.

| Label | Value |
|-------|-------|
| Production decision | `PC07_BLOCKED_PENDING_APPROVAL` |
| Pre-apply sub-gate | `PC07_NEEDS_FRESH_EXPORT_FIRST` |
| PC-01 | `PC01_MONITOR_NO_PATCH` |
| PC-07 (prior) | `PC07_READY_FOR_PRODUCTION_PROPOSAL` → fulfilled |

Awaiting operator review.
