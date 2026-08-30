# REPORT — I-SEO REPORT HUB MVP PHASE 1B SOURCE TO RUNTIME SYNC + LOCAL SMOKE 01

**project_id:** `iseo-report-hub`  
**Date:** 2026-07-24  
**Mode:** Model A source → runtime allowlist sync · local smoke · docs commit only · no push

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-commit) | `5f46c3df6695ec9607a7faa06e528be09340c0de` |
| Staged/index before writes | empty |
| Foreign WIP | preserved (not staged / not restored / not cleaned) |
| Source path | `X:\AI MARS\projects\iseo-report-hub\app-source\` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Write scope (runtime) | allowlisted files under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` only |
| Write scope (Active Brain) | Phase 1B result doc, closeout report, `OPERATIONAL-INDEX.md` |

---

## 2. Pre-sync Safety

| Check | Result |
|-------|--------|
| `app-source/` exists | yes |
| Runtime target exists | yes |
| Source `.env` / `.env.local` | absent |
| Runtime `.env` / `.env.local` | absent (pre-sync) |
| Nested `.git` (source / runtime) | absent |
| Source `vendor/` / `node_modules/` | absent |
| Runtime storage payloads (logs/uploads/cache non-`.keep`) | empty |
| PHP 8.3.30 executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` — present |
| Allowlist source presence | **44 / 44** present; missing **0** |

---

## 3. Sync Summary

| Field | Value |
|-------|-------|
| Direction | **source → runtime** |
| Method | Allowlist `Copy-Item` only (no wipe, no delete of unknown files) |
| Copied files count | **44** |
| Missing optional files | **0** (`docs/SOURCE-RUNTIME-POLICY.md` present) |
| Runtime wiped | **no** |
| Generated storage data touched | **no** (dirs preserved; no non-`.keep` payloads) |
| `app-source/` modified | **no** |

---

## 4. Runtime State After Sync

| Component | Present |
|-----------|---------|
| Front controller `public/index.php` | yes |
| Standalone `public/health.php` | yes |
| Bootstrap `app/bootstrap.php` | yes |
| Router `app/Support/Router.php` + `app/routes.php` | yes |
| Controllers (Base/Dashboard/Auth/Health) | yes |
| Services (Config/Auth/Csrf) | yes |
| Views + layout + partials | yes |
| CSS/JS assets | yes |
| Config examples | yes |
| DB | **no** |
| `.env` / `.env.local` | **no** |

Hash spot-check (source vs runtime): `public/index.php`, `app/bootstrap.php`, `app/routes.php`, `app/Support/Router.php` — **match**.

---

## 5. Smoke Tests

| Test | Result |
|------|--------|
| PHP executable | PHP 8.3.30 (`php-8.3.30-Win32-vs16-x64\php.exe`) |
| `php -l` on runtime PHP (25 files: public + app + config examples) | **PASS** — LINT_ERR=0 |
| CLI route `/` | STATUS=200 |
| CLI route `/health` | STATUS=200 |
| CLI route `/login` | STATUS=200 |
| CLI route `/not-existing` | STATUS=404 |
| Built-in server `php -S 127.0.0.1:8088 -t public public/index.php` | **PASS** — `/` 200, `/health` 200, `/login` 200, `/not-existing` 404; process **stopped** |
| DB | **Not tested** |

---

## 6. Validation

| Guard | Result |
|-------|--------|
| no `.env` | pass |
| no `.env.local` | pass |
| no secrets | pass |
| no DB creation/mutation | pass |
| no SQL execution | pass |
| no Composer/npm | pass |
| no vendor/node_modules | pass |
| no WordPress | pass |
| no vhost/hosts edits | pass |
| no service restart | pass |
| no demo workspace edits | pass |
| no registry changes | pass |
| no nested `.git` in runtime | pass |
| no generated log/upload/cache payloads created | pass |
| no push/fetch/pull/reset/clean/stash/checkout/restore | pass |
| `app-source/**` unmodified | pass |

---

## 7. Documentation

| Doc | Action |
|-----|--------|
| `product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md` | created |
| `OPERATIONAL-INDEX.md` | updated (Phase 1B complete; smoke; next = vhost/hosts charter) |
| This closeout report | created |

---

## 8. Commit

| Field | Value |
|-------|-------|
| Exact-path stage | yes |
| Staged list | `OPERATIONAL-INDEX.md`; `product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md`; `reports/REPORT-iseo-report-hub-mvp-phase-1b-source-to-runtime-sync-local-smoke-01.md` |
| Commit message | `docs(iseo-report-hub): record phase 1b runtime sync` |
| Commit hash | `223504692edfd05337a703b19d2b4865714d014c` (`22350469`) |
| HEAD verification | `git show --name-only --oneline --stat HEAD` — only the three Active Brain docs above |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Whether Laragon already auto-maps this sites path without manual hosts (not probed)
- Exact Apache vhost template contents when the domain charter runs
- Timing of first `.env.local` introduction (DB vs auth charter)

---

## 10. Recommended Next Action

**Local vhost/hosts mapping charter for `iseo-report-hub.test`.**

---

## 11. Files Changed

### Active Brain (Git)

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md` (modified)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-PHASE-1B-RUNTIME-SYNC-RESULT-v0.1.md` (created)
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-mvp-phase-1b-source-to-runtime-sync-local-smoke-01.md` (created)

### Runtime (outside Git)

- Allowlisted Phase 1A skeleton files copied under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` (44 files; not committed)

---

## 12. Git Actions

| Action | Done |
|--------|------|
| exact-path git add | yes |
| commit | yes |
| push | **no** |
| fetch | no |
| pull | no |
| checkout | no |
| reset | no |
| restore | no |
| clean | no |
| stash | no |
