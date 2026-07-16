# REPORT — MetaBOT SEO Agent PC14-FU03 HOTFIX01 Sandbox Design

**Date:** 2026-07-16  
**Classification:** Design-only — no live mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — PC14-FU03 HOTFIX01 sandbox design  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer · SEO Content Agent only  

| Label | Value |
|-------|-------|
| **Design** | `PC14_FU03_HOTFIX01_SANDBOX_DESIGN` |
| **Based on diagnostics** | `PC14_FU03_OPERATOR_SMOKE_DIAGNOSED_FIX_REQUIRED` |
| **Diagnostics commit** | `cab4597a` |
| **Production apply commit** | `44c05c3b` |
| **Production Worker** | `p4mqb4VuPcemIDlC` |
| **Smoke lock key** | `chat:499423375:1784151029009` |
| **Decision** | `PC14_FU03_HOTFIX01_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| **Recommended next** | `PC14_FU03_HOTFIX01_DESIGN_PERSIST` |
| **After persist** | `PC14_FU03_HOTFIX01_SANDBOX_IMPLEMENTATION` |
| **Final status** | `COMPLETE — PC14-FU03 HOTFIX01 sandbox design ready` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |

**Constraints honored:** No production/sandbox workflow patch. No Telegram / OpenRouter / Sheets. No `/run` / `/health` / `/locks`. No lock/memory cleanup. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

Operator smoke on PC14-FU03 reject path failed after a valid STRICT QA REJECT diagnostic was prepared: `Restore Format Run Items` still hard-requires `$('Format Run Pipeline').all()`, which is intentionally skipped on the reject branch. That aborts before final Telegram materials, Close Lock, and memory append (`blocked_dirty`), after a false “complete / sending materials…” preface.

HOTFIX01 design selects **Option A**: make both restore nodes reject-safe with fallback order `Format Run Pipeline` → `Format Strict Reject Message` → explicit throw. Node delta **0**. Optional connection reorder puts `Prepare Memory Row Run` first on the reject fan-out (matches clean-path order). Full FU03 rollback is **not** preferred. Design is ready for persist, then sandbox implementation.

---

## 2. Background

| Fact | Value |
|------|-------|
| Production apply | `44c05c3b` — harness 21/21 PASS (mocked repair) |
| Production Worker | `p4mqb4VuPcemIDlC` — active, 101 nodes, 9 FU03 nodes |
| Smoke | Intake `3353` OK · Worker `3354` error ~119s · task `seo202607152130389k7zou` |
| FU03 runtime | dirty(11) → live repair ~31s → dirty(17) → reject prepared |
| Diagnostics | `cab4597a` / `PC14_FU03_OPERATOR_SMOKE_DIAGNOSED_FIX_REQUIRED` |
| Prefers | HOTFIX01 over immediate full rollback |

---

## 3. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| Checkpoint `cab4597a` | Present (HEAD) — **PASS** |
| Checkpoint `44c05c3b` | Present (parent) — **PASS** |
| Staged index | Empty — **PASS** |
| Branch vs origin | **ahead 2 / behind 29** — noted; **no pull / no push** |
| Foreign WIP | Preserved (Website Factory / FP-0002 / OCPilot / `.recovery-temp`) — **PASS** |
| Live n8n mutation | **Not performed** |

Authority / evidence read: `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, safe-workflow / import-safe / grammar refs, FU03 diagnostics + production apply + sandbox design/implementation/proposal reports and manifests, after-apply sanitized Worker export, diagnostics JSON pack.

---

## 4. Smoke Diagnostics Recap

| Field | Finding |
|-------|---------|
| Path | dirty → repair → dirty → `Format Strict Reject Message` |
| Last node | `Restore Format Run Items` |
| Error | Node `Format Run Pipeline` hasn’t been executed |
| Preface | `Status Complete` sent ✅ complete / sending materials |
| Final materials | **not sent** |
| Close Lock | **not reached** — lock stayed `pending` / `active` |
| Memory | **not appended** (`blocked_dirty` intended) |
| Secondary risk | Identical bug on `Restore Format Run Items After Lock` |

