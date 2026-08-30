# i-SEO Report Hub — Pre-hosting Readiness Fix Result v0.1

**Дата:** 2026-08-24  
**Волна:** Pre-hosting Readiness Fix 01  
**Вердикт:** `PREHOSTING READINESS FIX PASS`

---

## 1. Что исправлено

- В canonical source добавлен `app-source/public/.htaccess`.
- Точный файл синхронизирован в local runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public\.htaccess`.
- Apache получает стандартный front-controller routing из каталога `public`: существующие файлы и каталоги отдаются напрямую, остальные запросы направляются в `index.php`.
- `DirectoryIndex index.php` задаёт входной файл, `Options -Indexes` отключает listing каталогов.
- Project-root rewrite через `/public` не добавлялся: source truth сохраняет безопасную схему **document root = `public`**.

Файл не содержит секретов, host credentials, доменных хаков или локальных абсолютных путей.

---

## 2. Почему `.htaccess` должен быть в source

Rewrite является частью исполняемого deployment baseline, а не ручной настройкой конкретной выкладки. Хранение `public/.htaccess` в `app-source`:

1. сохраняет правило вместе с front controller;
2. обеспечивает одинаковый source → runtime sync;
3. исключает зависимость от файла, созданного только вручную на host;
4. даёт оператору точный allowlisted файл для дозагрузки.

---

## 3. Содержимое и границы

Правило:

- не перехватывает существующие assets и каталоги (`!-f`, `!-d`);
- не содержит project-root redirect;
- не добавляет HTTPS, domain или hosting-specific rewrites;
- не затрагивает `.env.local`, storage, tools, DB, export/share/PDF.

`Options -Indexes` является обычным Apache hardening и успешно прошёл local Apache smoke. Если конкретный host запрещает директиву `Options` через `AllowOverride`, Apache может вернуть 500. В таком подтверждённом случае альтернативой будет убрать **только** строку `Options -Indexes`, сохранив `DirectoryIndex` и rewrite block, но изменение должно сначала попасть в canonical source отдельной точной волной и затем синхронизироваться; host-only ручной drift не является нормой.

---

## 4. Operator host upload

Если document root host настроен на каталог приложения `public`, при необходимости дозалить один файл:

- source: `projects/iseo-report-hub/app-source/public/.htaccess`;
- host: `<document-root>/.htaccess`, то есть физически host `public/.htaccess`.

Если host всё ещё использует `public_html` как document root, а приложение расположено под ним отдельным каталогом, этот `public/.htaccess` **не является** заменой project-root redirect. Не следует помещать его в произвольный `public_html` как root redirect. Рекомендуемая структура остаётся: document root subdomain `reports.i-seo.su` указывает непосредственно на application `public`.

---

## 5. Deployment hygiene

- Источник выкладки: `app-source`, не local runtime целиком.
- Host runtime требует отдельный некоммитимый `.env.local` с production `APP_*` / `DB_*`; source `.htaccess` его не заменяет.
- `tools/` исключается из host upload.
- PHP: **8.3** с ранее зафиксированными обязательными расширениями.
- WordPress-подобная замена URL в DB не нужна.
- `storage/` writable policy и `APP_DEBUG=false` остаются обязательными host checks.
- Host upload в этой волне не выполнялся.
- PDF/export/share остаются parked; новых ожиданий или DB rows эта волна не создаёт.

---

## 6. Local validation

- source/runtime SHA-256 совпадает: `90f735bade70b91c1f1090ea6b27d255d198ae6fdbf6f3f2bc88a5f7aad8fcb9`;
- `/health`, `/login`, authenticated dashboard, periods, monthly 7/8, previews и work-entry create: HTTP 200;
- anonymous `/`: HTTP 302;
- DB table counts до/после совпали;
- snapshots/exports/shares: `0 / 0 / 0`;
- local development remains ready.

---

## 7. Следующее действие

`I-SEO Report Hub — Production Config Normalization 01`
