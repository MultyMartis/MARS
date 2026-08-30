# I-SEO Report Hub — Demo User «Тест Проверочнов» Plan v0.1

**Status:** planning only — **no user creation in this wave**  
**Date:** 2026-08-21  
**Wave:** Pre-hosting Demo Scenario and Field Help Charter 01  
**Local DB target (future):** `iseo_report_hub_dev` @ `127.0.0.1:3306`

---

## Operator identity inputs (hard)

| Field | Operator value |
|-------|----------------|
| **Display name** | `Тест Проверочнов` |
| **Login requested** | `test` |
| **Password** | `test` (local/demo only) |
| **Intended role** | SEO specialist who authors reports |

---

## Auth model findings (from source + DB read-only)

| Topic | Finding |
|-------|---------|
| **Login field** | Auth uses **email**, not a separate username/login column |
| **UI** | `/login` form: `<input type="email" name="email">` — browsers enforce email format |
| **Lookup** | `AuthService::login()` selects `users` by `email` (lowercased/trimmed) |
| **Password** | Stored as `password_hash`; verified with `password_verify`; created via `password_hash(..., PASSWORD_DEFAULT)` in `tools/create-local-admin.php` |
| **Roles** | `roles.code` + `user_roles`; internal login requires at least one of: `admin_owner`, `seo_lead_reviewer`, `seo_specialist`, `account_client_manager`, `internal_viewer` |
| **Exact SEO worker role key** | **`seo_specialist`** (`SEO Specialist` — report authoring and weekly work) |
| **Bare login `test`** | **Not sufficient** as email credential: HTML5 `type="email"` + `FILTER_VALIDATE_EMAIL` patterns reject bare `test` |

### Existing local users (read-only probe 2026-08-21)

| id | name | email | status |
|----|------|-------|--------|
| 1 | Local Admin | `admin@iseo-report-hub.test` | active |
| 2 | Polygon WS Local Test | `polygon-ws@mail.ru` | active |

No `test` / `Тест Проверочнов` user yet.

Roles present: `admin_owner`, `seo_lead_reviewer`, **`seo_specialist`**, `account_client_manager`, `internal_viewer`, `client_viewer`.

---

## Recommended credential mapping for implementation

| Product field | Recommended value | Notes |
|---------------|-------------------|-------|
| `users.name` | `Тест Проверочнов` | Exact operator display name |
| `users.email` | `test@reports.i-seo.local` | Valid local placeholder email; **required** for login form |
| Visible “login” story for team | Explain that the app authenticates by **email**; operator’s word `test` maps to this email | Do **not** invent a username column in this wave |
| Password | `test` | Local/demo only; never for production host |
| Role | `seo_specialist` | Exact DB/app role code |
| Status | `active` | |

Optional future UX (out of scope now): allow display of a short login alias — **not** present today.

---

## Creation method (future implementation wave)

1. **Backup** `iseo_report_hub_dev` first (mysqldump or approved backup path under Storage).
2. Prefer a **controlled CLI helper** patterned after `tools/create-local-admin.php`:
   - refuse non-local DB name;
   - refuse if email exists;
   - assign role `seo_specialist` (not `admin_owner`);
   - password via env or hidden prompt — **never argv commit**;
   - never print password or hash.
3. Alternative: extend admin tool with `--role=seo_specialist` — only in an authorized implementation charter.
4. **Do not** create the user via ad-hoc SQL pasted into chat with hashes.

---

## Permissions expected for demo

With `seo_specialist`, the user should be able to (per current services):

- create/edit reporting periods (within specialist create roles);
- create/edit monthly report content, work entries, report blocks;
- use preview / assembly flows;
- **not** be treated as full `admin_owner` for reopen/admin-only paths.

If a future UI action requires admin, document the gap and either assign a second local admin session or escalate — do not silently elevate `test`.

---

## Safety

- Local DB only; **no** host user with password `test`
- Backup before insert; rollback = restore backup
- Do not print `password_hash`, session cookies, or `.env`
- If this DB is ever uploaded to host, **password policy must be revisited** before go-live (force rotate / disable weak demo accounts)
- Do not reuse this credential on production

---

## Acceptance for this plan doc

- Role key identified: `seo_specialist`
- Email/login mismatch documented with safe placeholder email
- Hasher path identified (`password_hash` / `password_verify`)
- Implementation deferred to DB-backed seed wave with backup
