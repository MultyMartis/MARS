# REPORT — I-SEO REPORT HUB REPORT EXPORT PDF ENGINE PROBE 01

**Status:** COMPLETE (read-only probe + docs)  
**project_id:** `iseo-report-hub`  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Probe 01  
**Primary commit:** `PENDING_PRIMARY`  
**Hash-record commit:** `PENDING_HASH_RECORD`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `4883cd391fef8bb756ae9b11550f6db088af5039` |
| Staged/index before (main) | **non-empty foreign** (`projects/client-ops-reporting-bridge/**` staged deletions/docs) — **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-pdf-engine-probe-01\repo` (detached at `4883cd39`) |
| i-SEO WIP before | **clean** |
| Foreign WIP | **preserved** (main index untouched) |
| Write scope | Active Brain docs only under allowlisted product/reports/OPERATIONAL-INDEX in clean worktree |

No STOP.

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| PDF Engine Charter primary / hash-record / tip | `e16fc4149712e1770c7b6dd8c53109469347c018` / `22f2f80eaa6fea18bc4a1b3f50a92f45ad74c5ed` / `4883cd391fef8bb756ae9b11550f6db088af5039` |
| HTML Export primary / hash-record | `25cf8d4229c1e31bf1159ed2976bb320340bb336` / `ce1c095a7d67192e59b764d7b9ea64229e1c48ae` |
| DB-08 primary / hash-record / clarify | `7b059bb2…` / `e0a13795…` / `3b35673f…` |
| DB (read-only) | `iseo_report_hub_dev` @ `127.0.0.1` |
| Counts | migrations **7**; tables **15**; users **1**; roles **6**; clients/projects/sites **1**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6**; report_snapshots **1**; report_exports **1**; pdf exports **0** |
| HTML export id 1 | key `snapshot-1-html-v1`; `html`/`ready`; checksum `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4`; size **5360** |
| Artifact FS | exists outside public; content has `monthly-1-v1` + `2026-07`; no `<script`; **no** `.pdf` under export storage |
| Current limitation before probe | no engine selected; no PDF artifact/row/routes |

---

## 3. Probe Commands / Scope

Classes of checks (read-only only):

- `Test-Path` / `Get-Item` / `Get-ChildItem` on candidate browser/wkhtmltopdf paths and Windows Fonts
- `where.exe` / `Get-Command` for msedge/chrome/chromium/firefox/wkhtmltopdf/composer/php
- Timed process `--version` where safe; `FileVersionInfo` for Edge/Chrome when CLI unreliable
- `composer --version` with Laragon PHP on PATH
- Laragon `php -v` / `php -m` (extension subset)
- SHA-256 + content sanity on HTML artifact; recursive `*.pdf` search under export storage (none)
- Read-only MySQL SELECT/COUNT via temporary PHP under `X:\AI MARS STORAGE\incoming\iseo-report-hub\_probe-temp\` (removed after use)

Confirmed: **no** PDF generation; **no** install/download; **no** DB mutation; **no** runtime/source mutation.

---

## 4. Engine Inventory

| Engine | Classification | Path / version |
|--------|----------------|----------------|
| Microsoft Edge | **AVAILABLE_READY** | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` — **150.0.4078.99** |
| Google Chrome | **AVAILABLE_READY** | `C:\Program Files\Google\Chrome\Application\chrome.exe` — **150.0.7871.182** |
| Chromium standalone | **MISSING** | — |
| Firefox Developer Edition | **NOT_RECOMMENDED_FOR_MVP** | `C:\Program Files\Firefox Developer Edition\firefox.exe` — **154.0b1** |
| Mozilla Firefox | **NOT_RECOMMENDED_FOR_MVP** | `C:\Program Files\Mozilla Firefox\firefox.exe` — **153.0** |
| wkhtmltopdf | **MISSING** / install deferred | — |
| Composer | CLI present; libs deferred | **2.10.1**; no project `composer.json` |
| PHP / extensions | env noted | **8.3.30**; mbstring/gd/intl/dom/xml/iconv/openssl/fileinfo/pdo_mysql/curl **on**; zip **off** |
| Fonts | Cyrillic-capable candidates present | Arial, Times New Roman, Calibri, Segoe UI **yes**; DejaVu **no** |

---

## 5. HTML Artifact / DB Findings

| Check | Result |
|-------|--------|
| HTML artifact | exists; 5360 B; checksum match; outside public |
| PDF files under export storage | **0** |
| `report_exports` | **1** HTML ready |
| `format=pdf` rows | **0** |

---

## 6. Recommendation

| Field | Value |
|-------|-------|
| Selected engine | **Microsoft Edge** |
| Exact path | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Version | **150.0.4078.99** |
| Alternate | Chrome `C:\Program Files\Google\Chrome\Application\chrome.exe` (**150.0.7871.182**) |
| Next action | **I-SEO Report Hub — Report Export PDF Browser Implementation 01** |

---

## 7. Future Implementation Boundary

- Source: ready HTML artifact (`monthly-1-v1.html` / export id 1).
- Output: `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` (outside public; not Git).
- Metadata: `report_exports` row `snapshot-1-pdf-v1`.
- Route: `POST /report-snapshots/{id}/exports/pdf`; auth-only download.
- Idempotency + checksum validation required.
- No public/share; no install unless separately approved.

---

## 8. Restrictions Confirmed

- no app-source edits
- no runtime edits
- no DB mutation
- no SQL/migration creation/edit
- no report_exports / report_snapshots / report_blocks / monthly_report_contents / weekly_checkpoint / reporting_period row changes
- no admin/password/hash changes
- no env changes
- no source sync
- no service restart
- no file/PDF generation
- no package install/download
- no push/fetch/pull/reset/clean/stash

---

## 9. Documentation

Created/updated:

- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md`
- `reports/REPORT-iseo-report-hub-report-export-pdf-engine-probe-01.md` (this file)
- `OPERATIONAL-INDEX.md` — Probe status; Edge selected; next = Browser Implementation 01; note no code/runtime/DB/PDF in probe

v0.1 Decision / v0.2 Implementation / v0.2 Validation plans **not** modified.

---

## 10. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted docs only |
| Commit message | `docs(iseo-report-hub): record pdf engine probe` |
| Primary commit hash | `PENDING_PRIMARY` |
| Hash-record message | `docs(iseo-report-hub): record pdf engine probe commit hash` |
| Hash-record commit hash | `PENDING_HASH_RECORD` |
| Push | **no** |

---

## 11. SAFE UNKNOWN

- Exact Edge/Chrome headless `--print-to-pdf` flag/exit behavior on this host (not executed; PDF write forbidden in probe).
- Firefox reliable CLI print-to-PDF path (not validated; not recommended).
- Non-Localhost production engine path (out of scope).

---

## 12. Recommended Next Action

**I-SEO Report Hub — Report Export PDF Browser Implementation 01**

---

## 13. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.3.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.3.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-export-pdf-engine-probe-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 14. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** (worktree) |
| commit | **yes** (primary + hash-record) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout / update-ref | **yes** — `git update-ref refs/heads/mars/canonical-post-recovery <new-tip>` from worktree after commits; scoped restore on main for i-SEO docs if needed |
| reset | **no** |
| restore | **scoped only** on main for allowlisted i-SEO docs if required to align working tree |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | used `X:\AI MARS STORAGE\git-sync-iseo-pdf-engine-probe-01\repo`; remove after update-ref when safe |
