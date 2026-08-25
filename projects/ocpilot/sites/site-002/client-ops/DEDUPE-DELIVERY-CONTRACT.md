# SITE-002 — Dedupe / Delivery Contract

## CURRENT STABLE BACKEND

**n8n Data Table:** `MARS Client Ops Dedupe — bzpm.ru`  
**Table ID:** `H6VYhwz7RXZCBMmu`

**Not Google Sheets. Not current BZPM operational memory via Sheets.**

## Semantics

| State | Meaning |
|-------|---------|
| FIRST_SEEN | Event first recorded |
| SENT | Delivered (or accepted as delivered per workflow) |

## Rules

- Same exact run replay → dedupe (no uncontrolled duplicate Telegram).
- Same recurring condition on a **later/new** run → **new independent event**.
- Report concurrency: `MAX_SAFE_REPORT_CONCURRENCY=1`.
- No uncontrolled retry loops.
- Bounded retry / failure durability statuses exist in dispatcher design (PENDING/SENDING/SENT/FAILED_RETRYABLE/FAILED_FINAL) — do not invent unbounded loops.

## Secrets

Do not print API keys, tokens, or table credentials in Git/reports.
