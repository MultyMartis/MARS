# REPORT — RV-01 PRODUCTION VOCABULARY RESEARCH

## Executive Summary

Исследование показывает, что рынок уже давно пришёл не к одной «плоской» номенклатуре, а к устойчивому набору уровней: **site type**, **page type**, **content/listing type**, **section/block/component**, **commercial pattern**, **trust pattern** и **SEO surface**. Это видно по тому, как Shopify разделяет **templates → sections → blocks**, Webflow — **CMS Collections / page templates / components**, WordPress — **pages / posts / templates / taxonomies**, а enterprise design systems — **components** и **patterns** как отдельные сущности. citeturn18search16turn18search0turn18search10turn10view7turn12view6turn7search16turn10view9

Главный вывод для Foundry: **Production Vocabulary нельзя строить только из локальных терминов вроде “landing”, “hero” или “FAQ”**. Канон рынка устроен иерархически. На верхнем уровне повторяются классы сайтов и страниц, ниже — повторяемые блоки, ещё ниже — коммерческие и trust-паттерны. Именно такое разделение поддерживают и builders, и CMS, и design systems, и поисковые экосистемы. citeturn10view1turn10view2turn12view4turn17view2turn10view9turn10view10turn10view11

По мировой практике в **core canon** без споров входят: landing/campaign, corporate/business, service business, ecommerce, catalog/B2B catalog, SaaS/product marketing, media/blog/publisher, directory/listings, manufacturer/industrial, healthcare/practice, education/course. На следующем уровне — real estate, restaurant/hospitality, nonprofit, event, community/membership, portfolio/personal. Marketplace — реальный класс, но он заметно более специализирован и не должен размывать ядро vocabulary для первого прохода. citeturn11view4turn11view7turn12view3turn12view4turn12view5turn9search3turn22search3turn22search5turn23search9

По page vocabulary рынок устойчиво повторяет: homepage, landing, about, contact, service, product, category/collection, blog listing, blog article, FAQ, case study, pricing, search results, resources/pillar, comparison/review, event, registration/confirmation, login/account, policy pages, 404/error и location/branch pages. Это не теоретический список: он буквально отражён в page types HubSpot, шаблонах Shopify, модели WordPress pages/posts և Google Search surfaces. citeturn12view4turn17view0turn17view2turn12view6turn20view11turn20view12

Для Block Vocabulary ядро состоит не из «красивых» маркетинговых секций, а из повторяемых primitives: header/navigation, hero, CTA/button, text/content section, cards/lists/grids, forms, footer, search, breadcrumbs, filters/sort, pagination, detail/specs sections. FAQ/accordion, reviews, logo strip, feature grid, pricing, comparison, process steps, related items и sticky CTA — это уже **common**, а before/after slider, countdown, stock counter, quick order list, calculator/configurator — **rare** и должны быть вынесены за пределы minimal canon. citeturn10view9turn10view10turn10view12turn18search16turn17view0turn17view4turn20view6turn10view3

Для SEO-поверхностей важно не смешивать «тип страницы» и «SERP tactic». **Product pages, category/collection pages, article pages, service pages, branch/location pages, FAQ/help pages, case studies и comparison/review pages** — это реальные SEO surfaces. Но **FAQ rich results** Google де-факто снял: 8 мая 2026 добавлено уведомление о депрекации, а 12 июня 2026 документация по FAQ rich result была удалена, потому что этот feature больше не показывается в поиске. Аналогично ранее был убран How-to rich result. Поэтому FAQ должен остаться в контентном canon, но не как ставка на SERP-расширение. citeturn20view10turn20view11turn20view12turn16view0turn16view2turn16view3

С точки зрения Foundry это означает следующее. На основании только пользовательского брифа нельзя безопасно пометить почти ни один vocabulary element как **Already Exists**. Корректная оценка сейчас — **provisional**: то, что уже названо в брифе, — **Partial**; то, что отраслевой стандарт, но не названо, — **Missing**; то, что существует, но слишком специализировано для первого слоя канона, — **Future**. Это не слабость отчёта, а правильное архитектурное ограничение при отсутствии текущего дампа Registry. Основа для WF-R01 therefore — не inventing terms, а **нормализация существующих рыночных терминов в строгие registry families**. citeturn10view4turn18search16turn10view7turn12view4

## Industry Canon

### Industry Site Types

Ниже — канонический список site types, которые реально повторяются в builders, CMS ecosystems и отраслевых шаблонах. Оценка зрелости и распространённости — это синтез по тому, насколько класс является first-class citizen в платформах, темах, structured-content моделях и vertical tooling. citeturn11view4turn12view3turn12view4turn17view0turn10view8

