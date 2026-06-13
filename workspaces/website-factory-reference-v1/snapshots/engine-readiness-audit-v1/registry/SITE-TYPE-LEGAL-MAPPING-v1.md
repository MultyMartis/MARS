# Website Factory — Site Type Legal Mapping v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/registry/`  
**Legal Pack (канон):** `workspaces/website-factory-reference-v1/legal/`  
**Правила внедрения:** [../legal/LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md)

**Статус:** documentation only — **не** юридическая экспертиза, **не** автоматическая проверка.

> **Superseded:** Canonical site-type legal mapping is [legal/SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) (Legal Pack v1 FROZEN). This registry v1 file is retained for historical reference only — **do not delete**.

---

## Legal Pack v1 — базовые документы

| ID | Документ | Шаблон | URL |
|----|----------|--------|-----|
| **L1** | Политика конфиденциальности | `privacy-policy-template.md` | `/privacy-policy/` |
| **L2** | Согласие на обработку персональных данных | `consent-personal-data-template.md` | `/consent-personal-data/` |
| **L3** | Пользовательское соглашение | `user-agreement-template.md` | `/user-agreement/` |
| **L4** | Политика Cookie-файлов | `cookie-files-policy-template.md` | `/cookie-files-policy/` |

**Footer Rule (production):** все четыре ссылки обязательны в футере полных Factory-сборок — см. LEGAL-IMPLEMENTATION-RULES §3.

**Consent Rule (формы):** канонический HTML чекбокса — см. LEGAL-IMPLEMENTATION-RULES §4.

---

## Легенда mapping

| Категория | Значение |
|-----------|----------|
| **Required** | Обязателен для production-сборки данного типа (при наличии условий §1 LEGAL-IMPLEMENTATION-RULES). |
| **Optional** | Рекомендуется по контексту; не блокирует базовую классификацию. |
| **Not Required** | Не входит в стандартный Legal Pack v1 для типа; не генерировать без отдельного charter. |
| **FUTURE EXPANSION** | Планируемое расширение Legal Pack — **не** часть v1 templates; требует human legal review. |

---

## LANDING

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2, L3, L4 — при full landing + production + сбор ПДн (формы). |
| **Optional** | — |
| **Not Required** | E-commerce offer, seller agreement, SLA. |

**Примечания:** типичный case — lead form → L2 consent rule обязателен. PPC landing без форм и без production — legal pages **не обязательны** (LEGAL-IMPLEMENTATION-RULES §2).

---

## PROMO

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2, L3, L4 — full site + production. |
| **Optional** | — |
| **Not Required** | Public offer (оферта), return policy, seller terms. |

**Примечания:** contact forms на money pages → L2. Cookie banner/policy — L4.

---

## CATALOG

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2, L3, L4 — full site + production; RFQ/request forms → L2. |
| **Optional** | — |
| **Not Required** | Public offer, payment terms, delivery policy (нет checkout). |

**Примечания:** без cart/payment Legal Pack v1 достаточен для базового production.

---

## ECOMMERCE

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2, L3, L4 — full site + production + checkout. |
| **Optional** | — |
| **Not Required** (v1 templates) | — |
| **FUTURE EXPANSION** | **Публичная оферта** (distance selling); **Политика возврата и обмена**; **Условия доставки**; **Правила оплаты**; документы для B2B (договор поставки). |

**Примечания:** ECOMMERCE **может требовать** документы beyond Legal Pack v1 — помечать **FUTURE EXPANSION** до появления шаблонов и legal sign-off. Не подменять L3 «Пользовательским соглашением» полноценной офертой без юриста.

---

## CORPORATE

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2, L3, L4 — baseline для production corporate site. |
| **Optional** | — |
| **Not Required** | Зависит от subtrees (ecommerce subtree → см. ECOMMERCE FUTURE EXPANSION). |
| **FUTURE EXPANSION** | Partner agreement pages; employee portal terms; investor disclaimer; sector-specific disclosures. |

**Примечания:** hybrid site — legal mapping **per subtree**; primary type не отменяет требования ecommerce/marketplace subtrees.

---

## SAAS

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2, L3, L4 — marketing site + signup + production. |
| **Optional** | — |
| **Not Required** (v1 templates) | — |
| **FUTURE EXPANSION** | **SLA / uptime policy**; **Subscription terms** (условия подписки); **Acceptable Use Policy**; **DPA** (data processing agreement для B2B); **Refund/cancellation policy**; **API terms**. |

**Примечания:** SAAS **may require additional legal documents in future** — обязательно маркировать отдельным charter; billing UI без subscription terms — **HITL / legal review**.

---

## WEB_APPLICATION

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2 — при сборе ПДn; L3, L4 — если публичный web shell в production. |
| **Optional** | L3, L4 — для minimal public login page без marketing. |
| **Not Required** | Marketing-oriented cookie policy если нет tracking на public shell. |
| **FUTURE EXPANSION** | **Terms of service (operational)**; **Admin/access policy**; **Data retention policy**; sector compliance (152-FZ addenda, GDPR annexes). |

**Примечания:** authenticated app — legal surface часто **отделена** от marketing Legal Pack; classify public vs app routes separately.

---

## MARKETPLACE

| Категория | Документы |
|-----------|-----------|
| **Required** | L1, L2, L3, L4 — platform marketing + accounts + production. |
| **Optional** | — |
| **Not Required** (v1 templates) | — |
| **FUTURE EXPANSION** | **Seller agreement** (договор с продавцом); **Buyer protection policy**; **Platform commission terms**; **Dispute resolution policy**; **Escrow/payment intermediary terms**; **Prohibited items policy**; **Rating/review policy**. |

**Примечания:** MARKETPLACE **may require additional legal documents in future** — highest legal expansion surface; Legal Pack v1 = **baseline only**.

---

## Сводная таблица — Legal Pack v1

| site_type_code | L1 Privacy | L2 Consent | L3 User Agreement | L4 Cookie | FUTURE EXPANSION |
|----------------|------------|------------|-------------------|-----------|------------------|
| **LANDING** | Required* | Required* | Required* | Required* | — |
| **PROMO** | Required* | Required* | Required* | Required* | — |
| **CATALOG** | Required* | Required* | Required* | Required* | — |
| **ECOMMERCE** | Required* | Required* | Required* | Required* | **Yes** — offer, returns, delivery, payment |
| **CORPORATE** | Required* | Required* | Required* | Required* | **Yes** — partner, portal, sector |
| **SAAS** | Required* | Required* | Required* | Required* | **Yes** — SLA, subscription, AUP, DPA |
| **WEB_APPLICATION** | Required† | Required† | Optional‡ | Optional‡ | **Yes** — operational ToS, retention |
| **MARKETPLACE** | Required* | Required* | Required* | Required* | **Yes** — seller, escrow, dispute |

\* При выполнении условий LEGAL-IMPLEMENTATION-RULES §1 (full site/landing, production, сбор ПДн).  
† При сборе ПДn в app/public shell.  
‡ Зависит от наличия публичного marketing shell и tracking.

---

## SAFE UNKNOWN

- Полный перечень FUTURE EXPANSION документов по отраслям — **не исчерпывающий**; финальный набор — **human legal review**.
- Автоматическая генерация legal pages — **не** заявлена в v1 registry.
- Cross-border (EU/US) compliance variants — **не** в Legal Pack v1.

---

*Legal mapping version: v1.*
