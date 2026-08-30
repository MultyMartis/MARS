# I-SEO Report Hub — UI Screenshot QA Inventory v0.1

**Status:** DISCOVERY / QA ONLY — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-07  
**Wave:** UI Screenshot QA, Brand Style and Nikita Templates Discovery 01  
**Baseline:** Demo Visual Shell Alignment Implementation 02 (`DEMO VISUAL SHELL ALIGNMENT PASS`)

---

## 1. Method

| Source | Use |
|--------|-----|
| Operator screenshot observations | Primary defect list for secondary CRUD/preview pages |
| `app-source` Views / CSS | Exact EN strings and machine keys |
| Live GET `http://iseo-report-hub.test/*` | Auth gate + `/health` only (no session → manager pages **302**) |
| Impl 02 smoke HTML under STORAGE | Authenticated chrome evidence for A–D surfaces |
| Russian UX Copy Dictionary v0.1 | Proposed RU replacements |

**Live GET note:** Without session, `/`, periods, monthly, preview, blocks, exports, shares redirect (302). `/health` **200**. No password login / POST / share mutation in this wave. Inventory for secondary pages is therefore **source + operator screenshots + prior smoke**, not fresh authenticated HTML dumps.

---

## 2. Page inventory (summary)

| URL | Title (expected / observed) | Auth | RU baseline | EN remaining | Severity peak |
|-----|-----------------------------|------|-------------|--------------|---------------|
| `/login` | Вход | public | Strong | Email label EN word only | MINOR |
| `/` | Обзор отчетов | required | Strong (Impl 02) | Fixture markers | ACCEPTED_TEST_FIXTURE |
| `/reporting-periods` | Отчетные периоды | required | Strong | — | not a problem (list) |
| `/reporting-periods/3` | Reporting period … | required | Weak | H2/buttons/Details/Actions | **BLOCKER** |
| `/reporting-periods/3/edit` | Edit reporting period | required | Weak | Form chrome EN | **BLOCKER** |
| `/monthly-reports/1` | Monthly report — … | required | Weak | Parent/Preview/Locked/Actions/fields EN | **BLOCKER** |
| `/monthly-reports/1/preview` | Preview | required | Weak | Preview/Back/Print/Snapshot/block titles EN | **BLOCKER** |
| `/monthly-reports/1/blocks` | Report blocks | required | Weak | Parent/Locked/Actions/View | **BLOCKER** |
| `/report-snapshots/1/exports` | Файлы отчета (list) | required | Mixed | Snapshot/export admin EN on detail paths | MAJOR |
| `/report-exports/4` | Файл отчета | required | Strong handoff-facing | Technical details still EN-leaning | MAJOR |
| `/report-exports/4/shares` | Ссылки для клиента | required | Strong | Machine keys in title (`snapshot-1-pdf-v2`) | MAJOR |
| `/health` | Состояние системы | public | Strong | LOCAL_FIXTURE / SAPI | TECHNICAL_INTERNAL / fixture |

---

## 3. Classification legend

| Code | Meaning |
|------|---------|
| **BLOCKER** | Prevents comfortable Russian SEO-manager testing of secondary CRUD/preview |
| **MAJOR** | Confusing but primary A–D flow usable |
| **MINOR** | Cosmetic |
| **ACCEPTED_TEST_FIXTURE** | Demo Client / Demo SEO / LOCAL_FIXTURE_ONLY — keep for now, label clearly |
| **FUTURE_TEMPLATE_SCOPE** | Field model / PDF client template — later waves |
| **TECHNICAL_INTERNAL** | Keep under «Технические детали» |

---

## 4. UI cleanup table (defects)

