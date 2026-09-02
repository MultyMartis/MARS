# i-SEO Sales — Data Open Questions v1

**Document:** `ISEO-SALES-DATA-OPEN-QUESTIONS-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03  
**Rule:** only genuine blockers/uncertainties — no invented business rules

---

## Q1. Exact `lead_id` generation algorithm

| Field | Content |
|-------|---------|
| **Question** | What exact algorithm mints production `lead_id` (`LEAD_<12 hex>` vs UUID/ULID vs `lead_<hex>`)? |
| **Evidence** | Architecture says UUID/ULID at parse; live samples show multiple string shapes |
| **Consequence** | PG stores opaque `text`; import safe. New minting must match product code |
| **Recommended default** | Keep opaque text uniqueness; mint in workflow/parser as today until single generator is documented |
| **Operator decision before migration?** | No for import; **Yes** before freezing Toolkit mint helper |

---

## Q2. CLEAN / DEDUP writer: append vs upsert (live)

| Field | Content |
|-------|---------|
| **Question** | Is current production CLEAN/DEDUP writer still `append` with empty `matchingColumns` (Sep 1 evidence) or restored to upsert? |
| **Evidence** | Sep 1 node-run samples vs older soak docs claiming `appendOrUpdate` |
| **Consequence** | Import must collapse duplicates; shadow dual-write must use PG upsert regardless |
| **Recommended default** | Treat Sheets as dirty append-capable; PG enforces uniqueness |
| **Operator decision before migration?** | No — validation spec already requires collapse. Optional ops fix for Sheets hygiene |

---

## Q3. Full `LEAD_DELIVERIES` / reminder ledger column enums

| Field | Content |
|-------|---------|
| **Question** | Exact status enum and full column set for `LEAD_DELIVERIES` and `REMINDER_DELIVERIES`? |
| **Evidence** | Partial fields proven (`lead_id`, telegram message/chat ids, action token, `reminder_key`); full enum SAFE UNKNOWN |
| **Consequence** | `deliveries.status` uses platform outbox enum; import mapping may need a one-time adapter |
| **Recommended default** | Map success→`sent`, failure→`dead`/`retry`, unknown→`sent` if message id present else `pending` |
| **Operator decision before migration?** | Prefer sample export review; not a schema blocker |

---

## Q4. Dual lifecycle vocabularies

| Field | Content |
|-------|---------|
| **Question** | Should PG permanently support both CRM lifecycle (`reviewing`…) and Telegram ops (`processed`/`spam`/`pending`)? |
| **Evidence** | LEAD-LIFECYCLE-v1 vs live Admin callback/reminder selectors |
| **Consequence** | CHECK admits union; product UX must pick canonical labels |
| **Recommended default** | Keep union in V1 CHECK; document ops subset as runtime writers |
| **Operator decision before migration?** | Soft — confirm before Admin UX redesign |

---

## Q5. Local PostgreSQL runtime availability

| Field | Content |
|-------|---------|
| **Question** | When will disposable PG under `X:\MARS-Localhost\databases\mars-bot-data\` be installed for apply validation? |
| **Evidence** | **RESOLVED_BY_SCHEMA_TEST (2026-09-03):** portable PostgreSQL 17.11 under MARS-Localhost; empty `mars` → migrations → fixtures → suites PASS (incl. repeatability). See `evidence/local-validation/iseo-sales-schema-v1/` and `REPORT-mars-data-layer-iseo-local-postgres-validation-v1.md`. |
| **Consequence** | Local schema apply is execution-validated; VEESP PG 18 foundation remains a separate Server Ops gate |
| **Recommended default** | Keep disposable runtime non-authoritative; reproduce from Git migrations only |
| **Operator decision before migration?** | **No** for local proof claim; **Yes** still for production server foundation |
