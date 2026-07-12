# REPORT — MetaBOT SEO Agent v14 PC14-FU02 Sandbox Patch Proposal

**Date:** 2026-07-13  
**Classification:** Proposal-only · documentation · no live n8n mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Worker TZ/outline-side strict residual sanitizer  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  

| Label | Value |
|-------|-------|
| **Backlog item** | `PC14_FU02_TZ_STRICT_RESIDUAL_CLEANUP_AUDIT` |
| **Proposal** | `PC14_FU02_SANDBOX_PATCH_PROPOSAL` |
| **Selected path** | **FU-02A / Option B** — dedicated TZ/outline sanitizer |
| **Decision** | `PC14_FU02_READY_FOR_SANDBOX_IMPLEMENTATION` |
| **Recommended next step** | `PC14_FU02_SANDBOX_PATCH_IMPLEMENTATION` |

**Current statuses preserved:**

| Item | Status |
|------|--------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` |
| PC14-FU-01 | `PC14_FU01_CLOSED_NEXT_SELECTED` |
| PC14-FU-02 audit | `PC14_FU02_READY_FOR_SANDBOX_PATCH_PROPOSAL` (predecessor) |
| Production Worker | `p4mqb4VuPcemIDlC` · active · Strict Cleanup `v15-strict-cleanup-pc14-fu01-r1` |

**Checkpoint commits verified through:** `535acbce` (FU-02 audit)

**Constraints honored:** No live n8n mutation. No Telegram / OpenRouter / Sheets. No sandbox create. No workflow patch. No push. Foreign WIP preserved.

---

## 1. Executive Summary

This proposal defines a **sandbox-only** future patch for PC14-FU-02: insert a dedicated TZ/outline sanitizer that removes PC-14 R1 + FU-01 strict residuals from SEO ТЗ / outline-side fields (especially `outline.tables.decision_reason`) **before** `Format Run Pipeline` renders Telegram/memory output.

| Item | Decision |
|------|----------|
| **Production** | Unchanged in this task and in the next implementation task until a separate production proposal |
| **Sandbox workflow name** | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02` |
| **Sandbox webhook (if needed)** | `seo-content-agent-worker-sandbox-pc14-fu02` |
| **Clone source** | Production Worker `p4mqb4VuPcemIDlC` |
| **Graph strategy** | **Strategy A** — insert code node `TZ Strict Cleanup` after `Run Extract Outline`, with mandatory companion `$()` / `$node[]` retargets |
| **Fallback** | **Strategy B** — sanitize inside `Run Extract Outline` if insertion/retarget harness fails |
| **Non-targets (wave 1)** | `Strict Cleanup` v15, `Strict Risk Scanner`, `Format Run Pipeline`, PC-07 lock nodes, final SEO Text path |
| **Harness gate** | Sandbox harness required before any production apply |

Smoke residual basis: Task ID `seo20260712201612oo0m85` — final SEO Text clean; SEO ТЗ still contains `для удобства восприятия` in table `Причина`.

**This task does not apply the patch.**

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Staged changes (pre-task) | Empty — **PASS** |
| HEAD at task start | `535acbce` — FU-02 TZ residual audit — **PASS** |
| Checkpoint `535acbce` | Present — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead **17** / behind **17** — **noted**; no pull / no push |
| Live API / Telegram / OpenRouter / Sheets | None this session — **PASS** |
| Foreign WIP | Preserved — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, FU-02 audit, FU-01 closeout / operator smoke / production apply / production proposal, PC-14 strict cleanup audit / closeout, issue backlog and test matrix.

**Evidence exports read:** `pc14-fu01-operator-smoke-*.json`, production Worker after-apply sanitized JSON, live-v14 `PROMPT-AND-CODE-NODE-INDEX-v14.md`, `NODE-INVENTORY-v14.md`.

---

## 3. Source Evidence Reviewed

