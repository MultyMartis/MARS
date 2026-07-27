# I-SEO Report Hub — Report Export PDF Engine Comparison v0.1

**Status:** PLANNING / COMPARISON ONLY — no install; no PDF generation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md)

---

## 1. Purpose

Сравнить кандидатов PDF generation для i-SEO Report Hub на Windows / Laragon / PHP 8.3.30 local MVP, учитывая уже существующий HTML export artifact.

---

## 2. Context constraints

| Constraint | Implication |
|------------|-------------|
| PHP 8.3.30 / Laragon / Windows | Engine must work (or be probed) in this environment |
| HTML artifact already exists | Prefer HTML→PDF over re-rendering live report |
| No Composer/npm/binary install by default | Probe-first; install needs operator approval |
| Cyrillic report content | Fonts / Unicode path required for any server PDF |
| Internal-only MVP | No public CDN; no client portal delivery |
| Process execution risk | Headless browser / CLI binaries need controlled allowlist |

---

## 3. Candidate: Browser print / manual PDF

| Aspect | Assessment |
|--------|------------|
| Method | Operator opens/downloads HTML artifact and prints to PDF manually |
| Server engine | **None** |
| Fidelity | High (browser print CSS), operator-dependent |
| Metadata | No automatic `report_exports` PDF row unless manually recorded |
| Dependencies | None |
| Security | Lowest server risk |
| Pros | Immediate; no install; uses existing auth HTML download |
| Cons | Not true server-generated PDF; not idempotent product path; weak audit of “PDF created” |
| MVP fit | Temporary fallback only |

---

## 4. Candidate: Headless Chromium / browser automation

| Aspect | Assessment |
|--------|------------|
| Method | Drive local Edge/Chrome (or similar) headless print-to-PDF from HTML file/URL |
| Fidelity | **Best** HTML/CSS fidelity among server options |
| Cyrillic | Good if system fonts available |
| Dependencies | Existing browser executable preferred; avoid npm browser download unless approved |
| Windows/Laragon | Feasible but heavier; needs process execution policy |
| Pros | Matches HTML artifact closely; strong layout |
| Cons | Process spawn; path allowlisting; timeout/hang risk; heavier than PHP lib |
| MVP fit | **Preferred candidate IF probe finds controllable local browser without install** |

---

## 5. Candidate: wkhtmltopdf

| Aspect | Assessment |
|--------|------------|
| Method | CLI HTML→PDF binary |
| Fidelity | Weaker modern CSS than Chromium |
| Cyrillic | Needs font validation |
| Dependencies | Binary install/path (not authorized in docs wave) |
| Pros | Simple CLI; mature for classic HTML |
| Cons | Install required if missing; CSS limits; Qt-era quirks |
| MVP fit | Secondary candidate only if probe finds it already installed **or** operator approves install |

---

## 6. Candidate: Dompdf

| Aspect | Assessment |
|--------|------------|
| Method | PHP Composer library |
| Fidelity | Limited CSS |
| Cyrillic | Font embedding setup can be tricky |
| Dependencies | Composer package (not authorized by default) |
| Pros | No external browser binary; pure PHP process |
| Cons | Layout limits; Composer policy; vendor footprint |
| MVP fit | Deferred until dependency approval; not preferred before probe |

---

## 7. Candidate: mPDF

| Aspect | Assessment |
|--------|------------|
| Method | PHP Composer library |
| Fidelity | CSS/layout limits (often better multilingual text than Dompdf) |
| Cyrillic | Generally stronger multilingual PDF text support than Dompdf in many cases |
| Dependencies | Composer package (not authorized by default) |
| Pros | Better text/Unicode story than Dompdf for some reports |
| Cons | Composer policy; not Chromium fidelity |
| MVP fit | Deferred until dependency approval; not preferred before probe |

---

## 8. Windows / Laragon considerations

- Prefer engines that reuse software already on the operator machine (Edge/Chrome) over new downloads.
- Laragon PHP can `proc_open` / CLI; must constrain executable allowlist and timeouts.
- Do not rely on system PATH alone — probe must record absolute executable paths when found.
- Avoid shipping browser binaries into Active Brain Git or runtime tree without charter.
- Runtime PDF write target remains under `storage/exports/reports/` (outside `public/`).

---

## 9. Cyrillic / font considerations

- Report content is Russian; any server PDF must prove glyph coverage.
- Headless browser usually inherits OS fonts — probe should note font availability signals safely.
- Dompdf/mPDF require explicit font registration/embedding plans before adoption.
- wkhtmltopdf needs font path validation.
- Manual print inherits operator browser fonts (good fidelity, not product automation).

---

## 10. Dependency / security considerations

| Risk | Control |
|------|---------|
| Unapproved Composer/npm | Require separate operator approval after probe |
| Binary download (Chromium/wkhtmltopdf) | Deny by default; approve path + checksum policy later |
| Arbitrary process execution | Allowlist executable paths; no shell injection from report content |
| Public URL fetch during PDF | Prefer local file input from storage HTML; avoid network fetch of report |
| Secrets in audit | No absolute paths if avoidable; no credentials; no `.env` |
| Public webroot leak | Never write PDF under `public/` |
| Git pollution | Never commit PDF binaries |

---

## 11. Recommendation matrix

| Candidate | Fidelity | Install burden | Security ops load | Cyrillic risk | Recommended now |
|-----------|----------|----------------|-------------------|---------------|-----------------|
| Manual browser print | High | None | Low | Low | Fallback only |
| Headless Chromium / local browser | Highest | None **if already present** | Medium | Low–medium | **Preferred after probe if available** |
| wkhtmltopdf | Medium | Binary if missing | Medium | Medium | Probe secondary |
| Dompdf | Lower | Composer | Medium | Medium–high | Deferred |
| mPDF | Medium (text) | Composer | Medium | Medium | Deferred |

**Charter recommendation:** do **not** pick a final install path in this wave. Run **PDF Engine Probe 01**, then select engine or STOP for operator approval.
