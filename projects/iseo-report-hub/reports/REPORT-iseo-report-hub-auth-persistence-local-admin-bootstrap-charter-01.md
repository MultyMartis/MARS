# REPORT — I-SEO REPORT HUB AUTH PERSISTENCE + LOCAL ADMIN BOOTSTRAP CHARTER 01

**project_id:** `iseo-report-hub`  
**Wave:** Auth Persistence + Local Admin Bootstrap Charter 01  
**Date:** 2026-07-24  
**Type:** documentation / policy only  

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-commit) | `1433bcb790ae38d0b7fac215245da21ceb175a44` |
| Staged / index (pre-write) | **Empty** |
| Foreign WIP | **Preserved** (not staged, not restored, not cleaned) |
| Write scope | Active Brain i-SEO Report Hub docs only (6 allowlisted paths) |
| App-source edits | **None** |
| Runtime edits | **None** |
| DB / SQL | **None** |

---

## 2. Docs Reviewed

Product / reports:

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `product/I-SEO-REPORT-HUB-MVP-PHASE-1A-APP-SKELETON-RESULT-v0.1.md`
- `product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md`
- `product/I-SEO-REPORT-HUB-LOCAL-HOSTS-RESMOKE-RESULT-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-CREATION-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md`
- `product/I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md`
- `product/I-SEO-REPORT-HUB-DB-01-DB-02-MIGRATION-APPLY-RESULT-v0.1.md`
- `reports/REPORT-iseo-report-hub-db-creation-db01-db02-migration-files-apply-01.md`
- `AGENTS.md` / `.cursorrules` (session authority)

App-source (read-only):

- `app/Services/AuthService.php` — stub login
- `app/Services/ConfigService.php`
- `app/Services/CsrfService.php`
- `app/Controllers/AuthController.php`
- `app/Controllers/HealthController.php`
- `app/bootstrap.php`
- `app/routes.php`
- `tools/db-migrate.php` (inspected as prior tool pattern authority via programme docs / path existence)
- `database/migrations/2026_07_24_000001_create_core_tables.sql`

App-source safety: no `.env` / `.env.local`, no nested `.git`, no `vendor/`, no `node_modules/`.

Runtime path confirmed present (not modified):  
`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`

---

## 3. Current DB/Auth State

| Fact | State |
|------|-------|
| DB `iseo_report_hub_dev` | **Exists** (attested) |
| First migration | **Applied** — `2026_07_24_000001_create_core_tables.sql` |
| Checksum | `71dd22d0a0a0af14854b4b40d72ae611c80d74af8bfe038a413110b0be722bb4` |
| Tables | `schema_migrations`, `users`, `roles`, `user_roles`, `audit_log`, `clients`, `projects`, `sites`, `project_type_profiles` |
| Roles count | **6** (attested) |
| Users count | **0** (attested) |
| Auth | **Stub** — `AuthService::login()` → `not_implemented` |
| `/health` DB probe | Still Phase 1A static note (unchanged this wave) |

No SQL re-check executed in this charter wave (forbidden by wave restrictions); counts taken from DB-01/DB-02 apply attestation.

---

## 4. Auth Persistence Charter Summary

Document: `product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md`

- **Login flow:** GET form → POST + CSRF → normalize email → active user query → `password_verify` → load roles → session payload → `last_login_at` → audit → redirect dashboard.
- **Logout:** clear auth session keys → audit `auth.logout` → `/login`.
- **Session:** regenerate ID on login; store `user_id` / email / name / roles / `authenticated_at`; never store password hash; no remember-me / OAuth in MVP.
- **Password:** `PASSWORD_DEFAULT` hash only; 12+ recommended; no plaintext in Git/logs/reports.
- **Roles:** dashboard = internal roles except `client_viewer`; admin tools = `admin_owner`; client portal separate.
- **Audit:** `auth.login.success` / `auth.login.failed` / `auth.logout` / `auth.bootstrap.admin_created` (+ later password change).

---

## 5. Local Admin Bootstrap Policy Summary

