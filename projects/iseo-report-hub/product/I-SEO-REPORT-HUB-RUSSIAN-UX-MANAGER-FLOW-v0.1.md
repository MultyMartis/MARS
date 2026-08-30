# I-SEO Report Hub — Russian UX Manager Flow v0.1

**Status:** PRODUCT UX TARGET — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Wave:** Russian UX and HTML Demo Alignment Charter 01

---

## 1. Target simple flow

1. **Главная**  
2. **Отчетные периоды**  
3. **Отчет за июль 2026** (пример периода)  
4. **Файлы отчета**  
5. **PDF готов**  
6. **Создать ссылку для клиента**  
7. **Скопировать сообщение**  
8. **Отправить клиенту вручную** (вне системы — Telegram / email)

PHP engine, DB, snapshots, exports, shares remain the backend path; UI must not force managers through technical vocabulary.

---

## 2. Screen A — Главная

**Purpose:** Orient + jump to work.

**Show:**
- «Система отчетов i-SEO»
- «Вход выполнен»
- «Тестовые данные» (when fixture / non-production data)
- Quick buttons:
  - Отчетные периоды
  - Последний отчет
  - Скачать PDF (deep-link to recommended export when known)
  - Ссылки для клиента

**Hide / demote:** Auth/Database/Runtime/CRUD status cards as primary grid; role dumps; Phase 1A notes.

**User:** SEO manager (primary).

---

## 3. Screen B — Отчет за месяц

**Purpose:** Understand one report at a glance.

**Show:**
- Клиент
- Проект
- Период
- Статус
- Основные блоки (human titles)
- Buttons:
  - Открыть файлы отчета
  - Скачать PDF
  - Ссылки для клиента

**Hide / demote:** Snapshot keys, checksums, `LOCAL_FIXTURE_ONLY` in titles for real reports, machine `block_key` as primary.

**User:** SEO manager / specialist.

---

## 4. Screen C — Файлы отчета

**Purpose:** One clear recommended client file.

**Show:**
- Primary card: **PDF для клиента** (shareable styled PDF when eligible)
- Status: Готово / Нельзя отправлять
- Actions: Скачать PDF · Ссылки для клиента

**Hide / demote:**
- Wide technical table as the first UI
- Legacy HTML/PDF rows → «Архив / технические версии»
- Render / template code columns on primary surface

**User:** SEO manager.

---

## 5. Screen D — Отправка клиенту

**Purpose:** Create link + copy texts.

**Show:**
- Readiness checklist (Russian)
- Active link status (есть / нет; срок)
- Button: Создать ссылку для клиента
- Optional: Название ссылки
- After create (once):
  - Public URL (once)
  - Короткое сообщение
  - Письмо
  - Внутренняя заметка
  - Copy buttons

**Hide / demote:**
- Revoked rows as default noisy list → collapsed «Отозванные ссылки»
- Export key / snapshot key / template code on primary panel
- Storage paths in copy surfaces (already policy)

**User:** SEO manager.

**Authority for message bodies:** Client Handoff UX Copy Pack v0.1 (RU).

---

## 6. Screen E — Technical details

**Purpose:** Operator/admin forensics without polluting manager flow.

**Default:** collapsed / separate section.

**Contents:** Snapshot, checksums, render engine/target, source HTML, storage path/disk, MIME, export key, template codes, migration-ish notes.

**User:** Admin / developer; advanced SEO lead only when needed.

---

## 7. Mapping current routes → target screens

| Current route (approx.) | Target screen |
|-------------------------|---------------|
| `/` | A — Главная |
| `/reporting-periods` (+ show) | Entry to B |
| `/monthly-reports/{id}` | B — Отчет за месяц |
| `/report-snapshots/{id}/exports` | C — Файлы отчета |
| `/report-exports/{id}` | C detail / bridge to D |
| `/report-exports/{id}/shares` | D — Отправка клиенту |
| `/health` | Admin Состояние системы |
| `/login` | Вход |

Backend IDs and snapshot steps may remain in URLs; labels must not require managers to say “snapshot”.

---

## 8. Acceptance checklist (future Visual QA)

- [ ] Manager completes flow A→D without English primary chrome  
- [ ] Recommended PDF obvious in ≤2 clicks from report  
- [ ] Share create shows once-URL + three copy actions in Russian  
- [ ] Technical details collapsed by default on export/shares  
- [ ] Footer does not claim «no DB / not synced» when runtime is live  
- [ ] No storage path / checksum in client-facing copy surfaces  
