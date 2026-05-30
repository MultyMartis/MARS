# Triumph Manipulator V6 — Legal Entity Discovery Status v1

**Версия:** v1  
**Дата:** 2026-05-30  
**Проект:** Triumph Manipulator V6  
**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Пилот:** Triumph Legal Entity Discovery Pilot v1  
**Статус:** **BLOCKED** — discovery не может продолжиться без первичных документов

**Канонические контракты (reference):**

| Контракт | Расположение |
|----------|--------------|
| LEGAL-ENTITY-DISCOVERY-v1 | `workspaces/website-factory-reference-v1/legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md` |
| LEGAL-ENTITY-CARD-v1 | `workspaces/website-factory-reference-v1/legal-entity/LEGAL-ENTITY-CARD-v1.md` |
| LEGAL-INPUT-SHEET-v1 | `workspaces/website-factory-reference-v1/legal/LEGAL-INPUT-SHEET-v1.md` |

**Запреты пилота (соблюдены):** legal pages, footer code, Legal Generation — **не выполнялись**.

---

## Current state

| Item | Status |
|------|--------|
| `project-input/legal-entity/` | **Создан** (2026-05-30) |
| Файлы в inbox | **0** — каталог пуст |
| `legal-entity/LEGAL-ENTITY-CARD-DRAFT-v1.md` | **Создан** — частичное заполнение, `NOT_READY` |
| Discovery phase | **BLOCKED** на Step 2 (P1 отсутствует) |
| Legal Entity Card completion | **BLOCKED** |
| Legal Input Sheet | **Не создан** — upstream card не READY |
| Legal Generation | **Не запускалась** |

---

## Required files (operator / client)

Минимальный рекомендуемый набор для разблокировки discovery (P1):

| # | Документ | Формат | Назначение |
|---|----------|--------|------------|
| 1 | ЕГРЮЛ / выписка | PDF | `legal_name`, `inn`, `ogrn`, `address`, `entity_type` |
| 2 | Карточка реквизитов / письмо с реквизитами | PDF, DOCX | Banking block, контакты, подтверждение наименования |
| 3 | Банковские реквизиты (при необходимости для charter) | PDF, DOCX, XLSX, JPG, PNG | Banking block |

**Канонический inbox:**

```text
workspaces/triumph-manipulator-landing-v6/project-input/legal-entity/
```

---

## Missing files

| Expected file (examples) | Status | Priority |
|--------------------------|--------|----------|
| `egrul.pdf` / `egrul-YYYY-MM-DD.pdf` | **Missing** | P1 |
| `requisites.docx` / `company-details.pdf` | **Missing** | P1 |
| `company-card.pdf` | **Missing** | P1 |
| `bank-details.pdf` / `bank-details.jpg` | **Missing** | P1 (optional for Core L1–L4, recommended) |
| `company-details.png` (scan визитки) | **Missing** | P1 |

**Примечание:** файлы из `incoming/website-factory-legal-cleanup/` — шаблоны legal pages (L1–L4), **не** источники данных о юрлице. **Не** класть их в `project-input/legal-entity/` как замену ЕГРЮЛ/реквизитов.

---

## Expected document types (operator guide)

Оператор размещает в `project-input/legal-entity/` **только** первичные документы о юридическом лице:

| Категория | Примеры имён | Форматы |
|-----------|--------------|---------|
| Учредительные / реквизиты | `requisites.docx`, `company-details.pdf` | PDF, DOCX |
| ЕГРЮЛ / выписка | `egrul.pdf`, `egrul-2026-05-30.pdf` | PDF |
| Банковские реквизиты | `bank-details.pdf`, `payment-details.xlsx` | PDF, DOCX, XLSX, JPG, PNG |
| Визитка / scan | `company-card.pdf`, `company-details.png` | PDF, JPG, PNG, WEBP |
| Договор / оферта (копия) | `public-offer-draft.pdf` | PDF, DOCX — secondary, не замена ЕГРЮЛ |

**Правила именования:** без пробелов в имени; дата в имени выписки ЕГРЮЛ; при обновлении — новый файл или суффикс `-v2`.

**Reference:** [LEGAL-ENTITY-INPUT-STANDARD-v1.md](../../website-factory-reference-v1/legal-entity/LEGAL-ENTITY-INPUT-STANDARD-v1.md)

---

## Readiness status

| Gate | Verdict | Reason |
|------|---------|--------|
| Discovery (P1 inbox) | **BLOCKED** | `project-input/legal-entity/` пуст — нет legal source documents |
| Legal Entity Card | **BLOCKED** | `company_name`, `legal_name` = UNKNOWN; `operator_verified = false`; нет P1 extraction |
| Legal Input Sheet | **BLOCKED** | Upstream card не READY |
| Legal Generation | **OUT OF SCOPE** | Пилот завершается на card gate |

**Следующий шаг оператора:** разместить P1-документы → повторный extraction → operator verify (P6) → `card_status = READY`.

---

## Related artifacts

| Artifact | Path |
|----------|------|
| Draft Legal Entity Card | [LEGAL-ENTITY-CARD-DRAFT-v1.md](LEGAL-ENTITY-CARD-DRAFT-v1.md) |
| Triumph gap report (prep) | `workspaces/website-factory-reference-v1/legal/pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md` |
| Triumph lesson | `workspaces/website-factory-reference-v1/legal-entity/TRIUMPH-LEGAL-ENTITY-LESSON-v1.md` |

---

## SAFE UNKNOWN

- Будет ли оператор предоставлять ЕГРЮЛ в inbox — **pending human action**.
- Точная каноническая строка `company_name` — **требует P1 + P6**; footer-сигналы не используются как production values в card.
- Git LFS для крупных PDF в Triumph workspace — **не определено**.

---

*Status version: v1. Pilot: Triumph Legal Entity Discovery Pilot v1.*
