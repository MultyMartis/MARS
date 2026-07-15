# REPORT — MetaBOT SEO Agent PC14-FU03 Production Proposal

**Date:** 2026-07-16  
**Classification:** Production proposal only · GET-only production + sandbox baseline · no live mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — PC14-FU03 Repair Loop / Strict Surface Governance  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  

| Label | Value |
|-------|-------|
| **Proposal** | `PC14_FU03_PRODUCTION_PROPOSAL` |
| **Based on sandbox implementation** | `PC14_FU03_SANDBOX_IMPLEMENTATION_APPLIED_HARNESS_VERIFIED` |
| **Sandbox implementation commit** | `a64da270` |
| **Sandbox workflow** | `tVGWi7Ud3zz2eGKo` |
| **Production Worker** | `p4mqb4VuPcemIDlC` |
| **Decision** | `PC14_FU03_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next step** | `PC14_FU03_PRODUCTION_PROPOSAL_PERSIST` |
| **Final status** | `COMPLETE — PC14-FU03 production proposal ready` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |

**Current statuses preserved / context:**

| Item | Status |
|------|--------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` |
| PC14-FU-01 | `PC14_FU01_CLOSED_NEXT_SELECTED` |
| PC14-FU-02 production apply | `PC14_FU02_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU-02 timeout diagnostics | `PC14_FU02_SMOKE_TIMEOUT_DIAGNOSED_RETRY_BLOCKED` |
| PC14-FU02 HOTFIX01 production apply | `PC14_FU02_HOTFIX01_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU03 governance audit | `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED` |
| PC14-FU03 repair loop proposal | `PC14_FU03_REPAIR_LOOP_PROPOSAL_READY_FOR_SANDBOX_DESIGN` |
| PC14-FU03 sandbox design | `PC14_FU03_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| PC14-FU03 sandbox implementation | `PC14_FU03_SANDBOX_IMPLEMENTATION_APPLIED_HARNESS_VERIFIED` (`a64da270`) |
| **This task** | `PC14_FU03_PRODUCTION_PROPOSAL` → ready for approval |

**Checkpoint commits verified through:** `a64da270`

**Constraints honored:** Production Worker **not** patched. Sandbox **not** mutated. No Telegram send. No OpenRouter call. No Sheets write. No `/run` / `/health` / `/locks`. No Intake/Admin mutation. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

PC14-FU03 is **ready for operator-approved production apply**. Fresh GETs confirm:

- Production Worker still matches the post-HOTFIX01 baseline (92 nodes, `updatedAt` `2026-07-13T21:49:02.829Z`, no FU03 nodes).
- Sandbox `tVGWi7Ud3zz2eGKo` still carries the harness-verified FU03 repair-loop implementation (101 nodes, inactive, 21/21 PASS).

| Field | Value |
|-------|-------|
| **Production Worker** | `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`) |
| **Active** | `true` |
| **Node count now** | `92` |
| **Node count after proposed apply** | `101` (+9 FU03) |
| **updatedAt** | `2026-07-13T21:49:02.829Z` (matches HOTFIX01) |
| **TZ version** | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` |
| **`structuredClone`** | `0` · `clonePlain` present |
| **Sandbox** | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03` (`tVGWi7Ud3zz2eGKo`, active `false`) |
| **Harness** | FU03-SOT / SCAN / REPAIR / BLOCK / MEM / GET / STRICT / SCOPE — **21/21 PASS** |
| **Diff scope** | Add 9 FU03 nodes · modify `Format Run Pipeline` + `Prepare Memory Row Run` · rewire Normalize→FU03 gate |
| **Production-critical exception** | Enable `Run Strict Surface Repair` (disabled only in sandbox) |

**This task does not perform live apply.** Operator approval + persistence + apply-phase fresh export are mandatory next gates.

**Decision:** `PC14_FU03_READY_FOR_PRODUCTION_APPROVAL`  
**Next:** `PC14_FU03_PRODUCTION_PROPOSAL_PERSIST`

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `d3f3fdf2` (after MetaBOT `a64da270`) — **PASS** |
| Checkpoint `a64da270` | Present — **PASS** |
| Staged index | Empty — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead **31** / behind **28** — **noted**; **no pull / no push** |
| Foreign WIP | Preserved (Website Factory / FP-0002 / recovery-temp / etc.) — **PASS** |
| Credentials | `local/tokens/n8n-api.env` present (values not printed) — **PASS** |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, FU03 sandbox implementation / design / repair-loop / governance reports, FU02 HOTFIX01 production apply report, issue backlog, sandbox implementation manifest + harness + scope/node/graph/connection/credential/PC-07 checks + after-patch sanitized Worker.

**=== MARS AGENT GUARDRAILS v1 ===**  
Lane: B · Phase: production proposal · Repo root: `X:\AI MARS` · Volume: AI WS (X:)  
SCOPE LOCK: `projects/metabot-seo-content-agent/` + `local/pc14-fu03-production-proposal-2026-07-16/` · Allowed: n8n GET production/sandbox (read-only), sanitized proposal evidence write · Forbidden: production/sandbox PUT/activate, Telegram, OpenRouter, Sheets write, `/run`, git stage/commit/push/pull/clean/reset.

---

## 3. Fresh Production Baseline

**Method:** `GET_ONLY` n8n API for `p4mqb4VuPcemIDlC`. Compared to committed HOTFIX01 after-apply sanitized baseline.

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `p4mqb4VuPcemIDlC` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker` | same | **PASS** |
| active | `true` | `true` | **PASS** |
| node count | `92` | `92` | **PASS** |
| updatedAt | `2026-07-13T21:49:02.829Z` | HOTFIX01 apply | **PASS** |
| FU03 nodes | **none** | none | **PASS** |
| `TZ Strict Cleanup` | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` | HOTFIX01 | **PASS** |
| `structuredClone` | `0` | `0` | **PASS** |
| `clonePlain` | present | present | **PASS** |
| Normalize → Format | direct | pre-FU03 | **PASS** |
| PC-07 Close Lock | `={{ $('Route Command').first().json.task_id }}` | same | **PASS** |
| Side-effect vs HOTFIX01 | no drift | none | **PASS** |
| Non-target jsCode vs HOTFIX01 | no unexpected drift | none | **PASS** |
| Route Command | unchanged vs HOTFIX01 | unchanged | **PASS** |

**Drift decision:** no unexpected drift since HOTFIX01 / sandbox implementation. Production remains valid apply target for FU03 graph/code only.

---

## 4. Fresh Sandbox Source

**Method:** live GET of `tVGWi7Ud3zz2eGKo` + committed sandbox after-patch evidence (`a64da270`).

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `tVGWi7Ud3zz2eGKo` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03` | same | **PASS** |
| active | `false` | `false` | **PASS** |
| node count | `101` | `101` | **PASS** |
| 9 FU03 nodes | all present | all present | **PASS** |
| Modified | `Format Run Pipeline`, `Prepare Memory Row Run` | same | **PASS** |
| `Run Strict Surface Repair` | present + **disabled** | sandbox-only disable | **PASS** |
| Side-effect nodes | Telegram/OpenRouter/Sheets/locks disabled | sandbox clone | **PASS** (do not copy to prod) |
| TZ HOTFIX01 | preserved | preserved | **PASS** |
| PC-07 Close Lock | preserved | preserved | **PASS** |
| Graph gate | Normalize → Build → Scan → IF → Format\|Repair…\|Reject | design | **PASS** |
| Harness 21/21 | `allPass=true` | PASS | **PASS** |
| Live vs committed evidence | jsCode align on FU03 targets | align | **PASS** |

