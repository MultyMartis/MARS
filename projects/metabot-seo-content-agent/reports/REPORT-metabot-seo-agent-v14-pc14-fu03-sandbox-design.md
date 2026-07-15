# REPORT — MetaBOT SEO Agent PC14-FU03 Sandbox Design

**Date:** 2026-07-16  
**Classification:** Design-only · sandbox implementation charter · documentation only  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — PC14-FU03 Repair Loop sandbox design  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer · SEO Content Agent only  

| Label | Value |
|-------|-------|
| **Design** | `PC14_FU03_SANDBOX_DESIGN` |
| **Based on proposal** | `PC14_FU03_REPAIR_LOOP_PROPOSAL_READY_FOR_SANDBOX_DESIGN` |
| **Proposal commit** | `56e82a05` |
| **Related smoke Task ID** | `seo20260713221847nksocr` |
| **Related Worker execution** | `3352` |
| **Decision** | `PC14_FU03_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| **Recommended next step** | `PC14_FU03_SANDBOX_DESIGN_PERSIST` |
| **Final status** | `COMPLETE — PC14-FU03 sandbox design ready` |

**Constraints honored:** No production/sandbox workflow mutation. No n8n API writes. No Telegram / OpenRouter / Sheets. No `/run`. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

This design turns the approved PC14-FU03 Repair Loop Proposal (Option C, commit `56e82a05`) into an **implementation-ready sandbox charter**. Production Worker `p4mqb4VuPcemIDlC` (92 nodes, post HOTFIX01) will be cloned to inactive sandbox `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03`.

Nine new nodes insert **after `Normalize Run Output`** and **before `Format Run Pipeline`**, implementing:

1. **Build Final Public Payload** — canonical user-visible surfaces; hide raw Strategy JSON  
2. **Final Surface Strict Scan** — central marker SOT (11 hard families incl. `наглядн*`)  
3. **IF clean** → modified Format → existing send/lock/memory  
4. **IF dirty** → bounded LLM repair (max 1) → re-scan → clean send or **hard block** with diagnostic only  

**Format strategy:** minimal edit to existing `Format Run Pipeline` (Choice 1) — not a parallel formatter. **JS cleanup expansion frozen.** PC-07 Close Lock mapping untouched.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `56e82a05` — PC14-FU03 repair loop proposal — **PASS** |
| Checkpoint through `56e82a05` | Present — **PASS** |
| Staged index | Empty — **PASS** |
| Remote divergence | Local/remote diverge noted; **no pull / no push** |
| Foreign WIP | Preserved (Website Factory / FP-0002 / `.recovery-temp` etc.) — **PASS** |
| Live n8n mutation | **Not performed** (design-only) |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, FU03 repair loop proposal report + exports, FU03 governance audit report + exports, FU02 HOTFIX01 sandbox manifest pattern, issue backlog (indexed).

---

## 3. Design Inputs

| Input | Role |
|-------|------|
| `REPORT-metabot-seo-agent-v14-pc14-fu03-repair-loop-proposal.md` | Approved Option C architecture |
| `pc14-fu03-repair-loop-*.json` (2026-07-16) | Node plan, surface policy, memory/get, harness, risk |
| `REPORT-metabot-seo-agent-v14-pc14-fu03-strict-surface-governance-audit.md` | Root cause + smoke residuals |
| `pc14-fu03-strict-surface-node-map.json` | Production graph tail, 92 nodes |
| `pc14-fu03-run-output-surface-map.json` | User-visible surface inventory |
| `pc14-fu03-qa-and-strict-gate-flow.json` | QA LLM vs JS ownership |
| Smoke `seo20260713221847nksocr` / exec `3352` | Strategy reason, QA summary, Text near-synonym residuals |

---

## 4. Sandbox Baseline Strategy

| Question | Design answer |
|----------|---------------|
| What sandbox workflow? | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03` |
| Clone baseline? | Production `p4mqb4VuPcemIDlC`, 92 nodes, TZ `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01` |
| Active? | `false` |
| Webhook | New path `seo-content-agent-worker-sandbox-pc14-fu03` (pattern per FU02 HOTFIX01) |
| Credentials | Preserve all production credential references unchanged |
| Side effects in harness | Disable Telegram, OpenRouter HTTP, Sheets append, lock close (mirror FU02 sandbox) |
| Scope freeze | No changes to Intake/Admin; no early-generation rewire; shortcut Switch→Format paths unchanged in v1 |

