# REPORT — MetaBOT SEO Agent v14 PC-14 Strict Cleanup / Strict Risk Enforcement Audit

**Task:** PC-14 — Strict Cleanup / Strict Risk Enforcement Read-Only Audit  
**Classification:** READ-ONLY audit · documentation only  
**Date:** 2026-07-10  
**Lane:** MetaBOT SEO Content Agent (`@seo_content_agent_bot`) — Intake / Worker / Admin  
**Checkpoint anchors:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`, `c1915bc8`, `6704b174`, `6efd6afa`, `e3dc9ef7`, `e36ce56e`, `7e1c50ca`, `335b7f3c`  
**PC-07 status preserved:** `PC07_PRODUCTION_APPLIED_VERIFIED`  
**PC-01 status preserved:** `PC01_MONITOR_NO_PATCH`

---

## 1. Executive Summary

PC-14 read-only audit explains why PC-07 smoke task `seo20260710103247agk8ki` delivered full `/run` output with SEO QA `reject` while strict markers `аккуратное`, `удобства`, and `позволяет` remained in the text block.

**Root cause (evidence-backed):** The run pipeline is designed as **detect-and-reject, not detect-and-repair-before-send**. Deterministic scanners and SEO QA correctly flag markers, but **no node after `Strict Cleanup` mutates `generated_text.content_markdown`**, and `Format Run Pipeline` always embeds the full markdown in section `=== 2. SEO Текст ===` regardless of `seoqa.verdict`.

**Secondary cause (lexicon / regex mismatch):** `Strict Cleanup` replacement map is **narrower and uses ASCII `\b` boundaries**, while `Strict Risk Scanner` uses **Unicode letter-boundary regex with fuller morphology**. Known gaps for the three smoke markers:

| Marker | Strict Cleanup removes? | Strict Risk Scanner detects? |
|--------|-------------------------|------------------------------|
| `аккуратное` | **No** — only `аккуратно` (adverb) | **Yes** — `аккуратн(ый\|ая\|ое\|…)` |
| `удобства` | **No** — not in replacement map | **Yes** — `удобств(о\|а\|у\|ом)` |
| `позволяет` | **Partial** — `\bпозволяет\b` only; `\b` unreliable for Cyrillic in JS | **Yes** — full morphology + Unicode boundaries |

**Behavior classification:** **C — Mixed (intended detection, unintended delivery of flagged text).**

**Recommendation:** `PC14_READY_FOR_PATCH_PROPOSAL` — conservative **R1** staged fix:

1. Align `Strict Cleanup` lexicon/regex with `Strict Risk Scanner` (deterministic repair).
2. Add prominent reject warning in `Format Run Pipeline` when `seoqa.verdict === 'reject'` or `strict_risk_scan.count > 0`.

**Final status:** `COMPLETE — PC-14 audit completed and next phase recommended`  
**PC-14 decision:** `PC14_READY_FOR_PATCH_PROPOSAL`

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Staged changes | Empty — **PASS** |
| Checkpoint `6263815c` | `6263815ce53a5570df864c21dd2dd713a9e4eaab` — **PASS** |
| Checkpoint `1b954990` | `1b9549900350e2e3e3e2ec26705737588132bffc` — **PASS** |
| Checkpoint `84dd9b07` | `84dd9b07c71c51dff75f293056c9846c3ade0e88` — **PASS** |
| Checkpoint `af6fc35d` | `af6fc35d65c019957c02127a518d8a748fcd6d92` — **PASS** |
| Checkpoint `61bb6019` | `61bb601944699109c5af918fb1b34319ca2f1820` — **PASS** |
| Checkpoint `58c8f0b7` | `58c8f0b7301378c0309dc005b79cf2408b43d982` — **PASS** |
| Checkpoint `bc222072` | `bc222072c69d7bf4e577fdca6100d2527343ea2d` — **PASS** |
| Checkpoint `46fc6335` | `46fc6335ef15cda26addb195b3fe49d66babaca8` — **PASS** |
| Checkpoint `c1915bc8` | `c1915bc8f0bcd0464cf655be2c4cc265ffb1a894` — **PASS** |
| Checkpoint `6704b174` | `6704b174c1e846739d001ad0e9eff8dc5bcb2d09` — **PASS** |
| Checkpoint `6efd6afa` | `6efd6afa626c48670e38bfa6c17e572ae80cfcb2` — **PASS** |
| Checkpoint `e3dc9ef7` | `e3dc9ef72f2a55c76879bcf945c09dfafd9b91d2` — **PASS** |
| Checkpoint `e36ce56e` | `e36ce56ed2343ec12d53c603d61cd84cd4fd3ebb` — **PASS** |
| Checkpoint `7e1c50ca` | `7e1c50ca047372ec865742b6f6fc676b96a399bc` — **PASS** |
| Checkpoint `335b7f3c` | `335b7f3c2d420b3a02f5aaea300b1b02946e1687` — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `n8n-project-development-rules-v1.md`, `metabot-developer/safe-workflow-patch-protocol-v1.md`, `REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md`, `REPORT-metabot-seo-agent-v14-issue-backlog-and-test-matrix.md`, `REPORT-metabot-seo-agent-v14-pc07-operator-smoke-verification.md`, `REPORT-metabot-seo-agent-v14-pc07-closeout-next-backlog-selection.md`, `known-issues.md`.

**Evidence exports read:** `exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sanitized.json`, `NODE-INVENTORY-v14.md`, `PROMPT-AND-CODE-NODE-INDEX-v14.md`, `RISK-AND-UNKNOWN-REGISTER-v14.md`, `exports/production-pc07/2026-07-10/pc07-operator-smoke-verify-summary.json`.

**Live API / Telegram / OpenRouter / Sheets:** not called (read-only audit).

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Area | Status |
|------|--------|
| Smart Reporter, I-SEO Report Hub, Website Factory, WordPress report hub | not touched |
| FP-0002, OCPilot workspaces | foreign WIP (`M` / `??`) preserved |
| `.recovery-temp/`, unrelated `workspaces/fp-0002-*` | preserved |
| Live n8n mutation, sandbox create/delete | not performed |
| PC-07 reopen | not requested — remains `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-01 | `PC01_MONITOR_NO_PATCH` preserved |
| Git stage / commit / push | not performed |

