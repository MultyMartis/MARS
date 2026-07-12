# REPORT — MetaBOT SEO Agent v14 PC14-FU-02 TZ Strict Residual Cleanup Audit / Proposal

**Date:** 2026-07-13  
**Classification:** READ-ONLY audit / proposal · documentation only  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Worker SEO ТЗ / outline-side residuals  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Backlog item:** `PC14_FU02_TZ_STRICT_RESIDUAL_CLEANUP_AUDIT`  
**Checkpoint commits verified through:** `f6fb295a` (PC14-FU-01 closeout + next backlog selection)

**Constraints honored:** No live n8n mutation. No Telegram / OpenRouter / Sheets calls. No workflow patch. No sandbox create. No push. Foreign WIP preserved.

---

## 1. Executive Summary

PC14-FU-01 left final SEO Text clean for PC-14 R1 and FU-01 families, but operator smoke Task ID `seo20260712201612oo0m85` still showed one strict residual in **SEO ТЗ / table reason**: phrase `для удобства восприятия`.

**Root cause (evidence-backed):** the phrase is **LLM-generated** into `outline.tables.decision_reason` during outline generation, then **passively rendered** by `Format Run Pipeline` into section `=== 1. SEO ТЗ ===`. It is **not hardcoded**. It is **outside** `Strict Cleanup` and `Strict Risk Scanner` scope, which mutate/scan only `generated_text.content_markdown`. Therefore `strict_risk_scan.count=0` and SEO QA `approved/100` are consistent with final-text cleanliness, while Telegram still shows a user-facing TZ residual.

**Recommended path:** **Option B / FU-02A** — dedicated TZ/outline-side sanitizer using the same v15 strict family map, applied to outline fields (especially `tables.decision_reason`) **without** changing Strict Cleanup v15 final-text behavior.

**Decision:** `PC14_FU02_READY_FOR_SANDBOX_PATCH_PROPOSAL`  
**Recommended next step:** `PC14_FU02_SANDBOX_PATCH_PROPOSAL`

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Staged changes (pre-task) | Empty — **PASS** |
| HEAD | `f6fb295a` — PC14-FU-01 closeout — **PASS** |
| Checkpoint `f6fb295a` | ancestor of HEAD — **PASS** |
| Checkpoints through FU-01 closeout | Present — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead **16** / behind **17** — **noted**; no pull / no push |
| Live API calls this session | None — **PASS** |
| Foreign WIP | Preserved — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, FU-01 closeout / operator smoke / production apply / production proposal / sandbox implementation, PC-14 strict cleanup audit, PC-14 closeout, issue backlog and test matrix.

**Evidence exports read:** `pc14-fu01-operator-smoke-*.json`, `pc14-fu01-production-harness-results.json`, `pc14-fu01-production-diff-scope-summary.json`, production Worker after-apply sanitized JSON, live-v14 `PROMPT-AND-CODE-NODE-INDEX-v14.md`, `NODE-INVENTORY-v14.md`.

---

## 3. Source Evidence Reviewed

| Source | Role |
|--------|------|
| `REPORT-metabot-seo-agent-v14-pc14-fu01-closeout-next-backlog-selection.md` | Selected FU-02; residual note |
| `REPORT-metabot-seo-agent-v14-pc14-fu01-operator-smoke-verification.md` | Live smoke residual classification |
| `pc14-fu01-operator-smoke-output-scan.json` | Area marker scan + TZ snippet |
| `pc14-fu01-operator-smoke-verify-summary.json` | Execution / QA / PC-07 guards |
| `SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu01.after-apply.sanitized.json` | Node code truth for outline / Strict Cleanup / Format |
| `PROMPT-AND-CODE-NODE-INDEX-v14.md` / `NODE-INVENTORY-v14.md` | Node inventory |
| PC-14 / FU-01 reports | Strict Cleanup scope = final text only |

**Smoke task under analysis:** `seo20260712201612oo0m85` (Intake `3343`, Worker `3344`).