**Re-export baseline at implementation:** Live Worker `updatedAt` may have drifted since `2026-07-13T21:49:02.829Z`; implementation task must readonly-export before patch.

---

## 5. Proposed Node-Level Design

### 5.1 New nodes (9)

| # | Node | Type | JS / LLM responsibility |
|---|------|------|---------------------------|
| 1 | **Build Final Public Payload** | Code | Compose `public_payload`; NL strict detect; custom task markers; hide Strategy JSON; build `telegram.parts_preview`; stash `internal_raw` |
| 2 | **Final Surface Strict Scan** | Code | Central SOT scan all public surfaces; emit `strict_surface_scan` |
| 3 | **IF Final Surface Clean** | IF | `verdict === 'clean'` → Format; else → repair |
| 4 | **Build Strict Surface Repair Payload** | Code | OpenRouter payload + residuals + protected_fields contract |
| 5 | **Run Strict Surface Repair** | HTTP | One OpenRouter call; model = same as Run Text Repair / SEO QA (`openai/gpt-4.1-mini`) |
| 6 | **Extract Strict Surface Repair** | Code | Parse JSON; merge repaired fields only; rebuild preview |
| 7 | **Final Surface Strict Re-Scan** | Code | Same SOT as #2 |
| 8 | **IF Repaired Surface Clean** | IF | Clean → Format; dirty → reject formatter |
| 9 | **Format Strict Reject Message** | Code | Diagnostic Telegram part + `memory_status=blocked_dirty` |

Version markers: `v1-pc14-fu03-*` per node-plan JSON.

### 5.2 Modified nodes

| Node | Change |
|------|--------|
| **Format Run Pipeline** | If `public_payload` present: render from sanitized surfaces; **no** `JSON.stringify(table_strategy)`; QA/factcheck summary only when `include_summary===true`; set `memory_status` |
| **Prepare Memory Row Run** | Add `memory_status`, `strict_surface_status`, `repair_attempts`, `sanitized_payload`, `blocked_diagnostic`, `raw_internal_ref` |
| **Route Command** (optional) | NL «не используй слова» → `strict_surface_requested=true`; parse custom banned tokens |

### 5.3 Unchanged

TZ Strict Cleanup, Strict Cleanup, Strict Risk Scanner, Postcheck, Close Lock Before Sending, Finish Lock, Take First Item, Send Telegram Run, all LLM generation nodes (except new repair HTTP).

---

## 6. Graph Wiring Plan

### Before (full Run tail)

```
Postcheck Strict Claims → Status Final → Restore Postcheck Data
  → Normalize Run Output → Format Run Pipeline
      ├→ Take First Item → … → Close Lock Before Sending → Send Telegram Run → Finish Lock
      └→ Prepare Memory Row Run → Append Memory Run
```

### After (full Run tail)

```
… → Normalize Run Output
  → Build Final Public Payload
  → Final Surface Strict Scan
  → IF Final Surface Clean
       ├─ TRUE → Format Run Pipeline (modified) → [existing send + memory approved_clean | repair_attempted_clean]
       └─ FALSE → Build Strict Surface Repair Payload
                 → Run Strict Surface Repair → Extract Strict Surface Repair
                 → Final Surface Strict Re-Scan → IF Repaired Surface Clean
                      ├─ TRUE → Format Run Pipeline → [send + memory repair_attempted_clean]
                      └─ FALSE → Format Strict Reject Message
                               → Take First Item → [existing lock/send chain]
                               → Prepare Memory Row Run (blocked_dirty)
```

**Connection removal:** `Normalize Run Output` → `Format Run Pipeline` (direct edge).

**Blocked-path join:** `Format Strict Reject Message` → `Take First Item` (bypasses Format on block). Recommended parallel edge to `Prepare Memory Row Run` for blocked memory row.

**Shortcut inputs to Format Run Pipeline** (outline-only, text-only, skip-factcheck) **unchanged** — they bypass FU03 gate in sandbox v1.

Detail: `pc14-fu03-sandbox-design-graph-plan.json`.

