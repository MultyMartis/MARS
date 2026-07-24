# I-SEO Report Hub — MVP Phase 1B Runtime Sync Result v0.1

**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Wave:** MVP Phase 1B Source → Runtime Sync + Local Smoke 01

---

## 1. Status

- **Phase 1B complete**
- **source → runtime sync performed** (allowlist copy only)
- **Runtime path:** `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- **Source path:** `X:\AI MARS\projects\iseo-report-hub\app-source\`
- **No DB** — no creation, no connection, no SQL
- **No vhost/hosts** — not configured
- **No secrets** — no `.env` / `.env.local` created

---

## 2. Sync Summary

| Field | Value |
|-------|-------|
| Source path | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Sync direction | **source → runtime** |
| Method | Allowlist `Copy-Item` (exact relative paths); no wipe / no mirror delete |
| Copied files count | **44** |
| Failed / missing | **0** |
| Optional `docs/SOURCE-RUNTIME-POLICY.md` | Present and copied |

---

## 3. Runtime State

- Phase 1A app skeleton **now present** in Localhost runtime
- Front controller: `public/index.php`
- Bootstrap / router / views / controllers / services: present under `app/`
- Public assets: `public/assets/css/app.css`, `public/assets/js/app.js`
- Config examples only (`config/*.example.php`); no live DB config
- **No DB**
- **No `.env.local`**

---

## 4. Smoke Tests

| Test | Result |
|------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` (PHP 8.3.30) |
| `php -l` (25 runtime PHP files) | **PASS** — 0 syntax errors |
| CLI route smoke `/`, `/health`, `/login`, `/not-existing` | **PASS** — 200 / 200 / 200 / 404 |
| Built-in server `127.0.0.1:8088` | **PASS** — same status codes; process stopped after smoke |
| DB | **Not tested** (out of scope) |

---

## 5. What Still Does Not Exist

- DB (`iseo_report_hub_dev` candidate not created)
- Real users
- Real auth persistence
- Migrations
- vhost / hosts mapping for `iseo-report-hub.test`
- `.env.local`
- Reports CRUD
- Client publishing

---

## 6. Security Notes

- No secrets introduced
- `.env` / `.env.local` absent in source and runtime
- No DB mutation
- Runtime generated dirs (`storage/logs`, `storage/uploads`, `storage/cache`) preserved; non-`.keep` payloads remain empty
- No upload / log / cache payloads created by this task
- No nested `.git`, `vendor/`, or `node_modules/` in runtime

---

## 7. Next Phase

**Recommended next action (one only):**

**Local vhost/hosts mapping charter for `iseo-report-hub.test`**

Rationale: Phase 1A skeleton is now in runtime and local smoke via PHP built-in server succeeded without DB. Domain mapping is the natural next local-access step before DB/auth charters. DB creation remains a separate explicit charter.

---

## 8. SAFE UNKNOWN

- Whether Laragon auto-vhost for the sites path already covers this folder without manual hosts (not probed in this wave)
- Operator preference for exact Apache vhost template contents when chartered
- When `.env.local` will first be introduced (DB charter vs auth charter)
