# I-SEO Report Hub — Report Export PDF Validation Plan v0.2

**Status:** PLANNING ONLY — no probe executed in this charter wave; no PDF smoke  
**project_id:** `iseo-report-hub`  
**Version:** v0.2  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md) (historical HTML/DB-08 plan)

---

## 1. Preflight (probe and future PDF waves)

| Check | Expected |
|-------|----------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` label `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| i-SEO WIP | clean before start (or charter-allowed paths only) |
| Staged | no `projects/iseo-report-hub/` unless intended; foreign-only → clean worktree |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` only |
| Baseline | HTML Artifact Implementation complete; export id 1 `html`/`ready` |
| Restrictions | no push/fetch/pull/reset/clean/stash; no secrets printed |

---

## 2. Probe validation

After PDF Engine Probe 01:

| Check | Expected |
|-------|----------|
| No package/binary install | confirmed |
| No PDF file created (default) | confirmed unless probe charter explicitly allowed generate |
| No DB mutation | `report_exports` count still **1**; no PDF row |
| No app-source / runtime mutation | unless docs-only allowlist |
| Engine inventory documented | Edge/Chrome/Firefox/wkhtmltopdf/composer/fonts notes |
| Recommendation | exact engine + path **or** STOP for operator approval |

---

## 3. Engine availability checks

Probe evidence should record for each candidate:

- exists: yes/no;
- absolute path if found (no secrets);
- version string if safely obtainable;
- notes on headless/print-to-PDF capability (known/unknown);
- install required: yes/no.

Do not treat “unknown” as “available”.

---

## 4. Source HTML artifact validation (before any PDF generate)

| Check | Expected |
|-------|----------|
| Export id | **1** (fixture) or target id |
| Key | `snapshot-1-html-v1` (fixture) |
| Format / status | `html` / `ready` |
| File exists | outside `public/` |
| File checksum | matches `report_exports.checksum_sha256` |
| Source snapshot checksum | matches `report_snapshots.checksum_sha256` |
| Snapshot status | `active` |

If mismatch: **do not** generate PDF; fail safely.

---

## 5. PDF generation validation (future implementation wave)

1. POST `/report-snapshots/{id}/exports/pdf` as allowed role + CSRF.
2. PDF file written under storage exports layout.
3. File size > 0.
4. Magic bytes start with `%PDF`.
5. Optional: basic text extraction or binary sanity only — **no** OCR requirement.
6. Engine name/version recorded in audit payload.

---

## 6. File checksum validation

- Compute SHA-256 of PDF bytes.
- Match `report_exports.checksum_sha256`.
- `source_snapshot_checksum_sha256` equals snapshot checksum (copied, not recomputed from live blocks).

---

## 7. DB metadata validation

| Field | Check |
|-------|-------|
| New row | `format=pdf`, `status=ready` |
| `export_key` | unique (e.g. `snapshot-1-pdf-v1`) |
| Paths | relative only; no absolute path column value |
| MIME | `application/pdf` |
| Counts | HTML row unchanged; snapshot/monthly/blocks/periods/weekly unchanged |
| Missing file + existing row | fail on download/create repair; no silent duplicate |

---

## 8. Download validation

1. GET `/report-exports/{pdf_id}` → 200 for allowed roles.
2. GET `/report-exports/{pdf_id}/download` → 200; PDF MIME or attachment disposition; body matches file.
3. Unauthenticated → redirect/401/403 per app pattern.
4. `client_viewer` → denied.

---

## 9. No-public validation

- No public/token/share route for PDF.
- PDF not under `public/`.
- No direct URL that bypasses auth download.
- No client portal / email delivery in MVP smoke.

---

## 10. No dependency install validation

Confirm for probe and default implementation:

- no Composer install/require;
- no npm install;
- no Chromium/wkhtmltopdf installer run;
- no vendor commit;
unless a separate operator-approved dependency charter exists and is cited in the implementation report.

---

## 11. Regression smoke

Preserve HTML export regression:

- HTML export still downloadable;
- HTML idempotent POST still returns same export;
- snapshot show still lists HTML export;
- no mutation of snapshot checksum / monthly status / blocks.

PDF idempotency (implementation wave):

- second POST PDF → same export id / key; ready PDF count unchanged;
- audit `report_export.pdf_idempotent_hit`.

---

## 12. STOP conditions

STOP if:

- preflight fails (root/volume/branch/scope);
- probe recommends install but operator approval missing;
- HTML source invalid;
- PDF would be written under public or Git;
- DB host/name wrong;
- secrets would be printed;
- foreign WIP would be staged;
- scoped commit cannot be guaranteed.
