# REPORT — I-SEO REPORT HUB PHASE 0 RUNTIME REVIEW + SOURCE RUNTIME POLICY 01

**project_id:** `iseo-report-hub`  
**Date:** 2026-07-24  
**Branch:** `mars/canonical-post-recovery`  
**HEAD at start:** `f0a79f07`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged / index before writes | **Empty** |
| Foreign WIP | **Preserved** (unrelated `M` / `??` not staged/restored/cleaned) |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| Write scope | Allowlisted Active Brain i-SEO docs + optional runtime policy doc only |
| DB / vhost / hosts / services | **Not touched** |

---

## 2. Runtime Review

| Check | Result |
|-------|--------|
| Runtime tree | Present — `app/`, `config/`, `database/`, `docs/`, `public/`, `storage/`, root README / `.env.example` / `.gitignore` |
| Index page | `public/index.php` — Phase 0 status; no DB |
| Health page | `public/health.php` — PHP + extensions; no DB |
| `.env.example` | Placeholders only (`CHANGE_ME`, candidate DB/domain) |
| `.gitignore` | Ignores `.env`, `.env.local`, storage logs/uploads/cache contents |
| Config examples | No real credentials (`CHANGE_ME` / getenv fallbacks) |
| Schema draft | `database/schema-draft-not-migration.md` — markdown only; **not** executable SQL |
| `.env` / `.env.local` | **Absent** |
| Nested `.git` | **Absent** |
| WordPress / vendor / node_modules | **Absent** |
| DB connection | **Not attempted** |
| CLI smoke `index.php` | **Pass** — PHP 8.3.30 CLI HTML render; DB not attempted |
| CLI smoke `health.php` | **Pass** — required extensions all present; SAPI `cli`; DB not attempted |

---

## 3. Source / Runtime Policy

| Topic | Decision |
|-------|----------|
| Active Brain docs authority | `X:\AI MARS\projects\iseo-report-hub\` |
| Localhost runtime workspace | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` |
| Separate Git repo for runtime | **No** |
| Runtime committed directly in this wave | **No** (outside monorepo) |
| Source preservation issue | Runtime files not versioned by normal Active Brain commits — temporary only |
| Model A | Source-first `app-source/` under Active Brain + sync to Localhost |
| Model B | Runtime-first + snapshots into Active Brain (not recommended long-term) |
| Recommendation | **Model A** before Phase 1; do **not** create `app-source/` in this wave |
| Phase 1 | **Blocked** until source model approved |

---

## 4. Files Created

**Active Brain:**

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-phase-0-runtime-review-source-runtime-policy-01.md`

**Runtime (outside Git; not committed):**

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\docs\SOURCE-RUNTIME-POLICY.md`

---

## 5. Files Modified

**Active Brain:**

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-PHASE-0-SCAFFOLD-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-mvp-phase-0-runtime-scaffold-01.md`

**Runtime app code:** **unchanged** (policy doc under `docs/` only).

---

## 6. Validation

| Constraint | Result |
|------------|--------|
| No DB created | Pass |
| No SQL executed | Pass |
| No vhost / hosts edits | Pass |
| No service restart | Pass |
| No secrets | Pass |
| No runtime app code edits (except optional policy doc) | Pass |
| No demo workspace edits | Pass |
| No registry changes | Pass |
| No runtime Git repo | Pass |
| No push / fetch / pull / reset / clean / stash / checkout / restore | Pass |

---

## 7. Commit

| Item | Value |
|------|-------|
| Exact-path `git add` | **Yes** — allowlisted Active Brain paths only |
| Commit | **Yes** |
| Message | `docs(iseo-report-hub): define source runtime policy` |
| Commit hash | `COMMIT_HASH_PLACEHOLDER` |
| HEAD verification | `git show --name-only --oneline --stat HEAD` — allowlisted docs only |
| Push | **No** |
| Runtime path staged | **No** |

---

## 8. SAFE UNKNOWN

- Whether `iseo-report-hub.test` already exists in hosts/vhost (not inspected).
- Whether MySQL already contains `iseo_report_hub_dev` (not queried).
- Exact Model A sync tooling (deferred to source-mirror charter).

---

## 9. Recommended Next Action

Create source mirror + deploy/sync charter for **Model A**, then proceed to Phase 1.

---

## 10. Files Changed

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-SOURCE-RUNTIME-POLICY-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-MVP-PHASE-0-SCAFFOLD-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-mvp-phase-0-runtime-scaffold-01.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-phase-0-runtime-review-source-runtime-policy-01.md`

Runtime local doc (not in Git):

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\docs\SOURCE-RUNTIME-POLICY.md`

---

## 11. Git Actions

| Action | Done |
|--------|------|
| exact-path `git add` | **yes** |
| commit | **yes** |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
