# WPilot Clean Install Checklist v1

**Classification:** Operator checklist — canonical clean-install validation path.  
**Status:** Documentation only — **not executed** in OPS-01.  
**Target release:** `metacode-wpilot` v0.3.0 (schema `0.2.0`)  
**Checkpoint reference:** `8c67478` (+ optional UX-01 working-tree additions)  
**Scope:** Disposable or clearly DEV/test WordPress only. Human-supervised.

---

## Purpose

Зафиксировать воспроизводимый сценарий **чистой установки** WPilot v0.3.0 через WordPress ZIP upload — без FTP, без ручного копирования отдельных файлов, без специальных условий хостинга.

Этот чеклист **не заменяет** runtime sprint evidence. Он описывает, что оператор должен проверить, чтобы доказать deploy reproducibility.

---

## Preflight

- [ ] Подтвердить: целевой сайт — **DEV/test**, не production.
- [ ] Подтвердить: чистый WordPress (новая установка или изолированный disposable instance).
- [ ] Подтвердить: REST API доступен (`/wp-json/` отвечает).
- [ ] Подтвердить: есть recovery-доступ (FTP/DB/hosting panel) на случай fatal при активации.
- [ ] Подтвердить: токены **не** будут вноситься в git, скриншоты публично, или логи CI.
- [ ] Выбрать **package source** и зафиксировать в evidence:
  - **A:** `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0.zip` (22 files, checkpoint `8c67478`, pre-UX-01), или
  - **B:** свежий ZIP из `projects/wpilot/plugin/metacode-wpilot/` (25 files, включает UX-01 + `languages/`, **требует** `metacode-wpilot-ru_RU.mo` для ru_RU).

---

## 1. Чистый WordPress

- [ ] WordPress установлен с нуля или восстановлен в known-clean state.
- [ ] Нет ранее установленного `metacode-wpilot` в `wp-content/plugins/`.
- [ ] Нет остаточных таблиц `wp_wpilot_*` в БД (или зафиксировано, что это fresh DB).
- [ ] `wp-content/uploads/` доступен для записи (потребуется для backup storage).

---

## 2. Установка ZIP

- [ ] Открыть **Plugins → Add New → Upload Plugin**.
- [ ] Загрузить выбранный ZIP (`metacode-wpilot-v0.3.0.zip` или freshly built).
- [ ] Подтвердить: WordPress распознал плагин **MetaCODE WPilot**.
- [ ] Подтвердить: root folder в ZIP = `metacode-wpilot/` (не вложенный repo path).
- [ ] Подтвердить: ZIP **не** содержит `.git`, credentials, local tokens, sprint evidence, `.recovery-temp`, operator STORAGE paths.
- [ ] Если package source = UX-01 tree: подтвердить наличие `admin/class-wpilot-admin-ui-model.php` и `languages/` в установленной копии.

---

## 3. Активация

- [ ] Активировать плагин через WordPress UI.
- [ ] Подтвердить: **нет fatal error** при активации.
- [ ] Подтвердить: активация **не** изменила контент сайта.
- [ ] Подтвердить: пункт меню **Settings → MetaCODE WPilot** появился.

---

## 4. Создание таблиц

- [ ] Открыть admin page или выполнить любой schema-touching REST call.
- [ ] Подтвердить: таблицы созданы/обновлены до schema `0.2.0`:
  - `wp_wpilot_backups`
  - `wp_wpilot_audit_log`
- [ ] Подтвердить: `WPilot_Schema::maybe_upgrade()` не вызывает ошибок (проверить debug log при `WP_DEBUG`).

---

## 5. Проверка Settings

- [ ] Открыть **Settings → MetaCODE WPilot**.
- [ ] Подтвердить default state:
  - Bridge: **disabled**
  - Write enabled: **disabled**
  - Emergency disabled: **false**
  - Token: **not generated**
  - DEV/test confirmation: **not confirmed**
- [ ] Подтвердить: admin UI отображает v0.3.0 runtime summary (если UX-01 package — Runtime Status / Proven Operations panels).
- [ ] Включить DEV/test confirmation + bridge + write readiness (по operator policy) **только если** REST/write операции авторизованы. Для production token-only onboarding (RC6+): токен может быть создан **без** DEV confirmation и **без** bridge; bridge/writes остаются выключенными до отдельного charter.
- [ ] Сгенерировать token; скопировать plaintext **один раз**; сохранить только в approved local storage.
- [ ] Обновить страницу — plaintext token **не** отображается повторно.
- [ ] Подтвердить: после генерации токена `bridge_enabled` / `write_enabled` / `dev_confirmed` **не** изменились сами по себе (RC6).

---

## 6. Проверка REST