| Тип сайта | Назначение, основные страницы и типичные блоки | Зрелость / распространённость | Канонический вердикт | FOUNDRY STATUS |
|---|---|---|---|---|
| Landing / Campaign | Одна цель: lead, signup, demo, sale. Типично: hero, CTA, proof, form, FAQ, removal of distractions. citeturn10view13turn10view14 | Очень зрелый, повсеместный | Core standard | Partial |
| Corporate / Business | Бренд, репутация, overview. Типично: Home, About, Contact, Services/Products, Team, Careers, Legal. Пользователи ожидают отдельные About и Contact страницы. citeturn12view6turn20view0turn20view1 | Очень зрелый, повсеместный | Core standard | Partial |
| Service Business | Продажа услуг, booking/consultation/quote. Типично: Service pages, Contact, Booking, FAQ, testimonials, credentials. Wix и Squarespace явно поддерживают forms/bookings/services/scheduling. citeturn10view1turn11view8turn20view12 | Очень зрелый, повсеместный | Core standard | Partial |
| Ecommerce Store | Каталог, товар, cart, checkout, policies. Shopify выделяет product, collection, cart, search, blogs; Google — merchant listing/product surfaces. citeturn17view0turn17view2turn20view10 | Очень зрелый, повсеместный | Core standard | Partial |
| Catalog / B2B Catalog | Большой ассортимент, поиск, фильтрация, often quote/self-service. Shopify collections, Adobe shared catalogs и B2B catalog features это подтверждают. citeturn17view1turn12view1turn19search16 | Очень зрелый в commerce-сегменте | Core standard | Partial |
| SaaS / Product Marketing | Demo, onboarding, pricing, feature communication, proof. Webflow SaaS templates специально акцентируют demo showcases, onboarding flows, pricing tables. citeturn12view5 | Очень зрелый | Core standard | Partial |
| Media / Blog / Publisher | Хронологический контент, sections, articles, archives, taxonomies. WordPress и Google Article docs делают этот класс базовым и системным. citeturn12view6turn12view7turn20view11 | Очень зрелый, повсеместный | Core standard | Partial |
| Directory / Listings | Списки сущностей: business listings, real estate, branches, members, jobs, locations. Webflow прямо использует directories, listings, branch locations и team directories как CMS use cases. citeturn10view8turn22search5turn22search2 | Зрелый, но не универсальный | Core standard | Partial |
| Manufacturer / Industrial | Capabilities, industries served, certifications, quote/inquiry, sometimes gated catalog. Wix выделяет Industrial, Webflow — manufacturing/industrial, Adobe/BigCommerce — B2B self-service и manufacturer commerce. citeturn11view4turn9search7turn20view16turn12view2 | Зрелый vertical standard | Core standard | Partial |
| Healthcare / Practice | Услуги, доверие, credential-heavy presentation, booking/contact, location/hours. Squarespace explicitly frames health sites around credibility, care and expertise. citeturn11view7turn20view13turn20view14 | Зрелый vertical standard | Core standard | Partial |
| Education / Course / School | Programs/courses, instructors, admissions/enrollment, schedules/resources. Wix and HubSpot expose education as a first-class business category. citeturn11view4turn12view4 | Зрелый vertical standard | Core standard | Partial |
| Auto / Dealership | Inventory listings, model detail pages, filters, financing/contact. Shopify includes Auto as a theme industry; Google has vehicle listing structured data for dealerships. citeturn10view3turn22search1turn22search7 | Зрелый vertical standard | Core standard | Partial |
| Real Estate | Property listings, filters, location data, agent pages. HubSpot exposes real estate themes; Webflow uses real estate listings as a CMS/listings use case. citeturn12view3turn12view4turn10view8turn22search2 | Зрелый vertical standard | Standard, но не в minimal core | Missing |
| Restaurant / Hospitality | Menus, reservations, locations, hours, specials, events. Squarespace and Wix expose restaurant-specific templates and reservation/menu tooling. citeturn11view4turn22search0turn22search3turn22search18 | Зрелый vertical standard | Standard, но не в minimal core | Missing |
| Nonprofit / Advocacy | Mission, donations, campaigns, programs, impact stories. HubSpot и Squarespace выделяют nonprofits/charities как отдельный класс. citeturn12view3turn12view4turn11view9 | Зрелый vertical standard | Standard, но не в minimal core | Missing |
| Event / Conference | Agenda, speakers, tickets/registration, venue, sponsors. HubSpot has event page/business types; Squarespace has events & experiences. citeturn12view4turn11view9 | Зрелый, но контекстный | Common standard | Missing |
| Community / Membership | Member content, gated content, profiles, events, subscriptions. Squarespace explicitly exposes content & memberships and community groups. citeturn11view8turn10view2 | Зрелый, но не universal | Common standard | Missing |
| Portfolio / Personal Brand | Showcase work, bio, services, contact. Squarespace and Wix both expose personal/portfolio as a primary class. citeturn10view2turn11view4 | Очень зрелый | Common standard | Missing |
| Marketplace | Two-sided supply/demand system, listings + transaction/lead workflow. Реальный класс, но builders чаще показывают его как examples/community patterns, а не как глубоко first-class native model. citeturn23search9turn23search3turn17view0 | Реален, но более специализирован | Specialized standard, не minimal core | Future |

