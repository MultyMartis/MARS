# Website Factory — Blueprint Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/blueprints/`  
**Статус:** обязательный контракт полей для всех canonical Blueprints  
**Связь:** [BLUEPRINT-SYSTEM-v1.md](BLUEPRINT-SYSTEM-v1.md)

**Не является:** JSON Schema, runtime validator, API contract

---

## Назначение

Каждый canonical Blueprint **обязан** содержать перечисленные ниже поля. Отсутствие любого обязательного поля делает Blueprint **неполным** для Factory gate.

Project-specific IA documents **могут** расширять optional-уровень; **не могут** ослаблять `exclusions` без reclassification и HITL.

---

## Обязательные поля

### 1. `site_type`

| Атрибут | Требование |
|---------|------------|
| **Тип** | `site_type_code` из [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| **Core v1** | `LANDING` \| `PROMO` \| `CATALOG` \| `ECOMMERCE` \| `CORPORATE` |
| **Формат** | UPPER_SNAKE_CASE, один код на Blueprint |

---

### 2. `business_goal`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Primary business outcome (1–3 предложения) |
| **Источник** | Registry `Primary goal` + project charter при необходимости |
| **Пример** | «Генерация лидов с одного URL под PPC» |

---

### 3. `page_structure`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Описание IA: single-page vs multi-page, hub-and-spoke, catalog tree, hybrid subtrees |
| **Формат** | Narrative + optional page tree diagram |
| **Обязательно** | Указать typical page count band |

---

### 4. `required_pages`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Список URL/page roles, без которых production **неполон** |
| **Включает** | Legal page slots (L1–L4 URLs) когда применимо по Legal Mapping |
| **Формат** | Таблица: page role · URL pattern · notes |

---

### 5. `required_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Block roles, обязательные для production-quality данного типа |
| **Источник** | [BLUEPRINT-BLOCK-MAPPING-v1.md](../block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md), [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md); role hints: [SITE-TYPE-BLOCK-MAPPING-v1.md](../registry/SITE-TYPE-BLOCK-MAPPING-v1.md) (superseded for `block_id`) |
| **Формат** | Per-page или global stack; указать page scope |

---

### 6. `optional_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Recommended + Optional blocks из Block Mapping |
| **Правило** | Operator выбирает subset; default Blueprint перечисляет **допустимые**, не project-specific picks |

---

### 7. `legal_requirements`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Required legal documents, footer links, consent rule triggers |
| **Источник** | [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md), [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) |
| **FUTURE** | Extension Pack references (ECOMMERCE, CORPORATE) — явно помечать |
| **Запрет** | Не изменять Legal Pack templates |

---

### 8. `seo_requirements`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | SEO priority, indexation policy, IA/SEO implications, schema intent |
| **Источник** | [SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md), [PAGE-SEO-CONTRACT-v1.md](../seo-architecture/PAGE-SEO-CONTRACT-v1.md) |
| **Запрет** | Не генерировать meta content |

---

### 9. `conversion_requirements`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Primary conversion model, CTA hierarchy, form/checkout triggers, traffic alignment |
| **Источник** | Registry + [SITE-TYPE-MATRIX-v1.md](../registry/SITE-TYPE-MATRIX-v1.md) |
| **Обязательно** | Один primary conversion path (или сегментированный для CORPORATE) |

---

### 10. `exclusions`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Features, pages, blocks **явно запрещённые** для типа |
| **Правило** | Reclassification required при нарушении (e.g. cart on CATALOG → ECOMMERCE) |
| **Формат** | Bullet list + consequence note |

---

## Метаданные Blueprint (рекомендуемые)

| Поле | Описание |
|------|----------|
| `blueprint_id` | `{SITE_TYPE}-BLUEPRINT-v1` |
| `version` | `v1` |
| `site_type_group` | `CORE` для Core Types |
| `reference_workspace` | Path если есть golden pattern |
| `typical_traffic_sources` | PPC, organic, direct, etc. |

---

## Минимальный checklist (operator)

Перед freeze Blueprint на проекте:

- [ ] Все 10 обязательных полей заполнены
- [ ] `site_type_code` ∈ closed Core list (или Extended с charter — **no Blueprint in v1**)
- [ ] `exclusions` согласованы с Registry
- [ ] Legal requirements ссылаются на Legal Pack v1 FROZEN
- [ ] Block names согласованы с Block Mapping v1
- [ ] Hybrid subtrees документированы (CORPORATE)

---

## SAFE UNKNOWN

- Formal JSON Schema for Blueprint Contract — **FUTURE**
- Cross-Blueprint inheritance rules (CORPORATE → CATALOG subtree) — **documented per Blueprint**, not in contract machine form

---

*Blueprint Contract version: v1.*