| Page | Item | Kind | Audience | Action | Severity | Proposed RU |
|------|------|------|----------|--------|----------|-------------|
| Period show | `Reporting period` | UI copy | Manager | translate | BLOCKER | Отчетный период |
| Period show | `Back to list` | UI copy | Manager | translate | BLOCKER | К списку периодов |
| Period show | `Weekly checkpoints` | UI copy | Manager | translate | BLOCKER | Еженедельные заметки |
| Period show | `Monthly report` / `Monthly report content` | UI copy | Manager | translate | BLOCKER | Месячный отчет / Содержание месячного отчета |
| Period show | `Details` / `Actions` / `View` | UI copy | Manager | translate | BLOCKER | Детали / Действия / Открыть |
| Period show | Note «Report blocks / PDF export: not implemented.» | Confusing / stale | Manager | remove or rewrite | MAJOR | Убрать или «Доступно через месячный отчет» |
| Period edit | `Edit reporting period` / `Save changes` / `Create period` | UI copy | Manager | translate | BLOCKER | Редактировать период / Сохранить / Создать период |
| Monthly show | `Monthly report` / `Parent period` / `Report blocks` / `Preview` | UI copy | Manager | translate | BLOCKER | Месячный отчет / К периоду / Блоки отчета / Предпросмотр |
| Monthly show | `Locked` / `Finalized — locked` / `Actions` | UI copy | Manager | translate | BLOCKER | Заблокировано / Финализирован — правки закрыты / Действия |
| Monthly show | `Executive summary` … `Next month plan` labels | UI copy + field model | Manager | translate now; remap later | BLOCKER / FUTURE_TEMPLATE_SCOPE | Краткий вывод / Что сделали / Результаты / Что изменилось / Проблемы и риски / План на следующий месяц |
| Monthly show | Snapshot key / checksum / ID primary | Technical | Admin | hide/collapse | MAJOR | «Технические детали» |
| Preview | `Preview` / `Back to monthly report` / `View report blocks` / `Print view` / `Snapshot` | UI copy | Manager | translate | BLOCKER | Предпросмотр / К месячному отчету / Блоки отчета / Версия для печати / Снимок |
| Preview | Block title map EN | UI copy | Manager | translate | BLOCKER | Same RU section titles as dictionary §6 |
| Blocks index/show | `Report blocks` / `Parent monthly report` / `Locked` / `Actions` / `View` | UI copy | Manager | translate | BLOCKER | Блоки отчета / К месячному отчету / Заблокировано / Действия / Открыть |
| Snapshot detail | Entire chrome EN (`Create snapshot`, `HTML export`, checksums, etc.) | UI copy | Admin | translate + collapse tech | MAJOR | Снимок отчета + «Технические детали» |
| Exports list title | `snapshot-1-pdf-v2` in page title | Machine key | Manager | demote | MAJOR | Человеческое имя файла / «PDF v2» |
| Shares | Title includes export key | Machine key | Manager | demote | MAJOR | Ссылки для клиента — PDF |
| Dashboard/footer | `Demo Client` / `Demo SEO Project` / `LOCAL_FIXTURE_ONLY` | Fixture | Manager | keep as fixture marker | ACCEPTED_TEST_FIXTURE | «Тестовые данные» badge + keep names |
| Dashboard | `Demo Monthly Report` (if shown) | Fixture | Manager | keep | ACCEPTED_TEST_FIXTURE | — |
| Any | `executive_summary` etc. raw keys | Machine key | Manager | hide; show RU title | BLOCKER | Never raw on manager surface |
| Any | `monthly-1-v1` / `snapshot-1-pdf-v2` | Machine key | Admin | technical details | TECHNICAL_INTERNAL | Ключ снимка / Ключ файла |
| Login | `Email` | UI copy | Manager | optional RU | MINOR | Email (acceptable) or Эл. почта |
| Health | SAPI / WordPress row | Technical | Admin | keep | TECHNICAL_INTERNAL | — |

---

## 5. Confusing / risky actions

| Action | Why confusing | Risk | Impl 03 guidance |
|--------|---------------|------|------------------|
| `Create snapshot` / `Re-check / create (idempotent)` | Eng + developer jargon | Accidental re-create noise | RU labels; keep behavior; no schema change |
| `Create styled HTML/PDF` on snapshot page | Competes with manager «Файлы отчета» | Manager may regen PDF | Demote to admin details; do not auto-run |
| `Finalize` / `Reopen` (if EN) | Lifecycle risk | Unlock finalized content | Ensure RU + confirm copy |
| Share create/revoke | Not EN-only; operational risk | Active test link | **Out of Impl 03** — optional Local Share QA Cleanup |
| Stale «PDF export: not implemented» | Lies about current capability | Trust loss | Fix/remove in Impl 03 |

---

## 6. Fixture vs product defects

| Label | Class |
|-------|-------|
| Demo Client / Demo SEO Project / Demo Monthly Report | ACCEPTED_TEST_FIXTURE |
| LOCAL_FIXTURE_ONLY | ACCEPTED_TEST_FIXTURE (footer/banner OK locally) |
| Period 2026-07 finalized / 2026-08 archived+draft | ACCEPTED_TEST_FIXTURE data state |
| Operator-attested active share id **7** `test-first-link` | Local test state — not UI copy defect; cleanup optional later |
| Generic 6 report field keys | Product model gap → FUTURE_TEMPLATE_SCOPE (Nikita / architecture) |

---

## 7. Likely Implementation 03 files

| Path | Why |
|------|-----|
| `app/Views/pages/reporting-periods/show.php` | EN chrome |
| `app/Views/pages/reporting-periods/form.php` / `edit.php` / `create.php` | EN form |
| `app/Views/pages/monthly-reports/show.php` | EN chrome + field labels |
| `app/Views/pages/monthly-reports/form.php` | EN field map |
| `app/Views/pages/report-preview/show.php` | EN preview chrome + titles |
| `app/Views/pages/report-blocks/*.php` | EN list/detail/forms |
| `app/Views/pages/weekly-checkpoints/*.php` | EN secondary |
| `app/Views/pages/report-snapshots/show.php` | EN snapshot admin |
| `app/Views/pages/report-exports/*.php` | Demote machine keys; polish |
| `app/Views/pages/report-export-shares/index.php` | Title/key demotion if needed |
| `app/Views/partials/*` / `layout.php` | Minor fixture badge clarity |
| `public/assets/css/app.css` | Brand token layer (see brand discovery) |
| Controllers only if page titles set in PHP | Title strings |

**Do not touch in Impl 03:** migrations, share create/revoke, PDF regen, client PDF template HTML, Nikita field schema.

---

## 8. Day-1 blocking vs minor

**Day-1 blocking for SEO-manager Russian test of full loop:** period detail/edit, monthly show/edit, preview, blocks — still largely English.

**Not day-1 blocking:** login/dashboard/periods list/exports/shares/health Russian chrome from Impl 01–02; fixture names; `#c8102e` vs live yellow (brand — Major product desire, not copy blocker).

---

## 9. SAFE UNKNOWN

- Exact authenticated HTML of secondary pages at discovery runtime (no session injection this wave).
- Whether operator share id 7 is still active in DB now (operator-attested; not re-probed).
- Whether any view strings come from controllers vs views only (spot-check controllers in Impl 03).
