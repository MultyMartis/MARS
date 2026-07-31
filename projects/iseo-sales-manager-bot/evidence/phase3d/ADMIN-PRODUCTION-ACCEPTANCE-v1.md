# ADMIN-PRODUCTION-ACCEPTANCE-v1

**Phase:** 3D  
**Method:** ephemeral Admin sidecar inject → Normalize Command (operator allowlisted); sidecar removed after  
**Allowlist size:** 1 (unchanged; Оля not added)

## Commands verified

| Command | Authorized | Notes |
|---------|------------|-------|
| `/status` | yes | Contour working; AI off; current poll time present; last lead/error timestamps present |
| `/health` | yes | Sheets + Gmail + Telegram available; eligible mails 0; AI off; AI probe not run |
| `/stats` | yes | 7-day window; **Тестовые заявки исключены**; AI off counts; flood-era reprocessed dominant |
| `/last_error` | yes | Historical `telegram_delivery_failed` shown as last error — **not** framed as active synthetic incident |
| `/config` | yes | Working contour; AI off; secrets hidden; allowlist count 1 |
| `/ai_status` | yes | AI off; probe disabled |

## Expectations

| Expectation | Result |
|-------------|--------|
| Production / working-contour wording | **pass** (Russian «рабочий контур») |
| Current poll time | **pass** |
| AI OFF | **pass** |
| SYNTHETIC_TEST excluded from stats | **pass** |
| Stale synthetic not presented as active incident | **pass** |
| Clean test lead in stats | **pending** (lead not submitted) |

## Final gates after test

Sales-Manager-v2 inactive · Operational.active · Admin.active · sidecar cleaned.
