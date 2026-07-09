# MetaBOT Developer — Safe Workflow Patch Protocol v1

**Status:** documented protocol — human-operated gate before live n8n patching  
**Applies to:** MetaBOT SEO Content Agent (`@seo_content_agent_bot`) — Intake / Worker / Admin  
**Classification:** MetaBOT Developer discipline · **not** automated enforcement  
**Checkpoint anchor:** `58c8f0b7` (/get + lock lifecycle audit recommends this protocol)  
**Related:** [n8n-project-development-rules-v1.md](../n8n-project-development-rules-v1.md) · [metabot-developer-concept-v1.md](../metabot-developer-concept-v1.md) · [n8n-workflow-json-grammar-v1.md](n8n-workflow-json-grammar-v1.md) · [n8n-import-safe-generation-rules-v1.md](n8n-import-safe-generation-rules-v1.md)

**Not:** live n8n API automation, CI policy, or permission to skip operator gates.

---

## 1. Protocol purpose

This protocol defines how MetaBOT Developer work moves from **evidence → patch proposal → sandbox clone → tests → approval → live apply → rollback**, without uncontrolled production edits to MetaBOT SEO Agent n8n workflows.

No live n8n graph change may proceed unless it follows this lifecycle. MARS sessions **stop** at prepared artifacts and operator instructions — they do **not** self-apply patches.

---

## 2. Protocol scope

### 2.1 In scope — workflows

| Workflow | Live name (v14 reference) |
|----------|---------------------------|
| **Intake** | `SEO Content Agent Beta.v14 - Intake` |
| **Worker** | `SEO Content Agent Beta.v14 - Worker` |
| **Admin** | `SEO Content Agent Beta.v14 - Admin` |

### 2.2 In scope — change types

- n8n node additions, edits, disables, deletes
- Code node logic changes
- connection / branch changes (IF, Switch, error paths)
- prompt payload changes (OpenRouter HTTP Request bodies)
- model configuration changes (per-stage model IDs, temperature)
- Google Sheets schema or tab changes when required by a patch
- Telegram UX message text and routing
- error-handling branches
- sandbox clone creation and disposable test graphs
- rollback planning and evidence capture

### 2.3 Out of scope

| System / lane | Status |
|---------------|--------|
| Smart Reporter | **OUT_OF_SCOPE** |
| I-SEO Report Hub | **OUT_OF_SCOPE** |
| Website Factory report demo | **OUT_OF_SCOPE** |
| WordPress report hub | **OUT_OF_SCOPE** |
| Unrelated MARS systems (MIG, ORCA, OPS, ATLAS) | **OUT_OF_SCOPE** unless separately chartered |
| File Export workflow (4th workflow) | **PLANNED** — not current patch target without evidence |
| Credential rotation, bot token changes | Separate operator charter only |

---

## 3. Authority hierarchy

When sources conflict, resolve in this order:

| Rank | Source | Role |
|------|--------|------|
| **1** | **Live n8n production** | Execution truth — behavior, credentials, webhooks, active graphs |
| **2** | **Fresh read-only export** | Patch baseline — operator or chartered exporter; not committed until sanitized |
| **3** | **Sanitized export committed to repo** | Evidence baseline — `exports/live-v14-evidence/` and successors |
| **4** | **v14 architecture review** | Synthesized I/W/A behavior — `REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md` |
| **5** | **Issue backlog / test matrix** | IB-xx / TC-xx / TR-xx IDs — `REPORT-metabot-seo-agent-v14-issue-backlog-and-test-matrix.md` |
| **6** | **/get + lock lifecycle audit** | Node-level paths for retrieval, reuse, locks — `REPORT-metabot-seo-agent-v14-get-lock-lifecycle-deep-audit.md` |
| **7** | **Legacy v13 docs** | Semantic reference only — `mega-map.md`, `OPERATIONAL-INDEX.md` — **drift risk** |

**Rule:** No patch may rely only on memory, chat paraphrase, or old docs. If live baseline is unknown, **STOP** — refresh evidence (Stage 2–3) before proposal.

---

## 4. Patch lifecycle

Each stage lists: **purpose**, **allowed actions**, **forbidden actions**, **required evidence**, **stop conditions**.

### Stage 1 — Problem selection