---

## 4. Residual Summary

### 4.1 Known residual (expected finding confirmed)

| Field | Value |
|-------|-------|
| Exact phrase (safe quote) | `для удобства восприятия` |
| Snippet (redacted evidence) | `…в табличном формате для удобства восприятия. Идеи таблиц: 1. Методы и параметры диагностики` |
| Location | SEO ТЗ → Tables → `Причина:` (`outline.tables.decision_reason`) |
| Marker family | `удобств*` (PC-14 R1) |
| Final SEO Text hits | **0** |
| Strategy hits | **0** |
| SEO QA / Factcheck hits | **0** |
| `strict_risk_scan.count` | **0** |
| SEO QA | `approved`, score `100` |
| Factcheck | `approved` |

### 4.2 Area classification (Task `seo20260712201612oo0m85`)

| Area | Hits | Output failure? | Strict-cleanup scope gap? | Fix in FU-02? |
|------|------|-----------------|---------------------------|---------------|
| User prompt | 8 (intentional forbidden stems) | **No** — prompt contamination ignored | N/A | **No** |
| SEO ТЗ / outline | 1 — `удобств*` in table reason | **Yes** — user-facing Telegram residual | **Yes** — outline not cleaned | **Yes** |
| SEO Strategy | 0 | No | No for this smoke | Monitor |
| Final SEO Text | 0 | No | No — FU-01 succeeded | **Must not regress** |
| Tables body in final text | 0 | No | No | Guard via NR06 |
| FAQ | 0 (this smoke) | No | Possible future surface | Include in sanitizer field list |
| SEO QA block | 0 | No | Scanner scope is text-only | Do not force reject for TZ-only |
| Factcheck | 0 | No | No | Preserve |
| Stored memory / Telegram | 1 (same TZ phrase in full output) | Yes (echo of TZ) | Same gap | Fixed if TZ cleaned before Format |
| Strict risk metadata | 0 | No | Detection gap for TZ | Optional Option D later |

**Do not reopen PC14-FU-01.** Final-text path remains verified.

---

## 5. Workflow Area Analysis

### 5.1 Pipeline relevance (outline → deliver)

```
Route Command
  → Build Outline Payload (prompt; asks LLM for tables.decision_reason)
  → Run Outline (OpenRouter)
  → Run Extract Outline (parse JSON; passthrough decision_reason)
  → … strategy / text / repair …
  → Strict Cleanup          ★ mutates ONLY generated_text.content_markdown
  → Strict Risk Scanner     ★ scans ONLY content_markdown
  → SEO QA / Factcheck
  → Format Run Pipeline     ★ renders outline.tables.decision_reason into SEO ТЗ
  → Append Memory / Telegram
```

### 5.2 Per-node findings

| Node | Type | Role | Touches | Can produce phrase? | Before/after Strict Cleanup | Sandbox candidate? |
|------|------|------|---------|---------------------|-----------------------------|--------------------|
| **Route Command** | code | Parse `/run`, flags, `tables_policy` | routing | No | Before | No (unless flag plumbing) |
| **Build Outline Payload** | code + prompt | Outline LLM system prompt + JSON schema with `tables.decision_reason` | SEO ТЗ generation | **Indirect** — LLM free to invent convenience phrasing; prompt forbids some promise verbs but **not** PC-14 R1 `удобств*` | Before | **Option A** candidate |
| **Run Outline** | HTTP | LLM call | outline JSON | **Yes** — likely origin | Before | No (external) |
| **Run Extract Outline** | code | Parse/normalize outline | SEO ТЗ object | Passthrough only; error fallback uses neutral Russian | Before | Possible insert point for Option B |
| **Build SEO Strategy / text / repair** | prompt/code | Downstream copy | strategy / final text | Not source of this residual | Around Strict Cleanup | Out of FU-02 primary scope |
| **Strict Cleanup** (`v15-strict-cleanup-pc14-fu01-r1`) | code | Deterministic replace | **Final SEO Text only** | Would neutralize `для удобства…` **if** applied to string; **does not** read outline | N/A (is the node) | **Do not broaden** in FU-02 — keep final-text guard intact |
| **Strict Risk Scanner** | code | Detect markers | **Final SEO Text only** | Detects `удобств*` in text; **ignores** TZ | After Strict Cleanup | Option D only |
| **Format Run Pipeline** | code | Build Telegram/memory text | SEO ТЗ + Text + QA | **Renders** `Причина: ${tables.decision_reason}` | After | Option C candidate (less preferred) |
| **Format Single Mode Message** | code | Single-mode formatter | TZ-like | Same `decision_reason` render pattern | Separate path | Include if single `/outline` in scope |
| **Append Memory / Send Telegram** | Sheets/Telegram | Persist/send | full output | Echo only | After Format | No |

