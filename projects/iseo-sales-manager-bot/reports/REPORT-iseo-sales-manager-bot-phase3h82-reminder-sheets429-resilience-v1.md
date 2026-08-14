# REPORT — ISEO-SALES-MANAGER-BOT PHASE 3H.8.2 REMINDER SHEETS 429 RESILIENCE

**Verdict:** `PHASE 3H.8.2 TECHNICAL REPAIR COMPLETE — REAL NEXT-WINDOW REMINDER ACCEPTANCE PENDING`

Do **not** treat this as `REMINDER LIVE PASS`.

---

## 1. Verdict

Technical repair for ACCESS_CONTROL HTTP 429 is deployed on Admin.dev. Isolated harness 23/23 PASS. One genuine spam lead reopened to pending as `REMINDER_ACCEPTANCE_LEAD_2`. Next natural proof: **2026-08-15 10:00 Europe/Moscow**. Soak not restarted. Phase 3I.1 blocked. AI OFF.

## 2. Proven real failure

`REMINDER_EVALUATION_ABORTED_BY_SHEETS_429` at 2026-08-14 10:00 Europe/Moscow. CLEAN succeeded; ACCESS 429; pending_count not computed; claims=0; Telegram=0; business date not marked sent.

## 3. 10:00 execution

Exec **30813** ~10:00:39–10:01:09 MSK. ACCESS HTTP 429. Native retryOnFail did not complete a 3×30s sequence (`executionTime` ~26–29s).

## 4. 10:15 execution

Exec **30821** 10:15:39–10:16:06 MSK. **Same ACCESS 429.** Window is 20 minutes; 10:15 is a same-window recovery slot. Quota still active (Ops 30822 also 429 at 10:16).

## 5. Reminder-critical Sheets reads

Four pre-decision reads per evaluation: CONFIG, CLEAN `lead_clean_v2` A1:ZZ500, ACCESS_CONTROL, REMINDER_DELIVERIES. Each once per run. See `evidence/phase3h82/REMINDER-CRITICAL-SHEETS-READS-v1.md`.

## 6. Quota pressure analysis

**SUSTAINED_PROJECT_QUOTA_PRESSURE** + **LOCAL_BURST_CONTRIBUTION**. 09:55–10:20 MSK: Admin 2 execs / ~12 Sheets runs; Ops 12 execs / ~72 Sheets runs. **No schedule stagger.**

## 7. Retry contract

`iseo-sheets-429-retry-v1.0`: 4 attempts; delays 0 / 5s / 15s / 30s; Retry-After 1–120s when sane; 429 only; hard limit; per-logical-read.

## 8. ACCESS_CONTROL repair

Explicit Wait loop on ACCESS error output. Successful retry resumes evaluator; recipients resolved once (expected 4). Exhaustion → `ERROR_SHEETS_429_ACCESS`; no claims; no Telegram; no sent-day stamp; no stale ACCESS fallback.

## 9. Other critical reads

CLEAN / CONFIG / REMINDER_DELIVERIES / CONFIG write: native `retryOnFail` maxTries=4 (30s CLEAN/ledger, 15s CONFIG). Not a product-wide Sheets wrap.

## 10. Per-execution read reuse

Reminder path already reads each sheet once per evaluation. No long-lived cache added.

## 11. All-retries-fail behavior

Harness C: ERROR, claims=0, sends=0, date not poisoned.

## 12. Non-429 behavior

Harness D: HTTP 500 → 1 attempt, no quota loop, ERROR, no claims.

## 13. Exactly-once under retry

Harness: 4 claims after recovery; second same-date eval 0 extra; failed run then later send still allowed.

## 14. Error observability

CONFIG keys for evaluation/decision/error class/stage/at/retry; pending_count=`not_computed` when appropriate. ERRORS append fallback if CONFIG write 429.

## 15. `/reminder_status`

Live Commands include Этап / Причина: лимит Google Sheets API / Повторные попытки. Decision word `Ошибка`. No secrets.

## 16. Zero-pending proof

`SKIPPED_ZERO_PENDING`, zero sends, not ERROR.

## 17. One-pending proof

pending=1 → recipients=4 / claims=4 / successes=4 (isolated fixture).

## 18. Post-change backup

Private stamp 2026-08-14T08-53-01-084Z. Admin 92 active. last_window still null.

## 19. Real acceptance lead

`REMINDER_ACCEPTANCE_LEAD_2` (`LEAD_A6A0FB0DBFF6`): spam→pending, same id, spam history kept, one reopen event, no new row, no card resurface.

## 20. Current pending count

**31** eligible pending (tests excluded) after reopen. CLEAN 129 rows.

## 21. Next real 10:00 window

**2026-08-15 10:00 Europe/Moscow** (also 10:15 same window if 10:00 retries exhaust).

## 22. System invariants

Ops 45 active · Admin 92 active · v2 inactive · one Gmail intake · reminder 10:00 Europe/Moscow · recipients=4 · reporting manual · AI OFF · OpenRouter=0 · customer auto-send=0 · workflows created=0.

## 23. Git

Worktree `X:\AI MARS STORAGE\git-sync-iseo-sm-phase3h82-20260814-151828\repo` (detached at canonical tip, then 4 commits). Scope `projects/iseo-sales-manager-bot/**`. Canonical push without force.

- `9670d447` fix(iseo-sales-manager-bot): retry reminder sheets reads on quota 429
- `cb1fc2f0` fix(iseo-sales-manager-bot): expose reminder quota failure state
- `89702763` test(iseo-sales-manager-bot): prove reminder exactly-once under retries
- docs commit in this wave: prepare next real reminder acceptance


## 24. Soak state

`INTERRUPTED — REAL REMINDER WINDOW FAILED ON SHEETS 429` — **not restarted**.

## 25. Phase 3I.1 gate

**Blocked.**

## 26. Stop condition

Met for this run: retry deployed; ACCESS 429 no longer immediately kills a recoverable reminder; fail-closed; date not poisoned; exactly-once under retry; `/reminder_status` truthful; one genuine lead reopened; next window recorded; no manual production reminder; soak stopped; 3I.1 not started.

---

## Counters

| Counter | Value |
|---|---|
| reminder-critical Sheets reads | 4 pre-decision |
| 429 retries configured | 3 (attempts 2–4) |
| max retry attempts | 4 |
| simulated single-429 recoveries | 1+ (harness A/F) |
| simulated multiple-429 recoveries | 1 (harness B) |
| all-retry failures | 1 (harness C) |
| claims created on failed runs | 0 |
| duplicate claims | 0 |
| duplicate reminder sends | 0 |
| zero-pending sends | 0 |
| one-pending recipients | 4 |
| one-pending successes | 4 |
| genuine acceptance leads reopened | 1 |
| current production pending count | 31 |
| reminder recipients | 4 |
| AI state | OFF |
| OpenRouter calls | 0 |
| customer auto-send | 0 |
| workflows created | 0 |
| soak restarted | 0 |
| Phase 3I.1 started | 0 |

## Evidence

`projects/iseo-sales-manager-bot/evidence/phase3h82/`
