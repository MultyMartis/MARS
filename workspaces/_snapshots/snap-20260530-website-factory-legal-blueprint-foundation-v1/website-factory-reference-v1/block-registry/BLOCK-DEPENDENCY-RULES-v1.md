# Website Factory — Block Dependency Rules v1

**Версия:** v1  
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

### Forms & legal

| Block | Dependency | Rule |
|-------|------------|------|
| `LEAD_FORM` | **requires** Consent Rule | Любая форма сбора ПДн |
| `LEAD_FORM` | **requires** `LEGAL_LINKS` (via `FOOTER`) | Footer Rule — canonical L1–L4 links in production |
| `CHECKOUT` | **requires** Consent Rule | Guest checkout / account registration with PD |

### Legal & system

| Block | Dependency | Rule |
|-------|------------|------|
| `LEGAL_LINKS` | **requires** Legal Pack v1 (FROZEN) | L1–L4 documents generated per [LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md) |
| `FOOTER` | **requires** `LEGAL_LINKS` slot | Production footer includes 4 canonical legal URLs |
| `FOOTER` | **recommends** `CONTACTS` data | NAP consistency with Legal Entity Card |

### Catalog structure

| Block | Dependency | Rule |
|-------|------------|------|
| `PRODUCT_GRID` | **requires** `CATEGORIES` (tree or PLP route) | Grid привязан к category URL |
| `CATEGORIES` | **recommends** breadcrumbs | Blueprint CATALOG — global nav context |
| `PRODUCT_CARD` on PDP | **requires** PDP page (not grid-only) | PDP blocks documented per Blueprint |

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

*Dependency rules version: v1.*
