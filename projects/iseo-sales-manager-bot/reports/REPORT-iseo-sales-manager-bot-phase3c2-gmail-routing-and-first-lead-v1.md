# REPORT — ISEO SALES MANAGER BOT PHASE 3C.2 GMAIL ROUTING REPAIR AND FIRST REAL LEAD ACCEPTANCE

**Date:** 2026-07-31  
**Project:** `projects/iseo-sales-manager-bot/`  
**Contour:** `n8n.ai-metacode.com`

## 1. Verdict

**PHASE 3C.2 COMPLETE — FIRST REAL LEAD ACCEPTED**

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch (worktree) | `temp/iseo-sm-phase3c2-*` from `origin/mars/canonical-post-recovery` |
| Dirty main WIP | present (foreign) — **not mutated** |
| Worktree | `X:\AI MARS STORAGE\worktrees\iseo-sm-phase3c2-20260731-181501` |

## 3. Incident Context

Phase 3C.1 found website-form mail in **Trash** without production incoming label → excluded by Operational `labelIds` query. This phase audited Gmail filters/external routing and unblocked end-to-end acceptance.

## 4. Affected Message Forensic

Incident candidate `2026-07-31T08:50:05Z`: Trash + IMPORTANT, no incoming/PROCESSED; sender matches filter #1 class; not restored. See `evidence/phase3c2/AFFECTED-MESSAGE-ROUTING-FORENSIC-v1.md`.

## 5. Gmail Filter Audit

2 filters; **0** Trash/delete actions; both add OPS incoming. Filter #1 matches website-form `from`. See `GMAIL-FILTER-AUDIT-v1.md`.

## 6. External Routing Check

Auto-forward off; IMAP off; POP leaveInInbox; no other active n8n Gmail intake. Trash actor remains **SAFE UNKNOWN** (not a Gmail filter). See `EXTERNAL-ROUTING-CHECK-v1.md`.

## 7. Root Cause

| Layer | Finding |
|-------|---------|
| Trash of incident mail | **Not** a Gmail filter — external/manual UNKNOWN |
| Missing eligibility (3C.1) | Incoming parent absent on Trash candidate |
| Blocked acceptance after labeling | Operational.dev **field loss**: Sheets lookup replaced lead → empty Telegram `chat_id`; stale Gmail `messageId` node refs → PROCESSED finalize failed → reprocess flood |

## 8. Gmail Routing Repair

**Gmail filters changed: 0** (already correct).  
OPS repaired: Classify Duplicate, Format Telegram, Send chatId, Gmail label messageId expressions.

## 9. Routing Dry Run

Filter #1 matches form sender; no Trash action; incoming configured. Historical Trash message not reprocessed.

## 10. New Website Test

Accepted message received `2026-07-31T11:11:41Z` (same sender class; not Trash).

## 11. Gmail Eligibility

Eligible under production incoming `labelIds`; fetched by Operational.dev.

## 12. Operational Execution

Sole intake Operational.dev; Sales-Manager-v2 inactive. Success finalization ~`2026-07-31T11:24:00Z` after OPS repairs.

## 13. RAW/CLEAN/Event Writes

RAW/CLEAN/DEDUP/LEAD_EVENTS written on process path (reprocessed status due to retry flood).

## 14. Telegram Delivery

Production card sent (`ai_off`); no synthetic footer; no internal ID leak; no automatic client reply. Possible duplicate cards during pre-fix flood.

## 15. Gmail Label Finalization

PROCESSED nested child added; incoming parent removed — only after Telegram success.

## 16. AI OFF Evidence

OpenRouter not executed; provider calls **0**; `processing_mode=ai_off`.

## 17. Admin Observability

Health/stats/last_error nodes present; live Admin spam avoided. OPS empty polls healthy after finalize. Operator may spot-check `/status` timestamps.

## 18. Final Workflow State

Sales-Manager-v2 **false** · Operational.dev **true** · Admin.dev **true** · production · AI OFF.

## 19. Workflow Count Gate

No new workflows. Two-workflow architecture preserved.

## 20. Files Created

`evidence/phase3c2/*` (12 required receipts), `architecture/GMAIL-INTAKE-FILTER-CONTRACT-v1.md`, this REPORT.

## 21. Files Changed

README, OPERATIONAL-INDEX, ROLLBACK-PLAN, OPERATIONAL-WORKFLOW-PATCH-SPEC (notes), HEALTHCHECK-CONTRACT (notes if needed).

## 22. Security Validation

No credentials, addresses, phones, domains, Gmail/Telegram/workbook/label IDs, or raw messages in git evidence.

## 23. Git Isolation

Clean worktree; allowlist `projects/iseo-sales-manager-bot/**`; foreign WIP untouched.

## 24. Commit

`fix(iseo-sales-manager-bot): repair gmail lead routing` (this wave)

## 25. Push

Pushed to `origin/mars/canonical-post-recovery` (no force) — see closeout.

## 26. Risks

- Trash actor still unknown — operator should check clients/manual habits.
- Telegram flood may have duplicated manager cards for one message.
- Accepted lead quality=`bad` (weak contacts) — still validates production path.

## 27. SAFE UNKNOWN

Exact actor that Trashed 08:50 unlabeled mail; whether any non-Gmail transport rule exists.

## 28. Remaining Operator Action

1. Confirm no client auto-Trash for website-form mail.  
2. Spot-check Admin `/status` `/health` `/stats` `/last_error`.  
3. Optional additional clean website test with valid contacts for Olya UX review.

## 29. Recommended Next Phase

**PHASE 3D — PRODUCTION STABILIZATION AND OLYA HANDOFF**

## 30. Production Boundary

- old final active: **false**
- new final active: **true**
- Admin final active: **true**
- Gmail filters changed: **0**
- real test emails inspected (bounded): **≤30 / probe window**
- real leads processed (finalized): **1**
- Gmail labels changed by n8n (finalized message): **2** (add PROCESSED + remove incoming)
- Telegram production cards: **≥1** (flood may have duplicated)
- automatic client messages: **0**
- AI provider calls: **0**
- rollback: **no**

## 31. Stop Condition

Stop after Gmail audit (no filter mutation required), OPS downstream repair, first real lead acceptance evidence, commit, push and report. Do not enable AI. Do not reactivate Sales-Manager-v2. Do not create workflows.
