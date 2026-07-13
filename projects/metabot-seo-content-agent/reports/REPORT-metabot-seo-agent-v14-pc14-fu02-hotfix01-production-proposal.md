# REPORT — MetaBOT SEO Agent PC14-FU02 HOTFIX01 Production Proposal

**Date:** 2026-07-14  
**Classification:** Production proposal only · GET-only production + sandbox baseline · no live mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — VM-safe `TZ Strict Cleanup` hotfix  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  

| Label | Value |
|-------|-------|
| **Hotfix** | `PC14_FU02_HOTFIX01_STRUCTUREDCLONE_VM_SAFE` |
| **Proposal** | `PC14_FU02_HOTFIX01_PRODUCTION_PROPOSAL` |
| **Production target** | `p4mqb4VuPcemIDlC` |
| **Sandbox source** | `6xpeMYaPxK7uGkIM` |
| **Decision** | `PC14_FU02_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next step** | `PC14_FU02_HOTFIX01_PRODUCTION_APPLY` |
| **Final status** | `COMPLETE — PC14-FU02 HOTFIX01 production proposal ready` |

**Current statuses preserved / context:**

| Item | Status |
|------|--------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` |
| PC14-FU-01 | `PC14_FU01_CLOSED_NEXT_SELECTED` |
| PC14-FU-02 production apply | `PC14_FU02_PRODUCTION_APPLIED_HARNESS_VERIFIED` (broken live `structuredClone`) |
| PC14-FU-02 operator smoke | `NOT VERIFIED` |
| PC14-FU-02 timeout diagnostics | `PC14_FU02_SMOKE_TIMEOUT_DIAGNOSED_RETRY_BLOCKED` |
| PC14-FU02 HOTFIX01 sandbox | `PC14_FU02_HOTFIX01_SANDBOX_APPLIED_HARNESS_VERIFIED` (`e9d12305`) |
| **This task** | `PC14_FU02_HOTFIX01_PRODUCTION_PROPOSAL` → ready for approval |

**Checkpoint commits verified through:** `e9d12305`

**Constraints honored:** Production Worker **not** patched. Sandbox **not** mutated. No Telegram send. No OpenRouter call. No Sheets write. No `/run` retry. No Intake/Admin mutation. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

PC14-FU02 HOTFIX01 is **ready for operator-approved production apply**. Fresh GET confirms production Worker still matches the broken FU-02 after-apply baseline (`structuredClone` ×2). Sandbox `6xpeMYaPxK7uGkIM` still carries the harness-verified VM-safe `clonePlain` patch (`v1.1-tz-strict-cleanup-pc14-fu02-hotfix01`).

