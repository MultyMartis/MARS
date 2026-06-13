# Website Factory — Visual Pattern Registry v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** initial pattern families — **architecture only**  
**Связь:** [VISUAL-PATTERN-CONTRACT-v1.md](VISUAL-PATTERN-CONTRACT-v1.md), [BLOCK-VISUAL-MAPPING-v1.md](BLOCK-VISUAL-MAPPING-v1.md)

**Не является:** pattern library UI, Figma kit, illustration brief, motion spec.

**Scope:** Core 5 `site_type_code` unless noted. All entries conform to [VISUAL-PATTERN-CONTRACT-v1.md](VISUAL-PATTERN-CONTRACT-v1.md).

---

## Registry index (families)

| pattern_id | pattern_name | Primary blocks |
|------------|--------------|----------------|
| VF_HERO_VALUE_PROPOSITION | Hero — value proposition | HERO |
| VF_HERO_OFFER_LED | Hero — offer / campaign led | HERO |
| VF_HERO_CATALOG_GATEWAY | Hero — catalog / shop gateway | HERO |
| VF_BENEFITS_OUTCOME_GRID | Benefits — outcome grid | BENEFITS |
| VF_BENEFITS_COMPARISON_STRIP | Benefits — comparison strip | BENEFITS |
| VF_FEATURES_CAPABILITY_GRID | Features — capability grid | FEATURES |
| VF_FEATURES_SPEC_HIGHLIGHT | Features — spec highlight | FEATURES |
| VF_SERVICES_OVERVIEW_GRID | Services — overview grid | SERVICES |
| VF_SERVICES_DETAIL_STACK | Services — detail stack | SERVICES |
| VF_TRUST_SOCIAL_PROOF_BAND | Trust — social proof band | TRUST, TESTIMONIALS |
| VF_TRUST_LOGO_STRIP | Trust — logo strip | TRUST, PARTNERS |
| VF_REVIEWS_AGGREGATE | Reviews — aggregate feed | REVIEWS |
| VF_REVIEWS_FEATURED_QUOTES | Reviews — featured quotes | TESTIMONIALS, REVIEWS |
| VF_FAQ_ACCORDION | FAQ — accordion hub | FAQ |
| VF_FAQ_INLINE_OBJECTIONS | FAQ — inline objections | FAQ |
| VF_CTA_PRIMARY_BAND | CTA — primary action band | CTA |
| VF_CTA_STICKY_MOBILE | CTA — sticky mobile reinforcement | CTA |
| VF_CONTACT_NAP_HUB | Contact — NAP hub | CONTACTS |
| VF_CONTACT_SPLIT_FORM_MAP | Contact — form + map split | CONTACTS, MAP |
| VF_GALLERY_MEDIA_GRID | Gallery — media grid | (PRODUCT_PAGE context) |
| VF_GALLERY_FEATURED_STRIP | Gallery — featured strip | (PRODUCT_PAGE context) |
| VF_PROCESS_STEP_TIMELINE | Process — step timeline | PROCESS |
| VF_PROCESS_PHASE_CARDS | Process — phase cards | PROCESS |
| VF_TEAM_GRID | Team — role grid | TEAM |
| VF_TEAM_LEADERSHIP_FOCUS | Team — leadership focus | TEAM |
| VF_CATALOG_CATEGORY_HUB | Catalog — category hub | CATEGORIES, CATEGORY_GRID |
| VF_CATALOG_FILTERED_GRID | Catalog — filtered product grid | CATEGORY_GRID, PRODUCT_GRID |
| VF_PRODUCT_CARD_GRID | Product — card grid | PRODUCT_CARD, PRODUCT_GRID |
| VF_PRODUCT_PDP_FOCUS | Product — PDP focus layout | PRODUCT_CARD (PDP) |
| VF_COMPARISON_TABLE | Comparison — attribute table | FEATURES, PRICING |
| VF_COMPARISON_TIER_MATRIX | Comparison — tier matrix | PRICING |
| VF_PRICING_TIER_TABLE | Pricing — tier table | PRICING |
| VF_PRICING_SINGLE_OFFER | Pricing — single offer | PRICING |
| VF_LEAD_FORM_INLINE | Lead form — inline capture | LEAD_FORM |
| VF_LEAD_FORM_DEDICATED_PANEL | Lead form — dedicated panel | LEAD_FORM |
| VF_CASES_PROOF_GRID | Cases — proof grid | CASES |
| VF_CERTIFICATES_BADGE_ROW | Certificates — badge row | CERTIFICATES |
| VF_ABOUT_NARRATIVE | About — narrative arc | ABOUT |
| VF_PARTNERS_LOGO_WALL | Partners — logo wall | PARTNERS |
| VF_DELIVERY_INFO_PANEL | Delivery — info panel | DELIVERY |
| VF_PAYMENT_METHODS_STRIP | Payment — methods strip | PAYMENT |
| VF_CHECKOUT_FLOW_STEPS | Checkout — flow steps | CHECKOUT |
| VF_CART_LINE_ITEMS | Cart — line items | CART |
| VF_LEGAL_DOCUMENT_BODY | Legal — document body | (LEGAL_PAGE — no marketing block) |
| VF_FOOTER_SITE_CHROME | Footer — site chrome | FOOTER, LEGAL_LINKS |
| VF_MAP_EMBED | Map — location embed | MAP |

