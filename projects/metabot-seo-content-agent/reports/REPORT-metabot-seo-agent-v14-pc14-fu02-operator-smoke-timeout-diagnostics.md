# REPORT — MetaBOT SEO Agent PC14-FU02 Operator Smoke Timeout Diagnostics

**Date:** 2026-07-14  
**Classification:** Read-only diagnostics — no live mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — post–PC14-FU02 production apply operator smoke  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  

| Label | Value |
|-------|-------|
| **Diagnostic target** | `PC14_FU02_OPERATOR_SMOKE_TIMEOUT_DIAGNOSTICS` |
| **Decision** | `PC14_FU02_SMOKE_TIMEOUT_DIAGNOSED_RETRY_BLOCKED` |
| **Recommended next step** | `PC14_FU02_FIX_REQUIRED_BEFORE_RETRY` |
| **Final status** | `COMPLETE — PC14-FU02 smoke timeout diagnosed` |
| **Prior gate** | `PC14_FU02_PRODUCTION_APPLIED_HARNESS_VERIFIED` (`1b7cda59`) |

**Constraints honored:** No workflow patch/update/activate. No Telegram send. No OpenRouter calls. No Google Sheets writes. No `/run` retry. No lock cleanup. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

Operator smoke after PC14-FU02 production apply **failed in ~33 seconds** — not a long hang/timeout.

| Field | Finding |
|-------|---------|
| Intake | `3345` — **success** (01:20 local / 18:20 UTC) |
| Worker | `3346` — **error** |
| Real Task ID | `seo202607131820100448ul` (generated in Worker; **not** shown to operator) |
| Last node | `TZ Strict Cleanup` |
| Error | `structuredClone is not defined [line 250]` |
| Outline LLM | `Run Outline` / `Run Extract Outline` **succeeded** (~30s OpenRouter) |
| Final Telegram | **not sent** |
| Memory append | **not executed** |
| Close Lock | **not executed** |
| `/locks` @ 01:57 | «Активных задач нет.» |

**Root cause:** production FU-02 sanitizer `TZ Strict Cleanup` (`v1-tz-strict-cleanup-pc14-fu02-r1`) uses `structuredClone`, which exists in the local Node harness but is **undefined** in the n8n Code-node / task-runner VM. Local harness PASS therefore **masked** a live runtime incompatibility.

**Retry:** **not safe** until sanitizer is patched (sandbox-safe clone), re-harnessed, and re-applied.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `1b7cda59` — PC14-FU02 production apply evidence — **PASS** |
| Checkpoint `1b7cda59` | Present — **PASS** |
| Staged index | Empty — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead **21** / behind **17** — **noted**; no pull / no push |
| Foreign WIP | Preserved — **PASS** |
| Credentials | `local/tokens/n8n-api.env` present (values not printed) — **PASS** |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, FU-02 production apply / proposal / sandbox implementation / operator smoke charter, FU-01 / PC-14 / PC-07 operator smoke reports, production apply manifest + harness + diff-scope + after-apply sanitized Worker export.

**=== MARS AGENT GUARDRAILS v1 ===**  
Lane: B · Phase: diagnose · Repo root: `X:\AI MARS` · Volume: AI WS (X:)  
SCOPE LOCK: `projects/metabot-seo-content-agent/` + `local/pc14-fu02-operator-smoke-diagnostics-2026-07-14/` · Allowed: n8n GET workflows/executions, local evidence write · Forbidden: workflow mutation, Telegram send, OpenRouter, Sheets write, git stage/commit/push/pull/clean/reset.

---

## 3. Operator Transcript Summary

| Time (local UTC+7) | Event |
|--------------------|-------|
| 01:20 | `/run` smoke brief with forced TZ phrase `для удобства восприятия` + coffee-machine repair sections + banned stems |
| 01:20 | Bot: «Задача выполняется» / этап «Формируем SEO-ТЗ...» |
| — | **No final result. No visible Task ID.** |
| 01:57 | `/health` → Sheets OK; `seo_active_jobs` readable (27); memory readable (621); system available |
| 01:57 | `/locks` → «Активных задач нет.» |

Smoke **not verified**.

---

## 4. Time Window Investigated

| Window | Value |
|--------|-------|
| Operator local | 2026-07-14 **01:15–02:05** (UTC+7) |
| Primary UTC | 2026-07-13 **18:15–19:05Z** |
| Smoke pair UTC | Intake `3345` 18:20:03Z → Worker `3346` 18:20:07–18:20:40Z |
| Health/locks UTC | Intake relay `3347`/`3349` + Admin `3348`/`3350` ≈ 18:57Z |

Phrase anchors matched on Worker `3346`: `PC14-FU02`, `production patch`, `кофемашин`, `для удобства восприятия`, `диагностика`, `разборка`, `проверка электрических цепей`, `сборка после ремонта`.

---

## 5. Intake Execution Findings

