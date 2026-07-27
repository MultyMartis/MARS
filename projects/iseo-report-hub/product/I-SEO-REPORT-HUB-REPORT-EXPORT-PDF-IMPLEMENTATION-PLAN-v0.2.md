# I-SEO Report Hub — Report Export PDF Implementation Plan v0.2

**Status:** PLANNING ONLY — no PDF; no engine install; no app-source in this charter wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.2  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Charter 01  
**Supersedes for next-step sequencing:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md) (v0.1 remains historical: DB-08 → HTML; v0.2 starts after HTML)  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md)

---

## 1. Next wave

**I-SEO Report Hub — Report Export PDF Engine Probe 01**

Purpose: read-only environment capture; recommend exact engine or STOP; **no** PDF generation unless separately authorized; **no** Composer/npm/binary install; **no** DB mutation; **no** app-source edits unless docs-only paths explicitly allowed by probe charter.

---

## 2. Probe scope

Probe should inspect (read-only):

| Check | Notes |
|-------|-------|
| Microsoft Edge executable | Common Windows path candidates |
| Google Chrome executable | If present |
| Firefox Developer Edition | Optional candidate |
| `wkhtmltopdf` | PATH / known install locations |
| Composer | Availability only (do not require packages) |
| PHP extensions | Image/font-related if useful (read-only) |
| Cyrillic fonts | Safe inventory only |
| CLI execution feasibility | Policy notes only; no PDF write |

Probe must **not**: install software; create PDF (unless future probe charter explicitly permits a one-shot generate — **not** default); mutate DB; sync source→runtime.

Probe output: recommended engine + absolute executable path (if any) **or** STOP for operator approval.

---

## 3. Then: PDF implementation (only if engine selected)

**Future wave name (after probe):**  
`I-SEO Report Hub — Report Export PDF Artifact Implementation 01` (exact title may be set by operator)

Planned work (not this charter):

1. Exact allowlist sync source → runtime if code changes.
2. Extend `ReportExportService` (or sibling) for format `pdf`.
3. Generate PDF from ready HTML artifact (preferred).
4. Write file under storage exports tree; insert `report_exports` PDF row.
5. Audit events; idempotency; auth download via existing download route.
6. Smoke per Validation Plan v0.2.
7. No public share; no HTML/snapshot/monthly/block mutation; no unapproved installs.

---

## 4. Future routes

Only after engine decision/probe:

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/report-snapshots/{id}/exports/pdf` | Create / idempotently return PDF export |
| GET | `/report-exports/{id}` | Existing detail — must support `format=pdf` |
| GET | `/report-exports/{id}/download` | Existing download — PDF MIME / attachment |

Forbidden: public route; token route; direct filesystem URL; GET mutation.

---

## 5. DB row expectations (future)

For fixture snapshot id 1 / HTML export id 1 baseline:

| Field | Expected |
|-------|----------|
| `export_key` | `snapshot-1-pdf-v1` |
| `format` | `pdf` |
| `status` | `ready` |
| `storage_disk` | `local` |
| `storage_path` | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` |
| `filename` | `monthly-1-v1.pdf` |
| `mime_type` | `application/pdf` |
| `file_size_bytes` | > 0 |
| `checksum_sha256` | file hash |
| `source_snapshot_checksum_sha256` | `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` |
| `created_by` | actor user id |
| `archived_at` | null |

No absolute path in DB. Idempotent second POST: count of ready PDF for same snapshot checksum unchanged.

If DB metadata exists but file missing: fail safely; no silent duplicate unless explicit repair charter.

---

## 6. Storage expectations

| Item | Value |
|------|-------|
| Root | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\` |
| Layout | `monthly-{id}/snapshot-{id}/{snapshot_key}.pdf` |
| Fixture example | `...\monthly-1\snapshot-1\monthly-1-v1.pdf` |
| Outside `public/` | required |
| Not in Git | required |
| Not Desktop/Downloads as SoT | required |

---

## 7. Smoke list (future PDF implementation)

1. HTML export exists; checksum matches metadata.
2. PDF created outside public webroot.
3. `report_exports` PDF row inserted.
4. File size > 0; magic bytes `%PDF`.
5. File checksum matches DB.
6. Download returns PDF MIME or attachment.
7. Second POST idempotent (count unchanged).
8. No public route; no HTML/snapshot/monthly/block mutation.
9. No Composer/npm install unless approved.
10. No secrets printed.

---

## 8. Commit policy

- Exact-path stage only; never `git add .` / `-A` / `commit -a`.
- Foreign WIP preserved; clean temporary worktree if main staged index is foreign-only.
- Docs-only for charter/probe; implementation wave uses its own allowlist.
- Commit and push are separate; **push no** unless operator explicitly authorizes.
- Hash-record follow-up docs commits allowed when closeout needs primary hash.

---

## 9. STOP conditions

STOP if:

- probe not done and implementation attempted;
- engine requires install without approval;
- HTML source invalid;
- wrong DB host/name;
- public/share scope creep;
- i-SEO WIP unclean / staged includes iseo unexpectedly;
- scoped commit cannot be guaranteed.
