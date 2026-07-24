# I-SEO Report Hub — Auth Persistence Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no code changed; no DB mutation; no admin user created  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub Auth Persistence + Local Admin Bootstrap Charter 01  
**Related:** [I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md](I-SEO-REPORT-HUB-LOCAL-ADMIN-BOOTSTRAP-POLICY-v0.1.md), [I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md](I-SEO-REPORT-HUB-DB-CONNECTION-HEALTH-POLICY-v0.1.md), [I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-01-DB-02-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-01-DB-02-MIGRATION-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-ROLE-AND-PERMISSION-MODEL-v0.1.md](I-SEO-REPORT-HUB-ROLE-AND-PERMISSION-MODEL-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Auth persistence **charter / planning** only |
| App-source code changed | **No** |
| Runtime code changed | **No** |
| DB mutation | **No** |
| Admin user created | **No** |
| Current login | **Stub** — `AuthService::login()` returns `not_implemented` |
| Auth tables | **Exist** (`users`, `roles`, `user_roles`, `audit_log`) via first migration |
| Users count | **0** (attested by DB-01/DB-02 apply result) |
| Roles count | **6** (attested by DB-01/DB-02 apply result) |

This charter defines how stub login becomes DB-backed authentication. It does **not** authorize implementation, bootstrap, or secret entry in this wave.

---

## 2. Objective

Convert Phase 1A stub auth into a local DB-backed login baseline that:

- authenticates against `users.password_hash` via PHP `password_verify`;
- stores password only as `password_hash` (via `password_hash` / `PASSWORD_DEFAULT`);
- loads roles from `roles` + `user_roles`;
- stores a **minimal** session user payload (no password hash);
- enables later protection of internal routes (dashboard / admin tools);
- keeps **client public publishing** (token URLs / published snapshots) **separate** from internal session auth.

Out of MVP for this auth layer:

- OAuth / SSO / external IdP;
- remember-me cookies;
- multi-factor auth;
- password reset email flows;
- real client portal login for `client_viewer` (future boundary only).

---

## 3. Current Tables

| Table | Role in auth |
|-------|----------------|
| `users` | Identity: email, `password_hash`, status, `last_login_at` |
| `roles` | Role catalog (`code`, `name`, `description`) |
| `user_roles` | Many-to-many assignment user ↔ role |
| `audit_log` | Auth and bootstrap events (no secrets in metadata) |

Attested DB state (DB-01/DB-02 apply, no mutation in this wave):

| Check | Value |
|-------|-------|
| DB | `iseo_report_hub_dev` |
| Roles seed | **6** rows |
| Users | **0** rows |
| First migration checksum | `71dd22d0a0a0af14854b4b40d72ae611c80d74af8bfe038a413110b0be722bb4` |

Seeded role codes (from migration):

- `admin_owner`
- `seo_lead_reviewer`
- `seo_specialist`
- `account_client_manager`
- `internal_viewer`
- `client_viewer`

---

## 4. Auth Flow

### Login (proposed)

1. `GET /login` renders the login form (CSRF field present).
2. `POST /login` validates CSRF (`CsrfService`).
3. Normalize email (trim + lowercase).
4. Query **active** user by email (`status = 'active'`).
5. Verify password with `password_verify($password, $user.password_hash)`.
6. Load role codes for the user via `user_roles` + `roles`.
7. Store session payload (see Session Policy).
8. Update `users.last_login_at`.
9. Write audit event `auth.login.success` or `auth.login.failed` (never log password / hash).
10. On success: regenerate session ID, then redirect to dashboard (`/`).

Failed login must:

- not reveal whether email exists (generic message);
- still audit `auth.login.failed` with safe metadata only (e.g. normalized email hash or truncated email only if operator policy later allows — default: email present only when useful and non-secret);
- not create a session user payload.

### Logout (proposed)

1. Clear session auth keys.
2. Audit `auth.logout` when a prior authenticated user existed.
3. Redirect to `/login`.

---

## 5. Session Policy

| Rule | Statement |
|------|-----------|
| Session name | Keep existing `iseo_report_hub_session` unless a later security charter changes it |
| Auth keys (proposed) | `auth_user_id`, `auth_email`, `auth_name`, `auth_roles` (array of role codes), `auth_authenticated_at` |
| Legacy stub keys | Remove / stop using `auth_demo_flag` and placeholder `auth_user` once real auth ships |
| Login | Call `session_regenerate_id(true)` after successful authentication |
| Logout | Unset auth keys; do not leave partial auth state |
| Forbidden in session | Password, password hash, CSRF secrets beyond existing token pattern, DB credentials |
| Remember-me | **Not** in MVP |
| OAuth | **Not** in MVP |

Minimal session user payload example (conceptual):

```text
user_id, email, name, roles[], authenticated_at
```

---

## 6. Password Policy

| Rule | Statement |
|------|-----------|
| Entry | Local admin password entered only through a **local secure prompt** (or local-only env var per bootstrap policy) |
| Storage | Only `users.password_hash` via `password_hash(..., PASSWORD_DEFAULT)` |
| Verify | `password_verify` only |
| Plaintext | Never in Git, reports, logs, audit metadata, flash messages, or health output |
| Minimum length | Recommended **12+** characters for local admin |
| Complexity | Operator-chosen; no weak hardcoded default password in source |
| Reset | Out of scope for this charter wave / MVP auth baseline |

---

## 7. Role Policy

Use existing seeded roles. MVP internal route access baseline:

| Surface | Allowed roles |
|---------|----------------|
| Dashboard (`/`) | Any **internal** authenticated role **except** `client_viewer` |
| Admin tools (future) | `admin_owner` only |
| `client_viewer` | Future public/client portal boundary — **not** used for internal admin in MVP auth |

Internal roles for dashboard MVP:

- `admin_owner`
- `seo_lead_reviewer`
- `seo_specialist`
- `account_client_manager`
- `internal_viewer`

Unauthenticated users hitting protected internal routes must be redirected to `/login`. Exact middleware shape is deferred to the implementation wave (controller guard vs shared helper).

Client public publishing (token URL / published snapshots) remains **outside** this session auth model.

---

## 8. Audit Policy

| Event | When |
|-------|------|
| `auth.login.success` | Successful DB-backed login |
| `auth.login.failed` | Failed login attempt (bad credentials / inactive / missing user) |
| `auth.logout` | Explicit logout of an authenticated session |
| `auth.bootstrap.admin_created` | Local admin bootstrap tool creates the first admin |
| `auth.password.changed` | Later (not required for first auth implementation wave) |

Audit rules:

- do **not** log password or password hash;
- metadata may include role codes, user id (after success), IP/user-agent columns already on `audit_log`;
- failed login may omit actor_user_id when no user resolved.

---

## 9. SAFE UNKNOWN

| Item | Why unknown |
|------|-------------|
| Exact flash / error copy for UI | Not fixed until implementation wave |
| Whether failed-login audit stores email plaintext vs redacted form | Deferred; must not leak secrets either way |
| Exact route-guard helper API | Not designed beyond role baseline |
| Production auth hardening (HTTPS-only cookies, HSTS, lockout) | Local MVP first; production not in this charter |
| Live re-count of users/roles at charter write time | Not re-queried in this wave (no SQL); attested counts from DB-01/DB-02 apply result remain authority unless a later read-only check updates them |