| Field | Value |
|-------|-------|
| **Production Worker** | `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`) |
| **Active** | `true` |
| **Node count** | `92` |
| **updatedAt** | `2026-07-13T16:40:11.596Z` (matches FU-02 apply) |
| **Current TZ version** | `v1-tz-strict-cleanup-pc14-fu02-r1` |
| **`structuredClone` in production** | **2** (broken) |
| **Proposed TZ version** | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` |
| **Graph** | `Run Extract Outline → TZ Strict Cleanup → Switch Run After Outline` (preserve) |
| **Sandbox harness** | TZ01–TZ07 · NR01–NR09 · SG01–SG05 · VM01–VM06 **PASS** (restricted VM) |
| **Diff scope** | jsCode/version of `TZ Strict Cleanup` only |

**This task does not perform live apply.** Operator approval and an apply-phase fresh export are mandatory pre-gates. **Do not retry `/run` smoke until hotfix is applied.**

**Decision:** `PC14_FU02_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL`  
**Next:** `PC14_FU02_HOTFIX01_PRODUCTION_APPLY`

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `e9d12305` — `docs(metabot): add pc14 fu02 hotfix sandbox evidence` — **PASS** |
| Checkpoint `e9d12305` | Present — **PASS** |
| Staged index | Empty — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead **23** / behind **17** — **noted**; **no pull / no push** |
| Foreign WIP | Preserved — **PASS** |
| Credentials | `local/tokens/n8n-api.env` present (values not printed) — **PASS** |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, HOTFIX01 sandbox implementation (`e9d12305`), FU-02 smoke timeout diagnostics, FU-02 production apply / proposal / sandbox evidence, issue backlog, hotfix01 manifest / harness / diff-scope / node-diff / after-patch sanitized Worker, production FU-02 after-apply sanitized Worker + apply diff-scope.

**=== MARS AGENT GUARDRAILS v1 ===**  
Lane: B · Phase: production proposal · Repo root: `X:\AI MARS` · Volume: AI WS (X:)  
SCOPE LOCK: `projects/metabot-seo-content-agent/` + `local/pc14-fu02-hotfix01-production-proposal-2026-07-14/` · Allowed: n8n GET production/sandbox (read-only), sanitized proposal evidence write · Forbidden: production/sandbox PUT/activate, Telegram, OpenRouter, Sheets write, `/run` retry, git stage/commit/push/pull/clean/reset.

---

## 3. Production Baseline Verification

**Method:** `GET_ONLY` via n8n API for `p4mqb4VuPcemIDlC`. Compared to committed FU-02 after-apply sanitized baseline and diagnostics expectation.

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `p4mqb4VuPcemIDlC` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker` | same | **PASS** |
| active | `true` | `true` | **PASS** |
| node count | `92` | `92` | **PASS** |
| updatedAt | `2026-07-13T16:40:11.596Z` | FU-02 apply timestamp | **PASS** |
| `TZ Strict Cleanup` | present | present | **PASS** |
| TZ version | `v1-tz-strict-cleanup-pc14-fu02-r1` | broken r1 | **PASS** |
| `structuredClone` count | **2** | **2** | **PASS** |
| `clonePlain` | absent | absent (pre-hotfix) | **PASS** |
| Graph | Extract → TZ → Switch | same | **PASS** |
| Retargets | Restore / Extract SEO Strategy → TZ | same | **PASS** |
| PC-07 Close Lock | `={{ $('Route Command').first().json.task_id }}` | same | **PASS** |
| Non-target jsCode vs FU-02 after-apply | none | none | **PASS** |
| TZ jsCode vs FU-02 after-apply | match | match | **PASS** |

**Drift decision:** no unexpected drift since `d6a7ac69` / `e9d12305` context. Production remains the known broken FU-02 state — **apply-ready for hotfix only**.

**Safety note:** repeated `/run` on outline path remains **unsafe** until hotfix apply.

---

## 4. Sandbox Source Verification

**Method:** live GET of `6xpeMYaPxK7uGkIM` + committed sandbox evidence (`e9d12305`).

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `6xpeMYaPxK7uGkIM` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02-hotfix01` | same | **PASS** |
| active | `false` | `false` | **PASS** |
| node count | `92` | `92` | **PASS** |
| TZ version | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` | hotfix01 | **PASS** |
| `structuredClone` | **0** | **0** | **PASS** |
| `clonePlain` | present | present | **PASS** |
| Graph / retargets | preserved | preserved | **PASS** |
| Harness TZ01–TZ07 | PASS | PASS | **PASS** |
| Harness NR01–NR09 | PASS | PASS | **PASS** |
| Harness SG01–SG05 | PASS (`scopeOk=true`) | PASS | **PASS** |
| Harness VM01–VM06 | PASS (restricted VM) | PASS | **PASS** |

**Prior FU-02 sandbox** `WCBIB9L2I8VbGtRs` — inspect-only context; **not** used as apply source.

**Sandbox decision:** source verified — suitable donor for production jsCode/version only.

---

## 5. Proposed Production Patch Scope

