# i-SEO Report Hub — App Pages Visual QA Inventory v0.1

**project_id:** `iseo-report-hub`  
**Wave:** App Pages Visual QA Preparation 01  
**Purpose:** карта экранов для ручной визуальной проверки оператором  
**Source of routes:** `app-source/app/routes.php` + views/controllers  
**Local base URL:** `http://iseo-report-hub.test/`  
**Login (local):** `polygon-ws@mail.ru` — пароль не печатать  
**PDF / export alignment:** отложены оператором (см. § Excluded)

---

## Audience legend

| Code | Meaning |
|------|---------|
| **client-facing** | то, что видит клиент / документ для клиента |
| **manager/internal** | рабочий экран менеджера / SEO |
| **admin/system** | служебное / health |
| **export/share internal** | файлы отчёта и ссылки (внутренний UI) |
| **auth/error/empty** | вход, ошибки, пустые состояния |

---

## P0 — обязательные скриншоты

| # | Route | Purpose | Audience | Login | Screenshot | Risk / what to check |
|---|-------|---------|----------|-------|------------|----------------------|
| 1 | `/login` | Вход | auth | no | **P0** | Форма, русский текст, нет debug EN |
| 2 | `/` | Главная (dashboard) | manager | yes | **P0** | Sidebar + topbar, статусы, нет токенов |
| 3 | `/reporting-periods` | Список отчётных периодов («список отчётов») | manager | yes | **P0** | Таблица/карточки, статусы, навигация |
| 4 | `/monthly-reports/1` | Карточка месячного отчёта (финализирован) | manager | yes | **P0** | Блокировка, финализация UI, работы, кнопки |
| 5 | `/monthly-reports/1` → секция `#work-entries` | Работы за месяц на карточке | manager | yes | **P0** | Карточки работ, бейджи, CTA (без Save) |
| 6 | `/monthly-reports/1/work-entries/create` | Форма новой работы | manager | yes | **P0** | Borders полей, русский, **не сохранять** |
| 7 | `/monthly-report-work-entries/1/edit` | Редактирование существующей работы | manager | yes | **P0** | Форма edit; **не сохранять** в этом проходе |
| 8 | `/monthly-reports/1/assembly-preview` | Сборка черновика из работ | manager | yes | **P0** | Иерархия, lock banner, **не Apply** |
| 9 | `/monthly-reports/1/preview` | Клиентский предпросмотр | client-facing (+ manager view) | yes | **P0** | Документный вид, без admin-кнопок |
| 10 | `/monthly-reports/1/preview/print` | Печатный предпросмотр | client-facing | yes | **P0** | Document-like, без sidebar-шума |
| 11 | `/report-snapshots/1/exports` | Список файлов экспорта | export/share | yes | **P0** | Список, статусы; **не генерировать** |
| 12 | `/report-exports/4` | Карточка export 4 | export/share | yes | **P0** | Метаданные без полного secret; **не download если не нужно** |
| 13 | `/report-exports/4/shares` | Ссылки для клиента | export/share | yes | **P0** | **Не создавать/revoke**; не копировать token в заметки |

---

## P1 — полезные скриншоты

| # | Route | Purpose | Audience | Login | Screenshot | Notes |
|---|-------|---------|----------|-------|------------|-------|
| 14 | `/reporting-periods/1` | Деталь периода | manager | yes | **P1** | Связки с weekly / monthly |
| 15 | `/reporting-periods/1/weekly-checkpoints` | Еженедельные заметки | manager | yes | **P1** | Список W1–W4 |
| 16 | `/monthly-reports/1/blocks` | Блоки отчёта | manager | yes | **P1** | 6 блоков |
| 17 | `/monthly-reports/5` | Draft / empty отчёт | empty | yes | **P1** | Пустые работы/блоки |
| 18 | `/monthly-reports/5/preview` | Preview пустого draft | client-facing / empty | yes | **P1** | Empty document state |
| 19 | `/report-snapshots/1` | Карточка снимка | export/share | yes | **P1** | Snapshot metadata |
| 20 | `/health` | Состояние системы | admin/system | no* | **P1** | Служебный экран; *доступен без login в sidebar guest |

\* `/health` в sidebar виден и без входа; не считать «продакшен health».

---

## P2 — опционально

| # | Route | Purpose | Audience | Priority |
|---|-------|---------|----------|----------|
| 21 | `/monthly-reports/1/edit` | Edit monthly (если unlocked — у id 1 обычно locked) | manager | **P2** |
| 22 | `/report-blocks/{id}` / edit | Деталь/edit блока | manager | **P2** |
| 23 | `/weekly-checkpoints/{id}` | Деталь checkpoint | manager | **P2** |
| 24 | `/reporting-periods/create` | Create period form | manager | **P2** — **не submit** |
| 25 | `/not-found` via unknown URL e.g. `/no-such-page-qa` | 404 | auth/error | **P2** |
| 26 | Unauthed hit `/monthly-reports/1` | Redirect to login | auth | **P2** |

---

## Export / share / public — special rules

| Route | Rule for this QA wave |
|-------|------------------------|
| `/share/report/{64-hex}` | **Не открывать по токену** в этом проходе. Не печатать token. |
| POST export generate (pdf/html/styled) | **Запрещено** |
| POST share create / revoke | **Запрещено** |
| Download export 4 | Опционально только просмотр UI; файл PDF не «регенерировать» |

---

## Auth / logout

| Route | Method | Notes |
|-------|--------|-------|
| `/login` | GET | Форма |
| `/login` | POST | Не скриншотить ошибку с паролем; при ошибке — только UI сообщения |
| `/logout` | GET | Безопасный выход; после прохода можно выйти |

---

## Catalogue / settings

Отдельных страниц каталога SEO (`/seo-work-…`) **нет** в текущих routes. Каталог виден как summary / selects внутри work entry forms. Отдельный system settings UI **отсутствует**.

---

## Excluded from this visual QA (operator decision)

- PDF regeneration  
- New export row / export HTML alignment implementation  
- Change to export 4 artifact  
- Client preview → PDF/export pipeline  
- Any POST that mutates DB (apply, finalize, reopen, save, share, export)

---

## Sidebar map (manager)

Из `partials/sidebar.php`:

1. Главная → `/`  
2. Отчетные периоды → `/reporting-periods`  
3. Файлы отчета → `/report-snapshots/1/exports`  
4. Ссылки для клиента → `/report-exports/4/shares`  
5. Состояние системы → `/health`

Клиентский preview **не** в sidebar — открывается с карточки месячного отчёта.
