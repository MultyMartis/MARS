# REPORT — MetaBOT SEO Agent v14 PC-07 Closeout and Next Backlog Selection

**Date:** 2026-07-10  
**Classification:** READ-ONLY closeout + backlog selection · documentation / planning only  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Intake / Worker / Admin  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Checkpoint commits verified:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`, `c1915bc8`, `6704b174`, `6efd6afa`, `e3dc9ef7`, `e36ce56e`, `7e1c50ca`

**Constraints honored:** No live n8n / Telegram / OpenRouter / Sheets calls. No workflow modifications. No staging. No commit. No push. Foreign WIP preserved.

---

## 1. Executive Summary

**PC-07 is closed.** Production Worker `p4mqb4VuPcemIDlC` node `Close Lock Before Sending` now promotes real `task_id` on successful `/run` lock close. Operator smoke task `seo20260710103247agk8ki` (Intake `3339`, Worker `3340`) confirms `memory` row `status=ok` and `seo_active_jobs` closed with `task_id=seo20260710103247agk8ki`, not `pending`.

**Final PC-07 status:** `PC07_PRODUCTION_APPLIED_VERIFIED`

**Recommended next task:** **PC-14 — Strict Cleanup / Strict Risk Enforcement Read-Only Audit** (maps to backlog **IB-10**, vNext **B05**, test cases **TQ-05**, **TQ-10**).

**Rationale:** PC-07 operator smoke surfaced a real content-quality signal — SEO QA `reject` with strict risk markers (`аккуратное`, `удобства`, `позволяет`) still present in delivered output. This is out of PC-07 scope but is the highest-value, lowest-risk next step: read-only pipeline audit before any prompt or code-node patch.

**Alternatives deferred:** `Finish Lock` symmetry (PC-07 smoke already proves close-node promotion; low urgency), sandbox/probe cleanup inventory (hygiene-only; no production impact), PC-08 expired-lock ignore (strong reliability candidate; better after quality audit or in parallel docs wave).

**Task status:** `COMPLETE — PC-07 closed and next backlog task selected`

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
| Live API calls this session | None — **PASS** |
| Foreign WIP | Preserved — **PASS** |

**Authority docs read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `n8n-project-development-rules-v1.md`, `safe-workflow-patch-protocol-v1.md`, v14 architecture review, issue backlog and test matrix, get/lock lifecycle audit, sandbox GET hygiene report, PC-07 proposal/sandbox/production/apply/operator-smoke reports.

**HEAD:** `7e1c50ca` (`docs(metabot): add pc07 operator smoke verification`). Branch ahead of `origin/mars/canonical-post-recovery` — per charter: no commit/push this task.

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Signal |
|-------------|--------|
| Smart Reporter | not touched |
| I-SEO Report Hub | not touched |
| Website Factory report demo | `M projects/mars-website-factory/...` — foreign WIP |
| WordPress report hub | `M workspaces/website-factory-operations/...` — foreign WIP |
| `workspaces/fp-0002-*` | foreign WIP |
| `projects/ocpilot/` | foreign WIP |
| `.recovery-temp/`, `.restore-test-temp/` | untracked foreign WIP |
| FP-0002 | foreign WIP |
| Live n8n / Telegram / OpenRouter / Sheets | no calls |
| Sandbox/probe workflow delete or activation | not performed |

---

## 4. PC-07 Final Closeout

### 4.1 Original issue

On the `/run` path, Worker closed `seo_active_jobs` with `status=done` while leaving `task_id=pending`. Single/reuse path already promoted real `task_id` via `Close Single Lock Before Sending`. This was an **observability and operator audit issue**, not a content generation or `/get` retrieval failure — `memory` always stored the real `task_id`.

**Backlog mapping:** IB-03, FM-14, TR-04.

### 4.2 Scope of fix

| Item | Value |
|------|-------|
| Workflow | Production Worker `p4mqb4VuPcemIDlC` |
| Node | `Close Lock Before Sending` |
| Change | One field: `task_id = {{ $('Route Command').first().json.task_id }}` |
| Out of scope | Intake, Admin, Telegram, OpenRouter, memory append, `/get`, `Finish Lock`, `Close Single Lock Before Sending` |

**Risk class:** R2 (single-node, single-field, proven pattern elsewhere in same workflow).

### 4.3 Verified smoke (operator, 2026-07-10)

| Field | Value |
|-------|-------|
| Task ID | `seo20260710103247agk8ki` |
| Intake execution | `3339` |
| Worker execution | `3340` |
| `memory` row | `mode=run`, `status=ok`, non-empty output (`output_length=9506`) |
| `seo_active_jobs` | Lock created `task_id=pending`, `status=active`; closed `task_id=seo20260710103247agk8ki`, `status=done`, `finished_at` set |
| Telegram | `✅ Задача завершена` (3 parts) — operator-reported |
| SEO QA | `reject` (strict risk markers) — **out of PC-07 scope** |
| Factcheck | `approved` — informational only |

### 4.4 Final PC-07 status label

**`PC07_PRODUCTION_APPLIED_VERIFIED`**

Prior gate `PC07_PRODUCTION_APPLIED_AWAITING_OPERATOR_SMOKE` is **closed**.

### 4.5 PC status register (current)

| PC | Status |
|----|--------|
| PC-01 | `PC01_MONITOR_NO_PATCH` |
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |

---

## 5. Evidence Chain

| Stage | Commit | Artifact | Outcome |
|-------|--------|----------|---------|
| Patch proposal | `6efd6afa` | `REPORT-metabot-seo-agent-v14-pc07-task-id-promotion-patch-proposal.md` | Static export confirms run-path `task_id` omission; gate `PC07_READY_FOR_SANDBOX_PATCH` |
| Sandbox implementation | `e3dc9ef7` | `REPORT-metabot-seo-agent-v14-pc07-sandbox-implementation.md` | Sandbox Worker `kw1fHttu173lrkeW`; harness tests PC07-01–05 pass; gate `PC07_READY_FOR_PRODUCTION_PROPOSAL` |
| Production proposal | `e36ce56e` | `REPORT-metabot-seo-agent-v14-pc07-production-proposal.md` | Operator approval checklist; rollback plan |
| Production apply | (session artifact; pre-`7e1c50ca`) | `REPORT-metabot-seo-agent-v14-pc07-production-apply.md` | Live patch applied; gate `PC07_PRODUCTION_APPLIED_AWAITING_OPERATOR_SMOKE` |
| Operator smoke verification | `7e1c50ca` | `REPORT-metabot-seo-agent-v14-pc07-operator-smoke-verification.md` | Live smoke pass; gate `PC07_PRODUCTION_APPLIED_VERIFIED` |

**Supporting evidence (pre-PC-07):** `58c8f0b7` lock lifecycle audit · `bc222072` safe patch protocol · `6704b174` next-selection rationale for PC-07 over PC-01 patch.

---

## 6. Remaining Notes / Reopen Criteria

### 6.1 Remaining non-blocking notes

| Note | Disposition |
|------|-------------|
| Historical `done` rows with `task_id=pending` | Not backfilled by PC-07; optional separate data-hygiene charter |
| `Finish Lock` still omits `task_id` | Unchanged; PC-07 smoke shows promotion at `Close Lock Before Sending` sufficient for `/run` success path |
| Mid-run `/locks` may show `pending` until close | By design — promotion at close only |
| Sandbox workflows remain inactive | `Worker.sandbox-pc07` (`kw1fHttu173lrkeW`), `Worker.sandbox-get` (`vNlQeuLl0ZCGEVo0`), `Intake.sandbox-get` (`K1SNvOt9AbVxqeux`); cleanup deferred |
| TEMP SCHEMA PROBE workflows | **SAFE UNKNOWN** — existence/count unverified this session |
| Local raw runners | `local/pc07-*`, `local/sandbox-get-*` — gitignored; not promoted |
| PC-07 smoke SEO QA `reject` | Quality signal for PC-14; not PC-07 failure |

### 6.2 PC-07 reopen criteria

Reopen PC-07 only if:

1. Future `/run` rows close with `task_id=pending` after successful completion.
2. `memory.task_id` and `seo_active_jobs.task_id` mismatch on new successful runs.
3. Production Worker mapping on `Close Lock Before Sending` disappears or reverts.
4. Close node stops updating the target row (`status`, `finished_at`, or `task_id`).
5. Operator executes documented rollback and requests re-verification.

---

## 7. Backlog Review Method

Selection criteria applied (in order):

1. **Safety** — prefer read-only / docs-first / sandbox-first; no immediate live production mutation unless strongly justified.
2. **Value** — production reliability, observability, or content quality; reduces recurring operator pain; aligns with PC-01 (`PC01_MONITOR_NO_PATCH`) and PC-07 learnings.
3. **Risk** — prefer R0/R1/R2; avoid high-risk workflow restructuring and broad prompt rewrites without scoped evidence.
4. **Evidence readiness** — sufficient committed reports/exports to start; clear acceptance tests.
5. **Current observed issue** — PC-07 smoke SEO QA `reject` with surviving strict markers weighs toward quality-path audit.

**Sources reviewed:**

- `REPORT-metabot-seo-agent-v14-issue-backlog-and-test-matrix.md` (IB-01–IB-20, TC/TR/TQ matrices)
- `REPORT-metabot-seo-agent-vnext-lane-reanchor-and-plan.md` (B01–B18)
- `REPORT-metabot-seo-agent-v14-get-lock-lifecycle-deep-audit.md` (PC-01–PC-13 patch catalog)
- `REPORT-metabot-seo-agent-v14-sandbox-get-hygiene-next-selection.md` (post-PC-01 ranking)
- `REPORT-metabot-seo-agent-v14-pc07-operator-smoke-verification.md` (live smoke quality signal)
- `known-issues.md`, architecture review §11–§13 (quality layers)

**PC-07 completion shifts priority:** IB-03 / PC-07 lock↔`task_id` sync is **resolved** for new `/run` completions. Next wave should address either **content quality** (smoke signal) or **remaining P0 reliability** (IB-02 stale locks, IB-04 orphan compensation) without undoing PC-07 evidence.

---

## 8. Candidate A — Strict Cleanup Enforcement

| Field | Value |
|-------|-------|
| **Proposed ID** | **PC-14** — Strict Cleanup / Strict Risk Enforcement Read-Only Audit |
| **Backlog IDs** | IB-10, B05, TQ-05, TQ-10, architecture review O4 |
| **Title** | Audit why strict-risk markers survive cleanup and appear in final `/run` output |
| **Problem** | PC-07 smoke: SEO QA correctly `reject`ed output containing strict risk markers `аккуратное`, `удобства`, `позволяет`. Scanners and QA detected them, but markers remained in delivered text. Known issue: Text Repair may reintroduce banned phrases; Strict Cleanup runs post-repair but may not neutralize all lexicon; Postcheck Strict Claims runs after factcheck — late in pipeline. `/run` does not default `--strict`. |
| **Why now** | Fresh production smoke evidence; PC-07 closed — quality gap is the most actionable new signal; aligns with `known-issues.md` Text Repair regression and distributed strict policy. |
| **Expected value** | Clear map of which nodes should remove vs only flag markers; basis for minimal R1/R2 patch proposal (not broad prompt rewrite); improves specialist trust in delivered text. |
| **Risk level** | **R0** (audit phase) → potential **R1–R2** patch follow-up |
| **Suggested first step** | Read-only audit of Worker sanitized export: `Strict Cleanup`, `Strict Risk Scanner`, `Postcheck Strict Claims`, `Build Text Repair Payload`, `Build SEOQA Payload`, `Format Run Pipeline` — document node order, lexicon sources, and whether reject verdict blocks marker display. |
| **Required evidence** | v14 Worker export (`exports/live-v14-evidence/2026-07-10/` or `exports/production-pc07/2026-07-10/`); PC-07 smoke task `seo20260710103247agk8ki` execution `3340` node outputs (operator-redacted); `known-issues.md`; TQ-05/TQ-10 from test matrix. |
| **Acceptance criteria** | Report answers: (1) which layer first introduced each marker; (2) whether Strict Cleanup lexicon covers them; (3) whether SEO QA `reject` still ships full text with markers; (4) recommended minimal fix scope (code vs prompt vs formatter). |
| **Decision** | **SELECTED** — highest value + safest first step |

---

## 9. Candidate B — Finish Lock Symmetry Audit

| Field | Value |
|-------|-------|
| **Proposed ID** | **PC-15** — `Finish Lock` Symmetry Read-Only Audit |
| **Backlog IDs** | IB-03 (residual), TR-04 (partial) |
| **Title** | Determine whether `Finish Lock` needs `task_id` promotion like `Close Lock Before Sending` |
| **Problem** | `Finish Lock` (post-`Send Telegram Run`) updates `seo_active_jobs` with `status`, `finished_at`, `lock_key` only — `task_id` column `removed: true`. PC-07 fixed `Close Lock Before Sending`; symmetry unknown. |
| **Why now** | PC-07 reports flagged as follow-up; smoke did not re-verify full `Finish Lock` chain. |
| **Expected value** | Confirms no regression risk from second close node; optional one-field symmetry patch if failure paths omit `Close Lock Before Sending`. |
| **Risk level** | **R0** (audit) · **R1** (optional symmetry patch) |
| **Suggested first step** | Trace run-path connections: when does `Finish Lock` execute vs `Close Lock Before Sending`? Map failure/cancel branches. |
| **Required evidence** | Worker sanitized JSON connections; PC-07 smoke execution `3340` — whether `Finish Lock` executed; lock lifecycle audit §lock close. |
| **Acceptance criteria** | Document: (1) success `/run` always hits `Close Lock Before Sending` before Telegram; (2) whether `Finish Lock` can overwrite promoted `task_id`; (3) patch needed yes/no. |
| **Decision** | **DEFERRED** — PC-07 smoke proves close-node promotion; `Finish Lock` omission likely harmless per prior audits; lower urgency than quality audit |

---

## 10. Candidate C — Sandbox / Probe Cleanup Inventory

| Field | Value |
|-------|-------|
| **Proposed ID** | **PC-16** — Sandbox and Probe Workflow Cleanup Inventory |
| **Backlog IDs** | Hygiene report §4; safe patch protocol §9.3 |
| **Title** | Inventory inactive sandbox/probe workflows for retain vs archive vs delete |
| **Problem** | Inactive clones remain: `Worker.sandbox-pc07` (`kw1fHttu173lrkeW`), `Worker.sandbox-get` (`vNlQeuLl0ZCGEVo0`), `Intake.sandbox-get` (`K1SNvOt9AbVxqeux`); possible `TEMP SCHEMA PROBE` workflows — **SAFE UNKNOWN**. |
| **Why now** | Post-PC-07 hygiene; reduces n8n clutter and accidental-activation risk. |
| **Expected value** | Operator-approved retention policy; destructive charter ready when needed. |
| **Risk level** | **R0** (inventory) · **R2+** (delete — explicit approval) |
| **Suggested first step** | Read-only n8n workflow list filtered by `.sandbox`, `probe`, `schema`, `MetaBOT` — names + active flag only. |
| **Required evidence** | Hygiene report `6704b174`; sandbox GET report `c1915bc8`; PC-07 sandbox report `e3dc9ef7`. |
| **Acceptance criteria** | Table: workflow ID, name, active, retain/delete recommendation, approval gate. |
| **Decision** | **DEFERRED** — valuable but no production reliability or content impact; requires operator inventory pass; can run parallel to PC-14 |

---

## 11. Other Backlog Candidates Considered

| ID | Title | Priority | Risk | Why considered | Why deferred |
|----|-------|----------|------|----------------|--------------|
| **PC-08** | Ignore expired locks in `Check Active Lock` (IB-02) | P0 | R2 | High user impact — false busy after TTL; ranked #3 pre-PC-07 | Intake live patch; PC-07 smoke did not exercise expiry; strong **second** candidate after PC-14 audit |
| **PC-04** | Filtered memory lookup on Worker `/get` (IB-05) | P1 | R2 | Quota/latency; GET paths proven in sandbox | Independent of PC-07/quality signal; no new production evidence |
| **PC-03** | `Send To Worker` error branch + lock compensation (IB-04) | P0 | R3 | Orphan lock pain | High-risk Intake restructure; defer until lock-sheet semantics stable post-PC-07 |
| **PC-06** | Reuse halt on missing `from:task_id` (IB-16) | P1 | R2–R3 | Wasted LLM cost | No new smoke signal; sandbox testable later |
| **PC-01** | `/get` IF From Task Exists patch (IB-01) | P0 | R2–R3 | Original P0 UX | **`PC01_MONITOR_NO_PATCH`** — sandbox disproved bypass hypothesis |
| **IB-18** | Docs v13/v14 drift | P1 | R0 | Parallel docs wave | Does not address production quality signal from smoke |
| **IB-07** | Worker error-handler subgraphs | P1 | R3 | Silent pipeline death | Broad R3; needs template design (lifecycle audit PC-11) |
| **PC-10** | `/stop-all-flow` honest docs (IB-06) | P1 | R0 | Operator trust | Docs-only; lower urgency than strict cleanup audit |
| **IB-11** | Central strict policy drift | P1 | R1+ | Overlaps PC-14 | PC-14 audit is prerequisite before consolidation spec |

---

## 12. Recommended Next Task

| Field | Value |
|-------|-------|
| **Selected candidate** | **PC-14 — Strict Cleanup / Strict Risk Enforcement Read-Only Audit** |
| **Reason for selection** | PC-07 production smoke produced a fresh, reproducible quality failure: strict markers detected by SEO QA but not removed from final output. Read-only audit is safest next step, has committed export evidence, clear acceptance tests (TQ-05, TQ-10), and addresses documented `known-issues.md` Text Repair regression without immediate live mutation. |
| **Risk level** | **R0** (this phase) |
| **Scope** | Worker run-path quality layers: `Final/Hard Cleanup` → `Text Repair` → `Strict Cleanup` → `Strict Risk Scanner` → `Content Score` → `SEO QA` → `Factcheck` → `Postcheck Strict Claims` → `Format Run Pipeline`; verdict handling when SEO QA = `reject` |
| **Non-scope** | Live n8n patch; prompt rewrites; OpenRouter model changes; Intake/Admin; lock lifecycle; `/get`; PC-07 reopen; sandbox delete |
| **First Cursor task type** | Read-only deep audit — single report, no code/workflow changes |
| **Expected output report** | `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-strict-cleanup-enforcement-audit.md` |
| **Final status labels (next task)** | Start: `PC14_AUDIT_PLANNED` → complete audit: `PC14_READY_FOR_PATCH_PROPOSAL` or `PC14_MONITOR_NO_PATCH` |
| **Live n8n/API access needed?** | **No** for audit phase (sanitized export + optional operator-redacted execution `3340` artifacts). **Yes** later only if patch proposal requires sandbox replay (separate charter). |

**Runner-up:** **PC-08** (expired lock ignore) — schedule immediately after PC-14 audit if operator prioritizes reliability over quality.

---

## 13. Proposed Next Prompt Outline

```markdown
# TASK — MetaBOT SEO Agent PC-14 Strict Cleanup / Strict Risk Enforcement Read-Only Audit

