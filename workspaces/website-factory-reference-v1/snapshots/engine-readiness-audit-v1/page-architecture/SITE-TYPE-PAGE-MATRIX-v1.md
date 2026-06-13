# Website Factory — Site Type × Page Type Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** authoritative page-type compatibility per Core site type — **documentation only**  
**Scope:** **Core Types only** — `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

**Связь:** [PAGE-TYPE-REGISTRY-v1.md](PAGE-TYPE-REGISTRY-v1.md), [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md)

**Не в scope v1:** `SAAS`, `WEB_APPLICATION`, `MARKETPLACE` — **нет** page architecture rows; reclassification required before use.

---

## Легенда

| Mark | Значение |
|------|----------|
| **REQUIRED** | Production-quality site **неполон** без ≥1 страницы этого типа (или эквивалента в Blueprint) |
| **OPTIONAL** | Допустимо по project IA / Blueprint recommended |
| **FORBIDDEN** | Явный drift; reclassification или удаление из IA |

---

## Matrix

| page_type ↓ / site_type → | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|---------------------------|---------|-------|---------|-----------|-----------|
| **HOME_PAGE** | FORBIDDEN | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| **LANDING_PAGE** | REQUIRED | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL |
| **SERVICE_PAGE** | FORBIDDEN | REQUIRED | FORBIDDEN | FORBIDDEN | OPTIONAL |
| **CATEGORY_PAGE** | FORBIDDEN | FORBIDDEN | REQUIRED | REQUIRED | OPTIONAL¹ |
| **PRODUCT_PAGE** | FORBIDDEN | FORBIDDEN | REQUIRED | REQUIRED | OPTIONAL¹ |
| **ABOUT_PAGE** | FORBIDDEN | REQUIRED | OPTIONAL | OPTIONAL | REQUIRED |
| **CONTACT_PAGE** | OPTIONAL² | REQUIRED | REQUIRED | REQUIRED | REQUIRED |
| **FAQ_PAGE** | OPTIONAL² | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| **REVIEWS_PAGE** | FORBIDDEN | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |
| **LEGAL_PAGE** | OPTIONAL³ | REQUIRED³ | REQUIRED³ | REQUIRED³ | REQUIRED³ |

¹ **CORPORATE:** только при наличии catalog/ecommerce **subtree** (см. [CORPORATE-BLUEPRINT-v1.md](../blueprints/CORPORATE-BLUEPRINT-v1.md)).

² **LANDING:** контакты/FAQ как **блоки** на `LANDING_PAGE`; отдельные routes — OPTIONAL, не REQUIRED.

³ **LEGAL_PAGE:** REQUIRED при production + сбор ПДн / full Factory build — см. [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) §1–2. PPC-only non-production — legal routes не обязательны.

---

## Per site type notes

### LANDING

| page_type | Mark | Notes |
|-----------|------|-------|
| `LANDING_PAGE` | REQUIRED | `/` — единственная conversion surface |
| `HOME_PAGE` | FORBIDDEN | Multi-page home → reclassify **PROMO** |
| `LEGAL_PAGE` | OPTIONAL³ | 4 URLs when production |
| All catalog/commerce pages | FORBIDDEN | → CATALOG / ECOMMERCE |

### PROMO

| page_type | Mark | Notes |
|-----------|------|-------|
| `HOME_PAGE` | REQUIRED | `/` hub |
| `SERVICE_PAGE` | REQUIRED | ≥1 `/services/{slug}/` |
| `ABOUT_PAGE` | REQUIRED | `/about/` |
| `CONTACT_PAGE` | REQUIRED | `/contacts/` |
| `LEGAL_PAGE` | REQUIRED³ | L1–L4 production |
| `LANDING_PAGE` | OPTIONAL | Campaign landings |
| `FAQ_PAGE`, `REVIEWS_PAGE` | OPTIONAL | Recommended for trust/SEO |

### CATALOG

| page_type | Mark | Notes |
|-----------|------|-------|
| `HOME_PAGE` | REQUIRED | Catalog entry |
| `CATEGORY_PAGE` | REQUIRED | ≥1 PLP |
| `PRODUCT_PAGE` | REQUIRED | ≥1 PDP |
| `CONTACT_PAGE` | REQUIRED | Support / RFQ |
| `LEGAL_PAGE` | REQUIRED³ | Production |
| `CART`, checkout routes | FORBIDDEN | → ECOMMERCE |

### ECOMMERCE

| page_type | Mark | Notes |
|-----------|------|-------|
| `HOME_PAGE` | REQUIRED | Shop home |
| `CATEGORY_PAGE` | REQUIRED | PLP tree |
| `PRODUCT_PAGE` | REQUIRED | PDP + ATC |
| `CONTACT_PAGE` | REQUIRED | Support |
| `LEGAL_PAGE` | REQUIRED³ | L1–L4 + checkout PD |
| `ABOUT_PAGE`, `FAQ_PAGE` | OPTIONAL | Trust / support |
| `SERVICE_PAGE` | FORBIDDEN | B2B services hub → PROMO hybrid |
| `LANDING_PAGE` | FORBIDDEN | Single-page model → LANDING type |

**Utility pages (not in registry minimum):** `/cart/`, `/checkout/` — REQUIRED per [ECOMMERCE-BLUEPRINT-v1.md](../blueprints/ECOMMERCE-BLUEPRINT-v1.md); governed by Blueprint + PAGE-DEPENDENCY-RULES, not this matrix column.

### CORPORATE

| page_type | Mark | Notes |
|-----------|------|-------|
| `HOME_PAGE` | REQUIRED | Corporate hub |
| `ABOUT_PAGE` | REQUIRED | Enterprise trust |
| `CONTACT_PAGE` | REQUIRED | |
| `LEGAL_PAGE` | REQUIRED³ | |
| `SERVICE_PAGE` | OPTIONAL | Solutions / industries |
| `CATEGORY_PAGE`, `PRODUCT_PAGE` | OPTIONAL¹ | Subtree only |
| `LANDING_PAGE` | OPTIONAL | Segment campaigns |
| `REVIEWS_PAGE`, `FAQ_PAGE` | OPTIONAL | |

---

## Validation checklist

- [ ] `site_type_code` ∈ {`LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`}
- [ ] Нет FORBIDDEN page types в project `required_pages`
- [ ] Все REQUIRED page types имеют page contract + URL
- [ ] CORPORATE subtrees documented per route group
- [ ] Extended site types **не** используют эту матрицу без charter

---

## SAFE UNKNOWN

- Formal machine validation of matrix — **FUTURE**
- Thank-you page as `page_type` — **FUTURE** (`UTILITY_PAGE`)

---

*Site Type × Page Type Matrix version: v1.*
