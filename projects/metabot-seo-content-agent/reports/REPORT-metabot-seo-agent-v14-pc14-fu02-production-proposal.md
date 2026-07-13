# REPORT — MetaBOT SEO Agent v14 PC14-FU02 Production Proposal

**Date:** 2026-07-13  
**Classification:** Production proposal only · GET-only production baseline · no live mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Worker TZ/outline-side strict residual sanitizer  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  

| Label | Value |
|-------|-------|
| **Backlog item** | `PC14_FU02_TZ_STRICT_RESIDUAL_CLEANUP_AUDIT` |
| **Proposal** | `PC14_FU02_PRODUCTION_PROPOSAL` |
| **Decision** | `PC14_FU02_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next step** | `PC14_FU02_PRODUCTION_APPLY` |

**Current statuses preserved:**

| Item | Status |
|------|--------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` |
| PC14-FU-01 | `PC14_FU01_CLOSED_NEXT_SELECTED` |
| PC14-FU-02 audit | `PC14_FU02_READY_FOR_SANDBOX_PATCH_PROPOSAL` (predecessor) |
| PC14-FU-02 sandbox proposal | `PC14_FU02_READY_FOR_SANDBOX_IMPLEMENTATION` (predecessor) |
| PC14-FU-02 sandbox implementation | `PC14_FU02_SANDBOX_PATCH_APPLIED_HARNESS_VERIFIED` (`ee0c4653`) |

**Checkpoint commits verified through:** `ee0c4653`

**Constraints honored:** Production Worker unchanged. Sandbox unchanged. No Telegram send. No OpenRouter call. No Sheets write. No Intake/Admin mutation. No push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

PC14-FU02 Strategy A is **ready for operator-approved production apply**. Fresh GET of production Worker confirms the FU-01 baseline is intact and the TZ node is absent. Sandbox evidence (`ee0c4653`) already inserted and harness-verified `TZ Strict Cleanup` on inactive clone `WCBIB9L2I8VbGtRs`.

| Field | Value |
|-------|-------|
| **Production Worker** | `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`) |
| **Active** | `true` |
| **Node count** | `91` |
| **updatedAt** | `2026-07-12T19:11:34.090Z` (matches FU-01 apply) |
| **TZ Strict Cleanup** | **absent** (expected pre-FU02) |
| **Strict Cleanup** | `v15-strict-cleanup-pc14-fu01-r1` |
| **PC-07 Close Lock** | `={{ $('Route Command').first().json.task_id }}` |
| **Pre-FU02 graph** | `Run Extract Outline → Switch Run After Outline` |
| **Proposed graph** | `Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline` |
| **Sanitizer version** | `v1-tz-strict-cleanup-pc14-fu02-r1` |
| **Retargets** | `Restore Outline Data`, `Extract SEO Strategy` |
| **Sandbox harness** | TZ01–TZ07 · NR01–NR09 · SG01–SG05 **PASS** |
| **Example cleanup** | `для удобства восприятия` → `для структурированного представления` |

**This task does not perform live apply.** Operator approval and an apply-phase fresh export are mandatory pre-gates.

**Decision label:** `PC14_FU02_READY_FOR_PRODUCTION_APPROVAL`  
**Task status:** `COMPLETE — PC14-FU02 production proposal completed`

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Staged changes (pre-task) | Empty — **PASS** |
| HEAD | `ee0c4653` — `docs(metabot): add pc14 fu02 sandbox evidence` — **PASS** |
| Checkpoint `ee0c4653` | Present — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead / behind noted; **no pull / no push** |
| Foreign WIP | Preserved — **PASS** |

**Authority docs / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, FU-02 sandbox implementation / proposal / audit, FU-01 closeout / operator smoke, issue backlog, sandbox-pc14-fu02 exports, production-pc14-fu01 after-apply sanitized Worker.

**Live API (authorized):** GET-only fresh production Worker read — **PASS** (no mutation).  
**Telegram / OpenRouter / Sheets writes:** not performed.

---

## 3. Source Evidence Reviewed

### 3.1 Checkpoint chain (recent)

| Checkpoint | Role |
|------------|------|
| `f6fb295a` | PC14-FU-01 closeout + next backlog selection |
| `535acbce` | PC14-FU02 TZ residual audit/proposal |
| `af306264` | PC14-FU02 sandbox patch proposal |
| `ee0c4653` | PC14-FU02 sandbox implementation evidence |

### 3.2 Sandbox evidence (`exports/sandbox-pc14-fu02/2026-07-13/`)

