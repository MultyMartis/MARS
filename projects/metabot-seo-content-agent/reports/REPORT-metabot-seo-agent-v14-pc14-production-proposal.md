# REPORT — MetaBOT SEO Agent v14 PC-14 Production Proposal

**Task:** PC-14 — Strict Cleanup Alignment + Reject Banner (production-apply proposal only)  
**Classification:** Proposal-only · no live n8n mutation  
**Date:** 2026-07-10  
**Lane:** MetaBOT SEO Content Agent (`@seo_content_agent_bot`) — Worker only  
**Checkpoint anchors:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`, `c1915bc8`, `6704b174`, `6efd6afa`, `e3dc9ef7`, `e36ce56e`, `7e1c50ca`, `335b7f3c`, `688e1c03`, `96a8f08f`, `39a43028`  
**PC-07 status preserved:** `PC07_PRODUCTION_APPLIED_VERIFIED`  
**PC-01 status preserved:** `PC01_MONITOR_NO_PATCH`  
**PC-14 prior status:** `PC14_READY_FOR_PRODUCTION_PROPOSAL`

---

## 1. Executive Summary

This report authorizes **proposal-only** promotion of the PC-14 R1 sandbox patch to **production Worker** `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`).

**Sandbox evidence (`39a43028`) confirms:**

- Two-node patch applied on inactive sandbox `SEO Content Agent Beta.v14 - Worker.sandbox-pc14` (`l4FRqKABF25SnXSj`).
- Harness method `SANDBOX_PATCH_APPLIED_HARNESS_LOCAL` — PC14-T01 through PC14-T08 **all PASS**.
- Production Worker **unchanged** during sandbox (`updatedAt` stable at `2026-07-10T09:09:55.305Z`).

**Proposed production changes (two nodes only):**

1. **`Strict Cleanup`** — apply sandbox-tested `v14-strict-cleanup-pc14-r1`: Unicode capture-boundary regex; cover `аккуратн*`, `удобств*` / `удобн*`, `позволя*`; remove weak ASCII `\b` and weak fallback `даёт возможность`.
2. **`Format Run Pipeline`** — add text-only `STRICT QA REJECT` banner when `seoqa.verdict === 'reject' || strict_risk_scan.count > 0`; insert after `Таблицы:` metadata and before `=== 1. SEO ТЗ ===`; preserve full text delivery; banner intentionally persists into memory and `/get`.

**Risk level:** R1 (two-node, deterministic, reversible, sandbox-verified).

**This task does not perform live apply.** Operator approval and fresh production export are mandatory pre-gates.

**PC-14 production decision:** `PC14_BLOCKED_PENDING_APPROVAL`  
**Pre-apply sub-gate:** `PC14_NEEDS_FRESH_EXPORT_FIRST`  
**Task status:** `COMPLETE — PC-14 production proposal completed`

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
| Checkpoint `688e1c03` | `688e1c03949b4a9f81892ef82f7b174e72dcf0e1` — **PASS** |
| Checkpoint `96a8f08f` | `96a8f08f6dc44ee21a83cd13b4a7032b69587e3e` — **PASS** |
| Checkpoint `39a43028` | `39a4302884bbd00a1f866bbfd37eb2a4508d7191` — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `n8n-project-development-rules-v1.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, PC-14 audit, PC-14 sandbox proposal, PC-14 sandbox implementation, PC-07 operator smoke verification.

**Evidence exports read:** sandbox before/after sanitized JSON, node diffs, test results, manifest.

**Live API / Telegram / OpenRouter / Sheets:** not called (proposal-only).

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Area | Status |
|------|--------|
| Smart Reporter, I-SEO Report Hub, Website Factory, WordPress report hub | not touched |
| FP-0002, OCPilot workspaces | foreign WIP (`M`) preserved |
| `.recovery-temp/` | preserved (`??`) |
| Production n8n mutation | **not performed** |
| Sandbox n8n mutation | **not performed** (this task) |
| PC-07 reopen | not requested — `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-01 | `PC01_MONITOR_NO_PATCH` preserved |
| Git stage / commit / push | not performed |

**Forbidden production changes (explicit):** Intake, Admin, OpenRouter HTTP nodes, Telegram send nodes, lock nodes, memory append nodes, `/get` nodes, `Close Lock Before Sending`, `Close Single Lock Before Sending`, `Finish Lock`, credentials, webhooks, workflow activation state (except documented save mechanics).

---

## 4. Production Patch Scope

| Field | Value |
|-------|-------|
| **Production workflow** | `SEO Content Agent Beta.v14 - Worker` |
| **Production workflow ID** | `p4mqb4VuPcemIDlC` |
| **Sandbox workflow** | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14` (`l4FRqKABF25SnXSj`) — evidence source only |
| **Nodes to patch** | `Strict Cleanup`, `Format Run Pipeline` |
| **Patch stage** | R1 — deterministic alignment + formatter warning |
| **Risk** | R1 |
| **IB/TQ mapping** | IB-10 (TQ-05 repair regression guard), IB-11 (partial lexicon parity for 3 families), TQ-01, TQ-05 |

