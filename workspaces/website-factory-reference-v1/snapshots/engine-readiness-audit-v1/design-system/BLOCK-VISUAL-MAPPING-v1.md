# Website Factory — Block Visual Mapping v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** authoritative `block_id` → visual pattern family map — **architecture only**  
**Связь:** [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md), [VISUAL-PATTERN-REGISTRY-v1.md](VISUAL-PATTERN-REGISTRY-v1.md), [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md)

**Не является:** component map, partial filename registry, CSS module map.

**Rule:** Pattern binding **valid only** when block stance is not FORBIDDEN for target page/blueprint.

---

## Mapping legend

| Column | Meaning |
|--------|---------|
| **Primary families** | Default architectural patterns for block |
| **Secondary families** | Allowed alternatives when IA requires |
| **Discouraged** | Permitted only with operator note — prefer primary |
| **N/A** | Block not in registry |

---

## Core block → pattern map (29 blocks)

| block_id | Primary pattern families | Secondary families | Discouraged |
|----------|-------------------------|-------------------|-------------|
| **HERO** | VF_HERO_VALUE_PROPOSITION, VF_HERO_OFFER_LED, VF_HERO_CATALOG_GATEWAY | — | Mixing two hero families on one page |
| **BENEFITS** | VF_BENEFITS_OUTCOME_GRID | VF_BENEFITS_COMPARISON_STRIP | VF_FEATURES_CAPABILITY_GRID as benefits substitute |
| **FEATURES** | VF_FEATURES_CAPABILITY_GRID, VF_FEATURES_SPEC_HIGHLIGHT | VF_COMPARISON_TABLE | VF_BENEFITS_* on spec-heavy PDP |
| **SERVICES** | VF_SERVICES_OVERVIEW_GRID, VF_SERVICES_DETAIL_STACK | — | VF_CATALOG_* families |
| **CATEGORIES** | VF_CATALOG_CATEGORY_HUB | — | Hero-led catalog without grid |
| **CATEGORY_GRID** | VF_CATALOG_FILTERED_GRID, VF_CATALOG_CATEGORY_HUB | VF_PRODUCT_CARD_GRID | VF_BENEFITS_OUTCOME_GRID |
| **PRODUCT_GRID** | VF_PRODUCT_CARD_GRID | VF_CATALOG_FILTERED_GRID | VF_HERO_OFFER_LED as grid header |
| **PRODUCT_CARD** | VF_PRODUCT_PDP_FOCUS, VF_PRODUCT_CARD_GRID | VF_GALLERY_MEDIA_GRID | VF_LEAD_FORM_DEDICATED_PANEL as PDP primary (ECOMMERCE) |
| **PRICING** | VF_PRICING_TIER_TABLE, VF_PRICING_SINGLE_OFFER | VF_COMPARISON_TIER_MATRIX | VF_COMPARISON_TABLE without pricing context |
| **PROCESS** | VF_PROCESS_STEP_TIMELINE | VF_PROCESS_PHASE_CARDS | VF_CATALOG_* on LANDING-only pages |
| **CASES** | VF_CASES_PROOF_GRID | VF_TRUST_SOCIAL_PROOF_BAND | VF_REVIEWS_AGGREGATE duplication |
| **TESTIMONIALS** | VF_REVIEWS_FEATURED_QUOTES, VF_TRUST_SOCIAL_PROOF_BAND | — | VF_REVIEWS_AGGREGATE on non-hub pages |
| **REVIEWS** | VF_REVIEWS_AGGREGATE, VF_REVIEWS_FEATURED_QUOTES | — | On LANDING (block FORBIDDEN) |
| **TRUST** | VF_TRUST_SOCIAL_PROOF_BAND, VF_TRUST_LOGO_STRIP | VF_CERTIFICATES_BADGE_ROW | VF_PARTNERS_LOGO_WALL only when partners block absent |
| **CERTIFICATES** | VF_CERTIFICATES_BADGE_ROW | VF_TRUST_SOCIAL_PROOF_BAND | Standalone without trust context |
| **TEAM** | VF_TEAM_GRID, VF_TEAM_LEADERSHIP_FOCUS | — | On LANDING (TEAM FORBIDDEN) |
| **ABOUT** | VF_ABOUT_NARRATIVE | VF_TEAM_GRID (linked) | VF_HERO_OFFER_LED on ABOUT_PAGE |
| **FAQ** | VF_FAQ_INLINE_OBJECTIONS, VF_FAQ_ACCORDION | — | VF_LEGAL_DOCUMENT_BODY |
| **CTA** | VF_CTA_PRIMARY_BAND, VF_CTA_STICKY_MOBILE | — | Multiple primary-band families competing |
| **LEAD_FORM** | VF_LEAD_FORM_DEDICATED_PANEL, VF_LEAD_FORM_INLINE | — | On LEGAL_PAGE; ECOMMERCE PDP primary |
| **CONTACTS** | VF_CONTACT_NAP_HUB, VF_CONTACT_SPLIT_FORM_MAP | VF_LEAD_FORM_INLINE | VF_HERO_VALUE_PROPOSITION as contact substitute |
| **MAP** | VF_MAP_EMBED | VF_CONTACT_SPLIT_FORM_MAP | Standalone without CONTACTS on CONTACT_PAGE |
| **PARTNERS** | VF_PARTNERS_LOGO_WALL, VF_TRUST_LOGO_STRIP | — | VF_REVIEWS_AGGREGATE |
| **DELIVERY** | VF_DELIVERY_INFO_PANEL | — | On LANDING (block FORBIDDEN) |
| **PAYMENT** | VF_PAYMENT_METHODS_STRIP | VF_CHECKOUT_FLOW_STEPS | Marketing CTA bands in checkout |
| **CHECKOUT** | VF_CHECKOUT_FLOW_STEPS | — | VF_CTA_STICKY_MOBILE site-wide on checkout |
| **CART** | VF_CART_LINE_ITEMS | — | VF_PRODUCT_PDP_FOCUS |
| **LEGAL_LINKS** | VF_FOOTER_SITE_CHROME | — | VF_LEGAL_DOCUMENT_BODY on non-legal routes |
| **FOOTER** | VF_FOOTER_SITE_CHROME | — | VF_HERO_* |

