# Website Factory — Page Dependency Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-architecture/`  
**Статус:** документированные связи между page types, Legal Pack, blocks — **documentation only**  
**Связь:** [PAGE-CONTRACT-v1.md](PAGE-CONTRACT-v1.md), [BLOCK-DEPENDENCY-RULES-v1.md](../block-registry/BLOCK-DEPENDENCY-RULES-v1.md)

---

## Назначение

Page dependency rules описывают **hard** (halt) и **soft** (recommended) связи на уровне **страниц** и page contracts. Дополняют block-level deps в Block Registry.

**Легенда:**

| Тип | Значение |
|-----|----------|
| **requires** | Страница / тип не может быть в production без зависимости |
| **recommends** | Улучшает IA; не блокирует v1 classification |
| **forbids** | Совместное появление запрещено без reclassification |

---

## Hard dependencies — page types

### Catalog & product

| Page type | Dependency | Rule |
|-----------|------------|------|
| `PRODUCT_PAGE` | **requires** `CATEGORY_PAGE` (tree or PLP parent) | PDP без category context = orphan URL; halt |
| `PRODUCT_PAGE` | **requires** Blueprint category tree | IA documented before PDP freeze |
| `CATEGORY_PAGE` | **recommends** `HOME_PAGE` | Nav path from entry |

### Legal

| Page type | Dependency | Rule |
|-----------|------------|------|
| `LEGAL_PAGE` | **requires** Legal Pack v1 (FROZEN) | [LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md) — templates + variables |
| `LEGAL_PAGE` | **requires** [LEGAL-PAGE-CONTRACT-v1.md](LEGAL-PAGE-CONTRACT-v1.md) | Layout + URL + H1 discipline |
| `LEGAL_PAGE` (production) | **requires** Legal Entity Card **READY** or verified Input Sheet | [LEGAL-ENTITY-DISCOVERY-RULES-v1.md](../legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md) — Triumph lesson |
| Production site with `LEGAL_PAGE` | **requires** Footer Rule | 4 canonical URLs in `FOOTER` / `LEGAL_LINKS` |

### Contact & forms

| Page type | Dependency | Rule |
|-----------|------------|------|
| `CONTACT_PAGE` | **requires** Consent Rule | When `LEAD_FORM` collects PD — [LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) §4 |
| `SERVICE_PAGE` | **requires** Consent Rule | When `LEAD_FORM` present |
| `LANDING_PAGE` | **requires** Consent Rule | When `LEAD_FORM` present |
| Any page with `LEAD_FORM` | **requires** `LEGAL_PAGE` routes (L2, L1 links) | Consent + Privacy URLs in checkbox |

### Commerce (ECOMMERCE — utility routes)

| Page / route | Dependency | Rule |
|--------------|------------|------|
| `CHECKOUT_PAGE` (utility) | **requires** `CART_PAGE` (utility) | Checkout без cart path → architectural error |
| `CHECKOUT_PAGE` | **requires** Consent Rule | Guest checkout / registration PD |
| `CHECKOUT_PAGE` | **requires** `LEGAL_PAGE` (production) | Checkout forms collect PD |
| `CART_PAGE` (utility) | **requires** ≥1 `PRODUCT_PAGE` in IA | Cart без product source |
| `PAYMENT` block context | **requires** `CHECKOUT_PAGE` | Per BLOCK-DEPENDENCY-RULES |

**Note:** `CART_PAGE` / `CHECKOUT_PAGE` — route-level roles in Blueprint, not minimum Page Type Registry codes.

### Site type constraints

| Condition | Rule |
|-----------|------|
| `CART_PAGE` on `CATALOG` | **forbids** — reclassify → `ECOMMERCE` |
| `CHECKOUT_PAGE` on `LANDING` / `PROMO` | **forbids** (default) |
| `SERVICE_PAGE` on `CATALOG` | **forbids** — use `PRODUCT_PAGE` or reclassify → `PROMO` |

---

## Soft dependencies — page types

| Page type | recommends | Rationale |
|-----------|------------|-----------|
| `SERVICE_PAGE` | `HOME_PAGE` in nav | Hub-and-spoke (PROMO) |
| `PRODUCT_PAGE` | `FAQ_PAGE` or inline `FAQ` | PDP objection handling |
| `REVIEWS_PAGE` | `SERVICE_PAGE` or `HOME_PAGE` link | Proof → money path |
| `ABOUT_PAGE` | `CONTACT_PAGE` | Trust → contact |
| `FAQ_PAGE` | `CONTACT_PAGE` | Escalation path |
| `HOME_PAGE` (ECOMMERCE) | `CATEGORY_PAGE` | Discovery entry |

---

## Cross-layer dependencies (page ↔ block)

| Page contract field | Block rule source |
|---------------------|-------------------|
| `required_blocks` | [BLOCK-DEPENDENCY-RULES-v1.md](../block-registry/BLOCK-DEPENDENCY-RULES-v1.md) |
| `LEAD_FORM` on page | Consent Rule + `LEGAL_LINKS` via `FOOTER` |
| `PRODUCT_PAGE` (ECOMMERCE) | `PRODUCT_CARD` requires PLP/category context |

**Authority:** Page-level `forbidden_blocks` **narrow** block usage; matrix FORBIDDEN **still applies** globally per site type.

---

## Triumph lessons (legal entity)

| Lesson | Page impact |
|--------|-------------|
| `legal_name` / `company_name` UNKNOWN | **STOP** `LEGAL_PAGE` generation |
| Footer as sole entity source | **forbids** for Legal Pack generation gate |
| Conflicting names in footer | Conflict report before `LEGAL_PAGE` freeze |

См. [TRIUMPH-LEGAL-ENTITY-LESSON-v1.md](../legal-entity/TRIUMPH-LEGAL-ENTITY-LESSON-v1.md) — **no Triumph workspace modifications**.

---

## Halt conditions (operator)

| Signal | Action |
|--------|--------|
| PDP without category parent | Halt; fix IA or CATEGORY_PAGE |
| Checkout without cart | Halt; ECOMMERCE flow error |
| `LEGAL_PAGE` with placeholders | Production FAIL — LEGAL-GENERATION-CONTRACT |
| Form without Consent Rule | Halt before Frontend |
| FORBIDDEN page type in matrix | Halt; reclassify site type |

---

## SAFE UNKNOWN

- Automated dependency graph validator — **FUTURE**
- Cross-project page template inheritance — **not defined**

---

*Page Dependency Rules version: v1.*
