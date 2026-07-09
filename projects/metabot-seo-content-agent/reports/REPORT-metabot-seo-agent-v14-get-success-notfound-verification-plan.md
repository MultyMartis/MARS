# REPORT — MetaBOT SEO Agent v14 /get Success vs Not-Found Verification Plan

**Date:** 2026-07-10  
**Classification:** READ-ONLY verification plan · patch proposal candidate only · no live API calls · no workflow modifications  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — `/get` success vs not-found paths  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Evidence pack:** `exports/live-v14-evidence/2026-07-10/`  
**Checkpoint commits verified:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`

**Operator observation (in scope):** `/get TASK_ID` previously worked in production — operator could send a task ID and receive task information/result. **Do not assume `/get` is globally broken.**

**Constraints honored:** No live n8n / Telegram / OpenRouter / Sheets calls. No workflow JSON patches. No staging. No commit. Foreign WIP preserved.

---

## 1. Executive Summary

This report reframes **PC-01** from a blind “fix `/get`” to **verify and harden `/get` not-found detection**, respecting operator evidence that **successful `/get existing_task_id` may already work**.

| Area | Finding | Implication |
|------|---------|-------------|
| **Success path** | Intake retrieval branch → filtered memory lookup → Worker `get` route → full-tab memory read → format → Telegram | **High confidence** from sanitized JSON; aligns with operator observation |
| **Not-found routing** | Intake `IF From Task Exists` checks `Boolean($json.task_id)` — **not** memory-row match; `Lookup From Task.alwaysOutputData=true` | Missing tasks may **bypass** Intake `Send NOT-FOUND` and reach Worker — **medium confidence** |
| **Worker fallback** | `Format Memory Get` emits explicit not-found text when `!memory_found \|\| !output` | Worker **can** deliver not-found — but only if pipeline reaches format/send |
| **Silent failure risk** | No error branches on `Send To Worker`, `Lookup Memory Get` zero items, `Send Telegram Memory Get` | User silence possible on **failure paths** — not necessarily on happy path |
| **Locks** | `/get` skips lock path (`lock: null`) | GET-07: repeated `/get` should not create lock — **high confidence** |

**Immediate recommendation:** **A — No patch yet; request live/sandbox test evidence first.** Static evidence supports a **conditional** PC-01 hardening proposal, but operator success observation and `alwaysOutputData` passthrough behavior require verification before any live n8n edit.

**Final status:** COMPLETE — /get verification plan and conservative patch candidate completed

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Checkpoint `6263815c` | exists ✓ |
| Checkpoint `1b954990` | exists ✓ |
| Checkpoint `84dd9b07` | exists ✓ |
| Checkpoint `af6fc35d` | exists ✓ |
| Checkpoint `61bb6019` | exists ✓ |
| Checkpoint `58c8f0b7` | exists ✓ |
| Checkpoint `bc222072` | exists ✓ |
| Staged changes | empty ✓ |
| Live API calls | none ✓ |
| Foreign WIP | preserved, not touched ✓ |

**Git note:** `HEAD` (`a7d19dee`) may differ from `origin/mars/canonical-post-recovery` (`0d1174a3`). Per charter: no commit/push in this task.

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Signal |
|-------------|--------|
| `projects/iseo-report-hub/` | not read |
| Smart Reporter docs | not read |
| Website Factory report demo | `M projects/mars-website-factory/...` — foreign WIP |
| WordPress report hub | `M workspaces/website-factory-operations/...` — foreign WIP |
| `workspaces/fp-0002-*` | foreign WIP |
| `projects/ocpilot/` | foreign WIP |
| `.recovery-temp/`, `.restore-test-temp/` | untracked foreign WIP |

---

## 4. Source Evidence

### 4.1 Governance and product docs (read)

| Source | Role |
|--------|------|
| `AGENTS.md`, `.cursorrules` | MARS boundaries, preflight |
| `README.md`, `OPERATIONAL-INDEX.md` | Product identity |
| `known-issues.md`, `telegram-commands.md` | `/get` silence documented |
| `memory-and-task-reuse.md`, `task-lifecycle.md` | Conceptual semantics |
| `metabot-developer/safe-workflow-patch-protocol-v1.md` | Patch gate (PC-01 wave order) |

### 4.2 Prior v14 reports (read)

| Source | Role |
|--------|------|
| `REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md` | Synthesized I/W/A architecture |
| `REPORT-metabot-seo-agent-v14-issue-backlog-and-test-matrix.md` | IB-01, TC-I11/I12, TR-12 |
| `REPORT-metabot-seo-agent-v14-get-lock-lifecycle-deep-audit.md` | Node-level `/get` paths, FM-01–05, PC-01 |

### 4.3 Live v14 evidence (read + JSON parse)

| Source | Role |
|--------|------|
| `WORKFLOW-MAP-v14.md` | Node index |
| `NODE-INVENTORY-v14.md` | No dedicated error-handler nodes on get path |
| `PROMPT-AND-CODE-NODE-INDEX-v14.md` | Code node sizes |
| `RISK-AND-UNKNOWN-REGISTER-v14.md` | Unknowns |
| `SEO-Content-Agent-Beta-v14-Intake.sanitized.json` | Intake `/get` branch |
| `SEO-Content-Agent-Beta-v14-Worker.sanitized.json` | Worker `get` route |

### 4.4 Authority hierarchy

1. **Live n8n** — execution truth (not accessed)
2. **Operator observation** — `/get existing_task_id` worked (in scope for this plan)
3. **v14 sanitized export** — best repo graph evidence
4. **Prior audits / backlog** — synthesized behavior and issue IDs

---

## 5. PC-01 Reframed

### 5.1 Previous framing (superseded for this task)

> “Fix `/get`” — implied global breakage.

### 5.2 New framing (active)

> **Verify and harden `/get` not-found detection**

| Statement | Status |
|-----------|--------|
| Successful `/get existing_task_id` is **expected to work** and **may already work** in production | **OPERATOR_CLARIFICATION + static evidence** |
| Audit concern is **not-found**, **lookup error**, **Worker handoff error**, and **Telegram send error** handling | **REPO_EVIDENCED** (FM-01–05, IB-01) |
| No live patch is justified until **both** success path and missing-task path are verified | **This report’s gate** |
| PC-01 patch candidate targets **Intake IF condition** (and optionally Worker guards) — **not** rewriting the success path | **Conservative scope** |

### 5.3 Relationship to source issues

| ID | Title | Relevance to reframed PC-01 |
|----|-------|----------------------------|
| **IB-01** | `/get` silent failure | Failure-path focus; does not negate success path |
| **FM-01** | `Send To Worker` HTTP fail | Handoff failure — silent |
| **FM-02** | `Send Telegram Memory Get` fail | Post-format silence |
| **FM-05** | `IF From Task Exists` logic | Not-found routing concern |
| **PC-01** | Fix `IF From Task Exists` | Renamed scope: verify first, harden IF second |

---

## 6. /get Success Path

Traced from sanitized Intake + Worker JSON for `/get seoEXISTING` where `seoEXISTING` exists in `memory` with non-empty `output`.

| Step | Workflow | Node | Expected input | Expected output | Why it should work (existing task) | Evidence confidence |
|------|----------|------|----------------|-----------------|-------------------------------------|---------------------|
| 1 | Intake | `Telegram Trigger` | Telegram message `/get seoEXISTING` | `message.text`, `chat.id`, `from` | Standard bot entry | **High** |
| 2 | Intake | `Detect Local Command` | `message.text` | `command=get`, `task_id=seoEXISTING`, `is_retrieval_command=true` | Regex `/^\/get\s+([a-zA-Z0-9_-]+)/i` | **High** |
| 3 | Intake | `IF Local Command` | `is_local_command=false` | false branch | `/get` is content command, not local | **High** |
| 4 | Intake | `IF Admin Command` | `is_admin_command=false` | false branch | `/get` not admin | **High** |
| 5 | Intake | `Route Retrieval Command` | `is_retrieval_command=true` | true branch | Code comment: retrieval **only** for `/get` | **High** |
| 6 | Intake | `Lookup From Task` | Filter `memory.task_id = seoEXISTING` | Row with `task_id`, `input`, `output`, … | Filtered Sheets lookup on `memory` tab | **High** |
| 7 | Intake | `IF From Task Exists` | `$json.task_id` from lookup row | **true** branch (row has `task_id`) | Matched row includes `task_id` column | **High** for existing row |
| 8 | Intake | `Build Worker Payload` | Lookup row + Telegram message | `worker_payload: { message, lock: null, status_message }` | `isRetrievalOnly` → `lock: null` | **High** |
| 9 | Intake | `Send To Worker` | `worker_payload` | HTTP POST to Worker webhook | Handoff to Worker graph | **High** (no lock created) |
| 10 | Worker | `Route Command` | `message.text` = `/get seoEXISTING` | `mode=get`, `route=get`, `from_task_id=seoEXISTING`, new ephemeral `task_id` | Parses second token as `fromTaskId` | **High** |
| 11 | Worker | `Switch Route` | `route=get` | output key `get` | Switch matches `get` | **High** |
| 12 | Worker | `Lookup Memory Get` | — | All rows from `memory` tab | Full-tab read (no filter in node) | **High** (inefficient but functional) |
| 13 | Worker | `Find Memory Get Row` | All memory rows + `route.from_task_id` | `{ ...row, memory_found: true, from_task_id, chat_id }` | Code filter `row.task_id === target` | **High** |
| 14 | Worker | `Format Memory Get` | Matched row fields | `{ telegram_text, chunk_count, … }` chunks | Formats input (3k) + full output | **High** |
| 15 | Worker | `Send Telegram Memory Get` | `telegram_text` per chunk | Telegram message(s) to user | User receives stored artifact | **High** |

**Operator alignment:** Steps 1–15 explain why `/get existing_task_id` returning task info/result is **consistent with v14 evidence**. No lock row is created; no `Task Accepted` message is sent (user may perceive delay until Worker responds).

**UX note:** No immediate “retrieving…” ack on get path — long Worker/Sheets latency can feel like silence even on success (FM-01 unrelated to routing).

---

## 7. /get Not-Found Path

Traced for `/get seoMISSING` where `seoMISSING` is absent from `memory`.

### 7.1 Intended path (design intent)

```
/get seoMISSING
  → Lookup From Task (no row)
  → IF From Task Exists = false
  → Send NOT-FOUND Message (Intake Telegram)
  → Worker NOT called
