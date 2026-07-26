# I-SEO Report Hub — DB-05 Monthly Report Content Validation Plan v0.1

**Status:** VALIDATION PLAN for next apply wave — no execution in this charter  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content DB-05 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md)

---

## 1. Preflight

Before apply-wave mutation:

1. Repo root `X:\AI MARS`; drive `X:`; volume `AI WS`.
2. Branch `mars/canonical-post-recovery`.
3. Staged index empty (or only apply-allowlisted paths if charter stages mid-wave carefully — prefer empty at start).
4. i-SEO unexpected WIP absent.
5. Foreign WIP preserved.
6. DB host exactly `127.0.0.1`; DB name exactly `iseo_report_hub_dev`.
7. Baseline counts: migrations **3**, tables **11**, reporting_periods **≥ 1**, weekly_checkpoints **≥ 1** for demo smoke context.
8. Confirm `monthly_report_contents` absent before apply.

---

## 2. Migration apply validation

| Gate | Expected |
|------|----------|
| `db-migrate.php status` | Pending `_000004` before apply |
| `db-migrate.php apply` | Success |
| Ledger | Row for `_000004` present with checksum |
| Migration count | **3 → 4** |
| Table count | **11 → 12** |
| Table exists | `monthly_report_contents` |

---

## 3. Idempotency

1. Re-run `db-migrate.php apply`.
2. Expect no-op / already-applied behavior.
3. No duplicate ledger rows.
4. No schema drift.

---

## 4. Table / columns validation

Confirm columns present (names + nullability/defaults align with schema plan):

- Identity / parent / status / title
- `executive_summary` / `work_completed` / `results_summary` / `key_findings`
- `risks_and_blockers` / `next_month_plan` / `client_notes` / `internal_notes`
- `source_weekly_checkpoint_ids`
- `owner_user_id` / `reviewer_user_id` / `created_by` / `updated_by`
- `reviewed_at` / `finalized_at` / `created_at` / `updated_at`

Confirm engine/charset: InnoDB / utf8mb4 (match project convention).

Confirm unique index on `reporting_period_id`.

---

## 5. FK validation

| FK | Expect |
|----|--------|
| `reporting_period_id` → `reporting_periods.id` | Present; ON DELETE RESTRICT |
| user FKs → `users.id` | Present; ON DELETE SET NULL |
| Insert with fake period id | Rejected |
| Delete period with child monthly content | Rejected (RESTRICT) while child exists |

No FK expected from JSON weekly ids to `weekly_checkpoints`.

---

## 6. Unique validation

| Case | Expect |
|------|--------|
| Duplicate `reporting_period_id` | Rejected |
| Second monthly row for same period | Rejected |
| Monthly rows under different periods | Allowed |

---

## 7. CHECK validation

| Case | Expect |
|------|--------|
| Invalid status string | Rejected |
| Valid statuses (`draft`, `in_progress`, `ready_for_review`, `reviewed`, `finalized`, `archived`) | Accepted |

Transition graph remains app/service policy (not DB CHECK).

---

## 8. JSON validation (if supported)

| Case | Expect |
|------|--------|
| Valid JSON array of ids | Accepted |
| Non-JSON text in JSON column | Rejected by MySQL JSON type |
| Optional JSON CHECK (if present) | Documented PASS/FAIL in apply result |
| Same-period membership of ids | App/service later; optional smoke note only |

If optional JSON CHECK is omitted for portability, rely on JSON type + app validation and record that decision in apply result.

---

## 9. Demo smoke row

Recommended demo row for future apply (charter wave **must not** insert):

| Field | Value |
|-------|-------|
| Parent | reporting period `period_key = 2026-07` resolved dynamically |
| `status` | `draft` |
| `title` | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| Content TEXT fields | Each contains `LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | JSON array of ids for `2026-07-W1` / `W2` / `W3` / `W4` if present, resolved by `checkpoint_key` |
| Owner / created_by / updated_by | Local admin id if safely resolvable |

Rules:

- No real client data.
- Optional: leave demo row in place after apply for later CRUD wave, or clean per apply charter.

---

## 10. Health / app regression

| Check | Expect |
|-------|--------|
| `/health` | Still usable / 200; safe DB status; no secrets |
| Reporting Period CRUD routes | Still work |
| Weekly Checkpoints CRUD routes | Still work |
| Auth login/session | Intact |
| Users / roles / clients / projects / sites counts | Unchanged by migration DDL |
| Reporting periods / weekly checkpoints rows | Unchanged by migration DDL (demo monthly insert is separate smoke step) |

---

## 11. No production / real data

| Forbidden | Rule |
|-----------|------|
| Production DB | Never |
| Real client monthly content | Never |
| Credential printing | Never |
| Broad wipe / truncate | Never without destructive charter |

---

## 12. STOP conditions

Stop and report if:

- Preflight fails
- Wrong DB target
- Migration apply fails or checksum conflict unexplained
- Unique/FK/CHECK gates fail
- Demo smoke would require real client rows
- Apply wave starts editing monthly CRUD UI without charter

Token:

`STOP — I-SEO MONTHLY REPORT CONTENT DB-05 VALIDATION FAILED`

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
