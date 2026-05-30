# Website Factory — CATALOG Blueprint v1

**Blueprint ID:** `CATALOG-BLUEPRINT-v1`  
**site_type_code:** `CATALOG`  
**site_type_group:** CORE  
**Контракт:** [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md)

---

## business_goal

**Primary:** Discovery и сравнение товаров/услуг; переход к RFQ, контакту, дилеру или офлайн-покупке — **без транзакции on-domain**.

**Direction:** Category structure · product/service pages · filtering · **NO cart · NO checkout · NO online payment** (mandatory exclusions).

---

## typical_traffic_sources

| Источник | Приоритет |
|----------|-----------|
| Organic (categories, long-tail PDP) | **Primary** |
| Contextual ads to PLP/PDP | Medium |
| Direct to brand SKU | Medium |
| PPC | Medium |

---

## page_structure

**Model:** Category tree + PLP + PDP (no commerce checkout path).

```
/                                    ← home / catalog entry
/catalog/ or /{category}/            ← category tree root
/{category}/{subcategory}/          ← PLP
/{category}/…/{product-slug}/        ← PDP
/search/                             ← optional site search results
/contacts/                           ← support / dealer contact
/faq/                                ← optional
/privacy-policy/ …                   ← legal L1–L4
```

**Typical page count:** 20–500+ URL (scales with assortment).

---

## required_pages

| Page role | URL pattern | Notes |
|-----------|-------------|-------|
| **Home / catalog entry** | `/` | Entry to category tree |
| **Category (PLP)** | `/{category}/` … | Grid + filters |
| **Product / service (PDP)** | `…/{product-slug}/` | Specs, gallery, RFQ CTA |
| **Contacts** | `/contacts/` | Support, dealer inquiries |
| **Legal L1–L4** | Standard legal URLs | Production |

**Recommended:**

| Page role | URL pattern |
|-----------|-------------|
| FAQ | `/faq/` |
| Search results | `/search/` |
| Comparison (utility) | `/compare/` (optional) |

---

## required_blocks

| Context | Required blocks |
|---------|-----------------|
| **Global** | Header/nav · Breadcrumbs · Legal footer |
| **PLP (category)** | Category intro (SEO) · Filters · Product/service cards · Pagination |
| **PDP** | Gallery · Specs / spec table · Primary CTA (RFQ / call / dealer) · Related items |
| **Support** | Contact block · FAQ (recommended) |

**Conversion blocks on PDP:** RFQ form · «Request price» · «Find dealer» · click-to-call — **not** add-to-cart.

---

## optional_blocks

| Block role | When |
|------------|------|
| Comparison table | Spec-heavy categories |
| Spec accordion | Long specifications |
| Downloads | PDFs, datasheets |
| Dealer / locator | Distribution model |
| Brand strip | Multi-brand catalog |
| Category intro SEO copy | PLP head content |

---

## conversion_requirements

| Requirement | Rule |
|-------------|------|
| **Primary conversion** | RFQ · request price · find dealer · click-to-call |
| **No cart path** | Add-to-cart **forbidden** |
| **Forms** | RFQ / dealer inquiry — Consent Rule |
| **PDP CTA** | Contact-led, not purchase-led |

**Matrix alignment:** Catalog **critical**; cart/payment **—** (absent).

---

## legal_requirements

**Source:** [SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) — CATALOG

| Requirement | Detail |
|-------------|--------|
| **Required documents** | L1, L2, L3, L4 — full site + production |
| **Footer links** | Все 4 — production |
| **Consent Rule** | RFQ, price request, dealer inquiry forms |
| **ECOMMERCE Extension** | **Not required** — no checkout |
| **Future expansion** | — |

---

## seo_requirements

**Source:** [SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — CATALOG

| Requirement | Detail |
|-------------|--------|
| **SEO priority** | **HIGH** |
| **Architecture** | Category tree + PDP long-tail |
| **Facets** | Controlled indexation policy; no infinite thin facet URLs |
| **Canonical** | Rules for filter combinations |
| **Pagination** | rel prev/next on PLP |
| **Schema** | `Product` / `ItemList` where honest |
| **Sitemap** | Segmented (categories, products) |
| **Crawl budget** | Monitor via Search Console |

**FUTURE:** dedicated faceted SEO addendum — not v1 Blueprint execution.

---

## exclusions

**Mandatory — non-negotiable for CATALOG v1:**

| Excluded | Rule |
|----------|------|
| **Cart** | **FORBIDDEN** — reclassify → `ECOMMERCE` |
| **Checkout** | **FORBIDDEN** — reclassify → `ECOMMERCE` |
| **Online payment** | **FORBIDDEN** — reclassify → `ECOMMERCE` |
| Payment summary blocks | **FORBIDDEN** |
| Order history / buyer account | **FORBIDDEN** |
| Subscriptions | Reclassify → `SAAS` |
| Multi-vendor seller stores | Reclassify → `MARKETPLACE` |
| Single-page PPC landing as primary | Reclassify → `LANDING` |

**Operator rule:** появление cart/checkout на production → **halt** + reclassify to `ECOMMERCE`.

---

*Catalog Blueprint version: v1.*
