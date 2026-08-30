# I-SEO Report Hub — Demo User Seed Spec v0.1

**Status:** seed design only — **no user creation in this wave**  
**Date:** 2026-08-21  
**Wave:** Demo User and Scenario Seed Charter 01  
**Implementation wave:** `I-SEO Report Hub — Demo User and Scenario Seed Implementation 01`

---

## 1. Credential mapping (operator inputs preserved)

| Field | Value | Notes |
|-------|-------|-------|
| Visible name | `Тест Проверочнов` | Exact operator spelling → `users.name` |
| Auth email / login | `test@reports.i-seo.local` | Required by current auth model |
| Operator shorthand | `test` | Human label only — **not** a DB username |
| Password | `test` | Local/demo only |
| Role key | `seo_specialist` | Exact `roles.code` |
| Status | `active` | `users.status` ENUM |

---

## 2. Auth model constraints

- Login form uses `type="email"`; bare `test` is rejected.
- Lookup is by lowercased/trimmed **email**.
- Password stored as `password_hash`; verify with `password_verify`.
- Seed must hash with PHP `password_hash($password, PASSWORD_DEFAULT)` consistent with `tools/create-local-admin.php`.
- **Never** print password, hash, session cookies, or tokens in docs, CLI stdout beyond success messages, or evidence JSON.

---

## 3. Local / demo markers

Schema has **no** dedicated `is_demo` user column. Use layered markers:

| Layer | Value |
|-------|-------|
| Email domain | `@reports.i-seo.local` |
| Evidence file | `demo-proverka-ids.json` → `user_id` |
| Audit event (recommended) | `demo_proverka.user_seeded` with metadata `{ "marker": "MARS_DEMO_PROVERKA_20260821" }` (no secrets) |
| Notes elsewhere | Client/project notes carry the same marker |

---

## 4. Idempotency rules

| Case | Action |
|------|--------|
| Email absent | Create user + assign `seo_specialist` only |
| Email exists **and** evidence/marker confirms local demo (`test@reports.i-seo.local` + marker in evidence or audit) | Allow update of `name`, role set (`seo_specialist`), password — only with `--confirm-local-demo-seed` |
| Email exists and is **not** the known demo email / unknown real user | **Refuse** — do not overwrite |
| User has unexpected roles (e.g. only `admin_owner` on a different email) | Out of scope — do not touch |
| Role `seo_specialist` missing from `roles` table | **STOP** — schema broken |

Do not assign `admin_owner` to the demo user.

---

## 5. Permissions expected

With `seo_specialist`, demo user should be able to:

- Edit monthly content, work entries, report blocks (non-finalized)
- Submit for review
- Use preview / assembly preview
- Own reporting periods as `owner_user_id` when seeded

Cannot (by design):

- Finalize / mark reviewed (needs lead/admin)
- Reopen finalized (admin only)
- Manage other users

If browser fill needs finalize for July, use Local Admin session **or** seed-set July status without UI finalize (see Data Spec).

---

## 6. Password safety

**WARNING:** password `test` is **local/demo only**.

Before any host upload / production:

1. Disable or delete this user **or**
2. Force rotate to a strong password **and**
3. Confirm it never appears in host dumps as an active weak account

Do not reuse this credential on `reports.i-seo.su`.

---

## 7. Rollback / cleanup

| Path | Method |
|------|--------|
| Preferred | Restore mysqldump backup taken before seed |
| Exact-id cleanup | `--cleanup` deletes **only** IDs listed in `demo-proverka-ids.json` for this marker (user role row + user if still marker-matched) |
| Forbidden | Broad `DELETE FROM users`; touching admin / polygon users; cleanup without backup |

---

## 8. Acceptance (user portion)

- Login succeeds at `/login` with email `test@reports.i-seo.local` / password `test`
- Session shows name `Тест Проверочнов`
- Role includes `seo_specialist`
- No password/hash printed in evidence
- Existing users 1 and 2 unchanged except incidental `last_login_at` if admin used separately