**Вывод по site types.** Для Foundry minimal canon должен включать не все возможные вертикали, а **ядро из повторяемых классов**: Landing, Corporate, Service Business, Ecommerce, Catalog/B2B Catalog, SaaS, Media/Publisher, Directory/Listings, Manufacturer, Healthcare, Education, Auto. Остальные — второй слой Expansion. Это соответствует и builder taxonomy, и CMS modeling practice. citeturn11view4turn12view4turn17view0turn10view8

### Industry Page Types

Стандарт page vocabulary подтверждается сразу несколькими системами: HubSpot фиксирует page types явно; Shopify — через default templates; WordPress — через pages/posts/archives/templates; NN/g подтверждает About/Contact как ожидаемые пользователями страницы. citeturn12view4turn17view0turn17view2turn12view6turn20view0turn20view1

| Тип страницы | Роль в каноне | Где это стандарт | Канонический вердикт | FOUNDRY STATUS |
|---|---|---|---|---|
| Homepage | Входная страница бренда или сайта | HubSpot, WordPress, corporate/ecommerce IA. citeturn12view4turn12view6turn20view3 | Core standard | Partial |
| Landing / Campaign | Трафик-specific conversion page | HubSpot, Unbounce, HubSpot best practices. citeturn12view4turn10view13turn10view14 | Core standard | Partial |
| About | Репутация, purpose, trust | NN/g, WordPress, HubSpot. citeturn20view1turn12view6turn12view4 | Core standard | Partial |
| Contact | Канал связи, location, phone/email/form | NN/g, WordPress, HubSpot. citeturn20view0turn12view6turn12view4 | Core standard | Partial |
| Service | Детальная страница услуги | HubSpot Services, service-business practice. citeturn12view4turn20view13 | Core standard | Partial |
| Product | Детальная товарная страница | Shopify product template, Google Product/Merchant listing. citeturn17view0turn20view10turn14search6 | Core standard | Partial |
| Category / Collection | Листинг группы товаров/сущностей | Shopify collections, Baymard category page. citeturn17view1turn10view5 | Core standard | Partial |
| FAQ | Ответы на типовые вопросы | HubSpot page type, FAQ content pattern. citeturn12view4turn20view8 | Core standard как content page | Partial |
| Blog Listing | Архив/лента контента | HubSpot, Shopify blog pages, WordPress archives. citeturn12view4turn17view3turn12view7 | Core standard | Missing |
| Blog Article | Временной контент / article page | Shopify blog post, WordPress posts, Google Article. citeturn17view3turn12view6turn20view11 | Core standard | Partial |
| Case Study | Proof page для B2B/services | HubSpot case studies are first-class content objects. citeturn21view1turn21view0 | Core standard for commercial sites | Partial |
| Comparison / Review | Сравнение решений или editorial review | Common in commercial research; Google supports pros/cons only for editorial product review pages. citeturn14search2turn12view4 | Common standard | Partial |
| Pricing | Коммерческая страница выбора плана/модели | HubSpot page type, Webflow SaaS patterns. citeturn12view4turn12view5 | Core standard for SaaS/services | Missing |
| Resources / Pillar | Информационный hub/cluster root | HubSpot page types include Resources and Pillar. citeturn12view4 | Common standard | Missing |
| Search Results | Internal findability surface | Shopify search page, IA best practices. citeturn17view4turn10view4 | Core standard for content/catalog sites | Missing |
| Event | Dedicated event page | HubSpot page type. citeturn12view4 | Common standard | Missing |
| Registration / Confirmation | End-state and conversion workflow pages | HubSpot exposes both Registration and Confirmation. citeturn12view4 | Common standard | Missing |
| Login / Account | Authenticated access page | HubSpot page type; common for SaaS, B2B, membership. citeturn12view4turn20view16 | Common standard | Missing |
| Policy Pages | Returns, shipping, privacy, terms | Ecommerce trust and Merchant Center return policy logic depend on clear policy surfaces. citeturn5search6turn5search2turn17view2 | Standard supporting surface | Missing |
| Location / Branch | Local/geo page for office/store/clinic/branch | Webflow branch locations, Google LocalBusiness. citeturn10view8turn20view12 | Standard for local/multi-location | Missing |
| 404 / Error | Recovery page | Shopify and HubSpot both expose error templates/pages. citeturn17view2turn12view4 | Standard supporting surface | Missing |

