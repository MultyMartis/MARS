# REPORT — ISEO SALES MANAGER BOT PHASE 3C.1 FIRST REAL LEAD INTAKE FAILURE DIAGNOSIS

**Date:** 2026-07-31  
**Project:** `projects/iseo-sales-manager-bot/`  
**Contour:** `n8n.ai-metacode.com`

## 1. Verdict

**PHASE 3C.1 COMPLETE — INTAKE REPAIRED, NEW TEST LEAD REQUIRED**

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\\AI MARS` |
| Volume | `X:` label **AI WS** |
| Dirty main WIP | present (foreign) — **not mutated** |
| Worktree | `X:\\AI MARS STORAGE\\worktrees\\iseo-sm-phase3c1-20260731-174754` @ `origin/mars/canonical-post-recovery` |
| n8n host | `n8n.ai-metacode.com` |

## 3. Operator Incident

Real website test on 2026-07-31 produced no Telegram lead card. Admin `/status` still showed last success/error **30.07.2026 22:49 МСК**. `/health` previously reported credential binding without a working query.

## 4. Test Email Delivery

**Found: yes.** Post-cutover automated-form-like mail exists (newest `2026-07-31T08:50:05.000Z`). Candidates are in **Trash**, without incoming/PROCESSED/ERROR labels.

## 5. Recent Executions

OPS polls ~every **30s** with Gmail Fetch **0 items** (sampled). PROD post-cutover executions: **0**. No Telegram lead sends in sampled window.

## 6. Trigger State

Schedule Trigger enabled and connected to Gmail Fetch Leads. No reconnect patch required.

## 7. Gmail Credential Binding

Credential reference present; hash parity with Sales-Manager-v2; bounded reads succeed. Not a stale-binding outage.

## 8. Gmail Filter Parity

Operational filter `labelIds` equals v2. Real candidates **lack** that label → excluded correctly by production boundary.

## 9. Label State

Trash=yes; incoming=no; PROCESSED=no; ERROR=no; custom labels=0. No post-cutover v2 processing evidenced.

## 10. Root Cause

Stopped at **Gmail label/query eligibility**: delivered form mail never became eligible for the accepted incoming-label intake (and sits in Trash).

## 11. Repair

Patched **same** Operational.dev + Admin.dev (no new workflow): Intake Gate / Switch for empty+error routes; `last_poll_success_at`; Admin Gmail health query wording; Error Handler stage vocabulary. Filter **not** broadened. No untrash/relabel.

## 12. Controlled Reprocessing

**Not performed** — message unlabeled + in Trash; safety contract forbids broad restore/relabel. New website test required.

## 13. First Real Lead Acceptance

**Pending** — not processed end-to-end.

## 14. RAW/CLEAN/Event Writes

For this incident lead: **0 / 0 / 0**.

## 15. Telegram Delivery

Production lead cards for this incident: **0**.

## 16. Gmail Label Finalization

No PROCESSED add / incoming remove for this lead (never reached Telegram success).

## 17. AI OFF Evidence

OpenRouter disabled; provider calls observed **0**; automatic client messages **0**.

## 18. Early Failure Observability

Empty polls now update `last_poll_success_at`. Gmail read failures route toward Error Handler / ERRORS / last_error_*. Stages documented in evidence.

## 19. Healthcheck Improvement

Verified production wording:

- `Gmail: доступен, запрос выполнен`
- `Найдено подходящих писем: 0`

## 20. Final Workflow State

Sales-Manager-v2 **false** · Operational.dev **true** · Admin.dev **true** · AI OFF · one operational active.

## 21. Rollback Status

**No rollback.**

## 22. Files Created

`evidence/phase3c1/*` + this REPORT.

## 23. Files Changed

README, OPERATIONAL-INDEX, HEALTHCHECK-CONTRACT, OPERATIONAL/ADMIN patch specs, ROLLBACK-PLAN (scoped notes).

## 24. Security Validation

No credentials, Gmail bodies, PII, Telegram IDs, workbook/label IDs, or unsanitized raw exports in git evidence.

## 25. Git Isolation

Clean worktree from `origin/mars/canonical-post-recovery`; allowlist `projects/iseo-sales-manager-bot/**`; foreign WIP untouched.

## 26. Commit

(filled after commit)

## 27. Push

(filled after push)

## 28. Risks

- Incoming-label Gmail automation may still be broken/misaligned — operator must verify before next test.
- Historical `last_error_at` may remain an older Telegram failure until superseded.
- Exact Trash actor remains SAFE UNKNOWN.

## 29. SAFE UNKNOWN

- Which system moved candidates to Trash.
- Whether website subject/from still matches the historical Gmail filter that applies the incoming label.

## 30. Remaining Operator Action

1. Verify Gmail filter applies incoming leads label to website form mail.  
2. Submit a new website test (do not rely on trashed unlabeled messages).  
3. Confirm Telegram card + `/status` lead timestamp.

## 31. Recommended Next Phase

**PHASE 3C.2 — FIRST REAL LEAD ACCEPTANCE AFTER LABEL ELIGIBILITY CONFIRMATION**

## 32. Production Boundary

- old final active: **false**
- new final active: **true**
- Admin final active: **true**
- real Gmail messages inspected (bounded): **≤25 per probe; distinct post-cutover candidates: 2**
- real leads processed: **0**
- Gmail labels changed by this phase: **0**
- Telegram production cards: **0**
- automatic client messages: **0**
- AI provider calls: **0**
- rollback: **no**

## 33. Stop Condition

Stop after diagnosis, minimal observability repair, evidence, commit, push and report. Do not begin additional feature work.
