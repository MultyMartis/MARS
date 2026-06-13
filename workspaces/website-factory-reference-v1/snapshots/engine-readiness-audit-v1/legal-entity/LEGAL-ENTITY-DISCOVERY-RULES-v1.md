# Website Factory — Legal Entity Discovery Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/legal-entity/`  
**Статус:** канонические правила discovery — **documentation only**  
**Не является:** runtime, OCR-сервисом, автоматическим scraper, юридической экспертизой

---

## Назначение

Legal Entity Discovery System v1 — **первичный слой** получения данных о клиентском юридическом лице для Website Factory.

Система заменяет ad-hoc практики:

| Запрещённый источник (как primary) | Почему |
|-----------------------------------|--------|
| Текст footer без operator verify | Drift, маркетинговые варианты, неполнота |
| Случайный контент страниц | Не юридический источник |
| Ручной поиск по workspace без структуры | Невоспроизводимый audit trail |
| Разрозненные project notes | Конфликты, отсутствие приоритетов |

**Единый output discovery:** [LEGAL-ENTITY-CARD-v1.md](LEGAL-ENTITY-CARD-v1.md) — **не** Legal Templates, **не** Footer, **не** Legal Input Sheet напрямую.

**Связанные документы:**

| Документ | Роль |
|----------|------|
| [LEGAL-ENTITY-WORKFLOW-v1.md](LEGAL-ENTITY-WORKFLOW-v1.md) | Human-operated workflow |
| [LEGAL-ENTITY-INPUT-STANDARD-v1.md](LEGAL-ENTITY-INPUT-STANDARD-v1.md) | `project-input/legal-entity/` |
| [LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md](LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md) | Извлечение из документов |
| [LEGAL-ENTITY-VALIDATION-RULES-v1.md](LEGAL-ENTITY-VALIDATION-RULES-v1.md) | Валидация и конфликты |
| [../legal/LEGAL-INPUT-SHEET-v1.md](../legal/LEGAL-INPUT-SHEET-v1.md) | Потребитель card после sign-off |
| [../legal/LEGAL-PACK-ARCHITECTURE-v1.md](../legal/LEGAL-PACK-ARCHITECTURE-v1.md) | Legal stack architecture |

**Out of scope:** Mobile App Factory (FUTURE separate factory); новые site types; новые factories; автоматическая генерация legal HTML.

---

## Каноническая структура проекта (Task 1)

Каждый **client production workspace** Website Factory **должен** резервировать путь:

```text
<project-workspace>/
└── project-input/
    └── legal-entity/
        ├── company-card.pdf          # пример
        ├── requisites.docx
        ├── egrul.pdf
        ├── bank-details.jpg
        └── README-operator-notes.md  # optional — не заменяет card
```

### Допустимые типы файлов в `project-input/legal-entity/`

| Категория | Форматы |
|-----------|---------|
| Документы | PDF, DOCX, XLSX |
| Изображения | JPG, PNG, WEBP |
| Сканы | PDF, JPG, PNG (отсканированные реквизиты) |
| Карточки | Визитки, company cards (image/PDF) |
| Реквизиты | DOCX, PDF, XLSX |
| ЕГРЮЛ / выписки | PDF |
| Банковские реквизиты | PDF, DOCX, image |

**Правила размещения:**

1. Один каталог — **единая точка входа** для оператора и агента.
2. Имена файлов — **описательные** (`egrul-2026-05.pdf`, не `scan3.jpg` без контекста).
3. Исходники **не удаляются** после extraction — остаются audit trail.
4. Каталог **не** подменяет Legal Entity Card: card — производный артефакт с metadata.
5. Card и Input Sheet хранятся **вне** canonical templates (`legal/` в reference workspace).

**Reference workspace:** `workspaces/website-factory-reference-v1/` описывает систему; **per-project** каталог создаётся в client workspace при charter.

---

## Приоритеты discovery (Task 2)

Канонический порядок источников (от высшего к низшему):

| Priority | Источник | Код | Описание |
|:--------:|----------|-----|----------|
| **1** | `project-input/legal-entity/` | `P1_PROJECT_INPUT` | Структурированные документы оператора |
| **2** | Явно переданные legal documents | `P2_EXPLICIT_DOCS` | Документы вне каталога, но явно помеченные оператором как legal source |
| **3** | Существующая project documentation | `P3_PROJECT_DOCS` | Charter, intake, signed contracts в repo |
| **4** | Website footer | `P4_FOOTER` | Только как сигнал — **не** auto-truth |
| **5** | Website content | `P5_SITE_CONTENT` | Страницы, partials, marketing copy |
| **6** | Ручное подтверждение оператора | `P6_OPERATOR_CONFIRM` | HITL sign-off, переписывает неопределённость, **не** нижние приоритеты без явного charter |

### Инвариант: no downgrade overwrite

```text
Если поле X заполнено из Priority N,
значение из Priority M (где M > N) НЕ МОЖЕТ перезаписать X
без operator_verified = true и записи в metadata/conflict report.
```

| Ситуация | Поведение |
|----------|-----------|
| P1 даёт `inn`, P4 даёт другой `inn` | Сохранить P1; зафиксировать конфликт в conflict report |
| Только P4/P5 доступны | Поле → extracted с `confidence_level` ≤ medium; **не** production-ready без P6 |
| P6 подтверждает значение, противоречащее P1 | **STOP** — требуется разрешение: обновить P1 source или отклонить P6 с обоснованием |

**Запрещено:** автоматическое слияние конфликтующих значений; «угадывание» при расхождении `company_name` / `legal_name`.

---

## Границы системы

| В scope | Out of scope |
|---------|--------------|
| Discovery, extraction rules, card schema, validation | Генерация L1–L4 HTML |
| Интеграция с Legal Input Sheet (consume) | Прямая запись в Legal Templates |
| Conflict reporting semantics | Новые site types / factories |
| Triumph lesson (отдельный doc) | Изменения Triumph workspace |

---

## Поток данных (summary)

```text
Sources (P1–P6)
        ↓
  Extraction (human/agent per guide)
        ↓
  LEGAL-ENTITY-CARD-v1
        ↓
  Validation + operator_verified
        ↓
  Legal Input Sheet (identity/entity blocks)
        ↓
  Legal Generation (L1–L4)
```

Подробно: [LEGAL-ENTITY-WORKFLOW-v1.md](LEGAL-ENTITY-WORKFLOW-v1.md).

---

## SAFE UNKNOWN

- Автоматический watcher на `project-input/legal-entity/` — **не реализован**.
- Единый machine-readable card format (JSON) — **FUTURE**; v1 canon = Markdown template.
- Международные юрлица (non-RU INN/OGRN) — **не стандартизированы** exhaustively в v1.

---

*Rules version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal-entity/`.*