**Вывод по page types.** Для Foundry критично не ограничиваться Home/Product/About/Contact. Современный canon рынка уже давно включает **pricing, case study, search results, blog listing, resources/pillar, policy, location, registration/confirmation** как полноценные page types, а не случайные исключения. citeturn12view4turn17view2turn21view1

## Vocabulary Registry Draft

### Industry Block Vocabulary

Стандарты builders и design systems сходятся в одном: page structure строится из модульных, переиспользуемых частей. GOV.UK, USWDS, Carbon и Atlassian говорят о reusable components; Shopify — о sections and blocks; Webflow — о reusable components. Это и должно лечь в основу Block Vocabulary. citeturn10view9turn10view10turn10view11turn10view12turn18search16turn18search10

#### Core

| Блок | Назначение | Когда обязателен | Вердикт | FOUNDRY STATUS |
|---|---|---|---|---|
| Header / Navigation | Основная навигация и orientation | Почти в любом multi-page сайте | Core | Missing |
| Hero | Первое смысловое сообщение страницы | На home, landing, service, SaaS, product-led pages | Core | Partial |
| Primary CTA / Button group | Запуск целевого действия | На любой коммерческой странице | Core | Partial |
| Content / Rich Text Section | Основной текстовый слой страницы | Почти везде | Core | Missing |
| Card / Grid / List | Сканируемое представление объектов | Listings, features, resources, team, posts | Core | Missing |
| Media block | Image/video/demo visualization | Home, landing, product, service, SaaS | Core | Missing |
| Form / Lead Form | Захват лида / заявки / контакта | Landing, contact, quote, demo, service | Core | Partial |
| Footer | Secondary nav, policies, contact, legal | Почти везде | Core | Missing |
| Search | Поиск по каталогу/сайту/директории | Обязателен на больших catalog/content/listing sites | Core context-dependent | Partial |
| Breadcrumbs | Понимание позиции в иерархии | Обязателен на hierarchical sites, category/product trees | Core context-dependent | Partial |
| Filters / Sort | Сужение длинных списков | Обязателен на catalog/listing/search-result pages | Core context-dependent | Partial |
| Pagination / Results count | Навигация по длинным спискам | Обязателен на long lists/search/filter results | Core context-dependent | Missing |
| Detail / Specs Section | Свойства товара/услуги/объекта | Product, service, listing detail | Core context-dependent | Missing |

Основание для core-списка: reusable components в GOV.UK/USWDS/Carbon/Atlassian, search/filter/listing patterns у Shopify/Baymard/MOJ, hierarchy cues через breadcrumbs. citeturn20view7turn20view8turn20view9turn10view12turn17view4turn10view5turn20view6

#### Common

| Блок | Назначение | Когда нужен чаще всего | Вердикт | FOUNDRY STATUS |
|---|---|---|---|---|
| FAQ / Accordion | Сжатие Q&A и вторичной информации | FAQ pages, service pages, product pages | Common | Partial |
| Testimonials / Reviews | Social proof | Landing, service, SaaS, ecommerce | Common | Partial |
| Trust bar / Logo strip | Быстрое доверие через logos/certs | B2B, SaaS, services, ecommerce | Common | Partial |
| Feature Grid | Структурный список преимуществ | SaaS, service, product, landing | Common | Partial |
| Pricing Table | Сравнение планов/пакетов | SaaS, subscriptions, services | Common | Missing |
| Comparison Table | Сопоставление опций | SaaS, editorial review, product/service comparison | Common | Partial |
| Process Steps | Пошаговый процесс работы | Services, B2B, healthcare, manufacturing | Common | Partial |
| Related Items | Продолжение пути пользователя | Product, article, case study, resources | Common | Missing |
| Team block | Доверие через people layer | Corporate, service, healthcare, agency | Common | Missing |
| Stats / KPIs | Quantified proof | B2B, SaaS, case studies, investor-like pages | Common | Missing |
| Contact details / Map | Локальность и доступность | Contact, branch, restaurant, healthcare | Common | Missing |
| Banner / Alert | Site-wide notice / state change | Gov, ecommerce, SaaS status, legal/update | Common | Missing |
| Sticky CTA / Sticky Header | Сохранение actions in view | Landing, product, mobile-heavy flows | Common, не universal | Partial |
| Timeline | Временная структура / roadmap / history | About, case study, process, project | Common, но не baseline | Partial |
| Map / Locator | Поиск филиала/точки/дилера | Local business, directory, healthcare, restaurant | Common vertical | Missing |