### 4.1 Strict Cleanup — production target

| Aspect | Current (production baseline) | Proposed (from sandbox `v14-strict-cleanup-pc14-r1`) |
|--------|-------------------------------|--------------------------------------------------------|
| Version | `v13-strict-cleanup-after-text-repair` | `v14-strict-cleanup-pc14-r1` |
| Boundary style | ASCII `\b` on most rules | Unicode capture-boundary: `(^|[^\p{L}\p{N}_])…(?=$|[^\p{L}\p{N}_])` with `u` flag |
| `аккуратн*` | `аккуратно` only | Full adjective morphology + adverb → `внимательн*` forms |
| `удобств*` / `удобн*` | absent | Noun + adjective morphology; phrase `для удобства` → `для наглядности` |
| `позволя*` | partial `\bпозволяет\b`; fallback `даёт возможность` | Full morphology; structural rewrites; **remove** `даёт возможность` fallback |
| jsCode size | 3314 chars | 6107 chars |
| Metadata | `strict_cleanup.applied` boolean | Add `replacements_count`, `families_patched: ['аккуратн','удобств','позволя']` |

### 4.2 Format Run Pipeline — production target

| Aspect | Current (production baseline) | Proposed (from sandbox) |
|--------|-------------------------------|-------------------------|
| Reject banner | absent | Text-only `STRICT QA REJECT` block |
| Trigger | n/a | `seoqa.verdict === 'reject'` OR `strict_risk_scan.count > 0` |
| Insertion point | n/a | After `Таблицы:` policy line, before `=== 1. SEO ТЗ ===` |
| Hard-block text body | n/a | **No** — full `=== 2. SEO Текст ===` preserved |
| jsCode size | 11755 chars | 12435 chars |
| Memory / `/get` | n/a | Banner stored in `full_output_text` — **intentional** |

---

## 5. Evidence Summary

### 5.1 Checkpoint chain

| Checkpoint | Report / artifact | Role |
|------------|-------------------|------|
| `688e1c03` | `REPORT-metabot-seo-agent-v14-pc14-strict-cleanup-enforcement-audit.md` | Root cause audit; `PC14_READY_FOR_PATCH_PROPOSAL` |
| `96a8f08f` | `REPORT-metabot-seo-agent-v14-pc14-sandbox-patch-proposal.md` | Sandbox patch design; `PC14_READY_FOR_SANDBOX_PATCH` |
| `39a43028` | `REPORT-metabot-seo-agent-v14-pc14-sandbox-patch-implementation.md` + `exports/sandbox-pc14/` | Sandbox apply + harness; `PC14_READY_FOR_PRODUCTION_PROPOSAL` |

### 5.2 Root cause (from PC-14 audit `688e1c03`)

**Classification: C — Mixed (intended detection, unintended delivery of flagged text).**

| Layer | Behavior |
|-------|----------|
| **Strict Cleanup** | Last deterministic text mutation; lexicon narrower than scanner; uses ASCII `\b` |
| **Strict Risk Scanner** | Always-on on `/run`; Unicode boundaries; fuller morphology; no text mutation |
| **SEO QA** | Caps to `reject` when `strict_risk_scan.count > 0` |
| **Format Run Pipeline** | Always embeds full `content_markdown` in `=== 2. SEO Текст ===` regardless of verdict |

**PC-07 smoke trigger:** task `seo20260710103247agk8ki` delivered full output with SEO QA `reject` while markers `аккуратное`, `удобства`, `позволяет` remained in text.

