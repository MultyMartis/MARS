# TELEGRAM SANDBOX DESTINATION MANIFEST v1

## Verdict

**ATTENTION — TELEGRAM SANDBOX DESTINATION REQUIRED**

## Priority checked

1. Existing operator-only private Telegram chat already connected to the Sales Manager bot — **not operator-confirmed as sandbox-safe**
2. Existing dedicated test chat controlled only by the operator — **not found / not attested**
3. Existing MetaBOT sandbox/admin chat explicitly approved for Sales Manager test delivery — **not found**

## Evidence

| Check | Result |
|-------|--------|
| CONFIG `telegram_manager_chat_id` | placeholder (`<MANAGER_CHAT_ID>`) |
| CONFIG `admin_user_ids` count | 0 (fail-closed) |
| Operational.dev Send Telegram Lead Card | disabled |
| Admin.dev Telegram Trigger / Safe Reply | disabled |
| Phase 3B gate item 13 (sandbox ≠ prod manager chat) | PENDING |
| Production manager chat reuse without operator-safe confirmation | FORBIDDEN |

## Action required from operator

Provide **one** approved sandbox destination (operator-only private chat or dedicated test chat), update CONFIG placeholders, and authorize enabling Telegram send on .dev only.
