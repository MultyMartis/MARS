# I-SEO Report Hub — Local Admin Bootstrap Policy v0.1

**Status:** POLICY ONLY — no admin user created; no password generated; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub Auth Persistence + Local Admin Bootstrap Charter 01  
**Related:** [I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-AUTH-PERSISTENCE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md](I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Local admin bootstrap **policy** only |
| Admin user created | **No** |
| Password generated | **No** |
| Password hash created | **No** |
| DB mutation | **No** |
| Bootstrap tool exists | **No** (planned for implementation wave) |

This policy defines how the **next** implementation wave may create exactly one local `admin_owner` for `iseo_report_hub_dev`. It does **not** authorize running bootstrap now.

---

## 2. Objective

Create **exactly one** local admin user for dev/test so that:

- UI login can be validated end-to-end;
- role `admin_owner` is assigned;
- audit records bootstrap;
- no production identity is assumed;
- no seed file with plaintext password enters Git.

---

## 3. Bootstrap Tool

| Location | Path |
|----------|------|
| Future source tool | `projects/iseo-report-hub/app-source/tools/create-local-admin.php` |
| Runtime after sync | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\create-local-admin.php` |

Rules:

- CLI only (same family as `db-migrate.php`);
- refuse HTTP invocation;
- use PDO via future `DatabaseService` or shared DB helper;
- strict local DB name guard for tools: target must be `iseo_report_hub_dev` unless a later charter expands environments;
- load credentials from runtime `.env.local` only — never print them.

---

## 4. Inputs

Required future inputs:

| Input | Notes |
|-------|-------|
| `name` | Display name |
| `email` | Unique; normalized (trim + lowercase) |
| `password` | From secure hidden prompt **or** local-only env variable |
| Role | Fixed: `admin_owner` |

Password handling rules:

- **never** pass password as a command-line argument if the shell records history;
- prefer interactive hidden prompt when available;
- if using an env var, it must be **local-only**, unset after use when practical, and **never** written into reports/Git;
- do not echo password or hash in tool output.

---

## 5. Idempotency

The tool must:

| Condition | Behavior |
|-----------|----------|
| Another `admin_owner` already exists | **Refuse** unless explicit `--confirm-existing` (or equivalent) is provided by operator |
| Same email already exists | Update / re-hash only with **explicit** operator approval flag |
| Silent duplicate admin | **Forbidden** |
| Users table empty | Allow create of first admin |

Default stance: one local admin bootstrap is intentional and rare; re-runs are HITL.

---

## 6. Security

| Rule | Statement |
|------|-----------|
| Hash | `password_hash($password, PASSWORD_DEFAULT)` |
| Plaintext | Not logged, not audited, not committed |
| Reports | May show email only if operator approves; otherwise redact (e.g. `a***@example.local`) |
| Seed files | No password-bearing seed SQL/JSON in Git |
| Identity | Local/dev only — not a production identity assumption |
| Status | Created user must be `active` |

---

## 7. Audit

On successful create, insert `audit_log` event:

- `event_type`: `auth.bootstrap.admin_created`
- `actor_user_id`: the new user id (or null if FK timing requires post-insert update — prefer set to new user)
- `entity_type` / `entity_id`: `user` / new id
- `metadata_json`: safe flags only, e.g. `{ "role": "admin_owner", "local_bootstrap": true }` — **no password**

---

## 8. Validation

After a future bootstrap (implementation wave), verify:

1. `users` count is the expected non-zero local count (typically **1** on first bootstrap).
2. `user_roles` links the user to `admin_owner`.
3. UI login with the chosen credentials succeeds.
4. Logout clears session and returns to login.
5. Failed login is audited as `auth.login.failed`.
6. Successful login is audited as `auth.login.success`.
7. No plaintext password appears in logs, reports, or health output.

---

## 9. SAFE UNKNOWN

| Item | Why unknown |
|------|-------------|
| Exact CLI flag names | Deferred to implementation (`--confirm-existing`, prompt library choice) |
| Whether Windows PHP can use interactive hidden prompt without extra deps | Must be verified in implementation wave; env-var fallback remains allowed under local-only rules |
| Exact admin email chosen by operator | Not decided in this policy wave |
| Whether a second local non-admin user will be needed soon | Out of scope |
