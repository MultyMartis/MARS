# Website Factory — Block Category System v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** каноническая primary category system — **documentation only**  
**Связь:** [BLOCK-CONTRACT-v1.md](BLOCK-CONTRACT-v1.md), [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md)

**Supersedes naming:** [BLOCK-CATEGORIES-v1.md](BLOCK-CATEGORIES-v1.md) remains as alias pointer; **this document is canonical** for `block_category`.

**Не является:** runtime taxonomy, CMS taxonomy engine, multi-tag classifier

---

## Назначение

Каждый canonical `block_id` принадлежит **ровно одной** primary `block_category`. Категория описывает IA / stack role; **не заменяет** `conversion_role` и **не переопределяет** site-type or page-type matrices.

**Правило v1:** secondary tagging запрещён. Project variants — в `notes`, не в category.

---

## Category registry

| category_id | Название | Назначение |
|-------------|----------|------------|
| `CONVERSION` | Conversion | Прямое или контекстное целевое действие: формы, CTA bands, cart/checkout path |
| `TRUST` | Trust | Снижение риска: social proof, отзывы, сертификаты, рейтинги |
| `CONTENT` | Content | Повествование, объяснение ценности, FAQ, process, hero, features |
| `CATALOG` | Catalog | Каталог: категории, сетки, карточки товаров/услуг |
| `COMPANY` | Company | О компании, команда, партнёры, кейсы, services hub |
| `CONTACT` | Contact | Контактные точки, карта, локации |
| `COMMERCE` | Commerce | Доставка, оплата — transaction-adjacent info (not cart/checkout) |
| `LEGAL` | Legal | Юридические ссылки и compliance surface |
| `NAVIGATION` | Navigation | Маршрутизация (v1: reserved — header/nav **GAP**) |
| `SYSTEM` | System | Footer shell, global chrome |

---

## Block assignment — full canonical set (29 blocks)

### CONVERSION

| block_id | block_name |
|----------|------------|
| `CTA` | CTA band / sticky CTA |
| `LEAD_FORM` | Lead / RFQ form |
| `CHECKOUT` | Checkout flow |
| `CART` | Shopping cart |

### TRUST

| block_id | block_name |
|----------|------------|
| `TRUST` | Social proof / logos / metrics |
| `TESTIMONIALS` | Testimonials — curated quotes |
| `REVIEWS` | Reviews — UGC ratings and review lists |
| `CERTIFICATES` | Certificates / licenses / awards |

### CONTENT

| block_id | block_name |
|----------|------------|
| `HERO` | Hero |
| `BENEFITS` | Benefits / value props |
| `FEATURES` | Features / capabilities / spec highlights |
| `PROCESS` | Process / how it works |
| `FAQ` | FAQ |
| `PRICING` | Pricing / tiers |

### CATALOG

| block_id | block_name |
|----------|------------|
| `CATEGORIES` | Category tree / taxonomy navigation |
| `CATEGORY_GRID` | Category tile grid (visual PLP entry) |
| `PRODUCT_GRID` | Product/service grid (PLP) |
| `PRODUCT_CARD` | Product/service card (grid unit or PDP) |

### NAVIGATION

| block_id | block_name |
|----------|------------|
| — | *Reserved — `HEADER_NAV` not in Core Library v1* |

### COMPANY

| block_id | block_name |
|----------|------------|
| `SERVICES` | Services overview |
| `CASES` | Cases / portfolio |
| `TEAM` | Team |
| `ABOUT` | About / company story |
| `PARTNERS` | Partners |

### CONTACT

| block_id | block_name |
|----------|------------|
| `CONTACTS` | Contact block |
| `MAP` | Map / locations |

### COMMERCE

| block_id | block_name |
|----------|------------|
| `DELIVERY` | Delivery / shipping info |
| `PAYMENT` | Payment methods / trust badges |

### LEGAL

| block_id | block_name |
|----------|------------|
| `LEGAL_LINKS` | Legal document links cluster |

### SYSTEM

| block_id | block_name |
|----------|------------|
| `FOOTER` | Footer shell |

---

## Category ↔ conversion_role (typical, not exclusive)

| block_category | Typical conversion_role |
|----------------|-------------------------|
| CONVERSION | PRIMARY_CONVERSION, SECONDARY_CONVERSION |
| TRUST | TRUST_SUPPORT |
| CONTENT | INFORMATIONAL, SECONDARY_CONVERSION |
| CATALOG | INFORMATIONAL |
| COMPANY | INFORMATIONAL, TRUST_SUPPORT |
| CONTACT | SECONDARY_CONVERSION, INFORMATIONAL |
| COMMERCE | INFORMATIONAL, TRUST_SUPPORT |
| LEGAL | LEGAL |
| NAVIGATION | SYSTEM, INFORMATIONAL |
| SYSTEM | SYSTEM |

Full role assignment: [BLOCK-CONVERSION-ROLES-v1.md](BLOCK-CONVERSION-ROLES-v1.md).

---

## Category decision guide

| If block primarily… | Assign category |
|---------------------|-----------------|
| Captures lead or completes purchase | CONVERSION |
| Shows logos, quotes, ratings, certs | TRUST |
| Explains offer, steps, FAQ, hero | CONTENT |
| Lists categories, grids, product units | CATALOG |
| Presents company, team, services, cases | COMPANY |
| Shows phone, email, map | CONTACT |
| Describes shipping or payment methods | COMMERCE |
| Links L1–L4 legal docs | LEGAL |
| Global footer / chrome | SYSTEM |

---

## SAFE UNKNOWN

- Subcategories (e.g. `TRUST > LOGOS`) — **not in v1**
- Multi-category blocks — **forbidden** in v1
- Header/nav `block_id` category assignment — **pending** HEADER_NAV charter

---

*Category System version: v1. Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
