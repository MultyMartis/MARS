# I-SEO Report Hub — Report Export / PDF Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export / PDF Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый product/design слой export / PDF** после Report Snapshot Implementation.

Цель charter:

1. Определить export model: артефакт строится из **`report_snapshots`**, не из live monthly/report_blocks.
2. Выбрать MVP-формат: **HTML export artifact** первым; **PDF отложен**.
3. Зафиксировать storage path policy вне public webroot и вне Git.
4. Зафиксировать filename / export_key / checksum / access / audit политики.
5. Рекомендовать DB-backed metadata table `report_exports` (DB-08) до HTML export implementation.
6. Подготовить design / storage / implementation / validation plans для следующих волн.
7. Не менять app-source / runtime / DB / не создавать файлы или PDF в этой волне.

Эта волна — **documentation / policy only**. Export и PDF **не** кодируются здесь.

---

## 2. Current Baseline

### Report Snapshot Implementation

| Item | Value |
|------|-------|
| Primary commit | `7d19979183947a25510915a7d36da9655c370673` — `feat(iseo-report-hub): add report snapshot workflow` |
| Hash-record | `040586fe96db91868704ed448402f640f438cb02` |
| Clarify | `c6b5d84161a751c594444a93510b159eb4c73a17` |
| Closeout-hashes | `7c3dbf1cabb119f645bfa94553087bfe40d412ea` |
| Smoke | **64/64 PASS** |
| Push | **no** |

### DB-07 Report Snapshots Migration Apply

| Item | Value |
|------|-------|
| Primary commit | `eb1d0ce544f42876a99ea4393a98ffa780bb6f1f` |
| Hash-record | `e290a29cb2d8d90994b47de371b3dbf763277de0` |
| Clarify | `a9b3c8e899d54cf56d34fab2bbd237fd99823feb` |
| Migration | `2026_07_27_000006_create_report_snapshots_table.sql` |
| SQL checksum | `8f1890f6595f5f9fedb3f1366a5207fad9eca55f94dbcc549406313d192c6ab0` |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **6** |
| Tables | **14** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** (`finalized`, `finalized_at` non-null) |
| report_blocks | **6** (all `reviewed`) |
| report_snapshots | **1** |

### Active snapshot v1

| Field | Value |
|-------|-------|
| id | **1** |
| snapshot_key | `monthly-1-v1` |
| version | **1** |
| status | `active` |
| render_mode | `blocks_primary` |
| checksum_sha256 | `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` |
| rendered_text | present |
| rendered_html | null |
| source weekly | `[1,2,3,7]` |
| source blocks | **6** |

### Already present (product surface)

- Auth persistence + local admin bootstrap
- Reporting Period / Weekly Checkpoints / Monthly Report Content / Report Blocks CRUD
- Internal monthly preview/render + browser print route
- Finalization workflow + locks
- Snapshot table + snapshot workflow + active snapshot v1

### Current limitation

- no export model;
- no PDF generation;
- no export file storage;
- no exported artifact metadata table;
- no export routes;
- no public/share/client portal;
- no file cleanup/archive policy for exports.

---

## 3. Problem

Система умеет создать **immutable snapshot** finalized monthly report (payload + checksum + version).

Но нет **downloadable/exportable artifact**:

- нет stored HTML/PDF файла, привязанного к snapshot;
- нет metadata lifecycle для exports;
- print route работает с **live** preview composition, не с frozen snapshot artifact;
- нет безопасного storage вне public webroot;
- нет auth download stream для артефакта;
- нет основания для будущего PDF без повторного решения storage/auth/idempotency.

Нужен internal export слой как next product/design step после snapshot.

---

## 4. Scope

### In scope

- internal export policy;
- snapshot as export source of truth;
- HTML export recommendation as first MVP artifact;
- PDF deferral (engine choice later);
- storage path policy;
- filename / export_key policy;
- future metadata table `report_exports` (DB-08);
- access / audit model;
- validation / smoke plan for later waves.

### Out of scope

- public share / token URLs;
- client portal;
- email delivery / scheduled sends;
- production deployment;
- actual PDF generation in this or the first HTML export wave;
- object storage / S3 / Drive;
- digital signatures / watermarking;
- app-source / runtime / DB changes in this charter wave.

---

## 5. Product Rules

1. **Export source of truth = `report_snapshots`.** Live `monthly_report_contents` / `report_blocks` не используются как content source для artifact (кроме permission/context если нужно).
2. **Internal-only for MVP.** `client_viewer` — no access. No public routes. No tokens.
3. **HTML artifact first.** Server-generated `.html` stored outside public docroot; served via authenticated route.
4. **PDF deferred.** No PDF engine in first export implementation unless operator explicitly approves a separate PDF engine charter.
5. **Artifacts never in Git.** Runtime storage only under Localhost `storage/exports/…`.
6. **No public webroot writes** for exports (`public/exports` forbidden).
7. **Deterministic safe filenames** from snapshot key + format (no Cyrillic, no client names, no raw titles).
8. **Checksum chain:** copy snapshot checksum into export metadata; separate file checksum for artifact bytes.
9. **Idempotent create** for same snapshot checksum + format when artifact exists.
10. **DB-backed metadata recommended** (`report_exports`) before / with first HTML export implementation.

---

## 6. Recommended MVP Sequence

| Order | Wave | Purpose |
|-------|------|---------|
| 1 | **This charter** | Policy / design / storage / validation — docs only |
| 2 | **Report Export DB-08 Migration Apply 01** | Create `report_exports` table (schema only) |
| 3 | **Report Export HTML Artifact Implementation 01** | Generate HTML from snapshot; store; auth download |
| 4 | **PDF Engine Charter** (later) | Choose engine for Windows/Laragon |
| 5 | **PDF Export Implementation** (later) | Only after HTML storage/auth lifecycle proven |

Do **not** jump to PDF generation before HTML export proves storage, auth serving, metadata, and idempotency.

---

## 7. Safety Boundary

| Boundary | Rule |
|----------|------|
| Git | No export files committed; no secrets |
| Public docroot | No direct filesystem URLs; no writes under `public/` |
| Source of truth | Snapshot payload only |
| Roles | Internal roles only; `client_viewer` denied |
| DB this wave | No mutation |
| App-source / runtime this wave | No edits; no sync |
| PDF | Not generated in charter or first HTML wave |
| Production | Out of scope |

STOP if next waves attempt: public share, client portal, email, Git storage of artifacts, or PDF without engine charter.

---

## 8. Next Implementation Wave

**One next action only:**

**I-SEO Report Hub — Report Export DB-08 Migration Apply 01**

Rationale: snapshots already use DB-backed lifecycle; export artifacts should have metadata (`report_exports`) before HTML generation so lifecycle, idempotency, and audit have a durable row identity.

After DB-08: **Report Export HTML Artifact Implementation 01**.

PDF remains deferred.
