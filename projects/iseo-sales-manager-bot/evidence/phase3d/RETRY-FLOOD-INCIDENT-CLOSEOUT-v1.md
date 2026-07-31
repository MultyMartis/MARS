# RETRY-FLOOD-INCIDENT-CLOSEOUT-v1

**Phase:** 3D  
**Incident window:** 2026-07-31T11:00:00Z → 2026-07-31T11:35:00Z  
**Workflow:** i-SEO Sales Manager - Operational.dev  
**Classification:** production incident — duplicate Telegram cards during finalize gap

## Root cause (closed)

1. DEDUP Sheets lookup replaced lead object → empty Telegram `chat_id` (fixed in Phase 3C.2).  
2. Gmail label nodes used retired messageId refs → PROCESSED failed after Telegram success (fixed in Phase 3C.2).  
3. Successful Telegram + failed Gmail finalize left incoming label → re-fetch loop → additional Telegram sends (addressed in Phase 3D idempotency guard).

## Sanitized incident matrix

| Stage | Attempts | Successes | Duplicates | Final State |
|-------|----------|-----------|------------|-------------|
| Operational executions (flood window) | 83 | 59 | n/a | window closed; empty polls after |
| Lead processing chains (same message) | 25 | 1 terminal | 24 | terminally PROCESSED |
| Telegram send | 25 | 6 | ~5 extra cards | duplicate cards during finalize gap |
| RAW append runs | 25 | 25 | 24 | append-per-retry (immutable RAW) |
| CLEAN write runs | 25 | 25 | 24 | reprocess/append path |
| DEDUP write runs | 25 | 25 | see audit | keys written on process path |
| LEAD_EVENTS runs | 6 | 6 | allowed | events may repeat without new business lead |
| Gmail PROCESSED + incoming remove | 25 | 1 | 0 | terminal labels applied |
| OpenRouter AI | 0 | 0 | 0 | AI OFF / not executed |

## Counts (sanitized)

- Unique Gmail messages in window: **1**
- Telegram successful sends: **6** (estimated duplicate cards beyond first: **5**)
- Failed Telegram attempts (empty chat era): **19**
- Terminal PROCESSED + incoming removed: **yes**
- AI provider calls: **0**
- Automatic client messages: **0**

## Closeout actions

| Action | Status |
|--------|--------|
| Phase 3C.2 field/wiring repair | done |
| Phase 3D delivery idempotency + bounded retry | done |
| Message terminally processed | yes |
| Reopen for same historical message | **forbidden** |

## Operator note

Managers may have received duplicate cards for the first accepted real lead before the finalize fix. Treat as closed incident; do not reprocess that Gmail message.
