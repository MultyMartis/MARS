# Website Factory — Legal Entity Extraction Guide v1

**Версия:** v1  
**Статус:** human/agent extraction semantics — **documentation only**  
**Не является:** OCR engine, автоматическим pipeline

---

## Назначение

Описывает **как** извлекать поля юрлица из источников в **Legal Entity Card v1**. Output **всегда** — card; **никогда** — прямая запись в Legal Templates, Footer, Legal Input Sheet.

**Output schema:** [LEGAL-ENTITY-CARD-v1.md](LEGAL-ENTITY-CARD-v1.md)  
**Priorities:** [LEGAL-ENTITY-DISCOVERY-RULES-v1.md](LEGAL-ENTITY-DISCOVERY-RULES-v1.md)

---

## Поддерживаемые типы источников

| Source type | Форматы | Типичные поля |
|-------------|---------|---------------|
| PDF | `.pdf` | `legal_name`, `inn`, `ogrn`, `kpp`, `address` |
| DOCX | `.docx` | Полный блок реквизитов, banking |
| XLSX | `.xlsx` | Табличные реквизиты |
| Images | JPG, PNG, WEBP | Визитки, сканы |
| Scans | PDF/JPG/PNG | То же, lower OCR confidence |
| Tables | XLSX, DOCX tables | Banking, ИНН/ОГРН |
| Bank cards (image) | JPG, PNG | `bank_name`, `bik`, accounts — **redact** card PAN |
| Company cards | image/PDF | `company_name`, `phone`, `email`, `website` |
| EGRUL extracts | PDF | `legal_name`, `inn`, `ogrn`, `kpp`, `address` |

---

## Процесс extraction (per field)

```text
1. Identify highest-priority source containing field
2. Extract literal value (no normalization beyond trim)
3. Record source_document path
4. Record source_priority code (P1–P6)
5. Assign confidence_level
6. If lower priority disagrees → conflict report, do NOT overwrite
```

---

## Field extraction hints (RU)

| Field | Где искать | Notes |
|-------|------------|-------|
| `legal_name` | ЕГРЮЛ, устав, реквизиты | Полная строка с ОПФ |
| `company_name` | Operator + marketing docs; **не** угадывать из footer | Часто требует P6 |
| `inn` | ЕГРЮЛ, реквизиты | 10 или 12 цифр |
| `ogrn` | ЕГРЮЛ | 13 цифр (юрлицо) |
| `kpp` | ЕГРЮЛ, реквизиты | 9 цифр |
| `address` | ЕГРЮЛ | Юридический адрес |
| `bank_name`, `bik`, accounts | Банковские реквизиты | Отдельный документ |

---

## Confidence levels

| Level | Когда |
|-------|-------|
| `high` | P1/P2 machine-readable doc or operator-verified copy |
| `medium` | P3 project doc or clean scan |
| `low` | P4 footer, P5 page content |
| `unknown` | Не извлечено — поле пустое или явный UNKNOWN |

**Правило:** `company_name` / `legal_name` из P4/P5 **не могут** быть `high` без P6.

---

## Запрещённые действия

| # | Запрет |
|---|--------|
| 1 | Писать extracted values в `legal/*-template.md` |
| 2 | Патчить footer partials напрямую |
| 3 | Заполнять Legal Input Sheet в том же шаге, что extraction |
| 4 | Нормализовать «Триумф» → «ООО «ТРИУМФ»» без operator |
| 5 | Merge conflicting INN/OGRN |

---

## Agent-assisted extraction (Cursor)

| Allowed | Forbidden |
|---------|-----------|
| Read files in `project-input/legal-entity/` | Commit guessed legal names |
| Draft card from template | Modify client HTML for «discovery» |
| Draft conflict report | Auto-approve `operator_verified` |

Оператор **обязан** выставить `operator_verified = true` перед Input Sheet.

---

## Пример output (fragment)

```markdown
| **legal_name** | ООО «ТРИУМФ» | project-input/legal-entity/egrul.pdf | P1_PROJECT_INPUT | high |
| **company_name** | UNKNOWN | — | — | unknown |
```

→ `card_status = NOT_READY` до P6.

---

## SAFE UNKNOWN

- Recommended OCR tools — **not specified**; human transcription acceptable.
- Non-RU entities — extraction hints **incomplete** v1.

---

*Guide version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal-entity/`.*