| Marker | Strict Cleanup (pre-patch) | Strict Risk Scanner | Gap |
|--------|---------------------------|---------------------|-----|
| `аккуратное` | Only `аккуратно` | `аккуратн(ый\|ая\|ое\|…)` | Adjective/neuter forms missing |
| `удобства` | Not in map | `удобств(о\|а\|у\|ом)` | Entire family missing |
| `позволяет` | `\bпозволяет\b`; fallback `даёт возможность` | `позволя(ет\|ют\|…\|ть)` + Unicode boundaries | `\b` unreliable for Cyrillic; weak fallback |

### 5.3 Exact sandbox node diffs

**Strict Cleanup** (`pc14-strict-cleanup-node-diff.json`):

| Field | Value |
|-------|-------|
| beforeVersion | `v13-strict-cleanup-after-text-repair` |
| afterVersion | `v14-strict-cleanup-pc14-r1` |
| beforeLength | 3314 |
| afterLength | 6107 |

**Format Run Pipeline** (`pc14-format-run-pipeline-node-diff.json`):

| Field | Value |
|-------|-------|
| beforeLength | 11755 |
| afterLength | 12435 |
| bannerInserted | true |
| beforeHadBanner | false |

**jsCode-only diff verification:** only `Strict Cleanup` and `Format Run Pipeline` changed; connections unchanged; lock nodes unchanged; `/get` nodes unchanged; production Worker unchanged.

### 5.4 Harness method and test results

| Field | Value |
|-------|-------|
| **Harness** | `SANDBOX_PATCH_APPLIED_HARNESS_LOCAL` |
| **Path** | Extract `jsCode` from sandbox after-patch export; run `Strict Cleanup` → `Strict Risk Scanner` → `Format Run Pipeline` locally |
| **OpenRouter / Telegram / Sheets** | suppressed |
| **Production during sandbox** | unchanged (`updatedAtBefore` = `updatedAtAfter` = `2026-07-10T09:09:55.305Z`) |

| Test | Result | Key observation |
|------|--------|-----------------|
| PC14-T01 (`аккуратное`) | **PASS** | → `внимательное снятие деталей`; `strictCount=0` |
| PC14-T02 (`удобства`) | **PASS** | → `для наглядности восприятия`; `strictCount=0` |
| PC14-T03 (`позволяет`) | **PASS** | → `что при этом возможно определить состояние`; `strictCount=0` |
| PC14-T04 (combined smoke) | **PASS** | All three families neutralized; `strictCount=0`; no banner |
| PC14-T05 (clean control) | **PASS** | byte-identical; `strictCount=0` |
| PC14-T06 (`гибкость` — not in cleanup map) | **PASS** | `strictCount=1`; banner present; full text preserved |
| PC14-T07 (clean approved) | **PASS** | No banner |
| PC14-T08 (lock diff guard) | **PASS** | Lock/get nodes unchanged vs production |

**testsSummary.allPass:** true

### 5.5 Remaining SAFE UNKNOWN (from evidence chain)

| Item | Status |
|------|--------|
| Production Worker current state vs `exports/live-v14-evidence/2026-07-10/` baseline | **SAFE UNKNOWN** until fresh export at apply time |
| n8n hosted Node.js exact version | **SAFE UNKNOWN** — capture-boundary regex chosen (no lookbehind dependency) |
| Russian morphology edge cases (rare inflections) | Requires operator copy QA on live smoke |
| Banner in memory/`/get` on first live reject run | **Documented intentional** — not yet live-verified |
| Whether production `updatedAt` still `2026-07-10T09:09:55.305Z` | **SAFE UNKNOWN** — re-check at fresh export |

---

## 6. Pre-Apply Requirements

Before any live production apply, **all** checks must pass. If any fails, live apply **must stop**.

| # | Requirement | Rationale |
|---|-------------|-----------|
| 1 | Fresh read-only export of production Worker `p4mqb4VuPcemIDlC` | Detect production drift since sandbox clone |
| 2 | Confirm production workflow name: `SEO Content Agent Beta.v14 - Worker` | ID/name mismatch guard |
| 3 | Confirm production baseline still matches expected pre-PC14 state for `Strict Cleanup` and `Format Run Pipeline` | Prevent patching wrong baseline or double-apply |
| 4 | Confirm PC-07 production patch still present: `Close Lock Before Sending` has real `task_id` mapping (`$('Route Command').first().json.task_id`) | PC-07 regression guard |
| 5 | Confirm no concurrent operator edits in n8n | Avoid overwrite conflict |
| 6 | Save raw rollback export to gitignored local path (e.g. `local/production-pc14-2026-07-10/before/`) | Rollback Option A |
| 7 | Save sanitized before-patch export to repo evidence path (e.g. `exports/production-pc14/2026-07-10/`) | Audit trail |
| 8 | Confirm operator approval for live patch | Human gate per `safe-workflow-patch-protocol-v1.md` |
| 9 | Confirm post-apply smoke mode: local/harness only, Telegram operator `/run`, or both | Scope charter for apply task |

