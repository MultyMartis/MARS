# I-SEO Report Hub — Laragon Preflight Result v0.1

**Status:** READ-ONLY PREFLIGHT COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** [Laragon Local Runtime Plan v0.1](I-SEO-REPORT-HUB-LARAGON-LOCAL-RUNTIME-PLAN-v0.1.md), [Platform Decision v0.1](I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Task type | Read-only Laragon / local runtime preflight |
| Runtime changes | **None** |
| Application code | **None** |
| SQL / migrations | **None** |
| Database created | **No** |
| Laragon config edits | **None** |
| Vhost / hosts edits | **None** |
| Service restart | **None** |
| Stage relative to MVP | **Before** Phase 0 scaffold charter |

This document records observed local environment facts. It does **not** authorize scaffold, DB creation, or Laragon changes.

---

## 2. Environment Summary

| Item | Result |
|------|--------|
| **Laragon found** | **Yes** |
| **Laragon version** | 8.6.1 (registry `DisplayVersion`; publisher leokhoa) |
| **Laragon root** | `X:\MARS-Localhost\laragon\` |
| **Shortcut target** | `X:\MARS-Localhost\laragon\laragon.exe` |
| **Common C:/D:/X: roots** | `C:\laragon`, `C:\Laragon`, `D:\laragon`, `D:\Laragon`, `X:\laragon`, `X:\Laragon` — **not found** |
| **`LARAGON_ROOT` env** | unset |
| **www** | `X:\MARS-Localhost\laragon\www` (DocumentRoot) |
| **bin** | `X:\MARS-Localhost\laragon\bin` |
| **etc** | `X:\MARS-Localhost\laragon\etc` |
| **data** | `X:\MARS-Localhost\laragon\data` |
| **usr** | `X:\MARS-Localhost\laragon\usr` |
| **Laragon process** | Running (`laragon.exe`) |
| **PHP (PATH)** | Not on system PATH (`php` not recognized) |
| **PHP (active Apache / profile)** | **8.3.30** ZTS — `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` |
| **PHP (secondary present)** | 8.5.8 NTS — present; **no** loaded `php.ini` when invoked; **not** bound in `mod_php.conf` |
| **Loaded php.ini (8.3)** | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.ini` |
| **MySQL client** | 8.4.3 — `X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysql.exe` (not on PATH) |
| **MySQL server** | 8.4.3 — `mysqld` running from same bin tree |
| **Web server** | **Apache/2.4.66 (Win64)** running (`httpd`) |
| **Nginx** | Binary present (`nginx-1.28.2`); **not** running |
| **Ports observed** | **80** LISTEN; **3306** LISTEN; **443** not listening; **8080** not listening |
| **AutoVirtualHosts** | `0` (manual site mapping expected) |
| **Existing www sites (names)** | `fws-0001`, `mli-smoke-001`, `shpigovsky` (+ `index.php`) |
| **iseo app paths** | `projects\iseo-report-hub\app\` — absent; `X:\MARS-Localhost\iseo-report-hub\` — absent; www/sites iseo entry — absent |

---

## 3. PHP Capability Check

Checked via Laragon PHP **8.3.30** CLI (`php -m`). This is the version referenced by Apache `mod_php.conf` and Laragon profile `default.ini`.

| Extension | Present | MVP relevance |
|-----------|---------|---------------|
| **pdo_mysql** | yes | **Required** — MySQL access via PDO |
| **mysqli** | yes | Useful alternate driver; not mandatory if PDO used |
| **mbstring** | yes | **Required** — UTF-8 / multilingual copy |
| **json** | yes | **Required** — payloads, snapshots, API-shaped data |
| **openssl** | yes | **Required** — HTTPS clients, crypto helpers, secure tokens |
| **fileinfo** | yes | **Required** — evidence upload MIME checks |
| **gd** | yes | Optional — image handling |
| **imagick** | no | Optional — not required for MVP start |
| **curl** | yes | Optional but useful — external HTTP |
| **intl** | yes | Optional but useful — locale/formatting |
| **session** | yes | **Required** — auth sessions |
| **pdo** | yes | **Required** — PDO core |

**Note:** PHP **8.5.8** NTS was probed separately: loaded configuration file `(none)`; most MVP extensions **absent** in that invocation. Treat **8.3.30** as the verified local PHP for Phase 0 planning unless operator deliberately switches Laragon PHP and re-verifies.

---

## 4. Database Capability Check

| Item | Result |
|------|--------|
| Client version | MySQL Community Server client **8.4.3** |
| Server process | `mysqld` listening on **3306** |
| Server connection tested | **Yes** — local client ran only `SELECT VERSION();` |
| Server version (safe) | **8.4.3** |
| Databases listed | **No** (policy) |
| DB `iseo_report_hub_dev` created | **No** |
| DB exists | **SAFE UNKNOWN** |
| Credentials exposed in docs/repo | **No** |
| Destructive DB commands | **None** |

---

## 5. Laragon Layout Assessment

### Option A — `X:\AI MARS\projects\iseo-report-hub\app\`

| Aspect | Assessment |
|--------|------------|
| Pros | Colocated with product docs; single tree for humans browsing the programme |
| Risks | Mixes docs WIP with runtime; foreign monorepo WIP already heavy; accidental commit of runtime artefacts; scheduled jobs must not run from dirty Active Brain |
| Git | Inside shared monorepo — needs strict ignore for `.env*`, uploads, vendor; selective staging discipline |
| Runtime | Would need Laragon DocumentRoot / vhost / junction into `www` or alias — not configured |
| MARS policy fit | Allowed only under explicit charter; weak fit for long-lived runtime/jobs |

### Option B — `X:\MARS-Localhost\iseo-report-hub\`

| Aspect | Assessment |
|--------|------------|
| Pros | Matches MARS Localhost runtime root; keeps dirty Active Brain out of runtime; Laragon already lives under `X:\MARS-Localhost\laragon\` |
| Risks | Needs source↔runtime sync/checkout policy; not created yet |
| Git | Outside Active Brain git tree by default — good for secrets/uploads; docs remain in repo |
| Runtime | Natural neighbor to Laragon; can later map into `www` via junction/vhost under a future charter |
| MARS policy fit | **Strong** for local runtime |

### Option C — Laragon `www` directly

| Aspect | Assessment |
|--------|------------|
| Pros | Native DocumentRoot; existing site pattern uses `www` entries |
| Risks | Runtime code under Laragon tree; less explicit product locus; still needs sync policy vs docs |
| Fit | Acceptable **docroot mount** target later; not preferred as sole source-of-truth for product code |

### Recommendation (Phase 0)

**Phased preference:**

1. Keep **documentation / design SoT** in `X:\AI MARS\projects\iseo-report-hub\`.
2. Prefer **runtime app root** at `X:\MARS-Localhost\iseo-report-hub\` (Option B) after explicit Phase 0 scaffold charter.
3. Optionally expose via Laragon `www` (junction/alias) or dedicated vhost — **only** in a later chartered step (no changes in this preflight).
4. Do **not** run scheduled/runtime jobs from dirty `X:\AI MARS`.
5. Do **not** create Option A `app\` unless operator explicitly chooses Active Brain colocation and ignore/sync rules are approved.

Exact layout remains operator-confirmed at Phase 0 gate.

---

## 6. Local Domain Candidate

| Item | Value |
|------|-------|
| Recommended domain | `iseo-report-hub.test` |
| Alternate | `iseo-report.local` |
| Currently resolves | **No** (DNS/hosts lookup failed for both candidates) |
| Hosts entries for iseo | **None** observed |
| Existing `.test` hosts (unrelated) | `fws-0001.test`, `shpigovsky.test`, `mli-smoke-001.test` |
| Vhost for iseo | **Not present** (sites-enabled has no iseo conf) |
| Vhost/hosts changes this task | **None** |

---

## 7. Local DB Candidate

| Item | Value |
|------|-------|
| Recommended DB name | `iseo_report_hub_dev` |
| Created this task | **No** |
| Exists | **SAFE UNKNOWN** (databases not listed) |

---

## 8. Secrets and Git Ignore

| Topic | Assessment |
|-------|------------|
| Future secrets file | `.env.local` (or `.env`) — **never commit** |
| Future template | `.env.example` with placeholders only |
| Root `.gitignore` | Ignores `.env`, `.env.*`, with exception `!.env.example` |
| `/local/` | Ignored only at **repo root** (`/local/`) — nested `projects/.../local/` **not** covered by that anchor |
| `storage/uploads/` | **No** dedicated ignore rule found |
| `vendor/` | **No** global ignore for PHP Composer vendor |
| If runtime on `X:\MARS-Localhost\...` | Outside Active Brain git — reduces secret/upload leak risk |
| Gaps / recommendations | Before Phase 0 scaffold: confirm runtime location; if any app files live under Active Brain, add scoped ignores for `vendor/`, uploads, and nested env/local paths; keep `.env.example` committed without secrets |

**This task did not edit `.gitignore`.**

---

## 9. Phase 0 Readiness

| Question | Answer |
|----------|--------|
| Ready for scaffold? | **Partial** |
| Hard blockers? | **None** for planning; **scaffold not authorized** until Phase 0 charter + operator inputs below |
| Soft blockers | Domain/vhost not configured; DB not created; PHP/mysql not on PATH; layout choice unconfirmed; sync policy for Option B unconfirmed |

### Required operator inputs before Phase 0 scaffold

1. Confirm runtime layout: **Option B** (`X:\MARS-Localhost\iseo-report-hub\`) vs Option A vs www-only mount.
2. Confirm local domain: `iseo-report-hub.test` (recommended) vs alternate.
3. Authorize (separate charter) vhost/hosts creation — not done here.
4. Authorize (separate charter) DB `iseo_report_hub_dev` creation — not done here.
5. Confirm PHP version pin: **8.3.30** (verified active) vs future switch to 8.5.x after re-preflight.
6. Confirm source/runtime sync policy if Option B (checkout vs copy vs junction).
7. Confirm ignore strategy for any in-repo app paths and upload storage location.
8. Confirm backup location for local DB/uploads under MARS Localhost/Storage policy.

---

## 10. SAFE UNKNOWN

- Whether database name `iseo_report_hub_dev` already exists (databases not listed).
- Whether Apache virtual host DocumentRoot for future iseo site will be `www` junction, `sites\php\...`, or another path.
- Whether operator intends HeidiSQL / phpMyAdmin as primary local DB UI (tools present; usage not verified).
- Whether production hosting path will mirror Laragon layout (out of scope).
- Exact Composer workflow for MVP (Composer installer present on machine; **not** used; not required to start per technical brief).
- Whether PHP 8.5.8 will be activated later (present but unverified for MVP extensions).
- Full contents of Laragon license/private usr files — not inspected beyond non-secret preference keys.
- Remote/HEAD divergence of Active Brain (`ahead 21, behind 62` observed) — foreign to this preflight; no pull/reset performed.
