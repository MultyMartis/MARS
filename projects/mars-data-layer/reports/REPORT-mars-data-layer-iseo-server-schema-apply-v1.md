# REPORT — mars-data-layer iSEO server schema apply v1

**Document:** `REPORT-mars-data-layer-iseo-server-schema-apply-v1`  
**Date:** 2026-09-03  
**Mode:** Agent — Cursor Auto  
**Process-line:** MARS DATA LAYER — SERVER PG18 APPLICATION SCHEMA APPLY / VALIDATION  
**Worktree:** `X:\AI MARS\worktrees\mars-data-layer-iseo-server-schema-apply-01`  
**Branch:** `wave/mars-data-layer-iseo-server-schema-apply-01`  
**Baseline tip:** `eb19cfad` (`origin/mars/canonical-post-recovery`)

Evidence root: `projects/mars-data-layer/evidence/server-validation/iseo-sales-schema-v1/`  
Tool (operator assist): `projects/mars-data-layer/tools/server-iseo-schema-apply-01.py`

---

## 1. Verdict

**SERVER PG18 SCHEMA APPLY PASS — ISEO SALES READY FOR SHADOW DATA MIGRATION**

Canonical Git migrations for `mars_core` + `app_iseo_sales` applied on VEESP-N8N-01 PostgreSQL **18.0**. Constraint, permission, function, idempotency, status-transition, outbox, job, inventory/EXPLAIN suites PASS. n8n unchanged. PRE/POST logical dumps on server. No Sheets import; no workflow cutover.

---

## 2. Server foundation

| Item | Value |
|---|---|
| Host / service | `mars-postgres` |
| Port (container) | `5432` |
| Database | `mars` |
| Network | `mars-postgres-net` |
| TLS | `disable` |
| Volume | `mars-postgres-data` |
| Public `5432` | **NOT EXPOSED** (PortBindings empty) |
| PostgreSQL | **18.0** (Debian 18.0-1.pgdg13+3) |
| Architecture change this wave | **None** |

---

## 3. Preflight

See `PREFLIGHT-v1.md`.

- Container healthy/running; version 18.0 confirmed.
- Unexpected application objects before apply: **0**.
- Disk/RAM/load captured; n8n API **36** workflows / **7** active.
- No STOP condition (no unknown app tables).

---

## 4. Pre-migration backup

See `PRE-MIGRATION-DUMP-v1.md`.

| Field | Value |
|---|---|
| timestamp_utc | `20260903T073534Z` |
| database | `mars` |
| format | plain SQL gzip |
| path | `/root/mars-backups/postgres/mars-pre-app-schema-20260903T073534Z.sql.gz` |
| size_bytes | `710` |
| gzip -t | PASS |

---

## 5. Migrations applied

See `MIGRATION-APPLY-v1.md`.

**Order (canonical only):**

1. roles / `001_*`
2. `database/core/0001_*`, `0002_*`
3. `database/app_iseo_sales/0001_*` … `0004_*`

| Field | Value |
|---|---|
| Bootstrap role (name only) | `mars_admin` |
| DDL role | `mars_migrator` (`SET ROLE` + `GRANT CREATE ON DATABASE mars`) |
| Runtime roles | **not** used for DDL |
| Result | APPLY SUCCESS |
| Object owner | `mars_migrator` |

No manual schema recreation. No secrets in evidence.

---

## 6. PG17→PG18 compatibility

See `PG17-TO-PG18-COMPATIBILITY-v1.md`.

| Classification | **PASS** |
|---|---|
| Local | PostgreSQL **17.11** |
| Server | PostgreSQL **18.0** |
| Migration SQL changes for PG18 | **None required** |
| Source fix this wave | `tests/iseo_sales/05_inventory_and_explain.sql` (invalid `n.nspname` probe — test bug, fixed in Git) |

---

## 7. mars_core

Present as designed: `schema_migrations`, `apps`, `data_contract_versions`, `workflow_releases` (+ indexes/constraints). Remains control metadata only — no iSEO business data introduced by this wave beyond migration/control seeds from Git.

Application migration recording: uses `mars_core.schema_migrations` as defined by source — **no invented** live registry outside migrations.

---

## 8. app_iseo_sales inventory

See `SCHEMA-INVENTORY-v1.md` and `SCHEMA-INVENTORY-RAW-v1.md`.

Tables, sequences, indexes, constraints, and nine functions (including `register_inbound_event`, `upsert_lead`, `change_lead_status`, `enqueue_delivery`, `enqueue_job`, `claim_jobs`) owned by `mars_migrator`. Expected set: **Valid**.

---

## 9. Roles / security

See `PERMISSION-TESTS-v1.md`, `ISOLATION-AND-IMMUTABILITY-v1.md`.

Roles exercised: `mars_migrator`, `iseo_runtime`, `iseo_agent`, `iseo_reader`.