```

### 7.2 Actual static evidence (suspected)

```
/get seoMISSING
  → Lookup From Task (no row, alwaysOutputData=true)
  → IF From Task Exists checks Boolean($json.task_id)
  → [TRUE if passthrough preserves parsed task_id from command]
  → Build Worker Payload → Send To Worker
  → Worker get route → Lookup Memory Get → Find Memory Get Row (memory_found=false)
  → Format Memory Get → Send Telegram Memory Get ("Task not found: seoMISSING")
```

### 7.3 Key questions answered

| Question | Answer | Confidence |
|----------|--------|------------|
| **What condition controls `IF From Task Exists`?** | `Boolean($json.task_id)` — boolean true on **any** truthy `task_id` in current item | **High** (JSON line 556) |
| **Memory row vs parsed task_id?** | Checks **task_id field presence**, **not** `memory_found`, **not** `output`, **not** row match proof | **High** |
| **`alwaysOutputData: true` effect?** | When lookup returns zero rows, n8n may still emit an output item; **`task_id` may be inherited from upstream/passthrough** (parsed command id), causing IF **true** | **Medium** — n8n version behavior **SAFE UNKNOWN** without live trace |
| **When does Intake `Send NOT-FOUND` fire?** | Only IF **false** branch — i.e. when `$json.task_id` is falsy after lookup | **High** |
| **Malformed `/get` (no task_id)?** | `Detect Local Command` leaves `task_id=''` → IF false → Intake NOT-FOUND with empty id in template | **Medium** — message may show blank task id |
| **SAFE UNKNOWN without live trace?** | Exact empty-lookup item shape from Google Sheets node v4.7 with `alwaysOutputData` | **Yes** |
| **Sandbox validation?** | TC-I12 / GET-02: trace which node sends not-found; compare Intake vs Worker execution branches | **Required before patch** |

### 7.4 Not-found silent failure modes (even if Worker reached)

| # | Condition | Current behavior | User impact | Confidence |
|---|-----------|------------------|-------------|------------|
| 1 | `Send To Worker` HTTP failure | No error branch | Silence | **High** |
| 2 | `Lookup Memory Get` returns **0 items** (non-error) | `Find Memory Get Row` may not execute | Silence (FM-03) | **Medium** |
| 3 | `Lookup Memory Get` Sheets error | `continueOnFail: true` — error item downstream | Misleading not-found or crash | **Medium** |
| 4 | `Send Telegram Memory Get` failure | No error branch | Silence (FM-02) | **High** |
| 5 | Intake `Lookup From Task` Sheets error | No `continueOnFail` evidenced | Intake halt — **SAFE UNKNOWN** | **Medium** |

---

## 8. Worker-Side Fallback

### 8.1 Worker get chain nodes

| Node | Role | Not-found behavior |
|------|------|-------------------|
| `Lookup Memory Get` | Read entire `memory` tab | No filter; `continueOnFail: true` |
| `Find Memory Get Row` | Code: match `route.from_task_id` | **Always returns 1 item** with `memory_found: false` when no match |
| `Format Memory Get` | Build Telegram text | Explicit: `Task not found: {fromId}` when `!memory_found \|\| !output`; also handles missing `fromId` |
| `Send Telegram Memory Get` | Send chunks | Strips `_`, `` ` ``, `*` for Telegram safety |

