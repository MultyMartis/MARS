# REPORT — ISEO SALES MANAGER BOT PHASE 3A SANITIZED BASELINE AND IMPLEMENTATION PACKAGE

**process_line:** ISEO-SALES-MANAGER-BOT — PHASE 3A SANITIZED BASELINE AND IMPLEMENTATION PACKAGE  
**date:** 2026-07-30  
**project_id:** `iseo-sales-manager-bot`

---

## 1. Verdict

**PHASE 3A COMPLETE — READY WITH SOURCE DROP REQUIRED**

Implementation package, sanitization contract, logical V1/V2 comparison, sandbox apply gate, and navigation updates are complete. Exact sanitized Sales-Manager-v1/v2 JSON baselines and XLSX-derived schema forensics are **blocked** until operator drops sources into the approved STORAGE path.

---

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume `X:` label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Main worktree HEAD (dirty) | `e1d2a178…` (diverged; foreign WIP present) |
| `origin/mars/canonical-post-recovery` | `445a1d93…` (Phase 2R registration commit) |
| Staged on dirty main | Foreign client-ops paths present — **not used as commit surface** |
| Commit surface | Clean temporary worktree from `origin/mars/canonical-post-recovery` |

**STOP tokens:** none for environment identity. Dirty main + divergence handled via temp worktree isolation.

---

## 3. Source Inventory

| # | Source role | Path / status | Type | Sensitive config | Safe for Git | Sanitization | Canonical status |
|---|-------------|---------------|------|------------------|--------------|--------------|------------------|
| 1 | Sales-Manager-v1 export | **MISSING** | — | unknown | no (raw) | required | not available |
| 2 | Sales-Manager-v2 export | **MISSING** | — | unknown | no (raw) | required | not available |
| 3 | RAW workbook XLSX | **MISSING** | — | unknown | no | schema md only | not available |
| 4 | CLEAN workbook XLSX | **MISSING** | — | unknown | no | schema md only | not available |
| 5 | Telegram examples | **MISSING** | — | possible PII | no if real | required | Phase 2 UX used |
| 6 | Phase 2 project docs | `projects/iseo-sales-manager-bot/**` | md | no | yes | n/a | **authority** |
| 7 | MetaBOT Admin sanitized | `…/exports/live-v14-evidence/2026-07-10/SEO-Content-Agent-Beta-v14-Admin.sanitized.json` | json | redacted pack | yes (existing) | done historically | Admin **pattern** only |

