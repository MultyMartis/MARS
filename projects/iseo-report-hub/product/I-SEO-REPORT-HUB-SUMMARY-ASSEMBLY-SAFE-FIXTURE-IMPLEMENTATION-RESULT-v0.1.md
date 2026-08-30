# I-SEO Report Hub — Summary Assembly Safe Fixture Implementation Result v0.1

**Status:** IMPLEMENTED (local write proof + cleanup)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Safe Fixture Implementation 01  
**Verdict:** `SUMMARY ASSEMBLY SAFE FIXTURE PASS`

Guarded local fixture tool created a temporary marked monthly, applied `next_month_plan` only, then removed fixture rows by exact ids. Report id **1** and id **5** unchanged. Baseline counts restored except `audit_log` (+2) and AUTO_INCREMENT gaps.

---

## 1. Tool

| Field | Value |
|-------|--------|
| Path | `app-source/tools/summary-assembly-safe-fixture.php` |
| Commands | `--create --confirm-local-fixture`; `--cleanup --ids=<path> --confirm-local-fixture` |
| Guards | CLI only; confirm flag; `APP_ENV=local`; DB name `iseo_report_hub_dev`; host `127.0.0.1`; local `APP_URL`; refuse monthly ids 1 and 5 |
| Marker | `MARS_FIXTURE_SUMMARY_APPLY_YYYYMMDD_HHMMSS` + `LOCAL_FIXTURE_ONLY` |
| Cleanup | exact JSON ids + marker match; order blocks → entries → monthly → fixture period; STOP if snapshot/export/share rows exist |

Do not commit `fixture-ids.json`, dumps, or STORAGE evidence.

---

## 2. Fixture shape (temporary)

This run:

| Piece | Value |
|-------|--------|
| Marker | `MARS_FIXTURE_SUMMARY_APPLY_20260817_134426` |
| Period | id **4**, `2099-01`, `active` |
| Monthly | id **6**, `in_progress`, not 1 or 5 |
| Blocks | 6 (`executive_summary` 10 … `next_month_plan` 15) |
| Entries | 7 (ids 9–15): done 4 / plan 2 / risk 1 / excluded 0 |
| Snapshots / exports / shares for fixture | **0** |
| Parents | client/project/site **1**; users **1** (CLI) and **2** (owner) |

Rows existed only for the proof window. Cleanup deleted them.

---

## 3. Write proof

| Check | Result |
|-------|--------|
| Preview | `GET /monthly-reports/6/assembly-preview` **200**; apply form enabled |
| Counts | done **4** / plan **2** / risks **1** / included **7** / excluded **0** |
| POST | `POST /monthly-reports/6/assembly-apply` with CSRF, `block_keys[]=next_month_plan`, `confirm_overwrite=1` → **302** `/monthly-reports/6` |
| Old body | placeholder `Черновой план до применения сборки. LOCAL_FIXTURE_ONLY` + marker |
| New body | Block Text Contract (intro + 2 plan bullets) |
| `summary` | unchanged |
| Other 5 blocks | unchanged |
| Work entries | unchanged |
| Monthly flats / status | unchanged (`in_progress`, flats NULL) |
| `next_month_plan.status` | `draft` → `in_progress` |
| Marker in `data_json` | kept |

Expected new body:

```
В следующем периоде запланированы работы:

- Запланирована доработка мета-тегов.
- Запланирована подготовка новых текстов.
```

---

## 4. Cleanup / baseline

Deleted: 6 blocks, 7 entries, monthly 6, period 4. Marker rows remaining: **0**.

| Metric | Before | After create | After apply | After cleanup |
|--------|--------|--------------|-------------|----------------|
| periods | 2 | 3 | 3 | **2** |
| monthly | 2 | 3 | 3 | **2** |
| blocks / r1 / r5 | 6 / 6 / 0 | 12 / 6 / 0 | 12 / 6 / 0 | **6 / 6 / 0** |
| entries / r1 / r5 | 7 / 7 / 0 | 14 / 7 / 0 | 14 / 7 / 0 | **7 / 7 / 0** |
| exports / shares / active / revoked | 4 / 7 / 1 / 6 | same | same | **same** |
| fixture marker monthlies | 0 | 1 | 1 | **0** |
| audit_log | 54 | — | — | **56** |

Acceptable residual: `audit_log` +2; AUTO_INCREMENT gaps (period 4, monthly 6, blocks 10–15, entries 9–15 will not be reused).

---

## 5. Safety locks

- Report id **1**: finalized; 6 blocks; 7 entries; `updated_at` max `2026-07-27 01:46:07`; body SHA unchanged.
- Report id **5**: draft; 0 blocks; 0 entries.
- Export 4 checksum prefix `a8c4d61c6216e8d70b19`; size 117055 unchanged.
- Share 7 `active` / `test-first-link`; shares 7 / active 1 / revoked 6.
- No PDF regeneration; no production; no `.env` edits.

---

## 6. Runtime sync

Exact file: `tools/summary-assembly-safe-fixture.php` source → runtime. No `.env` / storage / export / PDF / vendor / DB / WordPress.

---

## 7. Next

`Operator manual summary apply UI click-through`

Not next: reopen report 1; seed report 5; multi-block apply as default; PDF; Client Report Template Visual Alignment; screenshot QA; production; push.
