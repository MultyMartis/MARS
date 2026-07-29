# REPORT — ISEO SALES MANAGER BOT PHASE 3A.1 SOURCE INGEST AND SANITIZED BASELINES

**Date:** 2026-07-30  
**Process line:** ISEO-SALES-MANAGER-BOT — PHASE 3A.1 SOURCE INGEST AND SANITIZED BASELINES  
**Project locus:** `projects/iseo-sales-manager-bot/`

---

## 1. Verdict

**PHASE 3A.1 COMPLETE — READY FOR OPERATOR SANDBOX GATE**

(with documented implementation-spec corrections against exact sanitized source graph; architecture not redesigned)

---

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume label | `AI WS` |
| Canonical branch (worktree base) | `origin/mars/canonical-post-recovery` @ `f50508df` |
| Local dirty main index | **preserved** (foreign WIP untouched) |
| Commit construction | temporary clean worktree |
| Live n8n | not accessed |
| Google Sheets / Gmail / Telegram | not modified |

---

## 3. Source Inventory

| Exact filename | Size | Timestamp | Parse | Role | Sanitize required | Safe for Git | Structural risks |
|----------------|------|-----------|-------|------|-------------------|--------------|------------------|
| `Sales-Manager-v1 json.txt` | 40623 | 2026-07-30 01:51:30 | PASS | workflow v1 | yes | **no** (raw) | auth headers, bearer, instanceId, chat ids, workbook ids |
| `Sales-Manager-v2 json.txt` | 46752 | 2026-07-30 01:28:46 | PASS | workflow v2 | yes | **no** (raw) | same classes |
| `MetaBOT -Leads.DB.xlsx` | 18594 | 2026-07-30 02:01:41 | PASS | RAW workbook | schema only | **no** (xlsx) | customer row data |
| `MetaBOT -Leads_Manager.DB.xlsx` | 19401 | 2026-07-30 02:01:55 | PASS | CLEAN workbook | schema only | **no** (xlsx) | customer row data |

Raw SHA256: see `baselines/SOURCE-SANITIZATION-MANIFEST-v1.md`.

---

## 4. Raw Source Validation

| Item | V1 | V2 |
|------|----|----|
| Workflow name | `Sales-Manager-v1` | `Sales-Manager-v2` |
| Active (export) | false | false |
| Node count | 19 | 19 |
| Unique names | 19 | 19 |
| Broken connections | 0 | 0 |
| HTTP AI nodes | 2 | 2 |
| Code nodes | 6 | 6 |
| Gmail nodes | 5 | 5 |
| Sheets nodes | 3 | 3 |
| Telegram nodes | 1 | 1 |
| Settings | `executionOrder=v1`, `binaryMode=separate` | same |

No workflow code executed. No endpoints called.

---

## 5. Sanitization

Sanitized outputs promoted to Git:

- `baselines/Sales-Manager-v1.sanitized.json` — SHA256 `A1C9FD0607E9D7F6866CF491EFF7673070DC3BD3AE2703E6E65EF1212A915EB5`
- `baselines/Sales-Manager-v2.sanitized.json` — SHA256 `AD90715FD14B6F8EF568BCBD69CC0F123D41FF024296AD3E54D3B9FD11AB821C`

Placeholders applied per contract. Secret/PII residue scan: **PASS** (no bearer residue, no raw chat/label/workbook ids, no email PII).

OpenRouter material: discussed only as `<OPENROUTER_CREDENTIAL>` / redacted Authorization — **not** rotated or printed.

---

## 6. Sanitized Workflow Baselines

Valid JSON · unique node ids/names · connection integrity · known node types · expressions/code preserved · placeholder syntax intact.

Exact Russian sheet node names retained:

- `Запись лида (RAW)` → sheet `lead-base` / `<RAW_WORKBOOK_ID>`
- `Осмысленные лиды (CLEAN)` → sheet `lead-base-processed` / `<CLEAN_WORKBOOK_ID>`

---

## 7. V1/V2 Comparison

Node set and connection graph are **identical** (19 nodes, 18 edges). Material deltas are **code/parameter** changes:

| Area | Class |
|------|-------|
| Expanded Lead-Mail-Parser (2059→5939 chars) | IMPROVEMENT + residual DEFECT |
| Expanded AI prepare prompts | IMPROVEMENT / dual-AI retained DEFECT |
| Unchanged Normalize-AI-Result | NEUTRAL + DEFECT (discards quality fields) |
| Expanded AI #2 prepare | REGRESSION driver |
| Dual AI retained | DEFECT |
| Active false both | SAFE UNKNOWN live |

Full table: `baselines/SALES-MANAGER-V1-V2-COMPARISON-v1.md`.

---

## 8. V2 Node Inventory

19 nodes inventoried with type, typeVersion, role, upstream/downstream, side effects, credential category, Operational.dev disposition, risks.

Explicit anchors confirmed: RAW parallel write · two-call AI · discarded AI #1 quality fields · missing CLEAN first reply · full-table duplicate lookup · Telegram happy-path-only finalization · Gmail label branches.

---

## 9. V2 Connection Map

Documented in `baselines/SALES-MANAGER-V2-CONNECTION-MAP-v1.md`. Key: parser fans out to RAW and AI chain; PROCESSED only after Telegram node with **no** failure catch; ERROR path removes incoming.

---

## 10. RAW Workbook Findings

| Field | Value |
|-------|-------|
| Sheet | `lead-base` |
| Rows | 19 |
| Headers | 20 (includes four AI columns) |
| AI fill | 0% |
| email_subject | UNKNOWN 19/19 |
| client_contact errors | 6 |
| Overflow-suspect names | 8 |

---

## 11. CLEAN Workbook Findings