---

## 7. Data Contracts

Full schemas: `pc14-fu03-sandbox-design-data-contracts.json`.

### 7.1 Strict marker SOT

- Version: `v1-pc14-fu03-strict-marker-sot`  
- 11 hard families: `аккуратн*`, `удобств*`, `удобн*`, `позволя*`, `обеспеч*`, `контрол*`, `безопасн*`, `специализирован*`, `надежн*`, `надёжн*`, `наглядн*`  
- VM-safe: plain RegExp; no `structuredClone`  
- Duplicated into Scan, Re-Scan, Repair Payload nodes (single version string; patch script copies one canonical block)

### 7.2 Public payload

Top-level: `meta`, `surfaces`, `telegram`, `internal`.  
Key policy: `seo_strategy_public` = human bullets only; `seo_qa_public.include_summary` / `factcheck_public.include_summary` gated by scan.

### 7.3 Scan result

`verdict`, `count`, `residuals[]` (family, surface, field_path, snippet, severity), `surfaces_scanned`, `blocked`, `version`.

### 7.4 Repair payload / response

Payload: task_id, SOT, residuals, repairable surfaces, protected_fields, OpenRouter wrapper.  
Response: `status`, `repaired_surfaces`, `unchanged_protected_fields`, `notes`, `errors`.

### 7.5 Memory row

Statuses: `approved_clean`, `repair_attempted_clean`, `blocked_dirty`, `failed`.  
Never mark polluted composite approved.

### 7.6 `/get`

| Status | Public `/get` body |
|--------|-------------------|
| `approved_clean` / `repair_attempted_clean` | `sanitized_payload` |
| `blocked_dirty` | `blocked_diagnostic` only |
| `failed` / not found | Existing semantics |

---

## 8. Format Strategy

| Choice | Description | Verdict |
|--------|-------------|---------|
| **1** | Minimal `Format Run Pipeline` edit — consume `public_payload` when present | **Preferred** — preserves Take First Item / chunk / lock wiring |
| **2** | New `Format Final Public Payload` + bypass Format | **Not preferred** — duplicates multi-part logic, higher drift risk |

**Implementation rule:** Format must not invent unscanned free text after a clean gate verdict. Raw Strategy JSON **must not** appear in default Telegram output.

---

## 9. Strict Mode and NL Banned Words Policy

| Rule | Behavior |
|------|----------|
| Hard SOT | **Always** enforced on final public surfaces, even when `flags.strict=false` |
| NL triggers | «не используй слова», «запрещённые слова», «запрещенные слова» → `strict_surface_requested=true`, `effective_strict_surface_gate=true` |
| Custom words | Parsed into `custom_task_markers[]` for **this task only**; merged at scan time; **do not** mutate central SOT permanently |
| `flags.strict` | Still controls legacy Postcheck/Format content_markdown gates; FU03 final gate is independent |

Smoke `3352` ran with `strict=false` but NL ban list in brief — FU03 gate would still block/repair residuals.

---

## 10. Harness Plan

Offline harness; no Telegram / OpenRouter / Sheets side effects.

| Label | Assert |
|-------|--------|
| FU03-SOT-01 | Central SOT includes all PC14/FU01/FU02 families + `наглядн*` |
| FU03-SCAN-01 … 06 | Scan TZ, Strategy public, Text, QA summary, Factcheck summary, Telegram preview |
| FU03-REPAIR-01 … 04 | Payload build; Strategy/QA clean; task_id preserved |
| FU03-BLOCK-01 | Dirty after repair → diagnostic only |
| FU03-MEM-01 / 02 | Memory statuses approved_clean / blocked_dirty |
| FU03-GET-01 / 02 | `/get` sanitized vs diagnostic |
| FU03-STRICT-01 / 02 | NL trigger; hard SOT without strict flag |
| FU03-SCOPE-01 … 03 | Close Lock unchanged; credentials unchanged; no production mutation |

Fixtures: smoke `3352`, clean pass-through, repair success/fail, custom NL, Strategy hide, QA omit, memory/get.

Detail: `pc14-fu03-sandbox-design-harness-plan.json`.

---

## 11. Sandbox Implementation Evidence Requirements

Next task label: **`PC14_FU03_SANDBOX_IMPLEMENTATION`**.

