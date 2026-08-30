# I-SEO Report Hub — Report Export PDF Engine Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation; no PDF; no engine install  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **PDF engine decision layer** после Report Export HTML Artifact Implementation.

Цель charter:

1. Спроектировать PDF generation path на базе immutable snapshot / HTML export artifact.
2. Сравнить варианты PDF generation для Windows / Laragon / PHP 8.3 runtime.
3. Выбрать recommended MVP direction (probe-first, not immediate implementation).
4. Зафиксировать dependency / storage / access / audit policy.
5. Подготовить implementation + validation plans v0.2 для следующих волн.
6. Не устанавливать engines; не создавать PDF; не менять app-source / runtime / DB.

Эта волна — **documentation / policy only**.

---

## 2. Current Baseline

### Report Export HTML Artifact Implementation

| Item | Value |
|------|-------|
| Primary commit | `25cf8d4229c1e31bf1159ed2976bb320340bb336` — `feat(iseo-report-hub): add html report export workflow` |
| Hash-record | `ce1c095a7d67192e59b764d7b9ea64229e1c48ae` |
| Smoke / regression | **PASS** |
| Push | **no** |

### DB-08 Report Exports Migration Apply

| Item | Value |
|------|-------|
| Primary commit | `7b059bb285452735a5834bb1a5789d22e6733d06` |
| Hash-record | `e0a13795c1d71aa37fadad973bc63733b91a8fa7` |
| Clarify | `3b35673f2a5275d556a24f2642c8cc3814bfca1d` |
| Migrations | **7** |
| Tables | **15** |
| `report_exports` | exists |

### Report Snapshot Implementation

| Item | Value |
|------|-------|
| Primary commit | `7d19979183947a25510915a7d36da9655c370673` |
| Hash-record | `040586fe96db91868704ed448402f640f438cb02` |
| Clarify | `c6b5d84161a751c594444a93510b159eb4c73a17` |
| Closeout-hashes | `7c3dbf1cabb119f645bfa94553087bfe40d412ea` |
| Snapshot id | **1** |
| Key | `monthly-1-v1` |
| Status | `active` |
| Checksum | `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` |

### Current DB / export / artifact (read-only this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **7** |
| Tables | **15** |
| report_snapshots | **1** |
| report_exports | **1** |
| Export id 1 | key `snapshot-1-html-v1`; format `html`; status `ready` |
| File checksum | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| File size | **5360** bytes |
| Relative path | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html` |
| Absolute path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html` |
| Outside public webroot | **yes** |
| Auth-only download | **yes** |
| PDF export row | **0** |
| PDF file under exports | **none** |

### Already present

- Finalized monthly report
- Immutable snapshot
- Export metadata table (`report_exports`)
- HTML export artifact + auth-only download

### Current limitation

- no PDF engine selected or validated;
- no PDF route;
- no PDF artifact;
- no PDF dependency policy executed;
- no public share / client portal.

---

## 3. Problem

Система умеет:

- создать immutable snapshot;
- создать HTML export artifact вне public webroot;
- записать metadata в `report_exports`;
- отдать HTML через auth-only download.

Но нет:

- выбранного / проверенного PDF engine для Windows/Laragon/PHP;
- dependency policy для binary / Composer / browser automation;
- PDF storage/metadata row;
- PDF generation route;
- validated Cyrillic/font path for server-side PDF.

Нужен **engine decision + probe-first plan** до любой PDF implementation.

---

## 4. Scope

### In scope

- PDF engine comparison (manual print, headless browser, wkhtmltopdf, Dompdf, mPDF);
- dependency policy;
- storage / source / access / audit policy;
- probe plan;
- future implementation + validation plans (v0.2).

### Out of scope

- PDF generation;
- engine / package / binary install;
- app-source / runtime / DB mutation;
- public share / client portal / email delivery;
- production deployment.

---

## 5. Product Rules

1. PDF export строится из **`report_snapshots`** или существующего ready HTML export artifact — **не** из live monthly / report_blocks.
2. MVP: **internal-only**; auth-only download; **не** public share; **не** client portal; **не** email.
3. Artifact storage: вне public webroot; вне Git; relative path в DB; no absolute path в metadata.
4. Metadata: `report_exports` row (`format=pdf`, unique `export_key`, checksums, mime, size).
5. Preferred PDF input source: existing ready HTML export artifact whose `source_snapshot_checksum_sha256` matches snapshot.
6. Idempotency: ready PDF for same snapshot checksum + matching file checksum → return existing; no silent duplicate.
7. No Composer/npm/binary install without explicit operator approval after probe.
8. No production deployment in MVP local path.

---

## 6. Recommended Decision

1. **Do not** implement server-generated PDF immediately.
2. First run **PDF Engine Probe / Environment Capture** (read-only / no install):
   - browser executable candidates (Edge / Chrome / Firefox);
   - `wkhtmltopdf` availability;
   - Composer / PHP extension availability (read-only);
   - Cyrillic/font signals if safe;
   - document feasible engine or STOP.
3. After probe:
   - prefer **Headless Chromium / controlled local browser** only if already available without install;
   - otherwise defer until operator approves install/add of an engine;
   - avoid Composer libraries (Dompdf/mPDF) until dependency policy is explicitly approved.
4. Manual browser print remains temporary operator fallback (not true server PDF).

**Recommended next action:**  
`I-SEO Report Hub — Report Export PDF Engine Probe 01`

---

## 7. Safety Boundary

This wave and the probe wave must **not**:

- edit `app-source/**` (except docs outside app-source);
- edit runtime under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`;
- mutate DB / SQL / migrations;
- install Composer / npm / Chromium / wkhtmltopdf / Dompdf / mPDF;
- create PDF files;
- regenerate HTML artifacts;
- add public/token routes;
- push / fetch / pull / reset / clean / stash;
- touch foreign WIP.

Allowed: Active Brain docs under allowlisted paths; exact-path docs commits; clean temporary worktree when main index has foreign staged paths.

---

## 8. Next Wave

**I-SEO Report Hub — Report Export PDF Engine Probe 01**

Purpose: read-only environment capture; recommend exact engine or STOP; no PDF implementation unless a separate explicit charter later authorizes generation.
