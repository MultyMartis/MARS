# REPORT — MetaBOT SEO Agent vNext Lane Re-anchor and Plan

**Date:** 2026-07-10  
**Classification:** READ-ONLY lane re-anchor · vNext planning  
**Scope:** MetaBOT SEO Content Agent only (`project_id`: `metabot-seo-content-agent`)  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Checkpoint commit:** `84dd9b07` — `docs(metabot): add seo agent v14 architecture review`  
**Out of scope:** Smart Reporter, I-SEO Report Hub, Website Factory report demo, WordPress report shell

---

## 1. Executive Summary

Рабочая полоса **возвращена** к MetaBOT SEO Content Agent (`@seo_content_agent_bot`, Intake / Worker / Admin, n8n + Telegram + OpenRouter + Google Sheets). Последний корректный checkpoint — commit `84dd9b07`, включающий глубокий architecture review v14 и live evidence pack от 2026-07-10.

**Текущее состояние:** production-oriented внешняя система из трёх n8n workflow (Intake 20 nodes, Worker 91, Admin 15), документированная в MARS как knowledge layer; execution truth — live n8n.

**vNext фокус:** стабилизация и улучшение существующего SEO Content Agent — reliability (locks, `/get`, error visibility), docs v13→v14 sync, MetaBOT Developer patch discipline, quality-layer consolidation — **без** нового продукта и **без** Smart Reporter / Report Hub.

**Рекомендуемый порядок следующих шагов:**
1. Issue Backlog + Test Matrix (read-only)
2. `/get` + Lock Lifecycle Deep Audit (read-only + operator traces)
3. Safe Workflow Patch Protocol v1 (docs-only patch plan)

**Final status:** COMPLETE — MetaBOT SEO Agent lane re-anchored and vNext plan produced.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Checkpoint commit `84dd9b07` | exists ✓ |
| Staged changes | empty ✓ |
| Live API / n8n / Telegram / OpenRouter / Sheets calls | none ✓ |
| Foreign WIP | preserved, not touched ✓ |

**Read sources (this task):**
- `AGENTS.md`, `.cursorrules`
- `projects/metabot-seo-content-agent/README.md`, `OPERATIONAL-INDEX.md`
- `metabot-terminology-and-roles-v1.md`, `metabot-developer-concept-v1.md`, `n8n-project-development-rules-v1.md`
- `reports/REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md`
- `metabot-developer/n8n-workflow-json-grammar-v1.md`, `n8n-node-type-catalog-v14.md`, `n8n-import-safe-generation-rules-v1.md`
- `exports/live-v14-evidence/2026-07-10/WORKFLOW-MAP-v14.md`, `NODE-INVENTORY-v14.md`, `PROMPT-AND-CODE-NODE-INDEX-v14.md`, `RISK-AND-UNKNOWN-REGISTER-v14.md`

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

Следующие области **не читались, не изменялись, не анализировались** (кроме high-level git status):

- `projects/iseo-report-hub/`
- Smart Reporter docs
- Report Hub docs
- Website Factory report demo (`projects/mars-website-factory/...` — foreign WIP в git status)
- WordPress report hub architecture
- Client SEO report product docs

Foreign WIP (Website Factory, OCPilot, fp-0002 workspaces, `.recovery-temp/`) остаётся нетронутым.

---

## 4. Correct MetaBOT SEO Agent Checkpoint

### 4.1 What was completed

| Milestone | Evidence |
|-----------|----------|
| **MetaBOT Foundation Pack v1** | `OPERATIONAL-INDEX.md`, `metabot-terminology-and-roles-v1.md`, `metabot-developer-concept-v1.md`, `n8n-project-development-rules-v1.md` |
| **Canonical doc pack** | `projects/metabot-seo-content-agent/` — README, mega-map v13, workflow-map, lock/memory/QA docs |
| **Live v14 export + evidence** | `exports/live-v14-evidence/2026-07-10/` — sanitized JSON (3 workflows), WORKFLOW-MAP, NODE-INVENTORY, PROMPT-AND-CODE-NODE-INDEX, RISK-AND-UNKNOWN-REGISTER, SANITIZATION-REPORT |
| **v14 deep architecture review** | `reports/REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md` @ commit `84dd9b07` |
| **MetaBOT Developer n8n grammar** | `metabot-developer/n8n-workflow-json-grammar-v1.md`, `n8n-node-type-catalog-v14.md`, `n8n-import-safe-generation-rules-v1.md` @ commit `1b954990` |

