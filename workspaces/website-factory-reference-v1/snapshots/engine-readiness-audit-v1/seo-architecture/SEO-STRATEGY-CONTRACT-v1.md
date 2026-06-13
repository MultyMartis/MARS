# Website Factory — SEO Strategy Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** site-level SEO contract — **documentation only**  
**Связь:** [SEO-ARCHITECTURE-SYSTEM-v2.md](SEO-ARCHITECTURE-SYSTEM-v2.md), [SITE-TYPE-SEO-MAPPING-v2.md](SITE-TYPE-SEO-MAPPING-v2.md)

**Не является:** SEO audit, content plan, keyword map, sitemap file.

---

## Назначение

SEO Strategy Contract v1 — **обязательные поля на уровне сайта** (проект / Blueprint instance), фиксируемые **после** классификации `site_type_code` и **до** Page SEO Contracts.

Один контракт на проект (или на зафиксированный Blueprint revision).

---

## Обязательные поля

### 1. `site_type_code`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| **Core production default** | `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Правило** | Без изменения Registry в рамках SEO workstream |

---

### 2. `blueprint_id`

| Атрибут | Требование |
|---------|------------|
| **Пример** | `PROMO-BLUEPRINT-v1` |
| **Источник** | Canonical Core Blueprint для типа |

---

### 3. `primary_seo_goal`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Одна формулировка primary organic/search architecture outcome |
| **Источник** | [SITE-TYPE-SEO-MAPPING-v2.md](SITE-TYPE-SEO-MAPPING-v2.md) — не переписывать против типа без reclassification |
| **Пример (PROMO)** | «Индексируемые money pages по услугам + local/brand visibility» |

---

### 4. `secondary_seo_goal`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Supporting SEO outcome (0–2 предложения) |
| **Пример (LANDING)** | «Минимальная техническая индексация бренда + offer; organic не primary» |

---

### 5. `primary_traffic_alignment`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Канал, доминирующий в Blueprint `typical_traffic_sources` |
| **Допустимые значения** | `PPC` · `ORGANIC` · `BRAND` · `DIRECT` · `EMAIL` · `MIXED` |
| **Правило** | LANDING default → `PPC`; CATALOG/ECOMMERCE → `ORGANIC` co-primary |

---

### 6. `intent_mix_profile`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Ordered list primary intent types для сайта (из [SEARCH-INTENT-MODEL-v1.md](SEARCH-INTENT-MODEL-v1.md)) |
| **Источник** | SITE-TYPE-SEO-MAPPING-v2 «Typical intent mix» |
| **Формат** | `INTENT_A` (dominant), `INTENT_B`, … |

---

### 7. `seo_depth`

| Атрибут | Требование |
|---------|------------|
| **Шкала** | `MINIMAL` · `SELECTIVE` · `STANDARD` · `DEEP` |
| **LANDING** | `MINIMAL` |
| **PROMO / CATALOG / ECOMMERCE / CORPORATE** | `STANDARD` или `DEEP` per mapping |
| **Смысл** | Глубина SEO architecture work (IA, indexation, internal linking policy) — **не** word count |

---

### 8. `content_depth`

| Атрибут | Требование |
|---------|------------|
| **Шкала** | `MINIMAL` · `MODERATE` · `RICH` |
| **Смысл** | Ожидаемая полнота **сигналов** на money pages (specs, proof, FAQ depth) — **не** generated copy |
| **Запрет** | Не задавать keyword density или article volume |

---

### 9. `priority_pages`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | List `page_type` — SEO-critical routes |
| **Источник** | SITE-TYPE-SEO-MAPPING-v2 + Blueprint `required_pages` |
| **Правило** | Subset of SITE-TYPE-PAGE-MATRIX REQUIRED + OPTIONAL SEO-critical |

---

### 10. `global_seo_exclusions`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Site-wide SEO anti-patterns (architecture level) |
| **Примеры** | «No blog-first IA on LANDING»; «No checkout indexation on ECOMMERCE» |
| **Источник** | SITE-TYPE-SEO-MAPPING-v2 + [SEO-IMPLEMENTATION-RULES-v1.md](SEO-IMPLEMENTATION-RULES-v1.md) |

---

### 11. `indexation_policy_summary`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Default index / noindex posture by page class (money, legal, utility) |
| **Запрет** | Не писать готовые meta robots strings как production copy |

---

### 12. `internal_linking_policy`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Hub-and-spoke vs single-page; money page linking rules |
| **Пример** | PROMO: HOME → SERVICE → CONTACT; CATALOG: HOME → CATEGORY → PRODUCT |

---

### 13. `schema_intent_summary`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Какие schema **типы** допустимы на уровне сайта (Organization, Product, …) |
| **Запрет** | Не генерировать JSON-LD; только architectural intent |
| **Источник** | SITE-TYPE-SEO-MAPPING-v1/v2 hints + honest inventory rules |

---

### 14. `dependencies`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Upstream gates: Page Architecture frozen, Validation PASS, Legal Pack when production |
| **Формат** | dependency · source · halt rule |

---

## Рекомендуемые метаданные

| Поле | Описание |
|------|----------|
| `seo_strategy_contract_id` | `{PROJECT}-SEO-STRATEGY-v1` |
| `frozen_date` | Operator freeze before Design |
| `operator_signoff` | HITL reference |

---

## Checklist (operator)

- [ ] Все 14 обязательных полей заполнены
- [ ] `site_type_code` согласован с Registry (no new types)
- [ ] `primary_seo_goal` не противоречит SITE-TYPE-SEO-MAPPING-v2
- [ ] `priority_pages` ⊆ allowed page types in SITE-TYPE-PAGE-MATRIX-v1
- [ ] `global_seo_exclusions` включают type-specific forbidden patterns
- [ ] Page SEO Contracts созданы для каждой `priority_pages` route

---

## SAFE UNKNOWN

- JSON Schema for SEO Strategy Contract — **FUTURE** (see gaps).
- Multi-locale strategy variants — project charter.

---

*SEO Strategy Contract version: v1.*
