# REPORT — ISEO SALES MANAGER BOT PHASE 3D.2 PRODUCTION CLOSEOUT AND OLYA LIVE HANDOFF

**Date:** 2026-08-01  
**Project:** `projects/iseo-sales-manager-bot/`  
**Contour:** `n8n.ai-metacode.com`

## 1. Verdict

**PHASE 3D.2 COMPLETE — TECHNICAL CLOSEOUT, OLYA VISIBILITY PENDING**

Exactly-once clean lead confirmed; `/start` live (harness); next-step tautology removed; parser display aligned to `sm-parser-v3.1`; Admin/Operational remain active AI OFF. Olya destination visibility and registry promotion remain human gates. Operator-typed Telegram Trigger re-matrix pending after notice.

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch (worktree) | `temp/iseo-sm-phase3d2-*` @ `origin/mars/canonical-post-recovery` |
| Dirty main WIP | present (foreign) — **not mutated** |
| Named Sales/i-SEO workflows | 4 (v1/v2 inactive; Operational+Admin active) |
| Production gate trio | v2 inactive · Operational active · Admin active |

## 3. Pre-Patch State

- Parse Lead hash `F1067600843486FD` (= Phase 3D.1)
- Deterministic still contained tautology `Можно готовить следующий шаг.`
- Admin had no `/start`; deny text `Недостаточно прав.`
- CONFIG `parser_version` displayed `sm-parser-v3`

## 4. Clean Lead Exactly-Once

Accepted «Тест Парсер 3.1» lead:

| Stage | Attempts | Successful Business Result | Duplicate Delivery | Final State |
|-------|----------|----------------------------|--------------------|-------------|
| Gmail/parse | 1 | 1 | 0 | PARSED_v3.1 |
| Business | 1 | 1 | 0 | new |
| Telegram | 1 | 1 | 0 | DELIVERED_ONCE |
| Later polls | 49 | 0 | 0 | NO_RESEND |
| Skip/reprocess | 0 | 0 | 0 | NO_LATER_RESEND |

AI provider calls on lead: **0**. Automatic client replies: **0**.

## 5. Admin Start Contract

Authorized `/start` returns contour + AI mode dynamically (`рабочий` / `выключен` in production). `/start@bot` normalized.

## 6. Start Authorization

Unauthorized synthetic identity → `Доступ запрещён.` Harness PASS. No config/health/command leak.

## 7. Help Update

`/help` lists `/start` under «Начало»; `/test_lead` remains absent.

## 8. Next-Step UX Polish

Service-aware complete-lead guidance deployed. Formatter replay (no card resend) shows Audit line:

`Следующий шаг: Связаться с клиентом и уточнить детали аудита.`

## 9. Parser Version Alignment

Live Parse Lead remains `sm-parser-v3.1` (hash match). CONFIG updated `sm-parser-v3` → `sm-parser-v3.1`. `/config` harness shows aligned version.

## 10. Harness Results

Local harness: **18/18 PASS**. Live Admin harness: **7/7 PASS** (start, start@bot, unauth, help, config, ai_status, status).

## 11. Live Patch

Temporary deactivate → PUT same IDs → reactivate for Operational then Admin. Gates green. Node counts: Ops 34, Admin 28 (+Start). No new workflows. No rollback.

## 12. Real Telegram Acceptance

- Trigger registration: enabled
- Operator notice: sent
- Typed Trigger matrix (`/start`…`/ai_status`): **PENDING** (no typed executions in ~4 min window)
- Harness path already delivered correct replies to operator-private chat

## 13. Admin Production Closeout

`/status` `/config` `/ai_status` `/help` harness answers match production AI OFF + parser 3.1. Contour healthy.

## 14. Statistics and Error Lifecycle

Unchanged from Phase 3D.1 policy (unique leads vs technical retries; resolved error retention). No new active error introduced by this phase.

## 15. Olya Destination

Technical destination preserved from cutover. **OLYA_DESTINATION_VISIBILITY_PENDING**.

## 16. Olya Guide

`guides/OLYA-LEAD-WORK-GUIDE-v1.md` updated (v1.1) for live card behavior, drafts, duplicates, escalation to Андрей.

