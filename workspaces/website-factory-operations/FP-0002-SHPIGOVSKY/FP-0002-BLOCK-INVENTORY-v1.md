# FP-0002 — Block Inventory v1

**Document type:** Official Block Inventory (first release)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-11  
**Coordinator:** PER-0010 — Ольга Дягилева  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Visual source of truth:** PDF-макеты в `INCOMING/01_DESIGN/` (Figma отсутствует — **PROJECT DECISION**).  
**Home canonical:** Home v2 (`2026-06-11-home-v2/`); Home v1 — superseded для главной.

**Upstream inputs (read-only, не изменялись):**

| Input | Role |
|-------|------|
| FP-0002 DESIGN INTAKE AUDIT | Reusable Structure Audit, Template Discovery, Content Entities |
| FP-0002 HOME V2 INTAKE UPDATE | Актуальный порядок секций главной, превью генотипирования |
| FP-0002 PAGE INVENTORY v1 | Page ID, типы страниц, G-SERVICE, Missing Pages Register |

**Scope:** инвентаризация **уникальных визуальных блоков** по подтверждённым PDF. Одна секция на нескольких страницах = **один блок**. Missing pages (M-01…M-06) — **вне scope** v1.

**Out of scope (запреты charter):** Frontend Foundation, Design System, WordPress Architecture, ACF Architecture, Frontend Production Plan; определение grid, container, colors, typography.

---

# REPORT — FP-0002 BLOCK INVENTORY

**Git status (до работы):** ветка `mars/post-cycle8-live-tests`, up to date с `origin`. `INCOMING/01_DESIGN/` — **untracked** (`??`). Новый артефакт Block Inventory — **untracked**. Прочие изменения репозитория не затрагивались. Commit / push **не выполнялись**.

---

## 1. Executive Summary

Создан **первый официальный Block Inventory** проекта FP-0002 (Shpigovsky.ru).

| Метрика | Значение |
|---------|----------|
| Страниц в Page Inventory | **11** |
| Уникальных блоков (Block ID) | **40** |
| Групп классификации | **12** |
| Core Shared блоков | **7** |
| Shared блоков | **12** |
| Unique блоков | **21** |
| Подтверждённых вариантов (variant families) | **4** (Hero, Page Hero context, CTA, Service template depth) |
| Missing-page блоки (вне v1) | **6** (M-01…M-06) |

**Ключевые выводы:**

- Сайт **компонентный**: ~20+ повторяемых зон (Design Intake Audit) сведены в **40 именованных блоков**; **19** из них Core Shared или Shared, **21** — page-role Unique.
- Сервисная ветка **PG-002 / PG-003 / PG-004** — **одна система G-SERVICE** с **3 уникальными контентными блоками** (каталог хаба, листинг подраздела, тело leaf-услуги).
- **Home v2** меняет **порядок** и **состав карточек** превью услуг, но **не вводит** новых типов блоков.
- Визуальный слой **достаточен для старта Frontend Foundation** с оговорками: mobile gap блога/статьи, отсутствующие экраны из навигации, UI states — SAFE UNKNOWN.

---

## 2. Block Inventory

### 2.1 Master table

