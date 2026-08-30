# I-SEO Report Hub — Summary Assembly Safe Fixture Safety Policy v0.1

**Status:** CHARTER / SAFETY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Safe Fixture Charter 01

Binding for **Summary Assembly Safe Fixture Implementation 01**. This charter wave itself performs **no** writes.

---

## 1. Environment

| Item | Rule |
|------|------|
| DB | Local `iseo_report_hub_dev` @ `127.0.0.1:3306` only |
| `APP_ENV` | `local` |
| Production | **Forbidden** |
| WordPress / i-seo.su / WPilot | **Forbidden** |
| `.env` / `.env.local` | Do not edit |
| Report id 1 | **No mutation**, no reopen |
| Report id 5 | **No mutation** |

---

## 2. Backup

Mandatory full dump **before fixture create**. If dump fails → STOP.

Keep dump in STORAGE incoming. Do not commit. Do not delete the dump if cleanup fails.

---

## 3. Fixture marker

Every fixture-owned row must carry `MARS_FIXTURE_SUMMARY_APPLY_YYYYMMDD_HHMMSS`.  
Cleanup without marker verification is **forbidden**.

---

## 4. Forbidden mutations

| Target | Rule |
|--------|------|
| Report 1 blocks / entries / monthly / finalize / reopen | **No** |
| Report 5 | **No** |
| `report_snapshots` / `report_exports` / `report_export_shares` | **No insert/update/delete** |
| PDF artifacts / export storage | **No** |
| Catalogue tables | **No** (reuse only) |
| Demo client/project/site 1 | **No delete**; no required update |
| Shared existing period `2026-07` / `2026-08` | **No** |
| `schema_migrations` | **No** |
| Users / password hashes | **No** |
| DELETE outside fixture ids in JSON | **No** |
| Broad `WHERE title LIKE` / date-range cleanup | **No** |

Allowed in Implementation 01 after gates:

- INSERT fixture period + monthly + 6 blocks + 7 entries
- POST apply UPDATE of fixture `next_month_plan` only (via app)
- DELETE those fixture ids on cleanup
- `audit_log` inserts from app/tool

---

## 5. Publication chain

Apply must not create snapshots, exports, shares, or PDFs.  
If any appear on the fixture monthly: **STOP** before cleanup deletes them; operator inspects.

Report 1 share `test-first-link` / export 4 checksum prefix are regression locks.

---

## 6. Cleanup failure

If cleanup cannot verify marker or counts:

1. STOP.  
2. Keep backup.  
3. Keep remaining fixture rows.  
4. Report exact ids from JSON vs live.  
5. Do not run a second guessed DELETE.  
6. Do not restore production-style `git reset --hard` / `git clean`.

---

## 7. Acceptable residual state

| Residual | Acceptable? |
|----------|-------------|
| Zero fixture period/monthly/blocks/entries | **Required** |
| `audit_log` extra rows (create/apply) | **Yes** — document count delta; do not prune |
| AUTO_INCREMENT gaps | **Yes** |
| STORAGE dump + evidence JSON | **Yes** (not git) |
| Standing fixture monthly after impl | **No** for Implementation 01 |
| Changed report 1 / 5 / exports / shares | **No** |

If a later operator wants a standing lab report, that is a **separate** charter.

---

## 8. Existing safe target discovered later

If Implementation 01 finds a **new** non-finalized monthly with 6 blocks + entries and no exports/shares (not id 1, not id 5):

**Still prefer the dedicated marked fixture.**  
Ad-hoc reuse is less repeatable and cleanup is ambiguous. Discovery may be logged as SAFE UNKNOWN, then ignored for the write path.

---

## 9. Git

Exact-path commits. No `git add .`. No push unless the operator asks. Foreign WIP preserved. Evidence/backups not staged.

---

## 10. Secrets

No passwords, hashes, raw tokens, or `.env` in git docs. Login email `polygon-ws@mail.ru` may be named. Checksum **prefix** only.

---

## 11. SAFE UNKNOWN

- Whether `audit_log.entity_id` after block DELETE becomes an orphan pointer (expected; no FK on entity_id).  
- Operator appetite for a later prune-audit-log charter (not this wave).
