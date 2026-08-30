# REPORT — I-SEO REPORT HUB PRE-HOSTING DEMO SCENARIO AND FIELD HELP CHARTER 01

## 1. Verdict

`PRE-HOSTING DEMO SCENARIO FIELD HELP CHARTER COMPLETE`

## 2. Execution Verification

- Repo root: `X:\AI MARS`
- Volume: `X:` / `AI WS`
- Branch (main working tree): `mars/canonical-post-recovery`
- HEAD before: `04d575a48d84259cc450dfc8ed9bee62148fd255`
- Clean worktree used: `X:\AI MARS STORAGE\git-sync-iseo-report-hub-prehosting-demo-scenario-field-help-charter-01\repo`
- Feature branch: `docs/iseo-report-hub-prehosting-demo-scenario-field-help-charter-01`
- Foreign WIP on main: preserved (not staged/restored/cleaned)
- i-SEO scope before start: clean (no `projects/iseo-report-hub/` WIP/staged)
- App-source / runtime / DB: **unchanged**

## 3. Pre-hosting Tech Decision

- Subdomain: `reports.i-seo.su`
- SSL: operator states **already done**
- PHP: **8.3** (align with local Laragon 8.3.x)
- Host checks documented: PDO MySQL, mbstring, intl/fileinfo/curl as applicable, writable storage, rewrite to `public/`
- Upload: **not authorized** in this wave
- Doc: `product/I-SEO-REPORT-HUB-PREHOSTING-TECH-DECISION-v0.1.md`

## 4. Demo User Plan

- Name: `Тест Проверочнов`
- Operator login word: `test` → app requires **email** → plan: `test@reports.i-seo.local`
- Password: `test` (local/demo only; hash never printed)
- Role: **`seo_specialist`** (exact DB/app code)
- Auth: `AuthService` email + `password_verify`; login form `type="email"`
- Creation deferred to seed wave with backup
- Doc: `product/I-SEO-REPORT-HUB-DEMO-USER-TEST-PROVEROCHNOV-PLAN-v0.1.md`

## 5. Realistic Demo Scenario Plan

- Project literal: `ПРОВЕРКА.рa`
- Mixed-script: Cyrillic `р` (U+0440) + Latin `a` (U+0061) — documented; display keeps literal; slug ASCII
- Month 1: July 2026 — complete / finalized-ish full content
- Month 2: August 2026 — in progress through 2026-08-21
- Separate from Demo Client / report 1 / report 5
- Pseudo-metrics in prose/`demo:true` refs only
- Doc: `product/I-SEO-REPORT-HUB-REALISTIC-DEMO-SCENARIO-PROVERKA-PLAN-v0.1.md`

## 6. Browser Filling Strategy

- Firefox Developer Edition + profile `X:\MARS-Localhost\browser-profiles\firefox-developer\mars-research`
- Controlled seed for user + client/project/site (no client UI CRUD)
- Browser for work entries / blocks / texts / preview
- Issue capture on UI errors; no PDF/export/share
- Doc: `product/I-SEO-REPORT-HUB-BROWSER-FILLING-STRATEGY-v0.1.md`

## 7. Field Help Design

- `?` icon beside labels; click/keyboard opens hint + example
- First: work entry, report block, monthly content forms
- Reusable partial + static PHP help map; no DB migration
- Doc: `product/I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-DESIGN-v0.1.md`

## 8. Field Help Copy Pack

- Full Russian hints/examples for priority fields (client summary, internal note, evidence, risks, monthly sections, etc.)
- Doc: `product/I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md`

## 9. Implementation Sequence

1. **Field Help Question Icon Implementation 01** ← **next**
2. Demo User and Scenario Seed Charter 01
3. Demo User and Scenario Seed Implementation 01 (backup first)
4. Browser Filled Demo Report Pass 01
5. Pre-hosting Deployment Readiness Charter 01 (after demo accepted)
- Doc: `product/I-SEO-REPORT-HUB-DEMO-SCENARIO-FIELD-HELP-IMPLEMENTATION-SEQUENCE-v0.1.md`

## 10. Safety / Acceptance

- Charter: docs only — accepted criteria met
- Future field-help: no DB
- Future seed: backup required
- Host upload / PDF/export/share: frozen until explicit approval
- Doc: `product/I-SEO-REPORT-HUB-PREHOSTING-DEMO-FIELD-HELP-SAFETY-ACCEPTANCE-v0.1.md`

## 11. Docs Created

- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-PREHOSTING-TECH-DECISION-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-USER-TEST-PROVEROCHNOV-PLAN-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-REALISTIC-DEMO-SCENARIO-PROVERKA-PLAN-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-BROWSER-FILLING-STRATEGY-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-FIELD-HELP-QUESTION-ICON-DESIGN-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-DEMO-SCENARIO-FIELD-HELP-IMPLEMENTATION-SEQUENCE-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-PREHOSTING-DEMO-FIELD-HELP-SAFETY-ACCEPTANCE-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\reports\REPORT-iseo-report-hub-prehosting-demo-scenario-field-help-charter-01.md`
- `X:\AI MARS\projects\iseo-report-hub\OPERATIONAL-INDEX.md` (updated)

## 12. Restrictions Confirmed

- No code edits
- No runtime edits
- No DB mutation
- No user/report creation
- No share/export/PDF mutation
- No production upload
- No push
- No secrets/token printing

## 13. Commit

- Primary: `9c95b639d87e78649fe837b087c9e4824edfc824`
- Hash-record: `965b012d074bc40fd517ca9349a1034a776c907c`
- Tip HEAD: `59da72c82fedb2512c6375490c9a4cb7421fb2df`
- Push: **no**

## 14. SAFE UNKNOWN

- Whether host will be MySQL vs MariaDB (must verify before deploy)
- Whether `intl` is strictly required on host until host phpinfo probe
- Whether MARS browser-clicking plugin is available in the next fill environment (manual Firefox path remains valid)
- Exact period status enum labels preferred by operator for July “closed” vs leaving period `active` with monthly `finalized` — finalize in seed charter

## 15. Files Changed

Allowlisted docs only (see §11). No app-source / runtime / DB / evidence binaries.

## 16. Git Actions

Exact-path commits in clean worktree; merge into `mars/canonical-post-recovery`; scoped restore of allowlisted paths into main working tree; foreign WIP preserved; **no push**.