| | |
|---|---|
| **Purpose** | Choose one bounded issue or patch candidate (e.g. IB-01, PC-01) with repo evidence link. |
| **Allowed** | Read issues, audits, test matrix; rank by P0/P1; single-issue focus per patch wave. |
| **Forbidden** | Multi-issue “mega patch”; production edits; scope creep into out-of-scope lanes. |
| **Required evidence** | Issue ID(s); affected workflow(s); user/ops impact statement from backlog or audit. |
| **Stop conditions** | Issue not evidenced in repo; duplicate of in-flight patch; operator declares freeze. |

### Stage 2 — Evidence refresh decision

| | |
|---|---|
| **Purpose** | Decide whether committed export is fresh enough to patch against. |
| **Allowed** | Compare export date vs last production change; note drift; schedule fresh read-only export. |
| **Forbidden** | Assuming parity without operator attestation; patching from `workflow-sanitized-legacy.json` alone. |
| **Required evidence** | Export date; parity level: **VERIFIED** / **PARTIAL** / **UNKNOWN**; list of known drift. |
| **Stop conditions** | **UNKNOWN** parity + production-impacting patch → must refresh baseline (Stage 3). |

### Stage 3 — Baseline export

| | |
|---|---|
| **Purpose** | Capture read-only workflow JSON for affected graph(s) before any edit. |
| **Allowed** | Operator n8n export to `raw/` (gitignored) or Storage; run sanitizer; commit only sanitized pack when chartered. |
| **Forbidden** | Committing raw secrets; `git add .`; staging raw exports; MARS agent calling n8n API without charter. |
| **Required evidence** | Timestamped export per workflow; sanitizer report; workflow name + id (operator record). |
| **Stop conditions** | Export incomplete; sanitizer flags unsafe-to-commit; cannot access live n8n. |

### Stage 4 — Patch proposal

| | |
|---|---|
| **Purpose** | Author formal proposal using §5 structure — one patch ID, explicit boundaries. |
| **Allowed** | Doc-only proposal in MARS; link source issues; define desired vs current behavior. |
| **Forbidden** | Implementing in production; omitting rollback or test IDs; credential changes without separate approval. |
| **Required evidence** | Completed proposal template (§5); risk level (§8). |
| **Stop conditions** | Proposal incomplete; risk **R4 BLOCKED**; operator rejects scope. |

### Stage 5 — Node-level manifest

| | |
|---|---|
| **Purpose** | Enumerate every node/connection/field touched — no implicit edits. |
| **Allowed** | One manifest row per change; reference grammar v1 and node catalog v14. |
| **Forbidden** | “Replace whole workflow”; manifest missing connection diffs; undeclared credential touches. |
| **Required evidence** | Completed manifest (§6) for all non-DOC_ONLY changes. |
| **Stop conditions** | Manifest empty for R2+ patches; import risk undocumented. |

### Stage 6 — Risk classification

| | |
|---|---|
| **Purpose** | Assign R0–R4 (§8); determine approval depth and sandbox requirement. |
| **Allowed** | Escalate risk upward when uncertain; document SAFE UNKNOWNs. |
| **Forbidden** | Downgrading risk to skip sandbox; R3/R4 without operator review. |
| **Required evidence** | Risk level + rationale; security and data impact fields in proposal. |
| **Stop conditions** | **R4 BLOCKED** — do not proceed to implementation. |

### Stage 7 — Sandbox clone strategy

| | |
|---|---|
| **Purpose** | Plan disposable clone(s) per §10 — isolated from production webhooks and client traffic. |
| **Allowed** | Name clones with `.sandbox` suffix; document test webhook paths; test sheet rows/tabs. |
| **Forbidden** | Pointing sandbox at production webhook URLs; activating sandbox on production Telegram bot. |
| **Required evidence** | Clone naming list; test URL plan; Sheets/Telegram isolation notes. |
| **Stop conditions** | Cannot isolate webhooks or Sheets — **SAFE UNKNOWN** until operator verifies n8n UI mechanics. |

### Stage 8 — Test plan selection

| | |
|---|---|
| **Purpose** | Map patch to test matrix IDs (TC-xx, TR-xx) from issue backlog report. |
| **Allowed** | Minimum: happy path + regression + failure injection for changed route. |
| **Forbidden** | Production-only testing for R2+; skipping lock/memory tests when locks touched. |
| **Required evidence** | List of expected test IDs with pass criteria; environment = sandbox. |
| **Stop conditions** | No applicable tests for behavior change — add TR-xx case or STOP. |