| Block ID | Block Name | Block Type | First Appearance | Reused On (Page IDs) | Variant Count | Reuse Tier |
|----------|------------|------------|------------------|----------------------|---------------|------------|
| **FP-0002-BLK-001** | Header — Top Bar | Global Navigation | PG-002 | PG-001…PG-010 (все кроме PG-011) | 1 | Core Shared |
| **FP-0002-BLK-002** | Header — Main Navigation | Global Navigation | PG-002 | PG-001…PG-010 | 1 | Core Shared |
| **FP-0002-BLK-003** | Site Footer | Global Footer | PG-001 | PG-001…PG-010 | 1 | Core Shared |
| **FP-0002-BLK-004** | Mobile Sticky CTA Bar | Global Navigation | PG-001 (mob) | PG-001…PG-010 (mobile PDF) | 1 | Core Shared |
| **FP-0002-BLK-005** | Breadcrumbs | Navigation | PG-002 | PG-002…PG-010 (не PG-001, PG-011) | 1 | Core Shared |
| **FP-0002-BLK-006** | In-Page Anchor Navigation | Navigation | PG-002 | PG-002, PG-003, PG-004, PG-005 | 1 | Shared |
| **FP-0002-BLK-007** | Page Hero | Hero | PG-001 | PG-001, PG-002…PG-005, PG-008 | **4** | Core Shared |
| **FP-0002-BLK-008** | 404 Error Content | System | PG-011 | PG-011 | 1 | Unique |
| **FP-0002-BLK-009** | UTP Value Cards | Content | PG-001 | PG-001 | 1 | Unique |
| **FP-0002-BLK-010** | Home Services Preview Grid | Service | PG-001 | PG-001 | 1 | Unique |
| **FP-0002-BLK-011** | Service Catalog Category Grid | Service | PG-002 | PG-002 | 1 | Unique |
| **FP-0002-BLK-012** | Service Section Body | Service | PG-003 | PG-003 | 1 | Unique |
| **FP-0002-BLK-013** | Service Leaf Body | Service | PG-004 | PG-004 | 1 | Unique |
| **FP-0002-BLK-014** | Feature Cards «Нас выбирают» | Content | PG-001 | PG-001, PG-002 | 1 | Shared |
| **FP-0002-BLK-015** | Reviews Preview | Review | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-005 | 1 | Shared |
| **FP-0002-BLK-016** | Reviews Archive Listing | Review | PG-007 | PG-007 | 1 | Unique |
| **FP-0002-BLK-017** | Pagination | System | PG-007 | PG-007, PG-008 | 1 | Shared |
| **FP-0002-BLK-018** | Rehabilitation Steps (01–04) | Content | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-006, PG-007 | 1 | Shared |
| **FP-0002-BLK-019** | Guest Visit CTA Section | CTA | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-005, PG-008, PG-009 | 1 | Shared |
| **FP-0002-BLK-020** | Program Four Directions | Service | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-005 | 1 | Shared |
| **FP-0002-BLK-021** | Genotyping Detail Section | Service | PG-001 | PG-001 | 1 | Unique |
| **FP-0002-BLK-022** | Expert Opinion | Content | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-005, PG-008 | 1 | Shared |
| **FP-0002-BLK-023** | Comfort · Privacy · Care | Content | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-005 | 1 | Shared |
| **FP-0002-BLK-024** | Video Section | Content | PG-001 | PG-001 | 1 | Unique |
| **FP-0002-BLK-025** | Inline Consultation CTA | CTA | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-005, PG-008 | 1 | Core Shared |
| **FP-0002-BLK-026** | Specialists Cards Grid | Specialist | PG-001 | PG-001, PG-002, PG-003, PG-004, PG-005 | 1 | Shared |
| **FP-0002-BLK-027** | Articles Preview (Home) | Article | PG-001 | PG-001 | 1 | Unique |
| **FP-0002-BLK-028** | Blog Archive Cards Grid | Article | PG-008 | PG-008 | 1 | Unique |
| **FP-0002-BLK-029** | Article Table of Contents | Article | PG-009 | PG-009 | 1 | Unique |
| **FP-0002-BLK-030** | Article Long-Read Body | Article | PG-009 | PG-009 | 1 | Unique |
| **FP-0002-BLK-031** | Article Author Meta | Article | PG-009 | PG-009 | 1 | Unique |
| **FP-0002-BLK-032** | Article Sources / Bibliography | Article | PG-009 | PG-009 | 1 | Unique |
| **FP-0002-BLK-033** | Related Articles | Article | PG-009 | PG-009 | 1 | Unique |
| **FP-0002-BLK-034** | FAQ Accordion | FAQ | PG-001 | PG-001, PG-002, PG-003, PG-004 | 1 | Shared |
| **FP-0002-BLK-035** | Contact Form «Остались вопросы» | Form | PG-001 | PG-001, PG-002, PG-003, PG-004 | 1 | Shared |
| **FP-0002-BLK-036** | About Narrative — «Кто мы» | About | PG-005 | PG-005 | 1 | Unique |
| **FP-0002-BLK-037** | About Narrative — «Наш Дом» | About | PG-005 | PG-005 | 1 | Unique |
| **FP-0002-BLK-038** | About Infrastructure | About | PG-005 | PG-005 | 1 | Unique |
| **FP-0002-BLK-039** | Contacts Locations | Contact | PG-006 | PG-006 | 1 | Unique |
| **FP-0002-BLK-040** | Legal Document Body | Legal | PG-010 | PG-010 | 1 | Unique |

### 2.2 Block type legend

