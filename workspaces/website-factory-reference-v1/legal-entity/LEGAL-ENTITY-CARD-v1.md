# Website Factory — Legal Entity Card v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/legal-entity/`  
**Статус:** каноническая schema card — **documentation only**  
**Не является:** Legal Input Sheet, legal template, footer partial

---

## Назначение

**Legal Entity Card v1** — единый структурированный артефакт после discovery/extraction. Primary source of truth для:

- Legal Pages (через Input Sheet)
- Footer Data
- Contact Pages
- Company Information Blocks
- Contracts / Offers (FUTURE Extension Packs)
- Ecommerce / SaaS / Marketplace Extensions (entity block only)

**Правило:** Card создаётся **до** Legal Input Sheet. Input Sheet **потребляет** card, не выполняет discovery напрямую.

**Шаблон заполнения:** [LEGAL-ENTITY-CARD-TEMPLATE-v1.md](LEGAL-ENTITY-CARD-TEMPLATE-v1.md)

---

## Идентификатор card

| Поле | Тип | Обязательность | Описание |
|------|-----|:--------------:|----------|
| `card_id` | string | Required | Уникальный ID, напр. `triumph-manipulator-legal-entity-2026-05` |
| `project_name` | string | Required | Рабочее имя проекта |
| `workspace_path` | string | Recommended | Путь к client workspace |
| `created_at` | date | Required | Дата создания card |
| `updated_at` | date | Recommended | Последнее обновление |

---

## Identity block

| Поле | Тип | Обязательность | Maps to Input Sheet | Описание |
|------|-----|:--------------:|---------------------|----------|
| `company_name` | string | **Required** | `company_name` | Строка для подстановки в шаблоны (Оператор / Администрация) |
| `legal_name` | string | **Required** | `legal_name` | Полное наименование по учредительным документам / ЕГРЮЛ |
| `entity_type` | enum | Required | `entity_type` | `LEGAL_ENTITY` \| `INDIVIDUAL_ENTREPRENEUR` \| `SELF_EMPLOYED` \| `UNKNOWN` |
| `inn` | string | Conditional | `inn` | ИНН — required для юрлица/ИП |
| `ogrn` | string | Conditional | `ogrn` | ОГРН / ОГРНИП |
| `kpp` | string | Optional | — | КПП (только юрлицо) |
| `address` | string | Optional | `address` | Юридический / почтовый адрес |
| `email` | string | Recommended | `email` | Контактный email |
| `phone` | string | Recommended | `phone` | Контактный телефон |
| `website` | string | Optional | — | Сайт компании (если отличен от production domain) |

### `company_name` vs `legal_name`

| Правило | Действие |
|---------|----------|
| Совпадают | Оба поля = одна подтверждённая строка |
| Различаются (бренд vs ЕГРЮЛ) | Оба заполнены явно; `company_name` — для шаблонов после operator verify |
| Любое = пустое / не подтверждено | Card status = **NOT READY** для Input Sheet generation |

---

## Banking block

| Поле | Тип | Обязательность | Описание |
|------|-----|:--------------:|----------|
| `bank_name` | string | Optional | Наименование банка |
| `bik` | string | Optional | БИК |
| `checking_account` | string | Optional | Расчётный счёт |
| `correspondent_account` | string | Optional | Корреспондентский счёт |

**Примечание:** Banking block **не блокирует** Core Legal Pack L1–L4 v1, если пуст — но обязателен для счетов/оферт по project charter.

---

## Metadata block

| Поле | Тип | Обязательность | Описание |
|------|-----|:--------------:|----------|
| `source_document` | string | Required per filled field group | Файл или источник, напр. `project-input/legal-entity/egrul.pdf` |
| `source_priority` | enum | Required | `P1_PROJECT_INPUT` … `P6_OPERATOR_CONFIRM` — см. [LEGAL-ENTITY-DISCOVERY-RULES-v1.md](LEGAL-ENTITY-DISCOVERY-RULES-v1.md) |
| `confidence_level` | enum | Required | `high` \| `medium` \| `low` \| `unknown` |
| `operator_verified` | boolean | **Required before Input Sheet sign-off** | `true` только после HITL подтверждения полей card |

### Дополнительные metadata (recommended)

| Поле | Тип | Описание |
|------|-----|----------|
| `extraction_notes` | text | Как извлечено, ограничения OCR |
| `conflict_report_ref` | string | Ссылка на conflict report при расхождениях |
| `fields_unknown` | string[] | Список полей, оставшихся UNKNOWN |

---

## Card status

| Status | Условие | Следующий шаг |
|--------|---------|---------------|
| `DRAFT` | Extraction выполнен, не все поля verified | Validation + operator review |
| `CONFLICT` | Есть неразрешённые конфликты | Conflict report + HITL |
| `READY` | Required identity fields заполнены, `operator_verified = true` | Создать/обновить Legal Input Sheet |
| `NOT_READY` | `company_name` или `legal_name` не подтверждены | **STOP** — нельзя передавать в generation |

---

## Запреты (hard rules)

| # | Запрет |
|---|--------|
| 1 | Запись card-полей **напрямую** в `legal/*-template.md` |
| 2 | Запись card-полей **напрямую** в footer partials без Input Sheet + generation contract |
| 3 | Заполнение Legal Input Sheet из footer (P4) **без** card и operator verify |
| 4 | Auto-merge конфликтующих значений |
| 5 | Invented / guessed `company_name` или `legal_name` |

---

## Связь с Legal Input Sheet

| Card field | Input Sheet field |
|------------|-------------------|
| `company_name` | `company_name` |
| `legal_name` | `legal_name` |
| `entity_type` | `entity_type` |
| `inn` | `inn` |
| `ogrn` | `ogrn` |
| `address` | `address` (при `address_status = PROVIDED`) |
| `email` | `email` |
| `phone` | `phone` |

`domain` и derived URLs — **не** в card; задаются в Input Sheet Meta / Identity workflow.

---

## SAFE UNKNOWN

- JSON Schema export card — **не определён** v1.
- Хранение card в git vs operator channel — **per project charter**; рекомендуется path в workspace `legal/` или `project-input/`.

---

*Schema version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal-entity/`.*
