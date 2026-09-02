# REPORT — mars-data-layer iSEO local PostgreSQL validation v1

**Document:** `REPORT-mars-data-layer-iseo-local-postgres-validation-v1`  
**Date:** 2026-09-03  
**Mode:** Agent — Cursor Auto  
**Process-line:** MARS BOT DATA PLATFORM — LOCAL DISPOSABLE POSTGRES RUNTIME / ISEO SCHEMA EXECUTION VALIDATION  
**Worktree:** `X:\AI MARS\worktrees\mars-data-layer-iseo-local-postgres-validation-01`  
**Branch:** `wave/mars-data-layer-iseo-local-postgres-validation-01`  
**Baseline tip:** `eb19cfad` (`origin/mars/canonical-post-recovery`)

Evidence root: `projects/mars-data-layer/evidence/local-validation/iseo-sales-schema-v1/`

---

## 1. Verdict

**LOCAL POSTGRES VALIDATION PASS — ISEO SALES MIGRATIONS READY FOR SERVER FOUNDATION**

Empty `mars` → all Git migrations → synthetic fixtures → constraint / permission / extended suites PASS. Repeatability proven on reset (pass 2 and pass 3). No production systems touched.

---

## 2. Local environment

See `LOCAL-ENV-INVENTORY-v1.md`.

| Capability | Present | Notes |
|---|---|---|
| PostgreSQL (pre-task) | No | |
| Docker / Podman | No | |
| WSL | No | |
| Laragon | Yes | MySQL **3306** untouched |
| Port 5432 | Free | Local PG on **5433** |

---

## 3. Runtime chosen

**Option C — portable PostgreSQL 17.11** under `X:\MARS-Localhost\` (least invasive available).

- Runtime: `X:\MARS-Localhost\databases\mars-bot-data\` (non-authoritative)
- Binaries: `X:\MARS-Localhost\tools\postgresql\17.11\pgsql\`
- Listen: `127.0.0.1:5433`
- Secrets: `X:\AI MARS\local\mars-bot-data\` (never committed)

Option D (system-wide service) was **not** performed.

---

## 4. Database / migration apply

Contract **EMPTY DB → ALL MIGRATIONS → SUCCESS** met.

Order: roles → core 0001–0002 → app_iseo_sales 0001–0004 → synthetic fixtures.

Windows runner: `tests/iseo_sales/apply_and_test.ps1` (same SQL order as `01_schema_apply.sh`).

---

## 5. mars_core

Schemas/tables/indexes/grants present as designed (`schema_migrations`, `apps`, `data_contract_versions`, `workflow_releases`). Ownership `mars_owner`. PUBLIC permissions follow security standard as applied by migrations.

---

## 6. app_iseo_sales

All expected tables, indexes, and functions present. Inventory: `SCHEMA-INVENTORY-v1.md`. Placeholder schema `app_seo_content` exists for isolation tests.

---

## 7. Constraints

PASS — inbound unique source, lead upsert/unique lead_id, FK, NOT NULL/CHECK (`CONSTRAINT-TESTS-v1.md`).

---

## 8. Idempotency

PASS — inbound source idempotency; status transition idempotency key; stale version/status rejected (`IDEMPOTENCY-TESTS-v1.md`).

---

## 9. Functions

PASS — `register_inbound_event`, `upsert_lead`, `change_lead_status`, `enqueue_delivery`, `enqueue_job` valid / duplicate / invalid paths (`FUNCTION-TESTS-v1.md`).

---

## 10. Status transitions

PASS — atomic update + event + audit once; duplicate idempotency key does not duplicate side effects; stale expected state rejected.

---

## 11. Events / audit

PASS — domain events append correctly; runtime cannot UPDATE/DELETE event rows (immutability).

---

## 12. Deliveries / outbox

PASS — DB-only outbox/delivery intent with business state; no Telegram call (`OUTBOX-TESTS-v1.md`).

---

## 13. Jobs / retry

PASS — pending / available_at / lease / claim exclusivity via SKIP LOCKED (`JOB-TESTS-v1.md`).

---

## 14. Permissions

PASS — `iseo_runtime` / `iseo_agent` / `iseo_reader` boundaries (`PERMISSION-TESTS-v1.md`).

---

## 15. Isolation

PASS structural — `iseo_runtime` has no USAGE/CREATE on `app_seo_content`. Full SEO content app schema remains future work.

---

## 16. Migration repeatability

PASS — reset disposable DB, reapply from zero twice after first success (`MIGRATION-REPEATABILITY-v1.md`).

---

## 17. Performance sanity

Hot lookups use expected indexes (Index Scan on inbound source, lead_id, jobs status/available_at). No benchmarking project; no micro-optimization.

---

## 18. Open questions

See `OPEN-QUESTIONS-STATUS-v1.md`.

- **Q5** → `RESOLVED_BY_SCHEMA_TEST`
- Q1–Q4 remain operator / forensic / non-blocking as classified — not guessed.

---

## 19. Source fixes

**Authoritative migration SQL:** no bugfix required.

**Test harness additions (this wave):**

- `04_extended_local_validation.sql`
- `05_inventory_and_explain.sql`
- `apply_and_test.ps1`

Harness corrections only (argument order, claim assertions, ambiguous variable names, unique run IDs).

---

## 20. Server Ops compatibility

Handoff still targets **PostgreSQL 18** on VEESP — unchanged as production requirement.

Local validation used portable **17.11**; migrations applied cleanly. Added note to handoff: local proof does not replace server foundation execution.

**No server work executed.**

---

## 21. Git

- Clean worktree branch `wave/mars-data-layer-iseo-local-postgres-validation-01`
- Commit only under `projects/mars-data-layer/` (tests, evidence, report, handoff note)
- **Not committed:** `X:\MARS-Localhost\databases\mars-bot-data\`, tools binaries, `X:\AI MARS\local\mars-bot-data\` secrets
- Message: `test(mars-data-layer): validate iSEO schema on local PostgreSQL`
- Push: non-force

---

## 22. Next gate

1. Server Ops: execute PostgreSQL 18 foundation on VEESP-N8N-01 per handoff (separate charter).
2. Data-layer: apply same migrations as `mars_migrator` on server empty DB.
3. Operator decisions on open questions Q1–Q4 before production cutover.
4. Do **not** migrate Sheets / change n8n until those gates clear.

---

## Strict stops observed

- No VEESP-N8N-01 / production n8n / Google Sheets / production workflows / production credentials / production data
- No Laragon website DB changes
- No system-wide PostgreSQL Windows service install