### Stage 9 — Operator approval gate (planning)

| | |
|---|---|
| **Purpose** | Human sign-off on proposal + manifest + risk + test plan **before** sandbox implementation. |
| **Allowed** | Operator: approve / revise / reject / defer. |
| **Forbidden** | MARS or agent self-approval; proceeding on “implicit OK”. |
| **Required evidence** | Dated approval note (chat, ticket, or report section) referencing patch ID. |
| **Stop conditions** | No approval; approval conditional on unresolved SAFE UNKNOWN blocking the patch. |

### Stage 10 — Sandbox implementation

| | |
|---|---|
| **Purpose** | Apply node-level changes only on sandbox clone(s). |
| **Allowed** | n8n UI edits; import sanitized JSON fragments; Code node edits per manifest. |
| **Forbidden** | Production workflow edit; whole-workflow replace when node-level suffices; credential edits unless separately authorized. |
| **Required evidence** | Post-edit sandbox export (raw local); manifest tick-off per row. |
| **Stop conditions** | Import failure; graph validation errors; drift from manifest. |

### Stage 11 — Sandbox test execution

| | |
|---|---|
| **Purpose** | Run selected tests (§11 evidence protocol) in sandbox only. |
| **Allowed** | Manual Telegram test bot; webhook POST with fixture payloads; Sheets test rows. |
| **Forbidden** | Production `@seo_content_agent_bot` client traffic; destructive Sheets ops on production tabs. |
| **Required evidence** | Per-test evidence records (§11); pass/fail/unknown per test ID. |
| **Stop conditions** | Any P0 test fail; unexplained silent failure; lock orphan in sandbox. |

### Stage 12 — Before/after export comparison

| | |
|---|---|
| **Purpose** | Prove diff matches manifest — no surprise nodes or connections. |
| **Allowed** | JSON diff (sanitized); connection-key diff; grammar validation script. |
| **Forbidden** | Declaring “done” without diff review; hiding connection changes. |
| **Required evidence** | Diff summary tied to manifest rows; omitted fields per import-safe rules. |
| **Stop conditions** | Diff exceeds manifest scope → return to Stage 4 or reject patch. |

### Stage 13 — Production approval gate (apply)

| | |
|---|---|
| **Purpose** | Explicit operator authorization to touch live Intake/Worker/Admin. |
| **Allowed** | Apply only manifest-approved changes; one patch wave at a time when possible. |
| **Forbidden** | Apply during uncommunicated SEO user peak without ops notice; batch unrelated patches. |
| **Required evidence** | Sandbox test summary attached; rollback plan (Stage 16) confirmed. |
| **Stop conditions** | Failed sandbox matrix; operator STOP; incident freeze. |

### Stage 14 — Live apply

| | |
|---|---|
| **Purpose** | Operator applies approved node-level patch to production n8n. |
| **Allowed** | n8n UI save; selective import; version note in operator log. |
| **Forbidden** | Agent API apply; deactivating all three workflows without plan; webhook path change without separate approval. |
| **Required evidence** | Pre-apply production export snapshot (raw, local); apply timestamp; operator id. |
| **Stop conditions** | Import error; unexpected node drop; credential rebind failure. |

### Stage 15 — Production smoke test

| | |
|---|---|
| **Purpose** | Minimal live verification immediately after apply. |
| **Allowed** | Operator-run TC cases for changed route only; `/health` if Sheets touched. |
| **Forbidden** | Full regression suite on production without charter; load testing on live bot. |
| **Required evidence** | Smoke test record (§11); n8n execution id(s). |
| **Stop conditions** | Smoke fail → execute rollback (Stage 16) before further use. |

### Stage 16 — Rollback plan

| | |
|---|---|
| **Purpose** | Define reversibility **before** Stage 14; execute if triggered. |
| **Allowed** | n8n version history; prior export re-import; node-level reverse patch. |
| **Forbidden** | Rollback without evidence; `git reset --hard`; destructive Sheets cleanup without charter. |
| **Required evidence** | Rollback method in proposal; post-rollback smoke test if executed. |
| **Stop conditions** | No rollback source available → **R4** — do not apply. |