---

## Quick reference (block → family name)

| block_id | Pattern family names (operator shorthand) |
|----------|-------------------------------------------|
| HERO | Hero |
| BENEFITS | Benefits |
| FEATURES | Features, Comparison |
| SERVICES | Services |
| CATEGORIES, CATEGORY_GRID | Catalog |
| PRODUCT_GRID, PRODUCT_CARD | Product, Catalog, Gallery (PDP) |
| PRICING | Pricing, Comparison |
| PROCESS | Process |
| CASES | Cases, Trust |
| TESTIMONIALS, REVIEWS, TRUST, CERTIFICATES | Trust, Reviews |
| TEAM | Team |
| ABOUT | About, Team |
| FAQ | FAQ |
| CTA | CTA |
| LEAD_FORM | Lead Form |
| CONTACTS, MAP | Contact, Map |
| PARTNERS | Partners, Trust |
| DELIVERY, PAYMENT, CHECKOUT, CART | Delivery, Payment, Checkout, Cart |
| LEGAL_LINKS, FOOTER | Footer / Legal chrome |
| (LEGAL_PAGE body) | Legal document (no block_id) |

---

## Cross-layer gates

| Gate | Rule |
|------|------|
| Blueprint FORBIDDEN | No pattern binding for that block site-wide |
| Page FORBIDDEN | No pattern binding on that route |
| SEO page role | e.g. FAQ_PAGE hub → prefer VF_FAQ_ACCORDION over inline |
| Design site profile | See SITE-TYPE-DESIGN-MAPPING-v1 discouraged/forbidden families |

---

## SAFE UNKNOWN

- `sticky_cta.html` partial — implementation variant of canonical `CTA`; embedded video — media within content, not a `block_id` (see [BLOCK-REGISTRY-GAPS-v1.md](../block-registry/BLOCK-REGISTRY-GAPS-v1.md)).

---

*Block Visual Mapping version: v1.*