| Block Type | Meaning in FP-0002 |
|------------|-------------------|
| Global Navigation | Header zones, mobile sticky bar |
| Global Footer | Site-wide footer |
| Navigation | Breadcrumbs, in-page anchors |
| Hero | Page-level hero family |
| Service | Услуги, программа, каталог, генотипирование |
| Content | Narrative, UTP, feature, video, expert opinion |
| Review | Отзывы (preview и archive) |
| Article | Статьи / блог |
| Specialist | Карточки специалистов |
| FAQ | Аккордеон вопросов |
| Form | Контактная форма |
| CTA | Призывы к действию (секции и inline) |
| About | Уникальный narrative «О центре» |
| Contact | Контакты и локации |
| Legal | Правовой текст |
| System | 404, пагинация |

### 2.3 Page → block composition map

Секции страницы **не** являются Block ID; ниже — **состав** подтверждённых блоков.

| Page ID | Blocks (scroll order, canonical) |
|---------|--------------------------------|
| **PG-001** Home v2 | 001, 002, 007ᴴ, 009, 022, 010, 014, 015, 018, 019, 020, 021, 023, 024, 026, 027, 034, 035, 003 + 004 (mob) |
| **PG-002** Service Hub | 001, 002, 005, 006, 007ˢ, 011, 014, 020, 018, 022, 023, 026, 015, 034, 035, 019, 003 + 004 |
| **PG-003** Service Section | 001, 002, 005, 006, 007ˢ, 012, 020, 018, 022, 023, 026, 015, 034, 035, 019, 003 + 004 |
| **PG-004** Service Leaf | 001, 002, 005, 006, 007ˢ, 013, 020, 018, 022, 023, 026, 015, 034, 035, 019, 003 + 004 |
| **PG-005** About | 001, 002, 005, 006, 007ˢ, 036, 037, 038, 020, 018, 022, 023, 026, 015, 019, 003 + 004 |
| **PG-006** Contacts | 001, 002, 005, 039, 018, 003 + 004 |
| **PG-007** Reviews | 001, 002, 005, 016, 018, 017, 003 + 004 |
| **PG-008** Blog Hub | 001, 002, 005, 007ᴮ, 028, 017, 022, 019, 025, 003 + 004 |
| **PG-009** Article | 001, 002, 005, 029, 030, 031, 032, 033, 019, 003 + 004 (desktop only; mobile — gap) |
| **PG-010** Legal | 001, 002, 005, 040, 003 + 004 |
| **PG-011** 404 | 008, 003 + 004 |

**Legend:** 007ᴴ = Hero variant Home · 007ˢ = Hero variant Service/About · 007ᴮ = Hero variant Blog

---

## 3. Block Classification

Классификация по **фактическому пакету**, не по шаблонному примеру.

### 3.1 Global Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-001 | Header — Top Bar |
| FP-0002-BLK-002 | Header — Main Navigation |
| FP-0002-BLK-003 | Site Footer |
| FP-0002-BLK-004 | Mobile Sticky CTA Bar |

### 3.2 Navigation Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-005 | Breadcrumbs |
| FP-0002-BLK-006 | In-Page Anchor Navigation |

### 3.3 Hero Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-007 | Page Hero *(family)* |

### 3.4 Service Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-010 | Home Services Preview Grid |
| FP-0002-BLK-011 | Service Catalog Category Grid |
| FP-0002-BLK-012 | Service Section Body |
| FP-0002-BLK-013 | Service Leaf Body |
| FP-0002-BLK-020 | Program Four Directions |
| FP-0002-BLK-021 | Genotyping Detail Section |

### 3.5 Content Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-009 | UTP Value Cards |
| FP-0002-BLK-014 | Feature Cards «Нас выбирают» |
| FP-0002-BLK-018 | Rehabilitation Steps (01–04) |
| FP-0002-BLK-022 | Expert Opinion |
| FP-0002-BLK-023 | Comfort · Privacy · Care |
| FP-0002-BLK-024 | Video Section |

### 3.6 Review Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-015 | Reviews Preview |
| FP-0002-BLK-016 | Reviews Archive Listing |

### 3.7 Article Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-027 | Articles Preview (Home) |
| FP-0002-BLK-028 | Blog Archive Cards Grid |
| FP-0002-BLK-029 | Article Table of Contents |
| FP-0002-BLK-030 | Article Long-Read Body |
| FP-0002-BLK-031 | Article Author Meta |
| FP-0002-BLK-032 | Article Sources / Bibliography |
| FP-0002-BLK-033 | Related Articles |

### 3.8 Specialist Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-026 | Specialists Cards Grid |

### 3.9 FAQ Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-034 | FAQ Accordion |

### 3.10 CTA Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-019 | Guest Visit CTA Section |
| FP-0002-BLK-025 | Inline Consultation CTA |

