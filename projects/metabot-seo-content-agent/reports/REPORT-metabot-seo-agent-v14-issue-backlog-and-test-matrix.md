# REPORT — MetaBOT SEO Agent v14 Issue Backlog and Test Matrix

**Date:** 2026-07-10  
**Classification:** READ-ONLY analysis · test planning only  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Intake / Worker / Admin  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer  
**Evidence pack:** `exports/live-v14-evidence/2026-07-10/`  
**Checkpoint commits verified:** `6263815c`, `1b954990`, `84dd9b07`, `af6fc35d`

**Constraints honored:** No live n8n / Telegram / OpenRouter / Sheets calls. No workflow modifications. No staging. No commit.

---

## 1. Executive Summary

На основе committed v14 evidence (санитизированный live-export 2026-07-10, deep architecture review, vNext re-anchor plan, MetaBOT Developer grammar) сформирован **read-only issue backlog** из **20 issues** и **три тестовые матрицы** (command/route, quality regression, reliability) плюс **no-live test protocol** для будущей операторской верификации.

**Ключевые выводы:**

| Area | Finding | Priority |
|------|---------|----------|
| **Reliability** | Orphan locks, stale `active` rows, lock↔`task_id` desync (`pending`), Sheets quota/race — высокий ops-риск | P0 |
| **UX** | `/get` silent failure; `/stop-all-flow` не останавливает in-flight Worker/LLM | P0–P1 |
| **Quality** | Text Repair strict regression; distributed strict policy; single vs run drift | P1 |
| **Documentation** | mega-map / OPERATIONAL-INDEX всё ещё v13; WORKFLOW-MAP auto-index помечает handoff SAFE UNKNOWN (противоречит v14 review) | P1 |
| **Process** | Нет формализованного test protocol и safe patch protocol в repo (planned B14/B15) | P1 |

**Статус:** Backlog и матрицы **готовы к operator review**. Исполнение тестов **не производилось** — все case IDs предназначены для sandbox/staging с explicit approval.

---

## 2. Preflight

| Check | Result |
|-------|--------|
| CWD | `X:\AI MARS` ✓ |
| Volume X: label | `AI WS` ✓ |
| Git branch | `mars/canonical-post-recovery` ✓ |
| Checkpoint `6263815c` | exists — `docs(metabot): add foundation pack and live n8n evidence exporter` ✓ |
| Checkpoint `1b954990` | exists — `docs(metabot): add n8n workflow grammar references` ✓ |
| Checkpoint `84dd9b07` | exists — `docs(metabot): add seo agent v14 architecture review` ✓ |
| Checkpoint `af6fc35d` | exists — `docs(metabot): add seo agent vnext reanchor plan` ✓ |
| Staged changes | empty ✓ |
| Live API calls | none ✓ |
| Foreign WIP | preserved, not touched ✓ |

**Note:** `git log origin/mars/canonical-post-recovery..HEAD` shows unpushed commits (detour tail includes non-MetaBOT work). Per task charter: **no commit/push**; foreign WIP inventory acknowledged only.

---

## 3. Out-of-Scope Preserved

**OUT_OF_SCOPE_PRESERVED**

Следующие области **не читались, не изменялись, не анализировались** (кроме high-level git status):

| Path / area | Git status signal |
|-------------|-------------------|
| `projects/iseo-report-hub/` | not in scope |
| Smart Reporter docs | not in scope |
| Website Factory report demo | `M projects/mars-website-factory/...` — foreign WIP |
| WordPress report hub | `M workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/...` |
| `workspaces/fp-0002-*` | foreign WIP |
| `projects/ocpilot/` | foreign WIP |
| `.recovery-temp/`, `.restore-test-temp/` | untracked foreign WIP |

---

## 4. Source Evidence

### 4.1 Governance and product docs (read)

| Source | Role |
|--------|------|
| `AGENTS.md`, `.cursorrules` | MARS boundaries, preflight discipline |
| `README.md`, `OPERATIONAL-INDEX.md` | Product identity, v13 refs, work lines |
| `known-issues.md`, `telegram-commands.md` | Operational issues, command surface |

### 4.2 v14 analysis and planning (read)

| Source | Role |
|--------|------|
| `reports/REPORT-metabot-seo-agent-v14-deep-workflow-architecture-review.md` | Synthesized I/W/A architecture |
| `reports/REPORT-metabot-seo-agent-vnext-lane-reanchor-and-plan.md` | B01–B18 priority backlog seed |

### 4.3 MetaBOT Developer discipline (read)

