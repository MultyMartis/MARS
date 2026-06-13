# Website Factory — SEO Architecture Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/seo-architecture/`  
**Статус:** Site Type × Intent Type × Page Type compatibility — **documentation only**  
**Scope:** Core 5 — `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`

**Связь:** [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md), [SEARCH-INTENT-MODEL-v1.md](SEARCH-INTENT-MODEL-v1.md), [SITE-TYPE-SEO-MAPPING-v2.md](SITE-TYPE-SEO-MAPPING-v2.md)

**Не является:** automated matrix validator.

---

## Легенда ячеек

| Mark | Meaning |
|------|---------|
| **REQUIRED** | Primary or mandatory SEO binding: this page_type **must** carry this intent when page exists |
| **OPTIONAL** | Allowed when page exists; document in Page SEO Contract |
| **FORBIDDEN** | Architectural mismatch — do not assign this intent to this page_type under this site type |
| **—** | Page type not applicable (FORBIDDEN or absent per SITE-TYPE-PAGE-MATRIX-v1) |

**Precedence:** If `page_type` is FORBIDDEN in [SITE-TYPE-PAGE-MATRIX-v1.md](../page-architecture/SITE-TYPE-PAGE-MATRIX-v1.md), all intent cells are **—** (page must not exist).

---

## LANDING

| page_type ↓ / intent → | COMMERCIAL | TRANSACTIONAL | SERVICE | INFORMATIONAL | NAVIGATIONAL | BRAND | COMPARISON | LOCAL |
|------------------------|------------|-----------------|---------|---------------|--------------|-------|------------|-------|
| **LANDING_PAGE** | REQUIRED | REQUIRED | FORBIDDEN | OPTIONAL | FORBIDDEN | REQUIRED | OPTIONAL | OPTIONAL |
| **LEGAL_PAGE** | — | — | — | OPTIONAL | REQUIRED | — | — | — |
| **CONTACT_PAGE**² | — | — | — | — | OPTIONAL | — | — | OPTIONAL |
| **FAQ_PAGE**² | — | — | — | OPTIONAL | — | — | FORBIDDEN | — |
| **HOME_PAGE** | — | — | — | — | — | — | — | — |
| **SERVICE_PAGE** | — | — | — | — | — | — | — | — |
| **CATEGORY_PAGE** | — | — | — | — | — | — | — | — |
| **PRODUCT_PAGE** | — | — | — | — | — | — | — | — |
| **ABOUT_PAGE** | — | — | — | — | — | — | — | — |
| **REVIEWS_PAGE** | — | — | — | — | — | — | — | — |

² OPTIONAL route only — prefer blocks on `LANDING_PAGE` per PAGE matrix.

**Site-level rule:** Only one primary indexable conversion surface (`LANDING_PAGE`). No intent matrix row applies to blog/catalog pages.

---

## PROMO

| page_type ↓ / intent → | COMMERCIAL | TRANSACTIONAL | SERVICE | INFORMATIONAL | NAVIGATIONAL | BRAND | COMPARISON | LOCAL |
|------------------------|------------|-----------------|---------|---------------|--------------|-------|------------|-------|
| **HOME_PAGE** | OPTIONAL | FORBIDDEN | OPTIONAL | OPTIONAL | REQUIRED | REQUIRED | FORBIDDEN | OPTIONAL |
| **SERVICE_PAGE** | REQUIRED | FORBIDDEN | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL | OPTIONAL | OPTIONAL |
| **CONTACT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN | REQUIRED |
| **ABOUT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | REQUIRED | FORBIDDEN | FORBIDDEN |
| **FAQ_PAGE** | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **REVIEWS_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN |
| **LEGAL_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **LANDING_PAGE**¹ | REQUIRED | OPTIONAL | OPTIONAL | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | OPTIONAL |
| **CATEGORY_PAGE** | — | — | — | — | — | — | — | — |
| **PRODUCT_PAGE** | — | — | — | — | — | — | — | — |

¹ OPTIONAL campaign page.

---

## CATALOG

| page_type ↓ / intent → | COMMERCIAL | TRANSACTIONAL | SERVICE | INFORMATIONAL | NAVIGATIONAL | BRAND | COMPARISON | LOCAL |
|------------------------|------------|-----------------|---------|---------------|--------------|-------|------------|-------|
| **HOME_PAGE** | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | REQUIRED | FORBIDDEN | FORBIDDEN |
| **CATEGORY_PAGE** | REQUIRED | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | FORBIDDEN | OPTIONAL | FORBIDDEN |
| **PRODUCT_PAGE** | REQUIRED | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL | FORBIDDEN |
| **CONTACT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL |
| **FAQ_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **ABOUT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | OPTIONAL | FORBIDDEN | FORBIDDEN |
| **LEGAL_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **SERVICE_PAGE** | — | — | — | — | — | — | — | — |
| **LANDING_PAGE** | — | — | — | — | — | — | — | — |
| **REVIEWS_PAGE** | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL | OPTIONAL | OPTIONAL | FORBIDDEN | FORBIDDEN |