*Примечание:* кнопка «Заказать звонок» в BLK-001/002/004 — часть global chrome; отдельный modal-блок **не инвентаризирован** (M-06, SAFE UNKNOWN).

### 3.11 Form Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-035 | Contact Form «Остались вопросы» |

### 3.12 About Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-036 | About Narrative — «Кто мы» |
| FP-0002-BLK-037 | About Narrative — «Наш Дом» |
| FP-0002-BLK-038 | About Infrastructure |

### 3.13 Contact Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-039 | Contacts Locations |

### 3.14 Legal Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-040 | Legal Document Body |

### 3.15 System Blocks

| Block ID | Block Name |
|----------|------------|
| FP-0002-BLK-008 | 404 Error Content |
| FP-0002-BLK-017 | Pagination |

---

## 4. Reuse Analysis

### 4.1 Core Shared (массовое переиспользование, часть системы сайта)

| Block ID | Appearances | Role |
|----------|-------------|------|
| FP-0002-BLK-001 | 10 страниц | Top bar chrome |
| FP-0002-BLK-002 | 10 страниц | Primary nav |
| FP-0002-BLK-003 | 10 страниц | Footer |
| FP-0002-BLK-004 | 10 mobile PDF | Persistent mobile CTA |
| FP-0002-BLK-005 | 9 страниц | IA wayfinding |
| FP-0002-BLK-007 | 6+ контекстов | Hero family |
| FP-0002-BLK-025 | 6+ страниц | Conversion micro-CTA |

### 4.2 Shared (2+ страниц, не universal chrome)

| Block ID | Page count | Pages |
|----------|------------|-------|
| FP-0002-BLK-006 | 4 | PG-002, PG-003, PG-004, PG-005 |
| FP-0002-BLK-014 | 2 | PG-001, PG-002 |
| FP-0002-BLK-015 | 5 | PG-001…PG-005 (preview) |
| FP-0002-BLK-017 | 2 | PG-007, PG-008 |
| FP-0002-BLK-018 | 6 | PG-001…PG-004, PG-006, PG-007 |
| FP-0002-BLK-019 | 7 | PG-001…PG-005, PG-008, PG-009 |
| FP-0002-BLK-020 | 5 | PG-001…PG-005 |
| FP-0002-BLK-022 | 6 | PG-001…PG-005, PG-008 |
| FP-0002-BLK-023 | 5 | PG-001…PG-005 |
| FP-0002-BLK-026 | 5 | PG-001…PG-005 |
| FP-0002-BLK-034 | 4 | PG-001…PG-004 |
| FP-0002-BLK-035 | 4 | PG-001…PG-004 |

### 4.3 Unique (один тип страницы / один контекст)

| Block ID | Exclusive to |
|----------|--------------|
| FP-0002-BLK-008 | PG-011 |
| FP-0002-BLK-009 | PG-001 |
| FP-0002-BLK-010 | PG-001 |
| FP-0002-BLK-011 | PG-002 |
| FP-0002-BLK-012 | PG-003 |
| FP-0002-BLK-013 | PG-004 |
| FP-0002-BLK-016 | PG-007 |
| FP-0002-BLK-021 | PG-001 |
| FP-0002-BLK-024 | PG-001 |
| FP-0002-BLK-027 | PG-001 |
| FP-0002-BLK-028 | PG-008 |
| FP-0002-BLK-029…033 | PG-009 (5 блоков article single) |
| FP-0002-BLK-036…038 | PG-005 (3 about narrative) |
| FP-0002-BLK-039 | PG-006 |
| FP-0002-BLK-040 | PG-010 |

### 4.4 Reuse summary

| Tier | Count | % of inventory |
|------|-------|----------------|
| Core Shared | 7 | 18% |
| Shared | 12 | 30% |
| Unique | 21 | 52% |

**Вывод:** ~48% блоков переиспользуются (Core + Shared); при этом **scroll-каркас** услуг и главной собирается из **небольшого shared-ядра** (program, FAQ, form, specialists…) + **один IA-specific slot** на уровне услуги. Высокая доля Unique отражает **page-role blocks** (article single, about narrative, catalog levels), а не отсутствие системности.

---

## 5. Variant Analysis

Варианты фиксируются **только при подтверждении макетами**.

### 5.1 Page Hero (FP-0002-BLK-007) — 4 подтверждённых варианта