### 8.2 Answers

| Question | Answer |
|----------|--------|
| **Does Worker have its own not-found message?** | **Yes** — `Format Memory Get` |
| **Does Worker handle empty lookup?** | **Partially** — code node handles empty **match**, not necessarily **zero items** from Sheets |
| **Could `Find Memory Get Row` fail to run?** | **Yes** — if `Lookup Memory Get` outputs zero items (FM-03) |
| **Could user receive no message?** | **Yes** — handoff failure, zero-item lookup, Telegram send failure, early Worker crash |
| **Who should own final not-found?** | **Intake primary** (fast, no Worker cost); **Worker secondary** (defense in depth if Intake routes forward) |

### 8.3 Dual-path not-found architecture (evidenced)

| Owner | Node | Message |
|-------|------|---------|
| Intake | `Send NOT-FOUND Message` | `Task not found: {{ Detect Local Command.task_id }}` + memory hint |
| Worker | `Format Memory Get` → `Send Telegram Memory Get` | `Task not found: {fromId}` + column hint |

**Risk:** If Intake IF is wrong, Worker becomes **de facto** not-found owner — adds latency, full-tab read, and exposure to FM-01/02/03.

---

## 9. Verification Plan

### Level 1 — Static evidence verification (this task)

**No live calls.** Confirm logic from JSON.