| Source | Role |
|--------|------|
| `REPORT-metabot-seo-agent-v14-pc14-fu02-tz-strict-residual-cleanup-audit-proposal.md` | Root cause + FU-02A selection |
| `REPORT-metabot-seo-agent-v14-pc14-fu01-closeout-next-backlog-selection.md` | Selected FU-02 backlog |
| `REPORT-metabot-seo-agent-v14-pc14-fu01-operator-smoke-verification.md` | Live residual classification |
| `pc14-fu01-operator-smoke-output-scan.json` | TZ hit `удобств*` + snippet |
| `pc14-fu01-operator-smoke-verify-summary.json` | Worker `3344` / QA / PC-07 guards |
| `SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu01.after-apply.sanitized.json` | Graph + node code truth |
| `PROMPT-AND-CODE-NODE-INDEX-v14.md` / `NODE-INVENTORY-v14.md` | Node inventory |
| FU-01 / PC-14 reports | Strict Cleanup scope = final text only |

---

## 4. FU-02 Audit Recap

| Finding | Evidence |
|---------|----------|
| Residual phrase | `для удобства восприятия` |
| Field | `outline.tables.decision_reason` → Format `Причина:` |
| Origin | LLM outline generation (not hardcoded) |
| Final SEO Text | Clean for PC-14 R1 + FU-01 |
| `Strict Cleanup` / `Strict Risk Scanner` | Touch only `generated_text.content_markdown` |
| Classification | Outline/TZ-side **scope gap**, not FU-01 failure |
| Selected remediation | **FU-02A / Option B** — dedicated TZ/outline sanitizer |

Do **not** reopen PC14-FU-01. Do **not** broaden Strict Cleanup to outline in wave 1.

---

## 5. Graph Placement Analysis

### 5.1 Confirmed nodes (production after-apply export)

| Node | Exists? | Role |
|------|---------|------|
| `Run Extract Outline` | **Yes** | Parse outline JSON; emit `{ ..., outline }` |
| Immediate successor | `Switch Run After Outline` | Branch `outline_only` → Format; `continue` → Status Strategy |
| First SEO ТЗ renderer (run path) | `Format Run Pipeline` | Builds `=== 1. SEO ТЗ ===` including `Причина` |
| Existing outline normalization between extract and format? | **No dedicated sanitizer** | Only parse/passthrough |
| `Strict Cleanup` | After text repair | Final markdown only |
| `Strict Risk Scanner` | After table sanity | Final markdown only |

### 5.2 Relevant connections

```
Run Outline
  → Run Extract Outline
  → Switch Run After Outline
       ├─ outline_only=true  → Format Run Pipeline
       └─ continue           → Status Strategy → … → Restore Outline Data
                                                    → Build SEO Strategy Payload
                                                    → … text / Strict Cleanup / Format …
```

### 5.3 Hard name bindings (insertion risk)

| Consumer | Binding | Risk if new node inserted without retarget |
|----------|---------|--------------------------------------------|
| `Restore Outline Data` | `$('Run Extract Outline').all()` | Continues to read **unsanitized** outline on full `/run` path |
| `Extract SEO Strategy` | `$node['Run Extract Outline'].json` | Strategy extract may still see raw outline |

Therefore a bare “insert node only” change is **insufficient**. Strategy A requires companion retargets.

### 5.4 Strategy comparison

| Strategy | Description | Pros | Cons | Verdict |
|----------|-------------|------|------|---------|
| **A** | Insert `TZ Strict Cleanup` after `Run Extract Outline`; retarget Switch input + `$()` / `$node[]` readers | Clear scope; Format/Strict untouched; matches FU-02A | Connection + 2 reference edits | **Recommended** |
| **B** | Patch sanitize into end of `Run Extract Outline` | No connection changes; all `$('Run Extract Outline')` readers auto-clean | Mixes parse + sanitize | Fallback if A harness fails |
| **C** | Patch `Format Run Pipeline` | Last-mile clean | Masks data; higher blast radius; against wave-1 non-goals | Fallback only |
| **D** | Blocked pending graph evidence | — | Graph evidence is sufficient | **Not selected** |

### 5.5 Recommended graph strategy

**Strategy A — insert single new code node**

| Field | Value |
|-------|--------|
| New node name | `TZ Strict Cleanup` (alias acceptable: `Sanitize Outline Strict Families`) |
| Placement | Between `Run Extract Outline` and `Switch Run After Outline` |
| Connection change | `Run Extract Outline` → **`TZ Strict Cleanup`** → `Switch Run After Outline` |
| Companion edit 1 | `Restore Outline Data`: `$('Run Extract Outline')` → `$('TZ Strict Cleanup')` |
| Companion edit 2 | `Extract SEO Strategy`: `$node['Run Extract Outline']` → `$node['TZ Strict Cleanup']` |
| Unchanged | `Format Run Pipeline`, `Strict Cleanup`, `Strict Risk Scanner`, lock/Telegram/OpenRouter/Sheets nodes |