**Note:** `VF_GALLERY_*` binds to PRODUCT_PAGE / PDP block stacks (`FEATURES` media role architecturally on PDP) — not a separate `block_id` in v1 registry.

---

## Family entries (contract fields)

### Hero family

#### VF_HERO_VALUE_PROPOSITION

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CORPORATE |
| **supported_page_types** | LANDING_PAGE, HOME_PAGE, SERVICE_PAGE, ABOUT_PAGE |
| **supported_blocks** | HERO |
| **purpose** | Establish audience, outcome, and primary orientation above the fold without secondary funnels. |
| **strengths** | Clear single story; supports PPC message match; low navigation noise. |
| **weaknesses** | Weak for deep catalog entry; may under-serve multi-category shops. |
| **recommended_use** | LANDING primary page; PROMO/CORPORATE home when brand + service orientation dominates. |
| **forbidden_use** | LEGAL_PAGE; checkout/cart routes; block FORBIDDEN stances. |

#### VF_HERO_OFFER_LED

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO |
| **supported_page_types** | LANDING_PAGE, HOME_PAGE |
| **supported_blocks** | HERO |
| **purpose** | Lead with time-bound or package offer; reinforce campaign CTA hierarchy. |
| **strengths** | Aligns with promo/campaign traffic; supports single conversion path. |
| **weaknesses** | Can erode trust on corporate/about contexts if overused. |
| **recommended_use** | Campaign landings; seasonal PROMO home. |
| **forbidden_use** | CATALOG/ECOMMERCE category-first IA; LEGAL_PAGE. |

#### VF_HERO_CATALOG_GATEWAY

| Field | Value |
|-------|-------|
| **supported_site_types** | CATALOG, ECOMMERCE, CORPORATE |
| **supported_page_types** | HOME_PAGE, CATEGORY_PAGE |
| **supported_blocks** | HERO |
| **purpose** | Orient user toward category tree or featured assortment, not single service narrative. |
| **strengths** | Supports browse intent; bridges to PLP/grid patterns. |
| **weaknesses** | Dilutes single-offer LANDING conversion focus. |
| **recommended_use** | Shop/catalog home; top-level category intros. |
| **forbidden_use** | LANDING site type primary page; LEGAL_PAGE. |

---

### Benefits family

#### VF_BENEFITS_OUTCOME_GRID

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CORPORATE |
| **supported_page_types** | LANDING_PAGE, SERVICE_PAGE, HOME_PAGE |
| **supported_blocks** | BENEFITS |
| **purpose** | Enumerate customer outcomes and differentiators in scannable units. |
| **strengths** | Supports objection preemption before proof/CTA. |
| **weaknesses** | Redundant if FEATURES already dense on same page. |
| **recommended_use** | LANDING required stack; service money pages. |
| **forbidden_use** | CATALOG/ECOMMERCE where BENEFITS block FORBIDDEN at blueprint level. |

#### VF_BENEFITS_COMPARISON_STRIP

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO |
| **supported_page_types** | LANDING_PAGE |
| **supported_blocks** | BENEFITS |
| **purpose** | Contrast «us vs status quo» in horizontal narrative units. |
| **strengths** | Sharp positioning for commercial intent pages. |
| **weaknesses** | Can conflict with PRICING comparison if both compete for attention. |
| **recommended_use** | High-consideration offers before PRICING block. |
| **forbidden_use** | PDP/PLP primary content zones. |

