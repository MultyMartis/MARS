# Website Factory — Page Type Registry v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** каноническая классификация страниц — **documentation only**  
**Связь:** [PAGE-CONTRACT-v1.md](PAGE-CONTRACT-v1.md), [SITE-TYPE-PAGE-MATRIX-v1.md](SITE-TYPE-PAGE-MATRIX-v1.md)

**Не является:** CMS post types, URL router config, sitemap generator

---

## Назначение

Page Type Registry v1 — **стабильные `page_type` коды** для Page Architecture Contracts. Blueprint `required_pages` **маппятся** на `page_type` из этого реестра.

**Минимальный набор v1 (10 типов):** см. таблицы ниже.

**Расширения (не в минимальном реестре):** `CART_PAGE`, `CHECKOUT_PAGE`, `ORDER_CONFIRMATION_PAGE` — документированы в [PAGE-DEPENDENCY-RULES-v1.md](PAGE-DEPENDENCY-RULES-v1.md) для ECOMMERCE only.

---

## HOME_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `HOME_PAGE` |
| **Purpose** | Главная точка входа multi-page сайта: бренд, навигация к money pages, первичный CTA |
| **Typical use** | `/` на PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **Allowed site types** | `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Notes** | На `LANDING` — **FORBIDDEN** (используется `LANDING_PAGE`) |

---

## LANDING_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `LANDING_PAGE` |
| **Purpose** | Единая conversion surface: линейное повествование, один primary CTA path |
| **Typical use** | `/` на `LANDING`; campaign one-pagers на других типах (optional) |
| **Allowed site types** | `LANDING` (required); `PROMO`, `CORPORATE` (optional campaign) |
| **Notes** | Не путать с site type `LANDING` — это **page** type |

---

## SERVICE_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `SERVICE_PAGE` |
| **Purpose** | Money page услуги: описание, proof, форма/CTA |
| **Typical use** | `/services/{slug}/`, `/solutions/{slug}/` |
| **Allowed site types** | `PROMO`, `CORPORATE` |
| **Notes** | Services **index** может быть `HOME_PAGE` section или отдельный hub — документировать в project IA |

---

## CATEGORY_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `CATEGORY_PAGE` |
| **Purpose** | PLP / category hub: intro, grid, filters, drill-down к PDP |
| **Typical use** | `/{category}/`, `/catalog/{category}/` |
| **Allowed site types** | `CATALOG`, `ECOMMERCE`, `CORPORATE` (catalog subtree) |
| **Notes** | Требует category tree из Blueprint |

---

## PRODUCT_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `PRODUCT_PAGE` |
| **Purpose** | PDP: specs, gallery, trust, conversion (RFQ / ATC / CTA) |
| **Typical use** | `…/{product-slug}/` |
| **Allowed site types** | `CATALOG`, `ECOMMERCE`, `CORPORATE` (catalog/ecommerce subtree) |
| **Notes** | CATALOG: RFQ/contact CTA; ECOMMERCE: add-to-cart path |

---

## ABOUT_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `ABOUT_PAGE` |
| **Purpose** | История компании, команда, миссия — trust без direct commerce |
| **Typical use** | `/about/`, `/company/` |
| **Allowed site types** | `PROMO`, `CORPORATE` |
| **Notes** | **FORBIDDEN** на `LANDING` (reclassify → PROMO) |

---

## CONTACT_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `CONTACT_PAGE` |
| **Purpose** | Контактный hub: NAP, map, форма, часы работы |
| **Typical use** | `/contacts/`, `/contact/` |
| **Allowed site types** | `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Notes** | На `LANDING` контакты — **блок** на `LANDING_PAGE`, не отдельный route (optional `/contacts/` — project) |

---

## FAQ_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `FAQ_PAGE` |
| **Purpose** | Централизованный FAQ hub (дублирует или расширяет inline FAQ block) |
| **Typical use** | `/faq/`, `/help/faq/` |
| **Allowed site types** | `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Notes** | На `LANDING` FAQ — **блок** `FAQ` на primary page; отдельный `FAQ_PAGE` optional |

---

## REVIEWS_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `REVIEWS_PAGE` |
| **Purpose** | Агрегированные отзывы, рейтинги, кейсы-как-social-proof |
| **Typical use** | `/reviews/`, `/testimonials/`, `/clients/` |
| **Allowed site types** | `PROMO`, `CORPORATE` |
| **Notes** | Distinct from inline `TESTIMONIALS` / `TRUST` blocks on money pages |

---

## LEGAL_PAGE

| Поле | Значение |
|------|----------|
| **Code** | `LEGAL_PAGE` |
| **Purpose** | Юридический документ L1–L4 (или extension doc) |
| **Typical use** | `/privacy-policy/`, `/consent-personal-data/`, `/user-agreement/`, `/cookie-files-policy/` |
| **Allowed site types** | Все Core types при production + Legal Pack gate |
| **Notes** | Специализация: [LEGAL-PAGE-CONTRACT-v1.md](LEGAL-PAGE-CONTRACT-v1.md) |

---

## Mapping: Blueprint page role → page_type

| Blueprint page role (typical) | page_type |
|------------------------------|-----------|
| Primary landing | `LANDING_PAGE` |
| Home / shop home | `HOME_PAGE` |
| Service detail | `SERVICE_PAGE` |
| Category PLP | `CATEGORY_PAGE` |
| Product PDP | `PRODUCT_PAGE` |
| About | `ABOUT_PAGE` |
| Contacts | `CONTACT_PAGE` |
| FAQ hub | `FAQ_PAGE` |
| Reviews / testimonials hub | `REVIEWS_PAGE` |
| Legal L1–L4 | `LEGAL_PAGE` |

---

## SAFE UNKNOWN

- Blog / news `page_type` — **FUTURE** (`CONTENT_HUB_PAGE` not in v1 minimum)
- Account / buyer portal pages — **FUTURE** (ECOMMERCE extension)

---

*Page Type Registry version: v1.*