### Stage 17 — Evidence persistence

| | |
|---|---|
| **Purpose** | Retain audit trail for survivability and doc sync. |
| **Allowed** | MetaBOT Evidence Pack; sanitized post-patch export to `exports/` when chartered; operator Storage. |
| **Forbidden** | Committing raw exports; secrets in repo; staging unrelated foreign WIP. |
| **Required evidence** | Evidence pack per [n8n-project-development-rules-v1.md](../n8n-project-development-rules-v1.md) §15. |
| **Stop conditions** | Evidence pack incomplete for R2+ — flag PARTIAL in closeout report. |

### Stage 18 — Final documentation sync

| | |
|---|---|
| **Purpose** | Update product docs only when behavior change is verified — separate doc charter if needed. |
| **Allowed** | `known-issues.md`, `telegram-commands.md`, workflow docs — **only** with operator approval for doc wave. |
| **Forbidden** | This protocol does not authorize broad doc rewrites in the same task as patch apply unless chartered. |
| **Required evidence** | List of doc files updated or explicit “docs deferred” with issue IDs. |
| **Stop conditions** | Behavior changed but docs not scheduled — record IB-18 drift note. |

---

## 5. Patch proposal format

Every patch **must** use this structure (Markdown or equivalent operator ticket):

```markdown
## Patch proposal

| Field | Value |
|-------|-------|
| **patch ID** | `PATCH-YYYY-MM-DD-NNN` (e.g. PATCH-2026-07-15-001) |
| **title** | Short imperative title |
| **source issue IDs** | IB-xx, PC-xx, FM-xx |
| **affected workflow(s)** | Intake / Worker / Admin |
| **affected node(s)** | Exact node names from live export |
| **affected commands/routes** | e.g. `/get`, `get` route, lock path |
| **current behavior** | Factual — cite evidence export/audit |
| **desired behavior** | Testable outcome |
| **proposed change** | Narrative — no full JSON in proposal unless chartered |
| **no-change boundaries** | Nodes/routes explicitly untouched |
| **risk level** | R0–R4 (§8) |
| **security impact** | none / low / medium / high + note |
| **data impact** | Sheets rows, memory, locks, PII |
| **expected test IDs** | TC-xx, TR-xx list |
| **rollback method** | n8n history / prior export / reverse manifest |
| **required operator decisions** | Bullet list |
| **safe unknowns** | Items blocking certainty |
```

**Rule:** One primary patch ID per production apply wave. Related doc-only updates may share an ID only if **R0 DOC_ONLY**.

---

## 6. Node-level manifest format

One table row (or YAML object) per atomic change:

| Field | Required | Description |
|-------|----------|-------------|
| **workflow name** | yes | e.g. `SEO Content Agent Beta.v14 - Intake` |
| **workflow ID** | if known | Operator record — may stay out of repo |
| **node name** | yes | Connection key — exact match |
| **node type** | yes | e.g. `n8n-nodes-base.if` |
| **node typeVersion** | yes | From [n8n-node-type-catalog-v14.md](n8n-node-type-catalog-v14.md) |
| **current role** | yes | One sentence |
| **change type** | yes | See enum below |
| **expected JSON field touched** | yes | e.g. `parameters.conditions`, `parameters.jsCode` |
| **expected connection diff** | yes | Source → target branch changes, or `none` |
| **credentials touched?** | yes | **Default: no** — `yes` only with separate credential charter |
| **secrets touched?** | yes | **Always no** for repo artifacts |
| **import risk** | yes | low / medium / high + note |
| **rollback note** | yes | How to reverse this row |

**Change type enum:**

| Value | Meaning |
|-------|---------|
| `ADD_NODE` | New node + connections |
| `EDIT_NODE_PARAMETERS` | Non-code parameter edit |
| `EDIT_CODE` | Code node `jsCode` change |
| `EDIT_CONNECTION` | Wiring only |
| `DELETE_NODE` | Remove node — **high scrutiny** |
| `DISABLE_NODE` | `disabled: true` — prefer over delete when possible |
| `SHEET_SCHEMA_CHANGE` | Tab/column/filter schema |
| `DOC_ONLY` | No n8n change |

---

## 7. Risk levels

