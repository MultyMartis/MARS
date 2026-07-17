# REPORT — MetaBOT SEO Agent PC14-FU03 HOTFIX01 Production Proposal

**Date:** 2026-07-16  
**Classification:** Production proposal only — GET-only production + sandbox baseline · **no live mutation**  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — PC14-FU03 HOTFIX01 reject-safe restore  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer · SEO Content Agent only  

| Label | Value |
|-------|-------|
| **Proposal** | `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL` |
| **Based on sandbox implementation** | `PC14_FU03_HOTFIX01_SANDBOX_APPLIED_HARNESS_VERIFIED` |
| **Sandbox implementation commit** | `3a41bbc8` |
| **Design commit** | `7443c4e9` |
| **Diagnostics commit** | `cab4597a` |
| **Production apply commit** | `44c05c3b` |
| **Production Worker** | `p4mqb4VuPcemIDlC` |
| **Sandbox source** | `tVGWi7Ud3zz2eGKo` |
| **Decision** | `PC14_FU03_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next** | `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL_PERSIST` |
| **After persist** | `PC14_FU03_HOTFIX01_PRODUCTION_APPLY` |
| **Final status** | `COMPLETE — PC14-FU03 HOTFIX01 production proposal ready` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |

**Current statuses preserved / context:**

| Item | Status |
|------|--------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` |
| PC14-FU-01 | `PC14_FU01_CLOSED_NEXT_SELECTED` |
| PC14-FU-02 production apply | `PC14_FU02_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU02 HOTFIX01 production apply | `PC14_FU02_HOTFIX01_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU03 production apply | `PC14_FU03_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU03 operator smoke diagnostics | `PC14_FU03_OPERATOR_SMOKE_DIAGNOSED_FIX_REQUIRED` |
| PC14-FU03 HOTFIX01 sandbox design | `PC14_FU03_HOTFIX01_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| PC14-FU03 HOTFIX01 sandbox implementation | `PC14_FU03_HOTFIX01_SANDBOX_APPLIED_HARNESS_VERIFIED` |
| **This task** | `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL` → ready for approval |

**Constraints honored:** Production Worker **not** patched. Sandbox **not** mutated. No Telegram / OpenRouter / Sheets. No `/run` / `/health` / `/locks`. No lock/memory cleanup. No Intake/Admin mutation. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

PC14-FU03 HOTFIX01 is **ready for operator-approved production apply**. Fresh GET confirms production Worker `p4mqb4VuPcemIDlC` still has the known broken restore hard-require of `Format Run Pipeline` on both restore nodes. Sandbox `tVGWi7Ud3zz2eGKo` still carries the harness-verified dual-source fallback (`Format Run Pipeline` → `Format Strict Reject Message` → explicit throw). Automated preflight gates **all PASS**. Blockers: **none**.

| Field | Value |
|-------|-------|
| **Production Worker** | `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`) |
| **Active** | `true` |
| **Node count** | `101` |
| **FU03 nodes** | `9` |
| **updatedAt** | `2026-07-15T21:09:45.123Z` (matches FU03 apply) |
| **`Run Strict Surface Repair`** | enabled (`disabled=false`) |
| **Restore nodes** | both **broken** (HOTFIX01 **not** yet on production) |
| **Proposed patch** | jsCode replace on 2 restore nodes only · node delta **0** · connections unchanged |
| **Sandbox harness** | HF01 10/10 PASS (offline) |
| **Do not** | retry `/run` before production HOTFIX01 apply |

**Decision:** `PC14_FU03_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL`  
**Next:** `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL_PERSIST` → then `PC14_FU03_HOTFIX01_PRODUCTION_APPLY`

---

## 2. Background

PC14-FU03 production apply (`44c05c3b`) succeeded at harness level (101 nodes, 9 FU03, repair enabled). Operator smoke then failed: Worker execution `3354` aborted at `Restore Format Run Items` after a valid STRICT QA REJECT path skipped `Format Run Pipeline`. Downstream restore still called `$('Format Run Pipeline').all()`, blocking final Telegram materials, Close Lock, and memory `blocked_dirty`, after a false “complete / sending materials…” preface. Lock stayed `task_id=pending`.

HOTFIX01 design (`7443c4e9`) selected Option A — dual-source restore on both restore nodes, 0 node delta. Sandbox implementation (`3a41bbc8`) applied that patch to inactive `tVGWi7Ud3zz2eGKo` and verified HF01 10/10 offline. This task proposes the same two-node `jsCode` transplant onto production — **proposal only**.

