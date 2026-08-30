# I-SEO Report Hub — Report Export Template Metadata DB-09 Design v0.1

**Status:** DESIGN / POLICY ONLY — no schema apply; no migration file; no code  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export Template Metadata DB-09 Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-VALIDATION-PLAN-v0.1.md)
- Schema reference (read-only): `app-source/database/migrations/2026_07_27_000007_create_report_exports_table.sql`

---

## 1. Current schema context

`report_exports` (DB-08) currently stores artifact identity and storage metadata:

| Column | Notes |
|--------|-------|
| `id` | PK |
| `report_snapshot_id` | FK → `report_snapshots` RESTRICT |
| `monthly_report_content_id` | FK → `monthly_report_contents` RESTRICT |
| `export_key` | unique |
| `format` | CHECK `html` / `pdf` |
| `status` | CHECK `ready` / `failed` / `archived` |
| `storage_disk` / `storage_path` / `filename` / `mime_type` | storage identity |
| `file_size_bytes` / `checksum_sha256` | integrity |
| `source_snapshot_checksum_sha256` | snapshot binding |
| `created_by` / `created_at` / `archived_at` | audit |

**Missing:** template identity, template version, render target/engine/options, PDF→HTML lineage.

Existing local rows **1–4** must remain valid after ALTER (nullable new columns; no NOT NULL without default).

---

## 2. Options comparison

### Option A — Add nullable columns to `report_exports`

Candidate columns: `template_id`, `template_version`, `render_target`, `render_engine`, `render_options_json`, `source_html_export_id`, optional `metadata_json`.

| Pros | Cons |
|------|------|
| simplest query path | table grows |
| no join for UI | not a template registry |
| good MVP fit | limited normalization |
| easy repository SELECT | |

### Option B — Sidecar `report_export_render_metadata`

1:1 table keyed by `report_export_id`.

| Pros | Cons |
|------|------|
| keeps artifact table narrower | join required |
| easier to evolve metadata alone | more repository code |
| | more moving parts for MVP |

### Option C — `report_templates` registry

Registry of template keys/versions/config.

| Pros | Cons |
|------|------|
| future multi-template / branding ready | premature for current MVP |
| | needs admin/UI/assignment later |
| | does **not** alone solve per-export render metadata |

### Option D — Combined minimal

- DB-09: Option A columns now.
- Later DB-10/DB-11: registry + client assignment.

| Pros | Cons |
|------|------|
| matches current evidence (one template) | registry deferred (intentional) |
| unlocks durable UI without overbuilding | second schema wave later |

---

## 3. Recommended MVP decision

**Choose Option A (as Option D phased):**

1. DB-09 adds **nullable** render metadata columns to `report_exports`.
2. Defer `report_templates` registry.
3. Defer client assignment / branding tables.
4. Defer forced backfill repair UI.
5. Controlled local backfill for rows **3–4** only in Migration Apply wave (policy below; not executed in charter).

---

## 4. Recommended columns

| Column | Type | Null | Purpose |
|--------|------|------|---------|
| `template_id` | `VARCHAR(100)` | YES | e.g. `iseo_default_v1`; NULL = not recorded / legacy |
| `template_version` | `VARCHAR(50)` | YES | e.g. `1`; NULL with unknown template |
| `render_target` | `VARCHAR(50)` | YES | app vocabulary: `html_export`, `pdf_export`, … |
| `render_engine` | `VARCHAR(100)` | YES | e.g. `php_template_renderer`, `edge_headless_pdf` |
| `render_options_json` | `JSON` | YES | safe options only; no absolute paths; no secrets |
| `source_html_export_id` | `BIGINT UNSIGNED` | YES | PDF → HTML export lineage |
| `metadata_json` | `JSON` | YES | optional catch-all non-critical extras |

**Do not** use sentinel string `legacy_unrecorded` as stored `template_id` in MVP — prefer **NULL** = not recorded. UI maps NULL → “Template: not recorded / legacy”.

---

## 5. Indexes

| Index | Columns | Rationale |
|-------|---------|-----------|
| `idx_report_exports_template` | (`template_id`, `template_version`) | filter/list by template |
| `idx_report_exports_source_html` | (`source_html_export_id`) | lineage lookups / FK support |

