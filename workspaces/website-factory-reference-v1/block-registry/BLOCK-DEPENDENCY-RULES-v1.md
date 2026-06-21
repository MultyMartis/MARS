# Website Factory — Block Dependency Rules v1

**Версия:** v1.1 *(WF-R01.2 Gate 2 — structural rules additive)*  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** документированные связи между блоками — **documentation only**  
**Связь:** [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [../legal/LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md)

---

## Назначение

Dependency rules описывают **hard** (обязательные) и **soft** (рекомендуемые) связи между `block_id` и внешними системами (Legal Pack, Blueprint). Нарушение hard dependency = **halt** + HITL.

**Легенда:**

| Тип | Значение |
|-----|----------|
| **requires** | Блок не может быть в production без зависимости |
| **recommends** | Усиливает качество; не блокирует v1 classification |
| **excludes** | Совместное появление запрещено без reclassification |

---

## Hard dependencies

### Commerce chain

| Block | Dependency | Rule |
|-------|------------|------|
| `CHECKOUT` | **requires** `CART` | Checkout без cart path → reclassify или architectural error |
| `CHECKOUT` | **requires** `LEGAL_LINKS` | Checkout forms collect PD — Legal Pack + Consent Rule |
| `CHECKOUT` | **requires** Consent Rule | [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) §4 |
| `CART` | **requires** `PRODUCT_CARD` or catalog context | Cart без product source — invalid ECOMMERCE |
| `PAYMENT` | **requires** `CHECKOUT` | Payment block в checkout flow, not standalone marketing |
| `PRODUCT_CARD` | **requires** `PRODUCT_GRID` **or** `CATEGORIES` structure | Card без PLP/category context — orphan unit |
| `PRODUCT_CARD` | **requires** `PRODUCT_PAGE` on PDP | PDP host page mandatory for product detail layout |

### Forms & legal

| Block | Dependency | Rule |
|-------|------------|------|
| `LEAD_FORM` | **requires** Consent Rule | Любая форма сбора ПДн |
| `LEAD_FORM` | **requires** `LEGAL_LINKS` (via `FOOTER`) | Footer Rule — canonical L1–L4 links in production |
| `LEAD_FORM` | **requires** Contact Channel | Valid submission endpoint or CRM handoff documented in project IA |
| `CHECKOUT` | **requires** Consent Rule | Guest checkout / account registration with PD |

### Legal & system

| Block | Dependency | Rule |
|-------|------------|------|
| `LEGAL_LINKS` | **requires** Legal Pack v1 (FROZEN) | L1–L4 documents generated per [LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md) |
| `FOOTER` | **requires** `LEGAL_LINKS` slot | Production footer includes 4 canonical legal URLs |
| `FOOTER` | **recommends** `CONTACTS` data | NAP consistency with Legal Entity Card |
| `CONTACTS` | **requires** Contact Channel | Phone, email, or messenger reachable — Legal Entity Card NAP |

### Catalog structure

| Block | Dependency | Rule |
|-------|------------|------|
| `PRODUCT_GRID` | **requires** `CATEGORIES` (tree or PLP route) | Grid привязан к category URL |
| `PRODUCT_GRID` | **recommends** `FILTERS` | When filterable PLP — control surface vs result surface |
| `CATEGORY_GRID` | **requires** `CATEGORIES` taxonomy | Tile grid without tree — invalid |
| `CATEGORIES` | **recommends** breadcrumbs | Blueprint CATALOG — global nav context |
| `PRODUCT_CARD` | **requires** `PRODUCT_PAGE` context on PDP | Card без PDP route — orphan on marketing pages |
| `PRODUCT_CARD` | **requires** `PRODUCT_GRID` **or** `CATEGORIES` structure | Card без PLP/category context — orphan unit |
| `REVIEWS` | **requires** `REVIEWS_PAGE` or `PRODUCT_PAGE` | UGC reviews need host page |

---

## Soft dependencies (recommended)

| Block | recommends | Rationale |
|-------|------------|-----------|
| `HERO` | `BENEFITS` below fold | Value prop continuity (LANDING stack) |
| `LEAD_FORM` | `TRUST` or `TESTIMONIALS` above | Cold traffic conversion |
| `PRICING` | `LEAD_FORM` or `CTA` | Tier → action path |
| `CHECKOUT` | `DELIVERY` | Shipping clarity pre-payment |
| `CHECKOUT` | `PAYMENT` | Payment method trust |
| `CASES` | `SERVICES` | Proof tied to offering |
| `MAP` | `CONTACTS` | NAP + geo consistency |
| `CERTIFICATES` | `TRUST` | Layered proof |
| `CTA` | prior `INFORMATIONAL` blocks | Avoid premature ask |
| `PRODUCT_GRID` | `FILTERS` | Filterable PLP — WF-R01.2 Gate 2 closure |

---

## Structural block dependencies (WF-R01.2 Gate 2)

Authority: [wf-r01-2-structural-blocks-charter-v1.md](../../../projects/mars-website-factory/wf-r01-2-structural-blocks-charter-v1.md).

### Hard dependencies

| Block | Dependency | Rule |
|-------|------------|------|
| `FILTERS` | **requires** `PRODUCT_GRID` or list context | Filters without inventory view — invalid PLP |
| `HEADER_NAV` | **requires** Blueprint global shell zone | Shell block without blueprint zone — architectural error |

### Soft dependencies

| Block | recommends | Rationale |
|-------|------------|-----------|
| `HEADER_NAV` | `FOOTER`, `LEGAL_LINKS` | Production shell pair |
| `FILTERS` | `CATEGORIES`, `HEADER_NAV` | Taxonomy + shell context |
| `SEARCH` | `HEADER_NAV` | Typical header placement |
| `SEARCH` | `PRODUCT_GRID` on results page | Results list surface |
| `SEARCH` | `FILTERS` (soft pair) | Catalog discovery refinement |

### Exclusion dependencies (structural)

| Block A | excludes (with) | Consequence |
|---------|-----------------|-------------|
| `HEADER_NAV` | `HERO` content absorption | HEADER ≠ HERO — [layout-shell-governance.md](../../../projects/mars-website-factory/layout-shell-governance.md) |
| `FILTERS` | `LANDING`, `PROMO` site types | Catalog discovery only |
| `FILTERS` | merge into `PRODUCT_GRID` markup | Separate control vs result surfaces |
| `SEARCH` | primary conversion on `LANDING` | Discovery primitive — not LANDING primary CTA |
| `MEGA_MENU`, `MOBILE_NAV_DRAWER`, `UTILITY_NAV` | separate `block_id` | HEADER_NAV variants/composition only |

### Catalog surface ordering (constraint graph)

```text
HEADER_NAV → [BREADCRUMBS layout] → [page intro] → FILTERS → PRODUCT_GRID → [PAGINATION layout] → FOOTER
```

BREADCRUMBS and PAGINATION — layout-component policy (Tier B); not Gate 2 `block_id` rows.

---

## Exclusion dependencies (cross-block)

| Block A | excludes (with) | Consequence |
|---------|-----------------|-------------|
| `CART` | `CATALOG` site type without ECOMMERCE reclassification | CATALOG v1 — cart **FORBIDDEN** |
| `CHECKOUT` | `CATALOG`, `LANDING`, `PROMO` (Core without subtree) | Reclassify → `ECOMMERCE` |
| `PAYMENT` | non-commerce site types | Same as checkout |
| `PRODUCT_GRID` + `CART` on same PDP | RFQ-only CATALOG PDP | CATALOG PDP = contact-led CTA only |

---

## External system dependencies

| System | Blocks affected | Rule |
|--------|-----------------|------|
| **Legal Pack v1 (FROZEN)** | `LEGAL_LINKS`, `FOOTER`, `LEAD_FORM`, `CHECKOUT` | Do not modify Legal Pack; blocks reference it |
| **Legal Entity Card** | `CONTACTS`, `FOOTER`, `LEGAL_LINKS` | Entity data for substitution |
| **Blueprint** | All blocks | Block selection **after** Blueprint freeze — [BLOCK-IMPLEMENTATION-RULES-v1.md](BLOCK-IMPLEMENTATION-RULES-v1.md) |
| **Site Type Registry** | All blocks | `allowed_site_types` per [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md) |

---

## Charter examples (operator reference)

| Block | Dependency | Type |
|-------|------------|------|
| `CHECKOUT` | **requires** `CART` | Hard — commerce chain |
| `PRODUCT_CARD` | **requires** `PRODUCT_PAGE` | Hard — PDP context |
| `LEGAL_LINKS` | **requires** Legal Pack v1 (FROZEN) | Hard — external |
| `LEAD_FORM` | **requires** Consent Rule | Hard — legal |
| `CONTACTS` | **requires** Contact Channel | Hard — operational |
| `CATEGORY_GRID` | **requires** `CATEGORIES` | Hard — catalog IA |
| `PAYMENT` | **requires** `CHECKOUT` | Hard — commerce |

---

## Dependency graph (commerce subset)

```
CATEGORIES
    ↓
PRODUCT_GRID
    ↓
PRODUCT_CARD (PDP)
    ↓
CART
    ↓
CHECKOUT ← LEGAL_LINKS ← Legal Pack v1
    ↓       ↑ Consent Rule
PAYMENT
    ↓
DELIVERY (parallel info)
```

---

## SAFE UNKNOWN

- Machine validation of dependency graph — **not implemented**
- Version pinning when Legal Pack v2 appears — **FUTURE charter**

---

*Dependency rules version: v1.1 (WF-R01.2 Gate 2 structural slice).*
