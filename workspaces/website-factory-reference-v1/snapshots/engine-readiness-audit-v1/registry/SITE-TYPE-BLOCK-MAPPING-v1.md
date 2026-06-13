# Website Factory — Site Type Block Mapping v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/registry/`  
**Связь:** [SITE-TYPE-REGISTRY-v1.md](SITE-TYPE-REGISTRY-v1.md)

**Reference blocks (implemented):** `workspaces/website-factory-reference-v1/src/partials/sections/` — hero, social_proof, pricing, lead_form, cta_band, contact_block, sticky_cta, faq, cases.

**Статус:** documentation only — block **roles** for planning (narrative labels).

> **Superseded (canonical `block_id`):** [block-registry/BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md), [block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md](../block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md), [block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md](../block-registry/BLUEPRINT-BLOCK-MAPPING-v1.md). This v1 file is retained for historical block **role** hints only — **do not delete**. Do **not** use `projects/mars-website-factory/block-registry-v0.md` as canonical for new artefacts.

**Legacy external (not canon v1):** `projects/mars-website-factory/block-registry-v0.md` — snake_case IDs; pointer discipline only.

**Легенда:**

| Маркер | Значение |
|--------|----------|
| **Required** | Типично обязателен для production-quality данного типа |
| **Recommended** | Часто используется; усиливает conversion/trust |
| **Optional** | По контексту проекта |
| **Excluded** | Несовместимо с типом без reclassification |

---

## LANDING

| Категория | Blocks |
|-----------|--------|
| **Required** | Hero · Benefits (value props) · Process (how it works) · Trust (social proof) · FAQ · CTA (cta_band / sticky_cta) · Lead form · Contact block · Legal footer |
| **Recommended** | Pricing (if offer has tiers) · Cases · Modal callback |
| **Optional** | Logo strip · Risk reversal · Countdown (campaign) |
| **Excluded** | Category grid · Filters · Cart · Checkout · Account dashboard |

**Typical page stack:** Hero → Benefits → Process → Social proof → Pricing (opt) → FAQ → Lead form → CTA band → Contact → Sticky CTA

---

## PROMO

| Категория | Blocks |
|-----------|--------|
| **Required** | Header/nav · Hero (brand/service) · Services overview · About/company · Contact block · Legal footer |
| **Recommended** | Cases/portfolio · Social proof · FAQ · CTA band · Team · Map/locations |
| **Optional** | Blog/news teaser · Pricing ballpark · Lead form (per service page) · Careers entry |
| **Excluded** | Cart · Checkout · Product filters (catalog-scale) · Sticky conversion CTA (unless specific money page) |

**Typical pages (blocks per page):**

- **Home:** Hero · Services teaser · Proof · CTA · Contact  
- **Service:** Hero · Scope · Process · Cases · FAQ · Form · Contact  
- **About:** Hero · Story · Team · Proof  
- **Contacts:** Contact block · Map · FAQ  

---

## CATALOG

| Категория | Blocks |
|-----------|--------|
| **Required** | Header/nav · Category grid (PLP) · Product/service cards · Filters · Search · PDP template (specs, gallery, CTA) · Breadcrumbs · Contact · FAQ · Legal footer |
| **Recommended** | Comparison table · Spec accordion · Downloads · Dealer/locator · RFQ form |
| **Optional** | Category intro SEO copy · Brand strip · Support links |
| **Excluded** | **Cart · Checkout · Payment summary · Order history** |

**Typical pages:**

- **Category (PLP):** Category hero/intro · Filters · Card grid · FAQ · Contacts  
- **Product (PDP):** Gallery · Specs · CTA (request/call) · Related · Contact  

---

## ECOMMERCE

| Категория | Blocks |
|-----------|--------|
| **Required** | Header/nav · Category PLP · Filters · Product cards · PDP (price, variants, add-to-cart) · **Cart** · **Checkout** · Trust/payment badges · Returns/shipping info · Contact · Legal footer |
| **Recommended** | Reviews · Recommendations · Size/guide · Promo banner · Sticky add-to-cart (mobile) |
| **Optional** | Account/login · Wishlist · Cross-sell · FAQ |
| **Excluded** | Seller onboarding · Multi-vendor store fronts (→ MARKETPLACE) |

