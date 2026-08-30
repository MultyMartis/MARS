# I-SEO Report Hub — Summary Assembly Safe Fixture Scope v0.1

**Status:** CHARTER / SCOPE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Safe Fixture Charter 01  
**Depends on:** Summary Assembly Apply Implementation 01 (`PASS_WITH_LIMITED_WRITE_PROOF`)  
**Mode:** Option D — dedicated local fixture → one-block apply write proof → cleanup to baseline

This wave does **not** create the fixture. No app-source, runtime, DB, share, or PDF mutation.

---

## 1. Product goal

Provide a **repeatable, local-only, non-finalized** monthly report that can prove:

1. `GET /monthly-reports/{id}/assembly-preview` classifies work entries (4 / 2 / 1).
2. `POST /monthly-reports/{id}/assembly-apply` writes selected auto-block `report_blocks.body`.
3. Finalization locks still refuse report id **1**.
4. Existing snapshot / export / share / PDF of report id **1** stay unchanged.
5. Fixture rows can be removed by exact ids + marker so core table counts return to the pre-fixture baseline.

The fixture is **test infrastructure**, not a client report and not a reopen of report 1.

---

## 2. Locked option

| Option | Meaning | Verdict |
|--------|---------|---------|
| **A** Reuse monthly id **5** | Existing draft; 0 blocks / 0 entries; period id **3** is `2026-08` **archived** | **Rejected** |
| **B** Dedicated fixture, leave it in DB | Named local report, no cleanup | **Rejected** for Implementation 01 (pollutes local DB) |
| **C** Transaction-only fixture | Create + apply + rollback in one DB transaction | **Rejected** for HTTP write proof (browser/POST uses a separate connection) |
| **D** Backup → dedicated fixture → write proof → cleanup → verify counts | Explicit, practical, restores baseline | **Chosen MVP** |

Option D still uses a **dedicated** report (the useful part of B). The difference is **temporary lifetime**: rows exist only for the proof window.

---

## 3. Why not report id 1

Probed 2026-08-17 on `iseo_report_hub_dev` (SELECT only):

| Property | Value |
|----------|--------|
| id | **1** |
| status | `finalized` (`finalized_at` set) |
| period | id **1** / `2026-07` |
| blocks | **6**, all `reviewed` |
| work entries | **7** |
| snapshot | id **1** `monthly-1-v1` active |
| exports | **4** (all on monthly 1) |
| shares | **7** (active **1** id 7 / `test-first-link`; revoked **6**) |
| export 4 checksum prefix | `a8c4d61c6216e8d70b19` |

Apply is already refused here. Reopen is **out of scope**. Using id 1 would risk live preview vs issued PDF/share desync.

---

## 4. Why not report id 5

| Property | Value |
|----------|--------|
| id | **5** |
| status | `draft` |
| period | id **3** / `2026-08` **archived** |
| title | `Monthly report — 2026-08 — LOCAL_FIXTURE_ONLY` |
| blocks | **0** |
| work entries | **0** |
| exports / shares / snapshots | **0** for this monthly |

Reasons to leave it untouched:

- Origin is undocumented (foreign local residue). Apply Test Strategy already forbade seeding it without a dedicated fixture charter.
- Apply Implementation 01 does **not** INSERT missing shells; id 5 cannot prove apply.
- Parent period is **archived**. Seeding a working apply target onto an archived period is unclear and may collide with period CRUD semantics.
- `monthly_report_contents.reporting_period_id` is UNIQUE — id 5 already occupies period 3.
- Cleanup-by-marker would be unsafe on a row we did not create.

**Implementation 01 of this fixture must not UPDATE/DELETE id 5.**

---

## 5. Dedicated fixture shape

Create **one new** non-finalized monthly report in Implementation 01:

