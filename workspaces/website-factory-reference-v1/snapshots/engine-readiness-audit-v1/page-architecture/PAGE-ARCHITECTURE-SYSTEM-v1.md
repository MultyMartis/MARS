# Website Factory — Page Architecture System v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** канонический слой сборки страниц — **documentation only**  
**Дата:** 2026-05-31  
**Не является:** runtime, page generator, CMS schema, design tool, SEO/content generator, автоматическая валидация

---

## Назначение

Page Architecture System v1 — **пропущенный слой** между Blueprint (IA сайта) и Block Registry (секции на странице).

До v1 Website Factory формально знала:

| Слой | Что определено |
|------|----------------|
| Site Type | Класс сайта (`LANDING`, `PROMO`, …) |
| Blueprint | IA, `required_pages`, block stacks на уровне типа |
| Block Registry | `block_id`, матрица REQUIRED/OPTIONAL/FORBIDDEN |

**Не было формально:** как **конкретная страница** собирается — цель, роль, обязательные/запрещённые блоки, legal/SEO/conversion на уровне **page contract**.

Page Architecture Contracts v1 закрывают этот разрыв.

---

## Что такое Page Architecture Contract

**Page Architecture Contract** — документированный контракт **одного page_type** (или экземпляра страницы проекта), описывающий:

- зачем страница существует (`page_goal`, `page_role`);
- какие блоки **обязаны**, **могут** и **запрещены** на этой странице;
- legal, SEO и conversion требования **на уровне страницы**;
- зависимости от других страниц, Legal Pack, Blueprint.

Контракт **не** генерирует HTML, дизайн или контент. Он задаёт **архитектурные ограничения** до Design и Frontend.

**Канонические артефакты v1:**

| Файл | Роль |
|------|------|
| [PAGE-CONTRACT-v1.md](PAGE-CONTRACT-v1.md) | Обязательные поля контракта |
| [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) | Канонические `page_type` |
| [CORE-PAGE-ARCHITECTURES-v1.md](CORE-PAGE-ARCHITECTURES-v1.md) | Состав страниц (block stacks) |
| [SITE-TYPE-PAGE-MATRIX-v1.md](SITE-TYPE-PAGE-MATRIX-v1.md) | Site Type × Page Type |
| [PAGE-DEPENDENCY-RULES-v1.md](PAGE-DEPENDENCY-RULES-v1.md) | Межстраничные и legal deps |
| [LEGAL-PAGE-CONTRACT-v1.md](LEGAL-PAGE-CONTRACT-v1.md) | Специализация `LEGAL_PAGE` |
| [PAGE-IMPLEMENTATION-RULES-v1.md](PAGE-IMPLEMENTATION-RULES-v1.md) | Обязательный production flow |
| [PAGE-GAPS-v1.md](PAGE-GAPS-v1.md) | Оставшиеся пробелы |

---

## Production chain (полная цепочка)

```
Site Type          ← SITE-TYPE-REGISTRY-v1
        ↓
Blueprint          ← blueprints/{TYPE}-BLUEPRINT-v1
        ↓
Page Architecture  ← page-architecture/ (этот слой)
        ↓
Blocks             ← block-registry/ (block_id per page)
        ↓
Design             ← FUTURE: design system mapping
        ↓
Frontend           ← project build / reference partials
```

**Правило v1:** ни один блок **не выбирается** без зафиксированного page architecture для целевой страницы. Blueprint задаёт **какие page roles существуют**; Page Architecture задаёт **как каждая страница собирается из блоков**.

---

## Lifecycle

| Фаза | Действие | Gate |
|------|----------|------|
| **1. Classify** | `site_type_code` из Registry | Core Types для default production |
| **2. Blueprint** | Загрузить canonical Blueprint | `required_pages` известны |
| **3. Page matrix** | [SITE-TYPE-PAGE-MATRIX-v1.md](SITE-TYPE-PAGE-MATRIX-v1.md) — REQUIRED/OPTIONAL/FORBIDDEN page types | Нет FORBIDDEN page types в IA |
| **4. Page contracts** | Для каждой production-страницы — `page_type` + поля [PAGE-CONTRACT-v1.md](PAGE-CONTRACT-v1.md) | CORE-PAGE-ARCHITECTURES + project URL |
| **5. Block freeze** | `required_blocks` / `forbidden_blocks` per page | MATRIX v2 + PAGE-DEPENDENCY-RULES |
| **6. Legal gate** | `LEGAL_PAGE` → Legal Pack; forms → Consent Rule | Legal Pack v1 FROZEN |
| **7. Design** | Map blocks → visual components | **FUTURE** — не в scope v1 |
| **8. Frontend** | Partials / sections assembly | После block list frozen |

**Halt:** Design или Frontend **без** page architecture для каждой money/legal route = **drift risk** (см. mars-survivability operational patterns).

---

## Связи с upstream / downstream

### Site Type

- Определяет **допустимую вселенную** page types и блоков.
- Источник: [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md).
- Page Architecture **не** меняет `site_type_code`; при несовместимости page set → reclassification + HITL.

### Blueprint

- Задаёт `page_structure`, `required_pages`, exclusions на уровне сайта.
- Источник: [BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md), Core Blueprints v1.
- Page Architecture **детализирует** Blueprint `required_pages` в контракты `page_type` + block stacks.
- Blueprint **без** Page Architecture = неполный gate для block selection (см. [BLOCK-IMPLEMENTATION-RULES-v1.md](../block-registry/BLOCK-IMPLEMENTATION-RULES-v1.md) — обновлено flow в [PAGE-IMPLEMENTATION-RULES-v1.md](PAGE-IMPLEMENTATION-RULES-v1.md)).

### Block Registry

- `block_id` привязывается к **конкретной странице** через `required_blocks` / `optional_blocks` / `forbidden_blocks` в page contract.
- Матрица совместимости блоков: [SITE-TYPE-BLOCK-MATRIX-v2.md](../block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md).
- Page-level FORBIDDEN **сужает** допустимый subset matrix для данной страницы.

### Legal Pack

- `LEGAL_PAGE` требует Legal Pack v1 (FROZEN) и [LEGAL-PAGE-CONTRACT-v1.md](LEGAL-PAGE-CONTRACT-v1.md).
- Формы на money pages → Consent Rule, Footer Rule — [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md).
- Page Architecture **не** изменяет шаблоны Legal Pack.

### Design System

- **FUTURE** (Priority 5 в roadmap). Page Architecture передаёт **список блоков per page**; design mapping ещё не канонизирован.
- Legal pages: наследуют project design — см. LEGAL-PAGE-CONTRACT.

### Frontend

- Сборка секций/partials **после** frozen page contracts + block lists.
- Reference: `workspaces/website-factory-reference-v1/src/partials/sections/`.
- Page Architecture **не** генерирует код.

---

## Scope v1

| В scope | Вне scope |
|---------|-----------|
| Core site types: `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` | `SAAS`, `WEB_APPLICATION`, `MARKETPLACE` page architectures |
| 10 canonical page types + ECOMMERCE utility pages в dependency rules | Runtime page generator |
| Documentation contracts | Design / SEO / content generation |

---

## SAFE UNKNOWN

- Machine-readable JSON Schema для page contracts — **FUTURE**
- Автоматическая cross-check Blueprint `required_pages` ↔ page contracts — **FUTURE** (human-operated v1)
- Extended Types page architectures — **требуют charter**; не authored в v1

---

*Page Architecture System version: v1. Operator-approved 2026-05-31.*