---

## 4. Trigger Evidence

| Field | Value | Source |
|-------|-------|--------|
| Task ID | `seo20260710103247agk8ki` | PC-07 smoke report; `pc07-operator-smoke-verify-summary.json` |
| Command | `/run тестовая проверка PC-07: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин` | PC-07 operator smoke report |
| `--strict` flag | **Not present** in command | PC-07 smoke input |
| Worker execution | `3340` (success) | PC-07 verification |
| Intake execution | `3339` (success) | PC-07 verification |
| Telegram outcome | `✅ Задача завершена` — 3 parts | Operator-reported |
| SEO QA verdict | `reject` (strict risk markers) | Operator-reported; PC-07 closeout |
| Factcheck verdict | `approved` | Operator-reported |
| Surviving markers | `аккуратное`, `удобства`, `позволяет` | PC-07 closeout selection rationale |
| Memory row | `status=ok`, `mode=run`, `output_length=9506` | `pc07-operator-smoke-verify-summary.json` |

**Note:** Per-node execution payloads for execution `3340` (text snapshots at each pipeline stage) are **not** in committed repo evidence. Marker **section** placement in the 3-part Telegram output is **SAFE UNKNOWN** without operator-redacted execution replay.

---

## 5. Strict Marker Sources

### 5.1 Source inventory