Existing unique `export_key` and snapshot/monthly indexes remain.

---

## 6. FK policy — `source_html_export_id`

| Decision | Value |
|----------|-------|
| References | `report_exports(id)` (self-FK) |
| ON DELETE | **SET NULL** |
| Justification | Physical hard-delete of exports is not normal MVP behavior; if a source HTML row is ever removed/replaced, PDF rows should not fail migration/admin ops with RESTRICT deadlocks. SET NULL preserves PDF row and marks lineage unknown. Archive-by-status does not need FK action. |
| ON UPDATE | default / no cascade rewrite of ids |

Optional app rule (not DB CHECK): when `format = 'pdf'` and source known at create time, set `source_html_export_id`; when `format = 'html'`, column remains NULL.

---

## 7. Nullability and app-level constraints

### DB

- All new columns **nullable**.
- **No** strict CHECK on `template_id` yet (allows future ids without migration churn).
- **No** CHECK on `render_target` / `render_engine` in DB-09 — constrain in app first.
- JSON validity: native MySQL JSON type.

### App (future UI / create path)

Suggested vocabulary (not frozen CHECK):

| Field | Allowed examples |
|-------|------------------|
| `render_target` | `html_export`, `pdf_export` |
| `render_engine` | `php_template_renderer`, `edge_headless_pdf`, NULL for legacy |
| `template_id` | `iseo_default_v1`, NULL |
| `template_version` | `1`, NULL |

`render_options_json` must never store:

- absolute Windows paths;
- credentials / session tokens / `.env` values;
- real client secrets.

---

## 8. Backfill matrix (rows 1–4)

| id | key | template_id | template_version | render_target | render_engine | source_html_export_id | render_options_json |
|----|-----|-------------|------------------|---------------|---------------|----------------------|---------------------|
| 1 | `snapshot-1-html-v1` | NULL | NULL | NULL *(or optional `html_export` only if Apply wave proves safe; default NULL)* | NULL | NULL | NULL |
| 2 | `snapshot-1-pdf-v1` | NULL | NULL | NULL | NULL | NULL | NULL |
| 3 | `snapshot-1-html-v2` | `iseo_default_v1` | `1` | `html_export` | `php_template_renderer` | NULL | optional safe options |
| 4 | `snapshot-1-pdf-v2` | `iseo_default_v1` | `1` | `pdf_export` | `edge_headless_pdf` | **3** | optional safe engine/source details |

### Backfill rules

- Execute only in **DB-09 Migration Apply 01** (not this charter).
- Gate by **exact id AND exact export_key** (and preferably checksum match).
- Idempotent: re-run leaves same values; no row create/delete.
- **Never** set v1 rows to `iseo_default_v1`.
- Do not mutate artifacts, sizes, checksums, keys, storage paths.

---

## 9. UI behavior after DB-09

Future Implementation wave should:

| Condition | UI |
|-----------|-----|
| `template_id` IS NULL | `Template: not recorded / legacy` |
| `template_id` + version present | `Template: {id} v{version}` |
| PDF with `source_html_export_id` | `Source HTML export: #{id}` |
| PDF without source | omit or `Source HTML export: not recorded` |

Rules:

- Prefer DB columns over filename/content inference.
- Preserve current labels if metadata absent (graceful fallback).
- Never imply v1 had `iseo_default_v1`.

---

## 10. Future registry / client assignment relation

| Later wave | Role |
|------------|------|
| DB-10+ `report_templates` | registry of known templates/versions/config |
| Client assignment | map client/project → template preference |
| Delivery / share | read durable export metadata; do not invent from filenames |

DB-09 columns remain the **per-export fact table** even after a registry exists (`template_id` may later become FK-like soft key to registry `template_key`, without requiring immediate FK).

---

## 11. Compatibility

- Existing routes/repositories that SELECT `*` or explicit column lists must tolerate new nullable columns (Apply wave may include minimal repository SELECT updates only if required for smoke — prefer read-compatible defaults).
- No change to storage paths or public routes in DB-09.
- No new export rows required for schema success.
