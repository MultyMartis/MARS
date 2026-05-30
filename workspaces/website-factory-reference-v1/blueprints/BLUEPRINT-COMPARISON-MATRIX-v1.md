# Website Factory — Blueprint Comparison Matrix v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/blueprints/`  
**Статус:** сравнительная матрица Core Type Blueprints  
**Связь:** [BLUEPRINT-SYSTEM-v1.md](BLUEPRINT-SYSTEM-v1.md), [SITE-TYPE-MATRIX-v1.md](../registry/SITE-TYPE-MATRIX-v1.md)

**Scope:** Core Types only — `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE`.

---

## Легенда

| Значение | Смысл |
|----------|-------|
| **—** | Не применимо / отсутствует |
| **Low** | Минимальный уровень |
| **Medium** | Умеренный |
| **High** | Существенный |
| **Critical** | Primary или co-primary для типа |

---

## Матрица

| Dimension | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|-----------|---------|-------|---------|-----------|-----------|
| **Pages** | 1 (+ legal) | 5–15 | 20–500+ | 50–10k+ | 30–500+ |
| **SEO** | Low | **High** | **High** | **High** | **High** |
| **Conversion** | Single lead/action | Soft multi-page | RFQ / contact | Purchase funnel | Segmented multi-audience |
| **Legal (Core L1–L4)** | Required* | Required* | Required* | Required* | Required* |
| **Legal Extension** | — | — | — | **FUTURE** (E1–E4) | **FUTURE** (custom + subtrees) |
| **Catalog** | — | — | **Critical** | **Critical** | Optional subtree |
| **Cart** | — | — | **— (excluded)** | **Critical** | Optional subtree |
| **Checkout** | — | — | **— (excluded)** | **Critical** | Optional subtree |
| **Payment** | — | — | **— (excluded)** | **Critical** | Optional subtree |
| **Custom functionality** | Low | Low | Medium | Medium | **High** |
| **Integrations** | Low | Low | Medium | High | **High** |
| **Complexity** | **Low** | Medium | High | High | **High** |

\* При LEGAL-IMPLEMENTATION-RULES §1 (full site/landing, production, сбор ПДн).

---

## Pages — детализация

| site_type_code | Primary page model | Legal pages | Utility pages |
|----------------|-------------------|-------------|---------------|
| **LANDING** | Single `/` | L1–L4 (production) | thank-you (opt) |
| **PROMO** | Hub home + services + about + contacts | L1–L4 | blog/cases (opt) |
| **CATALOG** | Category tree + PLP + PDP | L1–L4 | search, faq |
| **ECOMMERCE** | Shop + PLP + PDP + cart + checkout | L1–L4 | account, returns, delivery |
| **CORPORATE** | Multi-audience hubs + solutions | L1–L4 | partners, careers, newsroom, subtrees |

---

## SEO — детализация

| site_type_code | Priority | Primary SEO mode |
|----------------|----------|------------------|
| **LANDING** | Low | Single-page / PPC alignment |
| **PROMO** | High | Brand + service intent |
| **CATALOG** | High | Category + PDP long-tail |
| **ECOMMERCE** | High | Transactional catalog + PDP |
| **CORPORATE** | High | Multi-audience hub-and-spoke |

---

## Conversion — детализация

| site_type_code | Primary conversion | CTA style |
|----------------|-------------------|-----------|
| **LANDING** | Lead / single action | One primary CTA, sticky mobile |
| **PROMO** | Contact / contextual lead | Soft, per-page |
| **CATALOG** | RFQ / price request / dealer | Contact-led on PDP |
| **ECOMMERCE** | Completed purchase | Add-to-cart → checkout |
| **CORPORATE** | Segment-specific (sales, partner, careers) | Multiple primaries by audience |

---

## Legal — детализация

| site_type_code | Core Pack | Consent triggers | Extension |
|----------------|-----------|------------------|-----------|
| **LANDING** | L1–L4* | Lead form, callback | — |
| **PROMO** | L1–L4* | Contact/lead forms | — |
| **CATALOG** | L1–L4* | RFQ, dealer forms | — |
| **ECOMMERCE** | L1–L4* | Checkout, registration | E1–E4 FUTURE |
| **CORPORATE** | L1–L4* | All subtree forms | Custom + subtree FUTURE |

---

## Catalog / Cart / Checkout — жёсткие границы

| Capability | LANDING | PROMO | CATALOG | ECOMMERCE | CORPORATE |
|------------|:-------:|:-----:|:-------:|:---------:|:---------:|
| Category PLP | — | — | ✓ | ✓ | ○ subtree |
| PDP | — | — | ✓ | ✓ | ○ subtree |
| Filters / search | — | — | ✓ | ✓ | ○ subtree |
| **Cart** | ✗ | ✗ | **✗ mandatory** | ✓ | ○ subtree |
| **Checkout** | ✗ | ✗ | **✗ mandatory** | ✓ | ○ subtree |
| **Payment** | ✗ | ✗ | **✗ mandatory** | ✓ | ○ subtree |

✓ = in scope · ✗ = excluded · ○ = optional subtree (inherit child Blueprint)

---

## Custom functionality & complexity

| site_type_code | Custom logic | Typical integrations | Operator HITL |
|----------------|--------------|---------------------|---------------|
| **LANDING** | Minimal | Form endpoint, analytics | Low |
| **PROMO** | Minimal | CRM, maps | Low |
| **CATALOG** | Medium | PIM, search, RFQ routing | Medium |
| **ECOMMERCE** | Medium | Payment, shipping, OMS | Medium–High |
| **CORPORATE** | **High** | SSO, ATS, CRM, ERP, portals | **High** |

---

## Blueprint file index

| site_type_code | Blueprint |
|----------------|-----------|
| LANDING | [LANDING-BLUEPRINT-v1.md](LANDING-BLUEPRINT-v1.md) |
| PROMO | [PROMO-BLUEPRINT-v1.md](PROMO-BLUEPRINT-v1.md) |
| CATALOG | [CATALOG-BLUEPRINT-v1.md](CATALOG-BLUEPRINT-v1.md) |
| ECOMMERCE | [ECOMMERCE-BLUEPRINT-v1.md](ECOMMERCE-BLUEPRINT-v1.md) |
| CORPORATE | [CORPORATE-BLUEPRINT-v1.md](CORPORATE-BLUEPRINT-v1.md) |

---

## SAFE UNKNOWN

- Weighted scoring for Blueprint selection in hybrid projects — **operator judgment**
- Automated matrix validation — **not implemented**

---

*Comparison matrix version: v1.*