**Typical pages:**

- **PLP:** Filters · Grid · Promo  
- **PDP:** Gallery · Price · ATC · Trust · Reviews  
- **Cart / Checkout:** Line items · Progress · Payment · Delivery  

---

## CORPORATE

| Категория | Blocks |
|-----------|--------|
| **Required** | Mega/primary nav · Brand hero · Solutions/services hub · Proof (logos/cases) · Contact · Legal footer |
| **Recommended** | Industries · Resource/blog teaser · Careers entry · Partner section · Newsroom · Global locations · Segment-specific CTAs |
| **Optional** | Investor snippet · Employee portal entry · Catalog/ecommerce subtree blocks (inherit CATALOG/ECOMMERCE) · Custom widgets per charter |
| **Excluded** | Single-page-only stack without IA · Pure dashboard blocks without marketing shell |

**Notes:** blocks **inherit from subtrees** — document per route group.

---

## SAAS

| Категория | Blocks |
|-----------|--------|
| **Required** | Marketing hero · Features · **Pricing tiers** · Signup/login entry · FAQ · Contact/support · Legal footer |
| **Recommended** | Social proof · Integration logos · Docs/help link · Product screenshots · CTA trial · Testimonials |
| **Optional** | Comparison · Changelog · Status page link · Blog |
| **Excluded** | Physical catalog PLP · Marketplace seller blocks · Industrial RFQ catalog patterns |

**App surface (authenticated):** dashboard, settings, billing — **outside** Website Factory v1 block kit; Extended architecture.

---

## WEB_APPLICATION

| Категория | Blocks |
|-----------|--------|
| **Required** | Login/auth · App shell (sidebar/top nav) · Dashboard/home · Data tables/forms · User menu · Legal links (minimal footer) |
| **Recommended** | Onboarding wizard · Notifications · Search (in-app) · Settings · Admin panels |
| **Optional** | Public marketing hero (if hybrid — use PROMO/LANDING blocks on public routes only) |
| **Excluded** | SEO landing blocks as primary · PPC sticky CTA · Catalog grid as core · Full marketing footer on app screens |

**Notes:** **Not a traditional website** — Factory conversion blocks apply only to optional public shell.

---

## MARKETPLACE

| Категория | Blocks |
|-----------|--------|
| **Required** | Platform hero · Category taxonomy · Listing cards · Listing detail · **Cart** · **Checkout** · Buyer account · Seller account entry · Search/filters · Trust/reviews · Contact · Legal footer |
| **Recommended** | Seller storefront · Seller onboarding · Rating/reviews · Dispute/help · Commission/fee disclosure · Platform proof |
| **Optional** | Featured listings · Promoted categories · Buyer protection banner · Seller dashboard (app-heavy) |
| **Excluded** | Single-vendor-only catalog without seller layer |

---

## Сводная таблица — ключевые blocks

| Block role | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE | SAAS | WEB_APP | MARKETPLACE |
|------------|---------|-------|---------|-----------|-----------|------|---------|-------------|
| Hero | ● | ● | ○ | ○ | ● | ● | ○ | ● |
| Lead form | ● | ○ | ○ | ○ | ○ | ○ | — | ○ |
| FAQ | ● | ○ | ○ | ○ | ○ | ● | — | ○ |
| Category/filters | — | — | ● | ● | ○ | — | — | ● |
| Cart/checkout | — | — | — | ● | — | — | — | ● |
| Pricing | ○ | ○ | — | ○ | — | ● | — | ○ |
| Social proof | ● | ○ | ○ | ○ | ● | ○ | — | ● |
| Sticky CTA | ● | — | — | ○ | — | ○ | — | — |
| App/dashboard | — | — | — | — | ○ | ● | ● | ● |

● Required · ○ Recommended/Optional · — Excluded/N/A

---

## SAFE UNKNOWN

- Canonical Block Registry v1 with `block_id` alignment to this mapping — **not yet created**; v0 block registry uses different `site_type_id` names.
- Machine validation of block ↔ site type compatibility — **future**.

---

*Block mapping version: v1.*
