# REPORT — I-SEO REPORT HUB PROJECT/CLIENT LOCAL FIXTURE CHARTER 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `fb039af2199a6aadf59beb53095f351a5e46ddbf` |
| Staged/index before | **empty** |
| i-SEO WIP before | **clean** (no modified/untracked under `projects/iseo-report-hub/`) |
| Foreign WIP | **Preserved** — unrelated `M`/`??` paths left untouched |
| Write scope | Active Brain docs only under `projects/iseo-report-hub/product/`, `reports/`, `OPERATIONAL-INDEX.md` |

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| DB-03 apply commit | `c19c29b8be79ecfc8c946dd624e8f21023c2db39` — `feat(iseo-report-hub): add db03 reporting periods migration` |
| DB-03 hash follow-up | `2f88d0ced9f32e11414a02c8b6a08aad7b047099` — `docs(iseo-report-hub): record db03 reporting periods migration commit hash` |
| Migration | `2026_07_25_000002_create_reporting_periods_table.sql` |
| Checksum | `5bc50e53ab20a347c8a278d1726be6c71d835b572f369a14d2256e3e986e3be9` |
| Batch | **2** |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration count | **2** |
| Table count | **10** |
| users / roles | **1** / **6** |
| clients / projects / sites | **0** / **0** / **0** |
| reporting_periods rows | **0** |
| Current limitation | Unique/FK smoke for `reporting_periods` remains **structural-only** because `projects = 0` |

Read-only DB check this wave confirmed the counts above. No DB mutation.

---

## 3. Charter Output

Created:

- `product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-project-client-local-fixture-charter-01.md`

Updated:

- `OPERATIONAL-INDEX.md` — local fixture charter status; reason (DB-03 FK/unique needs demo project); no data created; next apply candidate

---

## 4. Fixture Design Summary

| Entity | Planned identity | Marker |
|--------|------------------|--------|
| Client | `Demo Client` / slug `demo-client` / status `active` | `notes = LOCAL_FIXTURE_ONLY` |
| Project | `Demo SEO Project` / slug `demo-seo-project` / type `service_corporate` | slug + parent client marker (`projects` has no `notes` column) |
| Site | url `demo.example.test` (scheme TBD at apply) / primary | `label = LOCAL_FIXTURE_ONLY` |
| Reporting period | `period_key 2026-07` / `2026-07-01`–`2026-07-31` / `draft` / title `Demo July 2026` | `summary = LOCAL_FIXTURE_ONLY` |

Idempotency: client by slug; project by `(client_id, slug)`; site by project+primary/url; period by `(project_id, period_key)`.

**Decision:** fixture **required before** Reporting Period CRUD.

**Preferred model:** `tools/create-local-fixture.php` — not schema seed migration; not one-off SQL as primary path.

**This wave created zero fixture rows.**

---

## 5. Validation Plan

Documented for next apply wave:

- Pre counts `0/0/0/0` (clients/projects/sites/reporting_periods)
- Post counts `1/1/1/1` (or documented deferral)
- FK chain + period FK to demo project
- Unique duplicate `(project_id, 2026-07)` refused
- `/health` 200; login/dashboard still work
- Optional audit event if implemented
- No secrets in output/Git
- Cleanup deferred; no DROP/TRUNCATE

---

## 6. Restrictions Confirmed

- no app-source edits
- no runtime edits
- no DB mutation
- no SQL/tool creation
- no real client data
- no fixture rows
- no admin/password/hash changes
- no env changes
- no source→runtime sync
- no service restart
- no demo/registry changes
- no push/fetch/pull/reset/clean/stash

---

## 7. Commit

| Field | Value |
|-------|-------|
| Exact-path git add | **yes** — allowlisted docs only |
| Commit message | `docs(iseo-report-hub): add local fixture charter` |
| Commit hash | `PENDING_PRIMARY_COMMIT_HASH` |
| Hash-record follow-up | `PENDING_HASH_RECORD_COMMIT_HASH` (if needed) |
| Push | **no** |

---

## 8. SAFE UNKNOWN

- Exact `url` string form for demo site (`demo.example.test` vs `https://demo.example.test`) until apply wave checks any app validators (schema accepts VARCHAR only).
- Whether apply wave will also insert optional `project_type_profiles` / `audit_log` rows.
- Exact local admin numeric `id` (not hardcoded; resolve at apply).
- Whether HealthController `9/9` expected-table wording will be fixed in a later separate charter.

---

## 9. Recommended Next Action

**I-SEO Report Hub — Project/Client Local Fixture Apply 01**

---

## 10. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-project-client-local-fixture-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 11. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** |
| commit | **yes** (primary; hash-record follow-up if needed) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout | **no** |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
