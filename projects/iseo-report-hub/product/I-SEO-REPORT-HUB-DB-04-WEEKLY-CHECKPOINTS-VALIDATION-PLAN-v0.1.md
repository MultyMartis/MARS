# I-SEO Report Hub — DB-04 Weekly Checkpoints Validation Plan v0.1

**Status:** VALIDATION PLAN for next apply wave — no execution in this charter  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints DB-04 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md)

---

## 1. Preflight

Before apply-wave mutation:

1. Repo root `X:\AI MARS`; drive `X:`; volume `AI WS`.
2. Branch `mars/canonical-post-recovery`.
3. Staged index empty (or only apply-allowlisted paths if charter stages mid-wave carefully — prefer empty at start).
4. i-SEO unexpected WIP absent.
5. Foreign WIP preserved.
6. DB host exactly `127.0.0.1`; DB name exactly `iseo_report_hub_dev`.
7. Baseline counts: migrations **2**, tables **10**, reporting_periods **≥ 1** for demo smoke.
8. Confirm `weekly_checkpoints` absent before apply.

---

## 2. Migration apply validation

| Gate | Expected |
|------|----------|
| `db-migrate.php status` | Pending `_000003` before apply |
| `db-migrate.php apply` | Success |
| Ledger | Row for `_000003` present with checksum |
| Migration count | **2 → 3** |
| Table count | **10 → 11** |
| Table exists | `weekly_checkpoints` |

---

## 3. Idempotency

1. Re-run `db-migrate.php apply`.
2. Expect no-op / already-applied behavior.
3. No duplicate ledger rows.
4. No schema drift.

---

## 4. Table / columns validation

Confirm columns present (names + nullability/defaults align with schema plan):

- Identity / parent / week_index / checkpoint_key
- checkpoint_start / checkpoint_end / status / title
- summary / work_done / findings / next_steps / risks
- owner_user_id / reviewer_user_id / created_by / updated_by
- reviewed_at / completed_at / created_at / updated_at

Confirm engine/charset: InnoDB / utf8mb4 (match project convention).

---

## 5. FK validation

| FK | Expect |
|----|--------|
| `reporting_period_id` → `reporting_periods.id` | Present; ON DELETE RESTRICT |
| user FKs → `users.id` | Present; ON DELETE SET NULL |
| Insert with fake period id | Rejected |
| Delete period with child checkpoints | Rejected (RESTRICT) while children exist |

---

## 6. Unique validation

| Case | Expect |
|------|--------|
| Duplicate `(reporting_period_id, week_index)` | Rejected |
| Duplicate `(reporting_period_id, checkpoint_key)` | Rejected |
| Same checkpoint_key under different periods | Allowed |

---

## 7. CHECK validation

| Case | Expect |
|------|--------|
| `week_index` 0 or 7 | Rejected |
| `checkpoint_start` > `checkpoint_end` | Rejected |
| Invalid status string | Rejected |
| Valid statuses | Accepted |

Parent date containment remains **app/service** validation (document PASS/FAIL separately if tested in apply smoke).

---

## 8. Demo smoke rows

Recommended demo set for future apply (charter wave **must not** insert):

| Week | `checkpoint_key` | Status | Notes |
|------|------------------|--------|-------|
| W1 | `2026-07-W1` | `completed` | Date range = first week inside period; summary contains `LOCAL_FIXTURE_ONLY` |
| W2 | `2026-07-W2` | `reviewed` | Second week inside period |
| W3 | `2026-07-W3` | `draft` | Third week inside period |

Rules:

- Parent = reporting period `period_key = 2026-07` resolved dynamically.
- No real client data.
- Optional: leave demo rows in place after apply for later CRUD wave, or clean per apply charter.

---

## 9. Health / app regression

| Check | Expect |
|-------|--------|
| `/health` | Still usable / 200; safe DB status; no secrets |
| Reporting Period CRUD routes | Still work (list/detail for fixture + smoke periods) |
| Auth login/session | Intact |
| Users / roles / clients / projects / sites counts | Unchanged by migration DDL |
| Reporting periods rows | Unchanged by migration DDL (demo weekly inserts are separate smoke step) |

---

## 10. No production / real data

| Forbidden | Rule |
|-----------|------|
| Production DB | Never |
| Real client weekly content | Never |
| Credential printing | Never |
| Broad wipe / truncate | Never without destructive charter |

---

## 11. STOP conditions

Stop and report if:

- Preflight fails
- Wrong DB target
- Migration apply fails or checksum conflict unexplained
- Unique/FK/CHECK gates fail
- Demo smoke would require real client rows
- Apply wave starts editing app CRUD without charter

Token:

`STOP — I-SEO WEEKLY CHECKPOINTS DB-04 VALIDATION FAILED`

---

## 12. Charter-wave validation (this wave)

| Gate | Result required |
|------|-----------------|
| Docs-only writes | Pass |
| No SQL file created | Pass |
| No DB mutation | Pass |
| No app-source/runtime edits | Pass |
| Scoped docs commit | Pass |
| Push | Not performed |