| Source | Type | Pipeline role | `аккуратное` | `удобства` | `позволяет` | Morphology |
|--------|------|---------------|--------------|------------|-------------|------------|
| **Strict Cleanup** (code) | Deterministic replace | Mutates text post–Text Repair | Detect only `аккуратно` | **Not listed** | Listed (`\bпозволяет\b` + phrases) | Partial; `\b` boundaries |
| **Strict Risk Scanner** (code) | Deterministic scan | Scores/flags; no text mutation | **Yes** `аккуратн(ый\|ая\|ое\|…)` | **Yes** `удобств(о\|а\|у\|ом)` | **Yes** `позволя(ет\|ют\|…\|ть)` | Full; Unicode `(^[^\p{L}])…` |
| **Postcheck Strict Claims** (code) | Deterministic scan | Forces `seoqa.reject` when `strict=true` | **Yes** (limited set) | **No** | **No** | Partial; gated by `strict` |
| **Normalize Run Output** (code) | Scan + metadata | Final strict gate when `strict=true` | Scanner labels include | Scanner labels include | Scanner labels include | Same as Format Run gate |
| **Format Run Pipeline** (code) | Formatter + optional gate | Builds Telegram output; embeds full text | Scanner labels include | Scanner labels include | Scanner labels include | Final gate only if `strict=true` |
| **Build SEOQA Payload** (prompt) | LLM system prompt | Instructs SEO QA verdict caps | `аккуратно` in forbidden list | **Not explicit** | **Yes** in forbidden list | Prompt list, not regex |
| **Build Text Repair Payload** (prompt) | LLM system prompt | Repair pass before Strict Cleanup | **SAFE UNKNOWN** in strict block | Guidance for `удобство` neutralization | **SAFE UNKNOWN** in strict block | Conditional on `strict=true` |
| **Build Text Payload** (prompt) | LLM generation | Initial text | Avoidance when `strict=true` | **SAFE UNKNOWN** | Avoidance when `strict=true` | Conditional on `strict` |
| **Build Factcheck Payload** (prompt) | LLM factcheck | Late QA | **No** | **No** | Example phrase in prompt | N/A |
| **Final Text Cleanup** (code) | Deterministic replace | Pre–Text Repair | **No** | **No** | **No** | Limited set (`помогает`, etc.) |
| **Compute Content Score** (code) | Deterministic score | Feeds SEO QA | Indirect via `strict_risk_scan` | Indirect | Indirect | N/A |
| **known-issues.md** | Doc | Text Repair regression | Referenced generically | Referenced generically | Referenced generically | N/A |
| **IB-10** | Backlog | Text Repair strict regression | Maps to issue | Maps to issue | Maps to issue | TQ-05 |
| **IB-11** | Backlog | Central strict policy drift | Distributed lexicons | Distributed lexicons | Distributed lexicons | TQ-11, TQ-12 |
| **B05** (vNext) | Plan item | Text Repair strict regression | Same as IB-10 | Same as IB-10 | Same as IB-10 | P1 |
| **TQ-05** | Test | Post-repair cleanup | Must not reintroduce | Must not reintroduce | Must not reintroduce | P0 |
| **TQ-10** | Test | Postcheck after factcheck | Postcheck subset only | **Not in Postcheck lexicon** | **Not in Postcheck lexicon** | P1 |
| **Architecture review O4** | Report | Text Repair reintroduction | Documented risk | Documented risk | Documented risk | §11.4, §13 |

### 5.2 Key design facts

1. **`Strict Risk Scanner` always runs on `/run` path** (`applied: true`, version `v13-run-strict-risk-scanner-hard-v4`) — **not gated** by `--strict`.
2. **`Build SEOQA Payload` always caps verdict when `strict_risk_scan.count > 0`** — applies even without `--strict`.
3. **`Postcheck Strict Claims` marker scan runs only when `strict=true`** — on PC-07 smoke (no `--strict`), postcheck regex scan was **inactive**; reject came from SEO QA + `strict_risk_scan`.
4. **`Format Run Pipeline` FINAL STRICT GATE runs only when `strict=true`** — PC-07 smoke did not get formatter-level re-scan/downgrade from this gate; SEO QA reject still occurred via LLM + scanner feed.

---

## 6. Marker Origin Analysis

**Evidence limit:** No committed per-node text diff for execution `3340`. Analysis below is **inference from pipeline order + lexicon diff**, not line-level proof of first introduction.