Must produce:

- Sandbox workflow id  
- Before/after sanitized exports  
- Node / graph / connection diffs  
- Credential preservation + PC-07 Close Lock mapping evidence  
- Harness results (`allPass: true`)  
- Scope summary + manifest  
- Rollback notes (delete sandbox by id)  

Checklist: `pc14-fu03-sandbox-design-implementation-checklist.json`.

---

## 12. Risk and Rollback

| Risk | Mitigation |
|------|------------|
| Graph wiring errors | Single insertion point; static diff; FU03-SCOPE-01 |
| Repair cost/latency | Max 1 call; Strategy hidden |
| Repair hallucination | Rewrite-only + re-scan + block |
| False +/- | Proven stems; clean fixture; freeze synonym remaps |
| Blocked UX | Clear diagnostic + honest `/get` |
| Memory schema | Additive columns only |
| `/get` break | Status-aware selection; GET harness reuse |
| Strategy hide transparency | Human summary bullets; documented tradeoff |
| SOT drift across nodes | One version string + patch script canonical copy |

**Rollback:** Delete sandbox workflow; production unchanged; no live traffic until production proposal approved.

Detail: `pc14-fu03-sandbox-design-risk-rollback.json`.

---

## 13. Decision

| Field | Value |
|-------|-------|
| **Decision** | `PC14_FU03_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| **Recommended next step** | `PC14_FU03_SANDBOX_DESIGN_PERSIST` |
| **Then** | `PC14_FU03_SANDBOX_IMPLEMENTATION` |

No product blocker identified for preferred defaults (Strategy hide, summary-if-clean, max 1 repair).

---

## 14. Evidence Files Created

`projects/metabot-seo-content-agent/exports/pc14-fu03-sandbox-design/2026-07-16/`

- `pc14-fu03-sandbox-design-node-plan.json`  
- `pc14-fu03-sandbox-design-graph-plan.json`  
- `pc14-fu03-sandbox-design-data-contracts.json`  
- `pc14-fu03-sandbox-design-harness-plan.json`  
- `pc14-fu03-sandbox-design-risk-rollback.json`  
- `pc14-fu03-sandbox-design-implementation-checklist.json`  
- `PC14-FU03-SANDBOX-DESIGN-MANIFEST.md`  

Report:

- `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-sandbox-design.md`

No `local/` raw dump required for this design-only task.

---

## 15. Out-of-Scope Preserved

- Website Factory / FP-0002 / Shpigovsky foreign WIP untouched  
- No Intake/Admin/sandbox/production workflow mutation  
- No Telegram / OpenRouter / Sheets / `/run` / `/health` / `/locks`  
- No stage / commit / push / pull  
- No new JS cleanup regex expansion in legacy nodes  
- No PC-07 Close Lock remapping  

---

## 16. SAFE UNKNOWN

- Exact Google Sheets column headers for new memory fields (implementation must confirm sheet layout or use JSON blob column)  
- Whether `/get` handler lives in Intake vs Admin vs Worker memory read path — harness may mock contract until live GET re-verified  
- Human-readable `seo_strategy_public` bullet schema (minimal v1: h1 + section titles + table titles)  
- Live Worker node count/drift since HOTFIX01 export — re-export at implementation  
- Whether shortcut run modes (outline-only) should later pass through FU03 gate — deferred v1  

---

## 17. Final Status

| Field | Value |
|-------|-------|
| **Design** | `PC14_FU03_SANDBOX_DESIGN` |
| **Based on proposal** | `PC14_FU03_REPAIR_LOOP_PROPOSAL_READY_FOR_SANDBOX_DESIGN` |
| **Proposal commit** | `56e82a05` |
| **Related smoke Task ID** | `seo20260713221847nksocr` |
| **Related Worker execution** | `3352` |
| **Decision** | `PC14_FU03_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| **Recommended next step** | `PC14_FU03_SANDBOX_DESIGN_PERSIST` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` (workflow/execution/task IDs, commit hashes, redacted credential markers only; no API keys, tokens, Bearer, live spreadsheet IDs, or webhook secrets in generated evidence) |
| **Final status** | `COMPLETE — PC14-FU03 sandbox design ready` |

No stage. No commit.

Awaiting operator review.
