# i-SEO Report Hub — Pre-hosting DB URL / Path Audit v0.1

**Дата:** 2026-08-21  
**БД:** `iseo_report_hub_dev` @ `127.0.0.1:3306` (read-only scan)  
**Секреты / password hashes / share tokens:** не печатались

---

## Прямой ответ оператору

**Массовая замена URL в БД как в WordPress (`siteurl` / `home`) — НЕ нужна.**

- Таблиц `wp_options` / системного «адреса приложения» в БД **нет**.
- Базовый URL приложения берётся из **`.env.local` → `APP_URL`** (`ConfigService`), не из БД.
- Литералов `http://iseo-report-hub.test` / `https://iseo-report-hub.test` в текстовых колонках приложения: **0**.
- Абсолютных путей `X:\`, `MARS-Localhost`, `AI MARS` в текстовых колонках: **не найдено**.

---

## Объём скана

| Метрика | Значение |
|---------|----------|
| Таблиц | 19 |
| Текстовых колонок (без sensitive) | 106 |
| Паттернов | local app URL, host domain, localhost, 127.0.0.1, X:\, MARS-Localhost, AI MARS, storage\, storage/, http(s), proverka.example, ПРОВЕРКА.рф, ПРОВЕРКА.рa, Demo Client |
| Sensitive колонки | пропущены (`password*`, `*token*`, `*hash*`, `secret`, `csrf`) |

Evidence (не в git):  
`X:\AI MARS STORAGE\incoming\iseo-report-hub\prehosting-deployment-readiness-01\20260821-143230\db-url-path-scan.json`

---

## Состояние демо-контента (публичные счётчики)

| Таблица | Count |
|-------|-------|
| users | 3 |
| clients / projects / sites | 1 / 1 / 1 |
| reporting_periods | 2 |
| monthly_report_contents | 2 (id **7** finalized, id **8** in_progress) |
| report_blocks | 12 |
| report_snapshots / report_exports / report_export_shares | 0 / 0 / 0 |

Пользователи (email only): `admin@iseo-report-hub.test`, `polygon-ws@mail.ru`, `test@mail.ru`.

---

## Находки и классификация

### 1. System URL приложения — действий нет

| Проверка | Результат |
|----------|-----------|
| WP-like options | нет |
| `APP_URL` в строках БД | нет |
| Замена после импорта | **не требуется** |

`APP_URL` для хоста задать только в **`.env.local`**: `https://reports.i-seo.su`.

---

### 2. Demo / business content — оставить (или править руками позже)

| Таблица.колонка | Паттерн | Класс | Действие |
|----------------|---------|-------|----------|
| `sites.url` | `https://proverka.example` | demo site URL клиента | **не** app URL; можно оставить для демо или сменить вручную на реальный URL клиента |
| `sites.label`, `clients.name`, `projects.name`, titles/summaries/bodies | `ПРОВЕРКА.рф` | demo display name | оставить |
| `clients.notes` | содержит строку `Demo Client` | остаточный текст в notes | **не блокирует** хостинг; опционально почистить руками / отдельным polish |
| `users.email` = `admin@iseo-report-hub.test` | локальный email-домен | demo identity | не system URL; менять не обязательно для демо |

Строк с опечаткой `ПРОВЕРКА.рa` в скане как отдельный hit по паттерну не зафиксировано (сценарий уже на `.рф`).

---

### 3. Local filesystem paths — действий нет для импорта

| Таблица.колонка | Паттерн | Класс | Действие |
|----------------|---------|-------|----------|
| `audit_log.metadata_json` | относительные `storage/...` | audit meta прошлых export (строки есть, файлов/экспортов в БД = 0) | **не** абсолютные Windows-пути; замена не нужна |
| — | `X:\` / `MARS-Localhost` | — | **нет hits** |

Пустые каталоги runtime `storage/exports/reports/monthly-1/...` на хост **не копировать**.

---

### 4. Localhost / IP в аудите — no action

| Таблица.колонка | Паттерн | Класс |
|----------------|---------|-------|
| `audit_log.ip_address` | `127.0.0.1` | исторические IP локальных сессий |

После импорта старые audit-строки можно оставить; на работу UI не влияют.

---

### 5. Sensitive

Password hashes / share tokens **не сканировались и не выводились**.  
Пароль демо-пользователя `test` — известный локальный демо-пароль (не печатаем hash).

---

## Вывод для выкладки

1. Экспорт/импорт БД `iseo_report_hub_dev` **без** search-replace URL.
2. На хосте выставить `APP_URL=https://reports.i-seo.su` в `.env.local`.
3. `https://proverka.example` — поле сайта демо-сценария, не адрес Report Hub.
4. PDF/export/share в БД пустые — файловых артефактов экспорта тащить не нужно.
