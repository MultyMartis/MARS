# Website Factory — Page SEO Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** page-level SEO contract — **documentation only**  
**Связь:** [PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md) field `seo_requirements`, [SEARCH-INTENT-MODEL-v1.md](SEARCH-INTENT-MODEL-v1.md)

**Не является:** title/meta text, keyword list, schema JSON, content draft.

---

## Назначение

Page SEO Contract v1 — **обязательные SEO-поля для каждой production-страницы**, заполняемые после Site SEO Strategy и Page Architecture.

Детализирует `seo_requirements` в Page Contract v1 **без** замены остальных полей Page Contract.

---

## Обязательные поля

### 1. `page_type`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) |
| **Правило** | Must be allowed in [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md) for parent `site_type_code` |

---

### 2. `intent_type`

| Атрибут | Требование |
|---------|------------|
| **Источник** | [SEARCH-INTENT-MODEL-v1.md](SEARCH-INTENT-MODEL-v1.md) |
| **Формат** | One **primary** intent: `COMMERCIAL` · `TRANSACTIONAL` · `SERVICE` · `INFORMATIONAL` · `NAVIGATIONAL` · `BRAND` · `COMPARISON` · `LOCAL` |
| **Optional** | `secondary_intent_types` — list, max 2 |

---

### 3. `primary_goal`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Primary SEO outcome для этой страницы (1–2 предложения) |
| **Пример (`SERVICE_PAGE`)** | «Ранжирование по service + geo intent с конверсией в lead form» |
| **Запрет** | Не дублировать `page_goal` conversion wording без SEO angle |

---

### 4. `secondary_goal`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Supporting SEO outcome или «none» |
| **Пример (`PRODUCT_PAGE`)** | «Support category hub via internal links; capture long-tail spec queries» |

---

### 5. `required_content_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Architectural content **signals** that must exist (not copy) |
| **Примеры** | Unique H1 aligned with intent; spec table on PDP; service scope section; FAQ accordion for informational support |
| **Источник** | SITE-TYPE-SEO-MAPPING-v2 content_depth + CORE-PAGE-ARCHITECTURES block intent |
| **Запрет** | Keyword lists; word counts; generated paragraphs |

---

### 6. `required_conversion_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | CTA / form / ATC visibility aligned with intent and Blueprint |
| **Примеры** | Primary CTA above fold on `LANDING_PAGE`; RFQ on CATALOG PDP; ATC on ECOMMERCE PDP |
| **Источник** | Blueprint `conversion_requirements`, [BLOCK-CONVERSION-ROLES-v1.md](../block-registry/BLOCK-CONVERSION-ROLES-v1.md) |
| **Правило** | One primary conversion path per money page |

---

### 7. `required_trust_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Proof, legal, entity signals required for SEO trust (architecture) |
| **Примеры** | Testimonials block on service page; legal footer links on form pages; NAP on contact; authentic reviews policy on PDP |
| **Источник** | Legal mapping (read-only), block registry trust blocks |
| **Запрет** | Fabricated review schema intent |

---

### 8. `seo_depth`

| Атрибут | Требование |
|---------|------------|
| **Шкала** | `MINIMAL` · `SELECTIVE` · `STANDARD` · `DEEP` |
| **Правило** | Page depth ≤ site strategy ceiling from [SEO-STRATEGY-CONTRACT-v1.md](SEO-STRATEGY-CONTRACT-v1.md); may be lower on utility/legal |

---

### 9. `content_depth`

| Атрибут | Требование |
|---------|------------|
| **Шкала** | `MINIMAL` · `MODERATE` · `RICH` |
| **Правило** | Must satisfy `required_content_signals` level |

---

### 10. `exclusions`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Page-level SEO anti-patterns |
| **Примеры** | «No indexation of filtered facet URLs»; «No blog-length article on checkout»; «No competing H1 with HOME» |
| **Источник** | Site `global_seo_exclusions` + page-type defaults |

---

## Рекомендуемые поля (project IA)

| Поле | Описание |
|------|----------|
| `page_seo_contract_id` | `{PROJECT}-{page_type}-{slug}-SEO-v1` |
| `canonical_url` | Production URL |
| `indexation_intent` | `INDEX` · `NOINDEX` · `CONDITIONAL` |
| `schema_intent_types` | e.g. `Product`, `Service` — honest inventory only |
| `internal_link_targets` | Required outbound internal links (architecture) |

---

## Defaults by page_type (Core reference)

| page_type | Typical primary intent | Default seo_depth | Notes |
|-----------|------------------------|-------------------|-------|
| `LANDING_PAGE` | COMMERCIAL | MINIMAL | Single URL |
| `HOME_PAGE` | BRAND / NAVIGATIONAL | STANDARD | Hub |
| `SERVICE_PAGE` | SERVICE | STANDARD | Money |
| `CATEGORY_PAGE` | COMMERCIAL | DEEP | PLP |
| `PRODUCT_PAGE` | COMMERCIAL + TRANSACTIONAL | DEEP | PDP |
| `ABOUT_PAGE` | BRAND / INFORMATIONAL | SELECTIVE | Trust |
| `CONTACT_PAGE` | LOCAL / NAVIGATIONAL | SELECTIVE | NAP |
| `FAQ_PAGE` | INFORMATIONAL | SELECTIVE | Link to money |
| `REVIEWS_PAGE` | BRAND | SELECTIVE | Social proof hub |
| `LEGAL_PAGE` | NAVIGATIONAL | MINIMAL | Compliance |

Полная совместимость: [SEO-ARCHITECTURE-MATRIX-v1.md](SEO-ARCHITECTURE-MATRIX-v1.md).

---

## Checklist (operator)

- [ ] Все 10 обязательных полей заполнены
- [ ] `intent_type` согласован с SEARCH-INTENT-MODEL-v1
- [ ] `exclusions` не слабее site-level global exclusions
- [ ] Money pages имеют `required_conversion_signals`
- [ ] Form pages → trust signals include Legal Pack alignment
- [ ] Utility routes (cart/checkout) — **не** получают Page SEO Contract unless explicitly excluded with documented noindex

---

## SAFE UNKNOWN

- Formal merge of Page Contract + Page SEO Contract into one schema — **FUTURE**.
- Per-locale Page SEO Contract — project charter.

---

*Page SEO Contract version: v1.*