| Field | Decision |
|-------|----------|
| Display name | `MARS SAFE APPLY FIXTURE` |
| Marker | `MARS_FIXTURE_SUMMARY_APPLY_YYYYMMDD_HHMMSS` (unique per create run) |
| Also include | `LOCAL_FIXTURE_ONLY` so existing UI fixture badge still applies |
| Status | `in_progress` (allowed apply parent; not `finalized` / `archived`) |
| `finalized_at` | **NULL** |
| Snapshot / export / share / PDF | **None** — refuse create if any would be required; never insert these rows |
| Blocks | **6** shells (3 auto + 3 manual) |
| Work entries | **7** included, **0** excluded (mirror report 1 seed rules) |
| Weekly checkpoints | **Do not create** (assembly reads work entries, not weeklies) |
| Catalogue | **Reuse** existing `seo_work_categories` / `seo_work_items` (13 / 31) |
| Client / project / site | **Reuse** demo id **1** / `demo-client` / `demo-seo-project` / `https://demo.example.test` |
| Reporting period | **Create new** — cannot reuse `2026-07` (monthly 1) or `2026-08` (monthly 5); UNIQUE `(project_id, period_key)` |
| Users | **Reuse** existing users for `created_by` / `updated_by` (ids 1 and/or 2). Do not create users |

If demo client/project/site 1 is missing at impl time: create marked fixture parents and record those ids for cleanup. Current probe: they exist.

---

## 6. Persistent vs temporary

| Layer | Lifetime |
|-------|----------|
| Fixture **rows** | Temporary. Create → proof → cleanup in the same implementation wave. Do **not** leave the report in DB. |
| Fixture **scripts** | Persistent in `app-source/tools/` after Implementation 01 (guarded CLI). Not created in this charter wave. |
| Evidence JSON / dumps | STORAGE only; not git. |

Repeatability comes from the committed tool, not from a standing extra monthly report.

---

## 7. Tables populated vs reused

| Table | Action |
|-------|--------|
| `clients` / `projects` / `sites` | Reuse existing demo rows |
| `users` / `user_roles` / `roles` | Reuse |
| `seo_work_categories` / `seo_work_items` | Reuse |
| `reporting_periods` | **INSERT** one synthetic period (`period_key` unused, e.g. `2099-01`) |
| `monthly_report_contents` | **INSERT** one row |
| `report_blocks` | **INSERT** six rows |
| `monthly_report_work_entries` | **INSERT** seven rows |
| `weekly_checkpoints` | No change |
| `report_snapshots` / `report_exports` / `report_export_shares` | No change; **STOP** if fixture monthly accidentally gains any |
| `audit_log` | May gain fixture-create and apply events (acceptable residual after cleanup) |
| `schema_migrations` | No change |

---

## 8. How to guarantee no export / share / PDF relationship

1. Do not call snapshot / export / share / PDF services.
2. After create, SELECT counts for the new monthly id must be **0** snapshots, **0** exports, **0** shares.
3. Apply service already refuses `hasActiveShare`. Fixture must still have zero shares so the write path is the happy path, not the share gate.
4. Cleanup **STOP** if any snapshot/export/share rows exist for the fixture monthly (do not cascade-delete issued artifacts of unknown origin).
5. Report 1 export 4 checksum prefix and share 7 `active` / `test-first-link` are regression invariants.

---

## 9. How to identify as local / test-only

Required marker on every fixture-owned row that has a suitable text/JSON column:

- period `title` and `summary`
- monthly `title` and `internal_notes`
- each block `title` and `data_json.mars_fixture_marker`
- each work entry `internal_note`

Pattern:

```
MARS SAFE APPLY FIXTURE
MARS_FIXTURE_SUMMARY_APPLY_YYYYMMDD_HHMMSS
LOCAL_FIXTURE_ONLY
```

Do **not** use this marker on report 1, report 5, demo client, or catalogue rows.

Cleanup must match **exact marker + exact ids** from `fixture-ids.json`. Broad `LIKE '%FIXTURE%'` or date-only deletes are forbidden.

---

## 10. What this fixture is not

- Not reopen of report 1
- Not production data
- Not PDF regeneration
- Not screenshot QA
- Not client-report template work
- Not a standing second “real” demo report
- Not seeding of monthly id 5

---

## 11. SAFE UNKNOWN

- Exact autoincrement ids the next INSERT will receive (record at create time).  
- Whether operators later want a **standing** lab report after write proof exists. Default: no; recreate via script if needed.  
- Whether period `2099-01` is free at impl time — implementation must SELECT unused `period_key` if taken.
