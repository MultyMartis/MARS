# Website Factory — Site Type Registry v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/registry/`  
**Статус:** каноническая классификация Website Factory — **documentation only**  
**Не является:** runtime, автоматической валидацией, базой данных, генератором сайтов

---

## Назначение

Site Type Registry v1 — **первый классификационный слой** Website Factory. Все подсистемы (Legal Pack, SEO Pack, Design System, Block Registry, Information Architecture, Page Blueprints, workflows) **обязаны** ссылаться на `site_type_code` из этого реестра.

**Связанные документы:**

| Документ | Назначение |
|----------|------------|
| [SITE-TYPE-MATRIX-v1.md](SITE-TYPE-MATRIX-v1.md) | Сравнительная матрица |
| [../legal/SITE-TYPE-LEGAL-MAPPING-v2.md](../legal/SITE-TYPE-LEGAL-MAPPING-v2.md) | **Канон** — юридические требования (Legal Pack v1) |
| [SITE-TYPE-LEGAL-MAPPING-v1.md](SITE-TYPE-LEGAL-MAPPING-v1.md) | *Исторический* — superseded by legal v2 |
| [../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md](../seo-architecture/SITE-TYPE-SEO-MAPPING-v2.md) | **Канон** — SEO Architecture Layer v2 |
| [SITE-TYPE-SEO-MAPPING-v1.md](SITE-TYPE-SEO-MAPPING-v1.md) | *Исторический* — priority hints; superseded by seo-architecture/ |
| [../block-registry/BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) | **Канон** — `block_id` (29 ids) |
| [../block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md](../block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md) | **Канон** — site type × block matrix |
| [SITE-TYPE-BLOCK-MAPPING-v1.md](SITE-TYPE-BLOCK-MAPPING-v1.md) | *Исторический* — block roles; superseded by block-registry/ |
| [SITE-TYPE-IMPLEMENTATION-RULES-v1.md](SITE-TYPE-IMPLEMENTATION-RULES-v1.md) | Правила внедрения |
| [../legal/LEGAL-IMPLEMENTATION-RULES.md](../legal/LEGAL-IMPLEMENTATION-RULES.md) | Legal Pack — правила юридических страниц |

**Предшественник (не канон v1):** `projects/mars-website-factory/site-type-registry-v0.md` — отдельная таксономия; **не** смешивать идентификаторы v0 и v1 без явного charter.

---

## Таксономия v1