**Sandbox decision:** donor verified for production FU03 graph/code. Identity/active/side-effect disables must **not** be copied.

---

## 5. Production vs Sandbox Diff

| Category | Detail |
|----------|--------|
| **Nodes added (9)** | Build Final Public Payload · Final Surface Strict Scan · IF Final Surface Clean · Build Strict Surface Repair Payload · Run Strict Surface Repair · Extract Strict Surface Repair · Final Surface Strict Re-Scan · IF Repaired Surface Clean · Format Strict Reject Message |
| **Nodes removed** | none |
| **Nodes modified (2)** | `Format Run Pipeline` (12 435 → 16 169 js chars) · `Prepare Memory Row Run` (791 → 2 094) |
| **Connections** | Remove Normalize→Format; insert full FU03 gate graph (see connection plan) |
| **Ignore as patch diff** | id / name / active / webhook / updatedAt / tags / etc. |
| **Sandbox-only disables (11)** | Send Telegram Local/Single/Run/Memory Get · OpenRouter Single Mode · Append Memory Local/Single/Run · Close Lock Before Sending · Close Single Lock Before Sending · Finish Lock — **must remain production-enabled as currently configured** |
| **active** | prod `true` vs sandbox `false` — **not a patch field** |

---

## 6. Proposed Production Patch Scope