| Source | Role |
|--------|------|
| `metabot-developer/n8n-workflow-json-grammar-v1.md` | JSON grammar, omit rules |
| `metabot-developer/n8n-node-type-catalog-v14.md` | 126 nodes, typeVersions |
| `metabot-developer/n8n-import-safe-generation-rules-v1.md` | Import-safe generation |

### 4.4 Live v14 evidence pack (read)

| Source | Role |
|--------|------|
| `exports/live-v14-evidence/2026-07-10/WORKFLOW-MAP-v14.md` | Node/route index (handoff auto-index stale) |
| `exports/live-v14-evidence/2026-07-10/NODE-INVENTORY-v14.md` | 126 nodes, no error-handler nodes |
| `exports/live-v14-evidence/2026-07-10/PROMPT-AND-CODE-NODE-INDEX-v14.md` | Prompt/code node sizes |
| `exports/live-v14-evidence/2026-07-10/RISK-AND-UNKNOWN-REGISTER-v14.md` | Unknowns, operator gates |

### 4.5 Authority hierarchy (for test planning)

1. **Live n8n** — execution truth (not accessed this task)
2. **v14 sanitized export** — best repo graph evidence
3. **v14 architecture review** — synthesized behavior
4. **mega-map / OPERATIONAL-INDEX (v13)** — semantics with drift risk

---

## 5. Issue Backlog

**Legend:**  
- **Risk:** Low / Medium / High / Critical  
- **Priority:** P0 (immediate) / P1 (next wave) / P2 (planned) / P3 (research)  
- **Live n8n:** requires live execution trace to confirm  
- **Operator:** requires human policy/approval decision

### 5.1 Reliability and ops

| ID | Title | Category | Evidence source | Affected workflow | Affected route/command | Suspected cause | User impact | Risk | Verification method | Live n8n? | Operator? | Priority |
|----|-------|----------|-----------------|-------------------|------------------------|-----------------|-------------|------|---------------------|-----------|-----------|----------|
| **IB-01** | `/get` silent failure | UX / Reliability | `known-issues.md`; v14 review §5.3, §15.3; NODE-INVENTORY: no error nodes on get path | Worker (primary); Intake (handoff) | `/get task_id` → Worker `get` route | Missing error branch after `Lookup Memory Get` / `Find Memory Get Row`; Sheets timeout; Telegram send failure without fallback | User receives no message; perceives bot as broken | High | Trace n8n execution for `/get` with valid task_id; inject Sheets failure; check Telegram error path | Yes | No | **P0** |
| **IB-02** | Stale lock cleanup | Reliability | `known-issues.md`; v14 review §9; no auto-cleaner in export | Intake, Admin | All content commands; `/locks` | TTL 30 min on `expires_at` but no automated status transition for expired `active` rows | False busy; chat blocked until manual cleanup | High | Sample `seo_active_jobs` for `status=active` AND `expires_at < now`; test content command after expiry without admin action | Yes | Yes (TTL/cleanup policy) | **P0** |
| **IB-03** | Lock / `task_id` sync | Reliability | `known-issues.md`; Create Lock `task_id=pending`; v14 review §8, §14.3 | Intake, Worker | `/run`, `/text`, `/outline`, etc. | Lock created with `pending`; Worker assigns real `seo{ts}{rand}` — update path to jobs sheet **SAFE UNKNOWN** | `/locks` shows misleading `pending`; ops cannot correlate lock to memory row | Medium | Compare `seo_active_jobs.task_id` vs `memory.task_id` after successful run; check if promotion node exists in live graph | Yes | Yes (schema) | **P0** |
| **IB-04** | Error visibility after lock creation | Reliability | v14 review §5.6; Intake: Create Lock → Send To Worker (HTTP) | Intake | Content commands after lock create | HTTP POST to Worker webhook fails; no evidenced compensation; lock row remains `active` | Orphan lock; user may see Task Accepted then silence | High | Simulate Worker webhook down after lock create; observe Sheets row + Telegram follow-up | Yes | Yes (compensation design) | **P0** |
| **IB-05** | Google Sheets quota / race risk | Infrastructure | `known-issues.md`; v14 review §14.2; `/health` multi-read | Intake, Worker, Admin | `/health`; every lock check; memory append | Non-atomic reads/writes; concurrent commands per chat or fleet-wide health probes | System-wide slowdown; intermittent failures | High | Concurrent `/health` + content command; monitor quota errors in execution log | Yes | Yes (caching strategy) | **P1** |
| **IB-06** | Admin `/stop-all-flow` limitation | UX / Ops | v14 review §7.2; `known-issues.md` | Admin; indirect Worker | `/stop-all-flow` | Admin sets `status=cancelled` in Sheets only; cannot kill in-flight OpenRouter HTTP or n8n execution | Operator expects hard stop; LLM cost continues; user may still receive output | Medium | Run `/run`, invoke `/stop-all-flow` mid-pipeline; observe Worker completion and OpenRouter calls | Yes | Yes (semantics/runbook) | **P1** |
| **IB-07** | Worker error-handler subgraphs absent | Reliability | NODE-INVENTORY: no dedicated error nodes; v14 review §6.7 | Worker | All routes | OpenRouter/Sheets/Telegram failures propagate without user-facing error path | Silent pipeline death after Task Accepted | High | Force OpenRouter 5xx on one stage; check Telegram + lock close behavior | Yes | Yes | **P1** |
| **IB-08** | Admin ACL hardening | Security | v14 review §7.4; no ACL in export | Intake, Admin | `/help`, `/locks`, `/health`, `/stop-all-flow` | Any Telegram user reaching bot may invoke admin-routed commands | Unauthorized stop-all or health probes | High | Test admin commands from non-operator Telegram account | Yes | Yes (allowlist) | **P2** |
| **IB-09** | Intake `staticData` vs Sheets authority | Reliability | v14 review §8; grammar v1 §2.1 `staticData` legacy | Intake | Lock path | Export contains `global.seo_active_jobs` snapshot; operational SoT is Sheets | Debug confusion; possible stale local state if relied upon | Low–Medium | Compare Intake staticData in export vs live Sheets rows | Yes | No | **P2** |

