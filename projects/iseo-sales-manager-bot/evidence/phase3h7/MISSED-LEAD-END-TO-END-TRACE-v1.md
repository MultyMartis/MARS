# MISSED LEAD END-TO-END TRACE — Phase 3H.7

| # | Stage | Result for overnight window |
|---|---|---|
| 1 | Gmail message exists | SAFE UNKNOWN until reauth |
| 2 | Production label query (Incoming) | Not evaluable — Gmail API auth fail |
| 3 | Scheduled poll (~2 min) | YES — executions continue |
| 4 | Fetch Gmail returned message | NO — `invalid_grant` error item |
| 5 | Intake Gate | Routes `intake_route=error` / `gmail_read_failed` |
| 6–23 | Parser → Telegram | NOT REACHED |
| 24 | Silent empty branch | NO — error path taken |
| — | Error Handler (pre-patch) | **MISCLASSIFIED** as `telegram_delivery_failed` |
| — | Error Handler (post-patch) | Correct `gmail_read_failed` |

## Classification
Primary: **GMAIL_OAUTH_INVALID_GRANT** (auth failure blocks fetch).  
Secondary (observability): **ERROR_HANDLER_MISCLASSIFICATION_TO_TELEGRAM**.