- [ ] `GET /wp-json/wpilot/v1/ping` — success без token.
- [ ] `GET /wp-json/wpilot/v1/site-info` без token — refusal (`AUTH_MISSING` или equivalent).
- [ ] `GET /wp-json/wpilot/v1/site-info` с valid token — success envelope (`ok`, `data`, `meta`).
- [ ] Проверить read endpoints (8): `site-info`, `themes`, `plugins`, `pages`, `pages/{id}`, `pages/{id}/structure`, `indexing-state`.
- [ ] Проверить analysis endpoint: `POST /pages/{id}/replace-text/dry-run` (write_enabled required).
- [ ] Подтвердить: refusal codes детерминированы (`BRIDGE_DISABLED`, `AUTH_INVALID`, `TOKEN_REVOKED`, `EMERGENCY_DISABLED`).

---

## 7. Проверка Runtime Dashboard

- [ ] Admin page показывает namespace `wpilot/v1`.
- [ ] Endpoint inventory соответствует registered routes (8 read + 1 analysis + 3 proven write).
- [ ] Runtime maturity label: `proven_content_writes` (UX-01 UI) или equivalent в legacy admin copy.
- [ ] Emergency disable блокирует authenticated endpoints; clear emergency восстанавливает prior bridge state rules.

---

## 8. Проверка Localization

- [ ] Подтвердить `Text Domain: metacode-wpilot` и `Domain Path: /languages` в plugin header.
- [ ] Подтвердить `load_plugin_textdomain()` вызывается при init (UX-01+ packages).
- [ ] Для `ru_RU` locale:
  - [ ] `languages/metacode-wpilot-ru_RU.po` присутствует в package (UX-01+).
  - [ ] `languages/metacode-wpilot-ru_RU.mo` **скомпилирован и присутствует** (иначе — English fallback; gap, не pass).
  - [ ] Admin UI strings отображаются на русском (выборочная проверка: warning notice, Token Control, REST Endpoints headings).
- [ ] Для `en_US` — source strings без regression.

---

## 9. Проверка Backup

- [ ] На safe DEV page: `POST /wp-json/wpilot/v1/pages/{id}/backups` с valid token + write_enabled.
- [ ] Подтвердить: backup row в `wp_wpilot_backups`.
- [ ] Подтвердить: checksum `sha256:` в response.
- [ ] Подтвердить: audit event `backup_requested` → `backup_created` в `wp_wpilot_audit_log`.
- [ ] Подтвердить: `post_content` на странице **не изменился** после backup-only call.

---

## 10. Проверка Rollback

- [ ] После proven write (scoped-replace) или с existing backup: `POST /wp-json/wpilot/v1/pages/{id}/rollback`.
- [ ] Подтвердить: `post_content` восстановлен к backup checksum.
- [ ] Подтвердить: `validation_result: passed` (или equivalent success signal).
- [ ] Подтвердить: audit trail содержит `rollback_requested` → `rollback_verified`.
- [ ] На WPBakery page (если доступна): shortcode counts не нарушены после rollback.

**Optional full lifecycle (proven sprint parity):**

- [ ] `inspect` → `backup` → `scoped-replace` → validate → `rollback` на одной disposable DEV page.

---

## Stop Conditions

Остановить validation и эскалировать, если:

- Сайт оказался production или production-like без explicit charter.
- Token plaintext попал в git, публичный канал, или скриншот без redaction.
- Fatal error при активации или при первом REST call.
- ZIP package не совпадает с ожидаемым file inventory (missing `class-wpilot-admin-ui-model.php` при UX-01 bootstrap).
- Любой endpoint вне documented inventory отвечает как implemented write surface.

---

## Completion Criteria

Clean install считается **proven** только если **все** секции 1–10 пройдены с сохранённым evidence (screenshots, JSON responses, DB table checks, package hash/path).

До прохождения этого чеклиста:

- Deploy reproducibility = **not proven**
- ZIP installation = **SAFE UNKNOWN** (или partial — только packaging artifact exists)
- Recommended release status остаётся **B — Internal Release Ready**, не **C**.

---

## Evidence Artifacts (operator-local)

Рекомендуемое хранение (не в git):

```
X:\AI MARS STORAGE\wpilot\clean-install\<site>\<timestamp>\
  package-source.txt
  zip-sha256.txt
  activation-notes.txt
  ping.json
  site-info.json
  backup-result.json
  scoped-replace-result.json  (optional)
  rollback-result.json
  admin-screenshots/
```

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Date | 2026-06-19 |
| Executed | No — OPS-01 canonical checklist only |
| Replaces dev-install-checklist-v0 | No — complements for v0.3.0 clean install |