### 5.2 Quality and prompts

| ID | Title | Category | Evidence source | Affected workflow | Affected route/command | Suspected cause | User impact | Risk | Verification method | Live n8n? | Operator? | Priority |
|----|-------|----------|-----------------|-------------------|------------------------|-----------------|-------------|------|---------------------|-----------|-----------|----------|
| **IB-10** | Text Repair strict regression | Quality | `known-issues.md`; Build Text Repair Payload; v14 review §11.4, §13 | Worker | `/run` (run path); `/text` (single repair branch) | LLM Text Repair reintroduces banned phrases after Strict Cleanup / scanners | Compliance violations in delivered text | High | Pipeline sample with known banned phrases; diff pre/post Text Repair | Yes | No | **P1** |
| **IB-11** | Central strict policy drift | Quality / Architecture | v14 review §11.4, O5; distributed prompts + 4 JS scanners | Worker | `single`, `run`, `reuse`; `--strict` flag | No shared strict lexicon module; single vs run vs repair use different prompt copies | Inconsistent strict enforcement across modes | Medium | Same input via `/text --strict` vs `/run` + manual strict; compare scanner hits and output | Partial | Yes (policy owner) | **P1** |
| **IB-12** | Single vs run behavior divergence | UX / Quality | Route Command; v14 review §6.2, §13; `known-issues.md` strict inheritance | Worker | `single` vs `run` | `/run` does not default `--strict`; different pipeline depth (outline→strategy→text→QA layers) | Unexpected quality differences for same brief | Medium | Matrix: identical brief via `/run` vs `/text` + flags | Yes | No | **P1** |
| **IB-13** | SEO QA / factcheck rubric improvement | Quality | Build SEOQA/Factcheck Payloads; v14 review O15 | Worker | `/seoqa`, `/factcheck`, `/run` (late stages) | LLM verdict thresholds not calibrated to SEO team corpus | False pass / false reject | Medium | Curated good/bad corpus; compare verdicts vs human labels | Partial | Yes (SEO team) | **P2** |
| **IB-14** | Auto Polish regression | Quality | Auto Polish Text node; run path post-text | Worker | `/run` | LLM polish may alter strict-compliant text or introduce template smell | Quality drift after deterministic cleanup | Medium | Diff text before/after Auto Polish on strict-compliant sample | Yes | No | **P2** |
| **IB-15** | Content score vs SEO QA mismatch | Quality | Compute Content Score → Build SEOQA Payload | Worker | `/run` | Deterministic score may disagree with LLM SEO QA verdict | Operator confusion; false confidence | Low–Medium | Cases where content_score high but seoqa rejects (and vice versa) | Yes | No | **P2** |

### 5.3 Architecture, docs, process

