# I-SEO Report Hub — Report Export PDF Validation Plan v0.3

**Status:** PLANNING — probe complete; future Browser Implementation smoke  
**project_id:** `iseo-report-hub`  
**Version:** v0.3  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Probe 01  
**Supersedes sequencing of:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md) (v0.2 remains historical; **do not modify** v0.2)  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md)

---

## 1. Preflight

| Check | Expected |
|-------|----------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` label `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| i-SEO WIP | clean before start (or charter-allowed paths only) |
| Staged | no `projects/iseo-report-hub/` unless intended; foreign-only → clean worktree |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` only |
| Probe baseline | Edge selected; HTML export id **1** ready |
| Restrictions | no push/fetch/pull/reset/clean/stash; no secrets printed |

---

## 2. Engine executable validation

| Check | Expected |
|-------|----------|
| Primary path exists | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Version evidence | Product/FileVersion readable (e.g. **150.0.4078.99**) |
| Alternate | Chrome path optional fallback |
| Allowlist | Implementation uses absolute allowlisted path only — not PATH discovery of arbitrary `chrome` |
| No install | confirmed |

Probe already recorded Edge/Chrome as **AVAILABLE_READY**. Implementation must still validate headless print-to-PDF exit success.

---

## 3. HTML source validation

| Check | Expected |
|-------|----------|
| Export id (fixture) | **1** |
| Key | `snapshot-1-html-v1` |
| Format / status | `html` / `ready` |
| File exists | outside `public/` |
| Checksum | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` matches DB |
| Source snapshot checksum | matches `report_snapshots.checksum_sha256` |
| Snapshot status | `active` |

Mismatch → **do not** generate PDF; fail safely.

---

## 4. PDF output validation

1. POST `/report-snapshots/{id}/exports/pdf` as allowed role + CSRF.
2. File at `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf`.
3. Size > 0; magic bytes `%PDF`.
4. Outside `public/`; not under Git.
5. Engine name/version in audit (no secrets).

---

## 5. Metadata validation

| Field | Check |
|-------|-------|
| New row | `format=pdf`, `status=ready`, key `snapshot-1-pdf-v1` |
| Paths | relative only |
| MIME | `application/pdf` |
| Checksums | file SHA-256 matches DB; source snapshot checksum copied |
| Unchanged | HTML export row; snapshot; monthly; blocks; periods; weekly |

---

## 6. Idempotency

- Second POST with same snapshot checksum → same export id / no extra ready PDF row.
- If DB row exists but file missing → fail safely (no silent corrupt success).

---

## 7. Download / auth

1. GET `/report-exports/{pdf_id}` → 200 for allowed roles.
2. GET `/report-exports/{pdf_id}/download` → PDF body / disposition.
3. Unauthenticated → redirect/401/403 per app pattern.
4. `client_viewer` → denied.

---

## 8. No public

- No public/token/share route.
- PDF not under `public/`.
- No client portal / email delivery in MVP smoke.

---

## 9. No dependency install

- No Composer require / npm install / winget / choco / browser download.
- No wkhtmltopdf install.
- Use only probe-selected allowlisted Edge (or Chrome alternate).

---

## 10. Regression

- HTML export create/download still works.
- Snapshot show / export list still works.
- Finalized monthly + locks unchanged.
- Counts: migrations **7**; tables **15**; business fixtures unchanged except new PDF export row.

---

## 11. Probe validation (this wave — already required)

| Check | Expected |
|-------|----------|
| No package/binary install | confirmed |
| No PDF file created | confirmed |
| No DB mutation | `report_exports` still **1**; PDF rows **0** |
| No app-source / runtime mutation | docs-only |
| Engine inventory documented | complete |
| Recommendation | Edge exact path + Browser Implementation next |

---

## 12. STOP conditions

STOP if:

- Edge and Chrome missing at Implementation start;
- install proposed without approval;
- HTML checksum mismatch;
- wrong DB host/name;
- public route proposed;
- PDF write outside storage exports tree;
- scoped commit unsafe;
- foreign WIP would be staged.
