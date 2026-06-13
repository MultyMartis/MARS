# Website Factory — Page Type Design Mapping v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** v1 minimum 10 `page_type` design roles — **documentation only**  
**Связь:** [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md), [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md), [PAGE-SEO-CONTRACT-v1.md](../seo-architecture/PAGE-SEO-CONTRACT-v1.md)

**Не является:** page template HTML, layout wireframes.

---

## Легенда

| Term | Meaning |
|------|---------|
| **recommended_patterns** | Primary `VF_*` pattern families for page role |
| **forbidden_patterns** | Must not appear as primary architecture on route |
| **design_role** | Architectural purpose of page in IA (one paragraph max) |

---

## HOME_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **recommended_patterns** | VF_HERO_CATALOG_GATEWAY or VF_HERO_VALUE_PROPOSITION · VF_SERVICES_OVERVIEW_GRID or VF_CATALOG_CATEGORY_HUB · VF_TRUST_SOCIAL_PROOF_BAND · VF_CTA_PRIMARY_BAND · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_LEGAL_DOCUMENT_BODY · VF_CHECKOUT_FLOW_STEPS · VF_LEAD_FORM_DEDICATED_PANEL as sole page (unless project charter) · VF_HERO_OFFER_LED as only pattern on corporate without brand balance |
| **design_role** | Entry hub: orient to money routes (services or catalog), establish trust, route to primary conversion without linear-landing overload. |

---

## LANDING_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | LANDING (required); PROMO, CORPORATE (optional campaign) |
| **recommended_patterns** | VF_HERO_VALUE_PROPOSITION or VF_HERO_OFFER_LED · VF_BENEFITS_OUTCOME_GRID · VF_PROCESS_STEP_TIMELINE · VF_TRUST_SOCIAL_PROOF_BAND · VF_FAQ_INLINE_OBJECTIONS · VF_PRICING_* (optional) · VF_LEAD_FORM_DEDICATED_PANEL · VF_CTA_PRIMARY_BAND · VF_CTA_STICKY_MOBILE (LANDING contextual) · VF_CONTACT_NAP_HUB or inline contact · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_CATALOG_CATEGORY_HUB as primary · VF_PRODUCT_PDP_FOCUS · VF_REVIEWS_AGGREGATE as primary · VF_CHECKOUT_FLOW_STEPS · VF_LEGAL_DOCUMENT_BODY |
| **design_role** | Single conversion surface: linear narrative, one primary action, campaign message match, proof before capture. |

---

## SERVICE_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | PROMO, CORPORATE |
| **recommended_patterns** | VF_HERO_VALUE_PROPOSITION · VF_SERVICES_DETAIL_STACK · VF_BENEFITS_OUTCOME_GRID or VF_FEATURES_CAPABILITY_GRID · VF_TRUST_SOCIAL_PROOF_BAND · VF_CASES_PROOF_GRID · VF_FAQ_INLINE_OBJECTIONS or VF_FAQ_ACCORDION · VF_LEAD_FORM_DEDICATED_PANEL or VF_LEAD_FORM_INLINE · VF_CTA_PRIMARY_BAND · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_CATALOG_FILTERED_GRID as primary · VF_PRODUCT_PDP_FOCUS · VF_CHECKOUT_FLOW_STEPS · VF_LEGAL_DOCUMENT_BODY |
| **design_role** | Money page: service-specific narrative, proof, objection handling, primary lead/CTA aligned with Blueprint. |

---

## CATEGORY_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | CATALOG, ECOMMERCE, CORPORATE (catalog subtree) |
| **recommended_patterns** | VF_HERO_CATALOG_GATEWAY (compact) · VF_CATALOG_CATEGORY_HUB · VF_CATALOG_FILTERED_GRID · VF_PRODUCT_CARD_GRID · VF_TRUST_LOGO_STRIP (optional) · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_BENEFITS_OUTCOME_GRID as PLP primary · VF_PROCESS_STEP_TIMELINE · VF_LEAD_FORM_DEDICATED_PANEL as primary · VF_LEGAL_DOCUMENT_BODY · VF_HERO_OFFER_LED campaign hero |
| **design_role** | PLP: browse, filter, drill to PDP; intro + grid dominance; minimal narrative friction. |

---

## PRODUCT_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | CATALOG, ECOMMERCE, CORPORATE |
| **recommended_patterns** | VF_PRODUCT_PDP_FOCUS · VF_GALLERY_MEDIA_GRID · VF_FEATURES_SPEC_HIGHLIGHT · VF_TRUST_SOCIAL_PROOF_BAND · VF_FAQ_INLINE_OBJECTIONS (optional) · VF_DELIVERY_INFO_PANEL (ECOMMERCE) · VF_CTA_PRIMARY_BAND or ATC pattern (ECOMMERCE — Frontend future) · VF_LEAD_FORM_* (CATALOG RFQ) · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_BENEFITS_COMPARISON_STRIP as PDP core · VF_SERVICES_OVERVIEW_GRID · VF_CHECKOUT_FLOW_STEPS as PDP body · VF_LEGAL_DOCUMENT_BODY · VF_REVIEWS_AGGREGATE replacing PDP focus |
| **design_role** | PDP: product identity, specs/media, trust, conversion action (RFQ vs ATC per site type). |