---

### Trust / Reviews family

#### VF_TRUST_SOCIAL_PROOF_BAND

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **supported_page_types** | LANDING_PAGE, HOME_PAGE, SERVICE_PAGE, PRODUCT_PAGE |
| **supported_blocks** | TRUST, TESTIMONIALS |
| **purpose** | Aggregate credibility signals (metrics, quotes, badges) in one band. |
| **strengths** | Flexible across site types; supports conversion before form. |
| **weaknesses** | Generic if not tied to specific claims (HITL for regulated claims). |
| **recommended_use** | Post-hero or pre-CTA on conversion pages. |
| **forbidden_use** | LEGAL_PAGE body. |

#### VF_REVIEWS_AGGREGATE

| Field | Value |
|-------|-------|
| **supported_site_types** | PROMO, CORPORATE, CATALOG, ECOMMERCE |
| **supported_page_types** | REVIEWS_PAGE, HOME_PAGE |
| **supported_blocks** | REVIEWS |
| **purpose** | Present volume of third-party or platform reviews as hub content. |
| **strengths** | Supports REVIEWS_PAGE design role; SEO trust alignment. |
| **weaknesses** | Heavy duplication if TESTIMONIALS already on same route. |
| **recommended_use** | Dedicated reviews hub; optional catalog trust. |
| **forbidden_use** | LANDING blueprint (REVIEWS block FORBIDDEN). |

---

### FAQ family

#### VF_FAQ_ACCORDION

| Field | Value |
|-------|-------|
| **supported_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **supported_page_types** | FAQ_PAGE, HOME_PAGE, SERVICE_PAGE |
| **supported_blocks** | FAQ |
| **purpose** | Centralize many Q&A pairs with progressive disclosure. |
| **strengths** | Scales on FAQ_PAGE; reduces scroll fatigue. |
| **weaknesses** | Poor primary pattern for single-offer LANDING (prefer inline). |
| **recommended_use** | FAQ_PAGE required; support hubs. |
| **forbidden_use** | Fake FAQ for SEO only — content policy (SEO layer). |

#### VF_FAQ_INLINE_OBJECTIONS

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO |
| **supported_page_types** | LANDING_PAGE, SERVICE_PAGE |
| **supported_blocks** | FAQ |
| **purpose** | Handle objections inline in linear landing narrative. |
| **strengths** | Matches LANDING linear IA; supports PPC landing scan. |
| **weaknesses** | Does not scale to large support corpora alone. |
| **recommended_use** | LANDING required FAQ block. |
| **forbidden_use** | Replacing LEGAL_PAGE content. |

---

### CTA / Lead Form family

#### VF_CTA_PRIMARY_BAND

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, ECOMMERCE, CORPORATE |
| **supported_page_types** | LANDING_PAGE, SERVICE_PAGE, HOME_PAGE, PRODUCT_PAGE |
| **supported_blocks** | CTA |
| **purpose** | Repeat primary action in dedicated band between content sections. |
| **strengths** | Reinforces Blueprint single primary action. |
| **weaknesses** | Multiple bands → action ambiguity. |
| **recommended_use** | After proof or pricing sections. |
| **forbidden_use** | LEGAL_PAGE; PROMO site-wide sticky (LANDING-only pattern per block rules). |

#### VF_LEAD_FORM_DEDICATED_PANEL

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CATALOG, CORPORATE |
| **supported_page_types** | LANDING_PAGE, SERVICE_PAGE, CONTACT_PAGE |
| **supported_blocks** | LEAD_FORM |
| **purpose** | Isolate lead capture with consent and field grouping as focal panel. |
| **strengths** | Clear PII boundary; aligns with Legal consent rules. |
| **weaknesses** | Friction if placed before value proof on cold traffic. |
| **recommended_use** | LANDING required; RFQ catalog flows. |
| **forbidden_use** | ECOMMERCE primary PDP when LEAD_FORM forbidden; LEGAL_PAGE. |

---

### Catalog / Product family

#### VF_CATALOG_CATEGORY_HUB

| Field | Value |
|-------|-------|
| **supported_site_types** | CATALOG, ECOMMERCE, CORPORATE |
| **supported_page_types** | HOME_PAGE, CATEGORY_PAGE |
| **supported_blocks** | CATEGORIES, CATEGORY_GRID |
| **purpose** | Expose category tree and entry points to assortment. |
| **strengths** | Matches PLP/organic browse intent. |
| **weaknesses** | Wrong primary pattern for service-only PROMO. |
| **recommended_use** | Catalog home and category roots. |
| **forbidden_use** | LANDING, PROMO without catalog reclassification. |