| ID | Title | Category | Evidence source | Affected workflow | Affected route/command | Suspected cause | User impact | Risk | Verification method | Live n8n? | Operator? | Priority |
|----|-------|----------|-----------------|-------------------|------------------------|-----------------|-------------|------|---------------------|-----------|-----------|----------|
| **IB-16** | `from:task_id` / reuse behavior | UX / Reliability | v14 review §5.1, §6.3; Intake: reuse ≠ retrieval | Intake, Worker | `/text from:ID`, `/seoqa from:ID`, `/factcheck from:ID` | Users may expect retrieval; system creates **new** task with lock (except pure `/get`) | Duplicate tasks; unexpected locks; wrong mode | Medium | Test reuse modes with valid/invalid/missing task_id; observe lock + new task_id | Yes | No | **P1** |
| **IB-17** | Model config centralization | Architecture | `route.model \|\| 'openai/gpt-4.1-mini'` in payload builders; v14 §6.5 | Worker | All LLM stages | Model embedded per Code node; no central config | Cost/quality tuning opaque; stage-specific overrides unknown | Low–Medium | Inventory all HTTP payload builders in live export; document per-stage model | Yes | Yes (model budget) | **P2** |
| **IB-18** | Docs v13/v14 drift | Documentation | README, OPERATIONAL-INDEX (Worker v13); WORKFLOW-MAP handoff SAFE UNKNOWN vs review | All (planning) | N/A | Docs not synced after v14 export | Wrong planning assumptions | Medium | Doc diff pass: names, handoff HTTP POST, routes | No | No | **P1** |
| **IB-19** | n8n workflow test protocol | Process | vNext B14; `n8n-project-development-rules-v1.md` §12 | All | All commands/routes | No repeatable pre-deploy test checklist in repo | Regressions ship to production | Medium | Adopt §6–§8 matrices; operator sign-off template | Yes (staging) | Yes (staging access) | **P1** |
| **IB-20** | Safe workflow patch protocol | Process | vNext B15; grammar v1; import-safe rules; developer concept | All | N/A | Patch discipline documented in fragments only | Unsafe JSON import; production breakage | High | Author `safe-workflow-patch-protocol-v1.md` (separate task); dry-run on sandbox clone | No | Yes (approval gates) | **P1** |

---

## 6. Command / Route Test Matrix

**Convention:** Tests **not executed** in this task. **Confidence:** High = export + review agree; Medium = partial evidence; Low = SAFE UNKNOWN behavior.

### 6.1 Telegram / Intake

