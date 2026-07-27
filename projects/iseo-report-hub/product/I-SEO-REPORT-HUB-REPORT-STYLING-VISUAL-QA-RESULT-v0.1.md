# I-SEO Report Hub — Report Styling Visual QA Result v0.1

## 1. Status

- **complete**
- visual QA verdict: **PASS_WITH_MINOR_ISSUES**
- styled HTML v2 inspected: **yes**
- styled PDF v2 inspected: **yes** (structure/text + integrity; pixel screenshot of PDF viewer **not** reliable)
- screenshot evidence: **yes** (HTML v2); PDF page PNG attempts blank / inconclusive
- DB unchanged: **yes**
- artifacts unchanged: **yes**

## 2. Baseline

| Export id | key | format | status | size | checksum (sha256) |
|-----------|-----|--------|--------|------|-------------------|
| 1 | `snapshot-1-html-v1` | html | ready | 5360 | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| 2 | `snapshot-1-pdf-v1` | pdf | ready | 133005 | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` |
| 3 | `snapshot-1-html-v2` | html | ready | 8562 | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` |
| 4 | `snapshot-1-pdf-v2` | pdf | ready | 117055 | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` |

Artifact root: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\`

DB counts (before = after): schema_migrations **7**; tables **15**; report_exports **4** (html **2**, pdf **2**); report_snapshots **1**; monthly_report_contents **1** (finalized).

## 3. HTML v2 Structural QA

| Assertion | Result |
|-----------|--------|
| `<!DOCTYPE html>` / `<html` / `<head` / `<body` | PASS |
| charset UTF-8 | PASS |
| template id `iseo_default_v1` | PASS |
| template version `1` | PASS |
| snapshot key `monthly-1-v1` | PASS |
| period `2026-07` | PASS |
| title / client / project / site present | PASS |
| major sections (Executive Summary, Work Completed, Results Summary, Risks and Blockers, Key Findings, Next Month Plan) | PASS (as h2/h3 content) |
| weekly sources / diagnostics | PASS |
| embedded CSS + `@page` | PASS |
| no `<script` | PASS |
| no remote stylesheet / img / script assets | PASS |
| no absolute Windows paths in HTML source | PASS |
| no credentials/session/env patterns | PASS |
| size 8562 | PASS |
| fixture site URL `https://demo.example.test` in content (not CDN) | ACCEPTED_FOR_MVP |

## 4. HTML v2 Visual QA

Method: Edge headless `--screenshot` of local file copy under STORAGE.

Evidence: `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\html-v2-screen.png`

Findings:

- header / brand **i-SEO** visible; title readable
- metadata grid clear (period, client, project, site, template, checksum)
- section hierarchy clear; spacing consistent; no clipped/overlapping text
- risk block left accent visible
- typography readable; no mojibake in fixture Latin text
- template/version diagnostics present but footer-level, not intrusive
- professional enough for MVP internal/client-ready fixture review

Issues: see §7 (fixture English-only body; raw block keys in some titles).

## 5. PDF v2 QA

| Check | Result |
|-------|--------|
| `%PDF` magic | PASS |
| size 117055 / checksum match DB | PASS |
| page count | **3** (`pypdf` + `/Count`) |
| encrypted | **no** |
| text extraction (`pypdf`) | PASS — Executive Summary, Next Month Plan, `2026-07`, `iseo_default_v1`, LOCAL_FIXTURE, report blocks present |
| Edge headless PDF page PNG | inconclusive (blank gray frames) |
| WinRT rasterize | unavailable in this shell |

Visual findings (from text + HTML source fidelity):

- content spans 3 pages; not blank
- Edge print chrome injects date + `file:///X:/MARS-Localhost/.../monthly-1-v2.html` + page `n/3` into footer region
- badge text still says “HTML ARTIFACT” in PDF body (template render-target label)

## 6. HTTP QA

Server: temporary PHP built-in `127.0.0.1:8091` (read-only GET smoke; no POST create).

| Check | Result |
|-------|--------|
| `/health` 200 | PASS |
| `/login` 200 | PASS |
| `/not-existing` 404 | PASS |
| auth exports list shows v1+v2 | PASS |
| `/report-exports/3` + `/4` | PASS |
| download 3 HTML 200 | PASS |
| download 4 PDF 200 + `%PDF` | PASS |
| snapshot shows styled v2 available | PASS |
| `/share/exports/1` not public | PASS (404) |
| direct public artifact URL | not served as open file (302) |
| `report_exports` still 4 | PASS |
| smoke summary | **35/35 PASS** |

## 7. Findings

| Severity | Finding | Evidence | Recommendation |
|----------|---------|----------|----------------|
| ACCEPTED_FOR_MVP | Fixture body mostly English `LOCAL_FIXTURE_ONLY`; `lang=ru` + Arial stack support Cyrillic but body not exercised | HTML screenshot + source | Optional Cyrillic fixture later; not a styling blocker |
| ACCEPTED_FOR_MVP | Content URL `https://demo.example.test` in meta (not asset fetch) | HTML source | Keep; do not treat as external asset regression |
| MINOR | PDF Edge headers/footers leak local `file:///X:/...` path + print date | `pdf-v2-text-sample.txt` page 2 | Future PDF print flags / header-footer disable in export engine |
| MINOR | PDF badge still “HTML ARTIFACT” | PDF text p1 | Template render-target label for PDF export |
| MINOR | Some block titles use raw keys (`work_completed`) alongside human titles | HTML screenshot | Content/title normalization later |
| ACCEPTED_FOR_MVP | PDF pixel screenshot via headless Edge inconclusive | blank PNGs under STORAGE | Manual PDF viewer check optional; text extraction sufficient for this wave |

No BLOCKER / MAJOR findings.

## 8. Evidence Files

STORAGE only (not committed):

- `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\html-v2-screen.png`
- `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\html-v2-structural.txt`
- `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\pdf-v2-text-sample.txt`
- `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\pdf-v2-meta.txt`
- `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\http-visual-qa-results.txt`
- `X:\AI MARS STORAGE\incoming\iseo-report-hub\styling-visual-qa-01\http-visual-qa-smoke.php`
- inconclusive: `pdf-v2-page-1.png`, `pdf-v2-page-1b.png`, `pdf-v2-page-1-embed.png`

## 9. Restrictions

Confirmed: no DB mutation; no artifact mutation; no code/runtime changes; no new export rows; no package install; no secrets in docs; no public/share; no push.

## 10. Next Phase

**I-SEO Report Hub — Report Export Template Metadata DB-09 Charter 01**

## 11. SAFE UNKNOWN

- Pixel-perfect visual of PDF pages in this environment (headless Edge PDF viewer screenshots blank; WinRT PDF API unavailable).
- Exact Apache/`iseo-report-hub.test` HTTP behavior this session (port 80 not used; smoke on PHP built-in `8091`, consistent with prior apply wave).