---

## 3. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `3a41bbc8` — `docs(metabot): add pc14 fu03 hotfix01 sandbox evidence` — **PASS** |
| Checkpoints `3a41bbc8` / `7443c4e9` / `cab4597a` / `44c05c3b` | Present — **PASS** |
| Staged index | Empty — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead **3** / behind **42** — **noted**; **no pull / no push** |
| Foreign WIP | Preserved (Website Factory / FP-0002 / OCPilot / `.recovery-temp`) — **PASS** |
| Credentials | `local/tokens/n8n-api.env` present (values not printed) — **PASS** |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, HOTFIX01 sandbox implementation/design/diagnostics/production apply & proposal packs, sandbox implementation manifest + sanitized after/before + diffs + harness + PC-07/TZ/side-effect/production-unchanged/secret scans.

**=== MARS AGENT GUARDRAILS v1 ===**  
Lane: B · Phase: production proposal · Repo root: `X:\AI MARS` · Volume: AI WS (X:)  
SCOPE LOCK: `projects/metabot-seo-content-agent/` + `local/pc14-fu03-hotfix01-production-proposal-2026-07-16/` · Allowed: n8n GET production/sandbox (read-only), sanitized proposal evidence write · Forbidden: production/sandbox PUT/activate, Telegram, OpenRouter, Sheets write, `/run`, git stage/commit/push/pull/clean/reset.

---

## 4. Production Preproposal Baseline

**Method:** `GET_ONLY` via n8n API for `p4mqb4VuPcemIDlC`. Compared to committed FU03 after-apply sanitized baseline (`44c05c3b` evidence).

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `p4mqb4VuPcemIDlC` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker` | same | **PASS** |
| active | `true` | `true` | **PASS** |
| node count | `101` | `101` | **PASS** |
| FU03 nodes | `9` | `9` | **PASS** |
| updatedAt | `2026-07-15T21:09:45.123Z` | FU03 apply timestamp | **PASS** |
| `Run Strict Surface Repair` | enabled | enabled | **PASS** |
| `Restore Format Run Items` | broken hard-require | broken (pre-hotfix) | **PASS** |
| `Restore Format Run Items After Lock` | broken hard-require | broken (pre-hotfix) | **PASS** |
| HOTFIX01 already applied | **false** | false | **PASS** |
| PC-07 Close Lock | `={{ $('Route Command').first().json.task_id }}` | same | **PASS** |
| TZ HOTFIX01 | structuredClone=0, clonePlain present, version intact | same | **PASS** |
| Non-target drift vs FU03 after-apply | none | none | **PASS** |
| Credentials | redacted in sanitized export | redacted | **PASS** |

**Drift decision:** no unexpected drift. Production remains the known FU03-applied broken-restore state — **apply-ready for HOTFIX01 only**.

---

## 5. Sandbox HOTFIX01 Source Verification

**Method:** live GET of `tVGWi7Ud3zz2eGKo` + committed sandbox after evidence (`3a41bbc8`).

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `tVGWi7Ud3zz2eGKo` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03` | same | **PASS** |
| active | `false` | `false` | **PASS** |
| node count | `101` | `101` | **PASS** |
| FU03 nodes | `9` | `9` | **PASS** |
| `Run Strict Surface Repair` | disabled | disabled (sandbox) | **PASS** |
| Both restore nodes HOTFIX01 | `true` | true | **PASS** |
| Fallback order | Pipeline → Reject → throw | same | **PASS** |
| `restore_source` annotations | present | present | **PASS** |
| Live jsCode vs committed after | match | match | **PASS** |
| Connections vs committed | unchanged | unchanged | **PASS** |
| PC-07 / TZ | intact | intact | **PASS** |
| Harness | 10/10 PASS | 10/10 | **PASS** |

Sandbox remains inactive. Do **not** copy sandbox disabled side-effect states into production.

---

## 6. Proposed Production Delta

| Item | Detail |
|------|--------|
| Target | `p4mqb4VuPcemIDlC` |
| Patch nodes | `Restore Format Run Items`, `Restore Format Run Items After Lock` |
| Patch type | `jsCode` replace only |
| Source | sandbox HOTFIX01 after export (`tVGWi7Ud3zz2eGKo`) |
| Node delta | **0** |
| Connection changes | **none** |
| Entire-workflow copy | **forbidden** |