- before/after sanitized Worker JSON
- `pc14-fu02-tz-strict-cleanup-node-diff.json`
- `pc14-fu02-diff-scope-summary.json` (`scopeOk=true`)
- `pc14-fu02-harness-results.json`
- `PC14-FU02-SANDBOX-PATCH-MANIFEST.md`

### 3.3 Production FU-01 after-apply baseline

- `exports/production-pc14-fu01/2026-07-13/SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu01.after-apply.sanitized.json`

### 3.4 Fresh production GET (this task)

- Raw: `local/pc14-fu02-production-proposal-2026-07-13/worker.raw.json` (not staged)
- Sanitized proposal pack under `exports/production-pc14-fu02/2026-07-13/`

---

## 4. Production Baseline

**Method:** `GET_ONLY` via n8n API for `p4mqb4VuPcemIDlC`.

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `p4mqb4VuPcemIDlC` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker` | same | **PASS** |
| active | `true` | `true` | **PASS** |
| node count | `91` | `91` | **PASS** |
| updatedAt | `2026-07-12T19:11:34.090Z` | FU-01 apply timestamp | **PASS** |
| `TZ Strict Cleanup` | absent | absent | **PASS** |
| `Run Extract Outline` | present | present | **PASS** |
| `Switch Run After Outline` | present | present | **PASS** |
| Extract → Switch | direct | direct | **PASS** |
| Strict Cleanup | `v15-strict-cleanup-pc14-fu01-r1` | v15 | **PASS** |
| Strict Risk Scanner | matches FU-01 after-apply jsCode | unchanged | **PASS** |
| Format Run Pipeline | matches FU-01; has `STRICT QA REJECT` | unchanged | **PASS** |
| PC-07 Close Lock | `={{ $('Route Command').first().json.task_id }}` | same | **PASS** |
| Non-target jsCode drift vs FU-01 | none | none | **PASS** |

**Baseline decision input:** fresh, clean, apply-ready.

Evidence: `pc14-fu02-production-preproposal-baseline.json`.

---

## 5. Sandbox Evidence Summary

| Field | Value |
|-------|-------|
| Sandbox name | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02` |
| Sandbox ID | `WCBIB9L2I8VbGtRs` |
| Active | `false` |
| Strategy | **A** |
| Node count | 91 → **92** |
| Node added | `TZ Strict Cleanup` |
| Version | `v1-tz-strict-cleanup-pc14-fu02-r1` |
| Graph | `Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline` |
| Retargets | `Restore Outline Data`, `Extract SEO Strategy` |
| Harness | `SANDBOX_PATCH_APPLIED_HARNESS_LOCAL` — all PASS |
| Production during sandbox | unchanged |

Smoke residual basis addressed on TZ/outline path: `для удобства восприятия` → `для структурированного представления`.

---

## 6. Proposed Production Patch

**Strategy:** A  
**Risk:** R1 (deterministic Code insert + two companion retargets; sandbox-verified; reversible)

### Patch operations (future `PC14_FU02_PRODUCTION_APPLY` only)

1. Insert Code node `TZ Strict Cleanup` with jsCode from sandbox after-patch (`v1-tz-strict-cleanup-pc14-fu02-r1`).
2. Connect: `Run Extract Outline` → `TZ Strict Cleanup` → `Switch Run After Outline`.
3. Retarget `Restore Outline Data`: `$('Run Extract Outline')` → `$('TZ Strict Cleanup')`.
4. Retarget `Extract SEO Strategy`: `$node['Run Extract Outline']` → `$node['TZ Strict Cleanup']`.
5. Preserve Strict Cleanup v15, Strict Risk Scanner, Format Run Pipeline, Route Command, PC-07 locks, memory/active_jobs, Telegram, OpenRouter, Sheets, `/get`, credentials, and workflow `active=true`.

**Do not** mutate Intake/Admin. **Do not** call Telegram / OpenRouter / Sheets during apply.

---

## 7. Proposed Diff Scope

| Intended change | Detail |
|-----------------|--------|
| Added node | `TZ Strict Cleanup` |
| Connection path | `Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline` |
| Retargets | `Restore Outline Data`, `Extract SEO Strategy` |
| Node count | 91 → 92 |
| Unchanged | Strict Cleanup v15 · Strict Risk Scanner · Format Run Pipeline · Route Command · PC-07 · memory · Telegram · OpenRouter · Sheets · `/get` · credentials · active |

Any proposed after-state derived from sandbox is **proposed only / not applied / production unchanged**.

