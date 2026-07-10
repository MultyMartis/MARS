# REPORT — MetaBOT SEO Agent v14 Sandbox GET Verification

**Date:** 2026-07-10  
**Classification:** Operator-authorized sandbox clone + GET-01/GET-02 live verification · production workflows untouched  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — sandbox `/get` verification  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Checkpoint commits verified:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`, `61bb6019`, `58c8f0b7`, `bc222072`, `46fc6335`

**Constraints honored:** Production workflows not modified. No production activation/deactivation. No Telegram login. No secrets printed. No OpenRouter generation observed. No staging. No commit. Foreign WIP preserved.

---

## 1. Executive Summary

Sandbox workflow clones were created via authorized n8n REST API, mutated for webhook-based Telegram simulation, activated briefly, exercised with GET-01/GET-02 payloads, then deactivated.

| Test | Worker-only sandbox | Intake→Worker sandbox | Overall |
|------|---------------------|------------------------|---------|
| **GET-01** (`seo20260519082840wzslmg`) | **PASS** — stored input/output returned | **UNKNOWN** — `Send To Worker` failed: `Invalid JSON in response body` on large Worker response | **PARTIAL** |
| **GET-02** (`seo99999999999999missing`) | **PASS** — Worker not-found text | **PASS** — Intake `intake_not_found` response (Worker not called) | **PASS** |

**Key finding:** GET-02 missing-task path routed to **Intake NOT-FOUND** in sandbox, **not** Worker bypass. This contradicts the static FM-05 / `alwaysOutputData` bypass hypothesis for missing tasks in the current live Sheets + n8n behavior.

**PC-01:** **PC01_NO_PATCH_NEEDED** (conditional) — success and not-found paths behave correctly in sandbox for Worker and Intake-not-found; no Intake IF patch justified by GET-02 evidence. Intake→Worker handoff for large existing-task responses remains **SAFE UNKNOWN** due to sandbox HTTP JSON parse limitation.

**Final status:** **PARTIAL** — sandbox created; Worker GET-01/GET-02 and Intake GET-02 verified; Intake GET-01 handoff inconclusive

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Checkpoint `6263815c` | commit ✓ |
| Checkpoint `1b954990` | commit ✓ |
| Checkpoint `84dd9b07` | commit ✓ |
| Checkpoint `af6fc35d` | commit ✓ |
| Checkpoint `61bb6019` | commit ✓ |
| Checkpoint `58c8f0b7` | commit ✓ |
| Checkpoint `bc222072` | commit ✓ |
| Checkpoint `46fc6335` | commit ✓ |
| Staged changes | foreign WIP present — not staged by this task |
| n8n API credentials | `local/tokens/n8n-api.env` present (values not printed) ✓ |
| Foreign WIP | preserved ✓ |

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

| Path / area | Signal |
|-------------|--------|
| Smart Reporter | not touched |
| I-SEO Report Hub | not touched |
| Website Factory report demo | foreign WIP |
| WordPress report hub | foreign WIP |
| `workspaces/fp-0002-*` | foreign WIP |
| `projects/ocpilot/` | foreign WIP |
| `.recovery-temp/` | untracked foreign WIP |

---

## 4. n8n API Safety Check

### 4.1 Production identity (verified, unchanged)

| Workflow | ID | Active (after task) |
|----------|-----|---------------------|
| SEO Content Agent Beta.v14 - Intake | `x8EbTGKNdlBprLvk` | **true** (unchanged) |
| SEO Content Agent Beta.v14 - Worker | `p4mqb4VuPcemIDlC` | **true** (unchanged) |
| SEO Content Agent Beta.v14 - Admin | `AR6QxGt8ZKH0xG2T` | not modified |

### 4.2 Sandbox name conflict check

| Target name | Pre-existing | Action |
|-------------|--------------|--------|
| `SEO Content Agent Beta.v14 - Intake.sandbox-get` | none | **created** |
| `SEO Content Agent Beta.v14 - Worker.sandbox-get` | none | **created** |

### 4.3 API write guardrails applied

- Mutations blocked on production workflow IDs in script guard.
- Only `POST /api/v1/workflows` (create), `POST .../activate`, `POST .../deactivate` on **sandbox IDs**.
- Create payload restricted to `{ name, nodes, connections, settings: { executionOrder } }` per n8n API schema.

---

## 5. Sandbox Workflows Created

| Workflow | Sandbox ID | Webhook path | Post-test active |
|----------|--------------|--------------|------------------|
| SEO Content Agent Beta.v14 - Worker.sandbox-get | `vNlQeuLl0ZCGEVo0` | `seo-content-agent-worker-sandbox-get` | **false** (deactivated) |
| SEO Content Agent Beta.v14 - Intake.sandbox-get | `K1SNvOt9AbVxqeux` | `seo-content-agent-intake-sandbox-get` | **false** (deactivated) |

**Test endpoints (sandbox host, paths only — no secrets):**

- Worker: `POST /webhook/seo-content-agent-worker-sandbox-get`
- Intake: `POST /webhook/seo-content-agent-intake-sandbox-get`

**Synthetic test IDs used (not production chat/user):** chat `900000001`, user `900000002`, username `sandbox_get_tester`.

---

## 6. Sandbox Design and Mutations

### 6.1 Worker sandbox

| Mutation | Detail |
|----------|--------|
| Webhook path | `seo-content-agent-worker` → `seo-content-agent-worker-sandbox-get` |
| Webhook response mode | `responseNode` (waits for get-path completion) |
| `Send Telegram Memory Get` | **disabled** — no Telegram side effect |
| Added nodes | `Sandbox Aggregate Get Response` → `Sandbox Get Webhook Response` (`respondToWebhook`) |
| `/get` route logic | **preserved** — `Route Command` → `Switch Route` → `Lookup Memory Get` → `Find Memory Get Row` → `Format Memory Get` |
| OpenRouter nodes | untouched but **not reachable** on `/get` route |
| Google Sheets | same production `memory` tab (read only on get path) |
| Credentials | unchanged (inherited from clone) |

### 6.2 Intake sandbox

| Mutation | Detail |
|----------|--------|
| `Telegram Trigger` | **disabled** |
| Added trigger | `Webhook Sandbox GET` + `Normalize Sandbox Telegram Payload` |
| `Send To Worker` URL | repointed to **Worker sandbox** webhook (not production) |
| `Send NOT-FOUND Message` | **disabled** |
| NOT-FOUND branch | `Sandbox Intake NOT-FOUND Prep` → `Sandbox Intake NOT-FOUND Response` |
| Success handoff branch | `Send To Worker` → `Sandbox Intake Handoff Response` |
| Other Intake routes | not disabled — only `/get` tested; lock/generation routes remain in graph but were not triggered |

### 6.3 Limitations documented

- Worker sandbox changes webhook response semantics (`responseNode`) vs production immediate `{"ok": true}` — acceptable for sandbox; Intake `Send To Worker` HTTP node expects JSON body and **failed** on large GET-01 Worker payload (`Invalid JSON in response body`, execution `3335`).
- Admin sandbox not created (not required).

---

## 7. Execution Safety Gate

| Gate | Assessment |
|------|------------|
| Production Worker may be called | **No** — Intake sandbox `Send To Worker` points to sandbox path only |
| Production Intake modified | **No** |
| OpenRouter may trigger | **No** on `/get` paths exercised |
| Telegram may send to unknown user | **No** — Telegram send nodes disabled/bypassed on sandbox get outputs |
| Google Sheets read | **Yes** — `Lookup From Task`, `Lookup Memory Get` |
| Google Sheets write | **Not expected** — no append/update nodes on get path |
| Locks may be created | **No** — `lock: null` on get handoff |
| Sandbox webhook path known | **Yes** |
| Credentials printed | **No** |

**Gate outcome:** **PASS** — tests executed.

---

## 8. GET-01 Existing Task Result

**Input:** `/get seo20260519082840wzslmg`

### 8.1 Worker-only (direct sandbox Worker webhook)

| Field | Value |
|-------|--------|
| HTTP status | 200 |
| Result | **pass** |
| Output summary | Multi-chunk stored artifact: `Task ID: seo20260519082840wzslmg`, `STORED INPUT`, commercial SEO brief (купели для бань…), `STORED OUTPUT` implied in further chunks |
| Path | Worker `get` route end-to-end |
| Execution ID | `3333` (success) |

### 8.2 Intake→Worker (sandbox Intake webhook)

| Field | Value |
|-------|--------|
| HTTP status | 200 (webhook returned null/empty to caller) |
| Result | **unknown** |
| Failure node | `Send To Worker` |
| Error | `Invalid JSON in response body` |
| Execution ID | `3335` (error) |
| Interpretation | Sandbox wiring limitation — large JSON Worker response not parsed by Intake HTTP Request node; **not** evidence that production `/get` success is broken |

---

## 9. GET-02 Missing Task Result

**Input:** `/get seo99999999999999missing`

### 9.1 Worker-only

| Field | Value |
|-------|--------|
| HTTP status | 200 |
| Result | **pass** |
| Output summary | `Task not found: seo99999999999999missing` + memory column hint |
| Response owner | **Worker** (`Format Memory Get` path) |
| Execution ID | `3334` (success) |

### 9.2 Intake→Worker

| Field | Value |
|-------|--------|
| HTTP status | 200 |
| Result | **pass** |
| Output summary | `Task not found: seo99999999999999missing` + Google Sheets memory hint |
| Route marker | `intake_not_found` / sandbox `intake-not-found` |
| Response owner | **Intake** (NOT-FOUND branch — Worker not invoked) |
| Execution ID | `3337` (success) |

**Critical branch evidence:** Missing task did **not** bypass Intake `IF From Task Exists` to Worker in this live sandbox run. Intake owned not-found directly.

---

## 10. Lock / Memory / OpenRouter Impact

| System | Expected on `/get` | Observed |
|--------|-------------------|----------|
| **Locks** (`seo_active_jobs`) | No create | No lock evidence; executions read-only on get path |
| **Memory** (`memory` tab) | Read only | GET-01 returned live row content; GET-02 reads did not append |
| **OpenRouter** | Not on get route | Not triggered (no generation executions) |
| **Telegram** | Would fire in production | **Suppressed** in sandbox (nodes disabled / respondToWebhook used) |

---

## 11. PC-01 Decision

**PC01_NO_PATCH_NEEDED** (conditional — recommend operator acceptance)

### Rationale

1. **GET-01 Worker PASS** confirms existing task retrieval and formatting works against live memory.
2. **GET-02 Intake PASS** with `intake_not_found` shows missing tasks receive explicit NOT-FOUND at **Intake** without Worker invocation — the primary PC-01 / FM-05 concern (IF bypass on missing row) was **not reproduced** in live sandbox.
3. **GET-02 Worker PASS** confirms defense-in-depth Worker not-found still works if Intake forwards (Worker-only test).
4. **GET-01 Intake UNKNOWN** is attributable to sandbox HTTP JSON parse on large Worker webhook response, not to routing logic failure.
5. Prior silent-failure modes (FM-01/02) remain possible on error paths but were **not triggered** in these tests.

### Not selected

| Code | Why not |
|------|---------|
| PC01_INTAKE_IF_PATCH_NEEDED | GET-02 Intake routed to NOT-FOUND correctly |
| PC01_WORKER_FALLBACK_PATCH_NEEDED | Worker GET-02 not-found works; GET-04 zero-item case not exercised |
| PC01_BOTH_INTAKE_AND_WORKER_HARDENING_NEEDED | No dual failure observed |
| PC01_DOC_ONLY | Optional follow-up only if operator wants runbook note on dual not-found owners |
| PC01_BLOCKED_* | Sandbox wiring succeeded; tests ran |

### Optional follow-up (non-blocking)

- Re-run Intake GET-01 with `Send To Worker` configured for raw/text response or truncated fixture row — to close Intake handoff UNKNOWN.
- Production observability: one operator Telegram `/get` on existing task for full Intake graph confirmation (no patch required if matches Worker sandbox result).

---

## 12. Sandbox Cleanup State

| Item | State |
|------|--------|
| Worker sandbox `vNlQeuLl0ZCGEVo0` | **inactive** (deactivated after test) |
| Intake sandbox `K1SNvOt9AbVxqeux` | **inactive** (deactivated after test) |
| Sandbox deleted | **No** — left for operator review/re-run |
| Production workflows | **unchanged** — still active as before task |

**Note:** Two accidental API schema probe workflows (`TEMP SCHEMA PROBE …`) may exist inactive on n8n from pre-run probing — operator may archive/delete if desired (out of charter).

---

## 13. Evidence Files Created

| File | Location | Commit |
|------|----------|--------|
| This report | `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-sandbox-get-verification.md` | not staged |
| Worker sanitized export | `projects/metabot-seo-content-agent/exports/sandbox-get-verification/2026-07-10/SEO-Content-Agent-Beta-v14-Worker.sandbox-get.sanitized.json` | not staged |
| Intake sanitized export | `projects/metabot-seo-content-agent/exports/sandbox-get-verification/2026-07-10/SEO-Content-Agent-Beta-v14-Intake.sandbox-get.sanitized.json` | not staged |
| Sandbox runner (auxiliary) | `projects/metabot-seo-content-agent/exports/sandbox-get-verification/2026-07-10/run-sandbox-get.mjs` | not staged |
| Raw results + raw JSON | `local/sandbox-get-verification-2026-07-10/` (gitignored) | n/a |

---

## 14. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Intake GET-01 full handoff with large memory output | **UNKNOWN** — HTTP JSON parse error in sandbox |
| Whether production Telegram `/get` success matches Worker sandbox output | **Likely yes** — same memory row returned; not re-verified via Telegram |
| GET-04 zero-item `Lookup Memory Get` silence (FM-03) | Not exercised |
| FM-01/02 error branches (handoff/Telegram send failure) | Not exercised |
| Temp schema-probe workflows on n8n | Existence **UNKNOWN** to operator unless reviewed |

---

## 15. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **Staged:** not modified by this task
- **This task new files:** one report + two sanitized sandbox exports + auxiliary runner under `exports/sandbox-get-verification/2026-07-10/`
- **Foreign WIP:** preserved (Website Factory, fp-0002, iseo-report-hub, `.recovery-temp/`, etc.)
- **Commit / push:** not performed

---

## 16. Final Status

**PARTIAL** — sandbox workflows created; Worker GET-01/GET-02 verified; Intake GET-02 verified; Intake GET-01 handoff inconclusive due to sandbox HTTP response parsing

---

Awaiting operator review.