---

## ABOUT_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | PROMO, CORPORATE |
| **recommended_patterns** | VF_HERO_VALUE_PROPOSITION (compact) · VF_ABOUT_NARRATIVE · VF_TEAM_GRID or VF_TEAM_LEADERSHIP_FOCUS · VF_TRUST_SOCIAL_PROOF_BAND · VF_CASES_PROOF_GRID (optional) · VF_CTA_PRIMARY_BAND (soft) · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_LEAD_FORM_DEDICATED_PANEL as primary (PAGE-BLOCK mapping FORBIDDEN unless charter) · VF_CATALOG_* · VF_CHECKOUT_* · VF_PRICING_TIER_TABLE as primary · VF_LEGAL_DOCUMENT_BODY |
| **design_role** | Trust narrative: company story and people without hard commerce; supports SEO trust goals. |

---

## CONTACT_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **recommended_patterns** | VF_CONTACT_NAP_HUB · VF_CONTACT_SPLIT_FORM_MAP · VF_MAP_EMBED · VF_LEAD_FORM_INLINE (optional) · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_HERO_OFFER_LED · VF_BENEFITS_* · VF_CATALOG_* · VF_PRODUCT_PDP_FOCUS · VF_CHECKOUT_FLOW_STEPS · VF_LEGAL_DOCUMENT_BODY |
| **design_role** | Authoritative contact surface: verified NAP, optional form/map; no marketing stack substitution. |

---

## FAQ_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | PROMO, CATALOG, ECOMMERCE, CORPORATE |
| **recommended_patterns** | VF_FAQ_ACCORDION · VF_HERO_VALUE_PROPOSITION (compact optional) · VF_CTA_PRIMARY_BAND (support escalation, optional) · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_LEGAL_DOCUMENT_BODY · VF_LEAD_FORM_DEDICATED_PANEL as primary · VF_CATALOG_FILTERED_GRID · VF_PRODUCT_PDP_FOCUS |
| **design_role** | Support hub: scalable Q&A; may duplicate or extend inline FAQ blocks on other routes. |

---

## REVIEWS_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | PROMO, CORPORATE |
| **recommended_patterns** | VF_HERO_VALUE_PROPOSITION (intro) · VF_REVIEWS_AGGREGATE · VF_REVIEWS_FEATURED_QUOTES · VF_CASES_PROOF_GRID (optional) · VF_CTA_PRIMARY_BAND (optional) · VF_FOOTER_SITE_CHROME |
| **forbidden_patterns** | VF_LEGAL_DOCUMENT_BODY · VF_CATALOG_* · VF_CHECKOUT_* · VF_LEAD_FORM as primary when not in mapping |
| **design_role** | Social proof hub: aggregated reviews/testimonials distinct from inline trust bands on money pages. |

---

## LEGAL_PAGE

| Field | Value |
|-------|-------|
| **allowed_site_types** | All Core (production + Legal Pack) |
| **recommended_patterns** | VF_LEGAL_DOCUMENT_BODY · VF_FOOTER_SITE_CHROME (global inherit) |
| **forbidden_patterns** | All marketing families: VF_HERO_* · VF_CTA_* · VF_LEAD_FORM_* · VF_BENEFITS_* · VF_TRUST_SOCIAL_PROOF_BAND · VF_PRICING_* · VF_CATALOG_* · VF_PRODUCT_* |
| **design_role** | Legal document readability within project chrome; **inherits** site footer/nav shell — no conversion architecture. See [LEGAL-PAGE-CONTRACT-v1.md](../page-architecture/LEGAL-PAGE-CONTRACT-v1.md). |

---

## Page type summary

| page_type | Primary design focus | Top forbidden |
|-----------|---------------------|---------------|
| HOME_PAGE | Hub → money routes | Checkout, legal body |
| LANDING_PAGE | Linear conversion | Catalog/Product primary |
| SERVICE_PAGE | Service money page | Catalog grid primary |
| CATEGORY_PAGE | PLP browse | Benefits/process primary |
| PRODUCT_PAGE | PDP conversion | Checkout body on PDP |
| ABOUT_PAGE | Trust narrative | Aggressive lead primary |
| CONTACT_PAGE | NAP + contact | Marketing hero stack |
| FAQ_PAGE | Accordion hub | Legal body |
| REVIEWS_PAGE | Reviews aggregate | Catalog patterns |
| LEGAL_PAGE | Legal body only | All marketing patterns |

---

## SAFE UNKNOWN

- CART_PAGE / CHECKOUT_PAGE as formal `page_type` — **FUTURE** (ECOMMERCE extension); patterns documented under commerce utility in registry.

---

*Page Type Design Mapping version: v1.*
