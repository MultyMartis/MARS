# CLEAN SHEET SCHEMA BASELINE v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1  
**Source (STORAGE only):** `MetaBOT -Leads_Manager.DB.xlsx`  
**Raw SHA256:** `AF565F1CC4E273A4B7D24660CDB22D0A628699C67C0F49694155D1A7101B6DB4`  
**Git:** schema markdown only — XLSX not committed

---

## 1. Workbook / sheet

| Field | Value |
|-------|-------|
| Role | CLEAN |
| Sheet names | `lead-base-processed` |
| Future tabs (absent) | `lead_clean_v2`, `CONFIG`, `LEAD_EVENTS`, `ERRORS`, `DEDUP_INDEX` |
| Data rows | 19 |
| Historical policy | untouched |

## 2. Exact ordered headers

1. `lead_id`
2. `created_at`
3. `clean_name`
4. `primary_contact`
5. `phone`
6. `email`
7. `messenger`
8. `site`
9. `service`
10. `summary`
11. `quality_status`
12. `duplicate_status`
13. `manager_status`
14. `notes`

## 3. Fill rates (n=19)

| Header | Fill rate | Non-empty / 19 | Formulas | Error cells |
|--------|-----------|----------------|----------|-------------|
| `lead_id` | 100% | 19 | 0 | 0 |
| `created_at` | 100% | 19 | 0 | 0 |
| `clean_name` | 100% | 19 | 0 | 0 |
| `primary_contact` | 100% | 19 | 10 | 0 |
| `phone` | 79% | 15 | 0 | 0 |
| `email` | 16% | 3 | 0 | 0 |
| `messenger` | 11% | 2 | 0 | 0 |
| `site` | 58% | 11 | 0 | 0 |
| `service` | 100% | 19 | 0 | 0 |
| `summary` | 100% | 19 | 0 | 0 |
| `quality_status` | 100% | 19 | 0 | 0 |
| `duplicate_status` | 100% | 19 | 0 | 0 |
| `manager_status` | 100% | 19 | 0 | 0 |
| `notes` | 37% | 7 | 0 | 0 |

## 4. Technical enums

| Column | Distribution |
|--------|--------------|
| `service` | SEO 8 · Audit 8 · Other 3 |
| `quality_status` | ok 19/19 |
| `duplicate_status` | new 12 · repeat 7 |
| `manager_status` | new 19/19 |
| `messenger` | blank 17 · Telegram 2 |

Missing vs Phase 2 CLEAN v2: `first_reply_text`, `first_reply_source`, `priority`, `processing_mode`, `ai_status`, `fallback_used`, lifecycle fields, clarification/recommendation.

## 5. Formula / contact notes

| Finding | Evidence |
|---------|----------|
| Formula-like primary_contact | 10 cells |
| Email fill | 3/19 |
| Phone fill | 15/19 |
| Site fill | 11/19 |
| Notes fill | 7/19 |

Synthetic example: `quality_status=ok; duplicate_status=new; manager_status=new; service=SEO; summary=<SYNTHETIC_SUMMARY>`

## 6. Migration implications

1. Preserve historical tab.  
2. New `lead_clean_v2` with full Phase 2 headers.  
3. Do not trust historical `ok` without recompute.  
4. Replace full-sheet dedupe with `DEDUP_INDEX`.  
5. Persist first reply on CLEAN.
