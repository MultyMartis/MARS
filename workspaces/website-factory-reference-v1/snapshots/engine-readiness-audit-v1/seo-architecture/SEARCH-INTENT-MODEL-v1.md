# Website Factory — Search Intent Model v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** каноническая модель search intent — **documentation only**  
**Связь:** [SEO-ARCHITECTURE-SYSTEM-v2.md](SEO-ARCHITECTURE-SYSTEM-v2.md), [PAGE-SEO-CONTRACT-v1.md](PAGE-SEO-CONTRACT-v1.md)

**Не является:** keyword list, SERP classification tool, query research output, AI intent labelling.

---

## Назначение

Search Intent Model v1 — **стабильная таксономия** намерений поиска для привязки к `page_type` и SEO Strategy **до** создания контента.

Каждый production route получает **один primary** `intent_type` и опционально **secondary** intent(s) в Page SEO Contract.

---

## Легенда полей (per intent type)

| Поле | Описание |
|------|----------|
| **Purpose** | Зачем пользователь ищет; что хочет получить |
| **Search behaviour** | Типичные запросы, SERP expectations (архитектурно, не keyword DB) |
| **Typical pages** | `page_type` из [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) |
| **Conversion relationship** | Как intent связан с conversion path сайта |

---

## COMMERCIAL

| Поле | Значение |
|------|----------|
| **Purpose** | Оценить предложение, цену, условия покупки или заказа услуги до действия |
| **Search behaviour** | Запросы с коммерческими модификаторами («купить», «цена», «заказать», «стоимость»); сравнение предложений в выдаче; частые rich results (цена, наличие) на PDP/PLP |
| **Typical pages** | `PRODUCT_PAGE`, `CATEGORY_PAGE`, `HOME_PAGE` (shop entry), `SERVICE_PAGE` (priced services) |
| **Conversion relationship** | **Primary** для CATALOG / ECOMMERCE money routes; **secondary** на LANDING (offer evaluation в рамках одной страницы); ведёт к ATC, RFQ, form submit |

---

## TRANSACTIONAL

| Поле | Значение |
|------|----------|
| **Purpose** | Совершить действие сейчас: оформить, оплатить, забронировать, отправить заявку |
| **Search behaviour** | Высокий action intent; бренд + action; «оформить заказ» реже индексируется как отдельный URL |
| **Typical pages** | `PRODUCT_PAGE` (ECOMMERCE ATC path); utility routes cart/checkout — **SEO excluded** per implementation rules |
| **Conversion relationship** | **Primary** на PDP для ECOMMERCE; **не** SEO-target для checkout funnel; LANDING = single-page transactional surface |

---

## SERVICE

| Поле | Значение |
|------|----------|
| **Purpose** | Найти и выбрать поставщика услуги, специализацию, пакет работ |
| **Search behaviour** | «услуга + город», «под ключ», отраслевые запросы; local pack часто релевантен |
| **Typical pages** | `SERVICE_PAGE`, `HOME_PAGE` (PROMO hub), `CONTACT_PAGE` (supporting) |
| **Conversion relationship** | **Primary** для PROMO; **optional** для CORPORATE solutions; lead form / call CTA |

---

## INFORMATIONAL

| Поле | Значение |
|------|----------|
| **Purpose** | Узнать, понять, сравнить концепции без немедленной покупки |
| **Search behaviour** | «что такое», «как выбрать», guides; длинный хвост; featured snippets |
| **Typical pages** | `FAQ_PAGE`, `ABOUT_PAGE` (partial), blog/content hub — **FUTURE** `CONTENT_HUB_PAGE` not in registry v1 |
| **Conversion relationship** | **Supporting** — nurtures trust; **не** primary для LANDING; PROMO/CORPORATE — hub для internal linking to money pages |

---

## NAVIGATIONAL