| Check ID | Verification | Result (static) |
|----------|--------------|-----------------|
| S-01 | `/get` sets `is_retrieval_command=true` only for command `get` | **PASS** |
| S-02 | Retrieval branch skips `Create Lock Row` | **PASS** |
| S-03 | `Build Worker Payload` sets `lock: null` for get | **PASS** |
| S-04 | `IF From Task Exists` uses `Boolean($json.task_id)` | **PASS** — flags FM-05 |
| S-05 | `Lookup From Task` has `alwaysOutputData: true` + filter on `task_id` | **PASS** — flags passthrough risk |
| S-06 | Worker `Format Memory Get` has not-found branch | **PASS** |
| S-07 | No error handler on `Send To Worker` / `Send Telegram Memory Get` | **PASS** — flags FM-01/02 |
| S-08 | Operator success observation compatible with success path | **PASS** |

**Level 1 outcome:** Success path **statically sound**. Not-found routing **conditionally suspect** — live trace required.

---

### Level 2 — Sandbox / manual test plan

**Only after operator approval.** Use sandbox workflow clone or controlled production observability.

| Test ID | Input | Expected output | Lock behavior | Memory behavior | Pass/fail evidence | Environment |
|---------|-------|-----------------|-----------------|-----------------|-------------------|-------------|
| **GET-01** | `/get existing_task_id` (known memory row with output) | Formatted STORED INPUT + STORED OUTPUT chunks | **No** lock row created | Read only | Telegram text + n8n execution IDs (Intake + Worker); no `seo_active_jobs` append | Sandbox preferred; production observability OK if operator accepts |
| **GET-02** | `/get missing_task_id` | `Task not found: missing_task_id` | No lock | No write | **Critical:** record whether message came from **Intake** `Send NOT-FOUND` or **Worker** `Send Telegram Memory Get` (execution graph branch) | **Sandbox required** for branch proof |
| **GET-03** | `/get malformed_task_id` (e.g. `/get`, `/get !!!`, `/get seo bad id`) | Error or NOT-FOUND; no hang | No lock | No write | Telegram response + Intake parse fields | Sandbox |
| **GET-04** | Inject Sheets empty result (mock or test tab) | NOT-FOUND message; no silence | No lock | No write | n8n node output snapshot after `Lookup From Task` and `Lookup Memory Get` | **Sandbox required** |
| **GET-05** | Worker webhook unavailable after Intake true branch | User error notice (desired); currently likely silence | No lock on get | No write | Intake execution error branch absent = **FAIL** baseline | **Sandbox required** (break Worker URL) |
| **GET-06** | Telegram send failure after Worker format | User error or retry (desired); currently likely silence | No lock | No write | Worker execution reaches `Format Memory Get` but Telegram node fails | Sandbox (test chat / mock) |
| **GET-07** | Repeated `/get same_id` ×3 | Same result each time | **No** new lock rows | Read only | Query `seo_active_jobs` before/after — row count unchanged | Sandbox or production (read-only audit) |