| Field | Value |
|-------|-------|
| Workflow | Intake `x8EbTGKNdlBprLvk` |
| Execution | **`3345`** |
| Status | **success** |
| Started / stopped | `2026-07-13T18:20:03.074Z` → `18:20:07.518Z` |
| Last node | `Send To Worker` |
| Create Lock Row | `task_id=pending`, `status=active` |
| Send Task Accepted | `ok=true` (progress Telegram) |

**Answers:**

1. Did Intake run for `/run` @ 01:20? **Yes** (`3345`).  
2. Intake succeed or fail? **Succeed**.  

Later Intake `3347` / `3349` are `/health` and `/locks` relays to Admin (`Send To Admin`) — not the smoke `/run`.

---

## 6. Worker Execution Findings

| Field | Value |
|-------|-------|
| Workflow | Worker `p4mqb4VuPcemIDlC` |
| Execution | **`3346`** |
| Status | **error** (`finished=false`) |
| Duration | ~**33.1 s** |
| Started / stopped | `2026-07-13T18:20:07.495Z` → `18:20:40.622Z` |
| Route Command `task_id` | **`seo202607131820100448ul`** |
| Mode | `run` |
| Last node | **`TZ Strict Cleanup`** |
| Error | `ReferenceError: structuredClone is not defined [line 250]` |

**Production Worker metadata (live GET):** active `true`, **92** nodes, `updatedAt` `2026-07-13T16:40:11.596Z`, `TZ Strict Cleanup` present, version marker `v1-tz-strict-cleanup-pc14-fu02-r1`.

**Answers:**

4. Worker start? **Yes**.  
5. Outcome? **Error** (not cancel / not wall-clock timeout).  
6. Failed node? **`TZ Strict Cleanup`**.

`Run Outline` completed successfully (~29.7 s) — OpenRouter outline path **OK**. Failure is immediately after extract, inside FU-02 sanitizer.

---

## 7. Task ID / Lock Lifecycle

| Stage | Observation |
|-------|-------------|
| Intake lock create | `pending` / `active` |
| Worker Route Command | real ID **`seo202607131820100448ul`** |
| Operator Telegram Task ID | **not delivered** (pipeline stopped before final Format/Send) |
| Close Lock Before Sending | **not executed** |
| `/locks` @ 01:57 | Admin Format → «Активных задач нет.» |

**Answers:**

3. Real Task ID generated? **Yes** — `seo202607131820100448ul` (Worker-only visibility in this evidence).  
14–16. active_jobs created? **Yes** (Intake). Closed by Worker Close Lock? **No**. Close with real Task ID? **No** (Worker never reached close).  
17. Why `/locks` empty? Admin `3350` Format Locks Response sent empty-active text. Lookup Locks sample showed a sheet item `pending`/`active` (may be unrelated). Exact fate of **this** smoke `lock_key` row is **SAFE UNKNOWN** without chat-keyed Sheets read. Worker did **not** close it.

---

## 8. Memory / active_jobs Findings

| Store | Finding |
|-------|---------|
| Memory | `Append Memory Run` **not executed** — no smoke memory row from this run |
| active_jobs create | Intake `3345` wrote `pending`/`active` |
| active_jobs close | Worker close node **not run** |
| `/health` Admin `3348` | Sheets readable; sample rows present (not treated as smoke verification) |

Direct Google Sheets API **not** used (read-only inference from n8n node outputs + Admin executions).

---

## 9. Node Trace

Key path on Worker `3346`:

| Node | Executed | Notes |
|------|----------|-------|
| Route Command | yes | `task_id=seo202607131820100448ul`, `mode=run` |
| Status Outline / Build Outline Payload | yes | |
| Run Outline | yes | ~29.7 s — success |
| Run Extract Outline | **yes** | success |
| **TZ Strict Cleanup** | **yes → error** | `structuredClone` ReferenceError; no output items |
| Switch Run After Outline | **no** | |
| Format Run Pipeline | **no** | |
| Append Memory Run | **no** | |
| Close Lock Before Sending | **no** | |
| Send Telegram Run | **no** | final parts = 0 |

Progress at Telegram «Формируем SEO-ТЗ...» is consistent with Status Outline / early progress before failure.

Live jsCode still contains:

- line **250**: `const o = structuredClone(outline);`
- line **275**: `out.generated_text = structuredClone(out.generated_text);`

---

## 10. Failure Classification

| Class | Assessment |
|-------|------------|
| Primary | **FU-02 sanitizer runtime incompatibility** (`structuredClone` in n8n VM) |
| Not primary | OpenRouter timeout — outline **succeeded** |
| Not primary | n8n execution wall-clock timeout — failed at ~33 s on Code node |
| Not primary | Telegram final send — never reached |
| Not primary | Output chunking — never reached |
| Secondary / residual | Lock left without Worker close; operator saw empty `/locks` later — UX/ops concern, not root crash cause |

**Answers 7–12, 18:** Outline extract yes; TZ cleanup executed and failed; switch/final gen/Format/Telegram final **no**. Likely cause = **FU-02 `TZ Strict Cleanup` patch**.