| Level | Name | Sandbox required | Production apply | Operator approval |
|-------|------|------------------|------------------|-------------------|
| **R0** | DOC_ONLY | no | no | notify only |
| **R1** | SANDBOX_ONLY | yes | no | planning gate |
| **R2** | LOW_LIVE_PATCH | yes | yes, after smoke | planning + apply gates |
| **R3** | HIGH_LIVE_PATCH | yes + extended TR | yes, maintenance window | explicit + rollback ready |
| **R4** | BLOCKED | — | **forbidden** | STOP |

### Examples

| Example change | Typical level | Notes |
|----------------|---------------|-------|
| Doc sync (`known-issues`, runbook) | **R0** | No n8n edit |
| Telegram copy update (message text node) | **R2** | User-visible; sandbox Telegram |
| Fix `IF From Task Exists` (PC-01) | **R2** | Routing logic; TC-I12 |
| Filtered memory lookup (PC-04) | **R2** | Sheets read pattern; TC-W04 |
| Promote `task_id` on run close (PC-07) | **R2** | Jobs sheet write; TR-01, IB-03 |
| `Send To Worker` error branch + lock compensation (PC-03) | **R3** | Orphan lock risk; TR-14 |
| Code node rewrite (large `Route Command`) | **R3** | Blast radius |
| Sheets schema change (new column, tab rename) | **R3** | Data migration risk |
| Webhook path change (`seo-content-agent-worker`) | **R4** | Separate charter — breaks Intake handoff |
| Credential change (Telegram, OpenRouter, Sheets OAuth) | **R4** | Separate security charter |

**Escalation:** When in doubt, assign **higher** risk.

---

## 8. Mandatory safety rules

Hard rules — no exceptions without explicit operator charter:

1. **No live edit without operator approval** (Stages 9 and 13).
2. **No credential edits** unless separately authorized — manifest `credentials touched?` must stay `no` otherwise.
3. **No changing production webhook URLs** (`seo-content-agent-worker`, `seo-content-agent-admin`) without separate approval.
4. **No replacing whole workflow JSON** when node-level patch is sufficient.
5. **No raw secrets in repo** — sanitize before any commit.
6. **No staging raw exports** — `raw/` is gitignored local only.
7. **No `git add .` / `git add -A`** — selective staging per MARS contract.
8. **No patching from stale evidence** if live baseline is unknown — refresh export first.
9. **No destructive cleanup** (`git clean`, `reset --hard`, `Remove-Item -Recurse`, broad restore) during patch work.
10. **Preserve foreign WIP** — unrelated paths are OUT_OF_SCOPE_PRESERVED.
11. **Always create rollback notes** before production apply.
12. **Always capture before/after evidence** — Stage 3 and Stage 12 minimum.
13. **No live n8n / Telegram / OpenRouter / Google Sheets API calls** from MARS agents unless task explicitly charters and operator approves.
14. **Sandbox must not send production client-facing messages** or write production Sheets rows without isolation plan.
15. **Import-safe generation** — follow [n8n-import-safe-generation-rules-v1.md](n8n-import-safe-generation-rules-v1.md) (omit `webhookId`, `pinData`, `activeVersion`, secrets).

---

## 9. Sandbox clone protocol

### 9.1 Naming

Clone production workflows with **`.sandbox`** suffix:

| Production | Sandbox clone name |
|------------|-------------------|
| `SEO Content Agent Beta.v14 - Intake` | `SEO Content Agent Beta.v14 - Intake.sandbox` |
| `SEO Content Agent Beta.v14 - Worker` | `SEO Content Agent Beta.v14 - Worker.sandbox` |
| `SEO Content Agent Beta.v14 - Admin` | `SEO Content Agent Beta.v14 - Admin.sandbox` |

### 9.2 Isolation requirements

| Surface | Requirement |
|---------|-------------|
| **Webhooks** | Sandbox must **not** replace production webhook paths. Use test paths (e.g. `seo-content-agent-worker-sandbox`) or manual execution / pinned test payloads. |
| **Telegram** | Prefer test bot or test chat/user; no production SEO specialist traffic. |
| **Google Sheets** | Test tabs or clearly marked test rows; never delete production memory/jobs data from sandbox tests. |
| **OpenRouter** | Sandbox may use same credential — operator controls cost; prefer short fixtures for R1. |
| **Activation** | Sandbox workflows stay **inactive** on production triggers unless operator explicitly tests trigger path in isolated bot. |

