# Website Factory — Visual Pattern Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** обязательный контракт полей для каждой записи [VISUAL-PATTERN-REGISTRY-v1.md](VISUAL-PATTERN-REGISTRY-v1.md)  
**Связь:** [DESIGN-SYSTEM-MAPPING-v1.md](DESIGN-SYSTEM-MAPPING-v1.md), [BLOCK-VISUAL-MAPPING-v1.md](BLOCK-VISUAL-MAPPING-v1.md)

**Не является:** design token schema, color palette, typography scale, CSS class naming, Figma component spec, React/Vue component API.

---

## Назначение

Каждый **visual pattern** (архитектурная семья компоновки и роли контента) **обязан** иметь запись с полями ниже.

Паттерн описывает **структурную роль** (что пользователь должен понять/сделать), не визуальный стиль.

---

## Обязательные поля

### 1. `pattern_id`

| Атрибут | Требование |
|---------|------------|
| **Тип** | Stable canonical key |
| **Формат** | `VF_` + UPPER_SNAKE_CASE |
| **Пример** | `VF_HERO_VALUE_PROPOSITION` |
| **Правило** | Immutable в v1; новые id — только через registry charter + gap review |

**VF** = Visual Family (architectural pattern entry).

---

### 2. `pattern_name`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Human-readable operator label |
| **Пример** | Hero — value proposition led |

---

### 3. `supported_site_types`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| **Формат** | List of `site_type_code` |
| **Правило** | Subset of approved types; must not introduce new codes |

---

### 4. `supported_page_types`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) |
| **Формат** | List of `page_type` (v1 minimum 10) |
| **Правило** | Empty list **forbidden** — every pattern must declare at least one page context |

---

### 5. `supported_blocks`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) |
| **Формат** | One or more `block_id` this pattern **implements** architecturally |
| **Правило** | Must exist in Block Registry v1; no synthetic blocks |

---

### 6. `purpose`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | 1–3 предложения: информационная/конверсионная роль паттерна |
| **Запрет** | Цвета, шрифты, px, brand adjectives («modern», «premium») |

---

### 7. `strengths`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Bullet list (2–5): когда паттерн усиливает IA |
| **Пример** | «Single primary action path — aligns with LANDING conversion» |

---

### 8. `weaknesses`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Bullet list (2–5): риски misuse или cognitive load |
| **Пример** | «Poor fit for deep catalog browse — competes with grid scan» |

---

### 9. `recommended_use`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | When to select this pattern (site + page + block context) |
| **Связь** | Must be consistent with SITE-TYPE-DESIGN-MAPPING and PAGE-TYPE-DESIGN-MAPPING |

---

### 10. `forbidden_use`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Explicit anti-patterns (reclassification triggers if needed) |
| **Пример** | «On LEGAL_PAGE — any marketing hero pattern» |

---

## Optional fields (v1 — not required)

| Field | Note |
|-------|------|
| `pattern_variant_of` | Parent `pattern_id` for future variant trees |
| `seo_alignment_notes` | Pointer to PAGE-SEO-CONTRACT — defer detail to SEO layer |
| `accessibility_role_hint` | **FUTURE** — register in gaps |

---

## Validation rules (documentation)

| Rule | Severity |
|------|----------|
| `pattern_id` unique in registry | CRITICAL |
| Every `supported_blocks` entry ∈ Block Registry | CRITICAL |
| Pattern on FORBIDDEN block stance for page | CRITICAL — invalid binding |
| Styling fields in any contract field | CRITICAL — out of scope violation |

---

## Production usage (human-operated)

1. Confirm Validation PASS for target page.
2. List REQUIRED `block_id` from PAGE-BLOCK-MAPPING.
3. For each block, choose **one** `pattern_id` from BLOCK-VISUAL-MAPPING allowed set.
4. Verify against SITE-TYPE-DESIGN-MAPPING (preferred/discouraged/forbidden families).
5. Verify against PAGE-TYPE-DESIGN-MAPPING (recommended/forbidden).
6. Record choices in project design log (format **FUTURE** — see gaps).

---

*Visual Pattern Contract version: v1.*
