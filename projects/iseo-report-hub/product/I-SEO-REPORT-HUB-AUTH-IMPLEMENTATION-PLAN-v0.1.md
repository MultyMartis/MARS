# I-SEO Report Hub — Auth Implementation Plan v0.1

**Status:** PLAN ONLY — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub Auth Persistence + Local Admin Bootstrap Charter 01  
**Related:** [I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md](I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md), [I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md](I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md), [I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md](I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Implementation **plan** only |
| Code changed this wave | **No** |
| DB mutated this wave | **No** |
| Admin created this wave | **No** |

This plan names the next controlled implementation wave and its boundaries. Execution requires a separate operator charter.

---

## 2. Proposed Next Wave

**Name:** `I-SEO Report Hub — Auth Persistence + Local Admin Bootstrap Implementation 01`

Scope (future):

1. DB-backed login/logout replacing stub `AuthService`.
2. Local admin bootstrap CLI tool.
3. Safe DB status on `/health`.
4. Role-aware dashboard gate (internal roles; exclude `client_viewer`).
5. Source-first edits + allowlist sync to Localhost runtime.
6. Smoke tests listed below.

---

## 3. Source Files To Change

Likely Active Brain source paths under `projects/iseo-report-hub/app-source/`:

| Path | Purpose |
|------|---------|
| `app/bootstrap.php` | Wire `DatabaseService`; stop claiming “no DB” |
| `app/Services/ConfigService.php` | Mark DB configured when env is real; auth flags |
| `app/Services/AuthService.php` | Real login/logout/session/roles |
| `app/Services/CsrfService.php` | Keep CSRF; minor adjustments if needed |
| `app/Controllers/AuthController.php` | Success/fail redirects; remove stub messaging |
| `app/Controllers/DashboardController.php` | Require authenticated internal role |
| `app/Controllers/HealthController.php` | Safe DB status fields |
| `app/Support/Response.php` | Only if redirect/status helpers need tweaks |
| `app/Views/pages/login.php` | Remove “not implemented” warning when live |
| `app/Views/pages/health.php` | Render safe DB fields |
| `tools/create-local-admin.php` | **New** bootstrap CLI |
| `app/Services/DatabaseService.php` | **Optional/new** shared PDO service |
| `app/routes.php` | Only if guard wiring requires it |

Do **not** invent migrations for auth tables — they already exist.

---

## 4. Runtime Sync

Implementation wave must:

1. Edit **source first** (`app-source/`).
2. PHP lint changed files.
3. Sync **allowlisted** changed source files to  
   `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` per Deploy/Sync Policy.
4. Keep runtime `.env.local` **local-only** (outside Git).
5. Never create `app-source/.env.local`.
6. Not wipe runtime; not sync vendor/node_modules/dumps.

---

## 5. DB Actions

Implementation wave **may**:

- insert **one** local admin user (+ `user_roles` for `admin_owner`);
- update `last_login_at` on successful login;
- insert audit events (`auth.*`).

Implementation wave **must not**:

- create production data;
- dump DB into Git;
- create real client/org/project rows unless a separate charter says so;
- broaden schema beyond existing auth tables without a migration charter.

---

## 6. Tests

Required smoke for the implementation wave:

| # | Test |
|---|------|
| 1 | PHP lint on changed source files |
| 2 | CLI DB connection smoke (no credential print) |
| 3 | Local admin bootstrap smoke (idempotent refusal on re-run) |
| 4 | `GET /login` → 200 |
| 5 | `POST /login` success → session + redirect dashboard |
| 6 | `GET /` authenticated dashboard |
| 7 | Logout → session cleared + login |
| 8 | Failed login → generic error + audit |
| 9 | `/health` shows safe DB status |
| 10 | Users count expected after bootstrap |
| 11 | Audit events expected (`auth.bootstrap.admin_created`, login success/fail, logout) |

---

## 7. Rollback / Recovery

| Case | Action |
|------|--------|
| App login broken after deploy | Fix source and re-sync; do **not** destructive DB reset |
| Bad admin password | Re-run bootstrap update path with explicit approval; or disable user later via explicit command (not invented here) |
| Keep DB user | Prefer keep user row; disable only with explicit future command |
| Code rollback | Git commit of prior stub remains recoverable; runtime resync from source |
| Forbidden | Broad `DROP DATABASE`, `git clean`, wiping `.env.local` without operator intent |

---

## 8. SAFE UNKNOWN

| Item | Why unknown |
|------|-------------|
| Exact effort split across commits inside the implementation wave | Operator preference |
| Whether logout stays `GET /logout` or moves to POST | Security preference deferred (CSRF on logout) |
| Rate limiting / lockout thresholds | Not specified for local MVP |
| Whether health DB probe runs on every request or cached briefly | Deferred |
