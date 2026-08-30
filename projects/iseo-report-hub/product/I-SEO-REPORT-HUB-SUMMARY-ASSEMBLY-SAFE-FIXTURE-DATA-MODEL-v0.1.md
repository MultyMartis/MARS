# I-SEO Report Hub — Summary Assembly Safe Fixture Data Model v0.1

**Status:** CHARTER / DATA MODEL — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Safe Fixture Charter 01

No rows are inserted in this wave. Column lists come from committed migrations + 2026-08-17 SELECT probe.

---

## 1. Parent chain (required)

```
users (existing)
clients id 1  →  projects id 1  →  sites id 1
                 └── reporting_periods [NEW]
                        └── monthly_report_contents [NEW]
                               ├── report_blocks × 6 [NEW]
                               └── monthly_report_work_entries × 7 [NEW]
```

`monthly_report_contents.reporting_period_id` is **UNIQUE**.  
`reporting_periods` is **UNIQUE** on `(project_id, period_key)`.

Current occupied period keys on project 1: `2026-07`, `2026-08`.  
Recommended new key: `2099-01` (synthetic; not a real client month). If taken, pick the next unused `2099-MM`.

Weekly checkpoints are **not** in the chain. `source_weekly_checkpoint_ids` on monthly/blocks may be JSON `[]` or NULL.

---

## 2. Reused entities (do not create, do not delete)

| Entity | Probe 2026-08-17 | Role |
|--------|------------------|------|
| Client | id 1 `demo-client` / Demo Client | FK parent |
| Project | id 1 `demo-seo-project` | FK parent |
| Site | id 1 `https://demo.example.test` | Not FK of monthly; keep for org consistency |
| Categories | 13 `seo_work_categories` | Optional FK on entries |
| Work items | 31 `seo_work_items` | Optional FK on entries |
| User id 1 | `admin@iseo-report-hub.test` | `created_by` fallback |
| User id 2 | `polygon-ws@mail.ru` | Apply HTTP actor (local test login) |

Do not print passwords/hashes. Do not create a third user.

`created_by` / `updated_by` / `created_by_user_id` / `updated_by_user_id`: use user **2** if the row is created in a session-backed path; CLI tool may use user **1**. Record the chosen id in `fixture-ids.json`.

---

## 3. New `reporting_periods` row

| Column | Value |
|--------|--------|
| `project_id` | `1` |
| `period_key` | `2099-01` unless collision |
| `period_start` | `2099-01-01` |
| `period_end` | `2099-01-31` |
| `status` | `draft` or `active` (not `finalized` / `archived`) |
| `title` | `MARS SAFE APPLY FIXTURE — {MARKER} — LOCAL_FIXTURE_ONLY` |
| `summary` | `{MARKER}` |
| `owner_user_id` / `reviewer_user_id` | existing user or NULL |
| `created_by` / `updated_by` | existing user |
| `finalized_at` | **NULL** |

---

## 4. New `monthly_report_contents` row

| Column | Value |
|--------|--------|
| `reporting_period_id` | new period id |
| `status` | `in_progress` |
| `title` | `MARS SAFE APPLY FIXTURE — {MARKER} — LOCAL_FIXTURE_ONLY` |
| Flat text columns (`executive_summary` … `next_month_plan`) | NULL or short marker note — **not** the apply target |
| `client_notes` | NULL |
| `internal_notes` | `{MARKER}` |
| `source_weekly_checkpoint_ids` | NULL or `[]` |
| `owner_user_id` | existing user |
| `finalized_at` | **NULL** |
| `reviewed_at` | NULL |

Apply writes **`report_blocks.body` only**, not these flat columns. Keep flats empty or marker-only so a mistaken dual-write is detectable.

---

## 5. New `report_blocks` (exactly 6)

`block_type` = `block_key` for all six. Status **`draft`** (writable; not `archived` / `reviewed`).

| `block_key` | RU title | `sort_order` | Apply? | Initial `body` | Initial `summary` |
|-------------|----------|--------------|--------|----------------|-------------------|
| `executive_summary` | Краткое резюме | 10 | **No** | non-empty marker prose | marker or short RU |
| `work_completed` | Что сделали | 20 | Yes (not in first proof) | empty or marker | NULL or marker |
| `results_summary` | Результаты | 30 | **No** | non-empty marker prose | marker or short RU |
| `risks_and_blockers` | Риски и блокеры | 40 | Yes (not in first proof) | empty or marker | NULL or marker |
| `key_findings` | Ключевые выводы | 50 | **No** | non-empty marker prose | marker or short RU |
| `next_month_plan` | План на следующий месяц | 60 | **Yes — first proof** | **non-empty placeholder that differs from generated apply text** | short stale teaser (proves `summary` unchanged) |