Основание: accordions/breadcrumbs/banners как system components, reviews/ratings/trust on commerce and service pages, feature/pricing/process patterns in SaaS and landing ecosystems. citeturn20view8turn20view7turn10view10turn20view5turn12view5turn21view1turn20view13

#### Rare

| Блок | Назначение | Канонический статус | FOUNDRY STATUS |
|---|---|---|---|
| Before / After Slider | Визуальное сравнение состояния | Реальный, но segment-specific | Future |
| Countdown Timer | Срочность / deadline | Тактический, не базовый vocabulary | Future |
| Stock Counter | Scarcity/availability cue | Реальный в ecommerce, но узкий | Future |
| Quick Order List | Быстрый B2B reorder | Важен для B2B catalog, не для общего ядра | Future |
| Calculator / Configurator | Price/fit estimation | Реальный, но compute-specific | Future |

Основание: Shopify themes explicitly expose before/after slider, countdown timer, stock counter, quick order list as filterable theme features, что показывает их реальность, но одновременно и их **не-базовый** характер по сравнению с headers/forms/navigation. citeturn10view3

### Commercial Patterns

CRO-практика в builders и research-источниках показывает, что устойчивые паттерны довольно узкие: не все красивые композиции являются стандартом. Настоящий canon — это то, что повторяется в high-converting landing pages, SaaS pages и ecommerce IA. citeturn10view13turn10view14turn12view5turn20view3turn20view4

| Паттерн | Что делает | Рыночный статус | FOUNDRY STATUS |
|---|---|---|---|
| Single-goal landing | Убирает конкурирующие действия и ведёт к одной цели | Industry standard | Missing |
| Message match | Сохраняет связность ad/query → landing | Industry standard для кампаний | Missing |
| Above-the-fold value proposition + CTA | Быстро объясняет value и следующий шаг | Industry standard | Missing |
| Problem → Solution → Proof → CTA | Самый устойчивый коммерческий нарратив | Industry standard | Partial |
| Social proof near CTA | Снимает недоверие в точке решения | Industry standard | Partial |
| Product / service in action | Визуализирует использование | Industry standard | Missing |
| Feature / pricing comparison | Помогает выбору между пакетами или решениями | Industry standard для SaaS и comparison-led flows | Partial |
| Step-by-step process | Декомпозирует сложную услугу или journey | Industry standard для services/B2B | Partial |
| Curated category paths / subcategory tiles | Упрощает discovery в ecommerce | Industry standard для catalogs | Missing |
| Related recommendations | Продлевает browsing path | Industry standard для commerce/content | Missing |
| Industry or use-case segmentation | Делит страницу по vertical/use case | Common B2B standard, не universal | Partial |
| Sticky CTA | Спорный, но широко используемый enhancement | Common, не canonical baseline | Partial |
| Before / After narrative | Сильный паттерн для beauty/health/repair/renovation | Real, but segment-specific | Partial |

Основание: HubSpot и Unbounce фиксируют one-goal landing, clear CTA, above-the-fold messaging, social proof and distraction removal; Webflow SaaS выделяет pricing/feature communication; Baymard показывает значение curated category navigation и улучшения product-finding. citeturn10view13turn10view14turn12view5turn10view5turn20view3turn20view4

### Trust Patterns

NN/g сводит trustworthiness к четырём долговечным факторам: **design quality, up-front disclosure, comprehensive/current content, connection to the rest of the web**. Дальше verticals уже добавляют свои доказательства: ratings, policies, credentials, compliance, case studies, logos, contactability. citeturn10view15

