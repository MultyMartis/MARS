# I-SEO Report Hub — Local Fixture Validation Plan v0.1

**Status:** PLANNING ONLY — validation executes in apply wave, not this charter  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Project/Client Local Fixture Charter 01  
**Related:** [I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Preflight counts

Before any insert (apply wave):

| Check | Expected |
|-------|----------|
| DB name | exactly `iseo_report_hub_dev` |
| DB host | exactly `127.0.0.1` |
| Migration count | **2** |
| Table count | **10** |
| `reporting_periods` exists | **yes** |
| users / roles | **1** / **6** |
| clients | **0** |
| projects | **0** |
| sites | **0** |
| reporting_periods rows | **0** |

If clients/projects already contain non-fixture rows: **STOP** and escalate (do not invent merge logic in first apply).

If demo slugs already exist from a partial prior run: tool may continue in idempotent mode, but report must document pre-counts ≠ 0/0/0/0.

---

## 2. Apply / tool execution

| Check | Expected |
|-------|----------|
| Tool path | `tools/create-local-fixture.php` (after source authoring + sync if required) |
| Target DB guard | Refuses non-local DB name/host |
| Execution | Creates or reuses demo client/project/site/(period) |
| Output | IDs + counts only |
| Secrets | None printed |
| Schema | Unchanged |
| Migrations ledger | Unchanged (no new migration for fixture data) |

---

## 3. After counts

Preferred success:

| Table | Count |
|-------|-------|
| clients | **1** |
| projects | **1** |
| sites | **1** |
| reporting_periods | **1** |

If period row is deferred by operator decision during apply: document `1/1/1/0` and still prove that a temporary period insert for unique/FK smoke either ran and rolled back cleanly **or** is explicitly postponed with STOP on unique smoke claim.

Idempotent re-run: counts remain **1/1/1/1**; no duplicates.

---

## 4. FK validation

| Check | Expected |
|-------|----------|
| Project row references demo client | `projects.client_id` = demo client id |
| Site row references demo project | `sites.project_id` = demo project id |
| Period row references demo project | `reporting_periods.project_id` = demo project id |
| Invalid project_id period insert | Refused by FK (optional negative probe) |
| User FKs on period | `owner_user_id` / `created_by` either NULL or existing local admin id |

---

## 5. Unique validation

| Check | Expected |
|-------|----------|
| Second client with slug `demo-client` | Refused (unique `uq_clients_slug`) or tool short-circuits |
| Second project same client + `demo-seo-project` | Refused / short-circuit |
| Second period same project + `2026-07` | Refused by `uniq_reporting_periods_project_period` |
| Alternate period_key same project (e.g. `2026-08`) | Allowed if tested; not required for baseline fixture |

Primary unique smoke for DB-03: **duplicate `2026-07` on demo project must fail**.

---

## 6. Health / app smoke

| Check | Expected |
|-------|----------|
| `GET /health` | HTTP **200**; DB connection pass; migration count **2** |
| Health expected table wording | May still show `9/9` — known limitation; do not fail fixture wave solely on that |
| `GET /login` | HTTP **200** |
| `GET /not-existing` | HTTP **404** |
| App/auth code | Unchanged unless apply charter separately allows only the fixture tool |

---

## 7. Auth smoke

| Check | Expected |
|-------|----------|
| Local admin still present | email `admin@iseo-report-hub.test` |
| Login / dashboard | Still works (session path unchanged) |
| Logout | Still works |
| Password / hash | Never printed or committed |

---

## 8. Audit validation (if implemented)

| Check | Expected |
|-------|----------|
| Optional `audit_log` event | Present with fixture marker / entity refs |
| Metadata | No secrets |
| Actor | Local admin id or NULL per tool design |

If audit write is skipped: document as intentional; not a hard STOP unless apply charter makes it mandatory.

---

## 9. Rollback / cleanup notes

| Rule | Policy |
|------|--------|
| Same-wave automatic destructive cleanup | **Forbidden** |
| DROP / TRUNCATE | **Forbidden** |
| Future cleanup | Separate tool/charter; delete only `LOCAL_FIXTURE_ONLY` / demo-slug rows |
| Production cleanup | **Never** |
| Failed mid-apply | Prefer transactional insert where practical; report partial state honestly |

---

## 10. STOP conditions

STOP apply wave if:

- DB is not exactly `iseo_report_hub_dev` @ `127.0.0.1`
- Tool would mutate production/remote DB
- Real client data would be inserted
- Schema change is required to proceed
- Non-fixture client/project rows already block safe demo identity without operator decision
- Unique/FK smoke cannot be evidenced and report would falsely claim full smoke
- Secrets would appear in Git or tool stdout intended for reports
- Staged git area contains non-allowlisted paths for the apply commit

Charter wave STOP (this wave): any app-source/runtime/DB mutation, SQL/tool creation, or fixture row insert.