Evidence: `exports/pc14-fu03-operator-smoke-diagnostics/2026-07-16/`.

---

## 5. Current Graph Analysis

### Path A — clean

`Normalize Run Output` → `Build Final Public Payload` → `Final Surface Strict Scan` → `IF Final Surface Clean` [true] → `Format Run Pipeline` → `Take First Item` → `Status Complete` → `Restore Format Run Items` → `Close Lock Before Sending` → `Restore Format Run Items After Lock` → `Parse Mode` → `Send Telegram Run`  
(+ parallel `Prepare Memory Row Run` → `Append Memory Run` from Format)

### Path B — dirty then repair-clean

Same as A through initial dirty IF, then repair → re-scan clean → `Format Run Pipeline` → same downstream.

### Path C — dirty then reject (broken)

Repair → re-scan dirty → `Format Strict Reject Message` → fan-out to `Take First Item` + `Prepare Memory Row Run`  
Send chain: `Take First Item` → `Status Complete` → **`Restore Format Run Items` ERROR**  
Never reaches Close Lock / Restore After Lock / Parse Mode / Send Telegram Run.  
Smoke also showed `Prepare Memory Row Run` `run_count=0` despite an edge — likely fan-out order (`Take First` listed before memory) plus abort before/around memory scheduling.

### Why restore cannot use `$input`

`Status Complete` / `Close Lock Before Sending` consume or replace the item stream. Restore exists to reconstitute formatter chunks via named-node `.all()`. Input-based restore (Option C) is unsafe on the current chain.

Reject item shape already includes `telegram_text`, chunks metadata, real `task_id`, `memory_status=blocked_dirty`, `blocked_diagnostic` — compatible with `Parse Mode` / `Prepare Memory Row Run`.

---

## 6. Design Options

| Option | Idea | Verdict |
|--------|------|---------|
| **A** | Dual-source named-node restore fallback | **Selected** — minimal, reliable, 0 node delta |
| B | New unify/normalize node | Rejected — extra node + rewires |
| C | Restore from input items | Rejected — stream after Status/Close Lock is wrong |
| D | Rewire reject through Format-compatible shim | Rejected — broader clean-path risk |

Priority order used: minimal patch → n8n reliability → least clean-path impact → harness ease → rollback ease.

---

## 7. Selected Design

**Option A — reject-safe restore**

Both:
- `Restore Format Run Items`
- `Restore Format Run Items After Lock`

Use the same loader:

1. Try `Format Run Pipeline` if executed and non-empty  
2. Else try `Format Strict Reject Message` if executed and non-empty  
3. Else throw explicit HOTFIX01 error (do **not** return `[]`)

**Optional recommended hardening (connection-only):** reorder `Format Strict Reject Message` fan-out to `Prepare Memory Row Run` then `Take First Item` (match `Format Run Pipeline`).

**Unchanged:** FU03 scan/repair/SOT, Format Run Pipeline logic, Format Strict Reject Message jsCode, Status texts, Close Lock PC-07 mapping, TZ HOTFIX01, Intake/Admin, credentials, side-effect enabled states.

---

## 8. Node-Level Plan

| Node | Action |
|------|--------|
| `Restore Format Run Items` | Replace jsCode with reject-safe loader |
| `Restore Format Run Items After Lock` | Same jsCode |
| `Format Strict Reject Message` connections | Optional reorder only |
| All other nodes | No change |

Expected counts: **101 → 101** (Δ0).  
Sketch: `exports/pc14-fu03-hotfix01-sandbox-design/2026-07-16/pc14-fu03-hotfix01-code-sketches.json`.

Preserve checks at implement time:
- Close Lock `task_id` = `={{ $('Route Command').first().json.task_id }}`
- TZ marker `v1.1-tz-strict-cleanup-pc14-fu02-hotfix01`
- 9 FU03 nodes still present
- Side-effect enabled/disabled flags unchanged

---

## 9. Graph / Connection Plan

Required graph rewires: **none**.