### 6.1 Pipeline order (text-mutating vs scan-only)

```
Run Text (LLM) → Auto Fix → Auto Polish (LLM) → FAQ → Commercial
  → Final Text Cleanup (code) → Hard Final Cleanup (code)
  → Text Repair (LLM) → Extract Text Repair
  → Strict Cleanup (code) ★ last deterministic text mutation
  → Table Sanity Check → Strict Risk Scanner (scan)
  → Content Score → SEO QA (LLM) → Factcheck (LLM)
  → Postcheck Strict Claims (scan/verdict only)
  → Normalize Run Output → Format Run Pipeline → Telegram
```

### 6.2 Per-marker analysis

| Marker | Likely first introduction | Survived Strict Cleanup? | Cleanup had chance? | Notes |
|--------|---------------------------|--------------------------|---------------------|-------|
| **`аккуратное`** | LLM draft (`Run Text`) or `Text Repair` | **Yes** (inferred — scanner fired post-cleanup) | **Yes**, but map lacks adjective/neuter forms | Cleanup only replaces `аккуратно` |
| **`удобства`** | LLM draft or `Text Repair` / table-FAQ phrasing | **Yes** | **Yes**, but **no replacement rule** | Scanner matches genitive via `(о\|а\|у\|ом)` |
| **`позволяет`** | LLM draft or `Text Repair` | **Yes** | **Yes**, but `\bпозволяет\b` may fail on Cyrillic | Scanner uses Unicode boundaries; cleanup uses `\b` |

### 6.3 Likely section in delivered output

| Marker | Expected section | Confidence |
|--------|------------------|------------|
| All three | `=== 2. SEO Текст ===` body (`generated.content_markdown`) | **High** — formatter always includes full markdown |
| QA mention | `=== 3. SEO QA ===` problems/fixes may cite markers | **Medium** — depends on LLM SEO QA JSON |
| Not primary | Outline / Strategy / Factcheck sections | **High** — markers are text-body lexicon |

### 6.4 Was marker present before final cleanup?

**SAFE UNKNOWN** at per-node granularity. **Logical inference:** `Strict Risk Scanner` runs immediately after `Strict Cleanup` on the same `content_markdown`; non-zero `strict_risk_scan.count` implies markers were **already present after Strict Cleanup** on the smoke run.

---

## 7. Current Pipeline Behavior

### 7.1 Node behavior summary (run path)

| Stage | Node | Modifies text? | Detects markers? | Blocks Telegram? | Downgrades QA? | Operates on |
|-------|------|----------------|------------------|------------------|----------------|-------------|
| Generation | Run Text / Auto Polish / Text Repair | **Yes** (LLM) | Prompt avoidance only | No | No | `generated_text` |
| Pre-repair cleanup | Final Text Cleanup | **Yes** | Partial | No | No | `content_markdown` |
| Post-repair cleanup | **Strict Cleanup** | **Yes** | Implicit via replace | No | No | `content_markdown` |
| Scan | **Strict Risk Scanner** | No | **Yes** (always) | No | Feeds SEO QA | `content_markdown` |
| QA | Build SEOQA → Run SEO QA | No | Via prompt + scan input | No | **Yes** (`reject`) | JSON verdict |
| Late scan | Postcheck Strict Claims | No | If `strict=true` | No | Can force reject | `content_markdown` |
| Normalize | Normalize Run Output | No* | If `strict=true` | No | Can force reject | metadata |
| Deliver | **Format Run Pipeline** | No** | If `strict=true` | **No** | Can adjust verdict display | builds `telegram_text` |
| Send | Send Telegram Run | No | No | No | No | chunks |

\*Normalize may attach strict metadata; does not rewrite markdown in evidenced code.  
\*\*Formatter appends full `content_markdown` unchanged.

### 7.2 Delivery rule (critical)

`Format Run Pipeline` **always** executes:

```text
text += `${generated.content_markdown || '-'}\n\n`;
```

