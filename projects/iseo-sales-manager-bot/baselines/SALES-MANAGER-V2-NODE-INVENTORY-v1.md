# SALES MANAGER V2 NODE INVENTORY v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1  
**Source:** `baselines/Sales-Manager-v2.sanitized.json`  
**SHA256:** `AD90715FD14B6F8EF568BCBD69CC0F123D41FF024296AD3E54D3B9FD11AB821C`  
**Workflow:** `Sales-Manager-v2` · **active (export):** `false` · **nodes:** 19

## 1. Explicit defect anchors

| Anchor | Evidence |
|--------|----------|
| RAW parallel write | `Lead-Mail-Parser` → `Запись лида (RAW)` and `Prepare-OpenRouter-Request` |
| Two-call AI chain | `HTTP Request (AI #1)` then `AI-Normalizer (AI #2)` |
| Discarded first AI quality fields | `Normalize-AI-Result` keeps summary/service/priority/reply only |
| Missing CLEAN first reply persistence | CLEAN map lacks `first_reply_*` |
| Duplicate full-table lookup | `Find Duplicate Lead` on `lead-base-processed` |
| Telegram finalization gate | `message v2` → PROCESSED only; no fail branch |
| Gmail label branches | PROCESSED+remove incoming · ERROR+remove incoming |

## 2. Node table

| Node name | type | typeVersion | role | upstream | downstream | side effects | credential category | Operational.dev | known risk |
|-----------|------|-------------|------|----------|------------|--------------|---------------------|-----------------|------------|
| `Schedule Trigger` | `n8n-nodes-base.scheduleTrigger` | 1.3 | trigger | — | `Get many messages` | none | — | retained | — |
| `Get many messages` | `n8n-nodes-base.gmail` | 2.2 | gmail_fetch | `Schedule Trigger` | `Lead-Mail-Parser` | Gmail read/mutate | <GMAIL_CREDENTIAL> | changed | returnAll=true unbounded |
| `Add label PROCESSED` | `n8n-nodes-base.gmail` | 2.2 | gmail_label_mutate | `message v2` | `Remove label LEADS_ISEO` | Gmail read/mutate | <GMAIL_CREDENTIAL> | changed | — |
| `Add label ERROR` | `n8n-nodes-base.gmail` | 2.2 | gmail_label_mutate | `IF - Bad Quality` | `Remove label LEADS_ISEO2` | Gmail read/mutate | <GMAIL_CREDENTIAL> | changed | — |
| `Remove label LEADS_ISEO` | `n8n-nodes-base.gmail` | 2.2 | gmail_label_mutate | `Add label PROCESSED` | — | Gmail read/mutate | <GMAIL_CREDENTIAL> | changed | — |
| `Lead-Mail-Parser` | `n8n-nodes-base.code` | 2 | parser | `Get many messages` | `Запись лида (RAW)`, `Prepare-OpenRouter-Request` | none | — | changed | — |
| `Prepare-OpenRouter-Request` | `n8n-nodes-base.code` | 2 | ai_prepare | `Lead-Mail-Parser` | `HTTP Request (AI #1)` | none | — | changed | — |
| `Normalize-AI-Result` | `n8n-nodes-base.code` | 2 | normalize | `HTTP Request (AI #1)` | `Prepare-AI-Normalizer-Request` | none | — | changed | discards first AI quality fields; empty ai_reply |
| `Normalize-Clean-Lead` | `n8n-nodes-base.code` | 2 | normalize | `AI-Normalizer (AI #2)` | `Find Duplicate Lead` | none | — | changed | — |
| `message v2` | `n8n-nodes-base.telegram` | 1.2 | telegram_send | `Осмысленные лиды (CLEAN)` | `Add label PROCESSED` | Telegram send | <TELEGRAM_CREDENTIAL> | changed | no Telegram failure gate before PROCESSED |
| `Prepare-AI-Normalizer-Request` | `n8n-nodes-base.code` | 2 | ai_prepare_second | `Normalize-AI-Result` | `AI-Normalizer (AI #2)` | none | — | removed | dual AI chain |
| `HTTP Request (AI #1)` | `n8n-nodes-base.httpRequest` | 4.4 | ai_http | `Prepare-OpenRouter-Request` | `Normalize-AI-Result` | External HTTP (OpenRouter) | inline auth → `<OPENROUTER_CREDENTIAL>` | changed | — |
| `AI-Normalizer (AI #2)` | `n8n-nodes-base.httpRequest` | 4.4 | ai_http_second | `Prepare-AI-Normalizer-Request` | `Normalize-Clean-Lead` | External HTTP (OpenRouter) | inline auth → `<OPENROUTER_CREDENTIAL>` | removed | dual AI chain |
| `Запись лида (RAW)` | `n8n-nodes-base.googleSheets` | 4.7 | raw_write | `Lead-Mail-Parser` | — | Sheets append | <GOOGLE_SHEETS_CREDENTIAL> | changed | RAW parallel write; AI columns mapped empty |
| `Осмысленные лиды (CLEAN)` | `n8n-nodes-base.googleSheets` | 4.7 | clean_write | `IF - Bad Quality` | `message v2` | Sheets append | <GOOGLE_SHEETS_CREDENTIAL> | changed | missing first_reply/priority/AI fields |
| `IF - Bad Quality` | `n8n-nodes-base.if` | 2.3 | quality_branch | `Mark-Duplicate-Status` | `Add label ERROR`, `Осмысленные лиды (CLEAN)` | none | — | changed | ERROR path removes incoming |
| `Remove label LEADS_ISEO2` | `n8n-nodes-base.gmail` | 2.2 | gmail_label_mutate | `Add label ERROR` | — | Gmail read/mutate | <GMAIL_CREDENTIAL> | changed | — |
| `Find Duplicate Lead` | `n8n-nodes-base.googleSheets` | 4.7 | dedupe_lookup | `Normalize-Clean-Lead` | `Mark-Duplicate-Status` | Sheets read/lookup | <GOOGLE_SHEETS_CREDENTIAL> | changed | full-table CLEAN lookup |
| `Mark-Duplicate-Status` | `n8n-nodes-base.code` | 2 | dedupe_classify | `Find Duplicate Lead` | `IF - Bad Quality` | none | — | changed | weak duplicate classification |

## 3. Placeholder categories

| Category | Placeholder |
|----------|-------------|
| Gmail | `<GMAIL_CREDENTIAL>` |
| Sheets | `<GOOGLE_SHEETS_CREDENTIAL>` |
| Telegram | `<TELEGRAM_CREDENTIAL>` |
| OpenRouter | `<OPENROUTER_CREDENTIAL>` |
| Workbooks | `<RAW_WORKBOOK_ID>` / `<CLEAN_WORKBOOK_ID>` |
| Chat | `<MANAGER_CHAT_ID>` |
| Labels | `<INCOMING_GMAIL_LABEL_ID>` / `<PROCESSED_GMAIL_LABEL_ID>` / `<ERROR_GMAIL_LABEL_ID>` |
