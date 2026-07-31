# FIRST-REAL-LEAD-END-TO-END-v1

**Phase:** 3C.2  
**Execution anchor:** Operational success with Telegram + PROCESSED + incoming remove (sampled exec around 2026-07-31T11:24:00Z)

## Pipeline

| Stage | Result |
|-------|--------|
| Gmail delivery | yes |
| Not Trash | yes |
| Incoming label present at intake | yes |
| Production query eligible | yes |
| Operational executions for this message | multiple during pre-fix flood; **one successful finalization** |
| Sales-Manager-v2 executions | 0 (inactive) |
| RAW row | written (reprocess path) |
| CLEAN row | written/updated |
| Dedupe status | `reprocessed` (same Gmail message retries) |
| Telegram production card | sent (AI OFF card; length ~759) |
| Synthetic footer | **absent** |
| Internal IDs in card | **absent** |
| Manual-copy reply block | present / or explicit “no contact” wording per quality |
| Automatic client reply | **0** |
| AI provider calls | **0** (OpenRouter node not executed; `processing_mode=ai_off`) |
| Quality | `bad` (insufficient contact) — still a real form lead through production path |

## Flood note

Before chat_id / messageId repairs, Telegram failed with empty chat_id while incoming remained → ~30s reprocess loop. After Telegram send began succeeding, several cards may have been delivered before Gmail PROCESSED finalization completed. Post-fix: empty polls only.
