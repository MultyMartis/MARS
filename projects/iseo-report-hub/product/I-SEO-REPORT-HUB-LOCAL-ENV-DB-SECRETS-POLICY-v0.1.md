# I-SEO Report Hub — Local Env / DB Secrets Policy v0.1

**Status:** POLICY ONLY — no `.env.local` created; no credentials written  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub DB Creation + Schema Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md](I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md), `app-source/.env.example`, `app-source/config/database.example.php`

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Local env / DB secrets **policy** |
| `.env.local` created | **No** |
| `.env` created | **No** |
| Credentials written | **No** |
| DB connected | **No** |

This policy defines how local environment variables and DB secrets must be handled. It does **not** create env files or record real passwords.

---

## 2. Env File Policy

| File | Policy |
|------|--------|
| `.env.example` | **Committed** template with placeholders only |
| `.env.local` | **Local-only**, Git-ignored; holds real local values |
| `.env` | **Forbidden** unless separately approved; prefer `.env.local` for local overrides |
| Reports / commits | **Never** paste real credentials, connection strings with passwords, or dumps containing secrets |

Sync policy reminder: source → runtime must **not** overwrite runtime `.env` / `.env.local`.

---

## 3. Candidate Env Values

Placeholders only (aligned with current `app-source/.env.example`):

```env
APP_ENV=local
APP_DEBUG=true
APP_URL=http://iseo-report-hub.test

DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=iseo_report_hub_dev
DB_USERNAME=CHANGE_ME
DB_PASSWORD=CHANGE_ME
```

Additional non-secret path hints may exist in `.env.example` (`UPLOAD_PATH`, `LOG_PATH`). Do not invent production URLs or real usernames in documentation.

---

## 4. Storage Location

| Location | Assessment |
|----------|------------|
| `app-source/.env.local` | Technically ignorable via `.gitignore`, but **risky** — lives inside the monorepo tree; easy to stage by mistake if ignore gaps appear |
| Runtime `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\.env.local` | **Local runtime only**; outside Active Brain Git; matches Model A deploy target |
| **Recommended** | **Runtime `.env.local` only** for local execution; Active Brain keeps **`.env.example`** (and config examples) as SoT templates |

Future app loaders should look for runtime-local env without requiring secrets in Git.

---

## 5. Git Ignore Requirement

### Observed (this charter wave)

| Layer | Patterns relevant to env |
|-------|--------------------------|
| Repo root `.gitignore` | `.env`, `.env.*`, `!.env.example` |
| `app-source/.gitignore` | `.env`, `.env.local` |

### Assessment

- Root ignore covers broad `.env.*` with example exception — good for monorepo.
- `app-source/.gitignore` protects `.env` and `.env.local` explicitly.
- **Gap (document only; do not edit in this task):** `app-source/.gitignore` does **not** list a general `.env.*` pattern (e.g. `.env.production`, `.env.backup`). Root ignore may still protect if those files are considered from repo root; behavior for nested paths should be **re-verified** in a future ignore hygiene charter before creating additional env filenames.

**Do not change `.gitignore` in this wave.**

---

## 6. Reporting Policy

| Rule | Statement |
|------|-----------|
| Credentials | Do **not** record actual DB username/password in reports |
| Connection evidence | Report only **PASS** / **FAIL** (and redacted error class if useful) |
| Logs | Redact credentials from app logs and CLI output before pasting into Active Brain |
| Screenshots | Crop or blur env editors if they show secrets |

---

## 7. SAFE UNKNOWN

- Exact PHP env loader mechanism in Phase 1A+ (getenv vs dotenv library) — not required for this policy wave.
- Whether Windows/Laragon process identity affects file ACL on runtime `.env.local`.
- Final MySQL username string for local app user (must remain `CHANGE_ME` in Git until local-only create).
