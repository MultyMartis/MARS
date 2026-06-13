# Website Factory — Block Categories v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** alias pointer — **canonical category system:** [BLOCK-CATEGORY-SYSTEM-v1.md](BLOCK-CATEGORY-SYSTEM-v1.md)  
**Не является:** runtime taxonomy, CMS taxonomy engine, автоматическая классификация

**Связь:** [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [CORE-BLOCK-LIBRARY-v1.md](CORE-BLOCK-LIBRARY-v1.md)

---

## Назначение

Каждый блок Block Registry v1 принадлежит **одной primary category**. Категория определяет роль блока в IA и conversion stack, но **не заменяет** `conversion_role` и **не переопределяет** site type matrix.

**Правило:** secondary tagging (например, TRUST внутри Content) **запрещён** в v1 — один primary category на `block_id`.

---

## Категории

| category_id | Название | Назначение категории |
|-------------|----------|----------------------|
| `CONVERSION` | Conversion | Прямое или контекстное целевое действие: формы, CTA, checkout path |
| `TRUST` | Trust | Снижение риска, social proof, сертификаты, отзывы |
| `CONTENT` | Content | Повествование, объяснение ценности, FAQ, about, process |
| `CATALOG` | Catalog | Структура каталога: категории, сетки, карточки товаров/услуг |
| `NAVIGATION` | Navigation | Маршрутизация пользователя (в v1 — только FOOTER как system nav anchor; header/nav — **GAP**, см. [BLOCK-GAPS-v1.md](BLOCK-GAPS-v1.md)) |
| `COMPANY` | Company | О компании, команда, партнёры, кейсы как entity narrative |
| `CONTACT` | Contact | Контактные точки, карта, локации |
| `COMMERCE` | Commerce | Cart, checkout, payment, delivery — transaction path |
| `LEGAL` | Legal | Юридические ссылки и compliance surface |
| `SYSTEM` | System | Footer shell, legal links cluster, system chrome |

---

## Распределение блоков по категориям

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
| `TRUST` | Social proof / logos strip |
| `TESTIMONIALS` | Testimonials / reviews |
| `REVIEWS` | UGC reviews / ratings |
| `CERTIFICATES` | Certificates / licenses / awards |

### CONTENT

| block_id | block_name |
|----------|------------|
| `HERO` | Hero |
| `BENEFITS` | Benefits / value props |
| `FEATURES` | Features / capabilities |
| `PROCESS` | Process / how it works |
| `FAQ` | FAQ |
| `PRICING` | Pricing / tiers |

### CATALOG

| block_id | block_name |
|----------|------------|
| `CATEGORIES` | Category tree / PLP entry |
| `CATEGORY_GRID` | Category tile grid |
| `PRODUCT_GRID` | Product/service grid (PLP) |
| `PRODUCT_CARD` | Product/service card (unit in grid or list) |

### NAVIGATION

| block_id | block_name |
|----------|------------|
| — | *Reserved — header/nav block not in Core Library v1* |

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
| `FOOTER` | Footer shell (includes legal links slot) |

---

## Связь category ↔ conversion_role

| category_id | Typical conversion_role (not exclusive) |
|-------------|----------------------------------------|
| CONVERSION | PRIMARY_CONVERSION, SECONDARY_CONVERSION |
| TRUST | TRUST_SUPPORT |
| CONTENT | INFORMATIONAL |
| CATALOG | INFORMATIONAL, SECONDARY_CONVERSION |
| COMPANY | INFORMATIONAL, TRUST_SUPPORT |
| CONTACT | SECONDARY_CONVERSION, INFORMATIONAL |
| COMMERCE | PRIMARY_CONVERSION |
| LEGAL | LEGAL |
| SYSTEM | SYSTEM |

Полное назначение ролей — [BLOCK-CONVERSION-ROLES-v1.md](BLOCK-CONVERSION-ROLES-v1.md).

---

## SAFE UNKNOWN

- Subcategories (e.g. `TRUST > LOGOS`) — **not in v1**
- Multi-category blocks — **forbidden** in v1; use project IA notes for variants

---

*Categories version: v1. Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