**Sub-gate for this proposal:** `PC14_NEEDS_FRESH_EXPORT_FIRST` — committed evidence is sandbox-derived; production must be re-exported immediately before apply.

---

## 7. Production Apply Plan

**Plan only — do not execute in this task.**

Per `safe-workflow-patch-protocol-v1.md` Stages 6–8 (approval → live apply → evidence).

| Step | Action | Evidence output |
|------|--------|-----------------|
| 1 | GET production Worker `p4mqb4VuPcemIDlC` (read-only n8n API) | Raw JSON |
| 2 | Save raw before-patch export under gitignored local path | `local/production-pc14-YYYY-MM-DD/before/worker.raw.json` |
| 3 | Sanitize before-patch export | `exports/production-pc14/YYYY-MM-DD/*.before-patch.sanitized.json` |
| 4 | Verify baseline: `Strict Cleanup` = `v13-strict-cleanup-after-text-repair`; `Format Run Pipeline` has no banner | Diff guard |
| 5 | Verify PC-07: `Close Lock Before Sending` `task_id` mapping unchanged | Static check |
| 6 | Apply **only** two node `jsCode` changes from sandbox after-patch export | In-memory patch object |
| 7 | Save production Worker via n8n API PUT/PATCH | API response |
| 8 | Re-export production Worker | Raw after JSON |
| 9 | Sanitize after-patch export | `exports/production-pc14/YYYY-MM-DD/*.after-patch.sanitized.json` |
| 10 | Create node-level diffs | `pc14-production-strict-cleanup-node-diff.json`, `pc14-production-format-run-pipeline-node-diff.json` |
| 11 | Verify diff touches only expected nodes/fields (`jsCode` on two nodes) | Diff report |
| 12 | Confirm active state unchanged (unless n8n save mechanics require toggle — document if so) | `active` flag compare |
| 13 | Run post-apply harness (PC14-PROD-01) | `pc14-production-harness-results.json` |
| 14 | Optional: operator Telegram smoke (PC14-PROD-02, PC14-PROD-03) | Smoke report |
| 15 | Write apply report; **do not push** unless separately authorized | `REPORT-metabot-seo-agent-v14-pc14-production-apply.md` |

**Patch source of truth:** `exports/sandbox-pc14/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14.after-patch.sanitized.json` — extract `jsCode` for the two target nodes only.

---

## 8. Smoke Test Plan

### PC14-PROD-01 — local production export harness

**When:** Immediately after production save, before optional Telegram smoke.

**Method:** Extract post-patch `jsCode` from fresh production sanitized export; run same local harness as sandbox (`SANDBOX_PATCH_APPLIED_HARNESS_LOCAL`).

| Case | Input / condition | Expected |
|------|-------------------|----------|
| Marker cleanup 1 | `аккуратное снятие деталей` | Neutralized; `strict_risk_scan.count=0` |
| Marker cleanup 2 | `для удобства восприятия` | Neutralized; `strictCount=0` |
| Marker cleanup 3 | `что позволяет определить состояние` | Neutralized; `strictCount=0` |
| Combined smoke | PC-07 excerpt (three families) | All neutralized; no banner |
| Clean control | Neutral copy, no markers | byte-identical or >0.98 similarity |
| Reject banner | `гибкость` + mock `seoqa.reject` | Banner present; text preserved |
| No-banner approved | clean + `approved` + `count=0` | No `STRICT QA REJECT` |
| Lock diff guard | static diff vs before-patch export | Zero changes outside two nodes |

**Pass criteria:** Same pass behavior as sandbox PC14-T01–T08.

### PC14-PROD-02 — operator Telegram smoke (optional)

**When:** Only if operator approves live `/run` in apply charter.

**Input:** Short `/run` brief intentionally likely to produce strict markers (similar to PC-07 smoke but post-patch).

**Expected:**

- Strict markers removed before final output, **or** if any remain, `STRICT QA REJECT` banner present at top.
- Lock closes with real `task_id` (PC-07 guard).
- Memory row appended `status=ok`.
- No regression in PC-07 `task_id` promotion.

