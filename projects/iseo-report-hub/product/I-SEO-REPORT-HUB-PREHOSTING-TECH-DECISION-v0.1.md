# I-SEO Report Hub — Pre-hosting Tech Decision v0.1

**Status:** decision documented — **deployment not authorized**  
**Date:** 2026-08-21  
**Wave:** Pre-hosting Demo Scenario and Field Help Charter 01  
**Scope:** host PHP/runtime checks only — no upload, no DB import, no PDF/export regen

---

## Target host

| Field | Value |
|-------|-------|
| **Subdomain** | `reports.i-seo.su` |
| **SSL** | Operator states SSL **already done** for the subdomain |
| **Product local URL (dev)** | `http://iseo-report-hub.test/` |
| **Future public URL** | `https://reports.i-seo.su/` (intended; not live product proof in this wave) |

---

## Recommended PHP version

| Decision | Value |
|----------|-------|
| **Host PHP** | **PHP 8.3** (pin minor line; prefer latest 8.3.x available on host) |
| **Reason** | Local Laragon runtime used for development and acceptance is **PHP 8.3.x** (attested **8.3.30** in Laragon preflight / operational index). Keep host aligned with the tested line. |
| **Do not** | Downgrade to PHP 8.1/8.2 for convenience without a separate compatibility charter |

---

## Database engine

| Topic | Decision / note |
|-------|-----------------|
| **Local SoT** | MySQL **8.4.3** on Laragon (`iseo_report_hub_dev`) |
| **Host target** | MySQL **or** MariaDB — **compatibility must be verified before deploy** |
| **Schema notes** | Migrations use InnoDB, `utf8mb4`, and some MySQL 8-style defaults (e.g. `utf8mb4_0900_ai_ci` in early tables). MariaDB hosts may need collation/CHECK review. |
| **Action before upload** | Confirm host engine + version; dry-run schema apply on a staging DB; **do not** import production client data yet |

---

## Required host checks (pre-upload checklist)

Confirm on the hosting panel / phpinfo / CLI **before** any file or DB upload:

1. **PHP 8.3** selected for the subdomain / site
2. **PDO MySQL** (`pdo_mysql`) enabled
3. **mbstring** enabled (string/Unicode paths used throughout)
4. **intl** — enable if present/used; treat as required if host PHP build expects it for locale/IDN; otherwise verify app still runs without it (**SAFE UNKNOWN** until host probe)
5. **fileinfo** — required if uploads/exports touch MIME detection
6. **curl** — enable if any outbound HTTP helpers are used later; not a hard product dependency for local MVP UI
7. **OpenSSL** — expected with SSL/TLS on host
8. **JSON** extension — baseline PHP requirement for the app
9. **Write permissions** for storage / export / runtime writable directories (exact paths to confirm in deployment charter)
10. **URL rewriting / front controller routing** — Apache `AllowOverride` + rewrite, or equivalent Nginx `try_files` to `public/index.php`
11. **Document root** must point at app `public/` (or equivalent), not repo root
12. **Cron / scheduled jobs** — **SAFE UNKNOWN**: current MVP does not require product cron for report authoring; revisit only if host delivery/reminders are added

---

## Explicit non-actions (this wave and until operator approval)

- **Do not** upload application files to `reports.i-seo.su` in this charter wave
- **Do not** import/export local DB to host
- **Do not** regenerate PDF / export / share during pre-hosting decision
- **Do not** change production DNS beyond what operator already did for SSL
- **Do not** treat SSL-ready as deploy-ready

---

## Recommended next technical charter

After demo scenario is accepted locally:

`I-SEO Report Hub — Pre-hosting Deployment Readiness Charter 01`

That charter must cover: file layout, env secrets handling, DB migration path, rewrite rules, writable dirs, smoke checklist, and rollback — still **no** upload until explicit operator approval.

---

## Evidence used (read-only)

- Laragon / PHP pin in programme operational index (PHP 8.3.30 local)
- Operator inputs: subdomain, SSL done, PHP recommendation 8.3
- Optional local HTTP: `/health` and `/login` returned 200 in charter preflight (runtime available)