### 9.3 Lifecycle

- Sandbox clones are **disposable** — may be deleted after evidence captured.
- Patches proven in sandbox are re-applied to production via manifest — **not** by renaming sandbox to production.
- **No production activation** of sandbox graph without Stage 13 approval.

### 9.4 SAFE UNKNOWN — n8n mechanics

| Topic | Status | Verify later |
|-------|--------|--------------|
| Exact n8n UI “Duplicate workflow” vs API clone | **SAFE UNKNOWN** | Operator documents steps once |
| Whether duplicate copies `webhookId` | **SAFE UNKNOWN** | Strip/rebind before any sandbox activation |
| n8n workflow version history retention policy | **SAFE UNKNOWN** | Confirm with operator backup cadence |
| Cross-workflow `Execute Workflow` vs HTTP handoff in clone | **SAFE UNKNOWN** | v14 uses HTTP POST handoff per architecture review |

---

## 10. Test evidence protocol

Each test run produces one evidence record:

| Field | Required | Description |
|-------|----------|-------------|
| **test ID** | yes | From test matrix — TC-xx, TR-xx |
| **environment** | yes | `sandbox` / `production-smoke` |
| **workflow execution ID** | if available | n8n execution URL or id |
| **input payload summary** | yes | Command or webhook body — no secrets |
| **expected behavior** | yes | From matrix |
| **actual behavior** | yes | Factual outcome |
| **screenshots/log snippets** | when useful | Telegram, n8n node output |
| **Sheets before/after row summary** | when Sheets touched | lock_key, task_id, status — redacted |
| **Telegram output** | when applicable | Text excerpt or screenshot |
| **pass/fail/unknown** | yes | **unknown** requires follow-up TR case |
| **regression notes** | if fail | Related IB-xx |
| **rollback readiness** | yes | confirm pre-apply export exists if production-smoke |

Store evidence: operator ticket, `reports/` charter, or `X:\AI MARS STORAGE` per task — not raw credentials.

---

## 11. Rollback protocol

### 11.1 Rollback sources (preference order)

1. **n8n workflow version history** — fastest if retention confirmed.
2. **Prior sanitized export** — Stage 3 baseline re-import.
3. **Node-level reverse patch** — manifest rows applied in reverse (connection restore).
4. **Disabled sandbox clone** — reference only; not production rollback by itself.

### 11.2 Rollback triggers

Execute rollback when any of:

- production Telegram send failure on smoke path
- lock orphan spike after patch (active rows without completion)
- wrong user output / data leak to wrong chat
- memory corruption or destructive Sheets write
- secret exposure risk (logged token, committed key)
- unexpected workflow activation or webhook collision
- operator **STOP**

### 11.3 Rollback evidence

After rollback, capture:

- timestamp (UTC)
- operator decision and trigger
- workflow name/id and version/export id restored
- post-rollback smoke test (minimal TC for affected route)
- incident note for IB backlog if new failure mode

---

## 12. First patch wave guardrails

Based on `/get` + lock lifecycle audit (`58c8f0b7`). **This stage is planning only** — no n8n JSON in this protocol.

Recommended wave order after protocol adoption: **PC-01 → PC-04 → PC-07 → PC-03**.

### PC-01 — Fix `IF From Task Exists`

| | |
|---|---|
| **Why it matters** | Condition checks `Boolean($json.task_id)` not memory row match; with `Lookup From Task.alwaysOutputData=true`, missing tasks may route to Worker instead of Intake `Send NOT-FOUND` (FM-05, IB-01). |
| **Allowed at this stage** | Patch proposal + manifest for `IF From Task Exists` (and optionally `Lookup From Task`); evidence review of `alwaysOutputData` passthrough — **SAFE UNKNOWN** until live trace. |
| **Required sandbox tests** | **TC-I12** (`/get seoMISSING`); **TC-I11** regression (existing task). |
| **Production risks** | Low logic change; wrong fix could block all `/get` success paths. |
| **Data safety** | Read-only on memory for get; no lock rows. |
| **Operator approval** | **Required** — R2 LOW_LIVE_PATCH. |