**Apply strategy (document only — not executed):**

1. Fresh GET production.
2. Save raw rollback: `local/pc14-fu03-production-apply-2026-07-16/rollback/worker-before-pc14-fu03.raw.json`.
3. Transform production JSON in memory:
   - add 9 FU03 nodes from sandbox (production-safe positions; **enable** `Run Strict Surface Repair`);
   - modify `Format Run Pipeline` + `Prepare Memory Row Run` jsCode from sandbox;
   - apply connection plan (Normalize→FU03 gate; preserve Format→Memory/Take First; preserve shortcut→Format);
   - keep production id / name / webhook / `active=true`;
   - keep production side-effect enabled states + credentials;
   - keep PC-07 Close Lock mapping;
   - Intake/Admin untouched.
4. PUT production Worker only after operator approval in a **later** apply task.
5. Re-GET and verify: active true · 101 nodes · FU03 present · side-effects preserved · credentials preserved · PC-07 mapping · HOTFIX01 intact · harness/scope on sanitized export.

| Item | Detail |
|------|--------|
| Node count delta | 92 → 101 |
| Connection changes | yes (FU03 gate) |
| Credential changes | none (preserve production bindings) |
| Intake / Admin | unchanged |
| Strict Cleanup / Strict Risk Scanner maps | not expanded |
| TZ HOTFIX01 | preserved |

---

## 7. Production-Specific Decisions

### 7.1 Run Strict Surface Repair enabled state

- Sandbox: **disabled** (avoid live OpenRouter).
- Production: **enable** (`disabled=false`) with existing OpenRouter HTTP credential/header pattern (as used by repair/text HTTP nodes).
- Max **1** call per dirty task; skip when final scan is clean.
- Must be covered by post-apply operator smoke.

### 7.2 Side-effect node preservation

Preserve production Telegram / OpenRouter / Sheets append / lock nodes **as currently enabled**. Do not propagate sandbox `disabled=true`. Keep `active=true`.

### 7.3 Strategy output policy

Hide raw Strategy JSON by default; render safe strategy summary only if included in public payload; no `JSON.stringify(seoStrategy.table_strategy)` dump.

### 7.4 QA / Factcheck summary policy

Always include verdict/score; include free-text summaries only if clean per scan policy; otherwise omit / verdict-only.

### 7.5 Strict reject behavior

If dirty after repair: short diagnostic only — `STRICT QA REJECT — output blocked before final send`. Memory `blocked_dirty`. Close lock with real `task_id`.

### 7.6 Natural-language banned words

Central hard SOT always. NL custom markers detected in `Build Final Public Payload`. Route Command unchanged in this wave. Custom markers task-scoped.

---

## 8. Side-Effect Preservation

| Concern | Proposal action |
|---------|-----------------|
| Telegram sends | Keep production enabled states |
| OpenRouter (existing) | Keep production enabled states |
| Sheets lock/memory append | Keep production enabled states |
| Close Lock / Finish Lock | Keep production enabled + PC-07 `task_id` expression |
| New `Run Strict Surface Repair` | **Enable** in production (sandbox-only disable) |
| Sandbox `active=false` | Do not copy |
| Credentials | Preserve production credential bindings |
| Intake / Admin | Untouched |

Evidence: `exports/pc14-fu03-production-proposal/2026-07-16/pc14-fu03-production-proposal-side-effect-preservation.json`

---

## 9. Rollback Strategy

| Item | Detail |
|------|--------|
| Rollback file (apply phase) | `local/pc14-fu03-production-apply-2026-07-16/rollback/worker-before-pc14-fu03.raw.json` |
| Method | Fresh raw GET before PUT; on failure restore 92-node pre-FU03 Worker |
| Post-rollback verify | nodeCount=92 · no FU03 nodes · HOTFIX01 TZ · active=true · PC-07 mapping · side-effects restored |
| Proposal-phase raw reads | `local/pc14-fu03-production-proposal-2026-07-16/` (not for commit) |