| Variant | Context | Confirmed on | Distinction (факт макета) |
|---------|---------|--------------|---------------------------|
| **Home Hero** | Landing | PG-001 (v2) | Hero + буллеты УТП; в v2 зафиксирован **дубль** одного буллета (артефакт — SAFE UNKNOWN) |
| **Service Hero** | G-SERVICE + About | PG-002, PG-003, PG-004, PG-005 | Заголовок услуги/раздела + подзаголовок + CTA |
| **Blog Hero** | Content archive | PG-008 | Заголовок раздела «Статьи» |
| **Minimal Page Title** | Utility pages | PG-006, PG-007, PG-010 | Заголовок страницы без расширенного hero-набора (контакты, отзывы, legal) |

**Не подтверждено как отдельный layout-variant:** Compact FAQ vs Full FAQ — в макетах один паттерн accordion; различается **объём контента**, не тип блока.

### 5.2 CTA family — 3 подтверждённых паттерна + chrome

| Pattern | Block ID | Confirmed |
|---------|----------|-----------|
| Inline Consultation | BLK-025 | Кнопка/ссылка в секциях |
| Guest Visit Section | BLK-019 | Полноширинная секция «гостевой визит» |
| Mobile Sticky Trio | BLK-004 | Телефон · заказать звонок · записаться |
| Header Callback Button | BLK-002 | Кнопка без overlay-макета (M-06) |

### 5.3 Service card grids — 3 уровня (подтверждено G-SERVICE)

| Variant | Block ID | Level |
|---------|----------|-------|
| Home preview cards | BLK-010 | Home-only; v2 + «Генотипирование» |
| Hub category grid | BLK-011 | Service catalog root |
| Section / leaf bodies | BLK-012, BLK-013 | IA depth (не card grid) |

### 5.4 Article cards — 2 паттерна

| Variant | Block ID | Context |
|---------|----------|---------|
| Home preview (subset) | BLK-027 | PG-001 |
| Archive grid | BLK-028 | PG-008 |
| Related (subset) | BLK-033 | PG-009 |

BLK-027 и BLK-028 — **один card pattern**, разный scope выборки; для Frontend Foundation могут слиться в **Article Card**, но в inventory разделены по **page role** (preview vs archive).

---

## 6. Service Branch Audit

**Страницы:** FP-0002-PG-002 (хаб) · FP-0002-PG-003 (подраздел) · FP-0002-PG-004 (конечная)

### 6.1 Общая система G-SERVICE

Все три страницы используют **единый каркас** (Design Intake Audit · Page Inventory §3.2):

```
[Global chrome: BLK-001, 002, 003, 004]
→ BLK-005 Breadcrumbs (глубина меняется)
→ BLK-006 Anchor Nav (набор якорей меняется)
→ BLK-007 Service Hero
→ [UNIQUE CONTENT SLOT — см. ниже]
→ BLK-020 Program Four Directions
→ BLK-018 Rehabilitation Steps
→ BLK-022 Expert Opinion
→ BLK-023 Comfort · Privacy · Care
→ BLK-026 Specialists
→ BLK-015 Reviews Preview
→ BLK-034 FAQ
→ BLK-035 Contact Form
→ BLK-019 Guest Visit CTA
```

**Shared blocks в сервисной ветке:** 15 (включая global chrome).

### 6.2 Действительно уникальные блоки по уровню IA

| Level | Page ID | Unique Block | Что меняется между уровнями |
|-------|---------|--------------|----------------------------|
| **Hub** | PG-002 | **BLK-011** Service Catalog Category Grid | Список категорий (Зависимости, Психическое здоровье, РПП) + карточки направлений |
| **Section** | PG-003 | **BLK-012** Service Section Body | Narrative подраздела + дочерние услуги (пример: «Зависимости и пристрастия») |
| **Leaf** | PG-004 | **BLK-013** Service Leaf Body | Детальный контент конечной услуги (пример: «Лечение алкогольной зависимости») |

**Вывод для Forge WordPress / Frontend:** три PDF — **не три независимых дизайна**, а **один flexible service template** с **одним swap-slot** (BLK-011 / 012 / 013) и настраиваемыми breadcrumbs, anchor items, hero title.

### 6.3 Hub-only shared with Home

| Block | PG-002 | PG-001 |
|-------|--------|--------|
| BLK-014 Feature Cards | ✓ | ✓ |
| BLK-010 Home Services Preview | — | ✓ (другой scope, тот же card family) |

Карточки услуг на главной (BLK-010) и в хабе (BLK-011) — **родственные grid-паттерны**, но **разные Block ID** из-за разной IA-роли (promo preview vs catalog root).

