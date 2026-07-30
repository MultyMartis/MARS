# TELEGRAM FAILURE PATH EVIDENCE v1

## Method

Harness-injected `force_telegram_fail=true` on LIVE_TG_FAIL (no real bot destination mutation).

## Live result

| Check | Result |
|-------|--------|
| Error Handler executed | **YES** |
| OpenRouter executed | **NO** |
| Gmail PROCESSED real mutate | disabled / pass-through only |
| Incoming label removal | disabled |
| ERRORS synthetic row | written via HTTP evidence writer (`telegram_delivery_failed`, marker SYNTHETIC_TEST) |

## Graph policy (accepted)

IF Telegram Success false → Error Handler → Append ERRORS → Add Gmail ERROR → Preserve Gmail Incoming (no PROCESSED).

## Local harness

TG_FAIL_POLICY fixture: **PASS**
