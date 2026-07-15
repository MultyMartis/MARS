# REPORT — MetaBOT SEO Agent PC14-FU03 Repair Loop Proposal

**Date:** 2026-07-16  
**Classification:** Proposal-only · architecture / sandbox-first design charter · documentation only  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — PC14-FU03 Repair Loop / Strict Surface Governance  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer · SEO Content Agent only  

| Label | Value |
|-------|-------|
| **Proposal** | `PC14_FU03_REPAIR_LOOP_PROPOSAL` |
| **Based on audit** | `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED` |
| **Audit commit** | `230b490a` |
| **Related smoke Task ID** | `seo20260713221847nksocr` |
| **Related Worker execution** | `3352` |
| **Decision** | `PC14_FU03_REPAIR_LOOP_PROPOSAL_READY_FOR_SANDBOX_DESIGN` |
| **Recommended next step** | `PC14_FU03_PROPOSAL_PERSIST` |
| **Final status** | `COMPLETE — PC14-FU03 repair loop proposal ready` |

**Constraints honored:** No production/sandbox patch. No n8n workflow mutation. No Telegram / OpenRouter / Sheets writes. No `/run`. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

PC14-FU03 should **not** continue as another narrow JS regex patch. Smoke `seo20260713221847nksocr` / exec `3352` proved: TZ cleanup can pass while Strategy JSON, SEO QA summary, and near-synonym text still reach Telegram. SEO QA is already LLM-based; JS is an incomplete deterministic gate.

**Recommended path: Option C** — central strict marker SOT + final multi-surface JS scan gate + **bounded LLM repair (max 1 by default)** + re-scan + **hard block** of full send if dirty. Strategy raw JSON **hidden by default**; QA/Factcheck **verdict/score always**, free-text summaries **only if clean**. Memory stores raw vs sanitized with explicit statuses; `/get` returns sanitized approved or blocked diagnostic — never polluted “approved”.

This proposal is sandbox-first and ready for persistence/review, then `PC14_FU03_SANDBOX_DESIGN`.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `230b490a` — PC14-FU03 governance audit — **PASS** |
| Checkpoint `230b490a` | Present — **PASS** |
| Staged index | Empty — **PASS** |
| Remote divergence | noted (`origin` / local diverge); **no pull / no push** |
| Foreign WIP | Preserved (Website Factory / FP-0002 / unrelated exports) — **PASS** |
| Live n8n | **Not called** this task (read-only baseline taken from committed FU03 audit + HOTFIX01 evidence) |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, FU03 audit report + exports (`pc14-fu03-*-*.json`), HOTFIX01 production apply/proposal/sandbox reports (indexed by charter), issue backlog/test matrix path availability, FU03 residual/QA-gate/node-map evidence.

---

## 3. Problem Statement

Operator question (from FU03 audit): is QA JS or LLM, and does chasing residuals with JS create an infinite loop?

| Fact | Evidence |
|------|----------|
| SEO QA is LLM | `Build SEOQA Payload` → OpenRouter `Run SEO QA` |
| JS is cleanup/scan | `TZ Strict Cleanup`, `Strict Cleanup`, `Strict Risk Scanner`, partial Format/Postcheck |
| JS coverage incomplete | Strategy + QA summary + Telegram composite unscanned |
| Residuals despite “approved” QA | Strategy `table_strategy.reason`, QA summary phrase, Text near-synonym after remap |
| Infinite JS risk | Confirmed if each residual → new regex / synonym map |

Continuing FU02-style field cleanup expansion will not close multi-surface governance.

---

## 4. Current Governance Gap

| Gap | Detail |
|-----|--------|
| Marker lists duplicated | TZ / Strict Cleanup / Risk Scanner / Format / Postcheck / QA prompt — not one SOT |
| Scan scope narrow | Primarily `content_markdown` (+ outline TZ cleanup) |
| Strategy regenerates bans | After TZ cleans outline, Strategy LLM reintroduces phrase |
| Format dumps Strategy JSON | `JSON.stringify(table_strategy)` → Telegram |
| QA summary after scanner | Not re-scanned; can echo banned phrase |
| `strict=false` skips soft gates | NL ban list ≠ `--strict`; Format/Postcheck gates inactive |
| No bounded repair on final composite | Existing Text Repair is text-path only |
| Soft STRICT banner | Still sends material; not hard abort |

Production Worker baseline (post HOTFIX01, audit): `p4mqb4VuPcemIDlC`, active, 92 nodes, TZ `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01`.

---

## 5. Proposed Architecture

Six controlled layers (see `pc14-fu03-repair-loop-proposed-architecture.json`):

1. **Central Marker SOT** — detection contract  
2. **Final Public Payload Builder** — allowlisted user surfaces + raw internal  
3. **Final Multi-Surface Scan Gate** — SoT for send decision  
4. **Bounded LLM Repair Loop** — rewrite residuals only; max 1 (default)  
5. **Strict Reject / Block** — no full dirty send  
6. **Limited JS Cleanup Freeze** — keep shipped cleanups; no new rewrite arms race  

