# I-SEO Report Hub — Work Entry Editor Safety Policy v0.1

**Status:** CHARTER / SAFETY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Work Entry Editor Charter 01

Applies to **Work Entry Editor Implementation 01**. This charter wave itself performs **no** DB mutation.

---

## 1. Environment

| Item | Rule |
|------|------|
| DB | Local `iseo_report_hub_dev` @ `127.0.0.1:3306` only |
| Production | **Forbidden** |
| WordPress / i-seo.su / WPilot | **Forbidden** |
| Runtime public share | Do not create, revoke, or alter tokens |
| PDF / export artifacts | Do not regenerate or rewrite files |
| `.env` / `.env.local` | Do not edit |

---

## 2. Allowed mutations (implementation wave only)

| Target | Allowed? |
|--------|----------|
| `monthly_report_work_entries` INSERT | Yes (smoke test row) |
| `monthly_report_work_entries` UPDATE | Yes (that test row; not a mass edit of the 7 fixtures) |
| `monthly_report_work_entries` DELETE via **app route** | **No** (no route) |
| SQL DELETE of **one** documented test row after smoke | Yes, **Option D only**, by exact id + title match |
| Restore `monthly_report_work_entries` from table dump | Yes, rollback path |
| Full DB restore from backup | Only if smoke damaged other tables |
| `seo_work_categories` / `seo_work_items` | **No** |
| `monthly_report_contents` (incl. reopen/finalize) | **No** |
| `report_blocks` | **No** |
| `report_snapshots` / `report_exports` / `report_export_shares` | **No** |
| `schema_migrations` | **No** |
| sessions / audit tables | Incidental login/session rows from HTTP smoke are tolerated; do not hand-edit |

---

## 3. Backup (mandatory before first POST)

Path:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\work-entry-editor-implementation-01\backup\`

Minimum:

1. Full `mysqldump --single-transaction` of `iseo_report_hub_dev`.  
2. Table-only dump of `monthly_report_work_entries`.  
3. Record SHA256 + byte size in the implementation report.  
4. **Do not** commit dumps to git.

If dump fails → **STOP**. Do not POST.

---

## 4. Validation mutation strategy

### Options

| Option | What happens | Final entries_r1 | Risk |
|--------|----------------|------------------|------|
| **A** | Create test entry; set `deferred` + `internal`; **keep** it | 8 | Clutters fixture UI / future assembly |
| **B** | POST smoke then **full DB restore** | 7 | Restores shares/sessions too; broader than needed |
| **C** | Implement GET-only; skip POST smoke | 7 | Editor writes unproven |
| **D** (recommended) | Backup; POST create+update; **SQL DELETE only the test row**; verify 7 | 7 | Narrow; needs exact-id discipline |

### Recommendation

**Option D** is the default for Implementation 01.

Rationale:

- POST must be proven (reject C).  
- Keeping a `MARS TEST` row (A) pollutes the 7-entry fixture the operator already reviewed.  
- Full restore (B) is a valid emergency rollback but is wider than a one-row cleanup.  
- App still has **no DELETE route**; cleanup is a **chartered operator/agent SQL** against the local DB after smoke, not a product feature.

### Option D procedure

1. Record before: `entries_r1 = 7`.  
2. Create title exactly: `MARS TEST — редактор работ`.  
3. Edit to `status=deferred`, `client_visibility=internal`.  
4. Capture new `id`.  
5. `DELETE FROM monthly_report_work_entries WHERE id = :id AND title = 'MARS TEST — редактор работ' AND monthly_report_id = 1 LIMIT 1;`  
6. Verify count 7; fixtures unchanged; shares/exports/PDF prefix unchanged.  
7. If DELETE matches 0 rows → STOP and restore table dump (do not widen the DELETE).

### Operator override

The implementation prompt must state Option D as default and allow the operator to switch to:

- **A** — keep the internal/deferred test row (document count 8), or  
- **B** — full restore if they want a guaranteed pristine DB without SQL DELETE.

If the operator has not answered, Implementation 01 follows **D**.

---

## 5. Fixture / seed protection

- Do not UPDATE the original 7 rows in smoke.  
- Do not re-run `tools/seed-nikita-catalogue.php` unless a separate charter says so.  
- Do not DROP catalogue tables.

---

## 6. Share / export / PDF freeze

Before and after smoke, assert:

| Check | Expected |
|-------|----------|
| `report_exports` count | 4 |
| export id 4 checksum prefix | `a8c4d61c6216e8d70b19` |
| `report_export_shares` count | 7 |
| active shares | 1 (likely id 7 / `test-first-link`) |
| revoked | 6 |
| PDF files on disk | unchanged (no regen) |

Any drift → STOP; do not “fix” shares.

---

## 7. Rollback

| Situation | Action |
|-----------|--------|
| Test row leftover after failed DELETE | Table-dump restore of `monthly_report_work_entries` |
| Accidental fixture UPDATE | Table-dump restore |
| Damage outside work_entries | Full backup restore (local only; operator-visible) |
| Bad code | git revert of exact implementation commit; runtime re-sync from source |

This charter wave has nothing to roll back.

---

## 8. Secrets

Do not print DB passwords, password hashes, share tokens, or `.env` values in docs or smoke logs. Refer to share id / prefix only.

---

## 9. This charter wave

No backup required now (no mutation). Implementation 01 must not skip backup because this docs wave was clean.