### 6.4 Генотипирование в сервисной ветке

| Представление | Block | В service PDF? |
|---------------|-------|----------------|
| Top bar link | BLK-001 | ✓ (все страницы) |
| Программа 01/04 | BLK-020 | ✓ (PG-002…005) |
| Home preview card | BLK-010 | Только PG-001 (v2) |
| Детальная секция | BLK-021 | Только PG-001 |
| Отдельная service page | — | **Нет макета** (M-05) |

Генотипирование **не имеет** BLK-012/013-аналога в пакете — **PROJECT DECISION** (самостоятельное направление) + **SAFE UNKNOWN** (формат URL).

---

## 7. Content Entity Mapping

Связь блоков с контентными сущностями. CMS **не проектируется** — только фиксация связи.

| Block ID | Services | Articles | Reviews | Specialists | FAQ | Contacts | Legal | Static |
|----------|:--------:|:--------:|:-------:|:-----------:|:---:|:--------:|:-----:|:------:|
| BLK-001 | · | · | · | · | · | ✓ | · | ✓ |
| BLK-002 | · | · | · | · | · | ✓ | · | ✓ |
| BLK-003 | · | · | · | · | · | ✓ | ✓ | ✓ |
| BLK-004 | · | · | · | · | · | ✓ | · | ✓ |
| BLK-005 | · | · | · | · | · | · | · | ✓ |
| BLK-006 | ✓ | · | · | · | · | · | · | ✓ |
| BLK-007 | ✓ | · | · | · | · | · | · | ✓ |
| BLK-008 | · | · | · | · | · | · | · | ✓ |
| BLK-009 | · | · | · | · | · | · | · | ✓ |
| BLK-010 | ✓ | · | · | · | · | · | · | · |
| BLK-011 | ✓ | · | · | · | · | · | · | · |
| BLK-012 | ✓ | · | · | · | · | · | · | · |
| BLK-013 | ✓ | · | · | · | · | · | · | · |
| BLK-014 | · | · | · | · | · | · | · | ✓ |
| BLK-015 | · | · | ✓ | · | · | · | · | · |
| BLK-016 | · | · | ✓ | · | · | · | · | · |
| BLK-017 | · | · | ✓ | ✓ | · | · | · | ✓ |
| BLK-018 | · | · | · | · | · | · | · | ✓ |
| BLK-019 | · | · | · | · | · | · | · | ✓ |
| BLK-020 | ✓ | · | · | · | · | · | · | · |
| BLK-021 | ✓ | · | · | · | · | · | · | · |
| BLK-022 | · | · | · | · | · | · | · | ✓ |
| BLK-023 | · | · | · | · | · | · | · | ✓ |
| BLK-024 | · | · | · | · | · | · | · | ✓ |
| BLK-025 | · | · | · | · | · | · | · | ✓ |
| BLK-026 | · | · | · | ✓ | · | · | · | · |
| BLK-027 | · | ✓ | · | · | · | · | · | · |
| BLK-028 | · | ✓ | · | · | · | · | · | · |
| BLK-029…033 | · | ✓ | · | · | · | · | · | · |
| BLK-034 | · | · | · | · | ✓ | · | · | · |
| BLK-035 | · | · | · | · | · | ✓ | · | ✓ |
| BLK-036…038 | · | · | · | · | · | · | · | ✓ |
| BLK-039 | · | · | · | · | · | ✓ | · | · |
| BLK-040 | · | · | · | · | · | · | ✓ | · |

**Legend:** ✓ = блок явно привязан к сущности · = не привязан / chrome · пусто = static-only

**Примечания:**

- BLK-020 (программа) — **гибрид**: структура статична, направления соответствуют **service/program** сущности.
- BLK-022 (эксперт) — статичный narrative с именем Шпиговского в макете; контент заполнен на PG-001 v2.
- Footer (BLK-003) — legal **ссылки** + placeholder-колонки; сами legal-тексты — BLK-040 и будущие sub-pages (M-03, M-04).

---

## 8. Frontend Foundation Signals

Только **факты** из inventory; Foundation **не создан**.