Recommended:
```
Format Strict Reject Message
  ├─ Prepare Memory Row Run → Append Memory Run   (first)
  └─ Take First Item → Status Complete → Restore… (second)
```

After HOTFIX01, Path C continues through restore → Close Lock → restore-after-lock → Parse Mode → Send Telegram (diagnostic) and memory `blocked_dirty`.

---

## 10. Task ID / Lock / Memory Plan

| Checkpoint | Expected |
|------------|----------|
| After `Route Command` | real `seo…` task_id |
| After `Format Strict Reject Message` | same real task_id on items |
| After restore nodes | same (copied from formatter items) |
| `Close Lock Before Sending` | **PC-07 expression only** — Route Command task_id; never `pending` |
| Memory row | `memory_status=blocked_dirty`, same task_id |

PC-07 mapping remains sufficient after restore fix; reject items already carry real task_id for memory, but Close Lock must keep using Route Command (do not switch to item/`pending`).

---

## 11. Status Preface Plan

**Leave Status Complete / Status Final unchanged in HOTFIX01.**

Reason: minimal scope. Once restore works, STRICT QA REJECT materials follow the preface. Broader reject-aware preface UX is a later optional polish, not required to close the broken path.

---

## 12. Sandbox Implementation Plan

| Item | Design choice |
|------|----------------|
| Source of truth | Live production Worker `p4mqb4VuPcemIDlC` (current 101-node FU03) via read-only GET at implement time |
| Why not only old sandbox JSON | Production is execution truth after apply; re-GET avoids silent drift |
| Target sandbox | Prefer patch inactive `tVGWi7Ud3zz2eGKo` (`Worker.sandbox-pc14-fu03`) after confirming/syncing 101-node FU03 parity with production; acceptable alternative: new inactive clone `…sandbox-pc14-fu03-hotfix01` if operator wants isolation |
| Why existing sandbox OK | Prior FU03 apply source; inactive; continuity of harness tooling |
| Patch scope | Two restore jsCode bodies (+ optional reject fan-out order) |
| Node delta | 0 |
| Side effects in harness | No live Telegram / OpenRouter / Sheets |
| Intake/Admin | Untouched |
| Live operator smoke | Only after sandbox evidence + production proposal/apply approvals |

---

## 13. Harness Plan

Offline/local only. Required cases:

| ID | Expect |
|----|--------|
| `HF01-CLEAN-01` | clean → simulated send/close/memory |
| `HF01-REPAIR-CLEAN-01` | repair-clean → simulated send/close/memory |
| `HF01-REJECT-01` | reject → diagnostic send/close/memory `blocked_dirty` |
| `HF01-REJECT-TASKID-01` | real task_id; not `pending` at Close Lock source |
| `HF01-RESTORE-A-01` | Restore A OK without Format Run Pipeline |
| `HF01-RESTORE-B-01` | Restore B OK without Format Run Pipeline |
| `HF01-PC07-01` | Close Lock expression unchanged |
| `HF01-TZ-01` | TZ HOTFIX01 unchanged |
| `HF01-SIDEFX-01` | side-effect enabled states preserved |
| `HF01-SECRET-01` | no secrets in evidence |

---

## 14. Rollback / Safety Plan

| Preference | HOTFIX01 over full FU03 rollback |
|------------|----------------------------------|
| Full FU03 rollback source | `local/pc14-fu03-production-apply-2026-07-16/rollback/worker-before-pc14-fu03.raw.json` |
| Full rollback when | clean path also broken; sandbox harness fails without quick fix; unexpected production drift; credential/side-effect preservation cannot be assured |
| HOTFIX01 apply backups | Capture raw before-HOTFIX production + sandbox under `local/` during apply tasks |
| HOTFIX01 rollback | Restore prior restore-node jsCode (+ optional connection order) from before-HOTFIX raw |
| Pending smoke lock | Do not couple to rollback; see cleanup policy |

---

## 15. Pending Lock Cleanup Policy

Smoke lock `chat:499423375:1784151029009` stayed `task_id=pending` / `status=active` because Close Lock never ran.