---

## 10. Post-Apply Smoke Charter

**Do not run during this proposal task.**

```
/run тестовая проверка PC14-FU03 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

Expected: complete or strict-block; no raw Strategy JSON dump; no banned markers in full payload; residuals → diagnostic only; Task ID visible; lock closes; memory `approved_clean` | `repair_attempted_clean` | `blocked_dirty`.

Full charter: `exports/pc14-fu03-production-proposal/2026-07-16/pc14-fu03-production-proposal-smoke-charter.md`

---

## 11. Risk Classification

| Risk | Proposal blocking? | Apply blocking? | Mitigation |
|------|--------------------|-----------------|------------|
| Live repair OpenRouter call | no | no | max 1 · dirty-only · smoke |
| Graph/branch routing | no | no | connection plan + post-apply graph checks |
| Final send blocked UX | no | no | documented diagnostic UX |
| Memory schema compatibility | no | no | tolerant fields; Sheets expand deferred |
| `/get` live behavior | no | no | v1 out of FU03 gate; backlog |
| Shortcut modes bypass | no | no | accepted v1 Normalize-path-only |
| Sheets schema not expanded | no | no | SAFE UNKNOWN · non-blocking |
| Side-effect preservation | no | **yes** (gate in apply) | mandatory enabled-state checklist + re-GET |
| Rollback complexity | no | no | raw rollback before PUT |
| Local/remote git divergence | no | no | no pull/push; persist separately |

No proposal blockers found.

---

## 12. Evidence Files Created

**Repo (sanitized / proposal pack):**  
`projects/metabot-seo-content-agent/exports/pc14-fu03-production-proposal/2026-07-16/`

- `SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu03.before-proposal.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14-fu03.proposal-source.sanitized.json`
- `pc14-fu03-production-proposal-diff-summary.json`
- `pc14-fu03-production-proposal-node-plan.json`
- `pc14-fu03-production-proposal-connection-plan.json`
- `pc14-fu03-production-proposal-side-effect-preservation.json`
- `pc14-fu03-production-proposal-risk-rollback.json`
- `pc14-fu03-production-proposal-smoke-charter.md`
- `pc14-fu03-production-proposal-code-node-index.json` (optional)
- `pc14-fu03-production-proposal-secret-scan.json` (optional)
- `PC14-FU03-PRODUCTION-PROPOSAL-MANIFEST.md`
- `run-pc14-fu03-production-preproposal.mjs` (GET-only helper)

**Report:**  
`projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-production-proposal.md`

**Raw local (not for commit):**  
`local/pc14-fu03-production-proposal-2026-07-16/` — production GET, sandbox GET, `preproposal-result.json`

---

## 13. Out-of-Scope Preserved

- Website Factory / FP-0002 / Shpigovsky / recovery-temp / unrelated foreign WIP — **not touched**
- Intake / Admin workflows — **not touched**
- Production / sandbox Worker mutation — **not performed**
- Telegram / OpenRouter / Sheets / `/run` — **not called**
- Git stage / commit / push / pull — **not performed**

---

## 14. SAFE UNKNOWN

| Item | Acceptable for proposal? | Notes |
|------|--------------------------|-------|
| Shortcut modes bypass FU03 gate (v1) | yes | Normalize path only |
| `/get` live path mocked via memory contract in harness | yes | live `/get` not re-proven here |
| Sheets schema not expanded | yes | memory fields may not have columns |
| Live LLM repair quality untested | yes | sandbox repair node disabled; smoke after apply |
| Route Command NL flag unchanged | yes | detection in Build Final Public Payload |
| Branch ahead/behind vs origin | noted | irrelevant to n8n apply; no pull |

None of the above blocks this proposal.

---

## 15. Final Status

| Field | Value |
|-------|-------|
| **Proposal** | `PC14_FU03_PRODUCTION_PROPOSAL` |
| **Decision** | `PC14_FU03_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next** | `PC14_FU03_PRODUCTION_PROPOSAL_PERSIST` |
| **Final status** | `COMPLETE — PC14-FU03 production proposal ready` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |
| **Production apply** | **not executed** (awaits persist + operator-approved apply task) |

Awaiting operator review.
