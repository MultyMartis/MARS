# I-SEO Report Hub — Client Report Surface Audit v0.1

**Status:** CHARTER / AUDIT — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Charter 01  
**Authority:** Operator I-SEO Report Hub Client Report Template Visual Alignment Charter 01

No app-source, runtime, DB, export, share, or PDF mutation in this wave.

---

## 1. Purpose

Зафиксировать **текущие клиентские и около-клиентские поверхности** отчёта и решить:

- какая поверхность канонический **клиентский документ**;
- какие поверхности остаются **внутренними**;
- какая поверхность **кормит PDF**;
- какую поверхность выравнивать **первой**.

Это audit текущего кода/маршрутов, не visual QA всех admin-страниц.

---

## 2. Surface inventory

### 2.1 Internal monthly preview

| Field | Value |
|-------|--------|
| Route | `GET /monthly-reports/{id}/preview` |
| Print twin | `GET /monthly-reports/{id}/preview/print` |
| Controller | `ReportPreviewController` |
| View | `app/Views/pages/report-preview/show.php` (`print.php` requires the same file) |
| Layout | Default admin `layout.php` → sidebar + topbar + footer |
| Auth | Internal roles only |
| Content source | Live `ReportPreviewService::assemble()` (`blocks_primary` for report id **1**) |
| Admin chrome | **Yes** |
| Client-safe | **No** |

Current layout facts:

- badge `Только внутри`;
- operator controls: месячный отчёт / блоки / печать / снимок / (edit if not finalized);
- facts list with period `code`, snapshot key, weekly source links;
- each block shows `block_type`, status, `sort_order`, `block_key`;
- weekly sources section;
- `<details>` diagnostics (`render_mode`, weekly ids, metric refs, DB-05 fallback);
- print CSS hides sidebar/topbar/diagnostics/controls, but on-screen preview is an admin page.

**Verdict:** useful **operator working preview**, not a client report. Implementation 01 may **reuse the route** and replace the visual shell so the same URL becomes a document preview.

### 2.2 Export detail

| Field | Value |
|-------|--------|
| Route | `GET /report-exports/{id}` |
| Controller | `ReportExportController::show` |
| View | `app/Views/pages/report-exports/show.php` |
| Layout | Admin shell |
| Auth | Internal roles |
| Purpose | Artifact metadata, download, share/handoff readiness |
| Admin chrome | **Yes** |
| Client-safe | **No** |

Shows download / «Ссылки для клиента» / handoff checklist / technical checksums behind `<details>`. This is **manager delivery ops**, not the report body.

Related internal surfaces (also not client report):

- `GET /report-exports/{id}/shares`
- `GET /report-snapshots/{id}/exports`
- `GET /monthly-reports/{id}` (workspace + work entries)
- `GET /monthly-reports/{id}/assembly-preview` (manager assembly/apply)

### 2.3 Public share

| Field | Value |
|-------|--------|
| Route | `GET /share/report/{64-hex-token}` |
| Malformed tokens | same prefix → generic 404, no existence leak |
| Controller | `PublicReportShareController::download` |
| View | **None** — no `public-share/show.php` |
| Behaviour | Unauthenticated **PDF file stream** (`Content-Disposition: attachment`) |
| Token handling | Token hashed at rest; plaintext URL shown once at create; never print tokens in docs |
| Admin chrome | **No** (bare 404/410 HTML on deny) |
| Client-safe | **Yes as delivery channel** — streams existing PDF artifact; **does not render live HTML** |

Active local share (charter context, not re-probed for token): likely id **7** / `test-first-link` for export **4**. This wave must **not** open, copy, or print the token.

**Implication:** restyling live PHP views does **not** change what a client currently downloads from an active share, until a **new PDF artifact** is generated and a **new share** (or explicit regeneration charter) points at it.

### 2.4 PDF / export HTML template

| Field | Value |
|-------|--------|
| HTML generator | `ReportTemplateRenderer::render()` |
| Tokens | `ReportTemplateService::defaultTokens()` (`iseo_default_v1` v**1**) |
| CSS | Embedded in the HTML artifact (`embeddedCss()`); **not** `app.css` |
| HTML export v2 | export id **3** · `snapshot-1-html-v2` |
| PDF export v2 | export id **4** · `snapshot-1-pdf-v2` · checksum prefix `a8c4d61c6216e8d70b19` |
| PDF engine | Edge headless from the HTML artifact |
| Feeds PDF? | **Yes** — PDF v2 is print of styled HTML v2 |
| Visually aligned to target? | **Partial / not yet** |

Current export document still reads as an **internal artifact**:

- badge «Internal report export — HTML artifact»;
- meta grid includes snapshot key, checksum, render mode, template id;
- «Source weekly checkpoints»;
- block meta: `block_key` · type · sort;
- footer diagnostics (template/snapshot/checksum);
- English fixture titles / `LOCAL_FIXTURE` attested in Visual QA 01;
- Arial/system stack, dark brand `#0f172a`, **no i-SEO yellow**, no Manrope;
- risk left-bar exists, but overall look is technical export, not a client SEO report.

Historical v1 (ids **1–2**) stay legacy. Do not rewrite any existing artifact in this charter or in Implementation 01.

---

## 3. Classification

| Surface | Class | First visual wave? |
|---------|-------|--------------------|
| `/monthly-reports/{id}/preview` (+ print) | Internal route today; **target first client-document canvas** | **Yes** |
| `/monthly-reports/{id}/assembly-preview` | Internal manager assembly | No — already cleaned |
| `/report-exports/{id}` and shares UI | Internal delivery ops | No |
| `/share/report/{token}` | Client **delivery** of stored PDF | Not in Impl 01 (static file) |
| HTML/PDF artifacts 1–4 | Immutable issued files | No mutation |
| `ReportTemplateRenderer` | Future export/PDF source | Code may be prepared later; **no regen now** |

---

## 4. Canonical client report view (decision)

**Canonical client report = a dedicated document template**, not the admin preview page as it exists today.

| Role | Surface |
|------|---------|
| **Canonical document composition** | New reusable client report render (Option B) |
| **First live place to see it** | `GET /monthly-reports/1/preview` (same route; new document layout, no sidebar) |
| **Current client-delivered file** | PDF export **4** via public share stream |
| **PDF source** | Styled HTML export (today id **3** → PDF id **4**) |
| **Remain internal** | Admin shell, assembly/apply, export detail, share management, block CRUD, snapshot pages |

Do **not** treat export detail or assembly preview as the client report.

---

## 5. Align first

**Implementation 01** aligns the **live internal preview document** (`/monthly-reports/{id}/preview` and print twin).

Reasons:

- no checksum change;
- no share/export row change;
- operator can review the client look without regenerating issued PDF;
- public share stays on unchanged PDF **4**.

Later waves apply the same template to **future** HTML export, then an explicit **new** PDF proof export (never overwrite id **4**).

---

## 6. HTTP note (this charter)

Unauthenticated GET:

| URL | Result |
|-----|--------|
| `http://iseo-report-hub.test/health` | **200** |
| `/monthly-reports/1/preview` | **302** (login) |
| `/report-exports/4` | **302** (login) |

No share URL fetched. No screenshot required.

---

## 7. SAFE UNKNOWN

- Exact active-share id/label was not re-queried in this docs wave (charter context: id **7** / `test-first-link`).
- Whether operators later want a separate `/preview/client` URL vs replacing the existing preview route (recommendation: **replace visual of existing preview route**, keep path).