### 5.3 Hardcode check

| Check | Result |
|-------|--------|
| Literal `для удобства восприятия` in Worker JSON | **Absent** |
| Literal `для удобства` in prompts/code | **Absent** as hardcoded output string |
| `tables.decision_reason` schema field | **Present** in Build Outline Payload JSON schema |
| Formatter template | `if (tables.decision_reason) text += \`Причина: ${tables.decision_reason}\n\`` |

**Classification of phrase origin:** **prompt-generated by LLM** into structured outline field → **formatter echo**. Not a code hardcoded string. Not a heuristic inventing the exact Russian idiom (no heuristic found); heuristic only decides `tables.required` from `tables_policy`.

---

## 6. Root Cause Assessment

1. **Generation:** Outline LLM fills `tables.decision_reason` with natural Russian table-rationale prose. Smoke example uses the common idiom `для удобства восприятия`.
2. **Prompt gap:** `Build Outline Payload` bans several causal/promise stems (`обеспечит`, `помогает`, …) but does **not** ban PC-14 R1 families (`удобств*`, `аккуратн*`, `позволя*`) for TZ/outline.
3. **Scope gap:** `Strict Cleanup` v15 applies PC-14/FU-01 maps only to `generated_text.content_markdown`. Outline fields are never passed through `cleanText()`.
4. **Detection gap:** `Strict Risk Scanner` likewise reads only final markdown → `count=0` despite TZ residual.
5. **Delivery:** `Format Run Pipeline` always prints SEO ТЗ including `Причина`, so residual is **user-facing** in Telegram and memory.
6. **QA non-flag:** SEO QA approved because final text + text-scoped risk scan are clean; TZ residual is not treated as reject input.

**Therefore:** this is a **strict-cleanup / risk-scan scope gap for outline-side fields**, not a FU-01 regression and not a final-text failure.

**Similar residuals may appear** in TZ/outline for other families (`аккуратн*`, `удобн*`, `позволя*`, `обеспеч*`, `контрол*`, `безопасн*`, `специализирован*`, `надежн*`/`надёжн*`) even when final text is clean — FU-02 should cover the **family map**, not only the one smoke phrase.

---

## 7. Remediation Options

### Option A — Prompt-level instruction

Adjust `Build Outline Payload` (and possibly single-mode outline prompt) to forbid PC-14/FU-01 families in `decision_reason`, section summaries, FAQ goals, CTA.

| | |
|--|--|
| **Pros** | Low structural risk; no new node; addresses generation |
| **Cons** | Non-deterministic; LLM may still emit residuals |
| **Affected nodes** | Build Outline Payload (+ Build Single Payload if needed) |
| **Production risk** | Low–medium (prompt drift / outline quality) |
| **Tests** | TZ01–TZ07 prompts; NR07 structure |
| **Rollback** | Restore prior prompt string |

### Option B — TZ-side cleanup function (**recommended**)

After outline extract (or as a thin dedicated code node), apply v15-aligned strict family sanitizer to outline-side strings: at minimum `tables.decision_reason`; preferably also `meta_description`, section `summary`, FAQ `answer_goal`, `cta`, and string `table_ideas` fields. **Do not** alter `Strict Cleanup` final-text node.