Control flow:

- Clean first scan → format/send → `approved_clean`  
- Dirty → one repair → re-scan → clean → send → `repair_attempted_clean`  
- Still dirty → diagnostic only → `blocked_dirty`

---

## 6. Central Marker Source of Truth

Single JS data object/function reused by scan, re-scan, repair payload (and optional prompt injection).

**Required families (PC14 / FU01 / FU02):**  
`аккуратн*`, `удобств*`, `удобн*`, `позволя*`, `обеспеч*`, `контрол*`, `безопасн*`, `специализирован*`, `надежн*`, `надёжн*`

**Recommended add from smoke 3352:** `наглядн*` (cleanup synonym residual).

**Rules:**

- Hard SOT families always enforced on final public surfaces (even if `flags.strict=false`).  
- NL “не используй слова” / “запрещённые слова” → set `effective_strict_surface_gate` for gate activation clarity.  
- New families: update SOT (+ repair prompt) only — **not** multi-node regex maps.

---

## 7. User-Visible Surface Policy

Canonical public object before send:

| Field | Policy |
|-------|--------|
| `seo_tz` | Public; scanned |
| `seo_strategy_public` | **Preferred: hide raw Strategy JSON**; optional short human summary; scanned |
| `seo_text` | Public; scanned |
| `seo_qa_public` | Verdict + score always; **summary only if clean** |
| `factcheck_public` | Verdict always; **summary only if clean** |
| `metadata` | Task ID / flags headers |
| `tables_summary` | Allowlisted visible table notes |
| `telegram_parts_preview` | Composed public candidate; scanned |

Internal raw (`seo_strategy_raw`, `seoqa_raw`, …) never public Telegram / public `/get`.

**Strategy preferred option:** `HIDE_RAW_STRATEGY_JSON`  
**QA/Factcheck preferred option:** `VERDICT_SCORE_ALWAYS_SUMMARY_IF_CLEAN`  

Tradeoffs documented in `pc14-fu03-repair-loop-surface-policy.json`. No product blocker: preferred options are implementable and match smoke gaps.

---

## 8. Final Multi-Surface Scan Gate

Deterministic JS after public payload is built, **before** Telegram full send and before memory append as approved.

Scan all public surfaces (not only `content_markdown`). Residual records include: marker family, matched text, surface name, field path, snippet, severity. Verdict: clean / dirty.

This gate is the **send SoT**. Format must not invent unscanned free text after a clean verdict.

---

## 9. Bounded LLM Repair Loop

If first scan dirty:

1. Build repair payload: public payload + residuals + marker SOT + rewrite-only contract  
2. Call LLM once (default max attempts = **1**; **2** only with operator approval)  
3. Extract structured JSON; merge only repairable fields; preserve task_id, entities, table structure, metadata  
4. Re-scan with same SOT  
5. Clean → proceed; dirty → block path  

No open-ended retry. No new JS synonym maps for residuals found by repair.

---

## 10. Strict Reject / Block Policy

**Preferred:** block full content send when dirty after repair budget.

Send short diagnostic only:

`STRICT QA REJECT — output blocked before final send`  
+ Task ID + residual summary (surface / family / field / snippet)

Do **not** mark dirty output as approved in memory. Close lock still runs (PC-07 mapping untouched).

---

## 11. Memory and `/get` Contract

| Memory status | Telegram | `/get` |
|---------------|----------|--------|
| `approved_clean` | Full sanitized | Sanitized approved |
| `repair_attempted_clean` | Full sanitized (post-repair) | Sanitized approved |
| `blocked_dirty` | Diagnostic only | Diagnostic + residuals; no polluted full as approved |
| `failed` | Existing error UX | Failure / no approved content |

Store raw internal separately from sanitized approved. Public `/get` never returns raw internals (admin-only optional later).

---

## 12. Proposed Node-Level Plan

Least-risky insert: **after `Normalize Run Output`**, before / as gate around `Format Run Pipeline` → `Take First Item` → send path; approved memory append only on clean.

**Add (sandbox):**

- `Build Final Public Payload`  
- `Final Surface Strict Scan`  
- `IF Final Surface Clean`  
- Dirty: `Build Strict Repair Payload` → `Run Strict Surface Repair` → `Extract Strict Surface Repair` → `Final Surface Strict Re-Scan` → `IF Repaired Clean`  
- Dirty fail: `Format Strict Reject Message`  

**Modify lightly:**

- `Format Run Pipeline` — consume approved public payload; stop raw Strategy JSON dump  
- `Prepare Memory Row Run` — status + sanitized vs raw fields  
- Optional early flag parse — NL strict surface trigger  

**Do not touch:** PC-07 Close Lock mapping; credentials; early generation chain beyond optional flag detect; no production apply in this phase.

