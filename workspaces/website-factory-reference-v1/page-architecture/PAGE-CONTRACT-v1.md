# Website Factory — Page Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** обязательный контракт полей для каждой production-страницы  
**Связь:** [PAGE-ARCHITECTURE-SYSTEM-v1.md](PAGE-ARCHITECTURE-SYSTEM-v1.md), [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md)

**Не является:** JSON Schema, runtime validator, URL router, content template

---

## Назначение

Каждая production-страница Website Factory **обязана** иметь зафиксированный Page Contract (в project IA doc или эквиваленте), соответствующий полям ниже.

Отсутствие обязательного поля = **неполный** page gate → halt до Design/Frontend.

Project-specific IA **может** расширять `optional_blocks`; **не может** ослаблять `forbidden_blocks` или site-type FORBIDDEN page types без reclassification и HITL.

---

## Обязательные поля

### 1. `page_type`

| Атрибут | Требование |
|---------|------------|
| **Тип** | `page_type` из [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md) |
| **Формат** | UPPER_SNAKE_CASE |
| **Пример** | `SERVICE_PAGE`, `PRODUCT_PAGE`, `LEGAL_PAGE` |

---

### 2. `page_goal`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Primary outcome этой страницы (1–3 предложения) |
| **Источник** | Blueprint `business_goal` + page role в IA |
| **Пример** | «Конвертировать посетителя услуги в заявку» |

---

### 3. `page_role`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Роль в IA: hub, money, utility, legal, catalog, transaction |
| **Формат** | Один primary role + optional secondary tags |
| **Допустимые роли** | `CONVERSION` · `MONEY` · `HUB` · `NAVIGATION` · `CATALOG` · `TRANSACTION` · `LEGAL` · `UTILITY` · `TRUST` |

---

### 4. `required_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Ordered list `block_id` из [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) |
| **Источник** | [CORE-PAGE-ARCHITECTURES-v1.md](CORE-PAGE-ARCHITECTURES-v1.md) + Blueprint block stack |
| **Правило** | Каждый `block_id` должен быть REQUIRED или OPTIONAL в [SITE-TYPE-BLOCK-MATRIX-v2.md](../block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md) для данного `site_type_code` |

---

### 5. `optional_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Допустимые `block_id`, не обязательные для v1 classification |
| **Правило** | Только из OPTIONAL/Recommended cells matrix + CORE-PAGE-ARCHITECTURES allow-list |
| **Выбор** | Operator / project IA — subset документируется явно |

---

### 6. `forbidden_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | `block_id`, **запрещённые** на этой странице даже если matrix допускает на других страницах |
| **Источник** | Blueprint `exclusions` + page-type defaults (e.g. `CART` on `SERVICE_PAGE`) |
| **Пример** | `CHECKOUT` forbidden on `LANDING_PAGE` |

---

### 7. `legal_requirements`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Legal Pack slots, Footer Rule, Consent Rule, extension refs |
| **Источник** | [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md), [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) |
| **`LEGAL_PAGE`** | См. [LEGAL-PAGE-CONTRACT-v1.md](LEGAL-PAGE-CONTRACT-v1.md) |
| **Запрет** | Не изменять Legal Pack templates |

---

### 8. `seo_requirements`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Indexation intent, URL role, schema **intent** (не meta text) |
| **Источник** | [SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md), [PAGE-SEO-CONTRACT-v1.md](../seo-architecture/PAGE-SEO-CONTRACT-v1.md) + Blueprint `seo_requirements` (v1 hints: [SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — superseded) |
| **Запрет** | Не генерировать title/description/copy |

---

### 9. `conversion_requirements`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Primary CTA, form/checkout triggers, traffic alignment для страницы |
| **Источник** | Blueprint `conversion_requirements` + [BLOCK-CONVERSION-ROLES-v1.md](../block-registry/BLOCK-CONVERSION-ROLES-v1.md) |
| **Обязательно** | Один primary conversion path per money/conversion page |

---

### 10. `dependencies`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Required sibling pages, Legal Pack, blocks, external gates |
| **Источник** | [PAGE-DEPENDENCY-RULES-v1.md](PAGE-DEPENDENCY-RULES-v1.md) |
| **Формат** | List: dependency type · target · halt rule |

---

## Рекомендуемые метаданные (project IA)

| Поле | Описание |
|------|----------|
| `page_contract_id` | `{PROJECT}-{page_type}-{slug}-v1` |
| `canonical_url` | Production URL (trailing slash policy per project) |
| `site_type_code` | Parent site classification |
| `blueprint_id` | e.g. `PROMO-BLUEPRINT-v1` |
| `blueprint_page_ref` | Row in Blueprint `required_pages` |

---

## Минимальный checklist (operator)

Перед freeze page contract на проекте:

- [ ] Все 10 обязательных полей заполнены
- [ ] `page_type` ∈ Registry и разрешён [SITE-TYPE-PAGE-MATRIX-v1.md](SITE-TYPE-PAGE-MATRIX-v1.md)
- [ ] `required_blocks` ⊆ matrix (не FORBIDDEN)
- [ ] `forbidden_blocks` согласованы с Blueprint exclusions
- [ ] `dependencies` проверены по PAGE-DEPENDENCY-RULES
- [ ] `LEGAL_PAGE` → LEGAL-PAGE-CONTRACT + Legal Pack gate
- [ ] Forms → Consent Rule documented

---

## SAFE UNKNOWN

- Formal JSON Schema for Page Contract — **FUTURE**
- Per-locale page contract variants — **not in v1**

---

*Page Contract version: v1.*