**Preserve on production:** active `true`, id/name/webhook, credentials, Telegram/OpenRouter/Sheets enabled states, `Run Strict Surface Repair` **enabled**, PC-07 Close Lock mapping, TZ HOTFIX01, Intake/Admin untouched.

**Do not modify:** Format Run Pipeline, Format Strict Reject Message, Build Final Public Payload, Final Surface Strict Scan, Run Strict Surface Repair (except keep enabled), Extract Strict Surface Repair, Final Surface Strict Re-Scan, marker lists, TZ Strict Cleanup, PC-07 nodes, Intake, Admin, credentials, side-effect enabled states.

---

## 7. Target Node Diff

| Node | Prod length | Sandbox length | Prod broken | Sandbox HOTFIX01 | Would change |
|------|-------------|----------------|-------------|------------------|--------------|
| Restore Format Run Items | 150 | 1112 | true | true | **yes** |
| Restore Format Run Items After Lock | 150 | 1123 | true | true | **yes** |

Sandbox jsCode matches patch helper for both nodes. Production would receive dual-source restore with `restore_source` ∈ {`format_run_pipeline`, `format_strict_reject_message`}.

Note: literal version marker `v1-pc14-fu03-hotfix01-restore-reject-safe` is **not** required inside jsCode (functional fallback + harness verify the patch).

---

## 8. Production Apply Plan

Plan only — **not executed** in this task. Full steps in `pc14-fu03-hotfix01-production-proposal-apply-plan.json`.

1. GET production raw before apply.  
2. Save rollback: `local/pc14-fu03-hotfix01-production-apply-2026-07-16/rollback/worker-before-hotfix01.raw.json`.  
3. Sanitize before export.  
4. GET sandbox HOTFIX01 source.  
5. Extract only the two target `jsCode` values.  
6. Apply only those two values to production copy.  
7. Preserve id/name/active/webhook/credentials/non-targets/side-effects/PC-07/TZ/repair enabled.  
8. PUT production **only** after automated gates + operator approval.  
9. Re-GET production.  
10. Verify: active true, 101 nodes, 9 FU03, only 2 targets changed, node delta 0, connections unchanged, repair enabled, PC-07/TZ/side-effects/credentials intact, HOTFIX01 fallback present.  
11. Offline production-transformed harness HF01 **10/10** (no live side effects / no `/run`).  
12. Do **not** run operator smoke inside the apply task unless separately asked.

---

## 9. Rollback Plan

| Item | Detail |
|------|--------|
| Primary | Re-PUT production from raw before-hotfix01 backup |
| Path | `local/pc14-fu03-hotfix01-production-apply-2026-07-16/rollback/worker-before-hotfix01.raw.json` |
| Alternate | Restore both restore-node `jsCode` to broken `Format Run Pipeline` hard-require |
| Notes | Do not copy sandbox disabled side-effects; do not deactivate unless charter says so; pending lock cleanup remains separate |

---

## 10. Harness Plan

| Item | Detail |
|------|--------|
| Method | Offline local only — no Telegram / OpenRouter / Sheets / `/run` |
| When | After production transform (apply task), before claiming harness-verified |
| Cases | HF01-CLEAN-01, HF01-REPAIR-CLEAN-01, HF01-REJECT-01, HF01-REJECT-TASKID-01, HF01-RESTORE-A-01, HF01-RESTORE-B-01, HF01-PC07-01, HF01-TZ-01, HF01-SIDEFX-01, HF01-SECRET-01 |
| Expected | **10/10 PASS** |
| Reference | sandbox harness results under `pc14-fu03-hotfix01-sandbox-implementation/2026-07-16/` |

---

## 11. Operator Smoke Plan

**Do not execute now. Do not retry `/run` before production HOTFIX01 apply.**

Bait (same reject-path command as diagnostics):