| Item | Detail |
|------|--------|
| **Hotfix ID** | `PC14_FU02_HOTFIX01_STRUCTUREDCLONE_VM_SAFE` |
| **Node** | `TZ Strict Cleanup` only |
| **Change type** | jsCode + sanitizer version marker |
| **From** | `v1-tz-strict-cleanup-pc14-fu02-r1` + `structuredClone` ×2 |
| **To** | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` + `clonePlain` |
| **Node count delta** | 0 (92 → 92) |
| **Connections** | unchanged |
| **Retargets** | unchanged |
| **Intake / Admin** | unchanged |
| **active** | preserve `true` |
| **workflow id/name** | preserve |

**Explicit non-targets:** Strict Cleanup v15 · Strict Risk Scanner · Format Run Pipeline · Route Command · PC-07 Close Lock mapping · memory/active_jobs · Telegram · OpenRouter · Sheets · `/get` · credentials · node id/name/position/edges.

Proposed after-state is **proposed only / not applied / production unchanged**.

Evidence: `pc14-fu02-hotfix01-production-proposal-diff-preview.json`, `pc14-fu02-hotfix01-production-proposal-scope-summary.json`.

---

## 6. Proposed Apply Plan

For a future operator-approved `PC14_FU02_HOTFIX01_PRODUCTION_APPLY` task only:

1. Read current production Worker `p4mqb4VuPcemIDlC` immediately before apply.
2. Save raw rollback under `local/`:  
   `local/pc14-fu02-hotfix01-production-proposal-2026-07-14/rollback/worker-before-hotfix01.raw.json` (or apply-task dated equivalent).
3. Save sanitized before evidence under repo exports `production-pc14-fu02-hotfix01/`.
4. Patch only `TZ Strict Cleanup`:
   - replace node `jsCode` with sandbox hotfix jsCode from `6xpeMYaPxK7uGkIM`;
   - set version to `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01`;
   - remove all `structuredClone` calls;
   - retain `clonePlain` helper;
   - do not change node id / name / position / edges.
5. Submit production workflow update preserving `active=true`.
6. Re-read production Worker after update.
7. Verify: active true; nodes 92; `updatedAt` advanced; TZ version v1.1; `structuredClone` count 0; `clonePlain` present; graph / retargets / Strict Cleanup v15 / Scanner / Format / Route / PC-07 / memory / Telegram / OpenRouter / Sheets / credentials unchanged (redacted in evidence).
8. Run local post-apply structural/harness checks only: TZ01–TZ07 · NR01–NR09 · SG01–SG05 · VM01–VM06 (restricted VM).
9. Do **not** run Telegram smoke in the apply task.
10. Persist production apply evidence in that later task.
11. Then operator runs short Telegram smoke (separate charter).

**Forbidden during apply:** Intake/Admin mutation; activation toggle unless separately chartered; drive-by non-target edits; Telegram / OpenRouter / Sheets calls; `/run` retry before post-checks; committing raw rollback.

---

## 7. Rollback Plan

**No rollback is executed in this proposal task.**

If production hotfix apply fails or post-checks fail:

1. Do **not** retry `/run`.
2. Restore production Worker from saved raw rollback under `local/`.
3. Re-read Worker.
4. Confirm `active` restored to pre-apply state (`true`).
5. Confirm `TZ Strict Cleanup` version/code restored to broken pre-apply baseline (`v1-tz-strict-cleanup-pc14-fu02-r1`).
6. Create rollback report/evidence.
7. Do not continue to smoke until rollback/fix is reviewed.

**Important:** Rollback file remains **local only** — do not commit raw rollback.

---

## 8. Expected Post-Apply Checks

| Check | Expected |
|-------|----------|
| Workflow id / name | unchanged |
| active | `true` |
| node count | `92` |
| `updatedAt` | advanced past `2026-07-13T16:40:11.596Z` |
| TZ version | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` |
| `structuredClone` | **0** |
| `clonePlain` | present |
| Graph | Extract → TZ → Switch |
| Retargets | Restore / Extract SEO Strategy → TZ |
| Non-targets | unchanged |
| Local harness | TZ / NR / SG / VM all PASS |
| Secret scan | PASS or PASS_WITH_REVIEW_LABELS |

