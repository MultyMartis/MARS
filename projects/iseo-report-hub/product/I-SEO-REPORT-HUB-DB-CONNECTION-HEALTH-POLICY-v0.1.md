# I-SEO Report Hub — DB Connection / Health Policy v0.1

**Status:** POLICY ONLY — no app health code changed  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator I-SEO Report Hub Auth Persistence + Local Admin Bootstrap Charter 01  
**Related:** [I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-AUTH-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md](I-SEO-REPORT-HUB-LOCAL-ENV-DB-SECRETS-POLICY-v0.1.md), [I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md)

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | DB connection / health **policy** only |
| `/health` code changed | **No** |
| Current `/health` DB field | Static note: DB not configured / not tested in Phase 1A |
| Runtime `.env.local` | Exists outside Git (credentials redacted; not printed here) |
| DB | `iseo_report_hub_dev` exists; first migration applied |

This policy defines how a future implementation wave may add safe DB visibility to `/health` and introduce a shared DB connection service. It does **not** authorize code changes in this wave.

---

## 2. Objective

In the auth implementation wave (or a tightly coupled follow-on within that charter):

- add a safe DB status block to `/health`;
- probe connectivity without leaking secrets;
- keep health usable even when DB is down (degraded, not fatal for the whole app process where practical).

---

## 3. DB Connection Service

Recommended future source:

- `app-source/app/Services/DatabaseService.php`

| Rule | Statement |
|------|-----------|
| Driver | **PDO** only for app/tool connections |
| Local tool guard | Migration / admin bootstrap tools must **refuse** if configured DB name is not exactly `iseo_report_hub_dev` |
| Runtime app | May use the configured DB name after env loading (still expected local `iseo_report_hub_dev` in MVP) |
| Credentials | Loaded from runtime `.env.local` via `ConfigService`; **never** echoed |
| Connection | Lazy or explicit open; close/dispose cleanly in CLI tools |
| Errors | Surface safe summaries only |

`ConfigService` already parses `.env.local` when present; future work should flip `database.configured` / connection status based on real checks rather than Phase 1A placeholders.

---

## 4. Health Output

### Allowed fields

| Field | Example meaning |
|-------|-----------------|
| DB configured | yes / no (env present + required keys non-placeholder) |
| DB connection | pass / fail |
| DB name | `iseo_report_hub_dev` (name only) |
| Migration count | integer from `schema_migrations` when connected |
| Latest migration name | string from ledger when connected |
| Tables present count | integer when connected (optional) |

### Forbidden fields

| Forbidden | Reason |
|-----------|--------|
| Username / password | Secrets |
| DSN containing password | Secrets |
| Full stack traces in non-debug | Leak / noise |
| Full SQL error strings in non-debug | May include connection details |
| Client row dumps / sample data | Out of scope / privacy |

`/health` remains an operator/dev visibility surface for local MVP; production exposure rules are **SAFE UNKNOWN** / later hardening.

---

## 5. Failure Handling

| Rule | Statement |
|------|-----------|
| App fatal | Health check must **not** fatal the entire app on DB failure |
| Status | Show **degraded** / fail for DB while still returning a health page (HTTP 200 with degraded flag, or a documented non-5xx local convention — exact code deferred) |
| Logging | Safe error summary only (e.g. “connection refused”, “unknown database”) |
| Secrets | No credentials in logs or rendered HTML |

Auth routes may still depend on DB later; health itself must remain inspectable when auth/DB is broken.

---

## 6. SAFE UNKNOWN

| Item | Why unknown |
|------|-------------|
| Exact HTTP status when DB is down | Deferred (200+degraded vs 503) |
| Whether migration count is required on every health load | Performance/ops preference deferred |
| Production hardening of `/health` (auth gate / IP allowlist) | Not decided for local MVP |
| Whether `DatabaseService` is shared with `db-migrate.php` immediately | Preferred, but migrate tool already works; refactor timing is implementation choice |
