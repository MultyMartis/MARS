# Website Factory — Block Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** обязательный контракт полей для каждого canonical `block_id`  
**Связь:** [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [BLOCK-CATEGORY-SYSTEM-v1.md](BLOCK-CATEGORY-SYSTEM-v1.md), [BLOCK-CONVERSION-ROLES-v1.md](BLOCK-CONVERSION-ROLES-v1.md)

**Не является:** JSON Schema, runtime validator, CMS block schema, design spec, frontend component contract

---

## Назначение

Каждый блок Website Factory Block Registry **обязан** иметь запись, соответствующую полям ниже. Отсутствие обязательного поля = **неполный** block gate → halt до Page Architecture / Design.

Project IA **может** расширять optional placement; **не может** ослаблять FORBIDDEN stances из [PAGE-BLOCK-MAPPING-v1.md](PAGE-BLOCK-MAPPING-v1.md) или [BLUEPRINT-BLOCK-MAPPING-v1.md](BLUEPRINT-BLOCK-MAPPING-v1.md) без reclassification и HITL.

**Production bridge:**

```
Site Type → Blueprint → Page Architecture → Blocks → Design → Frontend
```

---

## Обязательные поля

### 1. `block_id`

| Атрибут | Требование |
|---------|------------|
| **Тип** | Stable canonical key |
| **Формат** | UPPER_SNAKE_CASE |
| **Пример** | `LEAD_FORM`, `PRODUCT_GRID` |
| **Правило** | Immutable после v1 freeze; variants — project notes, not new id без charter |

---

### 2. `block_name`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Human-readable label for operators and IA docs |
| **Пример** | Lead / RFQ form |

---

### 3. `block_category`

| Атрибут | Требование |
|---------|------------|
| **Тип** | `category_id` из [BLOCK-CATEGORY-SYSTEM-v1.md](BLOCK-CATEGORY-SYSTEM-v1.md) |
| **Формат** | UPPER_SNAKE_CASE |
| **Правило** | **One primary category** per `block_id`; secondary tags forbidden in v1 |

**Alias:** legacy field name `primary_category` in BLOCK-REGISTRY-v1 = `block_category`.

---

### 4. `purpose`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | 1–3 предложения — зачем блок существует в conversion / IA stack |
| **Источник** | Blueprint business goal + page role |

---

### 5. `conversion_role`

| Атрибут | Требование |
|---------|------------|
| **Тип** | Один primary role из [BLOCK-CONVERSION-ROLES-v1.md](BLOCK-CONVERSION-ROLES-v1.md) |
| **Допустимые значения** | `PRIMARY_CONVERSION` · `SECONDARY_CONVERSION` · `TRUST_SUPPORT` · `INFORMATIONAL` · `LEGAL` · `SYSTEM` |

---

### 6. `allowed_site_types`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Subset of Core site types where block **may** appear |
| **Core codes** | `LANDING` · `PROMO` · `CATALOG` · `ECOMMERCE` · `CORPORATE` |
| **Источник** | [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| **Правило** | Absence from list = implicit FORBIDDEN unless matrix override documented |

Per-site-type REQUIRED / OPTIONAL / FORBIDDEN — **authoritative** in [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md) and [BLUEPRINT-BLOCK-MAPPING-v1.md](BLUEPRINT-BLOCK-MAPPING-v1.md).

---

### 7. `allowed_page_types`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Subset of [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) codes |
| **Минимальный набор v1** | `HOME_PAGE` · `LANDING_PAGE` · `SERVICE_PAGE` · `CATEGORY_PAGE` · `PRODUCT_PAGE` · `ABOUT_PAGE` · `CONTACT_PAGE` · `FAQ_PAGE` · `REVIEWS_PAGE` · `LEGAL_PAGE` |
| **Правило** | Block may appear only on listed page types (plus utility routes documented in Blueprint) |

Per-page-type REQUIRED / OPTIONAL / FORBIDDEN — **authoritative** in [PAGE-BLOCK-MAPPING-v1.md](PAGE-BLOCK-MAPPING-v1.md).

---

### 8. `required_or_optional`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Registry **default** stance before site-type / page-type / blueprint override |
| **Допустимые значения** | `Required` · `Optional` · `Recommended` · `Contextual` · `Forbidden` (registry-level default only) |
| **Правило** | Blueprint and page mapping **override** this default |

---

### 9. `dependencies`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Hard (`requires`) and soft (`recommends`) deps — block_id, page_type, or external system |
| **Источник** | [BLOCK-DEPENDENCY-RULES-v1.md](BLOCK-DEPENDENCY-RULES-v1.md) |
| **External examples** | Legal Pack v1 (FROZEN) · Consent Rule · Legal Entity Card · Contact Channel |

---

### 10. `exclusions`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Site types, page types, or block_id pairings forbidden without reclassification |
| **Правило** | Violation → halt + HITL |

---

### 11. `notes`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Operator guidance: variants, reference partials, HITL triggers, known gaps |
| **Пример** | «Sticky mobile bar — CTA implementation variant, not separate block_id» |

---

## Contract instance template

```markdown
### {BLOCK_ID}

| Поле | Значение |
|------|----------|
| **block_id** | `{BLOCK_ID}` |
| **block_name** | {Human name} |
| **block_category** | {CATEGORY} |
| **purpose** | {Purpose text} |
| **conversion_role** | {ROLE} |
| **allowed_site_types** | {LIST} |
| **allowed_page_types** | {LIST} |
| **required_or_optional** | {Default stance} |
| **dependencies** | {requires / recommends} |
| **exclusions** | {FORBIDDEN pairings} |
| **notes** | {Guidance} |
```

---

## Validation rules (documentation-level)

| Rule | Description |
|------|-------------|
| **Unique block_id** | No duplicate keys in BLOCK-REGISTRY-v1 |
| **Category membership** | Every block_id appears exactly once in BLOCK-CATEGORY-SYSTEM-v1 |
| **Conversion role assignment** | Every block_id appears exactly once in BLOCK-CONVERSION-ROLES-v1 |
| **Matrix coverage** | Every Core block_id has row in SITE-TYPE-BLOCK-MATRIX-v2 |
| **Page mapping coverage** | Every block_id has stance per applicable page_type in PAGE-BLOCK-MAPPING-v1 |
| **Blueprint mapping coverage** | Every block_id has stance per applicable blueprint in BLUEPRINT-BLOCK-MAPPING-v1 |
| **Dependency closure** | Hard deps must reference existing block_id or frozen external system |
| **One primary conversion** | ≤1 `PRIMARY_CONVERSION` block as page primary — see conversion roles |

---

## Relationship to other contracts

| Layer | Contract | Block contract feeds |
|-------|----------|---------------------|
| Site type | SITE-TYPE-REGISTRY-v1 | `allowed_site_types` |
| Blueprint | BLUEPRINT-CONTRACT-v1 | `required_blocks` / `optional_blocks` → block_id |
| Page | PAGE-CONTRACT-v1 | `required_blocks` / `optional_blocks` / `forbidden_blocks` |
| Legal | LEGAL-PACK-v1-FREEZE | LEGAL_LINKS, form blocks |
| Design | **FUTURE** Design System Mapping | block_id → tokens/components |

---

## SAFE UNKNOWN

- JSON Schema export of this contract — **not created** in v1
- Automated contract linter — **not implemented**
- Extended Type block contracts (SAAS, WEB_APPLICATION, MARKETPLACE) — **out of scope**

---

*Block Contract version: v1. Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