| Сегмент | Наиболее типовые trust elements | Что считать отраслевым стандартом | FOUNDRY STATUS |
|---|---|---|---|
| B2B | About transparency, direct contact, client logos, case studies with metrics, pricing/quote cues, compliance/security, team/expertise | **Case studies + logos + clear contact + security/compliance** — это основной стандарт доверия | Missing |
| B2C | Reviews, rating count, returns/shipping/payment clarity, visible contact, secure checkout cues | **Reviews + policy clarity + secure checkout signals** — отраслевой минимум | Partial / Missing |
| Manufacturing | Certifications, industries served, capabilities, process explanation, RFQ/quote CTA, dealer/shared catalog logic | **Capabilities + certifications + quote path + industry fit** — vertical standard | Missing |
| Services | Credentials, testimonials, care/professional authority, consultation/booking, contact/location | **Credentials + testimonials + easy contact/booking** — основной trust stack | Missing |
| Ecommerce | Reviews with counts, shipping&returns, policies, payment/security, availability, merchant/product data | **Reviews + returns/shipping + secure payment + policy visibility** — baseline standard | Missing |

Основание по B2B and services: users expect About information to be clear, authentic, transparent; Contact page should expose complete contact details; HubSpot case studies include customer logo, metrics, testimonials, body and CTA; health/practice sites need credentials, press features and testimonials. citeturn20view1turn20view0turn21view1turn20view13turn20view14

Основание по ecommerce: ratings without rating counts reduce trust; Google merchant listings use price, availability, shipping and return information; returns policy is modeled as structured merchant data; checkout trust is tied to visible security cues. citeturn20view5turn20view10turn5search6turn10view16turn20view17

Основание по manufacturing/B2B commerce: Adobe and BigCommerce center B2B around self-service portals, shared catalogs, custom pricing and company workflows; BigCommerce trust/compliance is formalized through trust center and ISO/NIST alignment. citeturn12view1turn19search16turn20view16turn20view15

### SEO Content Patterns

Для SEO-поверхностей канон задают не статьи про SEO, а сами поисковые и CMS ecosystem signals: Google structured data docs, merchant docs, local business docs, product docs, article docs, plus first-class page/content models in HubSpot, Shopify, WordPress and Webflow CMS. citeturn20view10turn20view11turn20view12turn12view4turn17view0turn12view6turn10view8

| SEO surface | Реальная рыночная роль | Статус | FOUNDRY STATUS |
|---|---|---|---|
| Product Pages | Основная SEO и commerce surface для товарного спроса; Google product/merchant docs поддерживают product-level markup | Industry standard | Partial |
| Category / Collection Pages | Масштабная посадка под broad-intent и browse intent; core in Shopify and Baymard | Industry standard | Partial |
| Service Pages | Основная коммерческая SEO surface для услуг | Industry standard | Partial |
| Location / City / Branch Pages | Local SEO and multi-location visibility; LocalBusiness supports hours, departments, reviews | Industry standard | Partial |
| Blog / Article Pages | Informational and editorial surface; Article markup supported | Industry standard | Missing |
| FAQ / Help Pages | FAQ remains a valid content surface, но не как bet on FAQ rich results anymore | Industry standard content surface, obsolete as rich-result tactic | Partial |
| Comparison / Editorial Review Pages | Реальная surface для research intent; pros/cons enhancement only for editorial product review pages | Common standard | Partial |
| Case Studies | SEO + commercial proof surface for B2B/services | Common standard | Missing |
| Resource / Pillar Pages | Hub-style cluster roots, especially in HubSpot ecosystems | Common standard | Missing |
| Search Results / Internal Search | Реальная findability surface, especially on large catalogs/content sites | Standard support surface | Missing |
| Vehicle Listing Pages | Vertical standard for dealership inventory | Specialized standard | Missing |
| Policy Pages | Returns/shipping/policies support trust, commerce eligibility and coverage | Standard support surface | Missing |

**Критично важные устаревания.**  
FAQ rich result больше не показывается в Google Search: 8 мая 2026 feature был де-прекейтнут, 12 июня 2026 документация удалена. How-to rich result documentation тоже была удалена ранее как deprecated. И ещё одно ограничение: product rich results поддерживают **single-product pages**, а не category pages или lists. Это означает, что Foundry должен хранить FAQ и category pages как content/page types, но не обещать под них устаревшие rich-result outcomes. citeturn16view0turn16view2turn16view3turn15view0

## Foundry Gap Analysis

С учётом только предоставленного брифа и без дампа существующего Foundry Registry корректно делать **provisional gap analysis**. Надёжная логика такая:  
**Partial** — элемент явно назван в брифе;  
**Missing** — элемент отраслевой стандарт, но не назван;  
**Future** — элемент реален, но слишком узок для первый волны канона;  
**Already Exists** — нельзя безопасно поставить почти нигде без доказательства из текущей registry-модели. Это ограничение данных, а не недостаток исследования. citeturn10view4turn18search16turn12view4