Detail: `pc14-fu03-repair-loop-node-plan.json`.

---

## 13. Sandbox Harness Plan

Offline/sandbox fixtures; **no** Telegram / OpenRouter / Sheets side effects in harness.

Primary fixture: smoke `seo20260713221847nksocr` residuals (Strategy, QA, Text near-synonym) with `strict=false` + NL ban list.

Required labels: `FU03-SOT-01` … `FU03-SCOPE-03` as listed in `pc14-fu03-repair-loop-harness-plan.json`.

Production proposal only after harness green + import-safe sandbox JSON + allowlisted diff + secret scan.

---

## 14. Risk Matrix

| Risk | Mitigation |
|------|------------|
| Graph complexity | Post-Normalize insert; sandbox-first; freeze early graph |
| Repair cost/time | Max 1 call; hide Strategy reduces surface |
| Repair hallucination | Strict rewrite contract + mandatory re-scan + block |
| False positives | Reuse known families; clean-case harness |
| False negatives | Freeze synonym remaps; SOT updates for known escapes |
| Blocked UX | Clear diagnostic + `/get` honesty |
| Memory schema | Additive sandbox design |
| `/get` compatibility | Preserve success/not-found; status-aware body |
| Strategy hide impact | Documented; human summary optional |
| NL over-trigger | Narrow phrases; hard SOT always on final gate |

Full table: `pc14-fu03-repair-loop-risk-matrix.json`.

---

## 15. Decision Options

| Option | Description | Verdict |
|--------|-------------|---------|
| **A** | JS-only broad cleanup expansion | **Not recommended** — confirmed infinite-loop risk |
| **B** | Final multi-surface JS scan, no repair | Safer than today; may over-block (Strategy/QA residuals frequent) |
| **C** | Multi-surface scan + bounded LLM repair | **Recommended** — matches audit recommendation |
| **D** | Hide diagnostics; scan only SEO Text | Simpler; loses transparency; still fragile for Strategy path |

---

## 16. Recommended Path

**Option C**, with:

- Strategy debug JSON **hidden by default**  
- QA/Factcheck summaries **included only if clean** (verdict/score always)  
- Hard SOT on final public surfaces always  
- NL ban wording triggers surface-gate awareness  
- JS cleanup expansion **frozen**  
- Max repair attempts **1** (default)

No product decision is blocking preferred defaults; sandbox design can proceed after proposal persist.

---

## 17. Evidence Files Created

`projects/metabot-seo-content-agent/exports/pc14-fu03-repair-loop-proposal/2026-07-16/`

- `pc14-fu03-repair-loop-proposed-architecture.json`  
- `pc14-fu03-repair-loop-node-plan.json`  
- `pc14-fu03-repair-loop-surface-policy.json`  
- `pc14-fu03-repair-loop-memory-get-contract.json`  
- `pc14-fu03-repair-loop-harness-plan.json`  
- `pc14-fu03-repair-loop-risk-matrix.json`  
- `PC14-FU03-REPAIR-LOOP-PROPOSAL-MANIFEST.md`  

Report:

- `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-repair-loop-proposal.md`

No `local/` raw dump required for this proposal-only task.

---

## 18. Out-of-Scope Preserved

- Website Factory / FP-0002 / Shpigovsky foreign WIP untouched  
- No Intake/Admin/sandbox/production workflow mutation  
- No Telegram / OpenRouter / Sheets / `/run` / `/health` / `/locks`  
- No stage / commit / push / pull  
- No PC-07 Close Lock remapping  
- No credential changes  

---

## 19. SAFE UNKNOWN

- Exact Google Sheets column names for `memory_status` / raw vs sanitized (to be fixed in sandbox design)  
- Whether Intake must propagate NL-detected gate into Worker flags or Worker detects locally only  
- Preferred human-readable Strategy summary schema (bullets vs titles-only) if operators want more than hide  
- Whether second repair attempt (max=2) will ever be operator-approved for latency-sensitive runs  
- Live Worker drift since audit `updatedAt` `2026-07-13T21:49:02.829Z` — not re-fetched this task; sandbox design should re-export baseline  

---

## 20. Final Status

| Field | Value |
|-------|-------|
| **Proposal** | `PC14_FU03_REPAIR_LOOP_PROPOSAL` |
| **Based on audit** | `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED` |
| **Related smoke Task ID** | `seo20260713221847nksocr` |
| **Related Worker execution** | `3352` |
| **Decision** | `PC14_FU03_REPAIR_LOOP_PROPOSAL_READY_FOR_SANDBOX_DESIGN` |
| **Recommended next step** | `PC14_FU03_PROPOSAL_PERSIST` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` (workflow/execution/task IDs and operational labels only; no API keys, tokens, Bearer, spreadsheet live IDs, or webhook secrets in generated evidence) |
| **Final status** | `COMPLETE — PC14-FU03 repair loop proposal ready` |

No stage. No commit.

Awaiting operator review.