#### VF_PRODUCT_PDP_FOCUS

| Field | Value |
|-------|-------|
| **supported_site_types** | CATALOG, ECOMMERCE |
| **supported_page_types** | PRODUCT_PAGE |
| **supported_blocks** | PRODUCT_CARD, FEATURES |
| **purpose** | Prioritize product identity, specs, gallery, and conversion action on PDP. |
| **strengths** | Supports rich PDP SEO/content depth. |
| **weaknesses** | Requires disciplined media/spec content — not a layout shortcut. |
| **recommended_use** | All PRODUCT_PAGE instances. |
| **forbidden_use** | SERVICE_PAGE; LEGAL_PAGE. |

---

### Pricing / Comparison family

#### VF_PRICING_TIER_TABLE

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, ECOMMERCE, CORPORATE |
| **supported_page_types** | LANDING_PAGE, SERVICE_PAGE, HOME_PAGE |
| **supported_blocks** | PRICING |
| **purpose** | Present tiered offers with comparative attributes. |
| **strengths** | Clarifies package selection; supports commercial intent. |
| **weaknesses** | Regulated pricing claims need HITL. |
| **recommended_use** | Tiered SaaS-like offers on PROMO/CORPORATE. |
| **forbidden_use** | CATALOG blueprint (PRICING FORBIDDEN at blueprint). |

#### VF_COMPARISON_TABLE

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CORPORATE |
| **supported_page_types** | LANDING_PAGE, SERVICE_PAGE |
| **supported_blocks** | FEATURES, PRICING |
| **purpose** | Compare alternatives on attributes (not brand styling). |
| **strengths** | Decision support for considered purchases. |
| **weaknesses** | Maintenance burden if offer changes frequently. |
| **recommended_use** | B2B service selection pages. |
| **forbidden_use** | Thin affiliate-style comparison without substance. |

---

### Contact / Gallery / Process / Team

#### VF_CONTACT_NAP_HUB

| Field | Value |
|-------|-------|
| **supported_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **supported_page_types** | CONTACT_PAGE |
| **supported_blocks** | CONTACTS |
| **purpose** | Present name, address, phone, hours as authoritative NAP surface. |
| **strengths** | Legal Entity Discovery alignment; local SEO support. |
| **weaknesses** | Incomplete without verified entity data. |
| **recommended_use** | CONTACT_PAGE required block. |
| **forbidden_use** | Marketing hero stacking on contact route. |

#### VF_GALLERY_MEDIA_GRID

| Field | Value |
|-------|-------|
| **supported_site_types** | CATALOG, ECOMMERCE |
| **supported_page_types** | PRODUCT_PAGE |
| **supported_blocks** | FEATURES (media role on PDP) |
| **purpose** | Structural placement of product media for inspection and trust. |
| **strengths** | Supports rich PDP content depth. |
| **weaknesses** | Not a substitute for spec/trust blocks. |
| **recommended_use** | PDP with physical or visual products. |
| **forbidden_use** | LEGAL_PAGE; decorative-only galleries without product context. |

#### VF_PROCESS_STEP_TIMELINE

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CORPORATE |
| **supported_page_types** | LANDING_PAGE, SERVICE_PAGE, HOME_PAGE |
| **supported_blocks** | PROCESS |
| **purpose** | Show ordered steps from inquiry to delivery/outcome. |
| **strengths** | Reduces uncertainty on LANDING required stack. |
| **weaknesses** | Weak on catalog browse pages. |
| **recommended_use** | LANDING required PROCESS block. |
| **forbidden_use** | CATALOG/ECOMMERCE blueprint FORBIDDEN PROCESS. |

#### VF_TEAM_GRID

| Field | Value |
|-------|-------|
| **supported_site_types** | PROMO, CORPORATE |
| **supported_page_types** | ABOUT_PAGE |
| **supported_blocks** | TEAM |
| **purpose** | Introduce people and roles for trust on about surfaces. |
| **strengths** | Humanizes B2B corporate sites. |
| **weaknesses** | Privacy/policy constraints on personal data. |
| **recommended_use** | ABOUT_PAGE optional/recommended stacks. |
| **forbidden_use** | LANDING (TEAM FORBIDDEN). |

