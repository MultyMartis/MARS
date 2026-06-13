# Website Factory — Content Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** обязательный контракт полей для content binding (block / page / pattern scope)  
**Связь:** [CONTENT-SYSTEM-v1.md](CONTENT-SYSTEM-v1.md), [CONTENT-SIGNAL-REGISTRY-v1.md](CONTENT-SIGNAL-REGISTRY-v1.md)

**Не является:** copy template, CMS field schema, prompt spec, SEO meta template, JSON Schema export, runtime validator.

---

## Назначение

Каждая запись content binding (на уровне блока, страницы или задокументированного pattern scope) **обязана** соответствовать полям ниже.

Контракт описывает **семантические обязательства** (какие классы информации должны быть представлены), не формулировки.

---

## Обязательные поля

### 1. `content_id`

| Атрибут | Требование |
|---------|------------|
| **Тип** | Stable canonical key |
| **Формат** | `CC_` + UPPER_SNAKE_CASE scope suffix |
| **Примеры** | `CC_BLOCK_HERO`, `CC_PAGE_LANDING_PAGE`, `CC_SITE_LANDING` |
| **Правило** | Immutable в v1; новые id — только через registry charter + gap review |

**CC** = Content Contract entry (architectural binding record).

---

### 2. `content_role`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Одна primary роль записи в content architecture |
| **Допустимые значения** | `BLOCK_BINDING` · `PAGE_PROFILE` · `SITE_PROFILE` · `PATTERN_HINT` (documented only when cross-referenced to Design `VF_*`) |
| **Правило** | Ровно один primary `content_role` на запись |

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
| **Правило** | Empty list допустим **только** для `SITE_PROFILE` entries |

---

### 5. `supported_blocks`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) |
| **Формат** | One or more `block_id` |
| **Правило** | Must exist in Block Registry v1; empty list допустим **только** для `PAGE_PROFILE` / `SITE_PROFILE` without block scope |

---

### 6. `primary_goal`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | 1–3 предложения: какую **информационную или конверсионную задачу** закрывает binding |
| **Запрет** | Маркетинговые формулировки, slogans, примеры финального текста |

---

### 7. `required_signals`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [CONTENT-SIGNAL-REGISTRY-v1.md](CONTENT-SIGNAL-REGISTRY-v1.md) |
| **Формат** | List of `signal_id` |
| **Правило** | Каждый id должен быть в реестре; отсутствие required signal на production instance = content gate **INCOMPLETE** |

---

### 8. `optional_signals`

| Атрибут | Требование |
|---------|------------|
| **Формат** | List of `signal_id` |
| **Правило** | Subset of registry; operator/project may document chosen subset |

---

### 9. `forbidden_signals`

| Атрибут | Требование |
|---------|------------|
| **Формат** | List of `signal_id` |
| **Правило** | Overrides optional/required when misuse would violate site type, legal, or validation stance |
| **Примеры классов** | `urgency` на LEGAL_PAGE; `comparison` без catalog context; `price` на CATALOG PDP when RFQ-only |

---

### 10. `conversion_role`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [BLOCK-CONVERSION-ROLES-v1.md](../block-registry/BLOCK-CONVERSION-ROLES-v1.md) (для block scope) |
| **Допустимые значения** | `PRIMARY_CONVERSION` · `SECONDARY_CONVERSION` · `TRUST_SUPPORT` · `INFORMATIONAL` · `LEGAL` · `SYSTEM` · `PAGE_MIXED` (page profile only) |
| **Правило** | Block-level entries **должны** совпадать с Block Registry `conversion_role`, если scope = single `block_id` |

---

### 11. `trust_role`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Роль в trust stack: `NONE` · `PRIMARY_TRUST` · `SUPPORTING_TRUST` · `ENTITY_IDENTITY` · `SOCIAL_PROOF` · `COMPLIANCE` |
| **Правило** | Trust-bearing blocks (`TRUST`, `TESTIMONIALS`, `REVIEWS`, `CASES`, `CERTIFICATES`, `TEAM`, `ABOUT`) — non-`NONE` |

---

### 12. `notes`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | HITL gates, authentic UGC requirements, Legal Pack references, SEO/design alignment hints |
| **Запрет** | Sample headlines, body copy, meta strings |

---

## Связь с другими контрактами

| Layer | Contract | Content Layer usage |
|-------|----------|---------------------|
| Block | BLOCK-CONTRACT-v1 | `block_id`, `conversion_role`, allowed types |
| Page | PAGE-CONTRACT-v1 | `page_type`, `page_goal`, block stacks |
| SEO | PAGE-SEO-CONTRACT-v1 | Intent mix → signal emphasis |
| Design | VISUAL-PATTERN-CONTRACT-v1 | Pattern implements block; signals fill pattern slots |
| Legal | LEGAL-PAGE-CONTRACT-v1 | LEGAL_PAGE signal restrictions |

---

## Binding workflow (human-operated)

1. Resolve `site_type_code` + Blueprint.
2. Confirm Page Block Validation **not FAIL/CRITICAL**.
3. Select `page_type` → apply PAGE-CONTENT-CONTRACTS profile.
4. For each REQUIRED `block_id` on page → apply BLOCK-CONTENT-CONTRACTS.
5. Cross-check SITE-TYPE-CONTENT-MAPPING priorities and forbidden patterns.
6. Cross-check Design pattern (`VF_*`) does not imply forbidden signals.
7. Document project instance in IA — **без** генерации copy в v1.

---

## SAFE UNKNOWN

- JSON Schema for content contracts — **not defined**
- Per-locale required signal variants — **FUTURE**
- Machine-readable diff between Content v1 and CMS fields — **FUTURE**

---

*Content Contract version: v1. Canonical location: `workspaces/website-factory-reference-v1/content-contracts/`.*
