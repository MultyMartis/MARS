# Website Factory — Block Registry v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** **первый канонический Block Registry** Website Factory — **documentation only**  
**Не является:** runtime, CMS schema, component library, автоматическая валидация, design generation, frontend implementation

**Production bridge:**

```
Site Type → Blueprint → Pages → Blocks → Design → Frontend
```

**Связанные документы:**

| Документ | Назначение |
|----------|------------|
| [BLOCK-CATEGORIES-v1.md](BLOCK-CATEGORIES-v1.md) | Primary categories |
| [CORE-BLOCK-LIBRARY-v1.md](CORE-BLOCK-LIBRARY-v1.md) | Library overview + placement |
| [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md) | REQUIRED / OPTIONAL / FORBIDDEN per Core type |
| [BLOCK-DEPENDENCY-RULES-v1.md](BLOCK-DEPENDENCY-RULES-v1.md) | Inter-block relationships |
| [BLOCK-CONVERSION-ROLES-v1.md](BLOCK-CONVERSION-ROLES-v1.md) | Conversion classes |
| [BLOCK-IMPLEMENTATION-RULES-v1.md](BLOCK-IMPLEMENTATION-RULES-v1.md) | Factory usage flow |
| [BLOCK-GAPS-v1.md](BLOCK-GAPS-v1.md) | Remaining gaps |
| [../registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | Site types |
| [../blueprints/BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md) | Blueprints |
| [../registry/SITE-TYPE-BLOCK-MAPPING-v1.md](../registry/SITE-TYPE-BLOCK-MAPPING-v1.md) | Predecessor mapping (superseded for `block_id` by this registry) |

**Reference implementation (partial):** `workspaces/website-factory-reference-v1/src/partials/sections/` — hero, social_proof, pricing, lead_form, cta_band, contact_block, sticky_cta, faq, cases.

**Предшественник (не канон v1):** `projects/mars-website-factory/block-registry-v0.md` — snake_case IDs, v0 site types; **не смешивать** без charter.

---

## Field schema

| Поле | Формат | Описание |
|------|--------|----------|
| **block_id** | UPPER_SNAKE_CASE | Стабильный ключ |
| **block_name** | Human label | Отображаемое имя |
| **primary_category** | category_id из BLOCK-CATEGORIES-v1 | Одна primary category |
| **purpose** | Text | Зачем блок существует |
| **conversion_role** | Из BLOCK-CONVERSION-ROLES-v1 | PRIMARY / SECONDARY / TRUST / INFO / LEGAL / SYSTEM |
| **allowed_site_types** | Subset of Core types | Где блок **может** применяться |
| **required_or_optional** | Registry default | Default stance **до** matrix override per site type |
| **dependencies** | block_id or external | Hard deps — см. BLOCK-DEPENDENCY-RULES-v1 |
| **exclusions** | Site types or blocks | Forbidden pairings |

Per-site-type REQUIRED/OPTIONAL/FORBIDDEN — **authoritative** in [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md).

---

## Core Block Registry

### HERO

| Поле | Значение |
|------|----------|
| **block_id** | `HERO` |
| **block_name** | Hero |
| **primary_category** | CONTENT |
| **purpose** | Above-the-fold value proposition: offer, audience, primary orientation |
| **conversion_role** | SECONDARY_CONVERSION |
| **allowed_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Required on primary pages per Blueprint |
| **dependencies** | Blueprint page intent; legal claims need HITL |
| **exclusions** | Pure app screens (WEB_APPLICATION — out of Core scope) |

**Reference partial:** `hero.html`

---

### BENEFITS

| Поле | Значение |
|------|----------|
| **block_id** | `BENEFITS` |
| **block_name** | Benefits / value props |
| **primary_category** | CONTENT |
| **purpose** | Enumerate value propositions, outcomes, differentiators |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | LANDING, PROMO, CORPORATE |
| **required_or_optional** | Required (LANDING); Optional/Recommended (others) |
| **dependencies** | recommends `HERO` above |
| **exclusions** | — |

**Reference partial:** inline / hero-adjacent (not separate partial in reference workspace)

---

### SERVICES

| Поле | Значение |
|------|----------|
| **block_id** | `SERVICES` |
| **block_name** | Services overview |
| **primary_category** | COMPANY |
| **purpose** | Present service/product lines with drill-down to money pages |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | PROMO, CORPORATE |
| **required_or_optional** | Required (PROMO home/services); Optional (CORPORATE as solutions hub) |
| **dependencies** | recommends `CASES`, `PROCESS` |
| **exclusions** | Catalog-scale PLP (use CATALOG blocks) |

---

### CATEGORIES

| Поле | Значение |
|------|----------|
| **block_id** | `CATEGORIES` |
| **block_name** | Category tree / PLP entry |
| **primary_category** | CATALOG |
| **purpose** | Taxonomy navigation — category hubs and tree entry |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | CATALOG, ECOMMERCE, CORPORATE (subtree) |
| **required_or_optional** | Required (CATALOG, ECOMMERCE) |
| **dependencies** | requires IA category tree from Blueprint |
| **exclusions** | LANDING, PROMO (without reclassification) |

---

### PRODUCT_GRID

| Поле | Значение |
|------|----------|
| **block_id** | `PRODUCT_GRID` |
| **block_name** | Product/service grid (PLP) |
| **primary_category** | CATALOG |
| **purpose** | Filterable grid of product/service cards on PLP |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | CATALOG, ECOMMERCE, CORPORATE (subtree) |
| **required_or_optional** | Required (CATALOG, ECOMMERCE PLP) |
| **dependencies** | requires `CATEGORIES`; recommends filters (GAP — not separate block_id) |
| **exclusions** | LANDING, PROMO |

---

### PRODUCT_CARD

| Поле | Значение |
|------|----------|
| **block_id** | `PRODUCT_CARD` |
| **block_name** | Product/service card |
| **primary_category** | CATALOG |
| **purpose** | Single item unit in grid or PDP summary — specs, gallery, CTA |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | CATALOG, ECOMMERCE, CORPORATE (subtree) |
| **required_or_optional** | Required (PDP/PLP) |
| **dependencies** | requires `PRODUCT_GRID` or `CATEGORIES` structure |
| **exclusions** | LANDING, PROMO |

---

### PRICING

| Поле | Значение |
|------|----------|
| **block_id** | `PRICING` |
| **block_name** | Pricing / tiers |
| **primary_category** | CONTENT |
| **purpose** | Packages, tiers, ballpark pricing — decision support |
| **conversion_role** | SECONDARY_CONVERSION |
| **allowed_site_types** | LANDING, PROMO, ECOMMERCE, CORPORATE |
| **required_or_optional** | Optional (context-dependent) |
| **dependencies** | recommends `LEAD_FORM` or `CTA` |
| **exclusions** | CATALOG (RFQ model — price on PDP optional, not tier block) |

**Reference partial:** `pricing.html`

---

### PROCESS

| Поле | Значение |
|------|----------|
| **block_id** | `PROCESS` |
| **block_name** | Process / how it works |
| **primary_category** | CONTENT |
| **purpose** | Step-by-step explanation of engagement or purchase path |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | LANDING, PROMO, CORPORATE |
| **required_or_optional** | Required (LANDING); Recommended (PROMO service pages) |
| **dependencies** | recommends `HERO`, `BENEFITS` before |
| **exclusions** | — |

---

### CASES

| Поле | Значение |
|------|----------|
| **block_id** | `CASES` |
| **block_name** | Cases / portfolio |
| **primary_category** | COMPANY |
| **purpose** | Outcome-based proof — projects, clients, results |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | LANDING, PROMO, CORPORATE |
| **required_or_optional** | Optional |
| **dependencies** | recommends `SERVICES` context |
| **exclusions** | — |

**Reference partial:** `cases.html`

---

### TESTIMONIALS

| Поле | Значение |
|------|----------|
| **block_id** | `TESTIMONIALS` |
| **block_name** | Testimonials / reviews |
| **primary_category** | TRUST |
| **purpose** | Quote-based social proof; product reviews on ECOMMERCE PDP |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | LANDING, PROMO, ECOMMERCE, CORPORATE |
| **required_or_optional** | Optional |
| **dependencies** | authentic content required — HITL |
| **exclusions** | — |

**Reference partial:** overlaps `social_proof.html` (logos/metrics variant → `TRUST`)

---

### TRUST

| Поле | Значение |
|------|----------|
| **block_id** | `TRUST` |
| **block_name** | Social proof / logos / metrics |
| **primary_category** | TRUST |
| **purpose** | Logo strip, stats, badges — rapid credibility |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Required (LANDING); Recommended (others) |
| **dependencies** | — |
| **exclusions** | — |

**Reference partial:** `social_proof.html`

---

### CERTIFICATES

| Поле | Значение |
|------|----------|
| **block_id** | `CERTIFICATES` |
| **block_name** | Certificates / licenses |
| **primary_category** | TRUST |
| **purpose** | Regulated industries — licenses, ISO, awards |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Optional (industry-dependent) |
| **dependencies** | HITL for claim accuracy |
| **exclusions** | — |

---

### TEAM

| Поле | Значение |
|------|----------|
| **block_id** | `TEAM` |
| **block_name** | Team |
| **primary_category** | COMPANY |
| **purpose** | Leadership and staff presentation |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | PROMO, CORPORATE |
| **required_or_optional** | Optional |
| **dependencies** | often on `ABOUT` page |
| **exclusions** | — |

---

### ABOUT

| Поле | Значение |
|------|----------|
| **block_id** | `ABOUT` |
| **block_name** | About / company story |
| **primary_category** | COMPANY |
| **purpose** | Entity narrative, history, mission |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | PROMO, CORPORATE |
| **required_or_optional** | Required (about page) |
| **dependencies** | recommends `TEAM`, `TRUST` |
| **exclusions** | — |

---

### FAQ

| Поле | Значение |
|------|----------|
| **block_id** | `FAQ` |
| **block_name** | FAQ |
| **primary_category** | CONTENT |
| **purpose** | Objection handling, support reduction |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Required (LANDING); Recommended (others) |
| **dependencies** | genuine Q&A only — schema optional |
| **exclusions** | — |

**Reference partial:** `faq.html`

---

### CTA

| Поле | Значение |
|------|----------|
| **block_id** | `CTA` |
| **block_name** | CTA band / sticky CTA |
| **primary_category** | CONVERSION |
| **purpose** | Repeated primary action — band and mobile sticky |
| **conversion_role** | PRIMARY_CONVERSION |
| **allowed_site_types** | LANDING, PROMO, ECOMMERCE, CORPORATE |
| **required_or_optional** | Required (LANDING); Contextual (others) |
| **dependencies** | single primary action aligned with Blueprint |
| **exclusions** | Site-wide sticky on PROMO (LANDING pattern) |

**Reference partials:** `cta_band.html`, `sticky_cta.html`

---

### LEAD_FORM

| Поле | Значение |
|------|----------|
| **block_id** | `LEAD_FORM` |
| **block_name** | Lead / RFQ form |
| **primary_category** | CONVERSION |
| **purpose** | Capture leads, RFQ, price requests |
| **conversion_role** | PRIMARY_CONVERSION |
| **allowed_site_types** | LANDING, PROMO, CATALOG, CORPORATE |
| **required_or_optional** | Required (LANDING); Contextual (others) |
| **dependencies** | **requires** Consent Rule; **requires** Legal Pack via `FOOTER`/`LEGAL_LINKS` |
| **exclusions** | ECOMMERCE primary path (checkout replaces) |

**Reference partial:** `lead_form.html`

---

### CONTACTS

| Поле | Значение |
|------|----------|
| **block_id** | `CONTACTS` |
| **block_name** | Contact block |
| **primary_category** | CONTACT |
| **purpose** | Phone, email, address, messengers — contact hub |
| **conversion_role** | SECONDARY_CONVERSION |
| **allowed_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Required (most Core types) |
| **dependencies** | Legal Entity Card for NAP |
| **exclusions** | — |

**Reference partial:** `contact_block.html`

---

### MAP

| Поле | Значение |
|------|----------|
| **block_id** | `MAP` |
| **block_name** | Map / locations |
| **primary_category** | CONTACT |
| **purpose** | Geo visualization, offices, dealer locations |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Optional |
| **dependencies** | recommends `CONTACTS` NAP consistency |
| **exclusions** | — |

---

### PARTNERS

| Поле | Значение |
|------|----------|
| **block_id** | `PARTNERS` |
| **block_name** | Partners |
| **primary_category** | COMPANY |
| **purpose** | Partner ecosystem, logos, partner CTAs |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | CORPORATE |
| **required_or_optional** | Optional (recommended for B2B corp) |
| **dependencies** | partner page in Blueprint |
| **exclusions** | LANDING (unless campaign-specific — HITL) |

---

### DELIVERY

| Поле | Значение |
|------|----------|
| **block_id** | `DELIVERY` |
| **block_name** | Delivery / shipping info |
| **primary_category** | COMMERCE |
| **purpose** | Shipping options, timelines, regions |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | ECOMMERCE, CORPORATE (ecommerce subtree) |
| **required_or_optional** | Recommended (ECOMMERCE) |
| **dependencies** | ECOMMERCE Blueprint; legal extension E3 **FUTURE** |
| **exclusions** | LANDING, PROMO, CATALOG |

---

### PAYMENT

| Поле | Значение |
|------|----------|
| **block_id** | `PAYMENT` |
| **block_name** | Payment methods / trust |
| **primary_category** | COMMERCE |
| **purpose** | Payment icons, security badges at checkout |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | ECOMMERCE, CORPORATE (ecommerce subtree) |
| **required_or_optional** | Required (checkout context) |
| **dependencies** | **requires** `CHECKOUT`; legal extension E2 **FUTURE** |
| **exclusions** | All non-commerce Core types |

---

### CHECKOUT

| Поле | Значение |
|------|----------|
| **block_id** | `CHECKOUT` |
| **block_name** | Checkout flow |
| **primary_category** | CONVERSION |
| **purpose** | Order completion — delivery, payment, consent |
| **conversion_role** | PRIMARY_CONVERSION |
| **allowed_site_types** | ECOMMERCE, CORPORATE (ecommerce subtree) |
| **required_or_optional** | Required (ECOMMERCE) |
| **dependencies** | **requires** `CART`; Consent Rule; Legal Pack |
| **exclusions** | LANDING, PROMO, CATALOG |

---

### CART

| Поле | Значение |
|------|----------|
| **block_id** | `CART` |
| **block_name** | Shopping cart |
| **primary_category** | CONVERSION |
| **purpose** | Line items, quantity, proceed to checkout |
| **conversion_role** | SECONDARY_CONVERSION |
| **allowed_site_types** | ECOMMERCE, CORPORATE (ecommerce subtree) |
| **required_or_optional** | Required (ECOMMERCE) |
| **dependencies** | **requires** `PRODUCT_CARD` / catalog context |
| **exclusions** | **LANDING, PROMO, CATALOG** — FORBIDDEN without reclassification |

---

### LEGAL_LINKS

| Поле | Значение |
|------|----------|
| **block_id** | `LEGAL_LINKS` |
| **block_name** | Legal document links |
| **primary_category** | LEGAL |
| **purpose** | Canonical L1–L4 links cluster (Footer Rule) |
| **conversion_role** | LEGAL |
| **allowed_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Required (production) |
| **dependencies** | **requires** Legal Pack v1 (FROZEN) |
| **exclusions** | — |

---

### FOOTER

| Поле | Значение |
|------|----------|
| **block_id** | `FOOTER` |
| **block_name** | Footer shell |
| **primary_category** | SYSTEM |
| **purpose** | Global footer — legal links slot, NAP, secondary nav |
| **conversion_role** | SYSTEM |
| **allowed_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **required_or_optional** | Required |
| **dependencies** | **requires** `LEGAL_LINKS` in production |
| **exclusions** | App-only screens without marketing shell |

---

## Validation summary

| Check | Result |
|-------|--------|
| Core site types only in matrix v2 | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| No blocks for SAAS / WEB_APPLICATION / MARKETPLACE | **Confirmed** — Extended types out of Core Library v1 |
| Block count | 26 canonical `block_id` entries |
| Blueprint alignment | Cross-checked with 5 Core Blueprints v1 |

---

## SAFE UNKNOWN

- JSON Schema export for blocks — **not defined**
- Header/nav as canonical `block_id` — **GAP** — see [BLOCK-GAPS-v1.md](BLOCK-GAPS-v1.md)
- Automated sync with reference partial filenames — **manual** mapping only

---

*Registry version: v1. Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