| Role | Intended | Forbidden proven |
|---|---|---|
| `iseo_runtime` | App DML / approved functions | DDL; immutable event UPDATE/DELETE; foreign schema write |
| `iseo_agent` | Narrow functions | Arbitrary business UPDATE/DELETE; DDL |
| `iseo_reader` | SELECT | Writes |
| PUBLIC | no unnecessary create/write | suite PASS |

Permissions were not weakened to pass tests. Production n8n application PG credential **not** configured in this wave.

---

## 10. Constraints

**PASS** — `02_constraints.sql` (synthetic only). Duplicate source identity, `lead_id` uniqueness, FK, NOT NULL, CHECK behaviors match design. Synthetic rows cleaned after suites.

---

## 11. Idempotency

**IDEMPOTENCY = PASS** — same source / same idempotency key does not duplicate logical side effects (`04_extended_local_validation.sql`).

---

## 12. Functions

**PASS** — normal / duplicate / invalid paths for inbound register, lead upsert, status change, delivery enqueue, job enqueue (DB only; no Telegram/Gmail).

---

## 13. Status transitions

**PASS** — single atomic state change; domain event + audit append; stale expected version/state rejected; repeated idempotency key does not duplicate mutation.

---

## 14. Events / audit

**PASS** — append-on-transition; runtime cannot UPDATE/DELETE immutable `lead_events` history (privilege denial).

---

## 15. Outbox

**PASS** — business mutation + delivery intent in one DB transaction (no actual Telegram send; no n8n workflow).

---

## 16. Jobs / retry

**PASS** — pending / `available_at` / claim / retry / attempts / lease / completed-dead semantics exercised where implemented (`claim_jobs`, job suite paths in extended SQL). Concurrent double-claim residual: covered by `FOR UPDATE SKIP LOCKED` design + suite; no production load test.

---

## 17. Isolation

**PASS** — iSEO runtime/agent cannot write into placeholder `app_seo_content`. No SEO Content model built.

---

## 18. Index / query sanity

See `INDEX-EXPLAIN-v1.md`.

**EXPECTED INDEX USAGE = PASS** — hot lookups (inbound source, lead_id, pending leads, available jobs, pending deliveries) show Index/Bitmap Index Scan where data exists; Seq Scan acceptable on empty tables. No benchmark campaign.

---

## 19. Resource impact

See `RESOURCES-v1.md`.

| Metric (post-test) | Value |
|---|---|
| Host RAM | 3.8 GiB total; ~2.6 GiB available |
| Swap used | ~268 KiB |
| `mars-postgres` RSS | ~33.9 MiB |
| `n8n_n8n_1` RSS | ~1.106 GiB |
| Load avg | ~0.33 / 0.30 / 0.27 |
| Disk `/` | 66% used (~27G avail) |

**CURRENT PG18 + N8N RESOURCE HEADROOM:** **HEALTHY**  
No aggressive tuning this wave.

---

## 20. n8n unchanged

See `N8N-UNCHANGED-v1.md`.

- Same container ID and StartedAt; RestartCount `0`.
- Version still **2.14.2**.
- Workflows API before/after: **36** / **7** active.
- No recreate/restart; SQLite untouched; no Telegram synthetic sends; no production PG credential bind.

---

## 21. Post-apply backup

See `POST-APPLY-DUMP-v1.md`.

| Field | Value |
|---|---|
| timestamp_utc | `20260903T074124Z` |
| path | `/root/mars-backups/postgres/mars-post-app-schema-20260903T074124Z.sql.gz` |
| size_bytes | `10387` |
| role | **schema baseline before Sheets shadow import** |

Dump files remain **on server only** (not copied into Git).

---

## 22. Open questions

See `architecture/ISEO-SALES-DATA-OPEN-QUESTIONS-v1.md`.

| ID | Status |
|---|---|
| Q1–Q4 | **Preserved** (business; not resolved by synthetic server tests) |
| Q5 | Local + **server schema apply** evidence recorded; schema-apply claim no longer blocked |

---

## 23. Git

- Worktree branch: `wave/mars-data-layer-iseo-server-schema-apply-01`
- Scope committed: `projects/mars-data-layer/**` only
- Primary dirty tree `X:\AI MARS` **not** mutated
- No secrets; no server dump blobs in Git

---

## 24. Residuals

- Concurrent job claim under heavy multi-session load not stress-tested (design + suite only).
- Production n8n ↔ application PG credential binding deferred.
- Live Sheets data still outside PostgreSQL.
- Business open questions Q1–Q4 remain for product/ops.

---

## 25. Next gate

**STRICT STOP.** Next wave only:

`ISEO SALES SHEETS → POSTGRES SHADOW MIGRATION`

Do **not**: import Sheets in this report’s scope; change Sheets authority; create Operational.v3.dev; bind production workflows to PostgreSQL; activate PG-backed production processing; cutover.