**Format Run Pipeline can and must remain unchanged** under Strategy A/B.

If sandbox insertion or retarget tests fail: fall back to **Strategy B** in the same sandbox clone (still sandbox-only). Do **not** jump to production or Strategy C without a new proposal.

### 5.6 Single-mode note

`Format Single Mode Message` also renders `tables.decision_reason`. Wave-1 primary path is `/run` via `Run Extract Outline`. Single-mode `/outline` parity is **recommended for the same sandbox wave if low-cost** (reuse sanitizer helper), else document as follow-up — do not block Strategy A.

---

## 6. Proposed Patch Scope

### 6.1 In scope (sandbox implementation)

1. Clone production Worker `p4mqb4VuPcemIDlC` → inactive sandbox `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02`.
2. Optional webhook path rename to `seo-content-agent-worker-sandbox-pc14-fu02` if sandbox webhook is enabled for harness.
3. Insert / enable `TZ Strict Cleanup` (Strategy A) **or** Strategy B in-node sanitize.
4. Companion `$()` / `$node[]` retargets if Strategy A.
5. Sandbox harness side-effect suppression (Telegram / OpenRouter / Sheets writes).
6. Export before/after sanitized sandbox workflow + harness evidence (future task artifacts).

### 6.2 Sanitize allowlist (user-facing SEO ТЗ / outline fields)

Sanitize string (and string-bearing nested) values on:

| Path | Why |
|------|-----|
| `outline.tables.decision_reason` | Smoke residual primary |
| `outline.tables.table_ideas[]` title/purpose (and string ideas) | Printed as «Идеи таблиц» |
| `outline.meta_description` | Printed in SEO ТЗ |
| `outline.title_options[]` | Printed in SEO ТЗ |
| `outline.h1` | Printed |
| `outline.sections[].h2` | Printed |
| `outline.sections[].summary` | Printed as Summary |
| `outline.sections[].key_takeaways[]` | Printed as «Выводы» |
| `outline.sections[].visual_elements[]` | Printed as «Визуал» |
| `outline.sections[].keywords[]` | Printed (clean if residual) |
| `outline.faq[]` question / answer_goal if present | FAQ printed; answer_goal may feed prompts |
| `outline.cta` | Printed if string |
| `outline.entity_connections[]` reason/from/to strings | Printed |
| Any other string field later proven printed by `Format Run Pipeline` into SEO ТЗ | Expand allowlist with evidence |

### 6.3 Do not sanitize

| Field / area | Reason |
|--------------|--------|
| User prompt / `task_input` / `task_raw` | Intentional operator content |
| `generated_text.content_markdown` | Owned by Strict Cleanup v15 |
| SEO QA verdict/reason / problems | Quality metadata |
| Factcheck fields | Quality metadata |
| Raw LLM logs / HTTP bodies | Debug |
| Internal debug / scores except via Format TZ | Not TZ UX |
| Memory / `active_jobs` locks | PC-07 |
| `task_id` / routing / flags | Identity & control |

### 6.4 Explicit non-changes (wave 1)

- `Strict Cleanup` jsCode / version string `v15-strict-cleanup-pc14-fu01-r1`
- `Strict Risk Scanner` jsCode
- `Format Run Pipeline` jsCode (Strategy A/B)
- PC-07 `Close Lock Before Sending` mapping
- Production workflow active state
- Intake / Admin workflows

---

## 7. Sanitizer Design

### 7.1 Role

Pure deterministic function over allowlisted outline paths. Phrase-first, Unicode-aware, aligned with Strict Cleanup v15 family map. Preserve meaning and SEO structure; avoid blanking required fields.

### 7.2 Family map (v15-compatible)

**PC-14 R1:** `аккуратн*` · `удобств*` · `удобн*` · `позволя*`  
**FU-01:** `обеспеч*` · `контрол*` · `безопасн*` · `специализирован*` · `надежн*` · `надёжн*`

