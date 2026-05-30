# Website Factory — Site Type Legal Mapping v2

**Версия:** v2  
**Область:** `workspaces/website-factory-reference-v1/legal/`  
**Архитектура:** [LEGAL-PACK-ARCHITECTURE-v1.md](LEGAL-PACK-ARCHITECTURE-v1.md)  
**Правила внедрения:** [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md)  
**Site types:** [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) — **8 типов, без добавлений**

**Статус:** documentation only — **не** юридическая экспертиза, **не** автоматическая проверка.

**Предшественник:** [SITE-TYPE-LEGAL-MAPPING-v1.md](../registry/SITE-TYPE-LEGAL-MAPPING-v1.md) — сохранён; v2 расширяет матрицу footer/consent и extension surface.

---

## Легенда

| Символ / термин | Значение |
|-----------------|----------|
| **Required** | Обязателен при production + условиях LEGAL-IMPLEMENTATION-RULES §1 |
| **Optional** | Рекомендуется по контексту; не блокирует базовую классификацию |
| **Conditional** | Зависит от subtree / public shell / tracking |
| **FUTURE** | Extension Pack — шаблон **не** в Core v1; human legal review |
| **—** | Не применимо для типа |

### Core documents (L1–L4)

| ID | Документ | URL |
|----|----------|-----|
| L1 | Политика конфиденциальности | `/privacy-policy/` |
| L2 | Согласие на обработку персональных данных | `/consent-personal-data/` |
| L3 | Пользовательское соглашение | `/user-agreement/` |
| L4 | Политика Cookie-файлов | `/cookie-files-policy/` |

### Канонический Consent text (формы)

Единственный допустимый HTML — см. [LEGAL-IMPLEMENTATION-RULES.md §4](LEGAL-IMPLEMENTATION-RULES.md):

```html
Я&nbsp;даю согласие на&nbsp;обработку персональных данных в&nbsp;соответствии с&nbsp;<a href="/consent-personal-data/" target="_blank">Согласием на&nbsp;обработку персональных данных</a> и&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy/" target="_blank">Политикой конфиденциальности</a>.
```

### Канонические footer links (production)

| Текст ссылки (= H1) | URL |
|---------------------|-----|
| Политика конфиденциальности | `/privacy-policy/` |
| Согласие на обработку персональных данных | `/consent-personal-data/` |
| Пользовательское соглашение | `/user-agreement/` |
| Политика Cookie-файлов | `/cookie-files-policy/` |

---

## LANDING

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **Required legal documents** | L1, L2, L3, L4 — при full landing + production + сбор ПДн |
| **Optional legal documents** | — |
| **Future legal expansion** | — |
| **Required footer links** | Все 4 (L1–L4) — production |
| **Required consent texts** | Consent Rule — на каждой форме сбора ПДн |
| **Notes** | PPC landing без форм и без production — legal pages не обязательны (LEGAL-IMPLEMENTATION-RULES §2). Эталон: `website-factory-reference-v1`. |

---

## PROMO

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **Required legal documents** | L1, L2, L3, L4 — full site + production |
| **Optional legal documents** | — |
| **Future legal expansion** | — |
| **Required footer links** | Все 4 (L1–L4) — production |
| **Required consent texts** | Consent Rule — contact / lead forms на money pages |
| **Notes** | Multi-page IA; cookie banner ссылается на L4. |

---

## CATALOG

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **Required legal documents** | L1, L2, L3, L4 — full site + production |
| **Optional legal documents** | — |
| **Future legal expansion** | — |
| **Required footer links** | Все 4 (L1–L4) — production |
| **Required consent texts** | Consent Rule — RFQ / request price / dealer inquiry forms |
| **Notes** | Нет checkout — ECOMMERCE Extension не требуется. Core Pack достаточен для v1 production. |

---

## ECOMMERCE

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **Required legal documents** | L1, L2, L3, L4 — full site + production + checkout |
| **Optional legal documents** | — |
| **Future legal expansion** | **ECOMMERCE EXTENSION:** E1 Public Offer, E2 Payment Rules, E3 Delivery Rules, E4 Return Policy |
| **Required footer links** | Все 4 (L1–L4) — production; Extension docs — **FUTURE** footer entries после charter |
| **Required consent texts** | Consent Rule — checkout guest forms, account registration, newsletter opt-in с ПДн |
| **Notes** | L3 ≠ оферта. Ecommerce production **may require** Extension beyond Core — HITL / legal review. |

---

## CORPORATE

| Поле | Значение |
|------|----------|
| **site_type_group** | CORE |
| **Required legal documents** | L1, L2, L3, L4 — baseline production corporate site |
| **Optional legal documents** | — |
| **Future legal expansion** | **CORPORATE CUSTOM:** partner agreements, portal terms, investor disclaimers, sector disclosures; **subtree:** ECOMMERCE / SAAS / MARKETPLACE extensions |
| **Required footer links** | Все 4 (L1–L4) — production baseline |
| **Required consent texts** | Consent Rule — все формы сбора ПДn по subtrees |
| **Notes** | Hybrid by design — legal mapping **per route group**; primary `site_type_code` не отменяет subtree extensions. |

---

## SAAS