По семействам разрыв выглядит так:

| Семейство | Partial | Missing | Future | Комментарий |
|---|---:|---:|---:|---|
| Site Types | 13 | 6 | 1 | Ядро названо верно, но недостаёт real estate, restaurant, nonprofit, event, community, portfolio; marketplace лучше отнести в поздний слой |
| Page Types | 11 | 10 | 0 | Наиболее заметный пробел — blog listing, pricing, resources/pillar, search results, location, policy, state pages |
| Block Vocabulary | 14 | 13 | 5 | В примерах уже есть marketing-heavy blocks, но недостаёт structural primitives: header/nav, footer, cards/lists, pagination, map, team |
| Commercial Patterns | 7 | 5 | 0 | Нужна нормализация вокруг single-goal, message-match, proof-near-CTA, curated navigation |
| Trust Patterns | 1 | 12 | 0 | Самый большой пробел: trust canon пока выглядит как набор примеров, а не registry family |
| SEO Content Patterns | 6 | 6 | 0 | Нужно отделить content surfaces от устаревающих SERP tactics |

Эти числа — не “текущее состояние продукта”, а **safe inferred status from the brief only**. Они полезны тем, что показывают, где именно vocabulary уже “угадывает рынок”, а где ещё нет formal canon. Приоритетный пробел — не в exotic verticals, а в **missing structural language**: search results, policy pages, location pages, pricing pages, lists/grids/cards, pagination, related items, team, trust/certification primitives. citeturn12view4turn17view2turn20view6turn20view7turn21view1turn20view10

Есть и более глубокий gap. Сейчас в брифе рядом лежат сущности разных уровней: site types, page types, blocks, patterns и SEO surfaces. В индустрии это почти никогда не сваливается в один словарь. Shopify, Webflow, WordPress и design systems все подтверждают необходимость **registry families**, иначе vocabulary быстро становится неоднозначным: например, “Directory” — это site type, “Search Results” — page type, “Filters” — block, “Industry Segments” — commercial pattern, а “Location Pages” — SEO surface/page type intersection. citeturn18search16turn10view7turn12view6turn10view9turn10view10

Отдельный риск канона — переоценка модных или визуально ярких элементов. Shopify theme features показывает, что countdown, stock counter, quick order list и before/after slider существуют, но их существование не делает их ядром production vocabulary. Напротив, builders and design systems consistently center the banal but essential: templates, sections, blocks, lists, forms, search, navigation, breadcrumbs, pagination. Именно это и должно стать baseline canon. citeturn10view3turn18search16turn10view9turn20view6

## Recommendations For WF-R01

Для WF-R01 целесообразно зафиксировать не новые сущности, а **порядок нормализации уже существующей рыночной реальности**.

Первое. Принять **семейную структуру vocabulary** как hard rule:  
**Site Type → Page Type → Block → Commercial Pattern → Trust Pattern → SEO Surface**.  
Это самый важный архитектурный шаг, потому что именно он соответствует builders, CMS и design systems. Без него Registry неизбежно будет смешивать уровни абстракции. citeturn18search16turn10view7turn12view6turn10view9

Второе. Зафиксировать **minimal canon first**. Для Site Types — Landing, Corporate, Service Business, Ecommerce, Catalog/B2B Catalog, SaaS, Media/Publisher, Directory/Listings, Manufacturer, Healthcare, Education, Auto. Для Page Types — Homepage, Landing, About, Contact, Service, Product, Category/Collection, FAQ, Blog Listing, Blog Article, Case Study, Pricing, Search Results, Location, Policy, 404/Error. Для Blocks — header/nav, hero, CTA, content section, cards/list/grid, form, footer, search, breadcrumbs, filters, pagination, detail/specs, FAQ/accordion, reviews, trust bar, feature grid, pricing/comparison, process steps, related items. Всё остальное — expansion backlog. citeturn12view4turn17view0turn17view2turn10view8turn20view6turn20view7

Третье. Ввести **standard / common / specialized / obsolete** как отдельный registry attribute. Это позволит не спорить о существовании элемента, а аккуратно ранжировать его. Например:  
- **Standard**: Product, Category, Search Results, Breadcrumbs, FAQ/Accordion, Reviews, Pricing.  
- **Common**: Timeline, Industry Segments, Case Studies, Resource/Pillar.  
- **Specialized**: Vehicle Listing, Quick Order List, Calculator/Configurator, Marketplace.  
- **Obsolete/Declining as tactic**: FAQ rich result, How-to rich result. citeturn12view4turn20view10turn20view11turn16view0turn15view0

