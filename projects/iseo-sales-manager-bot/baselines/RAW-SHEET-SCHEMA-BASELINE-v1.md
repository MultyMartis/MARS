# RAW SHEET SCHEMA BASELINE v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1  
**Source (STORAGE only):** `MetaBOT -Leads.DB.xlsx`  
**Raw SHA256:** `FED01A145D4003FD9800834CA2771FD8BC07DC87ADA283E187FA172D63163DAA`  
**Git:** schema markdown only — XLSX not committed

---

## 1. Workbook / sheet

| Field | Value |
|-------|-------|
| Role | RAW |
| Sheet names | `lead-base` |
| Future tab (absent) | `lead_raw_v2` |
| Data rows | 19 |
| Historical policy | untouched |

## 2. Exact ordered headers

1. `lead_id`
2. `created_at`
3. `source`
4. `email_subject`
5. `client_name`
6. `contact_type`
7. `client_contact`
8. `client_phone`
9. `client_email`
10. `client_messenger`
11. `client_site`
12. `request_text`
13. `request_page`
14. `ip`
15. `ai_summary`
16. `ai_detected_service`
17. `ai_priority`
18. `ai_reply`
19. `manager_status`
20. `processing_status`

## 3. Fill rates (n=19)

| Header | Fill rate | Non-empty / 19 | Formulas | Error cells |
|--------|-----------|----------------|----------|-------------|
| `lead_id` | 100% | 19 | 0 | 0 |
| `created_at` | 100% | 19 | 0 | 0 |
| `source` | 100% | 19 | 0 | 0 |
| `email_subject` | 100% | 19 | 0 | 0 |
| `client_name` | 100% | 19 | 0 | 0 |
| `contact_type` | 100% | 19 | 0 | 0 |
| `client_contact` | 100% | 19 | 0 | 6 |
| `client_phone` | 89% | 17 | 0 | 0 |
| `client_email` | 16% | 3 | 0 | 0 |
| `client_messenger` | 0% | 0 | 0 | 0 |
| `client_site` | 68% | 13 | 0 | 0 |
| `request_text` | 26% | 5 | 0 | 0 |
| `request_page` | 16% | 3 | 0 | 0 |
| `ip` | 0% | 0 | 0 | 0 |
| `ai_summary` | 0% | 0 | 0 | 0 |
| `ai_detected_service` | 0% | 0 | 0 | 0 |
| `ai_priority` | 0% | 0 | 0 | 0 |
| `ai_reply` | 0% | 0 | 0 | 0 |
| `manager_status` | 100% | 19 | 0 | 0 |
| `processing_status` | 100% | 19 | 0 | 0 |

## 4. Aggregate findings

| Finding | Evidence |
|---------|----------|
| AI columns empty | four AI columns fill 0% |
| Subject collapsed | `email_subject=UNKNOWN` 19/19 |
| Name quality | UNKNOWN 11; overflow-suspect 8 |
| Contact errors | `client_contact` error cells 6 |
| Messenger / IP unused | 0% fill |
| Enums | `manager_status=new` 19; `processing_status=parsed` 19 |
| Contact types | phone 17 · email 2 |
| Duplicate lead_id groups | several keys repeated 2–3 times |
| Formulas | 0 |

Synthetic example: `lead_id=<SYNTHETIC_ID>; source=gmail; email_subject=UNKNOWN; client_name=UNKNOWN; contact_type=phone; ai_*=empty; manager_status=new; processing_status=parsed`

## 5. Migration implications

1. Keep `lead-base` historical.  
2. Create `lead_raw_v2` without AI columns.  
3. Stop writing empty AI fields into RAW.  
4. Do not seed DEDUP from `#ERROR!` contacts.  
5. Add `parser_version` on v2 tab.