### 4.2 Three live v14 workflows (REPO_EVIDENCED from sanitized export)

| Workflow | n8n ID | Nodes | Trigger | Role |
|----------|--------|-------|---------|------|
| **SEO Content Agent Beta.v14 - Intake** | `x8EbTGKNdlBprLvk` | 20 | Telegram Trigger | Gateway: command detect, lock, `/get` lookup, HTTP handoff |
| **SEO Content Agent Beta.v14 - Worker** | `p4mqb4VuPcemIDlC` | 91 | Webhook `seo-content-agent-worker` | Pipeline: outline→strategy→text→QA→factcheck→format |
| **SEO Content Agent Beta.v14 - Admin** | `AR6QxGt8ZKH0xG2T` | 15 | Webhook `seo-content-agent-admin` | Ops: `/locks`, `/health`, `/stop-all-flow`, help |

**Handoff (evidenced in v14 review):** Intake → Worker/Admin via **HTTP POST** (`Send To Worker`, `Send To Admin`), not executeWorkflow, not sheet-polling.

### 4.3 MetaBOT Developer — n8n grammar knowledge

- **Top-level JSON:** `name`, `nodes`, `connections`, `settings` — omit `activeVersion`, `pinData`, API metadata
- **126 nodes cataloged** across I/W/A — 62 Code, 19 Telegram, 16 Sheets, 11 HTTP, etc.
- **Import-safe rules:** no credentials in repo, omit `webhookId` on synthetic JSON, connections keyed by node **names**
- **Patterns:** Payload builder → HTTP (OpenRouter) → Extract; lock close before Telegram send; `splitMessage(3600)`

### 4.4 Current authority hierarchy

| Layer | Authority | Use for |
|-------|-----------|---------|
| **Live n8n** | Execution truth | Runtime behavior, credentials, webhooks |
| **v14 sanitized export** (`exports/live-v14-evidence/2026-07-10/`) | Best repo evidence of graph structure | Planning, patch proposals, grammar |
| **v14 architecture review** (`REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md`) | Synthesized analysis | vNext backlog, operator questions |
| **mega-map / OPERATIONAL-INDEX (v13 refs)** | Product semantics — **drift risk** | Historical context; sync to v14 pending |
| **legacy `workflow-sanitized-legacy.json`** | Legacy single-workflow snapshot | **Not** current I/W/A truth |

---

## 5. Current SEO Agent Product Understanding

| Dimension | Description |
|-----------|-------------|
| **Users** | i-SEO SEO specialists (OPERATOR_CLARIFICATION + export label `i-SEO`) |
| **Interface** | Telegram bot `@seo_content_agent_bot` |
| **Runtime** | External self-hosted n8n (not MARS) |
| **Workflows** | **Intake** (gateway) · **Worker** (compute) · **Admin** (ops/recovery) |
| **Outputs** | SEO ТЗ/outline, strategy, article/page text, SEO QA, factcheck, final cleanup/format |
| **State** | Google Sheets — `seo_active_jobs` (locks), `memory` (artifacts, get/reuse) |
| **LLM** | OpenRouter (`openai/gpt-4.1-mini` default evidenced in payload builders) |
| **Admin/recovery** | `/locks`, `/health`, `/stop-all-flow` — sheet-level cancel, not physical Worker stop |
| **Routes (Worker)** | `local`, `single`, `run`, `get`, `reuse` |
| **Concurrency** | Per-chat lock, TTL 30 min, `task_id=pending` at create |

**Not in scope:** Smart Reporter, client SEO reports, WordPress shells, File Export workflow (PLANNED only).

---

## 6. vNext Planning Scope

Planning categories and representative work — **evolution of existing agent**, not new product.

### Reliability fixes
- Stale/expired lock cleanup automation or admin path
- Lock ↔ `task_id` sync (`pending` → final `seo{timestamp}`)
- Orphan lock on `Send To Worker` HTTP failure after `Create Lock Row`
- Google Sheets quota/race mitigation (read caching, reduce health-check frequency)
- Error visibility after lock creation and mid-pipeline failures

