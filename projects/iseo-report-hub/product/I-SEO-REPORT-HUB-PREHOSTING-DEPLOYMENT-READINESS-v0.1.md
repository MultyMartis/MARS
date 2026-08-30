# i-SEO Report Hub — Pre-hosting Deployment Readiness v0.1

**Для:** Андрей (ручная выкладка)  
**Поддомен:** `https://reports.i-seo.su`  
**SSL:** уже создан оператором  
**Дата:** 2026-08-21  
**Связанные карты:** [FILE-PACKAGE-MAP](I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md) · [DB-URL-PATH-AUDIT](I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md)

Это **инструкция готовности**. Агент **не** загружал файлы на хостинг и **не** менял production.

---

## Краткий ответ на ваши вопросы

| Вопрос | Ответ |
|--------|--------|
| Можно ли выкладывать руками? | **Да**, после выполнения чек-листа ниже. Есть ATTENTION: нет `public/.htaccess` в source — rewrite нужно добавить вручную на хосте. |
| Что копировать? | Содержимое `app-source` (см. include), **не** весь MARS и **не** runtime «как есть». |
| Куда должен смотреть поддомен? | **`public`** |
| PHP? | **8.3** + расширения ниже |
| Что менять в config? | Создать на хосте **`.env.local`** (имя файла обязательно) с production `APP_URL` и DB credentials |
| Менять URL в БД как WordPress? | **Нет** |
| `https://proverka.example`? | Demo URL сайта клиента в `sites.url`, не адрес приложения |

---

## Что брать с локалки

### Source (рекомендуется)

`X:\AI MARS\projects\iseo-report-hub\app-source`

### Runtime (только для сверки / export DB, не как zip «всего сайта»)

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub`  
Локальный URL: `http://iseo-report-hub.test/`  
БД: `iseo_report_hub_dev`

### Финальная рекомендация

Подготовить чистую папку деплоя из **app-source** по [FILE-PACKAGE-MAP](I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md).  
БД экспортировать отдельно из Laragon/phpMyAdmin.

---

## Куда должен смотреть поддомен

```
Document root = <корень_сайта_на_хосте>/public
```

Пример структуры на хосте:

```
/iseo-report-hub/          ← корень приложения (не web root)
  app/
  config/
  storage/
  .env.local               ← создать на хосте
  public/                  ← СЮДА смотрит reports.i-seo.su
    index.php
    assets/
    .htaccess              ← создать вручную (см. ниже)
```

**Никогда** не направлять поддомен на корень проекта.

---

## PHP

| Требование | Значение |
|------------|----------|
| Версия | **PHP 8.3** (локально проверено 8.3.30) |
| Обязательные расширения | `pdo`, `pdo_mysql`, `mbstring`, `json`, `openssl`, `fileinfo`, `session` |
| Желательные | `curl`, `intl`, `gd`, `dom`/`xml` |
| Позже (PDF/архивы) | `zip`; `imagick`/`gd` — только если снова включат PDF/image pipeline |

**PDF отложен:** генерация PDF завязана на локальный Edge/Chrome headless (пути Windows в коде). На shared hosting PDF **не ожидать**. MVP без PDF допустим.

Composer: **не используется** — `composer install` на хосте не нужен.

---

## Что менять в config / `.env`

Приложение читает **только файл `.env.local`** в корне приложения (`ConfigService`).  
Файл с именем `.env` **не подхватится**.

### Шаблон для хоста (placeholders — без локальных секретов)

```env
APP_NAME="i-SEO Report Hub"
APP_ENV=production
APP_DEBUG=false
APP_URL=https://reports.i-seo.su

DB_HOST=CHANGE_ME_HOST
DB_PORT=3306
DB_DATABASE=CHANGE_ME_DB
DB_USERNAME=CHANGE_ME_USER
DB_PASSWORD=CHANGE_ME_PASSWORD
```

### Что взять / не брать с локалки

| Действие | |
|----------|--|
| **Не копировать** локальный `.env.local` | там `APP_URL=http://iseo-report-hub.test` и локальные DB_* |
| **Создать новый** `.env.local` на хосте | значения из панели хостинга |
| `UPLOAD_PATH` / `LOG_PATH` из `.env.example` | в коде ConfigService **не читаются**; storage path = `storage/` относительно корня |

Сессия: в `bootstrap.php` уже `cookie_httponly` + `SameSite=Lax`. Флага `cookie_secure` в коде нет — для HTTPS-демо обычно login работает; усиление Secure — отдельный code fix при желании.

