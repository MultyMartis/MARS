# REPORT — ISEO SALES MANAGER BOT PHASE 3B LIVE AUDIT AND DEV CONTOUR

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT — PHASE 3B LIVE AUDIT AND DEV CONTOUR CREATION  
**Date:** 2026-07-30

---

## 1. Verdict

**PHASE 3B COMPLETE — READY WITH PENDING SANDBOX TESTS**

Dev contour created (exactly two inactive workflows), v2 Sheets tabs created with validated headers, structural + local synthetic AI OFF/ON/dedupe/formatter tests passed, production Sales-Manager-v2 unchanged. Telegram sandbox delivery and live end-to-end n8n fixture runs remain pending operator sandbox chat approval.

---

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X: | `AI WS` |
| Main branch | `mars/canonical-post-recovery` |
| Main HEAD (dirty WIP) | `ecfd0675…` (foreign unpushed commits present — not used for this phase) |
| Starting remote tip | `34a9e04a4de87b5ef5f332cfa55fabf994e6edee` |
| Clean worktree | `X:\AI MARS STORAGE\worktrees\iseo-sm-phase3b` @ `34a9e04a` branch `tmp/iseo-sm-phase3b` |
| Main foreign WIP | preserved (not staged/restored/cleaned) |
| n8n API contour | `local/tokens/n8n-api.env` present |
| Baseline v2 SHA256 | `AD90715FD14B6F8EF568BCBD69CC0F123D41FF024296AD3E54D3B9FD11AB821C` (match) |

---

## 3. Authority and Evidence Read

Authoritative project docs under `projects/iseo-sales-manager-bot/` (architecture, implementation specs, baselines including Phase 3A.1 sanitized JSON). MetaBOT Programmer grammar/rules and Client Ops n8n write/create patterns reused. Guardrails: `projects/mars-survivability/guardrails/cursor-agent-guardrails-v1.md`.

---

## 4. Live Workflow Identification

| Field | Value |
|-------|-------|
| Name | `Sales-Manager-v2` |
| ID | `h8I2Tl2yl4uzhUnB` |
| Active | **true** (left unchanged) |
| Nodes | 19 |
| Edges | 18 |
| Parity | **PARITY** vs Phase 3A.1 node inventory / connection map |
| Legacy also present | inactive `Sales-Manager-v1` (not modified) |

---

## 5. Live vs Baseline Comparison

Node names, types/typeVersions, and connection graph: identical. Activation differs from sanitized export (`active=false` in export vs live `true`) — classified as non-blocking SAFE LIVE DRIFT on activation metadata only. No BLOCKING DRIFT.

---

## 6. Dependency Audit

| Role | Resolution |
|------|------------|
| RAW workbook | Distinct from CLEAN (hash `0b12c1bd6cbb`); historical `lead-base` |
| CLEAN workbook | Distinct (hash `1d0c5e6cb820`); historical `lead-base-processed` |
| Manager Telegram | Credential `Telegram account - Sales Manager for i-SEO` |
| Admin Telegram | Same Sales Manager bot recommended; Admin Trigger kept **disabled** pending coexistence decision |
| Gmail labels | Incoming / PROCESSED / ERROR bound (IDs local-only) |
| OpenRouter | Inline HTTP auth present on live AI nodes — **not** discussed/rotated |

---

## 7. Pre-Change Backup

Local-only: `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\backups\pre-dev-copy\`  
Includes raw + sanitized live export; raw SHA recorded in LIVE-AUDIT-SUMMARY (Storage). Production not modified for backup.

---

## 8. Operational.dev Creation

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Operational.dev` |
| ID | `xSnXPy8cEHoZw6xG` |
| Active | **false** |
| Nodes | 29 |
| Source | Exact live Sales-Manager-v2 copy + Operational patch |
| Schedule | disabled |
| OpenRouter | single node, disabled; AI OFF path has no executable connection |
| AI #2 | removed from .dev only |
| Telegram send | disabled |
| Gmail mutate | disabled |

