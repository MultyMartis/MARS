# I-SEO Report Hub — Report Styling / Client Template Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation; no artifact regeneration  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Styling / Client Template Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-HARDENING-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-HARDENING-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-BROWSER-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-BROWSER-IMPLEMENTATION-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **product/policy слой styling / client template** для HTML/PDF отчётов после Report Export PDF Hardening.

Цель charter:

1. Спроектировать styling/client template layer для monthly preview, HTML export и PDF export.
2. Зафиксировать rules: template source of truth, style tokens, client branding, HTML/PDF parity, snapshot immutability.
3. Сравнить model options (code-only / Git config / DB registry / client assignment) и выбрать MVP.
4. Подготовить implementation + validation plans для следующей волны.
5. Не менять app-source / runtime / DB / artifacts в этой волне.

Эта волна — **documentation / policy only**. Template CSS и render code **не** реализуются здесь.

---

## 2. Current Baseline

### Report Export PDF Hardening 01

| Item | Value |
|------|-------|
| Primary | `d8a1b9e10ad62773aebe9347593c6a87aded2259` |
| Hash-record | `01127fb5a0a673eda547fa49b8620713f493308a` |
| Tip clarify | `4e1798bcfc540ae0422d13853bc380e89f92bc81` |
| Status | **COMPLETE** |
| Push | **no** |
| Smoke | **67/67 PASS** |
| Coverage | path / anti-traversal / MIME / size / checksum / `%PDF` magic / idempotency / safe download headers |

### Report Export PDF Browser Implementation 01

| Item | Value |
|------|-------|
| Primary | `ddea70ba803cb196444377d43d9673633bbde7b5` |
| Final tip | `b24f6beb7488c15f393540900e3d94e1ad8733ee` |
| Engine | Microsoft Edge headless |
| PDF export id | **2** |
| Export key | `snapshot-1-pdf-v1` |
| PDF size / checksum | **133005** / `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` |

### Report Export HTML Artifact Implementation 01

| Item | Value |
|------|-------|
| Primary | `25cf8d4229c1e31bf1159ed2976bb320340bb336` |
| Hash-record | `ce1c095a7d67192e59b764d7b9ea64229e1c48ae` |
| HTML export id | **1** |
| Export key | `snapshot-1-html-v1` |
| HTML size / checksum | **5360** / `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |

### Snapshot / system state

| Item | Value |
|------|-------|
| Snapshot id | **1** · key `monthly-1-v1` · status `active` |
| Snapshot checksum | `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` |
| Expected DB | migrations **7**; tables **15**; `report_exports` **2** (html **1** + pdf **1**) |
| Auth downloads | **yes** |
| Public share / client portal / production | **no** |
| Current HTML styling | minimal embedded CSS in `ReportExportService::embeddedCss()` (Georgia/serif; no template id/version; no A4 `@page`; no formal design system) |

### Current limitation

- no styling/template charter;
- no formal report design system;
- no client template model;
- no client branding model;
- no HTML/PDF visual parity policy beyond current implementation;
- no template versioning policy;
- no repair/regeneration policy for styling changes.

---

## 3. Problem

Current exports **работают технически** (HTML + PDF + hardening + auth download), но:

- визуальный язык отчёта не спроектирован как product layer;
- нет явного template id/version как render policy;
- нет правил client branding vs i-SEO default;
- нет политики, что styling change **не** должен silently overwrite historical artifacts;
- нет согласованных A4/print / parity правил для Edge PDF path.

Без charter следующий implementation risk: ad-hoc CSS в builder, silent artifact mutation, schema creep для client branding слишком рано.

---

## 4. Scope

### In scope

- styling policy for preview / HTML export / PDF export / future client delivery;
- template model options + MVP decision;
- branding model (MVP vs later);
- snapshot/export immutability boundary;
- implementation plan for Default Template Implementation 01;
- validation plan for that future wave.

### Out of scope (this charter)

- app-source code edits;
- runtime edits;
- DB / SQL / migrations;
- HTML/PDF artifact regeneration;
- new `report_exports` rows;
- public share / client portal;
- package install;
- production deployment;
- binary logo asset introduction (deferred until rights/path confirmed).

---

## 5. Product Rules

1. **Snapshot is content SoT** — `report_snapshots` payload remains immutable input; template is **render policy**, not content.
2. **Template is deterministic** — same snapshot + same template id/version → same visual structure (modulo known engine quirks).
3. **HTML is the styled source** — PDF is derived from HTML via Edge; style once in HTML/print CSS.
4. **No silent overwrite** — existing ready HTML/PDF artifacts remain historical unless explicit repair/regeneration charter.
5. **No external assets in export** — no CDN, no remote fonts/images, no JS in export artifact.
6. **Embedded + print CSS allowed** — light theme; A4; printable margins; Edge-safe CSS.
7. **MVP branding = i-SEO default only** — client/project/site names from snapshot payload may appear; no logo upload / color picker / per-client CSS DB.
8. **Future metadata** — exports should eventually record `template_id`, `template_version`, `render_engine`, `render_options`, source checksums; DB-09 deferred.
9. **LOCAL_FIXTURE_ONLY** remains — no real client production data assumed.

---

## 6. Recommended MVP Decision

| Decision | Value |
|----------|-------|
| Template approach | **Code-first default template** (option A; optional Git-config tokens later without DB) |
| Template id | `iseo_default_v1` |
| Template version | `1` |
| Applies to | **future** generated HTML/PDF exports |
| Existing artifacts | **unchanged** historical records |
| DB-backed template registry | **not MVP** |
| Client-level template assignment | **not MVP** |
| Preferred next wave | **Report Styling Default Template Implementation 01** (no schema required) |
| Alternate if schema forced first | Report Export Template Metadata DB-09 Charter 01 — **not preferred** |

**Why code-first:** fastest; no migration; matches current `embeddedCss()` locus; proves visual/parity rules before inventing admin UI or `report_templates` table.

---

## 7. Safety Boundary

| Forbidden in this charter | Status |
|---------------------------|--------|
| app-source / runtime mutation | **yes — none** |
| DB mutation / migrations | **yes — none** |
| Artifact regeneration / new export rows | **yes — none** |
| Public share / client portal | **yes — none** |
| Package install / Composer / npm | **yes — none** |
| Push / fetch / pull / reset / clean / stash | **yes — none** (commit docs only; push no) |

Future implementation must preserve: export hardening guards; checksum/idempotency; auth-only downloads; snapshot immutability.

---

## 8. Next Wave

**Recommended single next action:**

`I-SEO Report Hub — Report Styling Default Template Implementation 01`

Scope preview (details in implementation plan):

- implement `iseo_default_v1` / version `1` in HTML artifact builder;
- embed template id/version in HTML (visible and/or meta/comment);
- print/@page A4 rules Edge-compatible;
- do **not** silently overwrite export ids 1–2;
- optional new export version only if that implementation charter explicitly allows;
- no DB-09 unless separately chartered.

---

## 9. Document set

| Doc | Role |
|-----|------|
| This charter | Product decision + boundary |
| Design v0.1 | Visual / branding / parity / metadata rules |
| Implementation plan v0.1 | Next-wave execution plan |
| Validation plan v0.1 | Future smoke / regression checks |