**Searched:** `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\` (absent→created empty drop dirs), `X:\AI MARS STORAGE\incoming\` name filter, project-local baselines/inputs.  
**Not searched:** arbitrary disks.

**Operator drop path:** `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\raw\`  
**Sanitized staging:** `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\sanitized\`

No credential values, tokens, webhook secrets, customer PII, or private spreadsheet identifiers are printed in this report.

---

## 4. Sanitization Result

| Step | Result |
|------|--------|
| Contract defined | **YES** — `baselines/SOURCE-SANITIZATION-MANIFEST-v1.md` |
| Execution on Sales Manager exports | **SKIPPED** — sources absent |
| Fake JSON reconstruction | **REFUSED** |
| Placeholders vocabulary | Defined (`<OPENROUTER_CREDENTIAL>`, Sheets/Gmail/Telegram/workbook/chat/label ids) |

---

## 5. Baseline Artifacts

| Artifact | Status |
|----------|--------|
| `Sales-Manager-v1.sanitized.json` | **BLOCKED** |
| `Sales-Manager-v2.sanitized.json` | **BLOCKED** |
| `SALES-MANAGER-V2-NODE-INVENTORY-v1.md` | **BLOCKED** (needs JSON) |
| `SALES-MANAGER-V2-CONNECTION-MAP-v1.md` | **BLOCKED** (needs JSON) |
| `RAW/CLEAN-SHEET-SCHEMA-BASELINE` from XLSX | **BLOCKED** |
| `SOURCE-GAP-MANIFEST-v1.md` | **CREATED** |
| `SOURCE-SANITIZATION-MANIFEST-v1.md` | **CREATED** |
| `SALES-MANAGER-V1-V2-COMPARISON-v1.md` | **CREATED** (logical / Phase 2 evidence) |

---

## 6. V1/V2 Comparison

Logical comparison documented: v2 dual-AI, RAW AI pretence, weak dedupe, optimistic quality, Telegram enum noise classified as defects/regressions; target Operational.dev removes AI #2, adds CONFIG + deterministic path + DEDUP_INDEX + Telegram success gate. Exact node-ID diff **SAFE UNKNOWN** until exports land.

---

## 7. Operational Patch Specification

Created: `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md` — 27 logical nodes, connections, sandbox disable defaults, Telegram-fail label policy, no Execute Workflow to Admin.

---

## 8. AI OFF Specification

Embedded in Operational patch + Phase 2 `AI-OFF-ON-CONTRACT-v1`: full deterministic outputs; service dictionaries; priority/quality rules; name/no-name reply templates; **zero** OpenRouter calls; canonical enums (`processing_mode=ai_off`, `ai_status=skipped`, `first_reply_source=template`).

---

## 9. AI ON Specification

One-call JSON schema; validation matrix; fallback reuses deterministic result; merge policy prefers stricter quality; no second normalizer LLM.

---

## 10. Admin Source Selection

Candidate: MetaBOT `SEO Content Agent Beta.v14 - Admin` sanitized (2026-07-10, 15 nodes). Reuse routing/Sheets/Telegram/health **patterns**; remove locks/stop-all-flow/SEO memory; require new allowlist auth + Sales Manager command set. **Not copied.**

---

## 11. Admin Patch Specification

Created: `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md` — 19 logical nodes; commands `/help`…`/config`; no operational Gmail processing.

---

## 12. Sheets Migration Specification

Created: `implementation/SHEETS-MIGRATION-SPEC-v1.md` — RAW `lead_raw_v2`; CLEAN `lead_clean_v2` + CONFIG + LEAD_EVENTS + ERRORS + DEDUP_INDEX; historical tabs preserved; AI default OFF in CONFIG; no Phase 3A Sheets mutation.

---

## 13. Dedupe Specification

Created: `implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md` — bounded `DEDUP_INDEX`; invalid keys rejected; `same_message`→`reprocessed`; site-only→`possible` without suppress.

---

## 14. Telegram Formatter

Created: `implementation/TELEGRAM-FORMATTER-SPEC-v1.md` — Russian maps; plain text/safe HTML; six synthetic examples; manager vs copy-ready reply separation.

---

## 15. Test Harness

Created: `implementation/TEST-HARNESS-SPEC-v1.md` — F01–F21 fixture table + Programmer gates G1–G11.

---

## 16. Sandbox Apply Gate

Created: `implementation/SANDBOX-APPLY-GATE-v1.md` — Phase 3B may/must-not; 10 operator confirmations **PENDING**; gate **closed**.

---

## 17. Files Created

- `projects/iseo-sales-manager-bot/baselines/SOURCE-GAP-MANIFEST-v1.md`
- `projects/iseo-sales-manager-bot/baselines/SOURCE-SANITIZATION-MANIFEST-v1.md`
- `projects/iseo-sales-manager-bot/baselines/SALES-MANAGER-V1-V2-COMPARISON-v1.md`
- `projects/iseo-sales-manager-bot/implementation/METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1.md`
- `projects/iseo-sales-manager-bot/implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`
- `projects/iseo-sales-manager-bot/implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md`
- `projects/iseo-sales-manager-bot/implementation/ADMIN-SOURCE-SELECTION-v1.md`
- `projects/iseo-sales-manager-bot/implementation/SHEETS-MIGRATION-SPEC-v1.md`
- `projects/iseo-sales-manager-bot/implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md`
- `projects/iseo-sales-manager-bot/implementation/TELEGRAM-FORMATTER-SPEC-v1.md`
- `projects/iseo-sales-manager-bot/implementation/TEST-HARNESS-SPEC-v1.md`
- `projects/iseo-sales-manager-bot/implementation/SANDBOX-APPLY-GATE-v1.md`
- `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-phase3a-sanitized-baseline-and-implementation-package-v1.md`

STORAGE (non-git): `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\{raw,sanitized,README.md}`

---

## 18. Files Changed

- `projects/iseo-sales-manager-bot/README.md`
- `projects/iseo-sales-manager-bot/OPERATIONAL-INDEX.md`

Registry: **not modified** (implementation not started).

---

## 19. Security Validation

| Check | Result |
|-------|--------|
| No secrets in new docs | PASS |
| No raw XLSX in Git | PASS |
| No unsanitized Sales Manager JSON | PASS (none created) |
| No real lead PII | PASS (synthetic examples only) |
| OpenRouter credential not discussed/embedded | PASS |
| Foreign WIP untouched | PASS |

---

## 20. Git Isolation

Dirty main worktree **not** used for commit. Temporary worktree from `origin/mars/canonical-post-recovery`; selective path transfer of `projects/iseo-sales-manager-bot/**` only.

---

## 21. Commit

Scoped commit (message): `docs(iseo-sales-manager-bot): prepare phase 3a implementation package`  
Exact hash: filled after commit wave.

---

## 22. Push

Target: `origin/mars/canonical-post-recovery` · no force push · filled after push wave.

---

## 23. Risks

| Risk | Note |
|------|------|
| Patching without JSON baseline | Mitigated by blocking JSON invent + Phase 3B read-only refresh |
| Enum alias drift (warning/bad vs needs_data/unusable) | Canonical Phase 2 enums mandated in brief |
| Dirty main divergence | Isolated via temp worktree |
| Operator delays source drop | Phase 3B should refresh baselines before apply |

---

## 24. SAFE UNKNOWN

- Live Sales-Manager-v2 node IDs, credentials, active state.  
- Exact RAW/CLEAN workbook document IDs.  
- One vs two Telegram bots.  
- Real header drift vs LEAD-DATA-MODEL.  
- Whether chat upload paths existed outside approved roots (not searched).

---

## 25. Required Operator Decisions

1. Drop v1/v2 exports + optional XLSX into STORAGE `raw/`.  
2. Complete SANDBOX-APPLY-GATE confirmations 1–10 before Phase 3B.  
3. Confirm manager/admin Telegram bot/chat split.  
4. Confirm sandbox workbook vs production workbook IDs.  
5. Keep AI OFF for first sandbox runs.

---

## 26. Recommended Next Phase

**PHASE 3B — LIVE READ-ONLY AUDIT AND DEV WORKFLOW CREATION**  
Only after explicit operator approval and source drop (strongly recommended before patch apply).

---

## 27. Production Boundary

No live n8n mutation, no workflow copies, no Sheets/Gmail/Telegram production side effects in Phase 3A. Original Sales-Manager-v2 remains untouched. Client auto-send remains forbidden.

---

## 28. Stop Condition

Stop after documentation, scoped commit, push, and this report.  
Do not access live n8n. Do not create workflow copies. Do not create Google Sheets tabs. Do not modify Gmail. Do not send Telegram. Do not process real leads. Do not begin Phase 3B.
