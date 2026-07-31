# REPORT — ISEO SALES MANAGER BOT PHASE 3D.2.1 ADMIN DUPLICATE REPLY AND RUNTIME STATE CLOSEOUT

**Date:** 2026-08-01  
**Project:** `projects/iseo-sales-manager-bot/`  
**Contour:** `n8n.ai-metacode.com`

## 1. Verdicts

**COMPLETE — DUPLICATE START WAS EXPECTED TEST OVERLAP**

**PHASE 3D.2.1 COMPLETE — PRODUCTION CLOSEOUT CLEAN**

(Harness + runtime fix + backfill accepted. Operator-typed Telegram Trigger re-matrix remains a human follow-up, same class as Phase 3D.2.)

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch (worktree) | `temp/iseo-sm-phase3d21-*` @ `origin/mars/canonical-post-recovery` |
| Dirty main WIP | present (foreign) — **not mutated** |
| Named Sales/i-SEO workflows | 4 |
| Production gate trio | v2 inactive · Operational active · Admin active |

## 3. Duplicate `/start` root cause

Two identical Start panels during Phase 3D.2 acceptance came from **two deliberate live-harness executions** (`auth_start` + `auth_start_suffix`) via temporary webhook → Normalize Command → Safe Telegram Reply. Telegram Trigger count for `/start` in that window: **0**. Retries: **0**. Reply node runs per execution: **1**.

Classification: **expected_harness_overlap**.

## 4. Idempotency patch decision

**No Admin command idempotency guard** — defect class was harness overlap, not same-update reprocessing.

## 5. n8n attribution footer

Permanent Admin/Ops Telegram send nodes re-asserted `appendAttribution=false`. Phase 3D.2.1 readiness sidecar forced the same. No credential change.

## 6. Canonical commands

Help already advertises `/ai_status` (not `/aistatus`). Readiness notice lists `/start` `/status` `/help` `/config` only. Aliases remain internal in Normalize Command.

## 7. Runtime-state forensic

Clean lead `F14196515232982B` had `telegram_ok=true` at Telegram Result Gate, but **Update Last Success / Runtime State** read the post-Gmail stub (`id`/`threadId`/`labelIds`) and wrote **error** keys (`processing_error`) instead of `last_lead_success_at`. `/status` therefore kept the stale **30.07.2026 22:49 МСК** lead stamp.

## 8. Runtime fix + backfill

- Patched Update node: prefer Telegram Result Gate; empty-poll isolation; monotonic newest success.
- Safe CONFIG backfill to `2026-07-31T17:47:40.000Z` → operator display **31.07.2026 20:47 МСК**.
- No Gmail replay, no Telegram resend, no RAW/CLEAN rows.

## 9. Real Telegram / harness results

| Check | Result |
|-------|--------|
| Live harness `/start` | PASS |
| Unauthorized `/start` | PASS (`Доступ запрещён.`) |
| `/help` canonical | PASS |
| `/config` `sm-parser-v3.1` | PASS |
| `/status` lead 31.07.2026 20:47 МСК | PASS |
| `/ai_status` AI OFF | PASS |
| Empty polls touch only poll stamp | PASS |
| Readiness notice sent (no attribution flag) | PASS |
| Typed Trigger matrix | PENDING (0 commands in 3 min window) |

## 10. Final active states

| Workflow | Active |
|----------|--------|
| Sales-Manager-v2 | false |
| Operational.dev | true |
| Admin.dev | true |

AI calls = **0**. Client messages = **0**. New workflows = **0**. Active Gmail intake = **1**.

## 11. Files

**Created:** `evidence/phase3d21/*` (10 docs), this report.

**Updated:** README, OPERATIONAL-INDEX, ADMIN-COMMAND-CONTRACT, HEALTHCHECK-CONTRACT, ADMIN/OPERATIONAL patch specs, TEST-HARNESS-SPEC, OPERATOR-RUNBOOK.

## 12. Security

No credentials, Telegram/Gmail IDs, phones, emails, domains, workbook IDs, or raw payloads in committed evidence.

## 13. Git

Clean worktree from `origin/mars/canonical-post-recovery`. Scoped `projects/iseo-sales-manager-bot/**` only.

Commit: `491bcc17` — `fix(iseo-sales-manager-bot): close admin reply and runtime state gaps`  
Pushed to `origin/mars/canonical-post-recovery` (no force).

## 14. STOP

Evidence, patch, acceptance (harness), commit, push, and report complete. AI remains OFF. Sales-Manager-v2 remains inactive. No Olya Admin. No client contact.
