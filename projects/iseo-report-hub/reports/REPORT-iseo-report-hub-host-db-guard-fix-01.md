# REPORT — I-SEO REPORT HUB HOST DB GUARD FIX 01

**Date:** 2026-08-21  
**Verdict:** `HOST DB GUARD FIX PASS`  
**Commit:** `f61b91f02f68ee9b6464104e5a4e67151ddad507`  
**Push:** no

---

## 1. Verdict

`HOST DB GUARD FIX PASS`

Local-only exact DB name guard no longer blocks normal web runtime. Production / host `DB_DATABASE` values (e.g. `nikel0rv_reports`) can be used when `APP_ENV=production`. Local CLI mutation tools still require `iseo_report_hub_dev` via explicit opt-in + tool-level checks.

---

## 2. Root cause

`DatabaseService::assertLocalDevDatabase()` unconditionally refused any DB name other than `iseo_report_hub_dev`.

That method was called from shared domain services (`ReportingPeriodService`, `WeeklyCheckpointService`, CRUD/export/snapshot services, etc.) on every DB path via `assertDb()`.

On host `https://reports.i-seo.su` with `APP_ENV=production` and host-specific `DB_DATABASE`, internal pages failed with:

`REFUSED: target DB must be exactly "iseo_report_hub_dev".`

---

## 3. Fix

| Change | Detail |
|--------|--------|
| `DatabaseService` | `assertLocalDevDatabase()` is **no-op** unless `enableLocalDevDatabaseGuard()` was called |
| Guard when enabled | Requires `APP_ENV=local` **and** exact DB name `iseo_report_hub_dev` |
| Web runtime | Services still call `assertLocalDevDatabase()`; without enable → no block |
| CLI tools | Call `enableLocalDevDatabaseGuard()` before assert: `demo-proverka-seed.php`, `summary-assembly-safe-fixture.php`, `create-local-admin.php`, `create-local-fixture.php` |
| Tool own checks | Seed tool still requires `--confirm-local-demo-seed` for mutations; still checks local env/host/name |

Secrets / passwords are not printed. DB was not mutated in this wave. Host upload was **not** performed.

---

## 4. Files changed (source)

| Path | Role |
|------|------|
| `projects/iseo-report-hub/app-source/app/Services/DatabaseService.php` | Conditional local guard |
| `projects/iseo-report-hub/app-source/tools/demo-proverka-seed.php` | Enable guard |
| `projects/iseo-report-hub/app-source/tools/summary-assembly-safe-fixture.php` | Enable guard |
| `projects/iseo-report-hub/app-source/tools/create-local-admin.php` | Enable guard |
| `projects/iseo-report-hub/app-source/tools/create-local-fixture.php` | Enable guard |
| `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-host-db-guard-fix-01.md` | This report |
| `projects/iseo-report-hub/OPERATIONAL-INDEX.md` | Status wave |

---

## 5. Runtime sync (local only)

Exact sync to `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`:

- `app/Services/DatabaseService.php`
- `tools/demo-proverka-seed.php`
- `tools/summary-assembly-safe-fixture.php`
- `tools/create-local-admin.php`
- `tools/create-local-fixture.php`

---

## 6. Validation

| Check | Result |
|-------|--------|
| PHP lint (source + runtime, 5 files) | PASS |
| `GET /health` | 200 |
| `GET /login` | 200 |
| `GET /reporting-periods` (authenticated local demo session) | 200; no `REFUSED: target DB must be exactly` |
| `GET /reporting-periods` (anonymous) | 302 → login (expected) |
| `php tools/demo-proverka-seed.php --status` | exit 0, `ok: true` |
| `php tools/demo-proverka-seed.php --create` (no confirm) | `REFUSED: --confirm-local-demo-seed is required` (exit 2) |
| Guard probe: assert without enable | no-op OK |
| Guard probe: enable on local + correct DB | OK |
| DB mutation | none |
| Host upload | none |
| `.env.local` edits | none |

---

## 7. Operator re-upload (host) — exact files

Re-upload **only** this app file from source (or synced equivalent):

1. `app/Services/DatabaseService.php`

**Do not** upload local tools to host (they remain local-only).

**Reminders:**

- Keep host `.env.local` with `APP_ENV=production`, host `DB_*`, `APP_URL=https://reports.i-seo.su`
- Set **`APP_DEBUG=false`** on host
- Do **not** run local seed/migrate/fixture tools against host DB
- No password/secret printing in diagnostics

---

## 8. Boundaries

- No host upload in this wave
- No DB dump/restore/mutation
- No `.env.local` changes
- No push
- Foreign WIP elsewhere in monorepo preserved / not staged

---

## 9. Next

Operator: re-upload `app/Services/DatabaseService.php` to `reports.i-seo.su`, confirm internal pages load with host DB name, keep `APP_DEBUG=false`.