Document: `product/I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md`

- **Future tool:** `app-source/tools/create-local-admin.php` → sync to runtime `tools/`.
- **Inputs:** name, email, password via hidden prompt or local-only env (never shell-history argv).
- **Idempotency:** refuse existing `admin_owner` without `--confirm-existing`; no silent duplicates.
- **Security:** `password_hash`; no seed password file; no production identity assumption.
- **Audit:** `auth.bootstrap.admin_created` with safe metadata only.
- **Validation:** users/role assignment, UI login/logout, failed-login audit.

---

## 6. DB Health Policy Summary

Document: `product/I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md`

- **Future service:** `app/Services/DatabaseService.php` (PDO).
- **Tool guard:** refuse non-`iseo_report_hub_dev` for local migration/admin tools.
- **Allowed health fields:** configured yes/no; connection pass/fail; DB name; migration count; latest migration; tables count.
- **Forbidden:** username/password; DSN with password; stack traces / full SQL errors in non-debug.
- **Failure:** degraded health, not app-wide fatal; safe log summary only.

---

## 7. Implementation Plan Summary

Document: `product/I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md`

- **Next wave name:** `I-SEO Report Hub — Auth Persistence + Local Admin Bootstrap Implementation 01`
- **Source files:** Auth/Config/Csrf/Health/Dashboard controllers + services, login/health views, optional `DatabaseService`, new `create-local-admin.php`
- **Runtime sync:** source-first; allowlist sync; keep `.env.local` runtime-only
- **DB actions allowed later:** one local admin + login timestamps + audit events
- **Tests:** lint, DB smoke, bootstrap, login success/fail, dashboard, logout, health DB status, counts/audits

---

## 8. Validation

| Restriction | Result |
|-------------|--------|
| No app-source code edits | **PASS** |
| No runtime edits | **PASS** |
| No DB mutation | **PASS** |
| No SQL | **PASS** |
| No admin user | **PASS** |
| No password / hash generated | **PASS** |
| No `.env` / `.env.local` changes | **PASS** |
| No credentials in docs | **PASS** |
| No source → runtime sync | **PASS** |
| No WordPress | **PASS** |
| No Composer / npm | **PASS** |
| No vhost / hosts / service restart | **PASS** |
| No demo / registry changes | **PASS** |
| No push / fetch / pull / reset / clean / stash | **PASS** (commit only, after docs) |

---

## 9. Commit

| Field | Value |
|-------|--------|
| Exact-path `git add` | **Yes** (6 Active Brain docs) |
| Commit | **Yes** — `docs(iseo-report-hub): add auth bootstrap charter` |
| Commit hash | *(filled after commit)* |
| Push | **No** |

Staged allowlist:

1. `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
2. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md`
3. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md`
4. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md`
5. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md`
6. `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-charter-01.md`

---

## 10. SAFE UNKNOWN

| Item | Note |
|------|------|
| Live users/roles re-count at charter time | Not re-queried (no SQL this wave); attested DB-01/DB-02 apply counts used |
| Operator-chosen local admin email/password | Deferred to implementation wave |
| Exact logout method (GET vs POST+CSRF) | Deferred |
| Exact `/health` HTTP code when DB down | Deferred (200+degraded vs 503) |
| Branch divergence vs `origin` | Local branch was ahead/behind remote before this commit; no pull/push performed |

---

## 11. Recommended Next Action

**Auth Persistence + Local Admin Bootstrap Implementation 01**

---

## 12. Files Changed

1. `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
2. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md`
3. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md`
4. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md`
5. `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md`
6. `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-auth-persistence-local-admin-bootstrap-charter-01.md`

---

## 13. Git Actions

| Action | Done |
|--------|------|
| Exact-path `git add` | **yes** |
| Commit | **yes** (after staging verification) |
| Push | **no** |
| Fetch | **no** |
| Pull | **no** |
| Checkout | **no** |
| Reset | **no** |
| Restore | **no** |
| Clean | **no** |
| Stash | **no** |