| Field | Value |
|-------|-------|
| Sheet | `lead-base-processed` |
| Rows | 19 |
| Headers | 14 (no first_reply / priority / AI meta) |
| quality_status | ok 19/19 |
| duplicate_status | new 12 / repeat 7 |
| manager_status | new 19/19 |
| primary_contact formula-like | 10 |

---

## 12. Data Quality Findings

See `baselines/SHEET-DATA-QUALITY-FINDINGS-v1.md` (Q1–Q10). No customer-identifying values published.

---

## 13. Implementation Package Reconciliation

| Spec area | Result |
|-----------|--------|
| Operational target architecture | Confirmed correct vs Phase 2; no redesign |
| Source node names / typeVersions | **Updated** mapping table in OPERATIONAL patch spec |
| AI #2 removal | Confirmed required by export |
| RAW branch timing / AI columns | Confirmed defect; spec already targeted |
| Gmail label / Telegram success gate | Spec already targeted; export proves missing fail gate |
| Sheets historical headers | Evidence added to SHEETS migration note |
| Dedupe full-table | Confirmed; DEDUP spec note added |
| MetaBOT Programmer grammar | Unchanged; baselines now available |
| Sandbox disabled defaults | Reaffirmed |
| Credential placeholders | Aligned |

---

## 14. Sandbox Gate Revalidation

Gate **revalidated** and remains **closed**.

Technically ready for operator review: **YES**.  
Phase 3B auto-approval: **NO**.

Pending operator items: live workflow id; RAW/CLEAN live confirmation; manager/admin chat decisions; auth for v2 tabs; auth for two .dev workflows; read-only n8n; synthetic tests; original untouched; AI OFF first runs; sandbox≠prod chats.

Item 11 (source drop + sanitized promotion): **DONE**.

---

## 15. Files Created

- `baselines/Sales-Manager-v1.sanitized.json`
- `baselines/Sales-Manager-v2.sanitized.json`
- `baselines/SALES-MANAGER-V2-NODE-INVENTORY-v1.md`
- `baselines/SALES-MANAGER-V2-CONNECTION-MAP-v1.md`
- `baselines/RAW-SHEET-SCHEMA-BASELINE-v1.md`
- `baselines/CLEAN-SHEET-SCHEMA-BASELINE-v1.md`
- `baselines/SHEET-DATA-QUALITY-FINDINGS-v1.md`
- `reports/REPORT-iseo-sales-manager-bot-phase3a1-source-ingest-and-sanitized-baselines-v1.md`

---

## 16. Files Changed

- `baselines/SOURCE-GAP-MANIFEST-v1.md` (CLOSED)
- `baselines/SOURCE-SANITIZATION-MANIFEST-v1.md` (executed)
- `baselines/SALES-MANAGER-V1-V2-COMPARISON-v1.md` (exact)
- `README.md`
- `OPERATIONAL-INDEX.md`
- `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`
- `implementation/SANDBOX-APPLY-GATE-v1.md`
- `implementation/METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1.md`
- `implementation/SHEETS-MIGRATION-SPEC-v1.md`
- `implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md`

Historical Phase 3A report **not** rewritten.

---

## 17. Security Validation

| Check | Result |
|-------|--------|
| No raw XLSX in Git | PASS |
| No unsanitized JSON in Git | PASS |
| No API keys / Authorization secrets | PASS |
| No real chat / workbook / label ids | PASS |
| No lead PII in docs | PASS |
| OpenRouter credential not discussed beyond placeholder | PASS |

---

## 18. Git Isolation

Clean temporary worktree based on `origin/mars/canonical-post-recovery`. Main dirty index and foreign WIP untouched. Allowlist: `projects/iseo-sales-manager-bot/**` only.

---

## 19. Commit

Primary scoped commit: `86642ad727151c4dc63b3332984c1d5c8b253b7b`  
Message: `docs(iseo-sales-manager-bot): add sanitized source baselines`

---

## 20. Push

Pushed to `origin/mars/canonical-post-recovery` (no force).  
Primary remote tip after main commit: `86642ad727151c4dc63b3332984c1d5c8b253b7b`  
This report section was refreshed in a follow-up hash-record commit on the same branch.

---

## 21. Risks

| Risk | Mitigation |
|------|------------|
| Export inactive ≠ live inactive | Phase 3B read-only attest |
| Export drift vs live graph | Re-export before patch |
| Residual PII if docs expanded carelessly | Keep aggregates only |
| Operator skips gate confirmations | Gate remains closed |

---

## 22. SAFE UNKNOWN

- Live active state and exact live workflow id  
- Whether RAW/CLEAN export workbooks are the current production pair  
- Exact n8n server version  
- Admin workflow export (not in drop)  
- Exact parser build ids (no `parser_version` column)

---

## 23. Remaining Operator Confirmations

1–10 and 12–13 in `implementation/SANDBOX-APPLY-GATE-v1.md` (item 11 done).

---

## 24. Recommended Next Phase

**PHASE 3B — LIVE READ-ONLY AUDIT AND DEV WORKFLOW CREATION**  
Only after explicit operator approval of the revalidated sandbox gate.

---

## 25. Production Boundary

| Boundary | Count / state |
|----------|----------------|
| live n8n access | none |
| workflow copies created | 0 |
| Google Sheets mutations | 0 |
| Gmail mutations | 0 |
| Telegram mutations | 0 |
| real leads processed | 0 |
| production mutations | 0 |

---

## 26. Stop Condition

Stopped after source ingest, sanitization, reconciliation, scoped commit, push, and this report.  
Did not access live n8n, create workflow copies, create Sheets tabs, modify Gmail labels, send Telegram messages, process real leads, or begin Phase 3B.