### UX fixes
- `/get` silent failure → explicit Telegram error path
- Busy message clarity when stale lock blocks chat
- Consistent status feedback for long `/run` pipelines
- Admin `/stop-all-flow` user messaging (sheet cancel ≠ execution stop)

### Quality improvements
- Text Repair strict regression (reintroduces banned phrases)
- SEO QA / factcheck rubric calibration
- `--strict` behavior consistency across single vs run
- Deterministic scanner ↔ LLM QA alignment

### Prompt architecture improvements
- Central strict policy module (shared lexicon + rules)
- Reduce duplication: single vs run vs repair payload builders
- Model-per-stage strategy documentation (not yet centralized)

### n8n architecture improvements
- Worker error-handler subgraphs (none in NODE-INVENTORY)
- Intake HTTP handoff retry/compensation
- Formatter node decomposition (`Format Run Pipeline` ~11.7k chars)
- Wait node purpose documentation (3-unit debounce)

### MetaBOT Developer tooling improvements
- Workflow clone/export/diff discipline
- Safe patch proposal format + node-level change manifest
- Import test checklist + rollback plan template
- Dry-run/sandbox workflow clone strategy

### Research / MIG-lite candidates (later)
- Pre-outline keyword/competitor acquisition — **PLANNED**, not blocker for technical MVP
- Wordstat/Yandex API — SAFE UNKNOWN

### Documentation sync
- mega-map, OPERATIONAL-INDEX, workflow-map: v13 → v14 Beta naming
- Handoff mechanism: close SAFE UNKNOWN in WORKFLOW-MAP auto-index
- Sheets schema canonical doc

### Tests and validation
- n8n workflow test protocol (Telegram command matrix)
- Lock lifecycle test cases
- Regression suite for strict mode / Text Repair
- Parity checklist: sanitized export ↔ live n8n

---

## 7. Priority Backlog

