# REPORT — MetaBOT SEO Agent v14 Sandbox GET Hygiene and Next Selection

**Date:** 2026-07-10  
**Classification:** READ-ONLY hygiene audit + next patch selection · no live n8n / Telegram / OpenRouter / Sheets calls · no workflow modifications  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — post sandbox GET verification  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Checkpoint commits verified:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`, `c1915bc8`

**Constraints honored:** Production workflows untouched. Sandbox workflows not activated/deactivated/deleted. No n8n API calls this session. No staging. No commit. Foreign WIP preserved.

---

## 1. Executive Summary

Post–sandbox GET verification hygiene is **acceptable for operator review**. Two inactive sandbox clones (`vNlQeuLl0ZCGEVo0`, `K1SNvOt9AbVxqeux`) remain on n8n as documented test fixtures; local raw results exist under gitignored `local/`; one untracked helper script (`run-sandbox-get.mjs`) is a candidate for future MetaBOT Developer tooling.

**PC-01 closeout:** **`PC01_MONITOR_NO_PATCH`** — sandbox disproved the primary `IF From Task Exists` bypass hypothesis for missing tasks; `IF From Task Exists` patch is **not justified** by current evidence. Intake GET-01 full handoff with large memory output remains **SAFE UNKNOWN**.

**Recommended next work item:** **PC-07 — promote `task_id` on run close** (`Close Lock Before Sending`). Static v14 export shows run-path lock close omits `task_id` while single-path `Close Single Lock Before Sending` promotes it — P0 **IB-03** desync with low implementation risk and clear sandbox tests.

**Final status:** **COMPLETE** — hygiene audit and next item selection completed

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Checkpoint `6263815c` | `6263815ce53a5570df864c21dd2dd713a9e4eaab` ✓ |
| Checkpoint `1b954990` | `1b9549900350e2e3e3e2ec26705737588132bffc` ✓ |
| Checkpoint `84dd9b07` | `84dd9b07c71c51dff75f293056c9846c3ade0e88` ✓ |
| Checkpoint `af6fc35d` | `af6fc35d65c019957c02127a518d8a748fcd6d92` ✓ |
| Checkpoint `61bb6019` | `61bb601944699109c5af918fb1b34319ca2f1820` ✓ |
| Checkpoint `58c8f0b7` | `58c8f0b7301378c0309dc005b79cf2408b43d982` ✓ |
| Checkpoint `bc222072` | `bc222072c69d7bf4e577fdca6100d2527343ea2d` ✓ |
| Checkpoint `46fc6335` | `46fc6335ef15cda26addb195b3fe49d66babaca8` ✓ |
| Checkpoint `c1915bc8` | `c1915bc8f0bcd0464cf655be2c4cc265ffb1a894` ✓ |
| Staged changes | empty ✓ |
| n8n API calls this session | none ✓ |
| Foreign WIP | preserved ✓ |

**Git note:** `HEAD` is ahead of `origin/mars/canonical-post-recovery` (includes `c1915bc8` sandbox GET evidence and unrelated commits). Per charter: no commit/push.

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Signal |
|-------------|--------|
| Smart Reporter | not touched |
| I-SEO Report Hub | `6c496b57`, `6e27dc99` on branch — not touched |
| Website Factory report demo | `M projects/mars-website-factory/...` — foreign WIP |
| WordPress report hub | `M workspaces/website-factory-operations/...` — foreign WIP |
| `workspaces/fp-0002-*` | foreign WIP |
| `projects/ocpilot/` | foreign WIP |
| `.recovery-temp/`, `.restore-test-temp/` | untracked foreign WIP |
| FP-0002 | foreign WIP |

---

## 4. Sandbox Hygiene Audit

### 4.1 n8n sandbox workflows (evidence from `c1915bc8` report only)

| Workflow | ID | Expected active | Repo evidence |
|----------|-----|-----------------|---------------|
| `SEO Content Agent Beta.v14 - Worker.sandbox-get` | `vNlQeuLl0ZCGEVo0` | **false** | Deactivated post-test in sandbox GET verification report |
| `SEO Content Agent Beta.v14 - Intake.sandbox-get` | `K1SNvOt9AbVxqeux` | **false** | Deactivated post-test in sandbox GET verification report |

**Live n8n state this session:** **SAFE UNKNOWN** — no read-only API call performed; operator should confirm inactive flag in n8n UI before reuse or delete.

#### Retain as reusable test fixtures?

**Yes — retain short-term (recommended).** The clones are purpose-built for GET-01/GET-02 regression with isolated webhook paths (`seo-content-agent-worker-sandbox-get`, `seo-content-agent-intake-sandbox-get`), production guardrails in `run-sandbox-get.mjs`, and committed sanitized exports under `exports/sandbox-get-verification/2026-07-10/`. They support re-running Intake GET-02 and Worker GET paths without touching production graphs.

#### Delete later?

**Yes — after operator sign-off and evidence archive.** Per [safe-workflow-patch-protocol-v1.md](../metabot-developer/safe-workflow-patch-protocol-v1.md) §9.3, sandbox clones are disposable once evidence is captured and no follow-up TR cases depend on them.

#### Rename/tag later?

**Optional.** Current `.sandbox-get` suffix is clear. If retained long-term, operator may add tags in n8n UI (e.g. `metabot`, `fixture`, `2026-07-10`) for inventory — not required now.

#### Operator approval before delete or reuse

| Action | Required approval |
|--------|-------------------|
| **Delete** sandbox workflows | Explicit destructive charter: workflow IDs, dry-run confirmation, no production ID overlap |
| **Activate** for re-test | Operator charter per patch protocol Stage 7–11; confirm webhook isolation and Telegram nodes disabled/bypassed |
| **Reuse** as base for PC-xx sandbox | New patch wave charter referencing fixture IDs or fresh clone |

#### Risk if inactive clones remain

| Risk | Severity | Mitigation |
|------|----------|------------|
| n8n workflow list clutter | Low | Periodic operator inventory |
| Accidental activation on production Telegram/Sheets | Medium | Keep **inactive**; document IDs; use production-ID blocklist in runner |
| Inherited production credentials on clone | Medium | Sandbox tests should use test rows/chats; no credential rotation in clone |
| Stale graph drift vs production | Low | Re-clone from fresh export before next patch wave |
| Webhook path collision if activated without isolation | Medium | Paths are distinct from production; verify before activate |

**Action this task:** Do not delete. Do not activate.

### 4.2 Temp / schema-probe workflows

| Source | Finding |
|--------|---------|
| Sandbox GET verification report §12 | Notes possible inactive `TEMP SCHEMA PROBE …` workflows from pre-run API schema probing |
| Repo evidence | No workflow IDs or names beyond that note |
| This session | No read-only n8n API inspection (not absolutely necessary; prior session already documented uncertainty) |

**Status:** **SAFE UNKNOWN** — existence, count, IDs, and active state unverified in this session.

**Proposed next action:** One operator or chartered read-only `GET /api/v1/workflows` inventory filtered by name patterns (`.sandbox`, `.sandbox-get`, `schema`, `probe`, `test`, `MetaBOT`, `SEO Content Agent`). List names + active flag only; no secrets. Archive or delete probe workflows only with explicit approval.

### 4.3 Local / raw / helper file audit

See §5.

---

## 5. Local / Raw / Helper File Audit

| Path | Exists | Classification | Rationale |
|------|--------|----------------|-----------|
| `local/sandbox-get-verification-2026-07-10/sandbox-get-results.json` | **Yes** (`Test-Path` true) | **KEEP_GITIGNORED_RAW** | Per n8n rules §5 — full execution results belong in gitignored `local/`; complements committed sanitized exports; content not re-read this session (permission/gitignore boundary) |
| `projects/metabot-seo-content-agent/exports/sandbox-get-verification/2026-07-10/run-sandbox-get.mjs` | **Yes** | **PROMOTE_TO_TOOL_CANDIDATE** | Reusable sandbox runner with production-ID mutation guard, sanitizer integration, and GET-01/GET-02 fixture payloads; should move to `projects/metabot-seo-content-agent/integrations/` or `metabot-developer/tools/` in a **separate charter** with README + operator approval; remain **untracked** until promoted |
| `exports/sandbox-get-verification/2026-07-10/*.sanitized.json` | **Yes** (committed `c1915bc8`) | **KEEP** (committed evidence) | Sanitized sandbox graph baseline |
| `reports/REPORT-metabot-seo-agent-v14-sandbox-get-verification.md` | **Yes** (committed `c1915bc8`) | **KEEP** | Primary verification evidence |
| `reports/REPORT-metabot-seo-agent-v14-bridge-get01-get02-verification.md` | **Yes** (untracked) | **UNKNOWN** | Pre-sandbox bridge attempt; operator may commit with hygiene wave or leave as session artifact |

**No deletes. No staging.**

---

## 6. PC-01 Closeout

**Status:** **`PC01_MONITOR_NO_PATCH`**

### Original concern

Static audit (**FM-05**, **IB-01**, **PC-01**) suspected `IF From Task Exists` checks `Boolean($json.task_id)` after `Lookup From Task` with `alwaysOutputData: true`, causing missing tasks to bypass Intake `Send NOT-FOUND` and reach Worker — contributing to `/get` silent or mis-routed failures.

### What static audit suspected

- Missing `/get` tasks route to Worker instead of Intake NOT-FOUND.
- `IF From Task Exists` patch required before other waves.

### What sandbox testing showed (`c1915bc8`)

| Test | Result | Implication |
|------|--------|-------------|
| Worker GET-01 (`seo20260519082840wzslmg`) | **PASS** | Existing task retrieval works against live `memory` |
| Worker GET-02 (`seo99999999999999missing`) | **PASS** | Worker not-found text works |
| Intake GET-02 | **PASS** | Intake NOT-FOUND branch; Worker **not** invoked |
| Intake GET-01 | **SAFE UNKNOWN** | Sandbox `Send To Worker` HTTP JSON parse failure on large Worker response — wiring artifact, not routing proof |

**Key:** GET-02 **contradicted** the FM-05 bypass hypothesis in live sandbox + Sheets behavior.

### Why `IF From Task Exists` patch is not justified now

1. Live sandbox GET-02 proved Intake owns not-found without Worker call.
2. Worker GET paths behave correctly for success and not-found.
3. Patching IF without reproduction risks breaking working `/get` success routing.
4. Remaining failure modes (FM-01/02/03/04) are **error-path** concerns, not IF routing — separate patch candidates.

### Remaining SAFE UNKNOWN — Intake GET-01 large response

Intake→Worker handoff for large stored artifacts was not proven in sandbox due to `Invalid JSON in response body` on `Send To Worker` (sandbox `responseNode` vs production fire-and-forget). **Does not** justify PC-01; **does** justify monitoring and optional follow-up (truncated fixture re-test or one operator Telegram `/get` smoke).

### Closeout disposition

| Option | Selected? |
|--------|-----------|
| PC01_CLOSED_NO_PATCH | No — Intake GET-01 and production Telegram parity not fully proven |
| **PC01_MONITOR_NO_PATCH** | **Yes** |
| PC01_REOPEN_IF_PROD_EVIDENCE | Implicit — reopen only if production traces show IF bypass |
| PC01_STILL_BLOCKED | No — sandbox evidence sufficient for no-patch decision |

**Monitor triggers:** Production `/get` missing-task reports; n8n traces showing Worker invoked without memory row; FM-01 handoff failures on success path.

---

## 7. Next Candidate Ranking

Ranking uses: operator impact, risk reduction, implementation risk, sandbox testability, production safety, Sheets schema dependency, LLM/Telegram dependency.

### Rank 1 — PC-07: Promote `task_id` on run close

| Field | Value |
|-------|-------|
| **Issue IDs** | PC-07, FM-14, IB-03 |
| **Description** | `/run` path `Close Lock Before Sending` leaves `seo_active_jobs.task_id` as `pending`; `Close Single Lock Before Sending` already writes real `task_id` |
| **Why now** | PC-01 deprioritized; static export diff is explicit (`task_id` column `removed: true` on run close vs `removed: false` on single close); P0 ops visibility for `/locks` |
| **Risks** | Wrong field mapping corrupts jobs row; must match lock_key lookup |
| **Sandbox tests** | TR-01, TC-I05 (`/run` success), TC-I08 (`/locks` display) |
| **Workflows touched** | Worker only — `Close Lock Before Sending` |
| **Production patch level** | **R2** LOW_LIVE_PATCH |
| **Sheets / LLM / Telegram** | Sheets write only; no LLM; Telegram optional for smoke |
| **Next action** | Patch proposal + node manifest (audit-only charter) |

### Rank 2 — PC-04: Filtered memory lookup (Worker get)

| Field | Value |
|-------|-------|
| **Issue IDs** | PC-04, FM-03, IB-05 |
| **Description** | `Lookup Memory Get` reads full `memory` tab; filter by `task_id` at node level |
| **Why now** | Quota/latency; complements proven GET paths; independent of PC-01 |
| **Risks** | Wrong filter breaks all `/get`; column name drift |
| **Sandbox tests** | TC-W04, TR-12 (Sheets failure inject) |
| **Workflows touched** | Worker — `Lookup Memory Get`, possibly `Find Memory Get Row` guards |
| **Production patch level** | **R2** |
| **Sheets / LLM / Telegram** | Sheets read; no LLM |
| **Next action** | Confirm column map (PC-13 sample); sandbox Worker-only GET regression |

### Rank 3 — PC-08: Ignore expired locks in `Check Active Lock`

| Field | Value |
|-------|-------|
| **Issue IDs** | PC-08, FM-13, IB-02 (related) |
| **Description** | `Check Active Lock` treats expired `active` rows as busy — false blocking after TTL |
| **Why now** | High user impact (chat blocked); code-node patch without new workflows |
| **Risks** | TTL policy mismatch; race with concurrent commands |
| **Sandbox tests** | TR-03, TC-I06 (busy vs expired) |
| **Workflows touched** | Intake — `Check Active Lock` |
| **Production patch level** | **R2** |
| **Sheets / LLM / Telegram** | Sheets read; Telegram busy message path |
| **Next action** | Sandbox with synthetic expired row in test sheet |

### Rank 4 — PC-03: `Send To Worker` error branch + lock compensation

| Field | Value |
|-------|-------|
| **Issue IDs** | PC-03, FM-07, IB-04 |
| **Description** | HTTP handoff failure after `Create Lock Row` leaves orphan `active` lock |
| **Why now** | P0 reliability; high operator pain (“Task Accepted” then silence) |
| **Risks** | **High** — wrong compensation deletes valid locks or double-closes; R3 |
| **Sandbox tests** | TR-14, TC-I04 regression, TC-I06 |
| **Workflows touched** | Intake — `Send To Worker` + new compensation branch |
| **Production patch level** | **R3** HIGH_LIVE_PATCH |
| **Sheets / LLM / Telegram** | Sheets write; Telegram error message |
| **Next action** | Defer until PC-07 (and ideally PC-08) reduce lock-sheet ambiguity |

### Rank 5 — PC-06: Reuse halt on missing source

| Field | Value |
|-------|-------|
| **Issue IDs** | PC-06, FM-06, TC-I16 |
| **Description** | Reuse with invalid `from:task_id` still runs LLM on `MEMORY_LOOKUP_FAILED` stub |
| **Why now** | Cost + confusing output + possible orphan lock |
| **Risks** | UX copy approval; must close lock cleanly on halt |
| **Sandbox tests** | TC-I16, TR-13 |
| **Workflows touched** | Worker — `Prepare Memory Reuse` + IF gate |
| **Production patch level** | **R2–R3** |
| **Sheets / LLM / Telegram** | Sheets read; **OpenRouter** on failure path unless stubbed |
| **Next action** | Sandbox with invalid `from:` — verify no OpenRouter call |

**Not in top 5 but noted:** IB-18 (docs drift) — R0 parallel; IB-19 (test protocol) — largely satisfied by safe-patch protocol; IB-07 (Worker error handlers) — broad R3; PC-05 (zero-item guard) — pairs with PC-04.

---

## 8. Recommended Next Item

**Select exactly one:** **PC-07 — Promote `task_id` on `Close Lock Before Sending`**

### Why PC-07 over PC-04 and PC-03

| Candidate | Reason not first |
|-----------|------------------|
| PC-04 | Higher blast radius on `/get` read path; filter/column verification needed |
| PC-03 | R3 compensation logic; should follow clearer jobs-sheet semantics |
| PC-08 | Strong alternative; PC-07 fixes **data correctness** that makes `/locks` and IB-02/03 triage trustworthy first |

### Evidence anchor

In `exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sanitized.json`:

- **`Close Lock Before Sending`** (run pipeline): `task_id` field mapping **`removed: true`** — does not promote real id.
- **`Close Single Lock Before Sending`** (single pipeline): `task_id` field **`removed: false`** — promotes real id.

Intake creates locks with `task_id: pending` (same export). FM-14 / IB-03 desync is **REPO_EVIDENCED** without requiring live Telegram.

### Recommended next action

Charter **audit-only / patch-proposal-only** task: PC-07 formal proposal + node manifest per safe-workflow-patch-protocol-v1.md §5–§6; no live n8n edit until operator Stage 9 approval.

---

## 9. Recommended Next Prompt Outline

**Title:** MetaBOT SEO Agent PC-07 Patch Proposal — Promote `task_id` on Run Lock Close

| Section | Content |
|---------|---------|
| **Goal** | Author PATCH proposal + node manifest for Worker `Close Lock Before Sending` to mirror single-path `task_id` promotion |
| **Allowed scope** | Read v14 exports, get/lock audits, backlog matrix; write one proposal report under `reports/`; optional sandbox clone plan referencing existing `.sandbox-get` fixtures or new `.sandbox` Worker clone |
| **Forbidden scope** | Live n8n edit; production activation; Telegram/OpenRouter/Sheets API calls; commit/push unless explicitly requested; PC-01 IF patch; unrelated lanes |
| **Expected deliverable** | `REPORT-metabot-seo-agent-v14-pc07-patch-proposal.md` with proposal table, manifest rows, risk R2, tests TR-01/TC-I05/TC-I08, rollback notes |
| **Task mode** | **Patch-proposal-only** (Stage 4–6 of patch protocol) — not sandbox implementation |

---

## 10. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Live n8n inactive flag for sandbox IDs `vNlQeuLl0ZCGEVo0`, `K1SNvOt9AbVxqeux` | Not re-verified this session |
| Temp schema-probe workflow names/IDs/count on n8n | **SAFE UNKNOWN** |
| Intake GET-01 full handoff (large memory) | **SAFE UNKNOWN** — sandbox HTTP JSON parse limitation |
| Production Telegram `/get` success vs Worker sandbox | **Likely yes** — not re-verified via Telegram |
| GET-04 / FM-03 zero-item `Lookup Memory Get` silence | Not exercised |
| FM-01/02 error branches on `/get` | Not exercised |
| `local/.../sandbox-get-results.json` contents | Exists; not read (gitignore/permission) |
| Whether `run-sandbox-get.mjs` should be committed | Operator decision — classify as tool candidate |

---

## 11. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-sandbox-get-hygiene-next-selection.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 12. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** includes `c1915bc8` (sandbox GET verification evidence)
- **Ahead of origin:** yes (MetaBOT + unrelated commits)
- **Staged:** empty
- **MetaBOT untracked (foreign to this report):**
  - `projects/metabot-seo-content-agent/exports/sandbox-get-verification/2026-07-10/run-sandbox-get.mjs`
  - `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-bridge-get01-get02-verification.md`
- **Foreign WIP:** preserved (Website Factory, fp-0002, iseo-report-hub, `.recovery-temp/`, etc.)
- **Commit / push:** not performed

---

## 13. Final Status

**COMPLETE** — hygiene audit and next item selection completed

---

Awaiting operator review.