Evidence: `pc14-fu02-production-proposed-node-diff.json`, `pc14-fu02-production-proposed-scope-summary.json`.

---

## 8. Production Apply Gate

**Next task (operator-approved only):** `PC14_FU02_PRODUCTION_APPLY`

The production apply prompt must **not** be generated in this task unless the operator asks after reviewing this report.

### Gate conditions

1. Fresh baseline collected (this proposal) or explicitly repeated immediately before apply.
2. Proposed diff scope exactly matches sandbox evidence `ee0c4653`.
3. No live drift in target nodes vs this preproposal baseline.
4. Workflow `active` state preserved (`true`).
5. Rollback raw export saved under `local/` before mutation.
6. Sanitized before/after evidence saved under `exports/production-pc14-fu02/`.
7. Harness or local structural checks pass post-apply.
8. No Telegram / OpenRouter / Sheets calls during apply.
9. Operator explicitly approves production apply.

### Forbidden during apply

- Intake/Admin mutation
- activation toggle unless separately chartered
- multi-node drive-by edits outside Strategy A scope
- staging raw/local/runner files without separate charter

---

## 9. Rollback Plan

**No rollback is executed in this proposal task.**

| Item | Detail |
|------|--------|
| **Rollback source** | Raw production before export created in future apply phase under `local/` |
| **Preferred action** | Restore production Worker from raw before export |
| **Targeted alternative** | Remove `TZ Strict Cleanup`, restore Extract→Switch connection, revert two retargets from raw before |

**Rollback triggers:** unexpected non-target jsCode change; active-state change; PC-07 mapping change; harness failure; Telegram smoke runtime failure; memory/active_jobs regression; unexpected side-effect node behavior.

---

## 10. Smoke Plan

**After** successful production apply + evidence persist, operator runs Telegram smoke manually (separate charter).

**Expectation:**

- SEO ТЗ no longer contains `для удобства восприятия` (sanitized to structured equivalent);
- final SEO Text remains clean for PC-14 R1 + FU-01 families;
- SEO QA / factcheck remain valid;
- PC-07 lock closure still uses real `task_id` from Route Command.

Suggested smoke focus: short `/run` that previously produced the residual phrase in SEO ТЗ / outline `decision_reason`. Exact Telegram wording is left to the operator apply/smoke charter.

---

## 11. Evidence Files Created

**Directory:** `projects/metabot-seo-content-agent/exports/production-pc14-fu02/2026-07-13/`

| File | Role |
|------|------|
| `SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02.preproposal.sanitized.json` | Fresh sanitized production snapshot |
| `pc14-fu02-production-preproposal-baseline.json` | Baseline checks + decision |
| `pc14-fu02-production-proposed-node-diff.json` | Proposed TZ insert + retargets |
| `pc14-fu02-production-proposed-scope-summary.json` | Proposed scope / unchanged areas |
| `PC14-FU02-PRODUCTION-PROPOSAL-MANIFEST.md` | Manifest |

**Raw / helper (local only — not staged):**

- `local/pc14-fu02-production-proposal-2026-07-13/worker.raw.json`
- `local/pc14-fu02-production-proposal-2026-07-13/run-pc14-fu02-production-preproposal.mjs`

---

## 12. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Status |
|-------------|--------|
| Smart Reporter, I-SEO Report Hub | not touched |
| Website Factory / WordPress / FP-0002 / Shpigovsky | foreign WIP preserved |
| OCPilot | foreign WIP preserved |
| `.recovery-temp/` and other untracked foreign WIP | preserved |
| Production n8n mutation | **not performed** |
| Sandbox n8n mutation | **not performed** |
| Intake / Admin | not mutated |
| Telegram / OpenRouter / Sheets | not called |
| Push / pull / clean / reset / stash / restore | **not performed** |

---

## 13. SAFE UNKNOWN

- Exact live operator Telegram smoke wording preferred for FU-02 residual verification beyond the residual phrase already evidenced.
- Whether concurrent operator edits occur between this proposal GET and future apply — apply phase must re-GET.
- Whether n8n metadata-only fields (positions, versionIds) may normalize on PUT beyond intentional Strategy A scope — document if observed at apply.

---

## 14. Final Status

| Label | Value |
|-------|-------|
| **Decision** | `PC14_FU02_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next step** | `PC14_FU02_PRODUCTION_APPLY` |
| **Task status** | `COMPLETE — PC14-FU02 production proposal completed` |

Awaiting operator review.
