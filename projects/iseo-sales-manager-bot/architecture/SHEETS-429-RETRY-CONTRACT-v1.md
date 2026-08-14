# SHEETS 429 RETRY CONTRACT v1

> **Phase 3H.8.2.2 (2026-08-14):** Reminder pending eligibility uses `iseo-reminder-current-state-selector-v1.0` — unique `lead_id` → authoritative current status → eligibility. First CLEAN pending row no longer wins. Production Reminder Build Claims adds no per-lead Sheets calls. Duplicate CLEAN row source forensic is deferred. Real 10:00 acceptance still pending.


**Contract id:** `iseo-sheets-429-retry-v1.0`  
**Phase:** 3H.8.2  
**Scope:** reminder evaluation pre-decision Google Sheets reads on Admin.dev only.

## Policy (chosen)

| Attempt | When | Delay before attempt |
|---|---|---|
| 1 | immediate | 0 |
| 2 | retry 1 | ~5 seconds |
| 3 | retry 2 | ~15 seconds |
| 4 | retry 3 | ~30 seconds |

- Maximum attempts: **4** (1 initial + 3 retries).
- Maximum added delay: **50 seconds**, plus Sheets call time. Fits inside the **20-minute** reminder window (`10:00` inclusive … `10:20` exclusive Europe/Moscow).
- If Google returns a sane `Retry-After` (1–120 seconds), that value **replaces** the scheduled delay for that attempt.
- **Only HTTP 429** (and equivalent quota messages: `too many requests`, `RESOURCE_EXHAUSTED`, `userRateLimitExceeded`) is retried.
- Non-429 (credentials, schema, malformed, 5xx) → **stop immediately**, explicit `ERROR`, no quota loop.
- Hard limit: no unbounded loop.

## Per-logical-read

Retry the **failing read**, not the whole reminder workflow.

- Before claims exist: safe to retry the read.
- After claims exist: do not blindly rerun claim creation.
- This phase covers **pre-decision** reads.

## Fail-closed (ACCESS_CONTROL)

If ACCESS_CONTROL cannot be read after all retries:

- decision: `ERROR_SHEETS_429_ACCESS`
- claims = 0
- Telegram attempts = 0
- do **not** stamp `pending_reminder_last_window`
- do **not** send using stale recipients

Recipient authorization is security-sensitive.

## Live Admin.dev mapping

| Read | Live mechanism |
|---|---|
| `Read ACCESS_CONTROL for Reminder` | explicit Wait loop 5s / 15s / 30s, max 4 attempts, `onError: continueErrorOutput` |
| `Read CLEAN for Reminder` | native `retryOnFail` maxTries=4, wait 30s |
| `Read Reminder CONFIG` | native `retryOnFail` maxTries=4, wait 15s |
| `Read REMINDER_DELIVERIES` | native `retryOnFail` maxTries=4, wait 30s |
| `Apply Reminder Window CONFIG Write` | native `retryOnFail` maxTries=4, wait 15s; if still blocked, Append ERRORS fallback |

Native ACCESS `retryOnFail` (3×30s) was **already on** at the failed 2026-08-14 10:00 window and did **not** complete a full retry sequence (`executionTime` ~26–29s). The explicit Wait loop is the repair.

## Isolated helper

`implementation/runtime-libs/sheets-429-retry-v1.mjs` — same bounds for harness / documentation. Not a runtime n8n import.

## Not in scope

- Unrelated Sheets usage outside reminder evaluation.
- Schedule stagger (not applied; see quota analysis).
- Long-lived ACCESS cache as send fallback.