| Поле | Значение |
|------|----------|
| **site_type_group** | EXTENDED |
| **Required legal documents** | L1, L2, L3, L4 — marketing site + signup + production |
| **Optional legal documents** | — |
| **Future legal expansion** | **SAAS EXTENSION:** S1 Subscription Terms, S2 AUP, S3 SLA, S4 DPA; refund/cancellation policy |
| **Required footer links** | Все 4 (L1–L4) — marketing shell production |
| **Required consent texts** | Consent Rule — signup, trial, billing contact forms |
| **Notes** | Billing UI без Subscription Terms — HITL. Mobile apps — **Mobile App Factory FUTURE**, out of scope. |

---

## WEB_APPLICATION

| Поле | Значение |
|------|----------|
| **site_type_group** | EXTENDED |
| **Required legal documents** | L1, L2 — при сборе ПДn; L3, L4 — **Conditional** (public marketing shell + tracking) |
| **Optional legal documents** | L3, L4 — minimal public login-only shell без marketing tracking |
| **Future legal expansion** | Operational ToS, admin/access policy, data retention policy, sector compliance addenda |
| **Required footer links** | Все 4 — если public marketing shell в production; иначе L1/L2 links minimum где applicable |
| **Required consent texts** | Consent Rule — registration, profile, support forms с ПДn |
| **Notes** | Authenticated app legal surface часто отделена от marketing Core Pack. Classify public vs app routes separately. |

---

## MARKETPLACE

| Поле | Значение |
|------|----------|
| **site_type_group** | EXTENDED |
| **Required legal documents** | L1, L2, L3, L4 — platform marketing + accounts + production |
| **Optional legal documents** | — |
| **Future legal expansion** | **MARKETPLACE EXTENSION:** M1 Seller Agreement, M2 Buyer Rules, M3 Dispute Resolution, M4 Marketplace Terms; escrow, prohibited items, review policy |
| **Required footer links** | Все 4 (L1–L4) — production |
| **Required consent texts** | Consent Rule — buyer/seller registration, contact forms |
| **Notes** | Highest legal expansion surface. Core Pack v1 = baseline only. |

---

## Сводная матрица

### Legal documents by site type

| site_type_code | L1 | L2 | L3 | L4 | Extension FUTURE |
|----------------|:--:|:--:|:--:|:--:|:----------------:|
| **LANDING** | Req* | Req* | Req* | Req* | — |
| **PROMO** | Req* | Req* | Req* | Req* | — |
| **CATALOG** | Req* | Req* | Req* | Req* | — |
| **ECOMMERCE** | Req* | Req* | Req* | Req* | **Yes** |
| **CORPORATE** | Req* | Req* | Req* | Req* | **Yes** |
| **SAAS** | Req* | Req* | Req* | Req* | **Yes** |
| **WEB_APPLICATION** | Req† | Req† | Cond‡ | Cond‡ | **Yes** |
| **MARKETPLACE** | Req* | Req* | Req* | Req* | **Yes** |

\* При LEGAL-IMPLEMENTATION-RULES §1 (full site/landing, production, сбор ПДn).  
† При сборе ПДn в app/public shell.  
‡ Conditional — public marketing shell + tracking.

### Footer links by site type (production)

| site_type_code | L1 link | L2 link | L3 link | L4 link |
|----------------|:-------:|:-------:|:-------:|:-------:|
| **LANDING** | ✓ | ✓ | ✓ | ✓ |
| **PROMO** | ✓ | ✓ | ✓ | ✓ |
| **CATALOG** | ✓ | ✓ | ✓ | ✓ |
| **ECOMMERCE** | ✓ | ✓ | ✓ | ✓ |
| **CORPORATE** | ✓ | ✓ | ✓ | ✓ |
| **SAAS** | ✓ | ✓ | ✓ | ✓ |
| **WEB_APPLICATION** | ✓† | ✓† | ✓‡ | ✓‡ |
| **MARKETPLACE** | ✓ | ✓ | ✓ | ✓ |

† Minimum where public pages exist. ‡ If marketing shell in production.

### Consent text by site type

| site_type_code | Consent Rule required when |
|----------------|----------------------------|
| **LANDING** | Lead form, callback, modal form |
| **PROMO** | Contact / lead forms on any page |
| **CATALOG** | RFQ, price request, dealer inquiry forms |
| **ECOMMERCE** | Checkout, registration, marketing opt-in with ПДn |
| **CORPORATE** | Any ПДn collection form across subtrees |
| **SAAS** | Signup, trial, billing contact forms |
| **WEB_APPLICATION** | Registration, profile, support ticket forms |
| **MARKETPLACE** | Buyer/seller registration, platform contact forms |

---

## Out of scope

| Factory | Status |
|---------|--------|
| **Mobile App Factory** | FUTURE separate factory — in-app privacy, store listings, native consent flows **не** покрываются данной матрицей |

---

## SAFE UNKNOWN

- Exhaustive industry compliance matrix — **не исчерпывающий**; final set — human legal review.
- Extension Pack footer link taxonomy — **не определён** до появления шаблонов.
- Automated legal page generation pipeline — **не заявлен** в v1.

---

*Legal mapping version: v2. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