| Группа | Коды |
|--------|------|
| **Core Types** (production targets по умолчанию) | `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Extended Types** (требуют дополнительной архитектуры) | `SAAS`, `WEB_APPLICATION`, `MARKETPLACE` |

**Итого:** 8 типов. Дополнительные типы **запрещены** в v1.

---

## Core Types

### LANDING

| Поле | Значение |
|------|----------|
| **Code** | `LANDING` |
| **Name** | Продающая страница |
| **Description** | Одностраничный коммерческий актив, оптимизированный под быструю конверсию и платный трафик. Минимальная навигация, один основной оффер, линейная структура повествования. |
| **Primary goal** | Генерация лидов или целевое действие (заявка, звонок, регистрация) с одного URL. |
| **Typical page count** | 1 основная страница; опционально thank-you и юридические страницы. |
| **Typical conversion model** | Форма / callback / click-to-call; один primary CTA; sticky CTA на mobile. |
| **Typical traffic sources** | PPC (Яндекс.Директ, Google Ads), ретаргетинг, email/SMS-кампании, партнёрские ссылки. |
| **Included features** | Hero, benefits, process, social proof, FAQ, lead form, sticky CTA, legal footer, modal callback. |
| **Excluded features** | Многостраничная IA, каталог, корзина, checkout, личный кабинет, сложные фильтры, marketplace-логика. |
| **Notes** | Эталон reference workspace: `workspaces/website-factory-reference-v1/`. Для RU commercial landings — QA preset в `projects/mars-website-factory/ru-landing-qa-preset-v1.md`. |

---

### PROMO

| Поле | Значение |
|------|----------|
| **Code** | `PROMO` |
| **Name** | Промо-сайт |
| **Description** | Многостраничное представление компании: услуги, о компании, кейсы, контакты. Строит доверие и поддерживает органический поиск без полноценной e-commerce или кастомной бизнес-логики. |
| **Primary goal** | Узнаваемость бренда, доверие, навигация к ключевым услугам и контактным точкам. |
| **Typical page count** | 5–15 страниц (главная, услуги, о нас, кейсы/портfolio, контакты, юридические). |
| **Typical conversion model** | Мягкие и контекстные CTA (заявка, звонок, «узнать больше»); формы на money pages. |
| **Typical traffic sources** | Органический поиск, брендовые запросы, рефералы, локальный SEO, контекстная реклама на hub-страницы. |
| **Included features** | Многостраничная навигация, service pages, about, cases/portfolio, blog/news (опционально), contact, legal pack, schema для organization/local business. |
| **Excluded features** | Корзина, checkout, онлайн-оплата, подписки, личный кабинет с ролями, marketplace, operational dashboards. |
| **Notes** | Отличие от `LANDING`: multi-page и SEO-capable IA. Отличие от `CORPORATE`: нет кастомной бизнес-функциональности и enterprise-интеграций. |

---

### CATALOG

| Поле | Значение |
|------|----------|
| **Code** | `CATALOG` |
| **Name** | Виртуальный каталог |
| **Description** | Структурированный каталог товаров или услуг с категориями, карточками, фильтрами и поиском. Конверсия через запрос, звонок или переход к дилеру — **без** транзакции на сайте. |
| **Primary goal** | Discovery и сравнение; переход к RFQ, контакту или офлайн-покупке. |
| **Typical page count** | 20–500+ URL (категории, PLP, PDP, support, contacts, legal). |
| **Typical conversion model** | RFQ / «запросить цену» / «найти дилера» / click-to-call; **нет** add-to-cart. |
| **Typical traffic sources** | Органический поиск (категории, long-tail), контекст на PLP/PDP, прямой трафик на брендовые SKU. |
| **Included features** | Category tree, PLP, PDP, filters, search, spec tables, comparison, downloads, dealer locator (опционально), FAQ, contacts. |
| **Excluded features** | **Корзина. Checkout. Онлайн-оплата.** Личный кабинет покупателя. Подписки. |
| **Notes** | Явное ограничение v1: catalog-only commerce path. При появлении cart/checkout — reclassify → `ECOMMERCE`. Faceted URL policy — отдельный SEO addendum (FUTURE). |

---

### ECOMMERCE

| Поле | Значение |
|------|----------|
| **Code** | `ECOMMERCE` |
| **Name** | Интернет-магазин |
| **Description** | Полный цикл онлайн-продаж: каталог, корзина, оформление заказа, оплата и доставка. |
| **Primary goal** | Завершение покупки on-domain. |
| **Typical page count** | 50–10 000+ URL (каталог, PDP, cart, checkout, account, policies). |
| **Typical conversion model** | PLP → PDP → cart → checkout → payment confirmation; guest или account checkout. |
| **Typical traffic sources** | Органический (transactional queries), performance marketing, email (abandoned cart), маркетплейс-переливы (если есть). |
| **Included features** | Catalog, cart, checkout, payment integration, delivery options, order status, returns policy, reviews, account (buyer). |
| **Excluded features** | Multi-vendor seller onboarding (→ `MARKETPLACE`). B2B operational ERP UI (→ `WEB_APPLICATION`). |
| **Notes** | Legal Pack v1 покрывает базовые 4 документа; **FUTURE EXPANSION** — оферта, возвраты, доставка (см. Legal Mapping). Payment/shipping stack — **SAFE UNKNOWN** до charter проекта. |

---

### CORPORATE

| Поле | Значение |
|------|----------|
| **Code** | `CORPORATE` |
| **Name** | Корпоративный сайт |
| **Description** | Комбинирует модели promo, catalog и ecommerce-поддеревья с кастомной бизнес-функциональностью: партнёрские разделы, сервисы для сотрудников, интеграции с внутренними системами. |
| **Primary goal** | Комплексное цифровое представление организации с сегментированными аудиториями (клиенты, партнёры, сотрудники, инвесторы). |
| **Typical page count** | 30–500+ URL; часто несколько поддеревьев с разной IA. |
| **Typical conversion model** | Сегментированные primary CTA по аудитории; demo/sales contact; partner portal entry; careers ATS. |
| **Typical traffic sources** | Брендовый organic, direct, PR, partner referrals, recruitment, B2B research queries. |
| **Included features** | Multi-audience nav, solutions/industries hubs, careers, investor/newsroom, partner sections, employee services, integrations (CRM, ATS, SSO — по charter), legal pack, optional catalog/ecommerce subtrees. |
| **Excluded features** | Full SaaS product surface (→ `SAAS`). Pure operational app without marketing shell (→ `WEB_APPLICATION`). Multi-sided marketplace core (→ `MARKETPLACE`). |
| **Notes** | **Hybrid by design:** документировать **primary** `site_type_code` **per route group**. HITL обязателен при regulated disclosures и conflicting CTAs. |

---

## Extended Types

### SAAS

| Поле | Значение |
|------|----------|
| **Code** | `SAAS` |
| **Name** | SaaS-платформа |
| **Description** | Продукт как сервис: подписки, пользовательские аккаунты, биллинг, product-led growth surface. Marketing site + authenticated product — единая или связанная property. |
| **Primary goal** | Регистрация, активация, удержание подписчиков; conversion trial → paid. |
| **Typical page count** | 10–100+ marketing URLs + app routes (login, dashboard, settings, billing). |
| **Typical conversion model** | Signup / trial → onboarding → subscription upgrade; in-app billing. |
| **Typical traffic sources** | Organic (product keywords), content marketing, PLG virality, paid acquisition, app store (web companion only — mobile apps **OUT OF SCOPE**). |
| **Included features** | Pricing tiers, signup/login, account management, subscription billing UI, product dashboards (marketing-facing), docs/help center, status page (optional). |
| **Excluded features** | Native mobile apps (Mobile App Factory — FUTURE). Multi-vendor marketplace. Heavy custom ERP (→ `WEB_APPLICATION`). |
| **Notes** | Extended Type — требует architecture charter beyond Core Factory defaults. Legal **FUTURE EXPANSION** (SLA, subscription terms). |

---

### WEB_APPLICATION

| Поле | Значение |
|------|----------|
| **Code** | `WEB_APPLICATION` |
| **Name** | Веб-приложение |
| **Description** | Бизнес-система с dashboards, management interfaces и operational workflows. **Не традиционный маркетинговый сайт** — primary value в authenticated task completion. |
| **Primary goal** | Выполнение операционных задач пользователем (управление, отчёты, workflows). |
| **Typical page count** | Мало публичных URL; основной объём — app screens (10–200+ views/routes). |
| **Typical conversion model** | Login → task completion; onboarding wizard; role-based access. |
| **Typical traffic sources** | Direct/bookmark, email notifications, SSO redirects, internal links — **не** SEO-first. |
| **Included features** | Auth, RBAC, dashboards, data tables, forms/workflows, notifications, admin panels, API integrations. |
| **Excluded features** | SEO landing programs, PPC-oriented single-page funnels, catalog commerce as primary surface. |
| **Notes** | Явно **not a traditional website**. Website Factory v1 blocks/SEO defaults **не применяются** без отдельного charter. Marketing shell (если есть) — classify subtree separately (`PROMO` / `LANDING`). |

---

### MARKETPLACE

| Поле | Значение |
|------|----------|
| **Code** | `MARKETPLACE` |
| **Name** | Маркетплейс |
| **Description** | Платформа-посредник: множество продавцов, множество покупателей, escrow/commission logic, seller onboarding. |
| **Primary goal** | Match supply and demand; transaction facilitation; platform take rate. |
| **Typical page count** | 100–100 000+ URL (listings, seller stores, categories, checkout, dispute flows). |
| **Typical conversion model** | Browse → listing → purchase; seller signup → listing publish; two-sided activation loops. |
| **Typical traffic sources** | Organic (listing long-tail), paid on categories, seller-driven traffic, brand/direct for platform. |
| **Included features** | Multi-seller catalog, seller accounts, buyer accounts, cart/checkout, payments split, reviews/ratings, dispute resolution UI, commission rules. |
| **Excluded features** | Single-vendor ecommerce simplification (→ `ECOMMERCE`). Pure SaaS without marketplace (→ `SAAS`). |
| **Notes** | Extended Type — highest complexity. Legal **FUTURE EXPANSION** (seller agreement, platform terms, escrow). Website Factory v1 — **classification and mapping only**; full production patterns **not** in Core scope. |

---

## Идентификаторы

| Поле | Формат |
|------|--------|
| **site_type_code** | UPPER_SNAKE_CASE — стабильный ключ (`LANDING`, `PROMO`, …) |
| **site_type_group** | `CORE` \| `EXTENDED` |

---

## SAFE UNKNOWN

- Machine-readable export (JSON Schema, YAML) для v1 — **не определён**; канон — Markdown.
- Industry-specific compliance (медицина, финансы, gambling) — **не закодирован** exhaustively; escalate HITL.
- Отношение v1 ↔ v0 registry при миграции legacy projects — **требует human charter** per project.

---

*Registry version: v1. Canonical location: `workspaces/website-factory-reference-v1/registry/`.*