---

### Commerce utility / Legal / Chrome

#### VF_CHECKOUT_FLOW_STEPS

| Field | Value |
|-------|-------|
| **supported_site_types** | ECOMMERCE |
| **supported_page_types** | (utility routes — not v1 page_type; ECOMMERCE only) |
| **supported_blocks** | CHECKOUT, PAYMENT |
| **purpose** | Guide transactional completion with step clarity. |
| **strengths** | Matches ecommerce funnel architecture. |
| **weaknesses** | SEO layer excludes checkout from index targets — design subordinate. |
| **recommended_use** | Checkout utility routes per Blueprint. |
| **forbidden_use** | Non-ECOMMERCE types; marketing landing primary. |

#### VF_LEGAL_DOCUMENT_BODY

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **supported_page_types** | LEGAL_PAGE |
| **supported_blocks** | (none — semantic legal body; FOOTER chrome elsewhere) |
| **purpose** | Readable legal text surface inheriting project chrome without marketing patterns. |
| **strengths** | Legal Pack compliance; no conversion distraction. |
| **weaknesses** | Not interchangeable with FAQ or ABOUT patterns. |
| **recommended_use** | All L1–L4 legal routes. |
| **forbidden_use** | HERO, CTA, LEAD_FORM, TRUST marketing patterns on same route. |

#### VF_FOOTER_SITE_CHROME

| Field | Value |
|-------|-------|
| **supported_site_types** | LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **supported_page_types** | All page types (global) |
| **supported_blocks** | FOOTER, LEGAL_LINKS |
| **purpose** | Site-wide navigation closure, legal links, secondary meta. |
| **strengths** | Consistent cross-route legal discoverability. |
| **weaknesses** | Overloaded footer harms mobile scan. |
| **recommended_use** | Every production route. |
| **forbidden_use** | Replacing LEGAL_PAGE primary content. |

---

## Remaining entries (summary rows)

Full contract parity — fields abbreviated; expand in project logs if needed.

| pattern_id | purpose (one line) |
|------------|-------------------|
| VF_FEATURES_CAPABILITY_GRID | Capability lists for product/service pages |
| VF_FEATURES_SPEC_HIGHLIGHT | Spec-focused highlights on PDP |
| VF_SERVICES_OVERVIEW_GRID | Service catalog overview on PROMO/CORPORATE |
| VF_SERVICES_DETAIL_STACK | Deep service narrative on SERVICE_PAGE |
| VF_TRUST_LOGO_STRIP | Logo-only credibility strip |
| VF_REVIEWS_FEATURED_QUOTES | Curated quotes on money pages |
| VF_CTA_STICKY_MOBILE | Mobile persistent primary action (LANDING contextual) |
| VF_CONTACT_SPLIT_FORM_MAP | Contact form beside map embed |
| VF_GALLERY_FEATURED_STRIP | Limited media strip when grid is heavy |
| VF_PROCESS_PHASE_CARDS | Phase-grouped process (fewer steps) |
| VF_TEAM_LEADERSHIP_FOCUS | Small leadership set vs full grid |
| VF_CATALOG_FILTERED_GRID | PLP with filter affordances |
| VF_PRODUCT_CARD_GRID | Repeatable card units in grids |
| VF_COMPARISON_TIER_MATRIX | Package tier matrix with pricing |
| VF_PRICING_SINGLE_OFFER | One primary price point |
| VF_LEAD_FORM_INLINE | Form embedded in narrative flow |
| VF_CASES_PROOF_GRID | Case study evidence grid |
| VF_CERTIFICATES_BADGE_ROW | Compliance/certification badges |
| VF_ABOUT_NARRATIVE | Company story arc |
| VF_PARTNERS_LOGO_WALL | Partner logos without full trust band |
| VF_DELIVERY_INFO_PANEL | Shipping/delivery expectations |
| VF_PAYMENT_METHODS_STRIP | Payment options disclosure |
| VF_CART_LINE_ITEMS | Cart review layout |
| VF_MAP_EMBED | Geographic embed supporting CONTACTS |

---

## SAFE UNKNOWN

- Exact variant count per family for Frontend — **FUTURE**.
- Pattern IDs for Extended site types — **not defined** in v1.

---

*Visual Pattern Registry version: v1.*
