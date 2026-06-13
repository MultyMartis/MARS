# Website Factory — Site Type SEO Mapping v2

**Версия:** v2  
**Дата:** 2026-06-01  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** Core 5 site type SEO profiles — **documentation only**  
**Scope:** `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` only

**Предшественник:** [registry/SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — priority hints; v2 — full architecture profile.

**Связь:** [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md), [SEARCH-INTENT-MODEL-v1.md](SEARCH-INTENT-MODEL-v1.md), [SEO-IMPLEMENTATION-RULES-v1.md](SEO-IMPLEMENTATION-RULES-v1.md)

**Не является:** SEO content generation, keyword research, meta templates.

**Extended types (SAAS, WEB_APPLICATION, MARKETPLACE):** остаются в registry v1 shallow mapping only — **not expanded** in v2 (see [SEO-ARCHITECTURE-GAPS-v1.md](SEO-ARCHITECTURE-GAPS-v1.md)).

---

## Легенда

| Term | Meaning |
|------|---------|
| **SEO depth** | `MINIMAL` · `SELECTIVE` · `STANDARD` · `DEEP` — architecture effort / IA complexity for search |
| **Content depth** | `MINIMAL` · `MODERATE` · `RICH` — required signal richness on key pages |
| **SEO priority (v1 compat)** | LOW / HIGH — retained for cross-reference |

---

## LANDING

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **SEO priority (v1)** | **LOW** |
| **Primary SEO goal** | Align single URL with PPC/campaign offer; technical baseline for brand+offer queries |
| **Secondary SEO goal** | Optional limited organic for branded + high-intent campaign terms |
| **Typical intent mix** | `COMMERCIAL` (dominant) · `TRANSACTIONAL` · `BRAND` · optional `LOCAL` |
| **SEO depth** | **MINIMAL** |
| **Content depth** | **MINIMAL** — offer clarity, proof blocks, single H1 intent |
| **Priority pages** | `LANDING_PAGE` (required); `LEGAL_PAGE` (production, navigational) |
| **Explicit exclusions** | Blog-first IA; multi-page organic hub (`HOME_PAGE`); category/product catalog SEO; `FAQ_PAGE` as SEO hub; comparison content program; content marketing scale |
| **Indexation posture** | Primary `/` index or campaign policy; `noindex` acceptable for pure PPC clones (document in strategy contract); legal routes per production rules |
| **Traffic alignment** | **PPC-first** (Blueprint) |

---

## PROMO

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **SEO priority (v1)** | **HIGH** |
| **Primary SEO goal** | Indexable service/money pages + brand/local visibility |
| **Secondary SEO goal** | Trust pages (about, reviews) supporting money page rankings |
| **Typical intent mix** | `SERVICE` · `LOCAL` · `BRAND` · `COMMERCIAL` · `INFORMATIONAL` (FAQ) |
| **SEO depth** | **STANDARD** |
| **Content depth** | **MODERATE** — unique service narratives, proof, NAP |
| **Priority pages** | `HOME_PAGE`, `SERVICE_PAGE`, `CONTACT_PAGE`, `ABOUT_PAGE`; optional `REVIEWS_PAGE`, `FAQ_PAGE` |
| **Explicit exclusions** | Checkout/cart strategy; catalog PLP/PDP at scale (→ CATALOG/ECOMMERCE); blog-only site without money pages; `LANDING_PAGE` as sole indexable surface |
| **Indexation posture** | Index money + trust; noindex thin duplicates / utility |
| **Traffic alignment** | **MIXED** — organic + brand + local |

---

## CATALOG

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **SEO priority (v1)** | **HIGH** |
| **Primary SEO goal** | Category (PLP) + product (PDP) long-tail visibility; RFQ conversion |
| **Secondary SEO goal** | Controlled technical indexation (facets, pagination policy) |
| **Typical intent mix** | `COMMERCIAL` · `INFORMATIONAL` (specs) · `NAVIGATIONAL` (category tree) |
| **SEO depth** | **DEEP** |
| **Content depth** | **RICH** on PDP — specs, media, trust; **MODERATE** on PLP |
| **Priority pages** | `HOME_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `CONTACT_PAGE` |
| **Explicit exclusions** | Checkout/cart SEO strategy (no transactional funnel indexation); blog-first without catalog IA; infinite thin facet URLs; pretending full ecommerce without reclassification |
| **Indexation posture** | Index PLP/PDP; facet policy documented; cart/checkout N/A (forbidden page types) |
| **Traffic alignment** | **ORGANIC** primary |

---

## ECOMMERCE

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **SEO priority (v1)** | **HIGH** |
| **Primary SEO goal** | Commercial catalog SEO — category + product + transactional PDP intent |
| **Secondary SEO goal** | Trust/support pages; policy indexation; CWV on PLP/PDP |
| **Typical intent mix** | `COMMERCIAL` · `TRANSACTIONAL` (PDP) · `INFORMATIONAL` (support) |
| **SEO depth** | **DEEP** |
| **Content depth** | **RICH** PDP; **MODERATE** PLP |
| **Priority pages** | `HOME_PAGE`, `CATEGORY_PAGE`, `PRODUCT_PAGE`, `CONTACT_PAGE`; optional `FAQ_PAGE`, `ABOUT_PAGE` |
| **Explicit exclusions** | **Checkout excluded from SEO targets** (cart/checkout/thank-you — utility, default noindex); B2B-only services hub as primary (`SERVICE_PAGE` forbidden); single-page LANDING model |
| **Indexation posture** | Index catalog + policies; utility funnel noindex |
| **Traffic alignment** | **ORGANIC** + paid product ads (project) |

---

## CORPORATE

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **SEO priority (v1)** | **HIGH** |
| **Primary SEO goal** | Brand + multi-audience hub-and-spoke; solutions/industries intent clarity |
| **Secondary SEO goal** | Thought leadership / news (optional subtree); employer brand (careers) if applicable |
| **Typical intent mix** | `BRAND` · `INFORMATIONAL` · `SERVICE` · `NAVIGATIONAL` · optional `COMMERCIAL` (catalog subtree) |
| **SEO depth** | **DEEP** (IA complexity) |
| **Content depth** | **MODERATE**–**RICH** on solutions; **MODERATE** corporate trust |
| **Priority pages** | `HOME_PAGE`, `ABOUT_PAGE`, `CONTACT_PAGE`; optional `SERVICE_PAGE`, `REVIEWS_PAGE`; subtree: `CATEGORY_PAGE`, `PRODUCT_PAGE` when catalog/ecommerce hybrid documented |
| **Explicit exclusions** | Cannibalizing duplicate solution URLs; unbounded blog without hub discipline; LANDING-only IA; checkout SEO on non-ECOMMERCE classification |
| **Indexation posture** | Index entity + solutions; subtree rules per route group; careers/index when ATS allows — project |
| **Traffic alignment** | **BRAND** + **ORGANIC** |

---

## Summary table

| site_type_code | SEO priority | Primary SEO goal (short) | SEO depth | Content depth | Primary traffic |
|----------------|--------------|--------------------------|-----------|---------------|-----------------|
| **LANDING** | LOW | PPC-aligned single URL | MINIMAL | MINIMAL | PPC |
| **PROMO** | HIGH | Service + local/brand pages | STANDARD | MODERATE | MIXED |
| **CATALOG** | HIGH | Category + PDP long-tail | DEEP | RICH (PDP) | ORGANIC |
| **ECOMMERCE** | HIGH | Commercial catalog + PDP | DEEP | RICH (PDP) | ORGANIC |
| **CORPORATE** | HIGH | Brand + multi-audience IA | DEEP | MODERATE–RICH | BRAND + ORGANIC |

---

## Cross-reference: page types

Матрица допустимых `page_type`: [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md).

SEO priority pages **must** be subset of matrix REQUIRED + SEO-relevant OPTIONAL.

---

## SAFE UNKNOWN

- Faceted SEO addendum for CATALOG — **FUTURE** (noted in v1).
- hreflang / multi-region — project charter.
- Extended type parity with this v2 depth — **not in scope**.

---

*Site Type SEO Mapping version: v2. Canonical location: `seo-architecture/` (successor to registry v1 hints).*
