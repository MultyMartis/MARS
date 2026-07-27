# I-SEO Report Hub — Report Export PDF Implementation Plan v0.3

**Status:** PLANNING — probe-selected Edge browser path; no PDF code in this probe wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.3  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Probe 01  
**Supersedes sequencing of:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md) (v0.2 remains historical; **do not modify** v0.2)  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md)

---

## 1. Selected / proposed engine (from probe)

| Field | Value |
|-------|-------|
| Engine | Microsoft Edge (Chromium) headless print-to-PDF |
| Exact executable | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Version evidence | **150.0.4078.99** |
| Alternate | `C:\Program Files\Google\Chrome\Application\chrome.exe` (**150.0.7871.182**) |
| Install | **Not required** for this path |
| Input | Existing ready HTML export artifact |
| Next wave | **I-SEO Report Hub — Report Export PDF Browser Implementation 01** |

---

## 2. Future route

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/report-snapshots/{id}/exports/pdf` | Create / idempotently return PDF export |
| GET | `/report-exports/{id}` | Existing detail — support `format=pdf` |
| GET | `/report-exports/{id}/download` | Existing download — PDF MIME / attachment |

Forbidden: public route; token route; direct filesystem URL; GET mutation.

---

## 3. Input

- Existing HTML export artifact for the snapshot (fixture: export id **1**, key `snapshot-1-html-v1`).
- Absolute file (Localhost):  
  `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html`
- Preconditions: `status=ready`; file checksum matches `report_exports.checksum_sha256`; `source_snapshot_checksum_sha256` matches active snapshot.
- Prefer `file://` or controlled local read of HTML bytes — **no** authenticated HTTP fetch that requires cookies in the browser process unless explicitly designed and approved.

---

## 4. Output

| Item | Value |
|------|-------|
| Absolute file | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.pdf` |
| Relative `storage_path` | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` |
| Filename | `monthly-1-v1.pdf` |
| MIME | `application/pdf` |
| Outside `public/` | required |
| Not in Git | required |

---

## 5. DB (`report_exports` PDF row)

| Field | Expected (fixture) |
|-------|--------------------|
| `export_key` | `snapshot-1-pdf-v1` |
| `format` | `pdf` |
| `status` | `ready` |
| `storage_disk` | `local` |
| `storage_path` | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` |
| `filename` | `monthly-1-v1.pdf` |
| `mime_type` | `application/pdf` |
| `file_size_bytes` | > 0 |
| `checksum_sha256` | SHA-256 of PDF bytes |
| `source_snapshot_checksum_sha256` | copy of snapshot checksum |
| Absolute path in DB | **forbidden** |

Idempotent second POST: ready PDF count for same snapshot checksum unchanged.

---

## 6. Storage

- Root: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\`
- Layout: `monthly-{id}/snapshot-{id}/{snapshot_key}.pdf`
- Outside public webroot; not Desktop/Downloads as SoT.

---

## 7. Engine invocation constraints (future Implementation)

- Allowlist absolute Edge path (Chrome alternate only if Edge missing/fails policy).
- Dedicated temp user-data-dir; headless; no network preference for local HTML; hard timeout.
- Do **not** run interactive `--version` probes that hang in production path.
- Capture engine name + version in audit payload (no secrets; prefer relative storage refs).
- Process execution risk: treat as controlled subprocess — never pass untrusted URL/path strings from clients.

---

## 8. Smoke (future Implementation)

1. HTML source exists; checksum match.
2. PDF created outside public; magic `%PDF`; size > 0.
3. `report_exports` PDF row inserted; checksum match.
4. Auth download returns PDF.
5. Second POST idempotent.
6. No install; no public route; no snapshot/monthly/blocks/period/weekly mutation.

---

## 9. Restrictions

- No install / download / Composer require / npm install unless operator explicitly expands charter.
- No PDF generation in Probe 01 (already satisfied).
- No public/share/client portal.
- No secrets in docs or logs.

---

## 10. STOP conditions

STOP Implementation if:

- Edge and Chrome allowlisted paths both missing or non-executable;
- proposed path requires install without approval;
- HTML export missing / checksum mismatch;
- DB target not `iseo_report_hub_dev` @ `127.0.0.1`;
- public/share route proposed;
- foreign WIP remediation required;
- scoped commit cannot be guaranteed.
