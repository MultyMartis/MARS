# Website Factory — Blueprint System v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/blueprints/`  
**Статус:** каноническая архитектурная система Website Factory — **documentation only**  
**Не является:** runtime, генератором страниц, design tool, SEO engine, content pipeline

---

## Что такое Blueprint

**Blueprint** — канонический архитектурный документ, описывающий **что** представляет собой сайт данного типа до начала SEO, дизайна и frontend production.

Blueprint отвечает на вопросы:

- Какой это `site_type_code` и какова бизнес-цель?
- Какие страницы обязательны и какова их IA?
- Какие секции (blocks) обязательны, рекомендованы или исключены?
- Какие legal, SEO и conversion требования применяются?
- Что **явно запрещено** для данного типа?

Blueprint **не содержит** HTML, CSS, контент, мета-теги или юридический текст. Это **контракт планирования**, на который ссылаются downstream-этапы Factory.

---

## Назначение

| Цель | Описание |
|------|----------|
| **Единый источник IA** | Снимает неоднозначность «что строим» до design/frontend |
| **Gate до production** | Блокирует drift: SEO/design/frontend без Blueprint — нарушение Factory discipline |
| **Согласование подсистем** | Связывает Registry, Legal Pack, SEO Mapping, Block Mapping в один артефакт per site type |
| **Operator clarity** | Человек и agent видят mandatory vs optional до intake close |
| **Gap visibility** | Отдельный [BLUEPRINT-GAPS-v1.md](BLUEPRINT-GAPS-v1.md) фиксирует, чего не хватает для full generation |

---

## Lifecycle

```
Intake / classification
        ↓
site_type_code selected (Registry)
        ↓
Blueprint selected / instantiated (per contract)
        ↓
Page list + block stack frozen (project IA doc)
        ↓
Legal Pack applied (per Legal Mapping)
        ↓
SEO strategy (per SEO Mapping — Blueprint informs scope, not content)
        ↓
Design System mapping (per site type complexity)
        ↓
Frontend production (blocks from Block Mapping, aligned to Blueprint)
        ↓
QA / HITL / deploy gate
```

| Фаза | Blueprint role |
|------|----------------|
| **Draft** | Operator выбирает canonical Blueprint по `site_type_code`; допускаются project-specific optional blocks |
| **Frozen** | `required_pages`, `required_blocks`, `exclusions` зафиксированы до SEO/design; изменения — HITL + drift note |
| **Superseded** | Новая версия Blueprint (v2+) не отменяет frozen project без explicit migration charter |

---

## Связь с подсистемами

### Site Type Registry

- **Registry** определяет таксономию и описание типов: [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md)
- **Blueprint** — operational instantiation Registry для production: один canonical Blueprint per Core Type
- `site_type_code` в Blueprint **должен** совпадать с Registry; дополнительные типы **запрещены**

### Legal Pack

- **Legal Pack v1 (FROZEN):** [legal/](../legal/) — шаблоны L1–L4, consent rule, footer rule
- Blueprint ссылается на [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) для `legal_requirements`
- Blueprint **не дублирует** юридические тексты; фиксирует **какие** документы и **где** (footer, forms, checkout)

### SEO Mapping

- [SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — приоритет и архитектурный режим
- Blueprint переносит SEO в `seo_requirements`: indexation scope, IA implications, schema intent
- Blueprint **не генерирует** title, description, keywords

### Block Registry / Block Mapping

- [SITE-TYPE-BLOCK-MAPPING-v1.md](../registry/SITE-TYPE-BLOCK-MAPPING-v1.md) — роли блоков per type
- Blueprint `required_blocks` / `optional_blocks` **выравниваются** с Block Mapping
- Canonical `block_id` registry ([block-registry-v0.md](../../projects/mars-website-factory/block-registry-v0.md)) — **отдельный слой**; полное выравнивание — см. [BLUEPRINT-GAPS-v1.md](BLUEPRINT-GAPS-v1.md)

### Design System

- Reference tokens/components: `workspaces/website-factory-reference-v1/src/scss/`
- Blueprint задаёт **complexity и UX model** (single-page vs multi-page, catalog depth)
- Design System mapping per site type — **FUTURE** priority (см. roadmap)

### Frontend Production

- Reference workspace — golden pattern для **LANDING**
- Frontend **implements** Blueprint pages + blocks; не переопределяет exclusions
- Hybrid sites (CORPORATE): Blueprint per route group + primary project Blueprint

---

## Canonical Blueprints (Core Types v1)

| Blueprint | site_type_code | File |
|-----------|----------------|------|
| Landing | `LANDING` | [LANDING-BLUEPRINT-v1.md](LANDING-BLUEPRINT-v1.md) |
| Promo | `PROMO` | [PROMO-BLUEPRINT-v1.md](PROMO-BLUEPRINT-v1.md) |
| Catalog | `CATALOG` | [CATALOG-BLUEPRINT-v1.md](CATALOG-BLUEPRINT-v1.md) |
| Ecommerce | `ECOMMERCE` | [ECOMMERCE-BLUEPRINT-v1.md](ECOMMERCE-BLUEPRINT-v1.md) |
| Corporate | `CORPORATE` | [CORPORATE-BLUEPRINT-v1.md](CORPORATE-BLUEPRINT-v1.md) |

**Extended Types** (`SAAS`, `WEB_APPLICATION`, `MARKETPLACE`) — **без Blueprint в v1**; требуют architecture charter.

---

## Связанные документы

| Документ | Назначение |
|----------|------------|
| [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md) | Обязательные поля каждого Blueprint |
| [BLUEPRINT-COMPARISON-MATRIX-v1.md](BLUEPRINT-COMPARISON-MATRIX-v1.md) | Сравнение Core Types |
| [BLUEPRINT-IMPLEMENTATION-RULES-v1.md](BLUEPRINT-IMPLEMENTATION-RULES-v1.md) | Правила использования в Factory |
| [BLUEPRINT-GAPS-v1.md](BLUEPRINT-GAPS-v1.md) | Пробелы до full generation |

---

## SAFE UNKNOWN

- Machine-readable Blueprint schema (JSON/YAML) — **не определён**; канон — Markdown
- Automated Blueprint validation gate — **не реализован**
- Project-level Blueprint fork vs strict canonical — **operator policy**; default = canonical + optional blocks only

---

*Blueprint System version: v1. Canonical location: `workspaces/website-factory-reference-v1/blueprints/`.*