before the SEO QA section, **regardless of `seoqa.verdict`**. There is **no branch** that omits or redacts text on `reject`.

### 7.3 Lock / memory behavior on reject

PC-07 smoke confirms: lock closed `status=done`, memory appended `status=ok` with full output — **reject does not fail the job or block memory append**.

---

## 8. Intended vs Unintended Behavior Classification

**Classification: C — Mixed**

| Aspect | Intended? | Evidence |
|--------|-----------|----------|
| Strict Risk Scanner flags markers on `/run` | **Yes** | Always-on scanner; `strict_risk_scan.verdict = reject` when count > 0 |
| SEO QA `reject` when `strict_risk_scan.count > 0` | **Yes** | `Build SEOQA Payload` system rules |
| Strict Cleanup as last text mutation | **Yes** | Node order in v14 export |
| Markers surviving cleanup due to lexicon/regex gaps | **Unintended** | Cleanup map ⊂ scanner map; `\b` vs Unicode boundaries |
| Full rejected text still delivered to Telegram | **Ambiguous / de facto intended** | No delivery gate in formatter; job completes `✅ Задача завершена` |
| No automatic repair retry after QA reject | **De facto intended** | No retry node exists |

**Not A (pure advisory):** QA `reject` is real and tied to deterministic scanner input.  
**Not B (pure bug):** Detection and verdict downgrade work; missing repair/delivery gate.  
**Best fit: C** — detection works; **no enforcement gate before send**.

---

## 9. Evidence Matrix

| Node | Type | Pipeline stage | Reads | Writes | Mutates final text? | Detects strict markers? | Blocks output? | Evidence source | Risk notes |
|------|------|----------------|-------|--------|---------------------|---------------------------|----------------|-----------------|------------|
| Build Text Payload | code/prompt | Text generation | brief, outline, flags | `openrouter_payload` | Indirect (LLM) | Prompt only if `strict` | No | Worker sanitized JSON | LLM may introduce markers |
| Auto Polish Text | code/prompt | Post-text polish | `generated_text` | `openrouter_payload` | Indirect (LLM) | No | No | PROMPT-AND-CODE-NODE-INDEX | IB-14 |
| Final Text Cleanup | code | Pre-repair | `content_markdown` | `generated_text` | **Yes** | Partial replace | No | Worker JSON | No аккуратн/удобств/позволяет |
| Build Text Repair Payload | code/prompt | Repair | `generated_text`, `strict` | `openrouter_payload` | Indirect (LLM) | Prompt if `strict` | No | Worker JSON | IB-10 / TQ-05 |
| Extract Text Repair | code | Post-repair | LLM response | `generated_text` | **Yes** | No | No | Worker JSON | — |
| **Strict Cleanup** | code | Post-repair | `content_markdown` | `generated_text`, `strict_cleanup` | **Yes** | Implicit | No | Worker JSON | **Lexicon gap / `\b`** |
| Table Sanity Check | code | Pre-score | tables in markdown | `table_sanity_check` | No | No | No | Worker JSON | — |
| **Strict Risk Scanner** | code | Pre-score | `content_markdown` | `strict_risk_scan` | No | **Yes** (always) | No | Worker JSON | Does not repair |
| Compute Content Score | code | Pre–SEO QA | text, scan results | `content_score` | No | Indirect | No | Worker JSON | — |
| Build SEOQA Payload | code/prompt | SEO QA | scan, text, outline | `openrouter_payload` | No | Via rules | No | Worker JSON | Forces reject cap |
| Run Extract SEO QA | code | SEO QA | LLM JSON | `seoqa` | No | Via LLM | No | Worker JSON | — |
| Build Factcheck Payload | code/prompt | Factcheck | text, brief | `openrouter_payload` | No | Prompt examples | No | Worker JSON | — |
| **Postcheck Strict Claims** | code | Post-factcheck | `content_markdown`, `strict` | `seoqa`, `factcheck` | No | If `strict` | No | Worker JSON | Subset lexicon; TQ-10 |
| Normalize Run Output | code | Pre-format | full item | metadata, optional gate | No | If `strict` | No | Worker JSON | Gate only |
| **Format Run Pipeline** | code | Final format | all artifacts | `telegram_text`, chunks | No | If `strict` (gate) | **No** | Worker JSON | **Ships full text on reject** |
| Close Lock Before Sending | sheets | Pre-send | lock context | `seo_active_jobs` | No | No | No | PC-07 evidence | Out of PC-14 scope |
| Send Telegram Run | telegram | Delivery | `telegram_text` | — | No | No | No | Worker JSON | Chunks to user |
| Prepare Memory Row Run | code | Post-format | `full_output_text` | memory row | No | No | No | PC-07 smoke | Stores rejected text |