---

## 9. Admin.dev Creation

| Field | Value |
|-------|-------|
| Name | `i-SEO Sales Manager - Admin.dev` |
| ID | `wLrLp4WQHm1VJmxz` |
| Active | **false** |
| Nodes | 22 |
| Pattern | MetaBOT v14 Admin (SEO locks removed) |
| Auth | fail-closed allowlist (`admin_user_ids`) |
| Commands | `/help` `/status` `/ai_status` `/ai_on` `/ai_off` `/health` `/stats` `/test_lead` `/last_error` `/config` |
| Telegram Trigger / Reply | disabled pending sandbox destination / coexistence |

---

## 10. Workflow Count Gate

New project workflows: **exactly 2**. No retained disposable clones. One accidental empty probe workflow during API capability probe was deleted immediately.

---

## 11. Sheets Tabs

Created/validated:

- RAW: `lead_raw_v2` (headers 29/29)
- CLEAN: `lead_clean_v2`, `CONFIG`, `LEAD_EVENTS`, `ERRORS`, `DEDUP_INDEX` (headers match spec)
- Historical tabs preserved
- `STATS_DAILY` not created

---

## 12. Configuration

CONFIG defaults include `ai_enabled=false`, `environment=dev`, `health_ai_probe_enabled=false`, placeholder chat ids, empty admin allowlist (fail-closed). No secrets stored.

---

## 13. Synthetic Tests

| Fixture | Mode | Expected | Actual | Result |
|---------|------|----------|--------|--------|
| STRUCT | structure | G1–G11 structural | 29 nodes; AI#2 absent; TG fail≠PROCESSED | PASS |
| F05 AI OFF | AI OFF | template, no OpenRouter | ai_off / skipped / Audit | PASS |
| F06 AI OFF | AI OFF | named SEO template | ai_off / skipped / SEO | PASS |
| F01 AI OFF | AI OFF | phone-only deterministic | ai_off / skipped | PASS |
| DEDUP F12 | dedupe | reprocessed/same_message | reprocessed/same_message | PASS |
| DEDUP F13 | dedupe | repeat/phone | repeat/phone | PASS |
| DEDUP F14 | dedupe | possible/site_only | possible/site_only | PASS |
| DEDUP invalid | dedupe | reject `44` / `#ERROR!` | rejected | PASS |
| AI invalid JSON | AI ON mocked | fallback | ai_fallback | PASS |
| AI unsafe promise | AI ON mocked | fallback | unsafe_promise→fallback | PASS |
| Telegram chars | telegram | escaped; no raw enums | escaped; separators | PASS |

---

## 14. AI OFF Zero-Token Validation

Graph: IF AI Enabled false → Merge AI or Fallback (no OpenRouter). OpenRouter node disabled. Local AI OFF fixtures executed without HTTP provider calls.

---

## 15. AI ON and Fallback Validation

Provider-backed OpenRouter calls: **not** performed (`health_ai_probe_enabled=false`). Mocked invalid JSON + unsafe promise → deterministic fallback: PASS.

---

## 16. Dedupe Validation

reprocessed / repeat / possible / invalid-key rejection: PASS (local harness).

---

## 17. Telegram Validation

Formatter: PASS (HTML escape, Russian maps, copy-ready separators).  
Delivery: **PENDING** — no approved sandbox destination; send nodes disabled; production manager chat not used.

---

## 18. Gmail Label Safety

No real Gmail label mutations. Graph: success → PROCESSED + remove incoming; TG fail → ERROR + Preserve Incoming (no PROCESSED).

---

## 19. Healthcheck

| Check | Result |
|-------|--------|
| CONFIG readable | PASS (headers + defaults) |
| RAW/CLEAN/EVENTS/ERRORS/DEDUP v2 readable | PASS |
| Gmail credential ref present on Operational | PASS (disabled mutate) |
| Telegram sandbox | PENDING / disabled |
| AI status | OFF |
| AI provider probe | SKIPPED |

---

## 20. Original Workflow Integrity

