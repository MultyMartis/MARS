# SEO Content Agent — Data Mapping v0

**Document:** `SEO-CONTENT-DATA-MAPPING-v0`  
**Status:** Placeholder inventory — **NOT** final schema  
**Date:** 2026-09-03  
**Canonical bot pack:** `projects/metabot-seo-content-agent/`  
**Legacy:** `projects/seo-content-agent/` (do not extend)

Do **not** create one table per spreadsheet/tab/notion of “active jobs list.”

---

## 1. Classification legend

Same classes as Sales mapping: `BUSINESS ENTITY`, `RUNTIME STATE`, `EVENT`, `AUDIT`, `PROJECTION`, `LEGACY SHEETS CONCEPT`.

---

## 2. Concept inventory

| Current concept | Likely class | PostgreSQL direction (v0) |
|-----------------|--------------|---------------------------|
| **jobs** | `RUNTIME STATE` | `jobs` queue with lease/retry fields |
| **active jobs** | `PROJECTION` / query | Filter on `jobs.status IN (...)` — not a second physical store |
| **memory** | Mixed | Split: operational vs conversation vs durable facts (see architecture §15) |
| **generation state** | `RUNTIME STATE` | Job payload/state machine columns or child `generation_runs` |
| **content artifacts** | `BUSINESS ENTITY` | Artifacts table(s) with version/status |
| **conversation memory** | `RUNTIME STATE` / bounded history | Conversation messages table with retention policy |
| **errors** | Error store | `errors` linked by `correlation_id` / `job_id` |
| **admin / Telegram state** | `RUNTIME STATE` + `AUDIT` | Callback/session state ephemeral where possible; admin actions → `audit_logs` |

---

## 3. Merge / disappear candidates

| Idea | Disposition |
|------|-------------|
| Separate “active jobs” sheet | Projection only |
| Undifferentiated “memory” blob | Split memory classes; **no pgvector in V1** |
| Generation progress only in n8n static data | Prefer durable job state in PG after migration |
| Admin chat as sole audit trail | Add `audit_logs` |

---

## 4. Non-goals for v0

- Final DDL;
- Phase 8 cutover;
- unifying Content + Sales into one schema.

---

## 5. Next mapping gate

`SEO-CONTENT-DATA-MAPPING-v1` after Sales path proves primitives; schema name `app_seo_content`.