---

## 10. Fix Options

### Option 1 — Read-only monitor / no patch

| Field | Value |
|-------|-------|
| **Risk** | R0 |
| **Description** | Keep detect + reject + deliver full text |
| **Changed nodes** | None |
| **Expected effect** | Status quo; operators must read SEO QA block |
| **Side effects** | Compliance risk remains |
| **Test plan** | Repeat PC-07 smoke; confirm reject + markers |
| **Rollback** | N/A |
| **Decision** | **Deferred** — does not address quality signal |

### Option 2 — Post-QA warning only (recommended stage 2)

| Field | Value |
|-------|-------|
| **Risk** | R1 |
| **Description** | In `Format Run Pipeline`, prepend banner when `seoqa.verdict === 'reject'` or `strict_risk_scan.count > 0` |
| **Changed nodes** | `Format Run Pipeline` |
| **Expected effect** | Operator sees explicit reject warning above text |
| **Side effects** | Text still contains markers; longer messages |
| **Test plan** | Sandbox `/run` with known markers; verify banner + 3-part split |
| **Rollback** | Revert formatter node |
| **Decision** | **Selected (stage 2)** — low risk, immediate UX improvement |

### Option 3 — Final cleanup retry before delivery

| Field | Value |
|-------|-------|
| **Risk** | R2 |
| **Description** | If `strict_risk_scan.count > 0`, run second deterministic cleanup or LLM repair before format |
| **Changed nodes** | New code node before `Format Run Pipeline` or extend `Normalize Run Output` |
| **Expected effect** | Fewer markers in delivered text |
| **Side effects** | Latency; possible grammar regression; LLM non-determinism if used |
| **Test plan** | TQ-05 + new retry-specific cases |
| **Rollback** | Disable node / restore JSON |
| **Decision** | **Deferred** — higher risk; try deterministic alignment first |

### Option 4 — Hard block delivery on strict violation

| Field | Value |
|-------|-------|
| **Risk** | R2 |
| **Description** | Omit `=== 2. SEO Текст ===` body when `reject` |
| **Changed nodes** | `Format Run Pipeline` |
| **Expected effect** | Markers not delivered |
| **Side effects** | Operators lose text/TZ bundle; `/get` memory still has full output unless also gated |
| **Test plan** | Reject case must show QA summary only; memory behavior test |
| **Rollback** | Revert formatter |
| **Decision** | **Deferred** — mixed operator value; memory inconsistency |

### Option 5 — Deterministic replacement map alignment (recommended stage 1)

| Field | Value |
|-------|-------|
| **Risk** | R1 (R2 if broad regex changes) |
| **Description** | Sync `Strict Cleanup` patterns with `Strict Risk Scanner`: add `аккуратн*` adjective forms, `удобств*`, `позволя*` morphology; replace `\b` with Unicode letter boundaries |
| **Changed nodes** | `Strict Cleanup` (primary); optionally `Final Text Cleanup` for earlier pass |
| **Expected effect** | Markers removed before scanner; `strict_risk_scan.count` → 0 for these cases |
| **Side effects** | Possible awkward neutral phrases; needs copy review |
| **Test plan** | TQ-05, TQ-01, PC-14 sandbox matrix §11 |
| **Rollback** | Restore prior `Strict Cleanup` jsCode from export |
| **Decision** | **Selected (stage 1)** — minimal, deterministic, addresses root lexicon gap |

