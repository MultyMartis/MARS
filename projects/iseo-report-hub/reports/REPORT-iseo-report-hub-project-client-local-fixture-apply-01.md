# REPORT — I-SEO REPORT HUB PROJECT/CLIENT LOCAL FIXTURE APPLY 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `b546e3e299606075d27c4364c676f8abf3896f7f` |
| Staged/index before | **empty** |
| i-SEO WIP before | **clean** (no modified/untracked under `projects/iseo-report-hub/`) |
| Foreign WIP | **Preserved** — unrelated `M`/`??` paths left untouched |
| Write scope | One source CLI tool + optional README; exact runtime copies of those two files; Active Brain result/report/`OPERATIONAL-INDEX` only; local DB inserts for fixture rows only |

---

## 2. Preflight

| Check | Result |
|-------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` — present (8.3.30) |
| MySQL executable | `X:\MARS-Localhost\laragon\bin\mysql\mysql-8.4.3-winx64\bin\mysql.exe` — present |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count before | **2** |
| Latest migration before | `2026_07_25_000002_create_reporting_periods_table.sql` |
| Table count before | **10** |
| users / roles before | **1 / 6** |
| clients / projects / sites / reporting_periods before | **0 / 0 / 0 / 0** |
| `reporting_periods` table | **exists** |
| Runtime `.env.local` | **present** (not printed; not edited; not committed) |

---

## 3. Source Tool

| Field | Value |
|-------|-------|
| Source path | `projects/iseo-report-hub/app-source/tools/create-local-fixture.php` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\create-local-fixture.php` |
| Local guards | CLI-only; DB name `iseo_report_hub_dev`; host `127.0.0.1`; required tables present; column inspection before insert |
| Idempotency | Full match → `already-present` exit 0; partial mismatch → STOP |
| Transaction / rollback | Single transaction; rollback on failure |
| Safe output | `created` / `already-present`, IDs, counts, validation summary, audit status — **no** credentials / password / hash |

---

## 4. Runtime Sync

| Item | Result |
|------|--------|
| Files copied | `tools/create-local-fixture.php`, `README.md` |
| Source/runtime hash match | **yes** (both files) |
| `.env.local` | **untouched** |
| Broad sync | **no** |

---

## 5. Fixture Apply

| Field | Result |
|-------|--------|
| First run | `result=created` exit **0** |
| Second run | `result=already-present` exit **0** |
| client_id | **1** (`Demo Client` / `demo-client`) |
| project_id | **1** (`Demo SEO Project` / `demo-seo-project`) |
| site_id | **1** (`https://demo.example.test`) |
| reporting_period_id | **1** (`2026-07`) |
| Counts after | clients/projects/sites/reporting_periods = **1/1/1/1** |
| Audit event | **yes** — `local_fixture.created` |

---

## 6. DB Validation

| Check | Result |
|-------|--------|
| FK joins | client → project → site / period **ok** |
| Unique duplicate validation | duplicate `(project_id, period_key)` insert rejected (SQLSTATE `23000`); transaction rolled back; count remains **1** |
| Constraints | `uniq_reporting_periods_project_period`; five FKs on `reporting_periods` present |
| `reporting_periods` smoke now non-structural | **yes** |

---

## 7. Health/App Smoke

| URL | Result |
|-----|--------|
| `/health` | **200**, overall **ok**, DB status **ok**, migration count **2** |
| `/login` | **200** |
| `/not-existing` | **404** |
| Auth baseline | **not modified** |

---

## 8. Restrictions Confirmed

| Restriction | Confirmed |
|-------------|-----------|
| No production DB | yes |
| No real client data | yes |
| No credentials in Git/report | yes |
| No password/hash in report | yes |
| No `.env` committed | yes |
| No source `.env.local` | yes |
| No schema migration edits | yes |
| No auth/app code edits | yes |
| No DB dump | yes |
| No WordPress | yes |
| No Composer/npm | yes |
| No vhost/hosts/service restart | yes |
| No demo/registry changes | yes |
| No push/fetch/pull/reset/clean/stash | yes |

---

## 9. Documentation

| Doc | Path |
|-----|------|
| Result | `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md` |
| OPERATIONAL-INDEX | updated (fixture apply status, tool path, counts, FK/unique, next stage) |
| This closeout | `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-project-client-local-fixture-apply-01.md` |

---

## 10. Commit

| Field | Value |
|-------|-------|
| Exact-path git add | `create-local-fixture.php`, `README.md`, result doc, this report, `OPERATIONAL-INDEX.md` |
| Staged list | allowlisted i-SEO paths only |
| Commit message | `feat(iseo-report-hub): add local fixture bootstrap` |
| Commit hash | `348b40896a86f5652ea8f7ba5ab5574ebc2abf2b` |
| HEAD verification | `348b40896a86f5652ea8f7ba5ab5574ebc2abf2b` matches primary commit |
| Push | **no** |

Hash-record follow-up: `docs(iseo-report-hub): record local fixture bootstrap commit hash`

---

## 11. SAFE UNKNOWN

- Whether `/health` expected-table display remains `9/9` vs `10/10` (not fixed in this wave; overall health **ok**).
- Future fixture cleanup/removal policy (explicitly out of scope).

---

## 12. Recommended Next Action

**I-SEO Report Hub — Reporting Period CRUD Charter 01**

---

## 13. Files Changed

### Git (Active Brain)

- `projects/iseo-report-hub/app-source/tools/create-local-fixture.php` (created)
- `projects/iseo-report-hub/app-source/README.md` (updated)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md` (created)
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-project-client-local-fixture-apply-01.md` (created)
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md` (updated)

### Runtime (outside Git)

- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\create-local-fixture.php`
- `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\README.md`

### DB mutation (`iseo_report_hub_dev` @ `127.0.0.1`)

- INSERT 1 client, 1 project, 1 site, 1 reporting_period, 1 audit event (`local_fixture.created`)
- No DELETE / DROP / TRUNCATE

---

## 14. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** (allowlisted only) |
| commit | **yes** (primary + optional hash-record) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
