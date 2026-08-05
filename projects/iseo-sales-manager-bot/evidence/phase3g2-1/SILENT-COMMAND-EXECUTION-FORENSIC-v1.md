# Silent-command execution forensic — Phase 3G.2.1

**Phase:** 3G.2.1  
**Status:** FILLED  
**Workflow:** Admin.dev `wLrLp4WQHm1VJmxz`  
**Sanitized labels only:** ADMIN_A · MOD_A  
**Forbidden:** Telegram IDs, chat IDs, usernames, workbook IDs, raw updates, unsanitized execution payloads.

## Operator window (live)

Profile / AI / stats commands succeeded; `/help`, `/start`, `/config` produced no Telegram reply (including `/help` retry).

## Execution samples (sanitized)

| Command | Exec class | Trigger | Normalize | Auth | Route | Builder node | Telegram Send |
|---------|------------|---------|-----------|------|-------|--------------|---------------|
| `/help` | error | received | `/help` | passed | Help branch | **Help** — `Unexpected token ')'` | not reached |
| `/help` (retry) | error | received | `/help` | passed | Help branch | **Help** — `Unexpected token ')'` | not reached |
| `/start` | error | received | `/start` | passed | Start branch | **Start** — `Unexpected token ')'` | not reached |
| `/config` | error | received | `/config` | passed | Config Summary | **Config Summary** — `Invalid or unexpected token` | not reached |
| `/ai_status` | success | received | `/ai_status` | passed | AI Status | OK | success |
| `/stats` | success | received | `/stats` | passed | Stats | OK | success |
| `/reply_profiles` | success | received | `/reply_profiles` | passed | Reply Profile Commands | OK | success |

## Path checklist

| Question | `/help` | `/start` | `/config` |
|----------|---------|----------|-----------|
| Telegram Trigger received? | yes | yes | yes |
| Router branch matched? | Help | Start | Config Summary |
| Command normalization correct? | yes | yes | yes |
| Authorization passed? | yes | yes | yes |
| Registry/builder returned item? | **no** (Code syntax error) | **no** | **no** |
| Non-empty text builder? | n/a | n/a | n/a |
| Reached Telegram Send? | no | no | no |
| Telegram Send executed? | no | no | no |
| Telegram HTML rejected? | no | no | no |
| Runtime exception? | **yes** | **yes** | **yes** |
| Branch terminated without output? | yes (error stop) | yes | yes |
| Merge/wait swallowed item? | no | no | no |
| PROFILE_EVENTS on common path? | no (not involved) | no | no |
| Invalid HTML in text? | n/a (never built) | n/a | n/a |
| Message length exceeded? | n/a | n/a | n/a |

## Result

- [x] Forensic filled from live executions (not static inspection alone)
