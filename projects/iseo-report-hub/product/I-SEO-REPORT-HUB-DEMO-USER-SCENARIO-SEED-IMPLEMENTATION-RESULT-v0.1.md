# I-SEO Report Hub — Demo User and Scenario Seed Implementation Result v0.1

**Status:** complete — local DB seed applied  
**Date:** 2026-08-21  
**Wave:** `I-SEO Report Hub — Demo User and Scenario Seed Implementation 01`  
**Verdict:** `DEMO USER SCENARIO SEED PASS`

---

## 1. What was done

Guarded CLI tool `app-source/tools/demo-proverka-seed.php` created and run against local DB `iseo_report_hub_dev` only.

Created:

| Entity | Value / ID |
|--------|------------|
| Demo user | `Тест Проверочнов` / `test@mail.ru` / role `seo_specialist` / active — **user_id=3** |
| Client | `ПРОВЕРКА.рa` — **client_id=2**, slug `proverka-demo` |
| Project | `SEO-продвижение ПРОВЕРКА.рa` — **project_id=2** |
| Site | `ПРОВЕРКА.рa` @ `https://proverka.example` — **site_id=2** |
| July period | **period_id=5**, `2026-07`, status `finalized` |
| August period | **period_id=6**, `2026-08`, status `active` |
| July monthly | **monthly_id=7**, status `finalized` (DB status only; no snapshot/export/share) |
| August monthly | **monthly_id=8**, status `in_progress` |
| Blocks | 6 July + 6 August |
| Work entries | 12 July + 10 August |
| Marker | `MARS_DEMO_PROVERKA_20260821` |

Operator-approved demo password exists as input fact: `test`. **Password hash was not printed** in CLI, evidence, or docs.

---

## 2. Backup

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-user-scenario-seed-implementation-01\backup\iseo_report_hub_dev-before-demo-proverka-seed-20260821-134512.sql` |
| Size | 86712 bytes |
| SHA256 | `1f8e72e3aea3ef8b5f458add779767d13feb6237a687a999e793488f953fa751` |

Backup is **not** committed to git.

---

## 3. Seed tool

| Item | Detail |
|------|--------|
| Source | `projects/iseo-report-hub/app-source/tools/demo-proverka-seed.php` |
| Runtime sync | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\demo-proverka-seed.php` |
| Modes | `--status`, `--create`, `--cleanup` |
| Mutation guard | `--confirm-local-demo-seed` + local APP_ENV/DB host/name/URL checks |

---

## 4. Report URLs (local)

Base: `http://iseo-report-hub.test`

- July detail: `/monthly-reports/7`
- July client preview: `/monthly-reports/7/preview`
- August detail: `/monthly-reports/8`
- August client preview: `/monthly-reports/8/preview`
- August work create: `/monthly-reports/8/work-entries/create`
- Sample work edit: `/monthly-report-work-entries/28/edit`
- Periods: `/reporting-periods/5`, `/reporting-periods/6`

---

## 5. Evidence (Storage only — not in git)

`X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-user-scenario-seed-implementation-01\20260821-134512\`

Includes: `demo-proverka-ids.json`, before/after status & counts, create/status logs, screenshots `01`–`09`, `DEMO-SEED-SCREENSHOT-INDEX.md`, `DEMO-SEED-ASSERTIONS.md`, `http-validation.json`.

---

## 6. Validation summary

| Check | Result |
|-------|--------|
| PHP lint seed tool | PASS |
| DB user/role/scenario | PASS |
| Export/share/snapshot totals unchanged (4 / 7 / 1) | PASS |
| Export 4 size/checksum prefix unchanged | PASS |
| Report 1 blocks/entries unchanged (6 / 7) | PASS |
| Report 5 blocks/entries unchanged (0 / 0) | PASS |
| Demo monthlies publication rows = 0 | PASS |
| HTTP GET required routes 200 | PASS |
| Login as `test@mail.ru` | PASS (may update `last_login_at`) |
| Screenshots @1920 full page | PASS |

---

## 7. Safety

- Local DB mutation: **yes** (expected)
- Report 1 / 5 mutation: **no**
- Export / share / PDF / snapshot create: **no**
- Production / host upload: **no**
- Hash / token printed: **no**

---

## 8. Next action

`I-SEO Report Hub — Browser Filled Demo Report Pass 01`