| Поле | Значение |
|------|----------|
| **Purpose** | Попасть на известный сайт, раздел, документ, контакт |
| **Search behaviour** | Бренд + раздел; «компания X контакты», «X политика конфиденциальности» |
| **Typical pages** | `HOME_PAGE`, `CONTACT_PAGE`, `LEGAL_PAGE`, footer-linked utility |
| **Conversion relationship** | **Low direct conversion**; **high** satisfaction / trust; legal navigational queries → `LEGAL_PAGE` |

---

## BRAND

| Поле | Значение |
|------|----------|
| **Purpose** | Подтвердить легитимность бренда, репутацию, официальный сайт |
| **Search behaviour** | Чистый бренд, «официальный сайт», отзывы о бренде |
| **Typical pages** | `HOME_PAGE`, `ABOUT_PAGE`, `REVIEWS_PAGE`, `LANDING_PAGE` (campaign brand match) |
| **Conversion relationship** | **Primary** для CORPORATE home; supports PROMO; LANDING — brand + offer alignment on single URL |

---

## COMPARISON

| Поле | Значение |
|------|----------|
| **Purpose** | Сравнить варианты, конкурентов, модели, тарифы |
| **Search behaviour** | «X vs Y», «лучший», «рейтинг», «альтернатива»; этические ограничения на claims |
| **Typical pages** | `SERVICE_PAGE`, `PRODUCT_PAGE` (comparison blocks), dedicated comparison URL — **project optional**, not separate `page_type` v1 |
| **Conversion relationship** | **Secondary** commercial path; must link to clear primary CTA without cannibalizing money pages |

---

## LOCAL

| Поле | Значение |
|------|----------|
| **Purpose** | Найти бизнес рядом, филиал, доставку в регионе |
| **Search behaviour** | Geo modifiers, maps pack, NAP consistency |
| **Typical pages** | `CONTACT_PAGE`, `HOME_PAGE`, `SERVICE_PAGE` (local services), `LANDING_PAGE` (single-location offer) |
| **Conversion relationship** | **Primary** when business is local-first PROMO; **signal** via NAP blocks, not separate site type |

---

## Intent assignment rules (architecture)

1. Каждая indexable production page — **ровно один** primary `intent_type`.
2. Secondary intent — максимум **два**; документировать в Page SEO Contract.
3. `LEGAL_PAGE` → primary **NAVIGATIONAL** (compliance navigational); secondary **INFORMATIONAL** optional.
4. Cart / checkout utility (ECOMMERCE) → **не** assign SEO intent; **excluded** from indexation strategy.
5. Intent **не** меняет `site_type_code`; при систематическом mismatch → reclassification HITL.

---

## Intent × site type (typical mix summary)

| site_type_code | Dominant intents | Rare / excluded |
|----------------|------------------|-----------------|
| **LANDING** | COMMERCIAL, TRANSACTIONAL, BRAND | INFORMATIONAL hub, COMPARISON blog |
| **PROMO** | SERVICE, LOCAL, BRAND, COMMERCIAL | Pure TRANSACTIONAL checkout |
| **CATALOG** | COMMERCIAL, INFORMATIONAL (PDP specs) | TRANSACTIONAL checkout |
| **ECOMMERCE** | COMMERCIAL, TRANSACTIONAL (PDP only) | Checkout as SEO target |
| **CORPORATE** | BRAND, INFORMATIONAL, SERVICE, NAVIGATIONAL | LANDING-only TRANSACTIONAL |

Деталь: [SITE-TYPE-SEO-MAPPING-v2.md](SITE-TYPE-SEO-MAPPING-v2.md), [SEO-ARCHITECTURE-MATRIX-v1.md](SEO-ARCHITECTURE-MATRIX-v1.md).

---

## SAFE UNKNOWN

- Machine-readable intent classifier — **FUTURE**.
- Regional intent nuances (RU vs global) — project charter.
- AI Overviews / zero-click impact per intent — **not modeled** in v1.

---

*Search Intent Model version: v1.*
