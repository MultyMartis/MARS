# I-SEO Report Hub — Report Export / PDF Implementation Plan v0.1

**Status:** PLANNING ONLY — no SQL created; no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export / PDF Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md)

---

## 1. Recommended next wave

**I-SEO Report Hub — Report Export DB-08 Migration Apply 01**

Purpose: create empty `report_exports` table in `iseo_report_hub_dev` @ `127.0.0.1` only; register schema migration; **no** export rows; **no** HTML/PDF generation; **no** routes.

---

## 2. Why DB-08 first

- Snapshots already established DB-backed lifecycle + checksum + audit pattern.
- Export artifacts need durable identity for list/detail/download/idempotency.
- Filesystem-only exports weaken audit and make orphan/missing-file detection harder.
- Schema can land before code (same pattern as DB-07 → Snapshot Implementation).

Alternative “HTML without metadata table” is allowed only if operator explicitly overrides; **not recommended**.

---

## 3. Suggested `report_exports` schema (DB-08) — design only

**Do not create SQL in this charter wave.**

Table: `report_exports`

| Column | Type | Notes |
|--------|------|-------|
| `id` | BIGINT UNSIGNED AUTO_INCREMENT PK | |
| `report_snapshot_id` | BIGINT UNSIGNED NOT NULL | FK → `report_snapshots(id)` ON DELETE RESTRICT |
| `monthly_report_content_id` | BIGINT UNSIGNED NOT NULL | FK → `monthly_report_contents(id)` ON DELETE RESTRICT |
| `export_key` | VARCHAR(128) NOT NULL | UNIQUE; e.g. `snapshot-1-html-v1` |
| `format` | VARCHAR(32) NOT NULL | CHECK: `html`, `pdf` |
| `status` | VARCHAR(32) NOT NULL DEFAULT `'ready'` | CHECK: `ready`, `failed`, `archived` |
| `storage_disk` | VARCHAR(32) NOT NULL DEFAULT `'local'` | |
| `storage_path` | VARCHAR(1024) NOT NULL | Relative under exports root |
| `filename` | VARCHAR(255) NOT NULL | e.g. `monthly-1-v1.html` |
| `mime_type` | VARCHAR(128) NOT NULL | e.g. `text/html; charset=UTF-8` |
| `file_size_bytes` | BIGINT UNSIGNED NULL | |
| `checksum_sha256` | CHAR(64) NULL | File bytes |
| `source_snapshot_checksum_sha256` | CHAR(64) NOT NULL | From snapshot |
| `created_by` | BIGINT UNSIGNED NULL | FK → `users(id)` ON DELETE SET NULL |
| `created_at` | DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP | |
| `archived_at` | DATETIME NULL | |

Indexes:

- UNIQUE (`export_key`)
- KEY (`report_snapshot_id`, `format`, `status`)
- KEY (`monthly_report_content_id`, `format`, `status`)

Suggested migration filename pattern (future apply wave):

`2026_07_27_000007_create_report_exports_table.sql` (exact name chosen in DB-08 apply).

---

## 4. Then: HTML export implementation (after DB-08)

**I-SEO Report Hub — Report Export HTML Artifact Implementation 01**

Planned work (not this wave):

1. Exact allowlist sync source → runtime if code changes.
2. `ReportExportService` / `ReportExportRepository` / controller / views.
3. Routes: list / POST html / detail / download.
4. Write HTML under `storage/exports/reports/…`.
5. Insert `report_exports` row; checksums; audit.
6. Smoke per Validation Plan.
7. No PDF; no public; no snapshot/monthly/block mutation.

---

## 5. PDF deferred after HTML export

Only after HTML proves storage + auth stream + metadata + idempotency:

1. PDF Engine Charter (binary/deps/fonts).
2. PDF Export Implementation (format `pdf` rows + generation).

Do not add PDF engine in HTML implementation unless operator explicitly approves.

---

## 6. Allowed DB actions — next waves

| Wave | Allowed |
|------|---------|
| DB-08 Apply | Create `report_exports` table; insert `schema_migrations` row; **no** business row changes except migration bookkeeping |
| HTML Implementation | Insert/update `report_exports` only; **no** mutate snapshots/monthly/blocks/periods/weekly |

Forbidden unless separate charter: DELETE hard; public publish tables; real client data imports.

---

## 7. Runtime sync policy

- Model A: change `app-source/` then exact allowlist sync → Localhost runtime.
- Do **not** sync export artifact files into Git.
- Ensure runtime `storage/exports` directory is creatable by PHP (permissions).
- No `.env` / `.env.local` secret changes unless separate charter requires a non-secret path config key.

---

## 8. Smoke list (future HTML wave — summary)

- Snapshot id 1 still active / checksum unchanged.
- POST HTML export creates `report_exports` + file outside public.
- Filename / export_key safe.
- File checksum matches metadata.
- Second POST idempotent.
- Auth detail/download OK; unauth denied.
- No public direct route; no PDF route.
- No mutation of snapshot/monthly/blocks/periods/weekly.

Full checks: [VALIDATION-PLAN](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md).

---

## 9. Commit policy

| Wave | Commit style |
|------|--------------|
| This charter | docs only: `docs(iseo-report-hub): add report export pdf charter` |
| DB-08 | migration SQL + docs; exact-path add; no push unless charter says |
| HTML impl | app-source + docs; exact-path; runtime sync separate evidence |

Never `git add .` / `-A` / `commit -a`. Preserve foreign WIP. No push by default.

---

## 10. STOP conditions

STOP if:

- attempt to generate PDF without engine charter;
- write exports under `public/` or into Git;
- mutate snapshot/monthly/block rows during export create;
- grant `client_viewer` export access;
- add public/token download;
- target wrong DB/host;
- staged foreign + iseo conflict without clean worktree;
- Composer/npm/package download without explicit approval.

Token: `STOP — I-SEO REPORT EXPORT / PDF SAFETY CONDITION FAILED`