```
/run тестовая проверка PC14-FU03 HOTFIX01 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

**Acceptable:** STRICT QA REJECT diagnostic sent + lock closes + memory `blocked_dirty`; **or** repair-clean materials + lock closes + memory `repair_attempted_clean` (or equivalent).

**Not acceptable:** false complete preface only; no final materials; pending lock left active; Worker error at restore nodes; banned markers in public output; raw Strategy JSON dump; stuck before Close Lock.

Pending old smoke lock cleanup remains **separate**, operator-approved only.

Full charter: `pc14-fu03-hotfix01-production-proposal-smoke-charter.md`.

---

## 12. Risk Matrix

| ID | Risk | Mitigation | Residual |
|----|------|------------|----------|
| R1 | Unexpected non-target drift at apply time | Preflight non-target drift gate → DRIFT_BLOCKED | low if gates hold |
| R2 | Copying sandbox disabled side-effects into production | jsCode-only transform; preserve production enabled states | low |
| R3 | Reject fan-out ordering still awkward under load | Dual-source restore; optional fan-out reorder deferred | medium (operator-observable) |
| R4 | False complete preface UX on reject | Smoke verifies materials/diagnostic + lock close | medium (UX) |
| R5 | Apply without offline harness | Mandatory HF01 10/10 after transform | low |
| R6 | `/run` before hotfix creates another pending lock | Charter forbids `/run` until apply | medium (ops) |

---

## 13. Evidence Files Created

Under `projects/metabot-seo-content-agent/exports/pc14-fu03-hotfix01-production-proposal/2026-07-16/`:

- `PC14-FU03-HOTFIX01-PRODUCTION-PROPOSAL-MANIFEST.md`
- `SEO-Content-Agent-Beta-v14-Worker.production-preproposal-hotfix01.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Worker.sandbox-hotfix01-source.sanitized.json`
- `pc14-fu03-hotfix01-production-proposal-delta.json`
- `pc14-fu03-hotfix01-production-proposal-target-node-diff.json`
- `pc14-fu03-hotfix01-production-proposal-preflight-gates.json`
- `pc14-fu03-hotfix01-production-proposal-apply-plan.json`
- `pc14-fu03-hotfix01-production-proposal-rollback-plan.json`
- `pc14-fu03-hotfix01-production-proposal-harness-plan.json`
- `pc14-fu03-hotfix01-production-proposal-smoke-charter.md`
- `pc14-fu03-hotfix01-production-proposal-risk-matrix.json`
- `pc14-fu03-hotfix01-production-proposal-secret-scan.json`
- Optional: `pc14-fu03-hotfix01-production-proposal-code-node-index.json`
- Optional: `pc14-fu03-hotfix01-production-proposal-side-effect-baseline.json`
- Optional: `pc14-fu03-hotfix01-production-proposal-structural-validation.json`
- Runner: `run-pc14-fu03-hotfix01-production-preproposal.mjs`

Raw local (not for commit yet): `local/pc14-fu03-hotfix01-production-proposal-2026-07-16/`  
(raw production preproposal, raw sandbox source, transform preview not-applied, preproposal-result, runner copy).

Report: `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-hotfix01-production-proposal.md`

---

## 14. Out-of-Scope Preserved

- No production PUT / activate / deactivate  
- No sandbox PUT / activate  
- No Intake / Admin changes  
- No Telegram / OpenRouter / Sheets live calls  
- No `/run` / `/health` / `/locks`  
- No lock or memory cleanup  
- No stage / commit / push / pull  
- Foreign WIP (Website Factory / FP-0002 / OCPilot / `.recovery-temp`) untouched  

---

## 15. SAFE UNKNOWN

- Exact live Telegram preface wording on reject path after HOTFIX01 (not re-smoked; sandbox inactive; no `/run` in this task).  
- Whether optional `Format Strict Reject Message` fan-out reorder is still needed under production load (deferred/open; not required for restore fix).  
- Exact n8n parallel fan-out timing under load remains operator-observable after apply + smoke.  
- Literal version string `v1-pc14-fu03-hotfix01-restore-reject-safe` is absent from restore `jsCode` (functional HOTFIX01 markers + harness verify the patch).  
- Whether the old pending smoke lock (`chat:499423375:1784151029009` / `seo202607152130389k7zou`) still exists live — out of scope; cleanup needs separate operator approval.

---

## 16. Final Status

| Field | Value |
|-------|-------|
| **Proposal** | `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL` |
| **Decision** | `PC14_FU03_HOTFIX01_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next** | `PC14_FU03_HOTFIX01_PRODUCTION_PROPOSAL_PERSIST` |
| **After persist** | `PC14_FU03_HOTFIX01_PRODUCTION_APPLY` |
| **Final status** | `COMPLETE — PC14-FU03 HOTFIX01 production proposal ready` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |
| **Production mutated** | **No** |
| **Sandbox mutated** | **No** |
| **Staged / committed** | **No** |

Awaiting operator review.