---

## 11. FU-02 Patch Impact Assessment

| Aspect | Finding |
|--------|---------|
| Causal? | **Yes** — failing node is exactly the FU-02-added sanitizer |
| Graph insert | `Run Extract Outline → TZ Strict Cleanup → Switch…` works as wired; crash is **inside** jsCode |
| Why harness missed it | Local harness runs in full Node (has `structuredClone`); n8n task-runner VM does not |
| PC-07 Close Lock mapping | Not exercised this run (node not reached) — no evidence of PC-07 regression from this failure mode |
| FU-01 Strict Cleanup | Not reached on this path |

---

## 12. Production Safety Assessment

| Question | Answer |
|----------|--------|
| Safe to retry same / full smoke now? | **No** |
| Worker active? | Yes — still hosts broken sanitizer on `/run` outline path |
| Sheets / `/health`? | OK per operator + Admin `3348` |
| Risk of another silent partial UX failure? | **High** — progress message then hard stop; no final; no Task ID |

**Answer 19:** production is **not** safe to retry smoke until FU-02 sanitizer is fixed.

---

## 13. Recommended Next Action

**Recommended next step:** `PC14_FU02_FIX_REQUIRED_BEFORE_RETRY`

Safest sequence (proposal-only here; **do not apply in this task**):

1. Patch `TZ Strict Cleanup` jsCode: replace `structuredClone(x)` with sandbox-safe clone (e.g. `JSON.parse(JSON.stringify(x))` or project-consistent deep clone helper).  
2. Re-run sandbox + harness; add an **n8n VM / sandbox-compat** check so Node-only APIs cannot pass harness alone.  
3. Production re-apply under safe-workflow protocol.  
4. Then short operator smoke (or scoped verify), not before the fix.

**Answer 20:** fix required before retry — not short smoke now.

---

## 14. Evidence Files Created

Under `projects/metabot-seo-content-agent/exports/production-pc14-fu02/2026-07-14/`:

| File | Role |
|------|------|
| `pc14-fu02-operator-smoke-diagnostics-summary.json` | Summary + Q&A + decision candidates |
| `pc14-fu02-operator-smoke-intake-execution.redacted.json` | Intake `3345` |
| `pc14-fu02-operator-smoke-worker-execution.redacted.json` | Worker `3346` |
| `pc14-fu02-operator-smoke-node-trace.redacted.json` | Node trace |
| `pc14-fu02-operator-smoke-active-jobs-row.redacted.json` | Lock lifecycle notes |
| `pc14-fu02-operator-smoke-memory-row.redacted.json` | Memory absence |
| `pc14-fu02-operator-smoke-admin-window.redacted.json` | Admin `/health` `3348` + `/locks` `3350` |
| `run-pc14-fu02-operator-smoke-diagnostics.mjs` | Finder script (helper) |
| `refine-pc14-fu02-smoke-diagnostics.mjs` | Refine script (helper) |

Raw (gitignored-local expected): `local/pc14-fu02-operator-smoke-diagnostics-2026-07-14/` — Intake/Worker/Admin raw execution dumps.

**Not staged. Not committed.**

---

## 15. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Status |
|-------------|--------|
| Live n8n workflows (I/W/A) | read-only GET only — **not mutated** |
| Telegram / OpenRouter / Sheets writes | **not performed** |
| Website Factory / FP-0002 / Shpigovsky | foreign WIP preserved |
| OCPilot and other unrelated WIP | foreign WIP preserved |
| git stage / commit / push / pull / clean / reset / stash / restore | **not performed** |

---

## 16. SAFE UNKNOWN

- Exact Google Sheets row for smoke `lock_key` after failure (still `active`? filtered? overwritten?) — no chat-keyed Sheets API read.  
- Exact Admin `/locks` filter rule that yields «Активных задач нет.» while sheet still has some `pending`/`active` samples.  
- Whether any Error Trigger / silent cleanup mutated locks between 18:20 and 18:57 — **no evidence found** in Worker `3346` of close/cleanup nodes.  
- Whether operator Telegram progress used Intake-only vs Worker Status Outline wording — both consistent with observed UX; Worker stopped after outline stage.

---

## 17. Final Status

| Label | Value |
|-------|-------|
| **Diagnostic target** | `PC14_FU02_OPERATOR_SMOKE_TIMEOUT_DIAGNOSTICS` |
| **Decision** | `PC14_FU02_SMOKE_TIMEOUT_DIAGNOSED_RETRY_BLOCKED` |
| **Recommended next step** | `PC14_FU02_FIX_REQUIRED_BEFORE_RETRY` |
| **Final status** | `COMPLETE — PC14-FU02 smoke timeout diagnosed` |
| **Secret scan (sanitized report/evidence)** | `PASS_WITH_REVIEW_LABELS` (see closeout) |
| **Git** | No stage / no commit / no push |

Awaiting operator review.