Verdict: **ORIGINAL_UNCHANGED** — same ID/name/active/node/edge counts after all .dev work.

---

## 21. Files Created

Under `projects/iseo-sales-manager-bot/`:

- `evidence/phase3b/LIVE-AUDIT-MANIFEST-v1.md`
- `evidence/phase3b/LIVE-VS-BASELINE-DIFF-v1.md`
- `evidence/phase3b/DEV-WORKFLOW-MANIFEST-v1.md`
- `evidence/phase3b/SHEETS-TAB-CREATION-EVIDENCE-v1.md`
- `evidence/phase3b/SYNTHETIC-TEST-RESULTS-v1.md`
- `evidence/phase3b/ORIGINAL-WORKFLOW-INTEGRITY-v1.md`
- `evidence/phase3b/PHASE3B-APPLY-RECEIPT-v1.md`
- `evidence/phase3b/Operational.dev.sanitized.json`
- `evidence/phase3b/Admin.dev.sanitized.json`
- `reports/REPORT-iseo-sales-manager-bot-phase3b-live-audit-and-dev-contour-v1.md`

---

## 22. Files Changed

- `README.md`
- `OPERATIONAL-INDEX.md`
- `implementation/SANDBOX-APPLY-GATE-v1.md`
- `plans/ROLLBACK-PLAN-v1.md`

---

## 23. Security Validation

Git paths contain no raw credentials, raw workbook/chat/label IDs, XLSX, or real lead PII. Raw backups remain Storage-local only. OpenRouter credential not printed/rotated.

---

## 24. Git Isolation

Temporary worktree from `origin/mars/canonical-post-recovery`. Main index untouched. Foreign WIP preserved.

---

## 25. Commit

See git section after push wave (primary + optional hash-record if required).

---

## 26. Push

Target: `origin/mars/canonical-post-recovery` (no force).

---

## 27. Risks

- Production remains active on 30s schedule (pre-existing).
- Admin Telegram Trigger coexistence with manager bot unresolved — left disabled.
- Operational Sheets write / Gmail / Telegram nodes still disabled pending sandbox acceptance.
- Earlier mistaken CLEAN create attempt targeted wrong outcome until corrected; final CLEAN titles verified on correct workbook.

---

## 28. SAFE UNKNOWN

- Exact production manager chat approval for any future sandbox ping.
- Whether Sales Manager Telegram Trigger can safely share one bot with Admin when both active.
- Full live n8n execution of synthetic fixtures through Sheets append nodes (local Code harness used).

---

## 29. Required Operator Decisions

1. Approve dedicated sandbox Telegram destination (or keep send disabled).
2. Decide Admin Trigger activation model (shared bot vs keep Admin inactive).
3. Optionally enable bounded synthetic Sheets writes on Operational.dev for live sandbox acceptance.

---

## 30. Recommended Next Phase

**PHASE 3B.1 — COMPLETE PENDING SANDBOX TESTS**  
(or PHASE 3C after sandbox chat + live fixture acceptance). Do not promote to production.

---

## 31. Production Boundary

| Metric | Count |
|--------|-------|
| original workflows modified | 0 |
| new workflows created | 2 |
| workflows activated for production use | 0 |
| real leads processed | 0 |
| real Gmail labels modified | 0 |
| real client messages sent | 0 |
| production manager messages sent | 0 |
| new Sheets tabs created | 6 (`lead_raw_v2` existed empty→headers; 5 CLEAN created) |
| synthetic rows written | CONFIG defaults only (no lead PII) |
| production mutations | 0 |

---

## 32. Stop Condition

Stop after live audit, two .dev workflows, approved v2 tabs, synthetic validation, evidence, scoped commit/push and this report. No Phase 3C. No activation of .dev for production. No modification of Sales-Manager-v2.

---

## Execution safety

- cwd: `X:\AI MARS` / clean worktree under Storage
- scope lock honored: yes
- destructive ops: none (accidental probe workflow deleted only)
- protected zone touch: none
