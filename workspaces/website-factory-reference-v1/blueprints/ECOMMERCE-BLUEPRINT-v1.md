# Website Factory — ECOMMERCE Blueprint v1

**Blueprint ID:** `ECOMMERCE-BLUEPRINT-v1`  
**site_type_code:** `ECOMMERCE`  
**site_type_group:** CORE  
**Контракт:** [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md)

---

## business_goal

**Primary:** Завершение покупки on-domain — полный цикл онлайн-продаж.

**Direction:** Catalog + product cards + **cart** + **checkout** + **payment** + order confirmation flow.

---

## typical_traffic_sources

| Источник | Приоритет |
|----------|-----------|
| Organic (transactional queries) | **High** |
| Performance marketing | High |
| Email (abandoned cart, promos) | Medium |
| Direct / brand | Medium |
| Marketplace overflow | Context-dependent |

---

## page_structure

**Model:** Catalog subtree + commerce transaction path.

```
/                                    ← shop home
/catalog/ …                          ← categories (PLP)
/…/{product-slug}/                   ← PDP
/cart/                               ← cart
/checkout/                           ← checkout flow
/order-confirmation/                 ← post-purchase
/account/ …                          ← buyer account (optional)
/delivery/ · /returns/               ← policy pages (recommended)
/privacy-policy/ …                   ← legal L1–L4
```

**Typical page count:** 50–10 000+ URL.

**Order flow:**

```
PLP → PDP → Add to cart → Cart → Checkout → Payment → Order confirmation
```

---

## required_pages

| Page role | URL pattern | Notes |
|-----------|-------------|-------|
| **Shop home** | `/` | Entry, promos |
| **Category PLP** | `/{category}/` … | Filters, grid |
| **Product PDP** | `…/{product-slug}/` | Price, variants, ATC |
| **Cart** | `/cart/` | Line items, proceed to checkout |
| **Checkout** | `/checkout/` | Guest or account path |
| **Order confirmation** | `/order-confirmation/` | Post-payment |
| **Legal L1–L4** | Standard URLs | Production + checkout |

**Recommended:**

| Page role | URL pattern |
|-----------|-------------|
| Returns policy | `/returns/` |
| Delivery / shipping | `/delivery/` |
| Account login/register | `/account/` |
| Order status | `/account/orders/` |

---

## required_blocks

| Context | Required blocks |
|---------|-----------------|
| **Global** | Header/nav · Breadcrumbs · Legal footer |
| **PLP** | Filters · Product cards · Promo banner (optional) |
| **PDP** | Gallery · Price · Variants · **Add-to-cart** · Trust badges |
| **Cart** | Line items · Quantity · Proceed CTA · Trust |
| **Checkout** | Progress indicator · Delivery · **Payment** · Consent on PD forms |
| **Post-purchase** | Order summary · Confirmation |

**Recommended:** Reviews · Recommendations · Sticky add-to-cart (mobile) · Returns/shipping info blocks

---

## optional_blocks

| Block role | When |
|------------|------|
| Account / login | Repeat buyers |
| Wishlist | Fashion, gifts |
| Cross-sell / upsell | AOV optimization |
| Size / fit guide | Apparel |
| FAQ | Support reduction |

---

## conversion_requirements

| Requirement | Rule |
|-------------|------|
| **Primary conversion** | Completed purchase on-domain |
| **Funnel** | PLP → PDP → cart → checkout → payment confirmation |
| **Checkout modes** | Guest and/or account |
| **Secondary** | Newsletter opt-in (with Consent if PD) |
| **Abandoned cart** | Email retargeting — **integration**, not Blueprint content |

**Matrix alignment:** Catalog, cart, payment — all **critical**.

---

## legal_requirements

**Source:** [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) — ECOMMERCE

| Requirement | Detail |
|-------------|--------|
| **Core documents** | L1, L2, L3, L4 — full site + production + checkout |
| **Footer links** | Все 4 — production |
| **Consent Rule** | Checkout guest forms, account registration, marketing opt-in with ПДн |
| **Future legal expansion** | **ECOMMERCE EXTENSION (dependency):** E1 Public Offer, E2 Payment Rules, E3 Delivery Rules, E4 Return Policy |

**Critical note:** L3 (User Agreement) **≠** public offer. Ecommerce production **may require** Extension beyond Core Pack v1 — **HITL / legal review** before go-live.

**Legal Pack v1 FROZEN** covers Core L1–L4 only; Extension templates **not in Core v1**.

---

## seo_requirements

**Source:** [SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — ECOMMERCE

| Requirement | Detail |
|-------------|--------|
| **SEO priority** | **HIGH** |
| **Catalog SEO** | As CATALOG (categories, PDP long-tail) |
| **Transactional intent** | Honest price/stock on PDP when applicable |
| **Schema** | `Product` with offer (price/stock when truthful); reviews if authentic |
| **Noindex** | Cart, checkout, account typically **noindex** |
| **Performance** | CWV critical on PLP/PDP |
| **Variants** | Duplicate PDP control |

---

## exclusions

| Excluded | Consequence if added |
|----------|---------------------|
| Multi-vendor seller onboarding | Reclassify → `MARKETPLACE` |
| Seller storefronts per vendor | Reclassify → `MARKETPLACE` |
| B2B operational ERP UI as primary | Reclassify → `WEB_APPLICATION` |
| RFQ-only catalog without cart | Reclassify → `CATALOG` |
| Subscription billing as primary | Reclassify → `SAAS` (+ legal extension) |

---

## Future dependencies

| Dependency | Status |
|------------|--------|
| ECOMMERCE Legal Extension (E1–E4) | **FUTURE** — charter + legal sign-off |
| Payment gateway integration spec | **SAFE UNKNOWN** — project charter |
| Shipping provider integration | **SAFE UNKNOWN** — project charter |
| Inventory / OMS sync | **SAFE UNKNOWN** — outside Blueprint v1 |

---

*Ecommerce Blueprint version: v1.*