### Option 6 — Prompt-only strengthening

| Field | Value |
|-------|-------|
| **Risk** | R1–R2 |
| **Description** | Expand forbidden lists in Text Repair / Text Payload prompts |
| **Changed nodes** | `Build Text Repair Payload`, `Build Text Payload` |
| **Expected effect** | Fewer markers at generation |
| **Side effects** | Non-deterministic; IB-11 drift continues |
| **Test plan** | TQ-05, TQ-11 |
| **Rollback** | Revert prompts |
| **Decision** | **Deferred** — supplement to Option 5, not standalone fix |

### Option 7 — Central strict lexicon module (IB-11 / B06)

| Field | Value |
|-------|-------|
| **Risk** | R2+ (multi-node) |
| **Description** | Single shared lexicon for cleanup + scanners + formatter |
| **Changed nodes** | Multiple — future wave |
| **Decision** | **Deferred** — after Option 5 proves insufficient |

---

## 11. Sandbox Test Plan

**Prerequisite:** Sandbox Worker clone (e.g. extend `Worker.sandbox-pc07` or new `Worker.sandbox-pc14`); inactive until operator charter. **Live n8n API:** required for sandbox patch wave only.

| Test ID | Input / command | Expected strict scan count | Expected QA verdict | Expected delivery | Memory | Lock | Pass criteria |
|---------|-----------------|----------------------------|---------------------|-------------------|--------|------|---------------|
| **PC14-T01** | `/run` brief seeded to produce «аккуратное обслуживание» | ≥1 (`аккуратный`) | `reject` (pre-patch) → `approved` or `approved_with_warnings` (post Option 5) | Pre-patch: text contains marker + QA reject; post-patch: marker absent or banner (Option 2) | `ok` row | `done` | Scan count matches grep |
| **PC14-T02** | `/run` brief with «для удобства клиентов» / «удобства» | ≥1 (`удобство`) | `reject` pre-patch | Same pattern | `ok` | `done` | `удобств` not in final text post Option 5 |
| **PC14-T03** | `/run` brief with «позволяет оценить состояние» | ≥1 (`позволяет`) | `reject` pre-patch | Marker neutralized post Option 5 | `ok` | `done` | No `позволя` in text |
| **PC14-T04** | Clean brief (neutral service copy) | 0 | `approved` or `approved_with_warnings` | Unchanged quality; no false positives | `ok` | `done` | No regression on clean copy |
| **PC14-T05** | Force `seoqa.reject` with clean strict scan (mock / edge brief) | 0 | `reject` | With Option 2: **banner present**; with Option 4: text body omitted | `ok` | `done` | Delivery matches selected option |
| **PC14-T06** | Post–Option 5: inject markers only in Text Repair output | 0 after Strict Cleanup | Not `reject` due to scan | No banned lexicon in Telegram | `ok` | `done` | TQ-05 parity |
| **PC14-T07** | `/run --strict` same as PC14-T01 | ≥1 pre-patch | `reject` | Postcheck + formatter gates active | `ok` | `done` | Stricter than non-strict path (TQ-12) |
| **PC14-T08** | Repeat PC-07 smoke brief | Document before/after | Compare to `seo20260710103247agk8ki` baseline | Regression guard | `ok` | `done` | No lock regression (PC-07 guard) |

**Fail criteria:** markers in delivered text with `reject` and no warning (post Option 2); `strict_risk_scan.count > 0` after Strict Cleanup (post Option 5); lock not `done`; memory missing row.

---

## 12. Recommendation