### PC-04 — Filtered memory lookup (Worker get)

| | |
|---|---|
| **Why it matters** | `Lookup Memory Get` reads full `memory` tab; quota/latency and silent failure risk (FM-03, IB-05). |
| **Allowed at this stage** | Manifest for `Lookup Memory Get` filter + downstream `Find Memory Get Row` guards. |
| **Required sandbox tests** | **TC-W04** (Worker `get` direct webhook); **TR-12** (Sheets failure inject). |
| **Production risks** | Medium — wrong filter breaks all `/get`; column name drift. |
| **Data safety** | Read-only; confirm column map with operator (PC-13 schema sample). |
| **Operator approval** | **Required** — R2. |

### PC-07 — Promote `task_id` on run close

| | |
|---|---|
| **Why it matters** | `/run` path leaves `seo_active_jobs.task_id` as `pending` while memory has real id (FM-14, IB-03). |
| **Allowed at this stage** | Manifest for `Close Lock Before Sending` field mapping; compare with `Close Single Lock Before Sending` pattern. |
| **Required sandbox tests** | **TR-01**; **TC-I05** `/run` success; **TC-I08** `/locks` display. |
| **Production risks** | Low if mirroring proven single-path promotion; wrong mapping corrupts jobs sheet. |
| **Data safety** | Updates existing lock rows — backup or test row first in sandbox. |
| **Operator approval** | **Required** — R2. |

### PC-03 — `Send To Worker` error branch + lock compensation

| | |
|---|---|
| **Why it matters** | After `Create Lock Row`, HTTP handoff failure leaves orphan `active` lock (FM-07, IB-04). |
| **Allowed at this stage** | Proposal for error branch on `Send To Worker` + compensation node (cancel lock or delete row); HTTP error taxonomy from logs — partial **SAFE UNKNOWN**. |
| **Required sandbox tests** | **TR-14** (Worker unreachable post-lock); **TC-I04** regression; busy/lock **TC-I06**. |
| **Production risks** | **High** — wrong compensation may delete valid locks or double-close. |
| **Data safety** | Writes `seo_active_jobs` — race with concurrent commands. |
| **Operator approval** | **Required** — R3 HIGH_LIVE_PATCH; apply after PC-01/04/07 unless operator reprioritizes. |

---

## 13. Protocol compliance checklist

Before any production apply, operator confirms:

- [ ] Patch ID and proposal (§5) complete
- [ ] Node manifest (§6) matches intended diff
- [ ] Risk level assigned and gates satisfied
- [ ] Sandbox clones named per §9
- [ ] All expected test IDs executed with evidence (§10)
- [ ] Before/after diff reviewed (Stage 12)
- [ ] Rollback source confirmed (§11)
- [ ] Stage 9 and Stage 13 approvals recorded
- [ ] No credential or production webhook path change without separate charter
- [ ] Foreign WIP untouched; no broad git staging

---

## 14. Relationship to other docs

| Document | Relationship |
|----------|--------------|
| [n8n-project-development-rules-v1.md](../n8n-project-development-rules-v1.md) | General discipline — this protocol **gates** SEO Agent v14 patches |
| [metabot-developer-concept-v1.md](../metabot-developer-concept-v1.md) | Role definition — human approval gates |
| [n8n-workflow-json-grammar-v1.md](n8n-workflow-json-grammar-v1.md) | JSON shape for manifests and diffs |
| [n8n-import-safe-generation-rules-v1.md](n8n-import-safe-generation-rules-v1.md) | Synthetic JSON and import hygiene |
| Issue backlog report | IB-xx / TC-xx / TR-xx source |
| Get/lock audit report | PC-xx candidates and failure modes |

**IB-20** (Safe workflow patch protocol) is satisfied by **this document** for v1. Execution of PC-01–07 remains **forbidden** until operator adopts this protocol and charters each patch wave.

---

## 15. Status honesty

- This file is **documentation only** — not automated enforcement.
- MARS does **not** execute MetaBOT workflows.
- Live n8n parity is **not** proven by publishing this protocol.
- Sandbox UI steps marked **SAFE UNKNOWN** require one-time operator verification and optional addendum.

---

*MetaBOT Developer · Safe Workflow Patch Protocol v1 · Lane B · checkpoint `58c8f0b7`*