| Rule | Policy |
|------|--------|
| This design task | **must not** clear the lock |
| Timing | Prefer wait until after HOTFIX01; prefer auto-expiry (`2026-07-15T22:00:32.713Z`) |
| `/locks` | May hide expired rows |
| Manual cleanup | Only with separate operator-approved charter if still sticky **and** blocks future `/run` |
| Avoid | Unchartered manual cleanup / Sheets edits |

---

## 16. Risk Matrix

| ID | Risk | Mitigation |
|----|------|------------|
| R1 | Wrong source if both formatters ran | Prefer Format Run Pipeline first |
| R2 | try/catch hides bugs | Throw if both miss; never silent empty |
| R3 | Clean regression | HF01 clean/repair-clean harness |
| R4 | Memory still skipped on later send failure | Recommended fan-out reorder |
| R5 | Retry before fix | No `/run` until HOTFIX01 applied |
| R6 | Full rollback blast | Prefer targeted HOTFIX01 |

---

## 17. Evidence Files Created

Under `projects/metabot-seo-content-agent/exports/pc14-fu03-hotfix01-sandbox-design/2026-07-16/`:

- `PC14-FU03-HOTFIX01-SANDBOX-DESIGN-MANIFEST.md`
- `pc14-fu03-hotfix01-root-cause-summary.json`
- `pc14-fu03-hotfix01-design-options.json`
- `pc14-fu03-hotfix01-selected-design.json`
- `pc14-fu03-hotfix01-node-plan.json`
- `pc14-fu03-hotfix01-graph-plan.json`
- `pc14-fu03-hotfix01-harness-plan.json`
- `pc14-fu03-hotfix01-risk-matrix.json`
- `pc14-fu03-hotfix01-lock-cleanup-policy.json`
- `pc14-fu03-hotfix01-rollback-plan.json`
- `pc14-fu03-hotfix01-code-sketches.json`
- `pc14-fu03-hotfix01-restore-node-analysis.json`
- `pc14-fu03-hotfix01-secret-scan.json`

Report: `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-fu03-hotfix01-sandbox-design.md`  
Raw local helper/facts (untracked): `local/pc14-fu03-hotfix01-sandbox-design-2026-07-16/`

---

## 18. Out-of-Scope Preserved

- No production/sandbox workflow update  
- No Intake/Admin changes  
- No Telegram / OpenRouter / Sheets / `/run` / lock or memory cleanup  
- No stage / commit / push / pull  
- Foreign WIP (Website Factory / FP-0002 / OCPilot / recovery-temp) untouched  
- No marker-list / strict SOT / Format Run Pipeline logic expansion  

---

## 19. SAFE UNKNOWN

| Item | Note |
|------|------|
| Exact n8n fan-out scheduler semantics | Memory `run_count=0` is consistent with ordered/aborting fan-out, but not proven from n8n source; connection reorder is hardening, not sole fix |
| Whether smoke lock still visible now | Expired timestamp suggests likely gone; confirm with operator `/locks` only in a chartered later task |
| Live sandbox current `updatedAt` parity | Must re-GET at sandbox implementation; design uses committed after-apply sanitized + smoke evidence |
| Clean-path live post-FU03 | Not re-proven by this reject smoke; assumed still viable pending HF01 harness |

---

## 20. Final Status

| Field | Value |
|-------|-------|
| Design | `PC14_FU03_HOTFIX01_SANDBOX_DESIGN` |
| Decision | `PC14_FU03_HOTFIX01_SANDBOX_DESIGN_READY_FOR_IMPLEMENTATION` |
| Recommended next | `PC14_FU03_HOTFIX01_DESIGN_PERSIST` |
| After persist | `PC14_FU03_HOTFIX01_SANDBOX_IMPLEMENTATION` |
| Final status | `COMPLETE — PC14-FU03 HOTFIX01 sandbox design ready` |
| Secret scan | `PASS_WITH_REVIEW_LABELS` |
| Persist in this task | **No** — design only |

Awaiting operator review.