## 17. Operator Runbook

`guides/OPERATOR-RUNBOOK-v1.md` updated with `/start`, final normal state, and dual-active warning.

## 18. Workflow Naming

Optional rename Operational.dev / Admin.dev → without `.dev` **deferred**.

## 19. Project Status

Registry row remains **`planned`**. Gate: `REGISTRY_STATUS_PROMOTION_PENDING`.

## 20. Final Workflow State

| Workflow | Active |
|----------|--------|
| Sales-Manager-v2 | false |
| Operational.dev | true |
| Admin.dev | true |

## 21. Workflow Count Gate

Named Sales/i-SEO workflows unchanged at **4**. New workflows this phase: **0**. Active Gmail intake: **1**.

## 22. Files Created

- `evidence/phase3d2/*` (12 evidence docs)
- `reports/REPORT-iseo-sales-manager-bot-phase3d2-production-closeout-and-olya-handoff-v1.md`

## 23. Files Changed

- `README.md`, `OPERATIONAL-INDEX.md`
- `architecture/ADMIN-COMMAND-CONTRACT-v1.md`
- `architecture/TELEGRAM-UX-CONTRACT-v1.md`
- `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md`
- `implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md`
- `implementation/TEST-HARNESS-SPEC-v1.md`
- `guides/OLYA-LEAD-WORK-GUIDE-v1.md`
- `guides/OPERATOR-RUNBOOK-v1.md`
- `plans/ROLLBACK-PLAN-v1.md`

## 24. Security Validation

No credentials, Telegram/Gmail IDs, phones, emails, domains, workbook IDs, or raw payloads in committed evidence.

## 25. Git Isolation

Clean worktree from `origin/mars/canonical-post-recovery`. Scoped paths under `projects/iseo-sales-manager-bot/**` only. Foreign WIP untouched.

## 26. Commit

Primary: `a5f24f5e` — `feat(iseo-sales-manager-bot): close production handoff`  
Tip hash record: `827af495` — `docs(iseo-sales-manager-bot): record phase 3d2 tip hash`

## 27. Push

Pushed to `origin/mars/canonical-post-recovery` (no force). Tip: `827af495`.

## 28. Risks

- Operator-typed Trigger matrix not observed in-window (registration verified; harness PASS).
- Olya visibility unconfirmed.
- Registry still `planned` despite live production contour.

## 29. SAFE UNKNOWN

- Whether Оля currently sees the manager chat without operator confirmation.
- Exact historical PROCESSED label actor details beyond sanitized final-state hints.

## 30. Remaining Operator Actions

1. Type `/start` `/help` `/status` `/config` `/ai_status` in the Admin bot chat (Trigger re-matrix).
2. Confirm Оля sees the destination chat (`OLYA_DESTINATION_VISIBILITY_PENDING`).
3. Decide registry promotion under separate governance charter.

## 31. Recommended Next Phase

No technical phase required until Olya visibility is confirmed.  
After confirmation, **PHASE 3E — CONTROLLED AI ON PILOT** only with a separate explicit charter.

## 32. Production Boundary

| Item | Value |
|------|-------|
| Sales-Manager-v2 active | false |
| Operational active | true |
| Admin active | true |
| Active Gmail intake count | 1 |
| Accepted clean leads | 1 (Тест Парсер 3.1) |
| Duplicate Telegram cards after clean lead | 0 |
| `/start` real operator harness replies | yes |
| Unauthorized `/start` harness | yes (`Доступ запрещён.`) |
| Operator-typed Trigger `/start` | pending |
| Parser version | sm-parser-v3.1 |
| Telegram production cards | exactly-once for clean lead |
| Gmail label finalizations | preserved policy |
| Automatic client messages | 0 |
| AI provider calls | 0 |
| New workflows | 0 |
| Rollback | no |

## 33. Stop Condition

Stop after exactly-once closeout, `/start` acceptance (harness), UX/version polish, Admin closeout, handoff documents, evidence, commit, push and report. Do not enable AI, reactivate v2, add Olya to allowlist, create workflows, auto-contact clients, or start Phase 3E.
