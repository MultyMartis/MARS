# i-SEO Report Hub — Pre-hosting File Package Map v0.1

**Дата:** 2026-08-21  
**Назначение:** точная карта файлов для ручной выкладки на `reports.i-seo.su`  
**Статус:** readiness docs only — **не** upload, **не** mutation runtime/DB

---

## Источники

| Роль | Путь |
|------|------|
| **Канонический source (брать отсюда)** | `X:\AI MARS\projects\iseo-report-hub\app-source` |
| **Local runtime (не пакет для хоста)** | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` |
| **Document root на хосте** | `<site-root>/public` |

**Итог:** копировать **содержимое `app-source`**, а не весь репозиторий MARS и не «как есть» runtime (в runtime есть `.env.local`, логи Apache, smoke-скрипты, пустые хвосты `storage/exports`).

Composer / `vendor/` — **нет** (приложение без Composer).

---

## Что включать (include)

Скопировать в корень сайта на хостинге:

| Путь | Зачем |
|------|--------|
| `app/` | PHP-приложение, views, services |
| `public/` | front controller + assets — **document root** |
| `config/` | `*.example.php` defaults (секретов нет) |
| `storage/` | скелет каталогов + `.gitignore` / `.keep` |
| `.env.example` | шаблон имён переменных (не секреты) |
| `.gitignore` | опционально |
| `README.md` | опционально |

Дополнительно на хосте **создать вручную**:

| Путь | Зачем |
|------|--------|
| `.env.local` | **именно это имя** читает `ConfigService` (не `.env`) |
| `storage/exports/` (+ `storage/exports/reports/` при желании) | для будущего PDF/export; сейчас пусто |
| `public/.htaccess` | в source **нет**; нужен для Apache rewrite (см. readiness doc) |

`database/` — **можно** положить вне web root как справочник миграций; для демо-импорта уже готовой БД **не обязателен**.

---

## Что не загружать (exclude)

| Путь / класс | Почему |
|--------------|--------|
| `.env.local` с локалки | локальные DB/APP_URL |
| любой `.env` с секретами | не тащить |
| `tools/` | CLI seed/migrate/admin; на проде опасно и не нужны |
| `docs/` внутри app-source | MARS/dev docs, не runtime |
| `storage/logs/*` (кроме `.keep`) | локальные логи |
| `storage/cache/*` (кроме `.keep`) | локальный cache |
| `storage/uploads/*` (кроме `.keep`) | локальные uploads |
| runtime `storage/exports/**` | хвосты старых путей; в БД exports = 0 |
| runtime `storage/_read-export-meta.php`, `storage/_smoke-export-html-01.php` | локальные smoke |
| `vendor/`, `node_modules/`, `composer.*` | отсутствуют / не нужны |
| `.git/` | не для хоста |
| MARS `reports/`, `product/`, evidence, backups SQL, screenshots | не app runtime |
| dump SQL внутрь `public/` | никогда |

---

## Рекомендуемый способ упаковки

1. Создать чистую папку, например `deploy-iseo-report-hub/`.
2. Скопировать из `app-source`: `app`, `public`, `config`, `storage` (только скелет), `.env.example`.
3. **Не** копировать `tools/`, `docs/`, `.env.local`.
4. Создать пустые `storage/exports` и `storage/exports/reports`.
5. Подготовить текст `.env.local` для хоста (placeholders → реальные значения панели).
6. Добавить `public/.htaccess` (см. readiness).
7. Залить на хостинг так, чтобы document root поддомена = `public`.

---

## Source vs runtime (кратко)

| | Source | Runtime |
|--|--------|---------|
| Файлов (примерно) | ~142 | ~147 |
| `.env.local` | нет | есть (локальный) |
| `storage/exports` | нет | пустые каталоги monthly-1 |
| Apache logs / smoke PHP | нет | есть |
| Приложение | SoT | копия + локальные хвосты |

---

## Document root

**Обязательно:** `…/public`  
**Запрещено:** корень проекта (`app/`, `storage/`, `config/`, `.env.local` не должны быть web-root).

Front controller: `public/index.php`. Отдельный `public/health.php` существует, но основной health — маршрут `/health` через router.