### PC14-PROD-03 — `/get` behavior (optional)

**When:** After PC14-PROD-02, if operator runs `/get task_id`.

**Expected:**

- `/get` returns stored output.
- If run was reject, banner visible in stored output — **intentional**.
- If run was clean approved, no banner.

---

## 9. Rollback Plan

### Option A — full workflow restore

1. Import raw pre-patch production export from gitignored `local/production-pc14-*/before/worker.raw.json`.
2. Verify `updatedAt` and node count match pre-apply snapshot.
3. Re-run PC14-PROD-01 harness against restored export (optional).

### Option B — reverse two nodes only

1. Copy pre-patch `jsCode` for `Strict Cleanup` and `Format Run Pipeline` from before-patch sanitized export.
2. Save production Worker via n8n API.
3. Verify version reverts to `v13-strict-cleanup-after-text-repair`; banner absent in formatter.

### Rollback triggers

| Trigger | Action |
|---------|--------|
| Production Worker save failure | Option A or B before any smoke |
| Unexpected diff (nodes beyond allowlist) | **Stop** — do not activate; Option A |
| Regex runtime crash in n8n execution log | Option B immediately |
| Final output empty or corrupt | Option A |
| Banner on clean approved output | Option B (formatter only) |
| Strict cleanup breaks clean text heavily (false positives) | Option B (Strict Cleanup only) or Option A |
| Lock/memory/PC-07 regression | Option A — full restore |
| Telegram send failure plausibly caused by formatter patch | Option B (formatter first); escalate to Option A if unresolved |

---

## 10. Risk Analysis

| Risk | Level | Assessment | Mitigation |
|------|-------|------------|------------|
| **R1 validity** | Low | Two-node deterministic patch; sandbox-verified; reversible | Fresh export gate; harness before Telegram smoke |
| **Unicode regex runtime** | Low–Medium | Capture-boundary pattern proven in `Strict Risk Scanner` and sandbox harness | PC14-PROD-01; rollback on crash |
| **Grammar/case awkwardness** | Medium | Replacement tables may produce stiff Russian in edge cases | PC14-T01–T03 parity on production harness; operator copy QA |
| **False positives** | Low–Medium | Narrow families; Unicode boundaries | PC14-T05 clean control on production export |
| **False negatives** | Medium | R1 covers 3 families only; other scanner labels (e.g. `гибкость`) remain | Banner (PC14-T06 pattern) provides operator visibility |
| **Operator UX — banner** | Low | Text-only; lists markers; no hard-block | Documented; operator approves persistence |
| **Banner in memory/`/get`** | Low (accepted) | Intentional visibility tradeoff | Operator approval gate item |
| **No hard-block tradeoff** | Medium (accepted) | Full rejected text still delivered | Aligns with PC-14 audit Option 2; not Option 4 |
| **PC-07 regression** | Low | No lock node edits; PC14-T08 passed | Pre-apply PC-07 mapping check; PC14-PROD-02 lock guard |
| **Production drift** | Medium | Production may have changed since `2026-07-10T09:09:55.305Z` | `PC14_NEEDS_FRESH_EXPORT_FIRST` |
| **Branch ahead of origin / no push** | Low | Local commits include sandbox evidence not yet on remote | Apply task does not require push; evidence captured locally |

**Overall risk level:** **R1** — acceptable for production apply **after** operator approval and fresh export.

---

## 11. Operator Approval Gate

Operator must explicitly confirm **all** items before live apply:

| # | Checklist item |
|---|----------------|
| 1 | Approve production Worker ID `p4mqb4VuPcemIDlC` |
| 2 | Approve two-node production patch (`Strict Cleanup`, `Format Run Pipeline` only) |
| 3 | Approve **no hard-block** behavior — full text still delivered on reject |
| 4 | Approve **banner persistence** in memory and `/get` output |
| 5 | Approve fresh production export + gitignored rollback export before apply |
| 6 | Approve post-apply local harness (PC14-PROD-01) |
| 7 | Choose Telegram smoke: **harness only** / **operator `/run`** / **both** |
| 8 | Approve replacement phrasing for `аккуратн*`, `удобств*`, `позволя*` (Russian copy QA) |
| 9 | Confirm no concurrent n8n edits during apply window |
| 10 | **No push** unless separately authorized |

**Without operator sign-off:** status remains `PC14_BLOCKED_PENDING_APPROVAL`.

---

## 12. Production Decision