| | |
|--|--|
| **Pros** | Deterministic; mirrors proven v15 map; isolates TZ from final text; matches default FU-02A |
| **Cons** | Needs careful field allowlist; grammar of replacements must be reviewed for short rationale strings |
| **Affected nodes** | New node **or** `Run Extract Outline` post-parse sanitize (prefer dedicated node for scope clarity) |
| **Production risk** | Medium — outline semantics change; final text path unchanged if scoped correctly |
| **Tests** | TZ01–TZ07 + NR01–NR08 + SG01–SG05 |
| **Rollback** | Disable/remove TZ sanitizer node; restore Extract Outline |

### Option C — Format Run Pipeline sanitation

Sanitize rendered TZ strings at format time before Telegram/memory.

| | |
|--|--|
| **Pros** | High visibility; catches any upstream residual at last mile |
| **Cons** | Masks generator issues; couples formatter to lexicon; higher blast radius vs PC-14 banner logic |
| **Affected nodes** | Format Run Pipeline (+ Format Single Mode Message) |
| **Production risk** | Medium–high |
| **Tests** | Same + formatter banner NR03 |
| **Rollback** | Restore Format jsCode from pre-patch export |

### Option D — Strict Risk Scanner scope expansion

Include SEO ТЗ / outline fields in risk scan (warn or feed QA).

| | |
|--|--|
| **Pros** | Detection guard; useful telemetry |
| **Cons** | Does not clean; may increase rejects/noise if QA consumes it |
| **Affected nodes** | Strict Risk Scanner (+ possibly SEO QA payload) |
| **Production risk** | Medium (false reject risk) |
| **Tests** | Detection cases; NR02/NR03 |
| **Rollback** | Restore scanner jsCode |

### Option E — Leave as documented residual

| | |
|--|--|
| **Pros** | Zero change risk |
| **Cons** | SEO ТЗ is user-facing; residual undermines strict trust after FU-01 |
| **Affected nodes** | None |
| **Production risk** | None operationally; trust/UX cost |
| **Recommendation** | **Not preferred** |

---

## 8. Recommended Path

**Selected:** **Option B — FU-02A TZ-side cleanup sanitizer**

**Implementation intent (proposal only — not applied here):**

1. Add a dedicated Worker code node (suggested name: `Strict Cleanup Outline` / `TZ Strict Sanitize`) **after** `Run Extract Outline` and **before** strategy/text branches consume outline.
2. Reuse v15 family map / Unicode-boundary helpers aligned with `Strict Cleanup` `v15-strict-cleanup-pc14-fu01-r1` (do not fork divergent lexicons).
3. Sanitize allowlisted outline string fields only; leave `generated_text` untouched.
4. Keep `Strict Cleanup`, `Strict Risk Scanner`, and `Format Run Pipeline` unchanged in the first sandbox wave (SG02–SG04).
5. Optional later: Option A prompt hardening as defense-in-depth; Option D detection if operators want TZ risk visibility without auto-reject.

**Why not A alone:** smoke already proves LLM emits residual despite existing promise bans.  
**Why not C first:** masks root field; risk to formatter/banner.  
**Why not D alone:** detection without cleanup leaves Telegram dirty.  
**Why not E:** SEO ТЗ is user-facing.

**Gate for next task:** `PC14_FU02_SANDBOX_PATCH_PROPOSAL`

---

## 9. Proposed Test Matrix

### TZ residual tests

| ID | Input / fixture | Expect |
|----|-----------------|--------|
| **TZ01** | `для удобства восприятия` in `decision_reason` | Neutralized / absent after TZ sanitize; structure kept |
| **TZ02** | `что позволяет` | Family cleaned per v15 map |
| **TZ03** | `для обеспечения безопасности` | FU-01 families cleaned |
| **TZ04** | `контроль качества` | Cleaned without empty wreckage |
| **TZ05** | `специализированные инструменты` | Cleaned |
| **TZ06** | `надежность соединений` / `надёжность…` | Both spellings cleaned |
| **TZ07** | Mixed multi-family rationale | All target families cleaned; readable Russian |

