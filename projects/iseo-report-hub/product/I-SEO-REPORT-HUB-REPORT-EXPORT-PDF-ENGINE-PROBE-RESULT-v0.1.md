# I-SEO Report Hub — Report Export PDF Engine Probe Result v0.1

**Status:** COMPLETE — read-only environment probe  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Probe 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.2.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Probe status | **complete** |
| Read-only | **yes** |
| Install / download | **no** |
| PDF generated | **no** |
| DB mutated | **no** |
| Runtime mutated | **no** |
| App-source mutated | **no** |
| Composer / npm install | **no** |

---

## 2. Baseline

| Item | Value |
|------|-------|
| HEAD at probe start | `4883cd391fef8bb756ae9b11550f6db088af5039` |
| PDF Engine Charter primary / hash-record / tip | `e16fc414…` / `22f2f80e…` / `4883cd39…` |
| HTML Export primary / hash-record | `25cf8d42…` / `ce1c095a…` |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **7** |
| tables | **15** |
| report_snapshots | **1** |
| report_exports | **1** (HTML only) |
| pdf `report_exports` rows | **0** |
| HTML export id | **1** |
| HTML export key | `snapshot-1-html-v1` |
| HTML format / status | `html` / `ready` |
| HTML storage_path | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html` |
| HTML checksum | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| HTML size | **5360** bytes |
| Absolute HTML path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html` |
| PDF files under export storage | **none** |

---

## 3. Engine Inventory

| Engine | Classification | Path | Version | Notes |
|--------|----------------|------|---------|-------|
| Microsoft Edge | **AVAILABLE_READY** | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` | Product/FileVersion **150.0.4078.99** (Application folder `150.0.4078.99`) | Preferred primary. `msedge` not on PATH. CLI `--version` unreliable/hang-prone on this host; version taken from `FileVersionInfo` / folder name. Chromium-family headless print-to-PDF **not executed** in this probe (forbidden). |
| Google Chrome | **AVAILABLE_READY** | `C:\Program Files\Google\Chrome\Application\chrome.exe` | Product/FileVersion **150.0.7871.182** | Alternate primary. `chrome` not on PATH. Same `--version` caveat; FileVersion confirmed. |
| Chromium (standalone) | **MISSING** | `C:\Program Files\Chromium\Application\chrome.exe` | — | Not found; PATH `chromium` empty. |
| Firefox Developer Edition | **NOT_RECOMMENDED_FOR_MVP** | `C:\Program Files\Firefox Developer Edition\firefox.exe` | **154.0b1** (`--version` OK) | Present (MARS Browser Workstation likely). Not preferred for CLI print-to-PDF without proven path. |
| Mozilla Firefox | **NOT_RECOMMENDED_FOR_MVP** | `C:\Program Files\Mozilla Firefox\firefox.exe` | **153.0** | Present; same non-preferred note. |
| wkhtmltopdf | **MISSING** / **DEFERRED_REQUIRES_INSTALL_APPROVAL** | known Program Files paths | — | Not on PATH; both `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe` and x86 path absent. |
| Composer | present (CLI only) | `C:\ProgramData\ComposerSetup\bin\composer.bat` | **2.10.1** (2026-06-04) | Available when PHP 8.3.30 is on PATH. **No** `composer.json` in app-source or runtime. Libraries = **DEFERRED_REQUIRES_INSTALL_APPROVAL**. |
| PHP / extensions | env ready for future PHP libs **only after approval** | Laragon `php-8.3.30-Win32-vs16-x64\php.exe` | **8.3.30** | Loaded: mbstring, gd, intl, dom, xml, iconv, openssl, fileinfo, pdo_mysql, curl. **zip** not loaded. System PATH has no `php` by default. |

---

## 4. Font / Cyrillic Readiness

| Font family | Present under `C:\Windows\Fonts` |
|-------------|----------------------------------|
| Arial | **yes** (`arial.ttf` + variants) |
| Times New Roman | **yes** (`times.ttf` + variants) |
| Calibri | **yes** |
| Segoe UI | **yes** (`segoeui.ttf` + variants) |
| DejaVu | **no** |

Limitations:

- Cyrillic likely OK for Edge/Chrome using system Arial/Segoe UI/Calibri — **not** proven by PDF render in this probe.
- DejaVu absent — relevant mainly if a future PHP engine (Dompdf/mPDF) were approved.
- **No** font files copied, committed, or shared.

---

## 5. HTML Artifact Readiness

| Check | Result |
|-------|--------|
| Exists | **yes** |
| Size | **5360** |
| SHA-256 | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` (matches expected) |
| Contains `monthly-1-v1` | **yes** |
| Contains `2026-07` | **yes** |
| `<script` tags | **none** detected (case-insensitive) |
| Outside `public/` | **yes** |
| Under export storage root | **yes** |

---

## 6. Security / Dependency Findings

- No install, download, Composer require, npm install, or binary fetch performed.
- Future PDF generation will require **allowlisted** process execution of a known browser path (Edge or Chrome) — not arbitrary PATH resolution.
- CLI `--version` on Edge/Chrome can hang or spawn UI processes; Implementation must use controlled headless flags, timeouts, and dedicated temp profile dirs — **no** interactive user profile.
- Composer present ≠ approval to add Dompdf/mPDF.
- wkhtmltopdf absent → any use requires explicit install approval.
- Probe wrote no runtime/source files; temporary DB-read PHP under `X:\AI MARS STORAGE\incoming\iseo-report-hub\_probe-temp\` removed after use.

---

## 7. Recommendation

| Field | Value |
|-------|-------|
| Selected candidate | **Microsoft Edge** (Chromium) |
| Exact executable | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Version evidence | **150.0.4078.99** |
| Alternate | Google Chrome `C:\Program Files\Google\Chrome\Application\chrome.exe` (**150.0.7871.182**) |
| Why | Both browsers already installed and versioned without install; HTML artifact ready; charter prefers headless/local browser; wkhtmltopdf missing; PHP PDF libs need Composer approval |
| Next action | **I-SEO Report Hub — Report Export PDF Browser Implementation 01** |

Do **not** recommend Firefox-first, wkhtmltopdf, or Composer libraries for MVP without separate operator approval.

---

## 8. Implementation Constraints

- No public / share / token download routes.
- PDF storage: `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` (outside public; not Git).
- `report_exports` PDF row policy: `export_key` `snapshot-1-pdf-v1`; format `pdf`; status `ready`; relative `storage_path` only.
- Input: existing ready HTML export artifact (id 1) with checksum match.
- Idempotency: second create must not duplicate ready PDF for same snapshot checksum.
- Download: auth-only via existing `/report-exports/{id}/download` pattern.
- No install in Implementation unless operator explicitly expands charter.

---

## 9. SAFE UNKNOWN

- Exact Edge/Chrome headless `--print-to-pdf` flag set, exit codes, and temp-profile behavior on this host — **not** executed (probe forbidden PDF write).
- Whether PHP `zip` extension is required for a future Composer PDF library — moot until library approval.
- Whether Firefox has a reliable headless print-to-PDF CLI on this host — not validated; not recommended for MVP.
- Long-term production host engine path (non-Localhost) — out of scope for this local probe.