**Mapped legacy test IDs:** GET-01 ≈ TC-I11; GET-02 ≈ TC-I12; GET-04 ≈ TR-12; GET-05 ≈ TR-14 / FM-01.

---

### Level 3 — Patch decision gate

| Gate | Criteria | Outcome |
|------|----------|---------|
| **No patch needed** | GET-01 PASS; GET-02 PASS with Worker not-found ≤2s; GET-05/06 acceptable or rare; operator accepts dual-path | Document behavior only (R0) |
| **Documentation-only** | Success + not-found work but dual-path confuses ops | Update `telegram-commands.md` / runbook (R0) |
| **Intake IF patch only** | GET-02 shows Worker handles not-found due to IF true on missing row; GET-01 regression PASS in sandbox | PC-01 Intake: check `output` or add Code node setting `memory_row_found` (R2) |
| **Worker fallback patch only** | GET-02 Intake NOT-FOUND works; GET-04/ zero-item lookup fails | PC-05 guard on `Find Memory Get Row` input (R2) |
| **Both Intake + Worker** | GET-02 fails silence; GET-04 fails; GET-05 fails | PC-01 + PC-05 (+ optional PC-02 ack) (R2) |
| **Stop — request live logs** | Inconclusive GET-02 branch; contradictory production traces | Capture 2–3 n8n execution exports before any edit |

**Hard stop:** Do **not** apply PC-01 to production until GET-01 **and** GET-02 pass in sandbox with evidence records per `safe-workflow-patch-protocol-v1.md` §10.

---

## 10. Patch Proposal Candidate

**Not implemented.** Proposal only — for operator review after Level 2.

### Patch header

| Field | Value |
|-------|-------|
| **patch ID** | `PATCH-2026-07-10-001` (candidate) |
| **title** | PC-01 — Verify and harden `/get` not-found detection |
| **source issue IDs** | IB-01, FM-01, FM-02, FM-05, PC-01 |
| **affected workflows** | Intake (primary); Worker (secondary guard) |
| **affected nodes** | See §11 manifest |
| **affected commands/routes** | `/get`, Worker route `get` |
| **risk level** | **R2 LOW_LIVE_PATCH** (after sandbox GET-01/02 pass) |