| Signal | Count / fact |
|--------|----------------|
| Hero family (BLK-007) | **1 family**, **4** confirmed layout contexts |
| Card patterns | **6** distinct grids: UTP (009), Service/Direction (010, 011), Feature (014), Specialist (026), Review (015, 016), Article (027, 028, 033) |
| CTA patterns | **3** section/button patterns (019, 025, 004) + header callback (002) |
| Forms | **1** — BLK-035 (имя, телефон, email, текст — по Design Intake Audit) |
| Tables | **0** — в макетах не обнаружены |
| Accordions | **1** — BLK-034 FAQ |
| Pagination | **1** component — BLK-017 on 2 archives |
| Repeating step grids | **1** — BLK-018 (4 steps) |
| Program repeater | **1** — BLK-020 (4 directions, numbered 01–04) |
| In-page anchor nav | **1** — BLK-006 |
| Long-scroll page templates | **≥4** (Home, G-SERVICE×3, About) |
| Article single complexity | **5** dedicated blocks (029–033) |
| Mobile responsive pairs | **9/11** pages; article single **desktop-only** |
| Placeholder density | **Высокая** на услугах (Lorem), footer, legal — риск для component binding |

---

## 9. WordPress Learning Signals

Сигналы для **AG-WP-001 Forge WordPress**; архитектура **не создана**.

### 9.1 Reusable patterns (block / pattern candidates)

| Block ID | WP pattern signal | Confidence |
|----------|-------------------|------------|
| BLK-001…004 | Global header/footer pattern | High |
| BLK-007 | Hero pattern variants | High |
| BLK-019, BLK-025 | CTA patterns | High |
| BLK-020 | Program section pattern | High |
| BLK-018 | Steps pattern | High |
| BLK-022, BLK-023 | Narrative band patterns | Medium |
| BLK-034 | FAQ accordion pattern | High |

### 9.2 Repeater candidates

| Block ID | Repeater signal | Fields (видимые в макете) |
|----------|-----------------|---------------------------|
| BLK-020 | Program directions | №, title, description |
| BLK-018 | Rehabilitation steps | №, title, text |
| BLK-034 | FAQ items | question, answer |
| BLK-026 | Specialists | photo, name, role |
| BLK-015, BLK-016 | Reviews | author, date, excerpt, «повод обращения» |
| BLK-027, BLK-028, BLK-033 | Articles | title, date, read time, thumbnail |
| BLK-032 | Article sources | citation fields |
| BLK-011 | Service categories | title, description, link |
| BLK-039 | Locations | address, phone, hours, map |

### 9.3 Flexible sections candidates (page builder / ACF flexible)

| Template | Flexible stack signal |
|----------|----------------------|
| **Home (PG-001)** | Ordered stack of 16 sections — strong flexible-content candidate |
| **G-SERVICE (PG-002…004)** | Fixed chrome + **one IA slot** (011/012/013) + shared tail — hybrid template |
| **About (PG-005)** | G-SERVICE tail + unique narrative trio (036–038) |
| **Article (PG-009)** | Semi-fixed: TOC + body + meta + sources + related |

### 9.4 Entity-driven blocks (не CPT design — только сигнал)

| Entity | Blocks |
|--------|--------|
| `service` hierarchy | BLK-010, 011, 012, 013, 020, 021 |
| `post` / article | BLK-027…033 |
| `review` | BLK-015, 016 |
| `specialist` | BLK-026 |
| `faq` | BLK-034 |
| Options (contacts, hours) | BLK-001, 003, 039 |
| Legal pages | BLK-040 (+ future M-03, M-04) |

---

## 10. Inventory Completeness

### 10.1 Подтверждено

| Область | Статус |
|---------|--------|
| Все 11 страниц Page Inventory | Блок-состав зафиксирован |
| Дедупликация секций → блоки | Выполнена (40 Block ID) |
| G-SERVICE unified system | PG-002/003/004 разобраны |
| Home v2 canonical | Порядок секций и BLK-010/022 учтены |
| Variant families | Hero, CTA, Service IA — по макетам |
| Content entity mapping | Таблица §7 |
| Missing pages | Вне scope; перечислены в §10.2 |

### 10.2 Не инвентаризировано (вне подтверждённых PDF)

| Ref | Элемент | Treatment |
|-----|---------|-----------|
| M-01 | Specialists listing page | Блок листинга **не создан**; BLK-026 только preview |
| M-02 | Review single / expand | Поведение BLK-015 CTA — SAFE UNKNOWN |
| M-03, M-04 | Legal sub-pages | Только BLK-040 hub; sub-templates TBD |
| M-05 | Genotyping service page | BLK-021 home-only; отдельный template нет |
| M-06 | Modal «Заказать звонок» | Не блок; кнопка в BLK-002/004 |

### 10.3 Ограничения полноты