`APP_URL` используется для абсолютных share-ссылок (PDF/share сейчас 0 рядов) — всё равно выставить правильно.

---

## Что в БД менять

См. полный аудит: [DB-URL-PATH-AUDIT](I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md)

| Тема | Вердикт |
|------|---------|
| WP-like URL replace | **Нет** |
| System app URL в БД | **Нет** |
| `sites.url` = `https://proverka.example` | demo content |
| Локальные `X:\` пути | **не найдены** |
| После импорта | только `.env.local` + smoke |

---

## Что не загружать

- `.env.local` с локалки  
- `tools/` (seed/migrate/admin CLI)  
- `docs/` app-source  
- логи / cache / uploads содержимое  
- runtime smoke PHP в `storage/`  
- старые `storage/exports/**`  
- backups, evidence, screenshots, dump SQL в `public/`  
- весь git / MARS monorepo  

Подробно: [FILE-PACKAGE-MAP](I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md)

---

## DB export / import

1. **Экспорт локально:** БД `iseo_report_hub_dev` (структура + данные), charset **utf8mb4**.  
   Инструмент: phpMyAdmin (Laragon) или `mysqldump`.  
2. **На хосте:** создать пустую БД в панели → импортировать dump.  
   Если панель уже создала БД — импорт **без** лишнего `CREATE DATABASE`, либо править dump под имя БД хоста.  
3. В `.env.local` прописать credentials хоста.  
4. Миграции на хосте для текущего демо **не гонять** — импортируете уже мигрированную локальную БД.

### Демо-доступ после импорта

- Логин: `test@mail.ru`  
- Пароль: `test` (локальный демо)  

**Риск:** поддомен публичный — сразу сменить пароль и/или закрыть Basic Auth / IP restrict, если команда не готова к открытому доступу.

---

## Storage / права

Нужна запись PHP-пользователем в:

- `storage/`
- `storage/exports/` (создать пустым)
- `storage/logs/`
- `storage/cache/`
- `storage/uploads/`

Права: «writable for PHP» через панель/файловый менеджер. Избегать `777`, если панель даёт безопасный вариант (владелец = PHP user).

Сессии PHP — обычно системный session save path хостинга (не обязательно писать в `storage/`).

---

## Security notes

1. Document root = **только** `public`.  
2. Не заливать `tools/` на хост (или удалить после любых локальных операций — на проде не нужны).  
3. Не класть SQL dump / `.env.local` в `public`.  
4. `APP_DEBUG=false` на хосте.  
5. Пароль `test` — только временный демо-доступ.  
6. PDF/Chromium на shared hosting — не рассчитывать.

### Apache rewrite (ATTENTION)

В `app-source/public` **нет** `.htaccess`. Без rewrite маршруты `/login`, `/health` и т.д. дадут 404.

Создайте `public/.htaccess` на хосте (типовой вариант):

```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^ index.php [L]
```

(Если панель Nginx — аналог `try_files $uri /index.php;` в конфиге сайта.)

---

## Smoke checklist после загрузки

1. PHP **8.3** в панели.  
2. Document root → `public`.  
3. Файлы залиты (без exclude).  
4. БД импортирована; `.env.local` создан.  
5. `storage` writable; есть `storage/exports`.  
6. Открыть:
   - `https://reports.i-seo.su/health`
   - `https://reports.i-seo.su/login`
7. Логин `test@mail.ru` / `test`.  
8. Проверить:
   - dashboard: `ПРОВЕРКА.рф`
   - `/reporting-periods`
   - `/monthly-reports/7` и `/monthly-reports/7/preview`
   - `/monthly-reports/8` и `/monthly-reports/8/preview`
   - `/monthly-reports/8/work-entries/create`
9. PDF / share / export — **не** ожидать.  
10. Если 500 → `.env.local`, PHP, DB, storage, debug.  
11. Если 404 → document root / rewrite.  
12. Если login fail → импорт БД / session cookie (Secure/HTTPS).

---

## Локальная проверка перед выкладкой (уже сделана в readiness wave)

| Проверка | Результат |
|----------|-----------|
| `/health` | 200 |
| `/login` | 200 |
| `/` без сессии | 302 (redirect) |
| DB URL scan | без WP-like app URL |

---

## Следующий шаг оператора

**Operator Manual Hosting Upload** на `reports.i-seo.su` по этому документу.  
Опционально позже: charter на добавление `public/.htaccess` в `app-source` и `cookie_secure` для HTTPS.