Lane: MetaBOT SEO Content Agent only.
Goal: Explain why strict risk markers survived cleanup in PC-07 smoke task seo20260710103247agk8ki.

Constraints:
- Read-only. No live n8n/Telegram/OpenRouter/Sheets calls unless operator explicitly authorizes redacted execution replay.
- No workflow patch. No commit unless requested.

Read:
- exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sanitized.json
- exports/production-pc07/2026-07-10/ (post-patch export)
- known-issues.md, architecture review §11–§13
- REPORT-metabot-seo-agent-v14-pc07-operator-smoke-verification.md
- issue backlog IB-10, TQ-05, TQ-10

Deliver:
- projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc14-strict-cleanup-enforcement-audit.md

Must answer:
1. Pipeline order and which node outputs contain аккуратное / удобства / позволяет
2. Strict Cleanup vs Strict Risk Scanner vs Postcheck lexicon coverage
3. Whether SEO QA reject still delivers full text with markers to Telegram
4. Minimal fix recommendation (if any) with risk class R0–R2
5. Sandbox test plan before any production patch

Final status: PC14_READY_FOR_PATCH_PROPOSAL | PC14_MONITOR_NO_PATCH | BLOCKED
```

---

## 14. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-pc07-closeout-next-backlog-selection.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 15. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** `7e1c50ca` — `docs(metabot): add pc07 operator smoke verification`
- **Ahead of origin:** yes (includes MetaBOT checkpoint chain through `7e1c50ca` plus unrelated commits)
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** preserved — Website Factory, OCPilot, fp-0002 workspaces, `.recovery-temp/`, etc.
- **Commit / push:** not performed

---

## 16. Final Status

**`COMPLETE — PC-07 closed and next backlog task selected`**

| Item | Status |
|------|--------|
| PC-07 closeout | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-01 | `PC01_MONITOR_NO_PATCH` (unchanged) |
| Next recommended task | **PC-14** — Strict Cleanup / Strict Risk Enforcement Read-Only Audit |
| Next task initial label | `PC14_AUDIT_PLANNED` |

---

Awaiting operator review.
