# I-SEO Report Hub — Demo Scenario «ПРОВЕРКА.рa» Data Spec v0.1

**Status:** seed design only — **no entity creation in this wave**  
**Date:** 2026-08-21  
**Operator “today”:** `2026-08-21`  
**Marker:** `MARS_DEMO_PROVERKA_20260821`  
**ASCII slug:** `proverka-demo`

---

## 1. Display names (literal preservation)

| Entity | Display value | Technical |
|--------|---------------|-----------|
| Client | `ПРОВЕРКА.рa` | slug `proverka-demo` |
| Project | `SEO-продвижение ПРОВЕРКА.рa` | slug `proverka-demo` |
| Site label | `ПРОВЕРКА.рa` | URL `https://proverka.example` |
| Primary site | yes (`is_primary=1`) | — |

### Mixed-script warning (operator literal)

String `ПРОВЕРКА.рa` contains:

| Part | Script |
|------|--------|
| `ПРОВЕРКА` | Cyrillic |
| `.` | punctuation |
| `р` | **Cyrillic** U+0440 |
| `a` | **Latin** U+0061 |

**Rules:** preserve display literal exactly; never “fix” to all-Cyrillic or all-Latin in UI seed data; use ASCII `proverka-demo` for slug/matching/cleanup.

Put marker in `clients.notes` and/or period/monthly `internal_notes` / titles where safe for grepping — **not** in client-facing titles as junk. Prefer notes + evidence JSON.

---

## 2. Narrative

SEO specialist **Тест Проверочнов** ведёт проект **второй месяц**.

| Month | Calendar | Story |
|-------|----------|-------|
| 1 | July 2026 (01–31) | Full completed monthly report |
| 2 | August 2026 (01–31) | In progress as of **2026-08-21** |

Project type: `service_corporate`.

Owner: demo user (`seo_specialist`).  
Reviewer: optional Local Admin; may be null for specialist-led demo.

---

## 3. Reporting periods — recommended statuses

| Month | `period_key` | Dates | Recommended `status` | Title (suggested) |
|-------|--------------|-------|----------------------|-------------------|
| July | `2026-07` | 2026-07-01 … 2026-07-31 | **`finalized`** | `Июль 2026 — ПРОВЕРКА.рa` |
| August | `2026-08` | 2026-08-01 … 2026-08-31 | **`active`** | `Август 2026 — ПРОВЕРКА.рa` |

Allowed period statuses (schema CHECK): `draft`, `active`, `weekly_review`, `monthly_review`, `finalized`, `archived`.  
There is **no** `closed` value — use `finalized` for closed month.

Create under **new** `project_id` only (not Demo Client project 1).

Optional: light W1–W4 `weekly_checkpoints` for July (complete) and August (W1–W3 filled, W4 open) — Implementation may seed shells; browser fill may enrich.

---

## 4. Monthly reports — recommended statuses

| Month | Recommended status | `finalized_at` | Snapshot / export / share |
|-------|--------------------|----------------|---------------------------|
| July | **`finalized`** via **seed direct status** (preferred for “closed month” training) | Set to `2026-08-01 10:00:00` (or similar post-month) | **None** |
| August | **`in_progress`** | null | **None** |

Allowed monthly statuses: `draft`, `in_progress`, `ready_for_review`, `reviewed`, `finalized`, `archived`.

### Finalization / artifact decision (hard)

| Approach | Verdict |
|----------|---------|
| Call UI finalize as `seo_specialist` | **Impossible** — finalize roles are lead/admin only |
| Seed status `finalized` + `finalized_at` **without** creating `report_snapshots` / `report_exports` / shares | **Recommended** — complete month story; no PDF/export/share side effects |
| Seed as `reviewed` only | Acceptable fallback if operator wants finalize strictly via admin UI later |
| Seed snapshot for July | **Out of scope** for Seed Implementation 01 unless operator explicitly expands charter |
| Seed export/PDF/share | **Forbidden** |

`ReportFinalizationService` does not auto-create exports/shares. Snapshot is a separate service — seed must **not** invoke it.

July content must still be full (texts + blocks + work entries) so client preview is credible even without snapshot.

August must remain editable (`in_progress`) for browser fill.

---

## 5. Titles (no LOCAL_FIXTURE_ONLY)

| Month | Monthly title |
|-------|---------------|
| July | `Ежемесячный отчёт SEO — июль 2026 — ПРОВЕРКА.рa` |
| August | `Ежемесячный отчёт SEO — август 2026 — ПРОВЕРКА.рa` |

Marker belongs in `internal_notes` / client notes / evidence — not as a fixture junk prefix in client titles.

---

## 6. Report blocks (seed shells)

Seed at least the six primary shells for **both** months (July filled; August partial):

| `block_key` | `block_type` | July status | August status |
|-------------|--------------|-------------|---------------|
| `executive_summary` | `executive_summary` | `approved` or `reviewed` | `in_progress` |
| `work_completed` | `work_completed` | `approved`/`reviewed` | `in_progress` |
| `results_summary` | `results_summary` | `approved`/`reviewed` | `draft`/`in_progress` |
| `key_findings` | `key_findings` | `approved`/`reviewed` | `in_progress` |
| `risks_and_blockers` | `risks_and_blockers` | `reviewed` | `in_progress` |
| `next_month_plan` | `next_month_plan` | `approved`/`reviewed` | `draft` |

Optional July: one `metric_snapshot` block with `"demo": true` in `data_json`.

---

## 7. Work entries volume

| Month | Minimum entries | Mix |
|-------|-----------------|-----|
| July | **10–14** | mostly `done` / `period_role=done`; 1–2 `risk`/`note` |
| August | **8–12** | mix `done` / `in_progress` / `planned` + ≥1 `risk` |

Visibility: mostly `client_facing` or `client_safe`; a few `internal`.

Link to catalogue `seo_work_items` where natural; manual titles allowed.

---

## 8. Metrics policy

- **No** dedicated metrics tables in current schema.
- Invented numbers live in monthly text fields, block bodies, and optional `metric_snapshot` / `source_metric_refs`.
- Always label as demo fiction in internal notes / content pack.
- Do not invent Topvisor account IDs or real credentials.

---

## 9. Isolation from Demo Client

| Must not change | IDs |
|-----------------|-----|
| Demo Client / project / site | 1 / 1 / 1 |
| Monthly reports | **1**, **5** |
| Snapshot / exports / shares | existing rows only |

Cleanup must be marker/ID exact — never cascade into Demo Client.

---

## 10. Hybrid boundary

| Seed Implementation 01 | Browser Fill Pass 01 |
|------------------------|----------------------|
| User, client, project, site | Login as test user |
| Two periods + two monthlies | Edit/enrich work entries |
| Core blocks + baseline texts | Edit blocks / monthly fields |
| Baseline work entries (enough to demo) | Adjust statuses / add missing |
| No export/share/PDF | Preview July + August |
| Evidence IDs JSON | Screenshots + UI issue log |

Do **not** combine browser fill into Seed Implementation 01 unless a later operator charter explicitly merges them.
