# REPORT — MetaBOT SEO Agent PC14-FU03 Strict Output Surface Governance Audit

**Date:** 2026-07-14  
**Classification:** READ-ONLY architecture audit / governance proposal · documentation only  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Worker QA ownership vs deterministic strict layers after PC14-FU02 HOTFIX01  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  

| Label | Value |
|-------|-------|
| **Audit** | `PC14_FU03_STRICT_OUTPUT_SURFACE_GOVERNANCE_AUDIT` |
| **Related smoke Task ID** | `seo20260713221847nksocr` |
| **Related Worker execution** | `3352` (success) |
| **Related production apply** | `PC14_FU02_HOTFIX01_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| **Decision** | `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED` |
| **Recommended next step** | `PC14_FU03_REPAIR_LOOP_PROPOSAL` |
| **Final status** | `COMPLETE — PC14-FU03 strict surface governance audit complete` |

**Constraints honored:** No production/sandbox patch. No n8n workflow mutation. No Telegram / OpenRouter / Sheets writes. No `/run`. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

SEO QA **уже LLM-based** (`Build SEOQA Payload` → OpenRouter `Run SEO QA`). JS **не заменяет** QA: это отдельные deterministic layers (`TZ Strict Cleanup`, `Strict Cleanup`, `Strict Risk Scanner`, partial gates in `Postcheck` / `Format`).

После HOTFIX01 top-level SEO ТЗ cleanup **работает** (`outline.tables.decision_reason` очищен). Но residual `для удобства восприятия` всё ещё ушёл в Telegram через **другие поверхности**: SEO Strategy `table_strategy.reason` и **SEO QA summary**, плюс near-synonym в SEO Text (`для наглядности восприятия` после JS remap).

Корень: **узкий scope** cleanup/scan (outline decision_reason + `content_markdown` only), **Strategy LLM перегенерирует** banned phrase после TZ cleanup, **Format** без фильтра сбрасывает Strategy JSON и QA summary в Telegram, **маркеры дублируются** в нескольких JS/prompt списках (не единый SOT), smoke шёл с `strict=false` (Format final gate/`Postcheck` force-reject отключены).

Риск бесконечного JS-фиксов **реален**, если отвечать на каждый residual новым regex. Контролируемая модель: **freeze cleanup expansion** → **JS scan gate на все user-visible surfaces** → **bounded LLM repair** → повторный scan → block send.

**Ответ оператору:** QA сейчас идёт через LLM; JS — safety/cleanup слой с неполным surface coverage. Без governance можно сползти в бесконечные JS-патчи; под контролем — только если JS cleanup заморозить и перенести rewrite в repair loop.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `8341f569` — HOTFIX01 production apply evidence — **PASS** |
| Checkpoint `8341f569` | Present — **PASS** |
| Staged index | Empty — **PASS** |
| Remote divergence | noted; **no pull / no push** |
| Foreign WIP | Preserved — **PASS** |
| Live n8n | GET-only Worker + execution `3352` — **PASS** |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, v14 architecture review, issue backlog/test matrix, PC-14 strict cleanup audit, FU-02 TZ residual audit/proposal, HOTFIX01 production apply, HOTFIX01 after-apply sanitized Worker, live GET Worker after HOTFIX01, execution outputs for `seo20260713221847nksocr`.

**Note on report paths:** PC-14 base audit file is `REPORT-metabot-seo-agent-v14-pc14-strict-cleanup-enforcement-audit.md` (PC-label match; naming differs slightly from some historical references).

---

## 3. Operator Concern

> «у нас сейчас QA идёт через JS ? … заложено что QA занималась LLM … можем попасть в бесконечный фикс JS функций?»

| Question | Evidence-backed answer |
|----------|------------------------|
| QA через JS? | **Нет.** SEO QA = LLM OpenRouter. |
| Есть ли LLM QA в схеме? | **Да** — payload + HTTP + extract + status + Format block `=== 3. SEO QA ===`. |
| JS что делает? | Deterministic cleanup/scan на **подмножестве** полей. |
| Бесконечный JS fix? | **Да, риск есть**, если продолжать patch-per-residual. Архитектурно не «всё уже под контролем» без final multi-surface gate + freeze cleanup + repair loop. |

---

## 4. Current QA Ownership

### Nodes

| Node | Role |
|------|------|
| `Build SEOQA Payload` | JS builds OpenRouter payload + system/user prompts |
| `Run SEO QA` | HTTP → OpenRouter |
| `Run Extract SEO QA` | Parse `seoqa` JSON |
| `Status SEO QA` | Telegram progress |
| `Postcheck Strict Claims` | Optional JS force-downgrade of `seoqa` / factcheck **only if `strict=true`** and content hits |
| `Format Run Pipeline` | Renders QA; optional FINAL STRICT GATE on **content_markdown** if `strict=true` |

### Answers (2.1)

1. SEO QA implemented by: `Build SEOQA Payload`, `Run SEO QA`, `Run Extract SEO QA` (+ soft post-gates).  
2. **LLM-based**, with **mixed** deterministic side-gates (`strict_risk_scan`, postcheck, format gate).  
3. Default model in payload: `openai/gpt-4.1-mini` (OpenRouter path).  
4. Receives: SEO Text (`content_markdown`), outline, SEO Strategy, original brief, `strict_risk_scan`, `content_score`, `table_sanity_check`. **Does not** receive final Telegram composite. Banned markers: **partial list** in prompt (missing explicit hard family `удобств*` / `удобн*`).  
5. Verdict **affects UX banner** (`STRICT QA REJECT` if reject or `strict_risk_scan.count>0`) but pipeline **still sends** material — not a hard abort/store block.  
6. **No** authority to force repair/retry loop.  
7. Runs **before** `Format Run Pipeline`.  
8. **Yes** — QA summary generated **after** `Strict Risk Scanner`, and is **not** scanned/cleaned afterward.

Smoke `3352`: `seoqa.verdict=approved`, `score=100`, summary contains `для удобства восприятия, как указано в брифе`.

---

## 5. Current Strict Cleanup / Scanner Ownership

| Node | Version (observed) | What it cleans/scans | Scope |
|------|--------------------|----------------------|-------|
| `TZ Strict Cleanup` | `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` | outline string fields incl. `tables.decision_reason`, sections, faq, … | **outline-side** |
| `Final Text Cleanup` / `Hard Final Cleanup` | (pre-strict) | formatting / limited marker replace on text | `content_markdown` |
| `Run Text Repair` | LLM | rewrite text | text |
| `Strict Cleanup` | `v15-strict-cleanup-pc14-fu01-r1` | PC-14/FU-01 families | **`content_markdown` only** |
| `Strict Risk Scanner` | `v13-run-strict-risk-scanner-hard-v4` | detect banned labels | **`content_markdown` only** |
| `Postcheck Strict Claims` | — | force QA/factcheck downgrade | content; **`strict=true` only**; marker set **narrower** (no `удобств`/`позволя`) |
| `Format Run Pipeline` FINAL STRICT GATE | — | downgrade seoqa/factcheck + banner | content; **`strict=true` only** |

**Ignored by text scanner/cleanup:** `seo_strategy` (incl. `table_strategy.reason`), `seoqa.summary`, factcheck summary, full Telegram composite, memory row as surface.

**Families:** duplicated across TZ / Strict Cleanup / Risk Scanner / Format / Postcheck / QA prompt — **not centralized**.

**Prompt + JS both** define banned wording; lists **overlap incompletely**.

Smoke graph order (abridged):

`Run Extract Outline → TZ Strict Cleanup → … Strategy … Text… Repair → Strict Cleanup → Table Sanity → Strict Risk Scanner → … Build SEOQA → Run SEO QA → Factcheck → Postcheck → Normalize → Format Run Pipeline → Send Telegram Run`

---

## 6. User-Visible Output Surface Map

| Surface | Source | Gen | Scanned | Cleaned | LLM repair | Telegram |
|---------|--------|-----|---------|---------|------------|----------|
| Task ID / flags / tables policy | Format | JS | no | no | no | yes |
| SEO ТЗ incl. `Причина:` | Outline→TZ→Format | LLM | no (TZ cleans) | TZ yes | no | yes |
| SEO Strategy + `Table strategy:` JSON | Strategy→Format | LLM | **no** | **no** | no | **yes** |
| SEO Текст / table explanation / FAQ-in-text | Text path→Strict→Format | LLM | **yes** | **yes** | yes (text repair) | yes |
| SEO QA verdict/score/summary/checks | QA→Format | LLM | **no** | **no** | no | **yes** |
| Factcheck verdict/summary | Factcheck→Format | LLM | **no** | **no** | no | yes |
| STRICT QA REJECT banner | Format | JS | uses risk/QA | n/a | no | conditional |
| Debug Strategy JSON | same as Strategy block | LLM | no | no | no | **yes (problem)** |

Evidence: `pc14-fu03-run-output-surface-map.json`.

---

## 7. HOTFIX01 Smoke Residual Analysis

| Dimension | Result |
|-----------|--------|
| Runtime / task completion | **PASS** (exec `3352`, 3/3 parts) |
| SEO QA / Factcheck reported | approved / 100 / approved |
| `strict` flag | **`false`** (NL ban list in brief ≠ `--strict`) |
| SEO ТЗ top-level `Причина` | **PASS** — cleaned to `для структурированного представления…` (`tz_strict_cleanup.count=1`, field `outline.tables.decision_reason`) |
| SEO Strategy `reason` | **FAIL residual** — `для удобства восприятия…` |
| SEO Text explanation | **PARTIAL** — `Таблица представлена для наглядности восприятия…` |
| SEO QA summary | **FAIL residual** — `…для удобства восприятия, как указано в брифе` |
| `strict_risk_scan` | `count=0`, `verdict=ok` (text-only; after cleanup) |

Classification matches prior Web-GPT note: RUNTIME PASS · TASK PASS · TZ PASS · FULL STRICT SURFACE **PARTIAL**.

---

## 8. Root Cause of Residuals

1. **Strategy regenerated banned phrase** after TZ cleaned outline reason; no Strategy-side cleanup/scan.  
2. **Format dumps** `JSON.stringify(seoStrategy.table_strategy)` into Telegram → residual becomes user-visible.  
3. **Strict Cleanup remap** `удобства → наглядности` on text creates **synonym residual** (`наглядности восприятия`) that scanner does not ban.  
4. **LLM QA** sees brief instruction to use the phrase + clean text + `strict_risk_scan.count=0` → **approves** and **echoes** phrase into summary.  
5. Prompt forbidden-markers list **does not hard-include `удобств*`**.  
6. Final gates in Format/Postcheck **skipped** because `strict=false`. Even with `strict=true`, Format/Postcheck still scan **only `content_markdown`**, not Strategy/QA summary.  
7. **Not** “Format reintroduces stale pre-TZ outline field”: cleaned outline reason stayed clean; unsanitized **parallel fields** were rendered.

---

## 9. Infinite JS Fix Risk

| Topic | Assessment |
|-------|------------|
| Loop risk | **Yes** — patch Strategy cleanup → QA summary → synonym after remap → next smoke finds new surface |
| Surfaces that keep producing residuals | Strategy reasons/risk_notes, QA/factcheck summaries, cleanup synonyms, any new rendered debug JSON |
| Band-aid | New regex per surface/phrase |
| Architectural | Central marker SOT + multi-surface scan gate + bounded LLM repair + freeze cleanup |
| Minimum JS to keep | Detection gate + small frozen cleanup maps for known-safe fields already shipped |
| Move to LLM/prompt | Semantic rewrite of residuals; hard contract that markers apply to **all** generated objects |

**Is everything under control today?** No — coverage gaps are proven by smoke `3352`.

---

## 10. Recommended Governance Model

| Layer | Owns |
|-------|------|
| **Generation Prompt Contract** | **Source of truth** for strict marker families; all generators (outline/strategy/text/QA) |
| **LLM SEO QA** | Semantic QA; hard-fail if markers present in reviewed objects; must not treat brief “inject bad phrase” as approval free-pass without flagging surface pollution |
| **LLM Repair Loop (bounded)** | Rewrite listed residuals/surfaces; max N attempts; no open-ended JS synonym arms race |
| **Deterministic JS Scan Gate** | Detect on **all user-visible surfaces** before send; send decision SoT |
| **Limited Deterministic Cleanup** | Freeze expansion; keep existing TZ/text maps only where safe |
| **Final Telegram Surface Gate** | Compose allowlisted surfaces; **hide/sanitize Strategy debug JSON**; scan or omit QA/factcheck summaries |

Policy recommendations:

- Block final send if any user-visible surface hits markers (`STRICT QA REJECT` = hard stop, not cosmetics).  
- QA/factcheck summaries: scan / sanitize / omit if polluted.  
- Strategy debug JSON: hide from Telegram or sanitize.  
- `/get`: return last **sanitized approved** payload; if only polluted stored — show residual flag, not silent “clean approved”.  
- Memory: store raw internals separately from sanitized user payload; never mark polluted as approved.

Hypothesis from charter **confirmed** by evidence: preferred path is **repair-loop + multi-surface JS gate**, not endless cleanup.

---

## 11. Recommended Next Backlog Item

| Field | Value |
|-------|-------|
| **Decision** | `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED` |
| **Recommended next** | `PC14_FU03_REPAIR_LOOP_PROPOSAL` |

Proposal should include: centralized marker module, final multi-surface scan gate, Strategy/QA surface policy, bounded repair loop wiring, Telegram composition rules, `/get`/memory contract — **sandbox-first**, per safe-workflow protocol.

Optional prior step if operator wants commit before proposal: `PC14_FU03_AUDIT_PERSIST` (this task intentionally does **not** stage/commit).

---

## 12. Evidence Files Created

`projects/metabot-seo-content-agent/exports/pc14-fu03-strict-surface-governance/2026-07-14/`

- `SEO-Content-Agent-Beta-v14-Worker.production-pc14-fu03-readonly.sanitized.json`
- `pc14-fu03-strict-surface-node-map.json`
- `pc14-fu03-run-output-surface-map.json`
- `pc14-fu03-qa-and-strict-gate-flow.json`
- `pc14-fu03-residual-surface-analysis.json`
- `pc14-fu03-governance-options.json`
- `PC14-FU03-STRICT-SURFACE-GOVERNANCE-MANIFEST.md`
- `pc14-fu03-readonly-gather-summary.json`
- `pc14-fu03-execution-node-outputs-redacted.json`
- `pc14-fu03-secret-scan.json` (after scan)

Local raw (not for commit):

- `local/pc14-fu03-strict-surface-governance-2026-07-14/worker-production-readonly.raw.json`
- `local/pc14-fu03-strict-surface-governance-2026-07-14/worker-execution-3352.raw.json`

Report:

- `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-strict-surface-governance-audit.md`

---

## 13. Out-of-Scope Preserved

- Website Factory / FP-0002 / Shpigovsky foreign WIP untouched  
- No Intake/Admin/sandbox mutation  
- No Telegram / OpenRouter / Sheets writes  
- No git stage/commit/push/pull  

---

## 14. SAFE UNKNOWN

- Whether operator will require `PC14_FU03_AUDIT_PERSIST` before repair-loop proposal  
- Exact desired UX for hiding Strategy block vs sanitizing in-place (product choice)  
- Whether Intake currently exposes/propagates `--strict` consistently for NL “не используй слова” briefs  
- Full Sheets memory cell schema for raw vs sanitized columns (not required for this graph audit)  
- Whether repairing Strategy before text generation is preferable to post-format repair-only (proposal trade-off)

---

## 15. Final Status

| Field | Value |
|-------|-------|
| **Audit** | `PC14_FU03_STRICT_OUTPUT_SURFACE_GOVERNANCE_AUDIT` |
| **Decision** | `PC14_FU03_GOVERNANCE_AUDIT_COMPLETE_REPAIR_LOOP_RECOMMENDED` |
| **Recommended next step** | `PC14_FU03_REPAIR_LOOP_PROPOSAL` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` (workflow/execution/task IDs and operational labels only in repo evidence; raw under `local/`; naive `sk-` regex also matches substring inside `risk-scanner` version ids — treated as false positive) |
| **Final status** | `COMPLETE — PC14-FU03 strict surface governance audit complete` |

No stage. No commit.

Awaiting operator review.
