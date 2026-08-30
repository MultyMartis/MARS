# I-SEO Report Hub — Report Export PDF Engine Decision v0.2

**Status:** DECISION — probe-backed engine selection; PDF implementation still deferred to next wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.2  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Probe 01  
**Supersedes sequencing of:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md) (v0.1 remains historical probe-first policy; **do not modify** v0.1)  
**Evidence:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-PROBE-RESULT-v0.1.md)

---

## 1. Probe summary

Read-only probe on Localhost host (2026-07-27):

- Microsoft Edge **available** at `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` — version **150.0.4078.99**.
- Google Chrome **available** at `C:\Program Files\Google\Chrome\Application\chrome.exe` — version **150.0.7871.182**.
- Standalone Chromium **missing**.
- Firefox / Firefox Developer Edition **present** but not preferred for MVP CLI PDF.
- wkhtmltopdf **missing**.
- Composer **2.10.1** present; **no** project `composer.json`; PHP PDF libraries **not** approved.
- HTML export artifact id **1** ready; checksum match; **no** PDF files; **no** PDF DB rows.
- **No** install, PDF generation, DB mutation, or runtime/source code change in probe.

---

## 2. Selected engine candidate

| Field | Value |
|-------|-------|
| Engine class | Headless / controlled local Chromium browser (Microsoft Edge) |
| Exact executable | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` |
| Version evidence | **150.0.4078.99** |
| Alternate allowlist path | `C:\Program Files\Google\Chrome\Application\chrome.exe` (**150.0.7871.182**) |
| Input source | Existing ready HTML export artifact |
| Install required for MVP path | **No** (use already-installed Edge) |

---

## 3. Rejected / deferred candidates

| Candidate | Disposition |
|-----------|-------------|
| Firefox Developer Edition / Firefox | **NOT_RECOMMENDED_FOR_MVP** — present; no proven CLI print-to-PDF as first engine |
| wkhtmltopdf | **MISSING** — requires install approval |
| Dompdf / mPDF / other Composer libs | **DEFERRED_REQUIRES_INSTALL_APPROVAL** — Composer present but no project deps; need explicit operator charter |
| Manual browser print | Interim ops workaround only — not automated `report_exports` PDF path |
| Downloading Chromium / npm browser fetchers | Denied without install approval |

---

## 4. Dependency approval state

| Item | State |
|------|-------|
| Edge / Chrome already on disk | **Approved for Implementation charter use** (allowlisted paths only) |
| New browser / Chromium download | **Not approved** |
| wkhtmltopdf install | **Not approved** |
| Composer require (Dompdf/mPDF/…) | **Not approved** |
| npm install / binary fetch | **Not approved** |
| Font file copy into Git | **Forbidden** |

Any expansion beyond allowlisted Edge/Chrome executables requires a separate operator approval wave.

---

## 5. Source HTML artifact policy

```
report_snapshots (immutable)
  → report_exports HTML (ready, checksum match)
    → PDF bytes via Edge headless print
      → report_exports PDF row + storage file
```

Rules unchanged from v0.1:

- Use HTML only if `status=ready` and source snapshot checksum matches.
- Do not silently render from live monthly/blocks if HTML missing or mismatched.
- Fixture baseline: export id **1**, key `snapshot-1-html-v1`, checksum `c194c62b81c6…`.

---

## 6. Future implementation boundary

Allowed in **Report Export PDF Browser Implementation 01** (separate charter):

- App-source PDF create path using allowlisted Edge (fallback Chrome) executable.
- Write PDF under storage exports tree; insert `report_exports` PDF metadata.
- Auth-only download; idempotency; smoke (`%PDF`, checksum).
- Exact-path source→runtime sync for allowlisted code only.

Forbidden unless separately approved:

- Install/download of engines or Composer packages.
- Public/share/token routes.
- Mutation of snapshots / monthly / blocks / periods / weekly.
- HTML artifact regeneration as side effect of PDF create (unless explicit repair charter).

---

## 7. Next action

**I-SEO Report Hub — Report Export PDF Browser Implementation 01**

One next action only. Probe is complete; engine candidate selected without install.
