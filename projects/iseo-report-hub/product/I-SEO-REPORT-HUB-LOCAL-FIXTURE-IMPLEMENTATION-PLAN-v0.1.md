# I-SEO Report Hub — Local Fixture Implementation Plan v0.1

**Status:** PLANNING ONLY — execute in next wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Project/Client Local Fixture Charter 01  
**Related:** [I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md)

---

## 1. Next wave name

**`I-SEO Report Hub — Project/Client Local Fixture Apply 01`**

Purpose: implement and run a local-only fixture tool that creates the demo client/project/site/(period) baseline so DB-03 FK/unique smoke and later Reporting Period CRUD have a safe FK target.

---

## 2. Preferred tool

| Field | Value |
|-------|-------|
| Preferred path | `app-source/tools/create-local-fixture.php` |
| Runtime copy | Sync to `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\create-local-fixture.php` when apply charter authorizes source→runtime sync for that file |
| Not preferred | Schema seed migration; one-off operator SQL as primary path |
| Behavior | Idempotent; refuse non-local DB; print IDs/counts only; optional audit event |

Suggested CLI surface (planning only; exact argv finalized in apply):

- default: create/reuse demo client + project + site + period
- flags may include dry-run / skip-period — **SAFE UNKNOWN** until apply designs argv

---

## 3. Allowed app-source files next wave

| Path | Purpose |
|------|---------|
| `app-source/tools/create-local-fixture.php` | Fixture CLI |
| Optional short tool README / comment header only if needed | Operator usage notes (no secrets) |
| Result docs under `product/` | Apply result |
| Closeout under `reports/` | Apply report |
| `OPERATIONAL-INDEX.md` | Status update |

**Not allowed without separate charter:** auth/controllers/views changes, schema migrations, HealthController expected-table fix (unless operator expands apply charter explicitly).

---

## 4. DB actions allowed next wave

On `iseo_report_hub_dev` @ `127.0.0.1` only:

1. Insert **one** demo client (`demo-client`) if absent  
2. Insert **one** demo project (`demo-seo-project`) if absent  
3. Insert **one** demo site (`demo.example.test` / agreed url) if absent  
4. Insert **one** demo reporting_period (`2026-07`) if absent  
5. Optional: one `project_type_profiles` row  
6. Optional: one `audit_log` fixture event  

---

## 5. DB actions not allowed

- Any production / remote DB
- Real client / project / domain data
- Destructive cleanup (DELETE of non-fixture rows, DROP, TRUNCATE)
- Schema CREATE/ALTER beyond existing tables
- New migration for seed data
- Password / user / role mutations
- `.env` / `.env.local` edits
- Broad table wipes

---

## 6. Smoke list

1. Preflight identity + counts  
2. Tool create (or idempotent reuse)  
3. After counts `1/1/1/1` (or documented deferral)  
4. FK chain client → project → site / period  
5. Unique duplicate period refused  
6. Idempotent second tool run  
7. `/health` 200 + DB pass  
8. Login / dashboard / logout still work  
9. No secrets in stdout/docs/Git  
10. Result + report docs + OPERATIONAL-INDEX update  

---

## 7. Commit policy

- Exact-path staging only (apply charter allowlist)
- No `git add .` / `-A` / `commit -a`
- Foreign WIP preserved
- Commit and push are separate; **push only if apply charter explicitly authorizes**
- Suggested primary message shape: `feat(iseo-report-hub): add local fixture tool` (finalize in apply charter)
- Docs-only hash-record follow-up if report needs commit hash

---

## 8. STOP conditions

STOP apply if:

- Preflight volume/branch/index/WIP rules fail
- DB target/host mismatch
- Tool cannot enforce local-only guard
- Real data would be required to proceed
- Schema change appears necessary
- Unique/FK smoke cannot be completed honestly
- Non-allowlisted paths enter the index
- Operator charter scope is exceeded (CRUD UI, production, cleanup)

---

## 9. Sequencing after apply

After successful Local Fixture Apply 01:

**Recommended next:** `Reporting Period CRUD Charter 01`

Rationale: project FK exists; unique/FK smoke evidenced; CRUD can target demo project without real client import.