| Test ID | Command / input | Expected Intake behavior | Expected Worker/Admin route | Expected Sheets behavior | Expected Telegram output | Expected lock behavior | Expected memory behavior | Evidence confidence | Known risk | Manual verification notes |
|---------|-----------------|--------------------------|----------------------------|--------------------------|--------------------------|------------------------|--------------------------|---------------------|------------|---------------------------|
| **TC-I01** | `/start` | `Detect Local Command` → local | Worker `local` (if misrouted) OR Intake only static response | None | Welcome / onboarding via `Send Local Intake Message` | No lock | No write | High | Low | Confirm no Worker HTTP call in n8n log |
| **TC-I02** | `/help` | Admin branch → `Send To Admin` | Admin: `Build Admin Response` | None | Help text via Admin Telegram | No lock | No write | High | Admin ACL (IB-08) | Trace Intake → Admin webhook |
| **TC-I03** | `/examples` | Admin branch | Admin: examples text | None | Examples via Admin | No lock | No write | High | Same as TC-I02 | — |
| **TC-I04** | `/text {brief}` (no lock) | Content path → lock create → Worker POST | Worker `single` | Append lock row `active`, `task_id=pending`; later Worker updates/close | Task Accepted → pipeline status → result chunks | Create → close on success (single path) | Append on completion | High | IB-03, IB-04 | Record `task_id` in memory vs jobs sheet |
| **TC-I05** | `/run {brief}` while no lock | Content path | Worker `run` | Same lock create | Task Accepted (run-specific text) → multi status → chunked output | Create → Close Lock Before Sending → Finish Lock | Append run row | High | Long runtime; IB-06 | Full pipeline timing |
| **TC-I06** | `/text {brief}` while active lock exists | `IF Busy` true | Worker **not** called | Lookup only | Busy message | No second lock | No new write | High | Stale lock false busy (IB-02) | Use fresh chat vs expired lock chat |
| **TC-I07** | `/unknowncmd` | Local branch | None | None | Static unknown-command response | No lock | No write | High | Low | — |
| **TC-I08** | `/locks` | Admin branch | Admin `locks` route | Read `seo_active_jobs` | Formatted lock list | No change | No write | High | Misleading `pending` (IB-03) | Compare to raw sheet |
| **TC-I09** | `/health` | Admin branch | Admin health route | Read jobs + memory tabs | Health summary | No change | No read/write by user | High | Sheets quota (IB-05) | Avoid rapid repeat |
| **TC-I10** | `/stop-all-flow` | Admin branch | Admin stop route | Cancel active rows | Success confirmation | Active → `cancelled` | No write | High | Does not stop Worker (IB-06) | Run during active `/run` |
| **TC-I11** | `/get seo1234567890` (exists in memory) | Retrieval branch → Worker payload `lock=null` | Worker `get` | Intake may lookup; Worker `Lookup Memory Get` | Formatted output chunks (max 3600) | No lock | Read only | Medium | Silent failure (IB-01) | Use known task_id from prior run |
| **TC-I12** | `/get seoMISSING` | Retrieval → not found | Worker **not** called if Intake lookup empty | Intake `Lookup From Task` | NOT-FOUND message | No lock | No write | High | Intake vs Worker double-lookup paths | Confirm which path handles missing |
| **TC-I13** | `/seoqa from:seoVALID` | Content + lock (not retrieval) | Worker `reuse` | Lock create + memory lookup for reuse | Task Accepted → single-mode QA output | New lock + new task_id | New append row | High | User expects no new task (IB-16) | Document UX expectation |
| **TC-I14** | `/factcheck from:seoVALID` | Content + lock | Worker `reuse` | Same | Factcheck output | Same | New row | High | Same | — |
| **TC-I15** | `/text from:seoVALID` | Content + lock | Worker `reuse` | Same | Text output | Same | New row | High | Same | — |
| **TC-I16** | `/text from:seoINVALID` | Content + lock | Worker `reuse` → missing row | Lock may still create | Error message **SAFE UNKNOWN** | Possible orphan lock | No reuse source | Low | IB-01, IB-04 | Critical edge case |
| **TC-I17** | Normal text without `/` prefix | Treated as content or ignored | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | Low | — | Confirm Intake parsing for free text |
| **TC-I18** | `/text --strict {brief}` | Content + lock; strict flag parsed | Worker `single` with `strict=true` | Lock create | Stricter output path | Standard single lock | Append | Medium | IB-11 | Compare to non-strict |
| **TC-I19** | `/run --no-factcheck {brief}` | Content + lock | Worker `run`; factcheck skipped | Lock create | Run without factcheck stages | Standard run lock | Append | High | Quality gap | Switch Run Factcheck branch |
| **TC-I20** | Admin cmd from non-operator user | **SAFE UNKNOWN** ACL | Admin | Same as operator? | Same? | — | — | Low | IB-08 | Security test |

### 6.2 Worker routes (direct webhook — staging only)

| Test ID | Route | Trigger input | Expected behavior | Sheets | Telegram | Lock | Memory | Confidence | Risk |
|---------|-------|---------------|-------------------|--------|----------|------|--------|------------|------|
| **TC-W01** | `local` | Invalid/help/start in Worker payload | `Format Local Response` → Telegram + Append Memory Local | Append local row | Local help text | None in payload | Append | High | Low |
| **TC-W02** | `single` | `/text` payload with lock | OpenRouter Single → optional repair → close lock → send | Close single lock; append | Status + result | Close before send | Append | High | IB-10 |
| **TC-W03** | `run` | `/run` payload with lock | Full pipeline §6.4 architecture review | Close + finish lock; append | Multi status + chunks | Close before send | Append | High | Duration, IB-06 |
| **TC-W04** | `get` | `/get` with `lock=null` | Memory lookup → format → chunk send | Read memory | Memory get output | None | Read only | Medium | IB-01 |
| **TC-W05** | `reuse` | `from_task_id` + mode text/seoqa/factcheck | Lookup reuse → Build Single Payload → single path | Lock from Intake; read memory | Reuse output | From Intake | New append | High | IB-16 |

### 6.3 Admin routes (direct webhook — staging only)

| Test ID | Command | Expected Admin behavior | Sheets | Telegram | Confidence | Risk |
|---------|---------|-------------------------|--------|----------|------------|------|
| **TC-A01** | `locks` | Lookup → format → send | Read jobs | Lock list | High | IB-03 |
| **TC-A02** | `health` | Jobs + memory health probes | Multi-read | Health text | High | IB-05 |
| **TC-A03** | `stop-all-flow` | Cancel all active locks | Update to `cancelled` | Success msg | High | IB-06 |
| **TC-A04** | `help` / `examples` | Static admin response | None | Help text | High | Low |
| **TC-A05** | Unknown admin cmd | **SAFE UNKNOWN** fallback | None | Error or default? | Low | — |

