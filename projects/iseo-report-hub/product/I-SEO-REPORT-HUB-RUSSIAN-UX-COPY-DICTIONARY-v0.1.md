# I-SEO Report Hub — Russian UX Copy Dictionary v0.1

**Status:** COPY / POLICY ONLY — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Wave:** Russian UX and HTML Demo Alignment Charter 01  
**Audience:** SEO managers / specialists (primary); admin_owner (secondary)

---

## 1. Rules

1. Default UI language: **Russian**.  
2. Keep English only in «Технические детали» or developer Health (optional).  
3. Prefer manager words over domain-model words.  
4. Do not put storage paths, checksums, token hashes, or render internals in primary chrome.  
5. Client-facing PDF copy ≠ admin chrome (see §5).  
6. Existing handoff copy pack (RU) remains authority for short/email/internal note bodies — see [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-COPY-PACK-v0.1.md).

---

## 2. Navigation

| Current (EN) | Target (RU) |
|--------------|-------------|
| Dashboard | Главная |
| Reporting periods | Отчетные периоды |
| Health | Состояние системы |
| Logout | Выйти |
| Login | Вход |
| Sign in | Войти |

---

## 3. Dashboard cards / status

| Current (EN) | Target (RU) | Notes |
|--------------|-------------|-------|
| Auth | Вход | Or hide card; show «Вход выполнен» |
| Database | База данных | Prefer admin-only / technical |
| Runtime | Локальный запуск | Prefer admin-only / technical |
| Reporting CRUD | Отчеты | Soften «CRUD» |
| Weekly checkpoints | Еженедельные заметки | Or «Недельные чекпоинты» if specialists know the term |
| Monthly reports | Месячные отчеты | |
| Report blocks | Блоки отчета | |
| Quick links | Быстрые действия | |
| ready / pending | Готово / В работе | Status pills |

### Dashboard target headlines

| Element | RU |
|---------|----|
| Product title | Система отчетов i-SEO |
| Auth ok | Вход выполнен |
| Fixture banner | Тестовые данные |
| Quick: periods | Отчетные периоды |
| Quick: last report | Последний отчет |
| Quick: PDF | Скачать PDF |
| Quick: shares | Ссылки для клиента |

---

## 4. Report / export / share

| Current (EN) | Target (RU) | Visibility |
|--------------|-------------|------------|
| Report exports | Файлы отчета | Primary (alt: Экспорты отчета) |
| Export detail | Файл отчета | Primary |
| Snapshot detail | Снимок отчета | Secondary / technical |
| Monthly report | Месячный отчет | Primary |
| Download PDF | Скачать PDF | Primary |
| Download HTML | Скачать HTML | Technical / archive |
| Public shares | Ссылки для клиента | Primary |
| Public share links | Ссылки для клиента | Primary |
| Shareable | Можно отправлять | Primary |
| Not shareable | Нельзя отправлять | Primary |
| Ready | Готово | Primary |
| Internal only | Только внутри | Badge ok if short |
| PDF artifact | PDF-файл | Prefer without «artifact» |
| HTML artifact | HTML-файл | Demote |
| Create HTML export | Создать HTML-файл | Admin |
| Create PDF export | Создать PDF | Manager if needed |
| All exports | Все файлы | Secondary |
| Client handoff readiness | Готовность к отправке клиенту | Primary |
| Create share for handoff | Создать ссылку для клиента | Primary |
| Optional label | Название ссылки | Primary |
| Active shares | Активные ссылки | Primary |
| Revoked rows | Отозванные ссылки | Secondary (collapsed) |
| Copy pack | Тексты для отправки | Primary |
| Copy short message | Скопировать короткое сообщение | Primary |
| Copy email | Скопировать письмо | Primary |
| Copy internal note | Скопировать внутреннюю заметку | Primary |
| Open shares / copy pack | Открыть ссылки и тексты | Primary |
| Not delivery ready | Не готово к отправке | Primary |
| no active share | Нет активной ссылки | Primary |
| active exists | Есть активная ссылка | Primary |

---

## 5. Technical terms (hide by default)

Show only under **«Технические детали»** (collapsed `<details>` or equivalent):

| Current (EN) | RU label (when shown) |
|--------------|------------------------|
| Snapshot | Снимок |
| Snapshot key | Ключ снимка |
| Checksum / File checksum | Контрольная сумма |
| Source snapshot checksum | Контрольная сумма снимка |
| Render engine | Движок генерации |
| Render target | Тип генерации |
| Source HTML | Исходный HTML |
| Storage path / Storage disk | Путь к файлу / Диск хранения |
| Export key | Ключ файла |
| MIME type | MIME-тип |
| Template id (`iseo_default_v1`) | Шаблон (код) |
| token_hash | (never show plaintext; hash only for admin forensic if ever) |

---

## 6. Client-facing PDF / report titles

| Element | Target RU |
|---------|-----------|
| Document title | SEO-отчет за {месяц год} (e.g. `SEO-отчет за июль 2026`) |
| Section | Краткий вывод |
| Section | Что сделали |
| Section | Результаты |
| Section | Что изменилось |
| Section | Проблемы и риски |
| Section | План на следующий месяц |
| Section | Комментарий специалиста |

**Remove from real client PDF:** `LOCAL_FIXTURE_ONLY`; `file:///` local footer paths; snapshot keys; checksums; block machine keys; render/template internals.

**Fixtures:** may keep obvious test labels; real reports must not.

**Demo client-report.html sections** (резюме, KPI, …) are a structural reference; Implementation may map demo anatomy → charter section list without requiring 1:1 demo section titles.

---

## 7. Login / Health / Footer

| Current | Target |
|---------|--------|
| Login / Local DB-backed authentication… | Вход · Короткая подсказка без «Phase 1A» |
| Email / Password | Email / Пароль |
| Overall / Runtime / PHP / Database… | Состояние системы (admin); менеджеру — опционально |
| Footer: `MARS Active Brain source · Phase 1A skeleton · no DB · runtime not synced` | Truthful local line, e.g. `i-SEO Report Hub · локальный запуск` (exact string TBD in Implementation; must not claim no DB when DB is active) |

---

## 8. Status / badge microcopy

| EN | RU |
|----|----|
| ready | Готово |
| pending | В работе |
| failed | Ошибка |
| revoked | Отозвана |
| expired | Истекла |
| Legacy / not recorded | Устаревший / не записан |
| Recorded template | Шаблон записан |
| Warnings | Предупреждения |
| Readiness checklist | Чек-лист готовности |