**Site-level rule:** `TRANSACTIONAL` intent **FORBIDDEN** at site level (no checkout SEO). RFQ = conversion signal, not transactional indexation target.

---

## ECOMMERCE

| page_type ↓ / intent → | COMMERCIAL | TRANSACTIONAL | SERVICE | INFORMATIONAL | NAVIGATIONAL | BRAND | COMPARISON | LOCAL |
|------------------------|------------|-----------------|---------|---------------|--------------|-------|------------|-------|
| **HOME_PAGE** | OPTIONAL | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | REQUIRED | FORBIDDEN | FORBIDDEN |
| **CATEGORY_PAGE** | REQUIRED | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | FORBIDDEN | OPTIONAL | FORBIDDEN |
| **PRODUCT_PAGE** | REQUIRED | REQUIRED | FORBIDDEN | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL | FORBIDDEN |
| **CONTACT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL |
| **FAQ_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **ABOUT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | OPTIONAL | FORBIDDEN | FORBIDDEN |
| **LEGAL_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **SERVICE_PAGE** | — | — | — | — | — | — | — | — |
| **LANDING_PAGE** | — | — | — | — | — | — | — | — |

**Utility routes (cart/checkout):** all intents **FORBIDDEN** — routes excluded from SEO architecture (Blueprint utility, not in page type registry minimum).

---

## CORPORATE

| page_type ↓ / intent → | COMMERCIAL | TRANSACTIONAL | SERVICE | INFORMATIONAL | NAVIGATIONAL | BRAND | COMPARISON | LOCAL |
|------------------------|------------|-----------------|---------|---------------|--------------|-------|------------|-------|
| **HOME_PAGE** | OPTIONAL | FORBIDDEN | OPTIONAL | OPTIONAL | REQUIRED | REQUIRED | FORBIDDEN | FORBIDDEN |
| **ABOUT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | REQUIRED | FORBIDDEN | FORBIDDEN |
| **CONTACT_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL |
| **SERVICE_PAGE**¹ | OPTIONAL | FORBIDDEN | REQUIRED | REQUIRED | FORBIDDEN | OPTIONAL | OPTIONAL | FORBIDDEN |
| **REVIEWS_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN |
| **FAQ_PAGE** | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | OPTIONAL | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **LEGAL_PAGE** | FORBIDDEN | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | FORBIDDEN | FORBIDDEN | FORBIDDEN |
| **CATEGORY_PAGE**¹ | REQUIRED | FORBIDDEN | FORBIDDEN | OPTIONAL | REQUIRED | FORBIDDEN | OPTIONAL | FORBIDDEN |
| **PRODUCT_PAGE**¹ | REQUIRED | OPTIONAL | FORBIDDEN | REQUIRED | OPTIONAL | FORBIDDEN | OPTIONAL | FORBIDDEN |
| **LANDING_PAGE**¹ | REQUIRED | OPTIONAL | OPTIONAL | FORBIDDEN | FORBIDDEN | REQUIRED | OPTIONAL | OPTIONAL |

¹ Subtree only — when catalog/ecommerce hybrid documented in Blueprint.

---

## Matrix validation rules

| # | Rule |
|---|------|
| M1 | Each indexable page has **exactly one** REQUIRED primary intent (one REQUIRED per row maximum across intents — if multiple REQUIRED, designate primary in Page SEO Contract) |
| M2 | No FORBIDDEN cell may be selected in Page SEO Contract |
| M3 | Page type must exist in SITE-TYPE-PAGE-MATRIX before applying this matrix |
| M4 | Site-level exclusions from SITE-TYPE-SEO-MAPPING-v2 override OPTIONAL → effective FORBIDDEN |
| M5 | Utility/checkout routes: no matrix row — documented noindex in SEO Strategy Contract only |

---

## Primary intent quick map (default)

| site_type | page_type | Default primary intent |
|-----------|-----------|------------------------|
| LANDING | LANDING_PAGE | COMMERCIAL |
| PROMO | SERVICE_PAGE | SERVICE |
| PROMO | HOME_PAGE | BRAND |
| CATALOG | CATEGORY_PAGE | COMMERCIAL |
| CATALOG | PRODUCT_PAGE | COMMERCIAL |
| ECOMMERCE | PRODUCT_PAGE | COMMERCIAL (+ TRANSACTIONAL secondary) |
| ECOMMERCE | CATEGORY_PAGE | COMMERCIAL |
| CORPORATE | HOME_PAGE | BRAND |
| CORPORATE | SERVICE_PAGE | SERVICE |
| * | LEGAL_PAGE | NAVIGATIONAL |

---

## SAFE UNKNOWN

- Machine validation of matrix cells — **FUTURE**.
- `CONTENT_HUB_PAGE` rows — **FUTURE** page type.

---

*SEO Architecture Matrix version: v1.*