| Gap | Impact on inventory |
|-----|---------------------|
| PG-009 mobile отсутствует | Mobile variants BLK-029…033 — **desktop only** |
| PG-008 mobile (misnamed file) | BLK-028 mobile source = `Блог конечная - моб.pdf` ‡ |
| UI states (hover, error, loading) | Не блоки; SAFE UNKNOWN |
| Pixel/layout diff Home v1→v2 | Inventory по текстовому аудиту PDF |
| Дубли UTP/hero в Home v2 | Не отдельные блоки; артефакт макета (U-08) |

### 10.4 Оценка полноты визуального слоя

| Dimension | Coverage |
|-----------|----------|
| Global chrome | **~95%** |
| Core marketing pages | **~90%** |
| Service branch | **~85%** (генотипирование как page — gap) |
| Content (blog/reviews) | **~75%** (mobile gaps, review single) |
| Legal | **~40%** (hub only; expansion planned) |
| System / edge UI | **~50%** (404 да; modal нет) |

**Итог:** визуальный слой **достаточно описан для Frontend Foundation** по основному production path; legal expansion и missing screens — **параллельный трек**.

---

## 11. Readiness Check

### Можно ли переходить к FP-0002 FRONTEND FOUNDATION?

**Да.**

### Обоснование

1. **Block Inventory v1 создан** — 40 уникальных Block ID с типом, first appearance, reuse tier, variant analysis.
2. **Дедупликация выполнена** — повторяющиеся секции (header, program, FAQ, form…) = один блок, не дубли по страницам.
3. **Service branch разрешена** — G-SERVICE = единая система; unique slots (011/012/013) идентифицированы для template design.
4. **Home v2 canonical** — порядок блоков PG-001 зафиксирован по v2.
5. **Frontend signals собраны** — количественные факты для component taxonomy без premature Design System.
6. **WP learning signals отделены** — pattern/repeater/flexible hints для AG-WP-001 без Architecture doc.
7. **Page Inventory readiness** — предыдущий этап дал **GO TO BLOCK INVENTORY**; текущий этап завершает обязательный prerequisite chain.

### Ограничения при Frontend Foundation (не HOLD)

- Mobile parity **PG-009** и именование **PG-008** mobile — пометить в Foundation как responsive debt.
- M-01…M-06 — не блокируют Foundation **shell + confirmed templates**; отдельные charters при появлении макетов.
- Placeholder-контент — Foundation должен различать **component** vs **content-ready** state.
- Figma отсутствует — PDF-only SoT; уточнения spacing/states через coordinator.

---

## 12. SAFE UNKNOWN

| # | Вопрос | Статус |
|---|--------|--------|
| U-01 | Breakpoints, grid, container width | SAFE UNKNOWN |
| U-02 | UI states: hover, focus, form error/loading | SAFE UNKNOWN |
| U-03 | Compact vs Full FAQ layout variant | SAFE UNKNOWN — один accordion pattern |
| U-04 | «Читать весь отзыв» — modal vs page (BLK-015) | SAFE UNKNOWN |
| U-05 | Modal «Заказать звонок» (M-06) | SAFE UNKNOWN |
| U-06 | Генотипирование URL / отдельная service page (M-05) | SAFE UNKNOWN |
| U-07 | Specialists listing template (M-01) | SAFE UNKNOWN |
| U-08 | Дубли УТП-карточек и hero-буллетов Home v2 — артефакт или задумка | SAFE UNKNOWN |
| U-09 | Куда ведёт карточка «Генотипирование» в BLK-010 | SAFE UNKNOWN |
| U-10 | Финальное количество FAQ items, услуг, отзывов, статей | SAFE UNKNOWN |
| U-11 | Article TOC — auto vs manual | SAFE UNKNOWN |
| U-12 | Contacts breadcrumb error в макете — reproduce or fix | SAFE UNKNOWN (координатор) |
| U-13 | Design Intake Audit / Home v2 reports — session only, not committed | SAFE UNKNOWN для audit trail |
| U-14 | PDF package untracked in git | Операционный риск evidence |

---

**GO TO FRONTEND FOUNDATION**

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Supersedes | — (first official Block Inventory) |
| Upstream | FP-0002-PAGE-INVENTORY-v1.md |
| Next artifact | FP-0002 FRONTEND FOUNDATION *(not created in this task)* |
| Changed in this task | **Created:** `FP-0002-BLOCK-INVENTORY-v1.md` |
| Commit / push | Not performed |

*Block Inventory only. No Frontend Foundation, Design System, WordPress Architecture, ACF Architecture, or Frontend Production Plan created.*
