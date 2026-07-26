# I-SEO Report Hub — DB-06 Report Blocks Validation Plan v0.1

**Status:** VALIDATION PLAN for next apply wave — no execution in this charter  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Report Blocks DB-06 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-06-REPORT-BLOCKS-SCHEMA-PLAN-v0.1.md)

---

## 1. Preflight

Before apply-wave mutation:

1. Repo root `X:\AI MARS`; drive `X:`; volume `AI WS`.
2. Branch `mars/canonical-post-recovery`.
3. Staged index empty (prefer empty at start).
4. i-SEO unexpected WIP absent.
5. Foreign WIP preserved.
6. DB host exactly `127.0.0.1`; DB name exactly `iseo_report_hub_dev`.
7. Baseline counts: migrations **4**, tables **12**, monthly_report_contents **≥ 1** for demo smoke context, weekly_checkpoints **≥ 1**.
8. Confirm `report_blocks` absent before apply.

---

## 2. Migration apply validation

| Gate | Expected |
|------|----------|
| `db-migrate.php status` | Pending `_000005` before apply |
| `db-migrate.php apply` | Success |
| Ledger | Row for `_000005` present with checksum |
| Migration count | **4 → 5** |
| Table count | **12 → 13** |
| Table exists | `report_blocks` |

---

## 3. Idempotency

1. Re-run `db-migrate.php apply`.
2. Expect no-op / already-applied behavior.
3. No duplicate ledger rows.
4. No schema drift.

---

## 4. Table / columns validation

Confirm columns present (names + nullability/defaults align with schema plan):

- Identity / parent / `block_key` / `block_type` / `sort_order` / status / title
- `body` / `summary`
- `data_json` / `source_weekly_checkpoint_ids` / `source_metric_refs`
- `owner_user_id` / `reviewer_user_id` / `created_by` / `updated_by`
- `reviewed_at` / `approved_at` / `created_at` / `updated_at`

Confirm engine/charset: InnoDB / utf8mb4 (match project convention).

Confirm unique index on `(monthly_report_content_id, block_key)`.

Confirm non-unique index on `(monthly_report_content_id, sort_order)`.

---

## 5. FK validation

| FK | Expect |
|----|--------|
| `monthly_report_content_id` → `monthly_report_contents.id` | Present; ON DELETE RESTRICT |
| user FKs → `users.id` | Present; ON DELETE SET NULL |
| Insert with fake monthly id | Rejected |
| Delete monthly content with child blocks | Rejected (RESTRICT) while children exist |

No FK expected from JSON weekly/metric fields.

---

## 6. Unique validation

| Case | Expect |
|------|--------|
| Duplicate `(monthly_report_content_id, block_key)` | Rejected |
| Same `block_key` under different monthly parents | Allowed |
| Duplicate `sort_order` under same parent | Allowed (MVP) |

---

## 7. CHECK validation

| Case | Expect |
|------|--------|
| Invalid status string | Rejected |
| Valid statuses (`draft`, `in_progress`, `ready_for_review`, `reviewed`, `approved`, `archived`) | Accepted |
| Invalid `block_type` | Rejected if DB CHECK present |
| Valid allowlisted `block_type` | Accepted |

Transition graph remains app/service policy (not DB CHECK).

---

## 8. JSON validation (if supported)

| Case | Expect |
|------|--------|
| Valid JSON array of weekly ids | Accepted |
| Valid JSON for `data_json` / `source_metric_refs` | Accepted |
| Non-JSON text in JSON column | Rejected by MySQL JSON type |
| Optional extra JSON CHECK | Prefer omit; document if present |
| Same-period membership of weekly ids | App/service later; optional smoke note only |

---

## 9. Fixture block smoke rows

Recommended fixture blocks for future apply (charter wave **must not** insert):

| Field | Value |
|-------|-------|
| Parent | monthly_report_content for `period_key = 2026-07` resolved dynamically |
| Block keys | `executive_summary`, `work_completed`, `results_summary`, `key_findings`, `next_month_plan` |
| Block types | Same as keys |
| Status | `draft` |
| sort_order | 10 / 20 / 30 / 40 / 50 |
| title / body / summary / JSON markers | `LOCAL_FIXTURE_ONLY` |
| source weekly ids | Resolved dynamically by checkpoint_key W1/W2/W3/W4 |
| owner / created_by / updated_by | Local admin id if safely resolvable |

Rules:

- No real client data.
- Optional: leave fixture blocks in place after apply for later CRUD/editor wave, or clean per apply charter.

---

## 10. Parent / monthly / weekly regression

| Check | Expect |
|-------|--------|
| `/health` | Still usable / 200; safe DB status; no secrets |
| Reporting Period CRUD routes | Still work |
| Weekly Checkpoints CRUD routes | Still work |
| Monthly Report Content CRUD routes | Still work |
| Users / roles / clients / projects / sites counts | Unchanged by migration DDL |
| Reporting periods / weekly checkpoints / monthly_report_contents rows | Unchanged by migration DDL (fixture block inserts are separate smoke step; parent monthly row content unchanged) |

---

## 11. No production / real data

| Forbidden | Rule |
|-----------|------|
| Production DB | Never |
| Real client block content | Never |
| Credential printing | Never |
| Broad wipe / truncate | Never without destructive charter |

---

## 12. STOP conditions

Stop and report if:

- Preflight fails
- Wrong DB target
- Migration apply fails or checksum conflict unexplained
- Unique/FK/CHECK gates fail
- Fixture smoke would require real client rows
- Apply wave starts editing report block CRUD UI without charter

Token:

`STOP — I-SEO REPORT BLOCKS DB-06 VALIDATION FAILED`

---

## 13. Charter-wave validation (this wave)

| Gate | Result required |
|------|-----------------|
| Docs-only writes | Pass |
| No SQL file created | Pass |
| No DB mutation | Pass |
| No app-source/runtime edits | Pass |
| Scoped docs commit | Pass |
| Push | Not performed |
