# I-SEO Report Hub — MVP Phase 0 Scaffold Result v0.1

**Status:** PHASE 0 SCAFFOLD CREATED  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator Phase 0 runtime scaffold charter; [MVP Implementation Phases v0.1](I-SEO-REPORT-HUB-MVP-IMPLEMENTATION-PHASES-v0.1.md); [Laragon Preflight Result v0.1](I-SEO-REPORT-HUB-LARAGON-PREFLIGHT-RESULT-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Phase 0 scaffold | **Created** |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| Implementation beyond scaffold | **None** |
| Database | **Not created** |
| Vhost / hosts | **Not created / not edited** |
| Secrets / `.env` | **None** (`.env.example` placeholders only) |
| Stage relative to product | **Before Phase 1** |

WordPress is **not** used. Platform remains custom **PHP + SQL/MySQL**.

---

## 2. Runtime Path

Exact approved path:

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub`

Local identity (operator-approved):

| Item | Value |
|------|-------|
| Domain (intended) | `iseo-report-hub.test` |
| DB candidate | `iseo_report_hub_dev` |
| PHP | 8.3.30 |

Docs remain in Active Brain: `X:\AI MARS\projects\iseo-report-hub\`.

---

## 3. Files Created

Runtime tree (under Localhost):

- `README.md`
- `.env.example`
- `.gitignore`
- `public/index.php`
- `public/health.php`
- `public/assets/css/app.css`
- `public/assets/js/app.js`
- `app/README.md`
- `app/Controllers/.keep`
- `app/Models/.keep`
- `app/Views/.keep`
- `app/Services/.keep`
- `app/Support/.keep`
- `config/README.md`
- `config/app.example.php`
- `config/database.example.php`
- `storage/README.md`
- `storage/.gitignore`
- `storage/logs/.keep`
- `storage/uploads/.keep`
- `storage/cache/.keep`
- `database/README.md`
- `database/schema-draft-not-migration.md`
- `database/seeds/README.md`
- `docs/README.md`

---

## 4. What Works Now

- PHP pages exist under `public/`.
- Index page shows app name, Phase 0 status, PHP version, no DB attempt.
- Health page reports PHP running, version, required/optional extensions; no DB attempt; `.env` not required.
- Static local CSS/JS (no external CDN).
- Folder placeholders for future MVC layers and storage.
- Config / env **examples** only.

---

## 5. What Does Not Exist Yet

- Auth / sessions product logic
- Database `iseo_report_hub_dev`
- SQL migrations / executable DDL
- Users, reports, evidence uploads pipeline
- Config loader / router / layout beyond static pages
- Laragon vhost / hosts mapping for `iseo-report-hub.test`
- Deployment / production package

---

## 6. Review Instructions

1. Browse files under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`.
2. Confirm no `.env` / `.env.local`.
3. Optionally execute pages via a **manually configured** local server mapping later, or PHP built-in server if the operator chooses.
4. **Do not assume** `http://iseo-report-hub.test` works until hosts/vhost are configured and smoke-tested.

---

## 7. Source / Runtime Note

| Fact | State |
|------|-------|
| Runtime files location | Outside Active Brain Git monorepo (`X:\MARS-Localhost\...`) |
| Phase 0 docs commit | Versions **documentation only** — does **not** commit runtime PHP tree |
| Source / runtime policy | [I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md](I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md) |
| Phase 1 gate | Requires approved **source preservation model** (recommend Model A: `app-source/` + sync) before code/auth/config work |

Optional local runtime mirror doc (not in Git):  
`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\docs\SOURCE-RUNTIME-POLICY.md`

---

## 8. Next Phase

**Phase 1 — App skeleton + config + auth baseline**

**Blocked** until source preservation model is approved (see Source / Runtime Policy v0.1).

Expected direction after gate (charter-dependent):

- config loader;
- environment handling (local `.env`, never committed);
- basic routing / layout;
- auth baseline (DB may still be deferred unless Phase 1 charter decides otherwise).

---

## 9. SAFE UNKNOWN

- Whether `iseo-report-hub.test` already exists in hosts/vhost on this machine (Phase 0 did not inspect or edit).
- Whether MySQL database name `iseo_report_hub_dev` already exists (Phase 0 did not query or create).
- Whether Apache DocumentRoot / alias already points at this scaffold (not verified).
- Exact operator preference for PHP built-in server vs Apache mapping for first smoke test.
