# Website Factory — Block Conversion Roles v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/block-registry/`  
**Статус:** канонические conversion classes для Block Registry  
**Связь:** [BLOCK-REGISTRY-v1.md](BLOCK-REGISTRY-v1.md), [BLOCK-CATEGORIES-v1.md](BLOCK-CATEGORIES-v1.md)

---

## Назначение

`conversion_role` описывает **коммерческую функцию** блока в conversion stack — не SEO-роль и не design variant. Один primary `conversion_role` на `block_id`.

---

## Conversion classes

| conversion_role | Описание | Ожидание в stack |
|-----------------|----------|------------------|
| `PRIMARY_CONVERSION` | Главное целевое действие страницы или funnel | ≤1 primary per page (HITL при конфликте) |
| `SECONDARY_CONVERSION` | Поддерживающее действие (звонок, «узнать больше», RFQ) | Subordinate к primary |
| `TRUST_SUPPORT` | Снижение риска, proof — не самостоятельная conversion | Между value prop и primary CTA |
| `INFORMATIONAL` | Объяснение, discovery, сравнение — без прямой транзакции | Питает decision path |
| `LEGAL` | Compliance surface — ссылки, disclosures | Footer / form-adjacent |
| `SYSTEM` | Shell, chrome — не conversion block | Global |

---

## Назначение ролей — Core Block Library

| block_id | conversion_role | Пояснение |
|----------|-----------------|-----------|
| `HERO` | SECONDARY_CONVERSION | Orientation + optional CTA; на LANDING часто ведёт к primary ниже по stack |
| `BENEFITS` | INFORMATIONAL | Value articulation |
| `SERVICES` | INFORMATIONAL | Service discovery |
| `CATEGORIES` | INFORMATIONAL | Catalog entry / taxonomy |
| `PRODUCT_GRID` | INFORMATIONAL | PLP browsing |
| `PRODUCT_CARD` | INFORMATIONAL | Unit display; may carry micro-CTA |
| `PRICING` | SECONDARY_CONVERSION | Tier selection → form or checkout |
| `PROCESS` | INFORMATIONAL | How-it-works |
| `CASES` | TRUST_SUPPORT | Proof via outcomes |
| `TESTIMONIALS` | TRUST_SUPPORT | Social proof quotes |
| `TRUST` | TRUST_SUPPORT | Logos, metrics, badges |
| `CERTIFICATES` | TRUST_SUPPORT | Regulated / licensed proof |
| `TEAM` | TRUST_SUPPORT | Human credibility |
| `ABOUT` | INFORMATIONAL | Entity narrative |
| `FAQ` | INFORMATIONAL | Objection handling |
| `CTA` | PRIMARY_CONVERSION | Repeated primary action (band / sticky) |
| `LEAD_FORM` | PRIMARY_CONVERSION | Form submit — primary на LANDING/PROMO money pages |
| `CONTACTS` | SECONDARY_CONVERSION | Contact hub |
| `MAP` | INFORMATIONAL | Geo / location context |
| `PARTNERS` | TRUST_SUPPORT | B2B credibility |
| `DELIVERY` | INFORMATIONAL | Pre-checkout reassurance |
| `PAYMENT` | TRUST_SUPPORT | Payment trust at checkout |
| `CHECKOUT` | PRIMARY_CONVERSION | Purchase completion |
| `CART` | SECONDARY_CONVERSION | Cart review → checkout |
| `LEGAL_LINKS` | LEGAL | L1–L4 link cluster |
| `FOOTER` | SYSTEM | Global shell |

---

## Primary conversion by site type (Blueprint alignment)

| site_type_code | Typical PRIMARY_CONVERSION blocks |
|----------------|-----------------------------------|
| `LANDING` | `LEAD_FORM`, `CTA` |
| `PROMO` | Contextual `LEAD_FORM`, `CTA`, `CONTACTS` |
| `CATALOG` | RFQ via `LEAD_FORM` on PDP; `CONTACTS` |
| `ECOMMERCE` | `CHECKOUT`; PDP add-to-cart → `CART` |
| `CORPORATE` | Segment-specific `LEAD_FORM` / `CONTACTS` / subtree commerce |

---

## Правила stacking

| Rule | Description |
|------|-------------|
| **One primary per page** | Не более одного `PRIMARY_CONVERSION` block role как «главный» на странице |
| **Trust before ask** | `TRUST_SUPPORT` blocks рекомендуются перед `PRIMARY_CONVERSION` на cold traffic pages |
| **Legal adjacent** | `LEAD_FORM` / `CHECKOUT` **must** satisfy Consent Rule — см. dependencies |
| **Commerce path** | `CART` → `CHECKOUT` → `PAYMENT` — единственный primary path для ECOMMERCE purchase |

---

## SAFE UNKNOWN

- Weighted conversion scoring per block — **not defined**
- A/B variant roles — **project-level**, not registry v1

---

*Conversion roles version: v1.*