### Non-regression

| ID | Guard |
|----|-------|
| **NR01** | Final SEO Text unchanged except expected final-path cleanup (TZ sanitize must not rewrite `content_markdown`) |
| **NR02** | SEO QA approved case stays approved when final text clean |
| **NR03** | `STRICT QA REJECT` banner still appears if final strict risk remains |
| **NR04** | PC-07 `active_jobs` close mapping unchanged |
| **NR05** | `/get` behavior unaffected |
| **NR06** | Tables still render (`Required` / `Причина` / `Идеи таблиц`) |
| **NR07** | Strategy/outline structurally complete (H1, sections, FAQ keys) |
| **NR08** | Sandbox harness: no OpenRouter / Telegram / Sheets side effects |

### Scope guards

| ID | Guard |
|----|-------|
| **SG01** | Only intended TZ/outline cleanup node patched |
| **SG02** | Strict Cleanup v15 intact (hash/version string) |
| **SG03** | Format Run Pipeline unchanged unless later wave selects Option C |
| **SG04** | Strict Risk Scanner unchanged unless later wave selects Option D |
| **SG05** | Production workflow `active` preserved on future apply |

---

## 10. Production Risk Assessment

| Risk | Level | Mitigation |
|------|-------|------------|
| Accidental final-text regression | High if wrong node patched | SG01–SG02; NR01 harness |
| Outline meaning damage from aggressive replaces | Medium | Phrase-first maps; TZ01–TZ07 human review samples |
| Formatter/banner regression | Medium if Option C chosen | Prefer Option B; NR03 |
| QA false rejects if Option D wired into verdict | Medium | Keep D detection-only or deferred |
| PC-07 / `/get` collateral | Low if lock/format nodes untouched | NR04–NR05 |
| Lexicon drift vs v15 | Medium | Share helpers/version note with Strict Cleanup |

**This audit does not authorize production apply.**

---

## 11. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Area | Status |
|------|--------|
| Live n8n / Telegram / OpenRouter / Sheets | no calls |
| Production / sandbox workflow mutation | not performed |
| Website Factory / FP-0002 / Shpigovsky | foreign WIP preserved |
| OCPilot / Smart Reporter / I-SEO Report Hub | preserved |
| `.recovery-temp/`, unrelated workspaces | preserved |
| PC14-FU-01 reopen | **not** reopened |
| PC-07 / PC-14 parent statuses | preserved |

---

## 12. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Exact per-node intermediate JSON for execution `3344` beyond committed smoke scans | Not re-fetched this session; residual placement inferred from scan + formatter code |
| Whether single-mode `/outline` path needs identical sanitizer in wave 1 | Likely yes for parity — confirm in sandbox proposal |
| Whether Option A+B combo should be one wave or two | Prefer B first; A optional follow-up |
| Live n8n drift since after-apply export `2026-07-13` | Assume FU-01 production state until next Stage-3 export |
| Optimal dedicated node name / connection wire exactness | Decide in sandbox patch proposal |

---

## 13. Final Status

| Label | Value |
|-------|-------|
| **Backlog item** | `PC14_FU02_TZ_STRICT_RESIDUAL_CLEANUP_AUDIT` |
| **Decision** | `PC14_FU02_READY_FOR_SANDBOX_PATCH_PROPOSAL` |
| **Recommended next step** | `PC14_FU02_SANDBOX_PATCH_PROPOSAL` |
| **Selected implementation path** | **FU-02A / Option B** — TZ-side cleanup sanitizer for SEO ТЗ / outline fields, v15 family map, final SEO Text untouched |
| **Task status** | COMPLETE — PC14-FU-02 audit/proposal ready for commit |

Awaiting operator review.