### Current behavior (evidence-based)

- Successful `/get existing_task_id`: Intake filtered lookup → Worker get → format → Telegram (**likely working** — operator observation).
- Missing task: Intake IF may route to Worker because condition checks `Boolean($json.task_id)` not memory match; Worker may send not-found **or** fail silently on error paths.
- No immediate user ack on get; handoff/Telegram errors have no fallback message.

### Desired behavior (testable)

1. `/get existing_task_id` — unchanged success output (GET-01 regression).
2. `/get missing_task_id` — user **always** receives explicit NOT-FOUND within bounded time; prefer Intake response without Worker call.
3. `/get` with Sheets/Telegram/handoff errors — user receives explicit error message (stretch; may be separate patch).
4. No lock rows created on any `/get` variant (GET-07).

### Proposed change (narrative — no JSON)

**Option A (preferred after GET-02 proves IF bug):** Insert Code node after `Lookup From Task` setting `memory_row_found = Boolean(output)` (or check row `timestamp` / `row_number`), change `IF From Task Exists` to test `memory_row_found`.

**Option B (minimal):** Change IF leftValue to also require `$json.output` non-empty.

**Option C (Worker-only guard):** Ensure `Find Memory Get Row` runs even when Sheets returns 0 items (PC-05) — does not fix unnecessary Worker invocation.

### No-change boundaries

- Do **not** modify success-path formatting in `Format Memory Get` unless GET-01 regression fails.
- Do **not** add locks to `/get`.
- Do **not** change Worker webhook URL, credentials, or `Route Command` get parsing without separate charter.
- Do **not** change `from:task_id` reuse lock path.

### Risk / impact

| Dimension | Assessment |
|-----------|------------|
| **Risk level** | R2 — wrong IF fix could block all `/get` success |
| **Data impact** | Read-only on `memory`; no lock writes on get |
| **Security impact** | Low — no ACL change; ensure not-found does not leak other users' task existence (**SAFE UNKNOWN** per-chat scope) |

### Required tests

GET-01, GET-02, GET-04, GET-07 (minimum); GET-05 if touching handoff.

### Rollback method

n8n workflow version history or re-import pre-patch sanitized Intake export (`6263815c` era baseline).

### Operator decisions needed

1. Approve Level 2 sandbox clone setup (C path) before patch.
2. Confirm preferred not-found owner: Intake-only vs dual-path OK.
3. Provide 1–2 historical n8n execution IDs for successful `/get` (optional — accelerates Level 1.5).
4. Decide whether GET-02 may run in production with observability only vs strict sandbox.

### SAFE UNKNOWN (blocking certainty)

- Exact `alwaysOutputData` empty-result item shape in production n8n + Sheets node v4.7.
- Whether production already differs from committed sanitized export.
- Per-user vs global memory visibility for task IDs.

---

## 11. Node-Level Manifest Candidate

**No JSON patches.** Manifest rows for potential PC-01 wave.

