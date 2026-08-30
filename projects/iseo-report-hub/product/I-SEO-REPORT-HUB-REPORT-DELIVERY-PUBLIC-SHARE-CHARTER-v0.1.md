# I-SEO Report Hub — Report Delivery / Public Share Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation; no SQL/migration file; no share token; no public route; no artifact regeneration  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Delivery / Public Share Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-UI-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-UI-IMPLEMENTATION-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-TEMPLATE-METADATA-DB09-MIGRATION-APPLY-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-VISUAL-QA-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-EXPORT-VERSION-APPLY-RESULT-v0.1.md)

---

## 1. Purpose

Спроектировать **docs/policy слой** для безопасной client-facing delivery finalized report exports без internal admin login.

Charter отвечает:

1. Какой export можно шарить?
2. Кто создаёт / отзывает share links?
3. Какой artifact отдаётся клиенту?
4. Как долго ссылка жива?
5. Как аудируется доступ?
6. Как доставить файл без exposure storage paths?
7. Как отключить / revoke sharing?
8. Что входит в MVP и что откладывается?

Эта волна — **documentation / policy only**. Code, DB-10 migration apply, token creation, public route и artifact mutation **не** выполняются здесь.

---

## 2. Current Baseline

### Report Export Template Metadata UI Implementation 01

| Item | Value |
|------|-------|
| Primary | `bd64bd03ec02c03592eb127cfc27ed34815aad6f` |
| Hash-record | `415da5eca71e65a7cb437ce2dac613cd3043a8db` |
| Tip HEAD (at charter start) | `6a282380bda621658787da0bd56f0b0cb3f3b63f` |
| Status | **COMPLETE** |
| Push | **no** |
| UI/repository/service | DB-09 metadata read/display + future styled write support |
| Smoke | HTTP **27/27 PASS** |
| Public/share | **none** |

### Report Export Template Metadata DB-09 Migration Apply 01

| Item | Value |
|------|-------|
| Primary | `c1e7ba2416f1e49ef0f115d0efa23ffcb7abd317` |
| Hash-record | `11e2c84a095a80692f62d0f4a106fb331475240f` |
| Tip | `4fe3c7e444db2b469e720c598c364f8f501fb9ac` |
| `schema_migrations` | **8** |
| Tables | **15** |
| `report_exports` | **4** |
| DB-09 columns/indexes/FK | present on `report_exports` |
| Backfill | ids **1–2** metadata NULL; ids **3–4** filled; id **4** `source_html_export_id=3` |

### Report Styling Visual QA 01

| Item | Value |
|------|-------|
| Primary | `1d1d3c0d4af462698dc8fef84c03d3d1673bdcab` |
| Verdict | **PASS_WITH_MINOR_ISSUES** |
| BLOCKER / MAJOR | **none** |
| Styled v2 | accepted for MVP |

### Export rows (ids 1–4)

| id | key | format | checksum (sha256) | template metadata |
|----|-----|--------|-------------------|-------------------|
| 1 | `snapshot-1-html-v1` | html | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` | legacy / not recorded |
| 2 | `snapshot-1-pdf-v1` | pdf | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` | legacy / not recorded |
| 3 | `snapshot-1-html-v2` | html | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` | `iseo_default_v1 v1` / HTML export / PHP template renderer |
| 4 | `snapshot-1-pdf-v2` | pdf | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` | `iseo_default_v1 v1` / PDF export / Edge headless PDF; source HTML id **3** |

### DB baseline (read-only check this charter)

| Metric | Value |
|--------|-------|
| Target | `iseo_report_hub_dev` @ `127.0.0.1` |
| schema_migrations | **8** |
| tables | **15** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |
| report_blocks | **6** |
| report_snapshots | **1** |
| report_exports | **4** (html **2**, pdf **2**) |

### Artifact baseline (read-only filesystem check)

Runtime storage root: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\`  
Checksums for v1/v2 HTML/PDF **match** expected values above. **No** mutation.

### Current limitation

- exports are **auth-only** internal downloads;
- **no** public share route;
- **no** client-facing delivery token model;
- **no** share lifecycle (create / expiry / revoke);
- **no** delivery audit model;
- **no** documented public access policy;
- **no** client portal;
- `/share` previously validated **404**.

---

## 3. Problem

Current downloads are auth-only. There is no safe client-facing delivery mechanism for finalized report exports.

Operators cannot:

- issue a controlled public link to a ready PDF;
- expire or revoke that link;
- audit client access without sharing admin credentials;
- deliver artifacts without exposing storage paths or creating a public webroot copy.

---

## 4. Scope

### In scope

- share model;
- access / eligibility policy;
- token / security policy;
- data model options (recommended `report_export_shares`);
- route / UI plan;
- validation plan;
- OPERATIONAL-INDEX update;
- closeout REPORT.

### Out of scope (this charter)

- code implementation;
- DB mutation;
- SQL / migration file creation or edit;
- share token creation;
- public route creation;
- artifact changes / regeneration;
- new export rows;
- email sending;
- client portal;
- production deployment.

---

## 5. Product Options

| Option | Summary | Pros | Cons | MVP? |
|--------|---------|------|------|------|
| **A** Internal-only delivery | Keep auth downloads; operator sends file manually | Safest now; no public surface | No self-service; no link lifecycle; weak delivery audit | No (keeps current gap) |
| **B** Tokenized public share | Admin creates token for export; public route streams if valid | Client delivery; auditable; limited surface | Token/URL risk; needs DB table + hardening | **Yes — recommended** |
| **C** Client portal login | Client users log in and download | Stronger identity; scalable later | Auth/UI/onboarding scope too large | Deferred |
| **D** One-time / limited links | Consume-once or max access | Tighter security | Friction / support; not needed for first MVP | Deferred (model `max_access_count` later) |
| **E** Email delivery | Send PDF or link by email | Familiar workflow | Mail config, size, deliverability, audit complexity | Deferred |

---

## 6. Recommended MVP Decision

**Option B — tokenized public share for ready styled PDF exports only.**

MVP rules:

- share only `format=pdf`, status `ready`, `template_id` not null, `render_target=pdf_export`;
- first eligible local export: id **4** (`snapshot-1-pdf-v2`);
- no HTML public share;
- no client portal;
- no email sending;
- no one-time link required;
- default expiry **30 days**;
- revoke supported;
- store **token hash** only; show plaintext URL **once** at creation;
- stream through app with path hardening + checksum validation;
- no raw storage path; no public listing; no public webroot artifact copy;
- audit events required.

Full design / security / implementation / validation: linked sibling docs.

---

## 7. Safety Boundary

This charter **must not**:

- edit `app-source/**` or Localhost runtime;
- mutate DB / create migration SQL;
- create share tokens or public routes;
- regenerate artifacts or change `report_exports` / snapshot / block / monthly / weekly / period rows;
- write artifacts into public docroot;
- change `.env` / `.env.local`;
- push / fetch / pull / reset / clean / stash;
- remediate foreign WIP.

Docs-only write paths are limited to the allowlisted charter / design / security / plan / validation / REPORT / OPERATIONAL-INDEX files.

---

## 8. Next Wave

Recommended next action:

**I-SEO Report Hub — Report Delivery Public Share DB-10 Migration Apply 01**

DB-10 intent (future wave):

- create `report_export_shares` table;
- **no** share token rows yet;
- **no** public route yet;
- validation only.

Follow-up after DB-10:

**I-SEO Report Hub — Report Delivery Public Share Implementation 01** — service/repository/controller/routes/UI + smoke.