| Label | Value | Rationale |
|-------|-------|-----------|
| **Primary decision** | `PC14_BLOCKED_PENDING_APPROVAL` | Proposal complete; live apply not authorized by this task |
| **Pre-apply sub-gate** | `PC14_NEEDS_FRESH_EXPORT_FIRST` | Production baseline must be re-exported before patch |
| **Evidence readiness** | Sandbox complete — `PC14_READY_FOR_PRODUCTION_PROPOSAL` satisfied | All PC14-T01–T08 pass; production unchanged during sandbox |
| **Not selected** | `PC14_READY_FOR_LIVE_APPLY` | Requires operator approval + fresh export |
| **Not selected** | `PC14_BLOCKED_RISK` | R1 mitigations adequate given sandbox evidence |
| **Not selected** | `PC14_DEFER` | No blocker beyond approval/export gates |

**Promotion path:** Operator approval → fresh export → apply task → PC14-PROD-01 → optional PC14-PROD-02/03 → `PC14_PRODUCTION_APPLIED_VERIFIED` (future label).

---

## 13. Recommended Next Prompt Outline

**Title:** `MetaBOT SEO Agent PC-14 Production Apply`

```markdown
Lane: MetaBOT SEO Content Agent only.
Goal: Apply PC-14 R1 two-node patch to production Worker p4mqb4VuPcemIDlC.

Prerequisites (operator-approved):
- Fresh read-only production export
- Rollback raw export saved (gitignored)
- PC-07 Close Lock Before Sending task_id mapping verified

Read:
- REPORT-metabot-seo-agent-v14-pc14-production-proposal.md
- exports/sandbox-pc14/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sandbox-pc14.after-patch.sanitized.json
- safe-workflow-patch-protocol-v1.md

Steps:
1. GET production Worker; save before raw + sanitized exports
2. Apply Strict Cleanup + Format Run Pipeline jsCode only
3. Save via n8n API; re-export; sanitize; node diffs
4. Run PC14-PROD-01 harness on production export
5. Optional: PC14-PROD-02 Telegram smoke; PC14-PROD-03 /get
6. Write REPORT-metabot-seo-agent-v14-pc14-production-apply.md

Constraints:
- Touch only two nodes
- No push unless requested
- Rollback on trigger table in production proposal

Final labels: PC14_PRODUCTION_APPLIED | PC14_PRODUCTION_APPLY_FAILED
```

---

## 14. Files Created

| Path | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-production-proposal.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 15. Git Status

| Field | Value |
|-------|-------|
| Branch | `mars/canonical-post-recovery` |
| Staged | empty |
| This task | one new untracked report |
| MetaBOT untracked (foreign to this task) | `exports/sandbox-pc14/`, `exports/production-pc07/`, prior PC reports — preserved |
| Foreign WIP | Website Factory, OCPilot, fp-0002 workspaces, `.recovery-temp/` — **OUT_OF_SCOPE_PRESERVED** |
| Unpushed commits | Present on branch (includes `39a43028` sandbox evidence) — **not pushed** (out of scope) |
| Commit / push | not performed |

---

## 16. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Production Worker current `jsCode` vs last committed `live-v14-evidence` export | **SAFE UNKNOWN** — fresh export required at apply |
| Production `updatedAt` since sandbox session | **SAFE UNKNOWN** — re-verify at apply |
| n8n hosted Node.js version | **SAFE UNKNOWN** — capture-boundary regex used |
| Rare Russian morphology edge cases | Operator copy QA on first live reject/smoke |
| Operator policy: hard-block on reject in future | **Operator clarification** — PC-14 explicitly rejects hard-block |
| Full IB-11 central lexicon parity | **Deferred** — R1 covers 3 smoke families only |
| Whether branch should be pushed before production apply | **Operator decision** — apply does not require push |

---

## 17. Final Status

| Label | Value |
|-------|-------|
| **Task status** | `COMPLETE — PC-14 production proposal completed` |
| **PC-14 production decision** | `PC14_BLOCKED_PENDING_APPROVAL` |
| **Pre-apply sub-gate** | `PC14_NEEDS_FRESH_EXPORT_FIRST` |
| **PC-07** | `PC07_PRODUCTION_APPLIED_VERIFIED` (unchanged) |
| **PC-01** | `PC01_MONITOR_NO_PATCH` (unchanged) |
| **Sandbox evidence** | `PC14_READY_FOR_PRODUCTION_PROPOSAL` (from `39a43028`) |

Awaiting operator review.