| Field | Value |
|-------|-------|
| **PC-14 decision** | **`PC14_READY_FOR_PATCH_PROPOSAL`** |
| **Selected approach** | **Staged R1:** Option 5 (Strict Cleanup alignment) → Option 2 (reject banner in formatter) |
| **Why** | Addresses evidenced lexicon/regex gap without blocking `/run` bundle delivery; improves operator visibility on reject |
| **Risk level** | R1 per stage |
| **Nodes likely involved** | `Strict Cleanup` (stage 1); `Format Run Pipeline` (stage 2) |
| **Forbidden nodes (stage 1–2)** | Intake, Admin, all lock nodes, OpenRouter HTTP nodes, `Route Command`, PC-07 `Close Lock Before Sending` |
| **Sandbox-first plan** | PC14-T01–T08 on inactive sandbox Worker; operator smoke only after sandbox pass |
| **Acceptance criteria** | PC14-T01–T04 pass; PC-07 lock/memory guards (PC14-T08); no new orphan locks |
| **Rollback criteria** | Any PC14-T08 lock regression; clean-copy false positive rate unacceptable; revert nodes from pre-patch export |
| **Live n8n API next task?** | **Yes** — sandbox clone export/import only, per `safe-workflow-patch-protocol-v1.md` |

**Not recommended now:** Option 4 hard block (operator workflow impact); Option 3 LLM retry (R2); Option 1 monitor-only (leaves compliance gap).

---

## 13. Proposed Next Prompt Outline

```markdown
# TASK — MetaBOT SEO Agent PC-14 Sandbox Patch Proposal (Strict Cleanup Alignment + Reject Banner)

Lane: MetaBOT SEO Content Agent only.
Goal: Propose sandbox patches for Strict Cleanup lexicon alignment (Option 5) and Format Run Pipeline reject banner (Option 2).

Constraints:
- Sandbox-first. No production patch without operator approval.
- Follow safe-workflow-patch-protocol-v1.md.
- Do not touch PC-07 lock nodes or Intake/Admin.
- No commit unless requested.

Read:
- REPORT-metabot-seo-agent-v14-pc14-strict-cleanup-enforcement-audit.md
- exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sanitized.json
- safe-workflow-patch-protocol-v1.md

Deliver:
- REPORT-metabot-seo-agent-v14-pc14-sandbox-patch-proposal.md
- Optional: sandbox node diff JSON under exports/sandbox-pc14/

Must include:
- Exact jsCode diff for Strict Cleanup (Unicode boundaries + morphology parity with Strict Risk Scanner)
- Exact jsCode diff for Format Run Pipeline banner
- Risk R1 assessment, rollback steps, PC14-T01–T08 mapping
- Production promotion gate separate from sandbox apply

Final status: PC14_SANDBOX_PATCH_PROPOSED | BLOCKED
```

---

## 14. Files Created

| Path | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-strict-cleanup-enforcement-audit.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 15. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** includes checkpoint chain through `335b7f3c` (verified)
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** preserved — Website Factory, OCPilot, fp-0002 workspaces, `.recovery-temp/`, etc. — **OUT_OF_SCOPE_PRESERVED**
- **Commit / push:** not performed

---

## 16. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Exact Telegram part/line for each marker in PC-07 smoke | **SAFE UNKNOWN** — no committed execution `3340` node text dumps |
| Whether markers appeared before or because of Text Repair on this run | **SAFE UNKNOWN** — no pre/post repair diff in repo |
| Whether `Strict Cleanup.applied === true` on execution `3340` | **SAFE UNKNOWN** — node output not in committed evidence |
| Post-close `seo_active_jobs` row reread via Sheets API | **SAFE UNKNOWN** — not required for PC-14 |
| Operator policy: should `/run` without `--strict` ever hard-block text on QA reject? | **Operator clarification** needed before Option 4 |
| Full parity of strict lexicon across single vs run branches | **Partial** — IB-11; out of minimal fix scope |

---

## 17. Final Status

**`COMPLETE — PC-14 audit completed and next phase recommended`**

| Label | Value |
|-------|-------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` (unchanged) |
| PC-01 | `PC01_MONITOR_NO_PATCH` (unchanged) |
| PC-14 audit | Complete |
| PC-14 decision | **`PC14_READY_FOR_PATCH_PROPOSAL`** |

Awaiting operator review.
