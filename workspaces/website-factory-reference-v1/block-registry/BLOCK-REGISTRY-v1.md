# Website Factory — Block Registry v1

**Версия:** v1.1 *(WF-R01.2 Gate 2 — additive structural slice)*  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** **канонический Block Registry** Website Factory — Block Registry Alignment v1 — **documentation only**  
**Не является:** runtime, CMS schema, component library, автоматическая валидация, design generation, frontend implementation

**Production bridge:**

```
Site Type → Blueprint → Pages → Blocks → Design → Frontend
```

**Связанные документы:**

| Документ | Назначение |
|----------|------------|
| [BLOCK-CONTRACT-v1.md](BLOCK-CONTRACT-v1.md) | Обязательные поля каждого block_id |
| [BLOCK-CATEGORY-SYSTEM-v1.md](BLOCK-CATEGORY-SYSTEM-v1.md) | Primary block_category taxonomy |
| [BLOCK-REGISTRY-AUDIT-v1.md](BLOCK-REGISTRY-AUDIT-v1.md) | Audit — duplicates, drift, gaps |
| [PAGE-BLOCK-MAPPING-v1.md](PAGE-BLOCK-MAPPING-v1.md) | REQUIRED / OPTIONAL / FORBIDDEN per page_type |
| [BLUEPRINT-BLOCK-MAPPING-v1.md](BLUEPRINT-BLOCK-MAPPING-v1.md) | REQUIRED / OPTIONAL / FORBIDDEN per Blueprint |
| [CORE-BLOCK-LIBRARY-v1.md](CORE-BLOCK-LIBRARY-v1.md) | Library overview + placement |
| [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md) | REQUIRED / OPTIONAL / FORBIDDEN per Core type |
| [BLOCK-DEPENDENCY-RULES-v1.md](BLOCK-DEPENDENCY-RULES-v1.md) | Inter-block relationships |
| [BLOCK-CONVERSION-ROLES-v1.md](BLOCK-CONVERSION-ROLES-v1.md) | Conversion classes |
| [BLOCK-IMPLEMENTATION-RULES-v1.md](BLOCK-IMPLEMENTATION-RULES-v1.md) | Factory usage flow |
| [BLOCK-REGISTRY-GAPS-v1.md](BLOCK-REGISTRY-GAPS-v1.md) | Cross-layer alignment gaps |
| [BLOCK-GAPS-v1.md](BLOCK-GAPS-v1.md) | Implementation / design gaps |
| [BLOCK-CATEGORIES-v1.md](BLOCK-CATEGORIES-v1.md) | Alias → BLOCK-CATEGORY-SYSTEM-v1 |
| [../registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | Site types |
| [../blueprints/BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md) | Blueprints |
| [../registry/SITE-TYPE-BLOCK-MAPPING-v1.md](../registry/SITE-TYPE-BLOCK-MAPPING-v1.md) | Predecessor mapping (superseded for `block_id` by this registry) |

**Reference implementation (partial):** `workspaces/website-factory-reference-v1/src/partials/sections/` — hero, benefits, process, testimonials, trust, pricing, lead_form, cta_band, contact_block, sticky_cta, faq, cases, footer.

**Предшественник (не канон v1):** `projects/mars-website-factory/block-registry-v0.md` — snake_case IDs, v0 site types; **не смешивать** без charter.

---

## Field schema

Authoritative contract: [BLOCK-CONTRACT-v1.md](BLOCK-CONTRACT-v1.md).

| Поле | Формат | Описание |
|------|--------|----------|
| **block_id** | UPPER_SNAKE_CASE | Стабильный ключ |
| **block_name** | Human label | Отображаемое имя |
| **block_category** | category_id из BLOCK-CATEGORY-SYSTEM-v1 | Одна primary category (`primary_category` = alias) |
| **purpose** | Text | Зачем блок существует |
| **conversion_role** | Из BLOCK-CONVERSION-ROLES-v1 | PRIMARY / SECONDARY / TRUST / INFO / LEGAL / SYSTEM |
| **allowed_site_types** | Subset of Core types | Где блок **может** применяться |
| **allowed_page_types** | Subset of PAGE-TYPE-REGISTRY-v1 | Где блок **может** размещаться на странице |
| **required_or_optional** | Registry default | Default stance **до** matrix override |
| **dependencies** | block_id or external | Hard deps — см. BLOCK-DEPENDENCY-RULES-v1 |
| **exclusions** | Site types, page types, or blocks | Forbidden pairings |
| **notes** | Text | Variants, partials, HITL, gaps |

Per-site-type stance — [SITE-TYPE-BLOCK-MATRIX-v2.md](SITE-TYPE-BLOCK-MATRIX-v2.md) · per Blueprint — [BLUEPRINT-BLOCK-MAPPING-v1.md](BLUEPRINT-BLOCK-MAPPING-v1.md) · per page_type — [PAGE-BLOCK-MAPPING-v1.md](PAGE-BLOCK-MAPPING-v1.md).

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

**Reference partial:** `benefits.html` (T1+ — WF-R01.3.2 Wave A1)

---

### FEATURES

| Поле | Значение |
|------|----------|
| **block_id** | `FEATURES` |
| **block_name** | Features / capabilities |
| **block_category** | CONTENT |
| **purpose** | Product or service capability lists, spec highlights, feature grids — distinct from outcome-oriented BENEFITS |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **allowed_page_types** | LANDING_PAGE, SERVICE_PAGE, PRODUCT_PAGE, HOME_PAGE |
| **required_or_optional** | Optional (context-dependent) |
| **dependencies** | recommends `HERO` or `PRODUCT_CARD` context |
| **exclusions** | ABOUT_PAGE as primary (use ABOUT block) |
| **notes** | Common on PDP and service money pages; SAAS-style feature grids map here in Extended types |

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

### CATEGORY_GRID

| Поле | Значение |
|------|----------|
| **block_id** | `CATEGORY_GRID` |
| **block_name** | Category tile grid |
| **block_category** | CATALOG |
| **purpose** | Visual grid of category tiles on shop/catalog home — entry to PLP routes |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | CATALOG, ECOMMERCE, CORPORATE (subtree) |
| **allowed_page_types** | HOME_PAGE |
| **required_or_optional** | Optional (recommended on catalog home) |
| **dependencies** | **requires** `CATEGORIES` taxonomy from Blueprint |
| **exclusions** | LANDING, PROMO |
| **notes** | Distinct from `CATEGORIES` nav/tree; v1 mapping "Category grid" from SITE-TYPE-BLOCK-MAPPING-v1 resolves here |

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
| **dependencies** | **requires** `CATEGORIES`; **recommends** `FILTERS` when filterable PLP |
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

**Reference partial:** `process.html` (T1+ — WF-R01.3.2 Wave A2)

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

**Reference partial:** `testimonials.html` — **PARTIAL** (WF-R01.3.2 Wave A3)

---

### REVIEWS

| Поле | Значение |
|------|----------|
| **block_id** | `REVIEWS` |
| **block_name** | Reviews / ratings (UGC) |
| **block_category** | TRUST |
| **purpose** | User-generated reviews with ratings, review lists — especially ECOMMERCE PDP and REVIEWS_PAGE hub |
| **conversion_role** | TRUST_SUPPORT |
| **allowed_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **allowed_page_types** | PRODUCT_PAGE, REVIEWS_PAGE, HOME_PAGE |
| **required_or_optional** | Optional (CATALOG); Recommended/Required (ECOMMERCE when reviews enabled) |
| **dependencies** | authentic UGC required — HITL; **requires** REVIEWS_PAGE or PDP context |
| **exclusions** | LANDING (use TESTIMONIALS for curated quotes) |
| **notes** | Distinct from `TESTIMONIALS` (curated editorial quotes); ECOMMERCE Blueprint "Reviews" maps here |

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

**Reference partial:** `trust.html` — **PARTIAL, narrowed** (WF-R01.3.2 Wave A3; metrics/logos/badges only)

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

## Structural Block Registry (WF-R01.2 Gate 2)

Tier A structural blocks — F3 Block → Structural Subtype. Authority: [wf-r01-2-structural-blocks-charter-v1.md](../../../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md).

### HEADER_NAV

| Поле | Значение |
|------|----------|
| **block_id** | `HEADER_NAV` |
| **block_name** | Header / primary navigation |
| **primary_category** | NAVIGATION |
| **purpose** | Global shell navigation: brand anchor, primary menu, utility slots (account/cart/phone/language), mobile drawer — persistent across route groups; enables orientation and IA traversal without carrying page narrative |
| **conversion_role** | SYSTEM |
| **allowed_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE; LANDING — contextual minimal (matrix override) |
| **allowed_page_types** | HOME_PAGE, LANDING_PAGE, SERVICE_PAGE, CATEGORY_PAGE, PRODUCT_PAGE, ABOUT_PAGE, CONTACT_PAGE, FAQ_PAGE, REVIEWS_PAGE, LEGAL_PAGE |
| **required_or_optional** | Contextual |
| **dependencies** | **recommends** `FOOTER`, `LEGAL_LINKS`; **requires** Blueprint global shell zone; **requires** [layout-shell-governance.md](../../../projects/mars-website-factory/layout-shell-governance.md) — HEADER ≠ HERO |
| **exclusions** | **Forbidden** absorption of `HERO` content; **Forbidden** separate ids: `MEGA_MENU`, `MOBILE_NAV_DRAWER`, `UTILITY_NAV`, `SKIP_LINK` — variants/composition in notes |
| **notes** | `maturity: standard` (RV-01 Core); `context_dependent: true`; `structural_subtype: true`; `vocabulary_source: WF-R01.2 ACCEPTED charter`; `mega_menu: variant` (not separate block_id); `utility_nav: composition` (cart icon ≠ `CART` page block); WF-R01.1 role `nav_mega_or_primary` → this id; `reference_partial: PENDING — WF-R01.3` |

**Reference partial:** **PENDING** — WF-R01.3.2/3.3

---

### FILTERS

| Поле | Значение |
|------|----------|
| **block_id** | `FILTERS` |
| **block_name** | Filters / refinement controls |
| **primary_category** | NAVIGATION |
| **purpose** | Faceted and refinement controls on PLP/list surfaces — control surface operating on inventory views; distinct from `PRODUCT_GRID` result surface |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | CATALOG, ECOMMERCE; CORPORATE — catalog subtree only; **excluded** LANDING, PROMO |
| **allowed_page_types** | CATEGORY_PAGE (primary); HOME_PAGE when catalog hub exposes filterable grid |
| **required_or_optional** | Contextual |
| **dependencies** | **requires** `PRODUCT_GRID` or list context on page; **recommends** `CATEGORIES`; **recommends** `HEADER_NAV` (shell); sort order = sub-variant in notes (`SORT_CONTROLS` forbidden as id) |
| **exclusions** | **Forbidden** on LANDING, PROMO; **Forbidden** merge into `PRODUCT_GRID` markup; **Forbidden** separate `SORT_CONTROLS`, `FACET_CHIPS`, `RESULTS_META` ids |
| **notes** | `maturity: common` (RV-01 context-dependent Core); `context_dependent: true`; `structural_subtype: true`; `vocabulary_source: WF-R01.2 ACCEPTED charter`; faceted SEO URL behavior → WF-R01.5 FUTURE; `reference_partial: PENDING — WF-R01.3` |

**Reference partial:** **PENDING** — WF-R01.3.4 W4

---

### SEARCH

| Поле | Значение |
|------|----------|
| **block_id** | `SEARCH` |
| **block_name** | Site / catalog search |
| **primary_category** | NAVIGATION |
| **purpose** | Query entry (header field, overlay, or dedicated surface), suggestions, and routing to results — discovery primitive for large IA and catalog findability |
| **conversion_role** | INFORMATIONAL |
| **allowed_site_types** | CATALOG, ECOMMERCE (obligatory); PROMO, CORPORATE (recommended); LANDING — forbidden/default off |
| **allowed_page_types** | Global shell (all multi-page types above); results host — `SEARCH_RESULTS_PAGE` glossary/planned; until page_type row exists, document `/search/` route in Blueprint notes |
| **required_or_optional** | Contextual |
| **dependencies** | **recommends** `HEADER_NAV` (typical placement); **recommends** `PRODUCT_GRID` on results pages; soft pair with `FILTERS` on catalog surfaces |
| **exclusions** | **Forbidden** as primary conversion surface on LANDING; **Forbidden** duplication of `CATEGORIES` tree navigation semantics |
| **notes** | `maturity: common` (RV-01); `context_dependent: true`; `structural_subtype: true`; `vocabulary_source: WF-R01.2 ACCEPTED charter`; RV-01 flags Search Results as Missing page type — R01.3.4 scaffold; `reference_partial: PENDING — WF-R01.3` |

**Reference partial:** **PENDING** — WF-R01.3.4 W4

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

**Reference partial:** `footer.html` — **PARTIAL** (WF-R01.3.2 Wave B1)

---

## Validation summary

| Check | Result |
|-------|--------|
| Core site types only in matrix v2 | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| No blocks for SAAS / WEB_APPLICATION / MARKETPLACE | **Confirmed** — Extended types out of Core Library v1 |
| Block count | **32** canonical `block_id` entries (29 Core + 3 structural Tier A) |
| Structural Tier A (WF-R01.2) | `HEADER_NAV`, `FILTERS`, `SEARCH` — registry rows **COMPLETE**; partials **PENDING** WF-R01.3 |
| Blueprint alignment | [BLUEPRINT-BLOCK-MAPPING-v1.md](BLUEPRINT-BLOCK-MAPPING-v1.md) |
| Page alignment | [PAGE-BLOCK-MAPPING-v1.md](PAGE-BLOCK-MAPPING-v1.md) |
| Contract compliance | [BLOCK-CONTRACT-v1.md](BLOCK-CONTRACT-v1.md) |

---

## SAFE UNKNOWN

- JSON Schema export for blocks — **not defined**
- Header/nav, filters, search registry rows — **CLOSED** (WF-R01.2 Gate 2); reference partials — **OPEN** → WF-R01.3
- Automated sync with reference partial filenames — **manual** mapping only

---

*Registry version: v1.1 (WF-R01.2 Gate 2 structural slice). Canonical location: `workspaces/website-factory-reference-v1/block-registry/`.*
