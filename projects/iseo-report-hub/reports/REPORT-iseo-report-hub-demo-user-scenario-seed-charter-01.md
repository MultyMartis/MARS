# REPORT — I-SEO REPORT HUB DEMO USER AND SCENARIO SEED CHARTER 01

## 1. Verdict

`DEMO USER SCENARIO SEED CHARTER COMPLETE`

## 2. Execution Verification

- Repo root: `X:\AI MARS`
- Volume: `X:` / `AI WS`
- Branch (main working tree): `mars/canonical-post-recovery`
- HEAD before: `83df042bf3aabd08720115f462e6fd1385d68e20`
- Clean worktree used: `X:\AI MARS STORAGE\git-sync-iseo-report-hub-demo-user-scenario-seed-charter-01\repo`
- Feature branch: `docs/iseo-report-hub-demo-user-scenario-seed-charter-01`
- Foreign WIP on main: preserved (not staged/restored/cleaned)
- i-SEO scope before start: clean
- Staged index before start: empty
- App-source / runtime / DB: **unchanged** (docs only)
- Optional HTTP: `/health` **200**, `/login` **200**
- Optional DB: read-only probe of `iseo_report_hub_dev` OK

## 3. Current State Audit

- Users: Local Admin + Polygon WS (`admin_owner`); **no** test user yet
- Role `seo_specialist` exists; login is **email**
- Demo Client / Demo SEO Project / report **1** finalized + report **5** empty draft — **preserve**
- Tables mapped for users/clients/projects/sites/periods/monthlies/blocks/work entries; **no** dedicated metrics table
- Exports **4**, shares **7** (6 revoked / 1 active on export 4), snapshot **1** — Demo Client only; freeze for new scenario
- Existing tools: `create-local-admin.php`, `create-local-fixture.php`, `seed-nikita-catalogue.php`, `summary-assembly-safe-fixture.php`

## 4. Demo User Seed Spec

- Name: `Тест Проверочнов`
- Email/login: `test@reports.i-seo.local` (operator shorthand `test`)
- Password: `test` (local/demo only; no hash in docs)
- Role: `seo_specialist` / status `active`
- Hasher: PHP `password_hash` / `password_verify` consistent with admin tool
- Idempotency: update only known demo email + marker; refuse unknown users
- Marker: `MARS_DEMO_PROVERKA_20260821`

## 5. Demo Scenario Data Spec

- Display literal: `ПРОВЕРКА.рa` (Cyrillic `р` + Latin `a` preserved)
- Project: `SEO-продвижение ПРОВЕРКА.рa`
- Slug: `proverka-demo`; URL: `https://proverka.example`
- July 2026: period `finalized`; monthly **seed-status `finalized`** with full content; **no** snapshot/export/share
- August 2026: period `active`; monthly `in_progress` as of 2026-08-21
- Separate client/project — do **not** reuse report 1/5

## 6. Demo Content Pack

- July: full RU sections + invented calm metrics (visits 1240→1480, etc.) + **12** work entries
- August: partial through 21st + MTD metrics + **10** work entries (done/in_progress/planned/risk)
- Metrics via prose / optional `metric_snapshot` JSON with `"demo": true`
- Explicit demo-fiction disclaimer

## 7. Seed Implementation Plan

- Wave: **Demo User and Scenario Seed Implementation 01**
- Backup: `X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-user-scenario-seed-implementation-01\backup\`
- Tool: `app-source/tools/demo-proverka-seed.php`
- Modes: `--create` / `--status` / `--cleanup`
- Guard: DB name + `127.0.0.1` + local env + `--confirm-local-demo-seed`
- Evidence: `demo-proverka-ids.json`; exact-id cleanup only
- No PDF/export/share; no report 1/5 changes

## 8. Browser Fill Follow-up

- Wave: **Browser Filled Demo Report Pass 01** (after seed)
- Firefox Developer + profile `X:\MARS-Localhost\browser-profiles\firefox-developer\mars-research`
- Login as `test@reports.i-seo.local`; periods → July/August → entries/blocks → previews
- Capture screenshots + UI issue log; no silent bypass; no PDF/export/share

## 9. Safety / Acceptance

- Backup + local-only + no production/host upload
- Password `test` local only
- Acceptance: login, project visible, two months, July full, August in progress, helps present, previews credible, baselines intact

## 10. Docs Created

- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-SEED-CURRENT-STATE-AUDIT-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-USER-SEED-SPEC-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-DATA-SPEC-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-SCENARIO-PROVERKA-CONTENT-PACK-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-IMPLEMENTATION-PLAN-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-SCENARIO-BROWSER-FILL-FOLLOWUP-PLAN-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-SCENARIO-SEED-SAFETY-ACCEPTANCE-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\reports\REPORT-iseo-report-hub-demo-user-scenario-seed-charter-01.md`
- `X:\AI MARS\projects\iseo-report-hub\OPERATIONAL-INDEX.md` (updated)

## 11. Restrictions Confirmed

- no code edits
- no runtime edits
- no DB mutation
- no user/report creation
- no share/export/PDF mutation
- no production
- no push
- no secrets/token printing

## 12. Commit

- primary: `6ec876743b98731fe532b8ef51857f9ae8972075`
- hash-record: `a1d10f995b59cc17f6a07051543d1c4f10780fa9`
- tip HEAD: `f47d98cc286dd840b4e1c757c90df829afd4fb8b`
- push: **no**

## 13. SAFE UNKNOWN

- Whether period UI can fully bind to a newly seeded project without extra UX work (verify in Implementation 01 / Browser Fill).
- Demo password length vs admin-tool min-12 interactive rule — operator-approved local exception for password `test` in Implementation 01.

## 14. Files Changed

Docs listed in §10 only (exact allowlist).

## 15. Git Actions

- Clean worktree commit on `docs/iseo-report-hub-demo-user-scenario-seed-charter-01`
- Scoped restore of allowlisted paths into main working tree
- Foreign WIP preserved
- **No push**

## 16. Exact next action

Run **`I-SEO Report Hub — Demo User and Scenario Seed Implementation 01`**: backup `iseo_report_hub_dev`, implement guarded `tools/demo-proverka-seed.php`, seed user + `ПРОВЕРКА.рa` July/August baseline, write `demo-proverka-ids.json`. Then **Browser Filled Demo Report Pass 01**. Do **not** upload to `reports.i-seo.su` unless operator explicitly commands it.
