# REPORT — ISEO SALES MANAGER BOT PHASE 3D PRODUCTION STABILIZATION AND OLYA HANDOFF

**Date:** 2026-07-31  
**Project:** `projects/iseo-sales-manager-bot/`  
**Contour:** `n8n.ai-metacode.com`

## 1. Verdict

**ATTENTION — CLEAN TEST LEAD FAILED**

Stabilization (incident closeout, exactly-once audit, idempotency/retry guard), Admin acceptance, Olya guide, and operator runbook are done. The required clean valid-contact website test lead was **not submitted** during the bounded readiness window (0 lead chains / 32 empty polls). Contour remained healthy; no new flood.

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Origin tip / worktree | `origin/mars/canonical-post-recovery` @ `0a0294fb` |
| Worktree | `X:\AI MARS STORAGE\worktrees\iseo-sm-phase3d-20260731-230553` |
| Dirty main WIP | present (foreign) — **not mutated** |
| Named Sales/i-SEO workflows | 4 (includes legacy inactive Sales-Manager-v1) |
| Production contour | Sales-Manager-v2 + Operational.dev + Admin.dev (IDs unchanged; hashes only in private Storage notes) |

## 3. Incident Closeout

Phase 3C.2 flood window closed with sanitized matrix (see `evidence/phase3d/RETRY-FLOOD-INCIDENT-CLOSEOUT-v1.md`):

- 1 unique Gmail message · 25 lead chains · 25 Telegram attempts · **6** successful sends (~5 duplicate cards) · 1 terminal PROCESSED · AI **0**.

## 4. Exactly-Once Audit

Delivery exactly-once after successful Telegram is enforced via CONFIG idempotency keys + skip branch. Exact DEDUP `normalized_value` matching patched. CLEAN remains append-on-retry (documented residual). Details: `EXACTLY-ONCE-SAFETY-AUDIT-v1.md`.

## 5. Retry/Flood Guard

Patched on Operational.dev (same IDs; **0** new workflows):

- `IF Need Telegram Send` + `Telegram Skip Pass`
- CONFIG `tg_delivered:<gmail_message_id>` / `tg_attempts:<gmail_message_id>`
- Max attempts **5** → `telegram_retry_exhausted`
- Resume Gmail finalize without resend when already delivered

## 6. Clean Test Lead

Readiness notice **sent**. Observe window ~15 min: **0** leads. Acceptance checklist pending operator submission.

## 7. Gmail Eligibility

No new eligible messages in the observe window. Production incoming query unchanged. Filters not mutated (**0**).

## 8. Operational Execution

Sole intake Operational.dev; empty polls healthy; Sales-Manager-v2 inactive throughout.

## 9. RAW/CLEAN/Event Writes

No new business writes in observe window. Incident window showed append-per-retry RAW/CLEAN/DEDUP and LEAD_EVENTS on successful Telegram attempts.

## 10. Telegram Delivery

Idempotency guard live. No new production cards in observe window. Historical flood duplicates closed as incident.

## 11. Gmail Finalization

Policy unchanged: PROCESSED + incoming remove only after Telegram success (or idempotent skip-success resume).

## 12. AI OFF Evidence

Admin `/ai_status` / `/config` / `/health`: AI off; probe disabled. OpenRouter not executed on observe polls (**0**).

## 13. Telegram UX Review

Reviewed finalized production card shape (exec flood-finalization path): required sections present; no synthetic footer; no internal IDs; no raw enums. Fresh clean-lead UX still pending. No wording change.

## 14. Olya Working Model

Cards → CONFIG manager destination; Оля needs read access there; no n8n/Gmail/credentials; manual copy reply; Sheets lifecycle; Admin allowlist **not** expanded.

## 15. Olya Guide

Created: `guides/OLYA-LEAD-WORK-GUIDE-v1.md` (12 required sections, Russian, no secrets).

## 16. Operator Runbook

Created: `guides/OPERATOR-RUNBOOK-v1.md` (Admin commands, failure ID, rollback, dual-active avoidance, evidence).

## 17. Monitoring Baseline