---

## 7. Quality Regression Test Matrix

| Test ID | Input sample type (not full production prompt) | Expected protection layer | Expected failure signal | Verification method | Priority |
|---------|-----------------------------------------------|---------------------------|-------------------------|---------------------|----------|
| **TQ-01** | Brief containing phrases «гарантируем рост», «помогает улучшить» | Strict Risk Scanner + SEO QA prompt + Postcheck Strict Claims | Scanners flag; SEO QA `reject` or edited output; no phrases in final Telegram | Run `/run` and `/text --strict`; grep output | **P0** |
| **TQ-02** | Brief requesting «закажите сейчас», «профессиональное решение» | Text prompts (SAFE CLAIMS) + Strict Cleanup + scanners | Phrases absent or explicitly rejected in QA block | Single vs run comparison | **P1** |
| **TQ-03** | Text with intentionally broken Markdown tables (`\|---\|`) | Table Sanity Check → may feed SEO QA | `table_sanity_check` issues; QA notes table problems | Inject malformed table in mid-pipeline sample | **P1** |
| **TQ-04** | Output with `_`, `` ` ``, `*` Telegram-unsafe chars | Parse Mode + Format Run Pipeline sanitizer | Stripped or escaped; no Telegram API 400 | Send long formatted result | **P2** |
| **TQ-05** | Strict-clean text then Text Repair stage (run path) | Build Text Repair Payload (temp 0.05) → Strict Cleanup after | **No reintroduction** of banned lexicon | Diff pre/post repair; IB-10 | **P0** |
| **TQ-06** | Strict-clean text then Auto Polish (LLM) | Auto Polish Text (temp 0.15) | No new forbidden promises; tone preserved | Diff pre/post polish | **P1** |
| **TQ-07** | Brief misaligned with outline (wrong H2 topics) | SEO QA JSON verdict | `reject` or low score with explicit mismatch reasons | `/seoqa --strict from:task` on bad pair | **P1** |
| **TQ-08** | Brief with unverifiable medical/legal claims | Factcheck JSON verdict | `unsafe` claims flagged; not presented as fact | `/factcheck --strict from:task` | **P1** |
| **TQ-09** | Content passing SEO QA despite scanner failures | Compute Content Score fed into SEO QA prompt | SEO QA should not `pass` when deterministic issues high | Force scanner failures; check QA verdict | **P1** |
| **TQ-10** | Factcheck pass despite strict marker remnants | Postcheck Strict Claims after factcheck | Postcheck catches regex strict markers | Inject markers before postcheck | **P1** |
| **TQ-11** | Same brief: `/run` vs `/text --strict` | Full pipeline vs single + strict flag | Quality parity within defined tolerance | Side-by-side output review | **P1** |
| **TQ-12** | `/run` without `--strict` vs with `--strict` | `--strict` flag in Route Command | Stricter lexicon enforcement when flag set | A/B output compare | **P1** |
| **TQ-13** | `--no-factcheck` run on claim-heavy brief | Switch Run Factcheck skip | Factcheck block omitted; claims may remain | Confirm factcheck section absent | **P2** |
| **TQ-14** | `outline_only` flag | Switch Run After Outline | Pipeline stops after outline; no text/QA | Check output structure | **P2** |
| **TQ-15** | `tables_policy=no` vs `auto` | Route Command flags → text builder | Table presence differs per policy | Compare outputs | **P2** |

---

## 8. Reliability Test Matrix

| Test ID | Route / scenario | Expected current behavior (if known) | Desired behavior later | Evidence confidence | Priority |
|---------|------------------|----------------------------------------|------------------------|---------------------|----------|
| **TR-01** | Lock creation on content cmd | Append `seo_active_jobs` row: `active`, `task_id=pending`, TTL 30m | Same + immediate `task_id` promotion when Worker starts | High | **P0** |
| **TR-02** | Duplicate lock same chat | Second command → Busy message; no second row | Same; optional queue-notify UX | High | **P1** |
| **TR-03** | Stale lock expiration | Busy if row still `active` after `expires_at` **unless** manual/admin cleanup | Auto-expire or ignore expired in `Check Active Lock` | Medium | **P0** |
| **TR-04** | Lock close after success (run) | `Close Lock Before Sending` → `Finish Lock` | Terminal status + final `task_id` in jobs sheet | High | **P0** |
| **TR-05** | Lock close after OpenRouter failure | **SAFE UNKNOWN** — no error nodes evidenced | Lock closed + user error Telegram; no orphan `active` | Low | **P0** |
| **TR-06** | Lock close after Telegram failure | **SAFE UNKNOWN** | Retry send or error notice; lock state consistent | Low | **P1** |
| **TR-07** | `/stop-all-flow` during in-flight Worker | Locks cancelled in sheet; Worker continues | Honest messaging + optional n8n execution cancel research | High | **P1** |
| **TR-08** | Google Sheets lookup failure (lock check) | **SAFE UNKNOWN** — may fail open or closed | Explicit error to user; no silent accept | Low | **P0** |
| **TR-09** | Google Sheets append failure (memory) | Some nodes have `continueOnFail` (Worker append) | User warned; ops alert; idempotent retry | Medium | **P1** |
| **TR-10** | OpenRouter timeout (120s) | HTTP node timeout; downstream **SAFE UNKNOWN** | Stage failure message; lock cleanup | Medium | **P0** |
| **TR-11** | Memory append failure after successful send | `continueOnFail` on some append nodes | User has output but `/get` later fails — document | Medium | **P1** |
| **TR-12** | `/get` lookup failure (Worker get) | Silent failure suspected (IB-01) | Explicit «ошибка поиска» Telegram message | Medium | **P0** |
| **TR-13** | Reuse missing `from:task_id` | **SAFE UNKNOWN** error path | NOT-FOUND style message; no orphan lock | Low | **P0** |
| **TR-14** | Intake HTTP handoff failure post-lock | Orphan `active` lock likely | Compensation: delete lock or mark failed + user notice | Low | **P0** |
| **TR-15** | Concurrent `/health` + content command | Sheets quota pressure | Rate-limit health; cache reads | Medium | **P1** |
| **TR-16** | Worker Wait node (3 units) | Debounce before processing | Documented purpose; no duplicate processing | Medium | **P2** |

---

## 9. No-Live Test Protocol

**Purpose:** Enable operator to validate v14 later **without breaking production**.

### 9.1 Principles

1. **Read-only first** — review sanitized export, execution logs, Sheets samples before any write action.
2. **No production webhook replacement** — never point Telegram bot or Intake handoff URLs to experimental graphs without rollback plan.
3. **Explicit approval gates** — sandbox clone, test chat, test sheet rows require written operator charter.
4. **Evidence discipline** — before/after export, screenshots, n8n execution IDs, redacted Sheets row samples.

### 9.2 Phased procedure

| Phase | Action | Approval required |
|-------|--------|-------------------|
| **0 — Inventory** | Confirm active workflows match v14 IDs (`x8EbTGKNdlBprLvk`, `p4mqb4VuPcemIDlC`, `AR6QxGt8ZKH0xG2T`) | No |
| **1 — Read-only trace** | Run TC-I01–I12 in **production** only if operator accepts observability risk; prefer historical n8n execution replay | Operator |
| **2 — Sandbox clone** | Duplicate all three workflows in n8n with suffix `.sandbox`; **inactive** until creds bound | **Explicit approval** |
| **3 — Test surfaces** | Dedicated Telegram test chat/user; duplicate Google Sheet tabs `seo_active_jobs_sandbox`, `memory_sandbox` | Operator |
| **4 — Webhook isolation** | Sandbox Worker/Admin webhooks on non-production paths; Intake clone points to sandbox URLs only in **test bot** instance | **Explicit approval** |
| **5 — Matrix execution** | Execute §6–§8 test IDs one category at a time; record pass/fail/UNKNOWN per row | Operator |
| **6 — Before/after export** | Export sandbox JSON before and after any patch; store outside git or in `raw/` (gitignored) | Operator |
| **7 — Rollback** | n8n version history restore; reactivate prior workflow version; restore webhook URLs; delete sandbox rows | Documented before phase 5 |
| **8 — Production patch** | Only via IB-20 safe patch protocol + IB-19 test matrix pass on sandbox | **Separate charter** |

### 9.3 Pass/fail recording template

```
Test ID:
Date:
Environment: production | sandbox
Workflow versions:
Input (redacted):
Expected:
Observed:
Sheets snapshot (row ids redacted):
n8n execution URL/ID:
Telegram screenshot:
Result: PASS | FAIL | UNKNOWN
Notes:
```

### 9.4 Forbidden during protocol

- Mass lock cancellation on production without ops runbook
- `stop-all-flow` on production during business hours without notice
- Committing unsanitized exports
- Patching Worker `Format Run Pipeline` / payload builders without SEO team review for quality tests

---

## 10. Recommended Next Actions

| # | Action | Owner | Depends on |
|---|--------|-------|------------|
| 1 | Operator review this backlog; confirm P0 ordering | Operator | — |
| 2 | Execute **Task 2** from vNext plan: `/get` + Lock Lifecycle Deep Audit (read-only + traces) | Cursor + Operator | This report |
| 3 | Execute **Task 3**: Safe Workflow Patch Protocol v1 doc | Cursor | IB-20 |
| 4 | Sandbox setup per §9; run TC-I11, TC-I06, TR-03, TR-12 first | Operator | Sandbox approval |
| 5 | Docs sync IB-18: mega-map / OPERATIONAL-INDEX → v14 Beta naming | Cursor/docs owner | Operator approval for edits |
| 6 | Sample `seo_active_jobs` for IB-02, IB-03 (redacted rows to MARS STORAGE incoming) | Operator | — |
| 7 | SEO team corpus collection for IB-13 (later; not blocker) | SEO team | — |

---

## 11. SAFE UNKNOWN

| Topic | Impact on testing |
|-------|-------------------|
| Production-only v14 vs parallel v13 | Matrix may target wrong graphs |
| Webhook production base URLs | Sandbox handoff URLs unverified |
| Full OpenRouter model map per stage | Quality tests may use unexpected models |
| `task_id` promotion in `seo_active_jobs` | TR-01, IB-03 tests inconclusive from export alone |
| Telegram admin ACL | TC-I20, IB-08 require live account matrix |
| Error/retry subgraphs | TR-05, TR-06, TR-08 behaviors undefined |
| Automated expired-lock cleanup | TR-03 desired behavior not implemented |
| Intake free-text (no slash) handling | TC-I17 |
| n8n server version | Import/patch compatibility |
| File Export workflow | Out of scope — PLANNED only |
| WORKFLOW-MAP-v14 handoff auto-index | Says SAFE UNKNOWN; contradicts architecture review — treat review as superseding for handoff |

---

## 12. Files Created

| File | Action |
|------|--------|
| `projects/metabot-seo-content-agent/reports/REPORT-metabot-seo-agent-v14-issue-backlog-and-test-matrix.md` | **Created** (this report) |

No existing docs modified. No staging. No commit.

---

## 13. Git Status

- **Branch:** `mars/canonical-post-recovery`
- **HEAD:** `be3db88f` (ahead of `origin/mars/canonical-post-recovery` @ `49ffdafe`)
- **Staged:** empty
- **This task:** one new untracked report under `projects/metabot-seo-content-agent/reports/`
- **Foreign WIP:** preserved — Website Factory, OCPilot, fp-0002 workspaces, `.recovery-temp/`, etc.
- **Commit / push:** not performed

---

## 14. Final Status

**COMPLETE — issue backlog and test matrix completed**

---

## 15. Status Appendix — PC14-FU-01 Closeout (2026-07-13)

Additive history only — does not rewrite §5 issue rows.

| Item | Status |
|------|--------|
| **PC14-FU-01** | **COMPLETE** — `PC14_FU01_CLOSED_NEXT_SELECTED` |
| Production Worker | `p4mqb4VuPcemIDlC` active on Strict Cleanup `v15-strict-cleanup-pc14-fu01-r1` |
| Production apply | commit `ebfaeb22` |
| Operator smoke | commit `5541811c` · Task ID `seo20260712201612oo0m85` |
| Final SEO Text | clean for PC-14 R1 + FU-01 families |
| SEO QA / Factcheck | approved · score `100` / approved |
| Known residual | `для удобства восприятия` in SEO ТЗ only (outside final SEO Text) |
| **Next selected** | `PC14_FU02_TZ_STRICT_RESIDUAL_CLEANUP_AUDIT` — read-only audit/proposal first |
| Closeout report | [REPORT-metabot-seo-agent-v14-pc14-fu01-closeout-next-backlog-selection.md](REPORT-metabot-seo-agent-v14-pc14-fu01-closeout-next-backlog-selection.md) |

Related original quality issues remain documented: **IB-10** (Text Repair strict regression), **IB-11** (central strict policy drift). FU-02 is the direct follow-up from current smoke residual, not a rewrite of those rows.

Awaiting operator review.