Четвёртое. Развести **page reality** и **SERP reality**. FAQ page, comparison page, category page и policy page должны жить в canon независимо от того, даёт ли Google под них расширенный сниппет. Это особенно важно после удаления FAQ rich result feature и How-to documentation. Иначе vocabulary будет ломаться при каждом поисковом изменении. citeturn16view0turn16view2turn15view0

Пятое. Сделать **trust canon** отдельным первоклассным слоем. Для коммерческого веба trust — не декоративное дополнение, а production primitive. Минимальный trust canon должен покрыть: About transparency, direct contact, credentials/certifications, testimonials/reviews, rating counts, logos, case studies with metrics, policy clarity, security/compliance, location/hours, booking/quote cues. citeturn10view15turn20view0turn20view1turn20view5turn20view13turn20view15

Шестое. Не canonize vertical exotica раньше времени. Marketplace, calculators, inventory widgets, countdowns, stock counters и niche modules имеют право на существование, но они не должны задавать язык системы раньше, чем будет стабилизирован structural canon. Это прямо следует из того, как builders выделяют sections/components versus feature add-ons. citeturn10view3turn18search16turn18search10

## Risks

Главный риск — **смешение уровней vocabulary**. Если site types, page types, blocks и patterns останутся в одном регистре без строгого разделения, система начнёт плодить двусмысленные сущности и конфликты классификации. Это противоречит тому, как рынок моделирует контент и UI. citeturn18search16turn10view7turn12view6

Второй риск — **перекос в маркетинговые секции при недомоделированной структуре**. Hero, CTA, testimonials и FAQ обычно вспоминаются первыми, но без navigation, search, filters, breadcrumbs, pagination, policies и search results Foundry vocabulary останется пригодным только для простых лендингов, а не для production-grade website factory. citeturn20view3turn20view4turn20view6turn20view7turn17view4

Третий риск — **путать SEO surface и search feature**. Product page или FAQ page — это устойчивые типы контента. FAQ rich result или How-to rich result — временные правила выдачи. После майско-июньских изменений Google по FAQ это особенно критично. citeturn16view0turn16view2turn15view0

Четвёртый риск — **переоценка exotic verticals** на старте WF-R01. Рынок действительно знает marketplace, calculators, quick-order B2B modules и vehicle listings, но builder/CMS reality показывает, что minimal canon должен начинаться с более базовых объектов и только потом расти в глубину. citeturn10view3turn22search1turn23search9

Пятый риск — **ложный статус Already Exists** без доступа к текущему Registry. Такой маркер создаст иллюзию зрелости там, где есть только устное совпадение терминов. Для архитекторского уровня это опаснее, чем аккуратный provisional status. citeturn10view4turn18search16

## SAFE UNKNOWN

Неизвестно текущее фактическое наполнение внутреннего Foundry Registry. Поэтому в этом отчёте **нельзя безопасно утверждать**, что какой-либо vocabulary element уже formalized внутри системы, если это не подтверждено отдельным артефактом Registry. По этой причине почти весь внутренний статус в отчёте — **provisional**. Это сознательное ограничение, чтобы не превратить gap analysis в guesswork. 

Неизвестно, как именно в Foundry сейчас различаются **site type**, **page type**, **template**, **blueprint**, **section/block** и **pattern**. Отчёт показывает, что рынок эти уровни различает, но не может утверждать, что Foundry уже делает это тем же способом. citeturn18search16turn10view7turn12view6turn10view9

Неизвестно, нужен ли Foundry в первой волне полный vertical coverage. Исследование показывает, что real estate, restaurant, nonprofit, community и event — реальные и устойчивые классы, но вопрос о том, включать ли их в **minimal canon** или вынести в **registry expansion**, зависит уже от внутреннего product scope, а не от отраслевой реальности. citeturn12view4turn22search3turn11view9

Неизвестно, насколько глубоко Foundry хочет моделировать **operational pages** — login, registration, confirmation, error, account, password. Рынок их признаёт как системные page types, но их приоритет для Foundry зависит от того, ограничивается ли canon маркетинговыми/публичными сайтами или стремится к более широкому production vocabulary. citeturn12view4turn17view2

Неизвестно, должен ли Foundry canon включать **structured-data-level terminology** как отдельный словарь или как свойства SEO surfaces. Исследование подтверждает важность Product, Article, LocalBusiness, policy and merchant data surfaces, но само решение о modeling depth — уже внутренний архитектурный выбор. citeturn20view10turn20view11turn20view12