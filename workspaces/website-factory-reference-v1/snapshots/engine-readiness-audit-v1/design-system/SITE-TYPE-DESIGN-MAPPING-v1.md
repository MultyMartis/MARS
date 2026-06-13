# Website Factory — Site Type Design Mapping v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** Core 5 design profiles — **documentation only**  
**Scope:** `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

**Связь:** [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md), [blueprints/](../blueprints/), [SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md)

**Не является:** brand guidelines, theme tokens, wireframes.

**Extended types:** SAAS, WEB_APPLICATION, MARKETPLACE — **not expanded** (see [DESIGN-SYSTEM-GAPS-v1.md](DESIGN-SYSTEM-GAPS-v1.md)).

---

## Легенда

| Term | Meaning |
|------|---------|
| **Preferred families** | Default pattern families for typical production |
| **Discouraged families** | Avoid unless documented operator exception |
| **Forbidden families** | Must not be primary design architecture for type |
| **Design priorities** | Ordered architectural goals (no visual styling) |

Family shorthand = pattern families in [VISUAL-PATTERN-REGISTRY-v1.md](VISUAL-PATTERN-REGISTRY-v1.md) (`VF_*` groups: Hero, Benefits, Catalog, Product, CTA, Lead Form, Trust, FAQ, Process, Pricing, Comparison, Contact, Checkout/Cart, Legal, Footer).

---

## LANDING

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **preferred_pattern_families** | Hero (value/offer led) · Benefits · Process · Trust · FAQ (inline) · Pricing (optional) · Lead Form · CTA · Contact · Footer |
| **discouraged_pattern_families** | Catalog · Product PDP focus · Reviews aggregate hub · Comparison table · Checkout/Cart · Services grid · Team |
| **forbidden_pattern_families** | Catalog hub/grid as primary IA · Product card grid · Checkout flow · Reviews hub as primary surface · Hero catalog gateway |
| **design_priorities** | 1) Single linear narrative 2) One primary action path 3) Message match for campaign 4) Proof before form 5) Minimal navigation chrome |

**Alignment:** SEO MINIMAL depth; `LANDING_PAGE` only primary conversion surface.

---

## PROMO

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **preferred_pattern_families** | Hero (value proposition) · Services · Trust · Testimonials/Reviews · FAQ (accordion on hub) · CTA · Lead Form · Contact · About/Team · Cases · Footer |
| **discouraged_pattern_families** | Hero offer-led on every route · Catalog filtered grid as home · Checkout · Comparison tier matrix without service context · Sticky mobile CTA site-wide |
| **forbidden_pattern_families** | Catalog category hub as site primary · Product PDP focus as home · Checkout/cart as marketing pages · LANDING-only linear stack as sole site IA |
| **design_priorities** | 1) Money page clarity (SERVICE_PAGE) 2) Trust supporting rankings 3) NAP consistency 4) Scannable service grid 5) Secondary hubs (FAQ/Reviews) without competing primary CTA |

**Alignment:** SEO STANDARD; multi-page organic architecture.

---

## CATALOG

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **preferred_pattern_families** | Hero (catalog gateway) · Catalog hub/grid · Product card/grid · Product PDP focus · Gallery · Trust · FAQ · Contact · Lead Form (RFQ) · Footer |
| **discouraged_pattern_families** | Benefits outcome grid as PLP primary · Process timeline · Pricing tier table (blueprint FORBIDDEN) · Lead form as PDP primary conversion · Hero offer-led campaign |
| **forbidden_pattern_families** | Benefits as required site-wide stack · Checkout/cart · Payment/checkout patterns · LANDING linear-only narrative · Services overview as primary IA |
| **design_priorities** | 1) Browse → PDP clarity 2) RFQ/contact conversion on PDP 3) Category tree discoverability 4) Spec/media richness on PDP 5) Trust without campaign noise |

**Alignment:** SEO DEEP catalog; no transactional checkout design.

---

## ECOMMERCE

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **preferred_pattern_families** | Hero (catalog gateway) · Catalog · Product PDP · Gallery · Trust · FAQ · Delivery · Payment · Cart · Checkout · CTA (contextual) · Contact · Footer |
| **discouraged_pattern_families** | Lead form dedicated panel as PDP primary · Benefits grid · Process timeline · Services grid · Hero value-only without assortment cue |
| **forbidden_pattern_families** | LANDING linear stack · Services money page as primary · RFQ-only PDP when type is ECOMMERCE · Marketing hero on checkout utility · SEO-targeted checkout embellishment |
| **design_priorities** | 1) PLP/PDP commercial clarity 2) Transaction path legibility 3) Utility funnel simplicity (cart/checkout) 4) Trust on PDP 5) Policy/delivery transparency |

**Alignment:** SEO DEEP on catalog; checkout **utility** not marketing design target.

---

## CORPORATE

| Dimension | Value |
|-----------|-------|
| **site_type_group** | CORE |
| **preferred_pattern_families** | Hero (value) · Services · About/Team · Trust · Cases · Partners · Features · FAQ · Contact · Catalog (optional subtree) · CTA (soft) · Footer |
| **discouraged_pattern_families** | Hero offer-led everywhere · Aggressive sticky CTA · Pricing tier table without B2B charter · Product grid as home without catalog intent |
| **forbidden_pattern_families** | LANDING-only single-page IA · Checkout-first architecture without ECOMMERCE reclassification · Campaign landing as only indexed surface |
| **design_priorities** | 1) Brand + credibility 2) Service/solution clarity 3) Optional catalog subtree consistency 4) Trust and compliance signals 5) Measured conversion (not aggressive promo) |

**Alignment:** SEO SELECTIVE/STANDARD; trust pages support money pages.

---

## Summary matrix

| site_type | Preferred (shorthand) | Forbidden (shorthand) |
|-----------|----------------------|------------------------|
| LANDING | Hero, Benefits, Process, Trust, FAQ inline, Lead Form, CTA | Catalog, Product grid, Checkout, Reviews hub |
| PROMO | Hero, Services, Trust, FAQ, Contact, About/Team | Catalog-primary, Checkout |
| CATALOG | Catalog, Product, Gallery, Trust, Contact, RFQ Lead Form | Benefits-required, Checkout |
| ECOMMERCE | Catalog, Product, Cart, Checkout, Delivery, Payment | LANDING stack, Services-primary |
| CORPORATE | Hero, Services, About, Trust, Cases, Contact | LANDING-only, Checkout-primary |

---

## SAFE UNKNOWN

- Design profile depth for Extended types — **FUTURE**.

---

*Site Type Design Mapping version: v1.*