Required overwrite-warning case: **`next_month_plan.body` must be non-empty** and **must not** equal the Block Text Contract output.

Recommended placeholder body:

```
PLACEHOLDER — MARS SAFE APPLY FIXTURE
This text must be overwritten by assembly apply.
{MARKER}
```

`data_json` (object, not a JSON array):

```json
{
  "mars_fixture_marker": "MARS_FIXTURE_SUMMARY_APPLY_YYYYMMDD_HHMMSS"
}
```

If `data_json` is an object, apply may merge provenance keys. Starting as an object is required so merge is testable.

Manual blocks remain present so preview shows three auto + three manual cards, and so apply of a forbidden key can be refused without missing-row skips.

---

## 6. New `monthly_report_work_entries` (exactly 7)

Mirror `tools/seed-nikita-catalogue.php` `monthlyFixtures()`, retargeted to the **new** monthly id. Unique titles per report (seed uniqueness is `monthly_report_id` + `title`).

| # | `period_role` | `status` | `client_visibility` | `sort_order` | Maps to |
|---|---------------|----------|---------------------|--------------|---------|
| 1 | `done` | `done` | `client_safe` | 10 | `work_completed` |
| 2 | `done` | `done` | `client_safe` | 20 | `work_completed` |
| 3 | `done` | `done` | `client_safe` | 30 | `work_completed` |
| 4 | `done` | `done` | `client_safe` | 40 | `work_completed` |
| 5 | `planned_next` | `planned` | `client_safe` | 50 | `next_month_plan` |
| 6 | `planned_next` | `planned` | `client_safe` | 60 | `next_month_plan` |
| 7 | `risk` | `blocked` | `client_safe` | 70 | `risks_and_blockers` |

**Excluded count: 0.** Do not add an `internal` or `cancelled` row in this MVP. A later edge-case fixture may add exclusions.

Copy titles / `client_summary` from the catalogue seed (client-safe demo sentences). Set `internal_note` to `{MARKER}` on every fixture entry (internal notes are excluded from apply body).

Reuse the same `work_item_slug` / `category_slug` mappings as the seed. Resolve ids by slug at create time; do not hardcode catalogue ids.

Expected preview stats after create:

| Stat | Value |
|------|--------|
| done / `work_completed` | **4** |
| plan / `next_month_plan` | **2** |
| risks / `risks_and_blockers` | **1** |
| included | **7** |
| excluded | **0** |

---

## 7. Expected apply body for `next_month_plan`

If entries match the seed summaries, `MonthlyReportSummaryAssemblyService::formatBlockBody` must produce:

```
В следующем периоде запланированы работы:

- Запланирована доработка мета-тегов.
- Запланирована подготовка новых текстов.
```

Write-proof compares captured new body to this contract (whitespace-normalized). Do not invent different verbs.

---

## 8. Entities that must stay zero for the fixture monthly

| Table | Count for new monthly id |
|-------|--------------------------|
| `report_snapshots` | 0 |
| `report_exports` | 0 |
| `report_export_shares` (via exports) | 0 |

No PDF files under runtime export storage for this monthly.

---

## 9. Marker strategy

| Location | How |
|----------|-----|
| Run id | `MARS_FIXTURE_SUMMARY_APPLY_` + UTC `Ymd_His` at create |
| Evidence | `fixture-ids.json` stores marker + all created ids + reused parent ids |
| Period / monthly title | human-readable + marker + `LOCAL_FIXTURE_ONLY` |
| Block `data_json.mars_fixture_marker` | exact marker |
| Entry `internal_note` | exact marker |
| Cleanup | load JSON; verify marker on each owned row; refuse on mismatch |

Do not put the marker only in `updated_at`. Do not rely on AUTO_INCREMENT ranges without JSON ids.

---

## 10. Dual-content path

Fixture monthly should have **non-archived blocks** so preview/render uses `blocks_primary`. Flat monthly columns are not apply targets.

---

## 11. SAFE UNKNOWN

- Whether `owner_user_id` NULL vs user 2 changes any apply gate (apply uses session user, not owner). Default: set owner to user 2.  
- Live catalogue slug existence if a future operator truncated items — create must resolve slugs and **STOP** if missing rather than insert catalogue rows.
