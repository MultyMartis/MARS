# I-SEO Report Hub — Report Export / PDF Design v0.1

**Status:** DESIGN / PLANNING ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export / PDF Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md)

---

## 1. Export definition

A **report export** is an internal downloadable artifact generated from an **active (or selected) `report_snapshots` row**.

It is:

- internal-only for MVP;
- generated from immutable snapshot payload;
- stored as a file outside public webroot;
- tracked by metadata (recommended: `report_exports`);
- served only through authenticated routes;
- **not** generated from live monthly/report_blocks content;
- **not** public share;
- **not** client portal;
- **not** email delivery;
- **not** production deployment.

First MVP format: **HTML** (`.html`). PDF is a later format after engine charter.

---

## 2. Source of truth

| Source | Role |
|--------|------|
| `report_snapshots` | **Sole content source** for export body (payload_json / rendered fields / metadata) |
| Snapshot checksum | Copied to export as `source_snapshot_checksum_sha256` |
| `monthly_report_contents` | Parent id / permission context only — not live body |
| `report_blocks` | **Not** read for export content (already frozen in snapshot) |
| Actor session | `created_by` on export metadata |

If snapshot status is not exportable (e.g. archived policy TBD), generation fails closed.

---

## 3. Format decision

| Option | Pros | Cons | MVP |
|--------|------|------|-----|
| 1. Browser print from snapshot HTML | Simple; no engine | No stored artifact | Keep as UX helper; not export SoT |
| 2. Server-generated HTML file | Deterministic; no PDF engine; proves storage/auth | Not PDF | **Recommended first** |
| 3. Server-generated PDF | Client-ready binary | Engine/deps/Windows brittle | **Deferred** |

**Decision:** Implementation sequence = HTML export artifact first → PDF engine charter → PDF implementation.

Existing `GET …/preview/print` remains live preview print — **not** a substitute for snapshot-based export.

---

## 4. HTML export design

### Content

HTML artifact should include:

- immutable snapshot header (key, version, status, checksum);
- report title;
- period / client / project / site context from snapshot payload;
- ordered blocks from snapshot payload;
- weekly source refs from snapshot payload;
- `generated_at` / `exported_at`;
- self-contained markup for local viewing.

### Safety

- no external CDN;
- no scripts;
- no secrets / credentials;
- escape user-provided content (title/body/summary);
- inline or embedded CSS only (artifact lives outside public assets path).

### Generation input

Prefer snapshot payload composition. Optional use of snapshot `rendered_text` as outline; do **not** require `rendered_html` (currently null on snapshot id 1).

---

## 5. PDF deferral

PDF options to evaluate in a **future PDF Engine Charter**:

- headless Chromium / browser print pipeline;
- wkhtmltopdf;
- Dompdf;
- mPDF.

Engine charter must decide: Windows/Laragon binary availability, Cyrillic fonts, layout fidelity, security, runtime path, dependency policy (no Composer/npm unless explicitly approved).

Until then: **no PDF routes**, **no PDF format generation** in HTML export wave.

---

## 6. Storage path

Runtime root (local):

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\`

Layout:

`monthly-{monthly_report_content_id}/snapshot-{snapshot_id}/`

Example:

`…\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html`

Full policy: [STORAGE-PLAN](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md).

---

## 7. Filename / export key

| Field | Policy | Example |
|-------|--------|---------|
| filename | `{snapshot_key}.{format}` | `monthly-1-v1.html` |
| export_key | `snapshot-{snapshot_id}-{format}-v1` | `snapshot-1-html-v1` |

Rules: ASCII; kebab/safe chars; no Cyrillic; no client names; no spaces; no raw user title.

---

## 8. Routes (future implementation, after DB-08)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/report-snapshots/{id}/exports` | List exports for snapshot |
| POST | `/report-snapshots/{id}/exports/html` | Generate HTML export (CSRF) |
| GET | `/report-exports/{id}` | Metadata / detail |
| GET | `/report-exports/{id}/download` | Authenticated stream/download |

Forbidden: public routes; token URLs; direct filesystem URLs; PDF routes until PDF wave.

---

## 9. Services / repositories (planned)

| Component | Responsibility |
|-----------|----------------|
| `ReportExportService` | Gates, idempotency, HTML render from snapshot, file write, checksum, audit |
| `ReportExportRepository` | CRUD for `report_exports` metadata |
| `ReportSnapshotRepository` (existing) | Load snapshot; no mutation |
| Controller(s) | Auth, CSRF, list/create/detail/download |

No hard DELETE of rows in MVP; archive status later.

---

## 10. UI integration (planned)

- Snapshot detail page: export list + “Generate HTML export” for allowed roles.
- Monthly show / snapshot card: link to exports when present.
- Export detail: metadata, checksums, download button.
- No public share UI.

---

## 11. Access model

| Role | Generate HTML | View / download |
|------|---------------|-----------------|
| `admin_owner` | yes | yes |
| `seo_lead_reviewer` | yes | yes |
| `seo_specialist` | no | yes |
| `account_client_manager` | no | yes |
| `internal_viewer` | no | yes (view + download for internal MVP) |
| `client_viewer` | no | no |

All routes require auth. CSRF on POST.

---

## 12. Audit events

| Event | When |
|-------|------|
| `report_export.created` | New metadata + file ready |
| `report_export.idempotent_hit` | Same checksum+format; existing returned |
| `report_export.downloaded` | Optional (may be noisy) |
| `report_export.creation_failed` | Generation failure |

Payload (no secrets): export_id; report_snapshot_id; monthly_report_content_id; format; relative storage_path; file checksum; source snapshot checksum; actor user id.

---

## 13. Idempotency

On POST generate HTML:

1. Load snapshot; require exportable status (MVP: `active`).
2. Look up existing `report_exports` for same snapshot + format + status `ready` with matching `source_snapshot_checksum_sha256`.
3. If metadata exists and file exists → return existing + `idempotent_hit`.
4. If metadata exists but file missing → mark `failed` or regenerate per implementation policy (document choice in HTML impl wave).
5. If checksum unchanged and ready export exists → do not create duplicate unless forced (forced = out of MVP).

---

## 14. No-public policy

- No public routes.
- No signed/token download URLs in MVP.
- No files under `public/`.
- No Git commit of artifacts.
- `client_viewer` denied.
- Download only after role check inside authenticated controller stream.