| Workflow | Node | Type | Current role | Suspected issue | Change type | JSON field touched | Connection risk | Credential impact | Import risk | Rollback note |
|----------|------|------|--------------|-----------------|-------------|-------------------|-----------------|-------------------|-------------|---------------|
| Intake | `Lookup From Task` | googleSheets v4.7 | Filtered memory read for `/get` | `alwaysOutputData` may mask empty result | EDIT_NODE_PARAMETERS (optional) | `alwaysOutputData`, `filtersUI` | Low — downstream IF depends on output shape | No | Low | Restore prior parameters |
| Intake | `IF From Task Exists` | if v2.3 | Branch exists vs not-found | Checks `task_id` not row match (FM-05) | EDIT_NODE_PARAMETERS | `parameters.conditions` | **High** — wrong condition breaks all get | No | Medium | Revert condition to `Boolean($json.task_id)` |
| Intake | *(new)* `Evaluate Memory Row Found` | code v2 | — | Needed to expose boolean row match | ADD_NODE | `parameters.jsCode` | Medium — insert between Lookup and IF | No | Medium | Delete node; reconnect Lookup→IF |
| Intake | `Send NOT-FOUND Message` | telegram v1.2 | Intake not-found Telegram | May be bypassed | None or DOC_ONLY | — | Low | No | Low | N/A |
| Intake | `Build Worker Payload` | code v2 | Build handoff body | Correct for get (`lock:null`) | **No change** | — | — | No | — | — |
| Intake | `Send To Worker` | httpRequest v4.4 | HTTP handoff | No error branch (FM-01) | EDIT_CONNECTION (future) | error output branch | Medium | No | Medium | Remove error branch |
| Worker | `Lookup Memory Get` | googleSheets v4 | Full-tab read | Quota/latency; no filter (PC-04 separate) | **Deferred** unless GET-04 fails | `filtersUI` | Medium | No | Medium | Separate patch wave |
| Worker | `Find Memory Get Row` | code v2 | Filter to target task | Zero input items → skip (FM-03) | EDIT_CODE | `parameters.jsCode` | Medium | No | Low | Restore prior jsCode |
| Worker | `Format Memory Get` | code v2 | Format get response | Not-found text exists | **No change** unless message copy approved | — | Low | No | Low | — |
| Worker | `Send Telegram Memory Get` | telegram v1 | Send get chunks | No error branch (FM-02) | EDIT_CONNECTION (future) | — | Medium | No | Medium | Separate patch |

---

## 12. Recommendation

**Selected: A — No patch proposal execution yet; request live/sandbox test evidence first**

### Rationale

1. **Operator observation** that `/get existing_task_id` worked weighs against assuming global breakage.
2. **Static evidence** shows a **complete success path** and a **Worker not-found fallback** — missing-task users may still get a message today via Worker.
3. **PC-01 IF concern** is real in JSON but **`alwaysOutputData` passthrough is SAFE UNKNOWN** until GET-02 traces a live execution.
4. **Silent failures** (FM-01/02/03) affect error paths on both success and not-found — fixing IF alone does not resolve silence.
5. **`safe-workflow-patch-protocol-v1.md`** mandates sandbox GET-01/02 before R2 apply.

### Suggested operator sequence

1. Review this report.
2. **Option C lite:** Provide 1–2 n8n execution URLs — one successful `/get`, one missing task (if available).
3. If no executions: approve **sandbox clone setup** (`*.sandbox` workflows per protocol §9).
4. Run **GET-01** and **GET-02** first; then re-evaluate patch gate (Level 3).
5. Only if GET-02 proves Intake bypass → promote PC-01 to formal sandbox implementation.

---

## 13. SAFE UNKNOWN

| Topic | Why it matters | Verify via |
|-------|----------------|------------|
| `alwaysOutputData` empty-result item shape | Determines IF true/false on missing task | GET-02 n8n node output |
| Production graph parity with sanitized export | Patch baseline drift | Fresh read-only export |
| Which node sent not-found in operator's past tests | Confirms Intake vs Worker ownership | Execution history |
| `Lookup Memory Get` zero-item behavior | FM-03 silence | GET-04 sandbox |
| Memory row ACL (per-user vs global) | Security of task_id guessing | Operator policy |
| Whether `/get` silence reports were missing-task vs existing-task vs error | Prioritization | Operator interview + logs |

---

## 14. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-get-success-notfound-verification-plan.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 15. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** `a7d19dee1d8f3d32126b36b5941b791defc42710`
- **origin/mars/canonical-post-recovery:** `0d1174a33130530be5cf65ef7ff0062b0c58c548`
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** preserved (Website Factory, fp-0002 workspaces, `.recovery-temp/`, etc.)
- **Commit / push:** not performed

---

## 16. Final Status

**COMPLETE — /get verification plan and conservative patch candidate completed**

---

Awaiting operator review.
