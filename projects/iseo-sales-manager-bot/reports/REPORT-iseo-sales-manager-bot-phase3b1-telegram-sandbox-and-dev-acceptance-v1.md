# REPORT — ISEO SALES MANAGER BOT PHASE 3B.1 TELEGRAM SANDBOX AND DEV ACCEPTANCE

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT — PHASE 3B.1 TELEGRAM SANDBOX AND DEV ACCEPTANCE  
**Date:** 2026-07-30

---

## 1. Verdict

**ATTENTION — TELEGRAM SANDBOX DESTINATION REQUIRED**

Sandbox destination could not be verified under the operator priority gate. Telegram delivery was not performed. Local + live AI OFF synthetic validation, zero-token runtime evidence, Sheets synthetic evidence, Admin command harness, original integrity, and production proposal are complete.

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\\AI MARS` |
| Volume X: | `AI WS` |
| Main branch | `mars/canonical-post-recovery` (dirty foreign WIP preserved; not used) |
| Clean worktree | `X:\\AI MARS STORAGE\\worktrees\\iseo-sm-phase3b1` @ origin tip |
| n8n API | `local/tokens/n8n-api.env` present |

## 3. Authority Read

Project docs under `projects/iseo-sales-manager-bot/` (README, OPERATIONAL-INDEX, architecture contracts, implementation specs, Phase 3B evidence/report). MetaBOT Programmer grammar / import-safe / safe-patch protocol. Guardrails session rules applied.

## 4. Sandbox Destination

See `evidence/phase3b1/TELEGRAM-SANDBOX-DESTINATION-MANIFEST-v1.md`.

CONFIG chat id remains placeholder; admin allowlist empty; .dev Telegram nodes disabled. No guess; no production manager send.

## 5. Workflow Snapshots

| Workflow | ID | Active | Nodes | Integrity |
|----------|----|--------|-------|-----------|
| Sales-Manager-v2 | h8I2Tl2yl4uzhUnB | true | 19 | ORIGINAL_UNCHANGED |
| Operational.dev | xSnXPy8cEHoZw6xG | false | 29 | restored |
| Admin.dev | wLrLp4WQHm1VJmxz | false | 22 | restored |

## 6. Operational AI OFF Tests

Local fixtures C01–C09 + structure + TG fail policy: harness PASS (see evidence). Live synthetic webhook executions: 5 success runs with Format cards; OpenRouter not executed.

## 7. Zero-Token Runtime Evidence

**PASS** — execution runData shows Prepare AI / OpenRouter / Validate AI **not executed** for all LIVE_* AI OFF cases.

## 8. Telegram Delivery

**0** sandbox messages. Blocked by destination gate. Formatter evidence captured from live Format node output (no Bot API `message_id`).

## 9. Telegram Failure Path

LIVE_TG_FAIL executed Error Handler with `force_telegram_fail`. ERRORS synthetic row preserved. PROCESSED/Gmail mutate nodes remained disabled.

## 10. AI ON Mocked Tests

Mocked Validate/Merge matrix executed; CONFIG left `ai_enabled=false`. Deadline-promise detector marked **GAP**.

## 11. Admin Authorization

Unauthorized AI ON denied in harness. Authorized toggle emits audit/config_write intents. Live Telegram admin identity not available (destination gate).

## 12. Admin Commands

`/help` `/status` `/ai_status` `/health` `/stats` `/last_error` `/config` unknown + AI on/off harness: PASS. Live Telegram replies not sent.

## 13. Healthcheck

Sheets/CONFIG/v2 tabs verified. Telegram sandbox ping pending. AI OFF. Dev workflows inactive.

## 14. Sheets Writes

Synthetic rows written via temporary HTTP append (native Sheets append nodes blocked by stale column cache). Counts: {"lead_raw_v2":2,"lead_clean_v2":3,"CONFIG":0,"LEAD_EVENTS":3,"ERRORS":1,"DEDUP_INDEX":4}.

## 15. Synthetic Data Policy

**Preserve** marked `SYNTHETIC_TEST` rows as sandbox evidence. No broad deletion. Historical tabs untouched.

## 16. Dev Workflow Integrity

Both .dev workflows restored inactive; temporary webhook/nodes removed; accepted graph restored.

## 17. Original Workflow Integrity

**ORIGINAL_UNCHANGED** (id/name/active/nodes/connectionHash/sanitizedHash).

## 18. Production Proposal

Prepared only — `evidence/phase3b1/PRODUCTION-PROPOSAL-v1.md`. Not applied.

## 19. Files Created

Under `evidence/phase3b1/` (13 manifests) + this report.

## 20. Files Changed

`README.md`, `OPERATIONAL-INDEX.md`, `implementation/SANDBOX-APPLY-GATE-v1.md`, `plans/ROLLBACK-PLAN-v1.md` (runtime facts).

## 21. Security Validation

No secrets, chat IDs, workbook IDs, tokens, or unsanitized exports committed. OpenRouter credential untouched.

## 22. Git Isolation

Clean worktree from `origin/mars/canonical-post-recovery`. Main foreign WIP / staged client-ops files untouched.

## 23. Commit

Primary: `e2cfb52d71165e2455a8f421a2138a95c7a11a14` — `test(iseo-sales-manager-bot): complete phase 3b1 sandbox acceptance`

## 24. Push

Pushed to `origin/mars/canonical-post-recovery` at `e2cfb52d71165e2455a8f421a2138a95c7a11a14` (fast-forward; no force).

## 25. Risks

- Telegram sandbox destination still unresolved
- Google Sheets append nodes need column refresh before production writes
- Parse Lead `require('crypto')` disallowed by n8n task-runner (must patch before live Parse on runners)
- Deadline unsafe-phrase detector gap

## 26. SAFE UNKNOWN

- Whether production manager chat is operator-private vs group (not attested)
- Exact coexistence model for Admin Telegram Trigger vs Sales Manager bot

## 27. Required Operator Decisions

1. Approve one sandbox Telegram destination and CONFIG values
2. Review sanitized live card previews
3. Review production proposal (no apply yet)
4. Authorize Sheets append column-refresh patch on .dev

## 28. Recommended Next Phase

**PHASE 3C — PRODUCTION PROPOSAL REVIEW AND CUTOVER GATE** — only after sandbox Telegram output is reviewed and destination is approved.

## 29. Production Boundary

- original workflow modified: **0**
- production workflows activated/deactivated: **0**
- new workflows created: **0**
- real Gmail leads processed: **0**
- real Gmail labels changed: **0**
- client messages sent: **0**
- production manager messages sent: **0**
- sandbox Telegram messages: **0**
- synthetic Sheets rows: **13**
- production cutover: **not performed**

## 30. Stop Condition

Stop after sandbox acceptance attempt, evidence, production proposal, scoped commit, push and report. Do not activate .dev for production, disable original, process real Gmail, contact clients, or begin Phase 3C apply.

## Execution safety

- cwd: worktree under `X:\\AI MARS STORAGE\\worktrees\\iseo-sm-phase3b1`
- scope lock honored: yes (`projects/iseo-sales-manager-bot/**`)
- destructive ops: none
- protected zone touch: none
