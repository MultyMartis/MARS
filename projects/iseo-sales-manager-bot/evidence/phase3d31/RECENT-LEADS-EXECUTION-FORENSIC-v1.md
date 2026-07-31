# RECENT-LEADS-EXECUTION-FORENSIC-v1

**Phase:** 3D.3.1  
**Scope:** Pre-fix Admin.dev executions for `/leads 3|5|10` (sanitized; no PII).

## Matrix (pre-fix defect)

| Command | Requested | Sheets Rows | Unique Leads (formatter cards) | Formatter Items (cards+notice) | Capture Items | Telegram Sends | Result |
|---------|-----------|-------------|-------------------------------|--------------------------------|---------------|----------------|--------|
| `/leads 3` | 3 | 36 | 3 | 4 | **1** | **1** | FAIL — only card 1 delivered |
| `/leads 5` | 5 | 36 | 5 | 6 | **1** | **1** | FAIL — only card 1 delivered |
| `/leads 10` | 10 | 36 | 5 (available) | 6 | **1** | **1** | FAIL — only card 1; honest available=5 collapsed |
| `/leads 7` | invalid | 36 | 0 | 1 (invalid) | 1 | 1 | PASS — invalid rejected |

Sample executions: `9855` (`/leads 3`), `9856` (`/leads 5`), `9858` (`/leads 10`).

## Root cause

1. **Primary:** `Capture Admin Reply` used `$input.first()` and returned a single item, collapsing Recent Leads multi-item output before `Safe Telegram Reply`.
2. **Secondary UX:** archive phone rendered `#ERROR! (Formula parse error.)` from corrupted CLEAN cells (Sheets USER_ENTERED + leading `+`).
3. **Cardinality:** after synthetic exclusion, ~5 unique business leads existed — `/leads 10` correctly could not invent 10, but still only sent card 1.

## Post-fix (acceptance)

| Command | Cards | Capture | Telegram items | Formula in card | Ordinals |
|---------|-------|---------|----------------|-----------------|----------|
| `/leads 3` | 3 | 4 | 4 | suppressed | 1..3 |
| `/leads 5` | 5 | 6 | 6 | suppressed | 1..5 |
| `/leads 10` | 5 (available) | 6 | 6 | suppressed | 1..5 |
| `/leads 7` | 0 | 1 | 1 | n/a | invalid warning |