**Smoke (after apply persistence, separate charter):** short `/run` that previously failed on outline path; expect Worker past `TZ Strict Cleanup` without `structuredClone is not defined`; residual phrase sanitization still works; PC-07 lock close still uses Route Command `task_id`.

---

## 9. Evidence Files Created

**Directory:** `projects/metabot-seo-content-agent/exports/production-pc14-fu02-hotfix01/2026-07-14/`

| File | Role |
|------|------|
| `SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu02-hotfix01.before-proposal.sanitized.json` | Fresh sanitized production baseline |
| `SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu02-hotfix01.source.sanitized.json` | Sanitized sandbox hotfix source |
| `pc14-fu02-hotfix01-production-proposal-diff-preview.json` | Proposed jsCode/version diff preview |
| `pc14-fu02-hotfix01-production-proposal-scope-summary.json` | Scope / checks / decision |
| `PC14-FU02-HOTFIX01-PRODUCTION-PROPOSAL-MANIFEST.md` | Manifest |
| `run-pc14-fu02-hotfix01-production-preproposal.mjs` | GET-only proposal runner |

**Raw / local only (not staged):**

- `local/pc14-fu02-hotfix01-production-proposal-2026-07-14/worker-before-proposal.raw.json`
- `local/pc14-fu02-hotfix01-production-proposal-2026-07-14/sandbox-hotfix01.source.raw.json`
- `local/pc14-fu02-hotfix01-production-proposal-2026-07-14/preproposal-result.json`

**Secret scan (proposal evidence):** `PASS_WITH_REVIEW_LABELS` — workflow IDs, execution/task IDs, commit hashes, redacted markers, operational labels only; no live API keys / bot tokens / sheet IDs / webhook secrets printed.

---

## 10. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Status |
|-------------|--------|
| Smart Reporter, I-SEO Report Hub | not touched |
| Website Factory / WordPress / FP-0002 / Shpigovsky | foreign WIP preserved |
| OCPilot | foreign WIP preserved |
| `.recovery-temp/` and other untracked foreign WIP | preserved |
| Production n8n mutation | **not performed** |
| Sandbox n8n mutation | **not performed** |
| Prior FU-02 sandbox `WCBIB9L2I8VbGtRs` | not overwritten |
| Intake / Admin | not mutated |
| Telegram / OpenRouter / Sheets | not called |
| `/run` retry | **not performed** |
| Push / pull / clean / reset / stash / restore / stage / commit | **not performed** |

---

## 11. SAFE UNKNOWN

- Exact operator Telegram smoke wording and timing preferred after hotfix apply (separate charter).
- Whether any parallel non-outline Worker paths could still reference other `structuredClone` sites — **not scanned in this proposal beyond `TZ Strict Cleanup`** (hotfix scope is that node only; verify during apply if charter expands).
- Live n8n Code-node VM minor version / task-runner build — confirmed broken for `structuredClone` via execution `3346`; assumed unchanged until apply.

---

## 12. Final Status

| Label | Value |
|-------|-------|
| **Hotfix** | `PC14_FU02_HOTFIX01_STRUCTUREDCLONE_VM_SAFE` |
| **Proposal** | `PC14_FU02_HOTFIX01_PRODUCTION_PROPOSAL` |
| **Production target** | `p4mqb4VuPcemIDlC` |
| **Sandbox source** | `6xpeMYaPxK7uGkIM` |
| **Decision** | `PC14_FU02_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next step** | `PC14_FU02_HOTFIX01_PRODUCTION_APPLY` |
| **Final status** | `COMPLETE — PC14-FU02 HOTFIX01 production proposal ready` |

**Git:** proposal report/evidence created locally — **not staged / not committed** (persist later after operator review).

Awaiting operator review.