Defined 7-day Admin `/stats` + CONFIG timestamps metrics in `PRODUCTION-MONITORING-BASELINE-v1.md`. No monitoring workflow added.

## 18. Admin Acceptance

`/status` `/health` `/stats` `/last_error` `/config` `/ai_status` authorized and answered. Working contour; AI off; SYNTHETIC excluded; last error historical (not active synthetic incident). Clean lead not yet in stats.

## 19. Workflow Naming

**Deferred** — wait for clean-lead acceptance; avoid Trigger registration risk. Sales-Manager-v2 not renamed.

## 20. Project Status

Registry status remains **planned**. Promotion to active/production requires a **separate governance gate** (not opened). No registry path mutated.

## 21. Final Workflow State

| Workflow | Active |
|----------|--------|
| Sales-Manager-v2 | false |
| Operational.dev | true |
| Admin.dev | true |
| Sales-Manager-v1 (legacy) | false |

environment=production · ai_enabled=false

## 22. Workflow Count Gate

No new workflows created. Legacy v1 remains inactive pre-existing. Active Gmail intake count = **1**.

## 23. Files Created

- `evidence/phase3d/*` (10 receipts)
- `guides/OLYA-LEAD-WORK-GUIDE-v1.md`
- `guides/OPERATOR-RUNBOOK-v1.md`
- this REPORT

## 24. Files Changed

- `README.md`
- `OPERATIONAL-INDEX.md`
- `plans/ROLLBACK-PLAN-v1.md`
- `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`

## 25. Security Validation

No credentials, Telegram/Gmail/workbook/label IDs, PII, raw execution payloads, or unsanitized exports in git paths.

## 26. Git Isolation

Clean worktree from `origin/mars/canonical-post-recovery`; allowlist `projects/iseo-sales-manager-bot/**`; foreign WIP untouched.

## 27. Commit

`6aeb918e` — `feat(iseo-sales-manager-bot): stabilize production and prepare olya handoff` (17 paths under `projects/iseo-sales-manager-bot/**`)

## 28. Push

Pushed to `origin/mars/canonical-post-recovery` (`0a0294fb..6aeb918e`, no force).

## 29. Risks

- Clean valid-contact lead still unverified end-to-end.
- CLEAN Sheets node still appends on retries (row duplication possible; Telegram fan-out guarded).
- CONFIG accumulates per-message delivery keys (v1 acceptable).
- `/status` last-lead timestamp may lag relative to flood-finalized lead (observability nuance).
- Оля Telegram destination membership needs operator confirmation.

## 30. SAFE UNKNOWN

- Exact Olya membership in current manager Telegram destination.
- Historical Trash actor (unchanged).
- Whether registry row exists outside documented “planned” claim (no `iseo-sales-manager-bot` line found in `registry/project-registry.md` during this pass).

## 31. Remaining Operator Actions

1. Submit **one** clean website test lead (test name + valid contact + SEO/Audit + no real client data).  
2. Confirm exactly one Telegram card and no duplicates across several polls.  
3. Confirm Оля can read the manager destination.  
4. Optional: approve `.dev` rename after clean-lead acceptance.  
5. Optional later: registry promotion charter.

## 32. Recommended Next Phase

**PHASE 3E — CONTROLLED AI ON PILOT** — only after clean-lead acceptance **and** separate operator approval.

## 33. Production Boundary

| Item | Value |
|------|-------|
| Sales-Manager-v2 active | false |
| Operational active | true |
| Admin active | true |
| Active Gmail intake count | 1 |
| Clean test leads processed | 0 (pending) |
| Telegram production cards (this phase window) | 0 new |
| Duplicate cards (incident window, closed) | ~5 estimated |
| Gmail label changes (this phase) | 0 new messages |
| Automatic client messages | 0 |
| AI provider calls | 0 |
| New workflows | 0 |
| Rollback | no |

## 34. Stop Condition

Stop after stabilization patch, readiness notice + observe window, Olya/operator guides, evidence, commit, push and report. Do not enable AI. Do not reactivate Sales-Manager-v2. Do not add Оля to Admin allowlist. Do not create workflows. Do not automatically contact clients.