Reuse v15 helpers: Unicode boundaries `BP`/`BS`, `rb()`, phrase-first longest matches, then morphology maps where grammar-safe.

### 7.3 Suggested replacement intent (examples)

| Input residual | Preferred replacement intent |
|----------------|------------------------------|
| `для удобства восприятия` | `для структурированного представления` (prefer full-phrase rule **before** shorter `для удобств(а\|о)` → `для наглядности`) |
| `что позволяет` / `что позволяет определить` | Prefer v15-safe phrasing (`при этом возможно` / `используется для…`); avoid banned synonym loops |
| `для обеспечения безопасности` | `для соблюдения требований работы` (or v15 longer-phrase maps first) |
| `контроль качества` | `проверка результата` |
| `специализированные инструменты` | `профильные инструменты` **or** v15 `инструменты для измерений` — pick one map and keep harness stable |
| `надежность соединений` / `надёжность соединений` | `стабильность соединений` |

**Rule:** longest phrase first; do not leave orphan tails (e.g. avoid `для наглядности восприятия`).

### 7.4 Shape hardening

| Risk | Design response |
|------|-----------------|
| `decision_reason` null / missing | No-op |
| Non-string reason | Coerce string only if safe; else skip |
| Nested table_ideas objects | Clean `title` / `purpose` strings |
| Empty after clean | Keep prior non-empty value if replacement would empty required reason; log `tz_strict_cleanup.skipped_empty` in node meta (sandbox telemetry) |

### 7.5 Node contract (proposed)

```text
Input:  Run Extract Outline item json (route fields + outline)
Output: same json shape with sanitized outline + meta:
  tz_strict_cleanup: {
    version: 'v1-tz-strict-cleanup-pc14-fu02-r1',
    replacements: <number>,
    paths_touched: <string[]>
  }
```

Must **not** mutate `generated_text` (absent at this stage anyway).

### 7.6 Sandbox harness requirement

**Mandatory** before any production proposal/apply:

1. Offline pure-function unit harness for TZ01–TZ07.
2. Sandbox workflow clone with side effects disabled.
3. Before/after sanitized exports + scope diff (only intended nodes).
4. Non-regression NR01–NR09 + SG01–SG05 evidence.
5. Operator approval gate for later production proposal.

---

## 8. Sandbox Implementation Plan

**Next task label:** `PC14_FU02_SANDBOX_PATCH_IMPLEMENTATION`

| Step | Action |
|------|--------|
| 1 | Clone production Worker `p4mqb4VuPcemIDlC` → `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu02` |
| 2 | Ensure sandbox **inactive** (or safe webhook-only harness) |
| 3 | Disable/suppress side-effect nodes: Telegram sends, OpenRouter HTTP, Google Sheets writes, memory append if not needed |
| 4 | Apply Strategy A (preferred) or Strategy B (fallback): TZ/outline sanitizer only + companion retargets |
| 5 | Do **not** touch production |
| 6 | Export before/after sanitized sandbox workflow JSON |
| 7 | Run FU-02 harness (TZ / NR / SG) |
| 8 | Produce sandbox implementation report + evidence pack |
| 9 | Do not stage/commit implementation artifacts unless separately requested |

Production apply remains a **later** gated task after sandbox evidence + operator approval.

---

## 9. FU-02 Harness Matrix

### 9.1 TZ residual tests

| ID | Fixture | Expect |
|----|---------|--------|
| **TZ01** | `для удобства восприятия` | Family gone; readable Russian; field non-empty |
| **TZ02** | `что позволяет определить` | `позволя*` cleaned |
| **TZ03** | `для обеспечения безопасности` | `обеспеч*` / `безопасн*` cleaned |
| **TZ04** | `контроль качества` | → neutral (`проверка результата` class) |
| **TZ05** | `специализированные инструменты` | cleaned |
| **TZ06** | `надежность соединений` (+ `надёжность…`) | both spellings cleaned |
| **TZ07** | Mixed multi-family sentence | All target families cleaned; meaning preserved; no empty required fields |

### 9.2 Non-regression

