# Website Factory — Core Page Architectures v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** канонические block stacks per `page_type` — **documentation only**  
**Связь:** [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md), [CORE-BLOCK-LIBRARY-v1.md](../block-registry/CORE-BLOCK-LIBRARY-v1.md)

**Не является:** автоматический composer, design spec, content outline

---

## Назначение

Документ задаёт **типовой состав** (required + recommended optional) для каждого canonical `page_type`. Project IA **может** добавлять optional blocks из matrix; **не может** удалять required без HITL.

`block_id` — authoritative keys из Block Registry v1.

---

## LANDING_PAGE

**Typical URL:** `/` (site type `LANDING`)

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `HERO` | required |
| 2 | `BENEFITS` | required |
| 3 | `PROCESS` | required |
| 4 | `TRUST` or `TESTIMONIALS` | required (social proof) |
| 5 | `FAQ` | required |
| 6 | `LEAD_FORM` | required |
| 7 | `CTA` | required (incl. mobile sticky variant where applicable — same `block_id`; ref. partial `sticky_cta.html`) |
| 8 | `CONTACTS` | required |
| 9 | `FOOTER` | required (incl. `LEGAL_LINKS`) |

**Optional:** `PRICING`, `CASES`, `CERTIFICATES`

**Optional media (not `block_id`):** embedded video within `HERO` or content sections — implementation note only; not in Core 29 registry.

**Forbidden:** `CART`, `CHECKOUT`, `PAYMENT`, `CATEGORIES`, `PRODUCT_GRID`, `SERVICES` (multi-page hub)

**Blueprint ref:** [LANDING-BLUEPRINT-v1.md](../blueprints/LANDING-BLUEPRINT-v1.md)

---

## HOME_PAGE

**Typical URL:** `/`

### PROMO / CORPORATE (marketing home)

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `HERO` | required |
| 2 | `BENEFITS` | recommended |
| 3 | `SERVICES` | required (PROMO) / optional (CORPORATE) |
| 4 | `CASES` or `TRUST` | recommended |
| 5 | `CTA` | required |
| 6 | `CONTACTS` or teaser to `CONTACT_PAGE` | required |
| 7 | `FOOTER` | required |

**Optional:** `FAQ` (teaser), `PARTNERS`, `PROCESS`, `PRICING`

### CATALOG / ECOMMERCE (shop home)

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `HERO` or promo banner | required |
| 2 | `CATEGORIES` | required |
| 3 | `PRODUCT_GRID` | recommended |
| 4 | `CTA` | optional |
| 5 | `FOOTER` | required |

**Forbidden (CATALOG home):** `CART`, `CHECKOUT`, `PAYMENT`

---

## SERVICE_PAGE

**Typical URL:** `/services/{slug}/`

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `HERO` | required |
| 2 | Service description (content / `BENEFITS`) | required |
| 3 | `BENEFITS` | recommended |
| 4 | `CASES` | recommended |
| 5 | `PROCESS` | optional |
| 6 | `FAQ` | required |
| 7 | `LEAD_FORM` | required |
| 8 | `CTA` | required |
| 9 | `TRUST` | recommended |
| 10 | `FOOTER` | required |

**Forbidden:** `CART`, `CHECKOUT`, `PRODUCT_GRID` (catalog-scale)

**Blueprint ref:** [PROMO-BLUEPRINT-v1.md](../blueprints/PROMO-BLUEPRINT-v1.md)

---

## CATEGORY_PAGE

**Typical URL:** `/{category}/`

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | Category intro (`HERO` or compact header) | required |
| 2 | `CATEGORIES` (subcats) | optional |
| 3 | `PRODUCT_GRID` | required |
| 4 | Filters (UI — may be part of grid block) | required per Blueprint |
| 5 | `CTA` (RFQ / contact) | required (CATALOG) |
| 6 | `FOOTER` | required |

**Forbidden:** `LEAD_FORM` as sole conversion without RFQ context on PLP — document CTA type in project IA

**Blueprint ref:** [CATALOG-BLUEPRINT-v1.md](../blueprints/CATALOG-BLUEPRINT-v1.md)

---

## PRODUCT_PAGE

**Typical URL:** `…/{product-slug}/`

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `PRODUCT_CARD` (PDP layout) | required |
| 2 | Product info / specs (within card or adjacent) | required |
| 3 | `BENEFITS` or features list | recommended |
| 4 | `TRUST` | required |
| 5 | `CTA` | required |
| 6 | `FAQ` | optional |
| 7 | `FOOTER` | required |

### ECOMMERCE additions

| block_id | Stance |
|----------|--------|
| Add-to-cart (within `PRODUCT_CARD`) | required |
| `CTA` (mobile sticky / ATC variant) | recommended |

**CATALOG:** ATC blocks **forbidden** — RFQ / `LEAD_FORM` / contact CTA

**Blueprint ref:** CATALOG / ECOMMERCE Blueprints

---

## ABOUT_PAGE

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `HERO` | required |
| 2 | Company story (content) | required |
| 3 | `TRUST` / team | recommended |
| 4 | `CERTIFICATES` | optional |
| 5 | `CTA` | optional |
| 6 | `FOOTER` | required |

**Forbidden:** `CHECKOUT`, `CART`, `LEAD_FORM` as primary unless project charter

---

## CONTACT_PAGE

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `CONTACTS` | required |
| 2 | `MAP` | optional |
| 3 | `LEAD_FORM` | recommended |
| 4 | `FOOTER` | required |

**Legal:** `LEAD_FORM` → Consent Rule (PAGE-DEPENDENCY-RULES)

---

## FAQ_PAGE

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | Page intro (`HERO` compact or H1 region) | required |
| 2 | `FAQ` | required |
| 3 | `CTA` | optional |
| 4 | `FOOTER` | required |

---

## REVIEWS_PAGE

| Order | block_id | Stance |
|-------|----------|--------|
| 1 | `HERO` or intro | required |
| 2 | `TESTIMONIALS` / `TRUST` | required |
| 3 | `CASES` | optional |
| 4 | `CTA` | recommended |
| 5 | `FOOTER` | required |

---

## LEGAL_PAGE

**Не дублировать block stack здесь** — authoritative: [LEGAL-PAGE-CONTRACT-v1.md](LEGAL-PAGE-CONTRACT-v1.md).

**Summary:** semantic HTML body in project content container; **no** marketing block stack (`HERO`, `LEAD_FORM`, etc.) on legal routes.

---

## ECOMMERCE utility pages (dependency layer only)

Не входят в минимальный Page Type Registry; block stacks в Blueprint:

| Route role | Typical blocks |
|------------|----------------|
| Cart (`/cart/`) | `CART`, `CTA`, `FOOTER` |
| Checkout (`/checkout/`) | `CHECKOUT`, `PAYMENT`, Consent Rule, `FOOTER` |
| Order confirmation | confirmation content, `FOOTER` |

См. [PAGE-DEPENDENCY-RULES-v1.md](PAGE-DEPENDENCY-RULES-v1.md).

---

## SAFE UNKNOWN

- Per-industry SERVICE_PAGE variants (medical, B2B heavy) — **project IA**, not cataloged in v1
- Breadcrumbs as formal `block_id` — **FUTURE** (see BLOCK-GAPS)

---

*Core Page Architectures version: v1.*