| ID | Title | Category | Evidence (v14 review) | Why it matters | Risk | Proposed next investigation | Priority | Live n8n verify? | Operator decision? |
|----|-------|----------|----------------------|----------------|------|---------------------------|----------|------------------|-------------------|
| **B01** | `/get` silent failure | UX fixes | known-issues; get branch no error nodes; v14 §5.3, §15.3 | Users lose trust; task exists but no output | Medium — false negatives | Trace Worker `get` path failures in n8n execution log; map missing error branches | **P0** | Yes | No |
| **B02** | Stale lock cleanup | Reliability | known-issues; TTL 30m, no auto cleaner; v14 §9 | False busy blocks all content commands per chat | High — ops blocker | Sample `seo_active_jobs` for expired `active` rows; design admin/cron cleanup | **P0** | Yes | Yes (TTL policy) |
| **B03** | Lock / task_id sync | Reliability | Create Lock `task_id=pending`; v14 §8, §14.3 | Ops confusion; `/locks` misleading | Medium | Trace Worker nodes updating jobs sheet; confirm if `pending` ever promoted | **P0** | Yes | Yes (schema) |
| **B04** | Admin `/stop-all-flow` limitation | UX fixes | v14 §7.2 — sheet cancel only | Operators expect hard stop; LLM continues | Medium — cost + confusion | Document runbook; evaluate n8n cancel API feasibility | **P1** | Yes | Yes (semantics) |
| **B05** | Text Repair strict regression | Quality | known-issues; Build Text Repair Payload; v14 §11.4, §13 | Banned phrases reappear after cleanup | High — compliance | Diff repair output vs Strict Cleanup on sample tasks | **P1** | Yes | No (later SEO rubric) |
| **B06** | Central strict policy | Prompt architecture | distributed prompts + 4 JS scanners; v14 §11.4, O5 | single vs run drift | Medium | Extract strict lexicon from Code nodes; design shared module spec | **P1** | No | Yes (policy owner) |
| **B07** | Model config centralization | Prompt architecture | `route.model \|\| 'openai/gpt-4.1-mini'` in builders; v14 §6.5, O11 | Cost/quality opaque; hard to tune per stage | Low–Medium | Inventory all payload builders for model overrides | **P2** | Yes | Yes (model budget) |
| **B08** | Error visibility after lock create | Reliability | v14 §5.6 — HTTP failure after lock SAFE UNKNOWN | Orphan locks, silent failures | High | Reproduce `Send To Worker` failure; check compensation path | **P0** | Yes | Yes (compensation design) |
| **B09** | Google Sheets quota/race risk | Reliability | every lock = read; health multi-read; v14 §14.2, O1 | System-wide slowdown | High | `/health` frequency; concurrent command test | **P1** | Yes | Yes (caching strategy) |
| **B10** | Docs v13/v14 drift | Documentation sync | mega-map v13; OPERATIONAL-INDEX Worker v13; v14 §17.8, O9 | Planning errors, wrong handoff assumptions | Medium | Doc diff pass: v14 names, handoff, routes | **P1** | No | No |
| **B11** | SEO QA / factcheck rubric | Quality | Build SEOQA/Factcheck Payloads; v14 §11, O15 | Verdict quality not calibrated to team | Medium | Collect good/bad output corpus (later SEO team) | **P2** | Partial | Yes (SEO team later) |
| **B12** | Single vs run mode behavior | UX + Quality | Route Command; `--strict` not default on `/run`; v14 §6.2, §13 | Unexpected quality differences | Medium | Matrix: same input via `/run` vs `/text` + `--strict` | **P1** | Yes | No |
| **B13** | from:task_id / reuse behavior | UX + Reliability | Intake: reuse ≠ retrieval; Worker reuse branch; v14 §5.1, §6.3 | Wrong user expectations for `from:` | Medium | Test reuse for seoqa/factcheck/text modes | **P1** | Yes | No |
| **B14** | n8n workflow test protocol | Tests and validation | n8n-project-development-rules §12; v14 review §19 | No repeatable pre-deploy checks | Medium | Author test matrix from telegram-commands + v14 routes | **P1** | Yes (staging) | Yes (staging access) |
| **B15** | Safe workflow patch protocol | MetaBOT Developer tooling | grammar v1, import-safe rules; developer concept | Unsafe patches break production | High | Write `Safe Workflow Patch Protocol v1` doc | **P1** | No | Yes (approval gates) |
| **B16** | Admin ACL hardening | Reliability / Security | no ACL in export; v14 §7.4, O8 | Any bot user may run admin commands | High | Operator confirm Telegram allowlist | **P2** | Yes | Yes |
| **B17** | Worker error-handler subgraphs | n8n architecture | NODE-INVENTORY: no error nodes; v14 §6.7 | Silent pipeline failures | High | n8n execution history for failed runs | **P1** | Yes | Yes |
| **B18** | MIG-lite research layer | Research | OPERATIONAL-INDEX PLANNED; v14 O10 | Future acquisition — not MVP blocker | Low | Charter after technical stabilization | **P3** | No | Yes |

---

## 8. Improvements Possible Without SEO Team Interviews

Operator-as-authority; no SEO specialist interviews required for:

| Area | Actions |
|------|---------|
| **Technical reliability** | B02, B03, B08, B09 — lock lifecycle, orphan compensation, Sheets quota |
| **Lock cleanup** | Expired row detection; admin command or scheduled n8n workflow design |
| **`/get`** | B01 — error branch design from export analysis + execution traces |
| **Admin visibility** | B04 — honest `/stop-all-flow` runbook; `/locks` format improvements |
| **Strict policy consolidation** | B06 — technical extraction of lexicon from Code nodes (implementation spec) |
| **Docs sync** | B10 — v14 naming, handoff HTTP POST, route model |
| **Test protocol** | B14 — command × route matrix from committed evidence |
| **Workflow patch discipline** | B15 — MetaBOT Developer protocol |
| **Prompt/code inventory** | PROMPT-AND-CODE-NODE-INDEX already exists; extend with change-impact tags |
| **Import-safe snippets** | grammar v1 + import-safe rules for fragment generation |
| **Dry-run/sandbox clone** | Clone v14 workflows in n8n sandbox; run B14 matrix without production touch |

---

## 9. Later SEO Team Feedback Topics

Secondary — **not blockers** for next technical MVP:

- Output quality bar (acceptable vs reject examples)
- SEO QA rubric weights and verdict thresholds
- Preferred ТЗ / outline structure and mandatory fields
- Final text format (headings, tables, CTA blocks)
- Factcheck usefulness and claim categories
- Table policy (`--tables yes|no|auto`) typical cases
- Client/project-specific examples and niche templates
- Whether `/run` should imply stricter defaults than single commands

---

## 10. MetaBOT Developer Next Capabilities

For SEO Content Agent evolution, MetaBOT Developer should gain:

| Capability | Description |
|------------|-------------|
| **Workflow clone/export/diff discipline** | Sanitized export → diff narrative vs live; version labels (`Beta.v14`) |
| **Patch proposal format** | Markdown manifest: workflow, nodes touched, connections changed, risk class |
| **Safe JSON fragment generation** | Per grammar v1 + import-safe rules; no `webhookId`, no secrets |
| **Import test checklist** | Credential rebind, webhook activation, single-node smoke test |
| **Node-level change manifest** | Map each edit to NODE-INVENTORY role + regression tests |
| **Rollback plan** | Prior export ID, n8n version history steps, webhook URL restore |
| **Evidence before/after** | Execution screenshots/log IDs, Sheets row samples (redacted) |
| **No live deploy without operator approval** | MARS stops at artifacts + instructions — per developer concept gates |

---

## 11. Recommended Next 3 Cursor Tasks

### Task 1 — MetaBOT SEO Agent v14 — Issue Backlog and Test Matrix

| Field | Value |
|-------|-------|
| **Purpose** | Expand B01–B18 into executable test matrix with expected inputs/outputs per route |
| **Input evidence** | v14 review, WORKFLOW-MAP, telegram-commands.md, known-issues.md |
| **Allowed** | Read committed docs; create one report under `reports/` |
| **Forbidden** | Live n8n API; workflow JSON edits; prompt changes; commit |
| **Expected output** | `REPORT-metabot-seo-agent-v14-test-matrix.md` with pass/fail/UNKNOWN columns |

### Task 2 — MetaBOT SEO Agent v14 — `/get` and Lock Lifecycle Deep Audit

| Field | Value |
|-------|-------|
| **Purpose** | Trace Intake→Worker paths for `/get`, lock create/close, `pending` task_id; propose compensation designs (docs only) |
| **Input evidence** | Sanitized v14 JSON, v14 review §5–9, NODE-INVENTORY lock nodes |
| **Allowed** | Read export JSON; operator-provided execution log excerpts if supplied |
| **Forbidden** | Live n8n modify; Sheets API; Telegram |
| **Expected output** | Audit report with sequence diagrams, orphan-lock scenarios, recommended fix options (not implemented) |

### Task 3 — MetaBOT Developer — Safe Workflow Patch Protocol v1

| Field | Value |
|-------|-------|
| **Purpose** | Formalize patch proposal, sandbox test, operator approval, rollback — extends n8n-project-development-rules |
| **Input evidence** | grammar v1, import-safe rules, developer concept, v14 sanitizer lessons |
| **Allowed** | Create one doc under `metabot-developer/` |
| **Forbidden** | Live deploy; workflow JSON generation for production; commit unless requested |
| **Expected output** | `metabot-developer/safe-workflow-patch-protocol-v1.md` with templates |

---

## 12. SAFE UNKNOWN

| Topic | Notes |
|-------|-------|
| Production-only v14 vs parallel v13 | Operator must confirm single active set |
| Webhook production base URLs | Redacted in export |
| Full OpenRouter model map per stage | Only default evidenced |
| `task_id` promotion in `seo_active_jobs` | Not traced in export |
| Telegram admin ACL | Not in repo |
| Error/retry subgraphs | Not in NODE-INVENTORY |
| Automated expired-lock cleanup | Not evidenced |
| Intake `staticData` vs Sheets authority | Conflicting signals in export |
| n8n server version | Not in JSON |
| File Export workflow | PLANNED only |
| Whether v14 is sole production | Operator confirmation needed |

---

## 13. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-vnext-lane-reanchor-and-plan.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 14. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **Checkpoint:** `84dd9b07` present on branch
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** unchanged (Website Factory, OCPilot, fp-0002 workspaces, `.recovery-temp/`, etc.)

---

## 15. Final Status

**COMPLETE — MetaBOT SEO Agent lane re-anchored and vNext plan produced**

---

Awaiting operator review.