| ID | Guard |
|----|-------|
| **NR01** | Final SEO Text / `content_markdown` untouched by TZ sanitizer |
| **NR02** | Strict Cleanup v15 node unchanged (hash/version) |
| **NR03** | Strict Risk Scanner unchanged |
| **NR04** | Format Run Pipeline unchanged under Strategy A/B |
| **NR05** | SEO QA approved case remains structurally valid when final text clean |
| **NR06** | Tables still render (`Required` / `Причина` / `Идеи таблиц`) |
| **NR07** | Outline sections still include summary / key_takeaways / entities / visual fields as expected |
| **NR08** | No OpenRouter / Telegram / Sheets side effects in sandbox harness |
| **NR09** | PC-14 / FU-01 final-text cleanup tests remain PASS |

### 9.3 Scope guards

| ID | Guard |
|----|-------|
| **SG01** | Only intended TZ sanitizer insert/patch (+ Strategy A companion retargets) |
| **SG02** | No lock / memory /get / Telegram / OpenRouter node logic changes beyond sandbox disables |
| **SG03** | PC-07 Close Lock mapping unchanged |
| **SG04** | Production workflow active state unchanged |
| **SG05** | Sandbox remains inactive unless explicitly needed for a controlled test |

---

## 10. Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Nested/irregular outline shapes | Medium | Allowlist paths; type guards; no deep blind walk of entire JSON |
| `decision_reason` null/object variance | Medium | Coerce/skip safely; TZ01–TZ07 fixtures |
| Over-cleaning degrades SEO ТЗ quality | Medium | Phrase-first maps; human review samples; preserve non-empty |
| New node insertion breaks connections | Medium–High | Strategy A companion retargets; harness SG01; Strategy B fallback |
| `$('Run Extract Outline')` bypasses sanitizer | High if ignored | Mandatory retarget of `Restore Outline Data` + `Extract SEO Strategy` |
| Patching Format masks generator issues | High (Strategy C) | Prefer A/B; C only as last resort proposal |
| Accidental final-text / QA mutation | High if wrong scope | Path allowlist; NR01–NR03 |
| Production drift vs 2026-07-13 export | Medium | Re-export baseline before apply |
| Single-mode residual remains | Low–Medium | Optional same-wave helper; else follow-up |

**Production apply gate:** sandbox evidence + operator approval + separate production proposal only.

---

## 11. Non-Goals

- Production apply in this or the immediate sandbox-implementation wave without approval
- Broadening Strict Cleanup / Strict Risk Scanner to outline in wave 1
- Prompt-only Option A as the sole fix
- Formatter-only Option C as primary
- Reopening FU-01 final-text work
- Changing PC-07 lock lifecycle
- Live Telegram / OpenRouter / Sheets calls during proposal

---

## 12. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Area | Status |
|------|--------|
| Live n8n / Telegram / OpenRouter / Sheets | no calls |
| Production / sandbox workflow mutation | not performed in this proposal task |
| Website Factory / FP-0002 / Shpigovsky | foreign WIP preserved |
| OCPilot / Smart Reporter / I-SEO Report Hub | preserved |
| `.recovery-temp/`, unrelated workspaces | preserved |
| PC-07 / PC-14 / FU-01 statuses | preserved |

---

## 13. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Live n8n drift since production after-apply export `2026-07-13` | Assume FU-01 production state until next Stage-3 export |
| Exact n8n UI connection editor behavior for insert | Confirm in sandbox implementation |
| Whether single-mode must be patched in the same sandbox commit | Prefer yes if low-cost; not a gate for Strategy A design |
| Optimal synonym choice where task examples diverge from v15 (`профильные` vs `инструменты для измерений`) | Resolve in sandbox harness review |
| Whether `answer_goal` appears in live Format output | Present in schema/prompts; Format currently prints FAQ questions — still allowlist |

---

## 14. Final Status

| Label | Value |
|-------|-------|
| **Backlog item** | `PC14_FU02_TZ_STRICT_RESIDUAL_CLEANUP_AUDIT` |
| **Proposal** | `PC14_FU02_SANDBOX_PATCH_PROPOSAL` |
| **Decision** | `PC14_FU02_READY_FOR_SANDBOX_IMPLEMENTATION` |
| **Recommended next step** | `PC14_FU02_SANDBOX_PATCH_IMPLEMENTATION` |
| **Graph strategy** | **Strategy A** (+ companion retargets); **Strategy B** fallback |
| **Task status** | COMPLETE — PC14-FU02 sandbox patch proposal ready for commit |

Awaiting operator review.
