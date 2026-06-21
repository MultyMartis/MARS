# FP-0002 — Page Inventory v1

**Document type:** Official Page Inventory (first release)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-11  
**Coordinator:** PER-0010 — Ольга Дягилева  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Visual source of truth:** PDF-макеты в `INCOMING/01_DESIGN/` (Figma отсутствует и не планируется — **PROJECT DECISION**).  

**Upstream inputs (read-only, не изменялись):**

| Input | Role |
|-------|------|
| FP-0002 DESIGN INTAKE AUDIT | Базовое обнаружение страниц и шаблонов |
| FP-0002 HOME V2 INTAKE UPDATE | Актуализация главной (Home v2 = canonical) |

**Scope:** фиксация фактического состава страниц по подтверждённым макетам. Новые страницы **не проектировались**.

---

# REPORT — FP-0002 PAGE INVENTORY

**Git status (до работы):** ветка `mars/post-cycle8-live-tests`, up to date с `origin`. Папка `INCOMING/01_DESIGN/` — **untracked** (`??`). Прочие изменения репозитория не затрагивались. Commit / push **не выполнялись**.

---

## 1. Executive Summary

Создан **первый официальный Page Inventory** проекта FP-0002 (Shpigovsky.ru).

**Подтверждённый состав пакета:** **11 логических страниц** (типов экранов), представленных **24 PDF-макетами** (22 исходных + 2 Home v2; Home v1 помечен как superseded для главной).

| Метрика | Значение |
|---------|----------|
| Страниц в inventory | **11** |
| Desktop-макетов | **11** (+ Home v1 archived) |
| Mobile-макетов | **11** (+ Home v2 mobile) |
| Полные пары desktop + mobile | **9 из 11** |
| Группы классификации | Core · Service · Content · System · Legal |
| Missing Pages Register | **6 записей** (упомянуты в макетах / решения проекта, без отдельного PDF) |

**Ключевые решения проекта (не блокеры):**

- PDF — визуальный SoT; Figma не используется.
- **Home v2** — актуальная версия главной.
- **Генотипирование** — самостоятельное направление услуг (не только секция главной).
- Страница **специалистов** в дизайн-пакете отсутствует.
- **Детальная страница отзыва** — планируется в будущем.
- **Legal-раздел** будет расширен относительно единственного макета «Правовая инфа».

Inventory описывает **только то, что есть в макетах**, плюс регистр отсутствующих экранов без проектирования новых сущностей.

---

## 2. Page Inventory

### 2.1 Master table

| Page ID | Page Name | Page Type | Design Source | Desktop | Mobile | Status |
|---------|-----------|-----------|---------------|---------|--------|--------|
| **FP-0002-PG-001** | Главная | Home | `2026-06-11-home-v2/Главная страница (v2).pdf` · `… - моб (v2).pdf` | ✓ | ✓ | **Design Ready** — canonical **v2**; v1 superseded |
| **FP-0002-PG-002** | Услуги — хаб | Service Hub | `Услуги хаб.pdf` · `Услуги хаб - моб.pdf` | ✓ | ✓ | **Design Ready** |
| **FP-0002-PG-003** | Услуга — подраздел | Service Section | `Услуга подраздел.pdf` · `Услуга подраздел - моб.pdf` | ✓ | ✓ | **Design Ready** — шаблон; пример: «Зависимости и пристрастия» |
| **FP-0002-PG-004** | Услуга — конечная | Service Leaf | `Услуга конечная.pdf` · `Услуга конечная - моб.pdf` | ✓ | ✓ | **Design Ready** — шаблон; пример: «Лечение алкогольной зависимости» |
| **FP-0002-PG-005** | О центре | About | `О центре.pdf` · `О центре - моб.pdf` | ✓ | ✓ | **Design Ready** |
| **FP-0002-PG-006** | Контакты | Contacts | `Контакты.pdf` · `Контакты - моб.pdf` | ✓ | ✓ | **Design Ready** — breadcrumb-ошибка в макете зафиксирована |
| **FP-0002-PG-007** | Отзывы | Reviews Archive | `Отзывы.pdf` · `Отзывы - моб.pdf` | ✓ | ✓ | **Design Ready** — листинг; детальная страница вне пакета |
| **FP-0002-PG-008** | Статьи — хаб | Blog Archive | `Блог хаб.pdf` · `Блог конечная - моб.pdf` ‡ | ✓ | ✓ ‡ | **Partial** — mobile-файл под неверным именем ‡ |
| **FP-0002-PG-009** | Статья | Blog Single | `Статья.pdf` | ✓ | ✗ | **Partial** — mobile-макет отсутствует |
| **FP-0002-PG-010** | Правовая информация | Legal Hub | `Правовая инфа.pdf` · `Правовая инфа - моб.pdf` | ✓ | ✓ | **Design Ready** — шаблон; подстраницы расширятся (**PROJECT DECISION**) |
| **FP-0002-PG-011** | 404 | Error | `404.pdf` · `404 - моб.pdf` | ✓ | ✓ | **Design Ready** |

‡ Файл `Блог конечная - моб.pdf` по содержанию соответствует **блог-хабу**, не одиночной статье (Design Intake Audit).

### 2.2 Superseded design sources

| Page | Superseded source | Replaced by | Note |
|------|-------------------|-------------|------|
| FP-0002-PG-001 Главная | `Главная стр.pdf` · `Главная стр - моб.pdf` (v1) | Home v2 PDFs | Ревизия 2026-06-11; порядок секций и превью услуг изменены |

### 2.3 Page type definitions (inventory scope)

| Page Type | Meaning in FP-0002 pack |
|-----------|-------------------------|
| **Home** | Единственная landing-страница сайта |
| **Service Hub** | Корень каталога услуг |
| **Service Section** | Промежуточный уровень IA услуг (шаблон) |
| **Service Leaf** | Конечная услуга (шаблон) |
| **About** | Институциональная страница «О центре» |
| **Contacts** | Контакты и локации |
| **Reviews Archive** | Листинг отзывов |
| **Blog Archive** | Листинг статей («Статьи» в nav) |
| **Blog Single** | Детальная статья |
| **Legal Hub** | Хаб правовой информации |
| **Error** | Страница 404 |

---

## 3. Page Classification

### 3.1 Core Pages

| Page ID | Page Name | Template role |
|---------|-----------|---------------|
| FP-0002-PG-001 | Главная | T1 — Home |
| FP-0002-PG-005 | О центре | G-ABOUT (уникальный narrative, общие блоки с услугами) |
| FP-0002-PG-006 | Контакты | T2 — Contacts |

### 3.2 Service Pages

| Page ID | Page Name | Level in service tree |
|---------|-----------|----------------------|
| FP-0002-PG-002 | Услуги — хаб | Level 0 — catalog root |
| FP-0002-PG-003 | Услуга — подраздел | Level 1 — section |
| FP-0002-PG-004 | Услуга — конечная | Level 2 — leaf |

Все три страницы относятся к группе шаблонов **G-SERVICE** (общий каркас: header, breadcrumbs, in-page anchor nav, hero, повторяющиеся блоки).

### 3.3 Content Pages

| Page ID | Page Name | Content entity |
|---------|-----------|----------------|
| FP-0002-PG-007 | Отзывы | Отзывы (листинг) |
| FP-0002-PG-008 | Статьи — хаб | Статьи / блог |
| FP-0002-PG-009 | Статья | Статья (single) |

### 3.4 System Pages

| Page ID | Page Name |
|---------|-----------|
| FP-0002-PG-011 | 404 |

### 3.5 Legal Pages

| Page ID | Page Name |
|---------|-----------|
| FP-0002-PG-010 | Правовая информация |

На момент inventory — **один** legal-макет. Расширение раздела — **PROJECT DECISION** (см. §5).

---

## 4. Service Tree Inventory

### 4.1 Структура по факту макетов

```
Услуги — хаб (FP-0002-PG-002)
├── Услуга — подраздел (FP-0002-PG-003)     ← шаблон; пример: «Зависимости и пристрастия»
│   └── Услуга — конечная (FP-0002-PG-004)  ← шаблон; пример: «Лечение алкогольной зависимости»
├── … (другие подразделы — SAFE UNKNOWN, только примеры в PDF)
└── …
```

### 4.2 Категории услуг (видимые в макетах)

| Категория | Где подтверждена | Отдельный макет подраздела |
|-----------|------------------|----------------------------|
| Зависимости и пристрастия | Услуги хаб, подраздел, конечная | ✓ (пример подраздела) |
| Психическое здоровье | Услуги хаб | SAFE UNKNOWN |
| Расстройства пищевого поведения (РПП) | Услуги хаб | SAFE UNKNOWN |

Количество и полный перечень leaf-услуг в production — **SAFE UNKNOWN** (в пакете только примеры).

### 4.3 Генотипирование — отдельное направление услуг

| Аспект | Статус |
|--------|--------|
| Классификация | **PROJECT DECISION** — генотипирование является **самостоятельным направлением услуг**, не подразделом другой категории |
| Отдельный PDF страницы услуги | **Отсутствует** |
| Представление в макетах | Top bar (все основные экраны); блок «Программа центра» (01/04); детальная секция на главной; карточка в превью «Лечение и профилактика» (**Home v2**) |
| Уровень в service tree | **Вне иерархии хаб → подраздел → конечная** — параллельное направление; leaf/section-макет не предоставлен |

```
[Генотипирование]  ← самостоятельное направление (PROJECT DECISION)
     │
     ├── секция / ссылки на главной (FP-0002-PG-001)
     ├── программа 01/04 (повторяемый блок на нескольких страницах)
     └── отдельная страница услуги — SAFE UNKNOWN (макета нет)
```

---

## 5. Missing Pages Register

Страницы и экраны, **упомянутые в макетах или зафиксированные решениями проекта**, но **отсутствующие как отдельный PDF** в `01_DESIGN/`.

| # | Упоминание | Где встречается | Status | Комментарий |
|---|------------|-----------------|--------|-------------|
| M-01 | **Специалисты** (листинг) | Header top bar, блоки «все специалисты» на главной, услугах, о центре | **PROJECT DECISION** | Страница **пока отсутствует** в дизайн-пакете — зафиксировано решением проекта; не блокер inventory |
| M-02 | **Детальная страница отзыва** | «Читать весь отзыв» на главной, услугах, о центре | **PROJECT DECISION** | Предполагается **в будущем**; поведение (modal vs page) — SAFE UNKNOWN |
| M-03 | **Пользовательское соглашение** | Footer, правовая страница | **PROJECT DECISION** | Legal-раздел **будет расширен** относительно макета; отдельный PDF не предоставлен |
| M-04 | **Политика ПДн / Согласие / Cookies** (отдельные документы) | Список на «Правовая инфа», footer | **PROJECT DECISION** | Входит в расширение legal-раздела; макеты подстраниц отсутствую |
| M-05 | **Генотипирование** (отдельная страница услуги) | Top bar, программа, главная | **PROJECT DECISION** + **SAFE UNKNOWN** | Направление услуг подтверждено; **формат страницы** (отдельный URL vs anchor vs только главная) — SAFE UNKNOWN |
| M-06 | **Modal «Заказать звонок»** | Кнопка в header / sticky bar | **SAFE UNKNOWN** | CTA есть; экран overlay не предоставлен |

---

## 6. Inventory Completeness

### 6.1 Подтверждено

| Область | Деталь |
|---------|--------|
| Полный перечень типов страниц в PDF-пакете | **11 типов** — все заинвентаризированы с Page ID |
| Responsive-покрытие | **9/11** полных пар; **2 Partial** (блог-хаб naming, статья без mobile) |
| Классификация по группам | Core · Service · Content · System · Legal |
| Service tree (3 уровня + генотипирование) | Зафиксирован по макетам и PROJECT DECISION |
| Home canonical version | **v2** (2026-06-11) |
| Visual SoT | PDF-only — PROJECT DECISION |
| Missing pages | Зарегистрированы без проектирования |

### 6.2 Отсутствует в пакете (не inventаризируется как страница)

| Элемент | Inventory treatment |
|---------|---------------------|
| Figma / design manifest | Не планируется — PROJECT DECISION |
| Страница специалистов | Missing Pages Register M-01 |
| Детальная страница отзыва | Missing Pages Register M-02 |
| Legal sub-pages (кроме hub) | Missing Pages Register M-03, M-04 |
| Отдельная страница генотипирования | Missing Pages Register M-05 |
| Modal states | Missing Pages Register M-06 |
| Финальный sitemap / количество услуг и статей | SAFE UNKNOWN |

### 6.3 Требует будущих решений (без проектирования в данном документе)

| Вопрос | Текущий статус |
|--------|----------------|
| Mobile-макет одиночной статьи | SAFE UNKNOWN — предоставить или подтвердить reuse desktop-логики |
| Переименование `Блог конечная - моб.pdf` | SAFE UNKNOWN — операционная задача координатора |
| URL и IA для генотипирования как направления | PROJECT DECISION (направление) + SAFE UNKNOWN (страница) |
| Состав расширенного legal-раздела | PROJECT DECISION (расширение) — конкретный перечень страниц TBD |
| Дубли УТП/hero-буллетов в Home v2 | SAFE UNKNOWN — верификация у PER-0010 |

---

## 7. Readiness Check

### Можно ли переходить к FP-0002 BLOCK INVENTORY?

**Да.**

### Обоснование

1. **Page Inventory v1 создан** — все 11 страниц пакета имеют Page ID, тип, design source, responsive-статус и классификацию.
2. **Service tree зафиксирован** — три уровня услуг + генотипирование как параллельное направление; Block Inventory может опираться на повторяющиеся зоны G-SERVICE без нового page discovery.
3. **Missing Pages Register отделён** — отсутствующие экраны не смешиваются с подтверждённым inventory; Block Inventory работает по **существующим** PDF, missing items — параллельный трек решений.
4. **Home v2 canonical** — единственная версия главной для block-level работы; v1 не создаёт двусмысленности в inventory.
5. **Partial-страницы (блог, статья)** — ограничивают mobile block parity, но **не блокируют** desktop Block Inventory и inventory блоков с пометкой responsive gap.

### Ограничения при Block Inventory (не HOLD для старта)

- Mobile-варианты блоков для **FP-0002-PG-009** (Статья) — только desktop PDF до поступления mobile или решения reuse.
- **FP-0002-PG-008** mobile — опирается на файл с неверным именем; при block inventory фиксировать источник явно.
- Блоки missing pages (специалисты-листинг, review single, legal sub-pages) — **вне scope** Block Inventory v1 до появления макетов или отдельного charter.

---

## 8. SAFE UNKNOWN

| # | Вопрос | Статус |
|---|--------|--------|
| U-01 | Breakpoints и grid (кроме факта desktop/mobile PDF) | SAFE UNKNOWN |
| U-02 | UI states: hover, focus, error, loading форм | SAFE UNKNOWN |
| U-03 | Финальное количество услуг, статей, отзывов | SAFE UNKNOWN |
| U-04 | Поведение «Читать весь отзыв» | SAFE UNKNOWN |
| U-05 | URL/IA страницы генотипирования | SAFE UNKNOWN (направление — PROJECT DECISION) |
| U-06 | Modal «Заказать звонок» | SAFE UNKNOWN |
| U-07 | Поиск по сайту, языковые версии | SAFE UNKNOWN |
| U-08 | Дубли секций Home v2 — артефакт или задумка | SAFE UNKNOWN |
| U-09 | Актуальность `INCOMING/01_DESIGN/README.md` («Empty») vs факт intake | Расхождение зафиксировано; git: PDF untracked |
| U-10 | Design Intake Audit / Home v2 Update как файлы в repo | Отчёты в agent session; **не** committed artifacts в `FP-0002-SHPIGOVSKY/` |

---

**GO TO BLOCK INVENTORY**

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Supersedes | — (first official Page Inventory) |
| Next artifact | FP-0002 BLOCK INVENTORY *(not created in this task)* |
| Changed in this task | **Created:** `FP-0002-PAGE-INVENTORY-v1.md` |
| Commit / push | Not performed |

*Inventory only. No Block Inventory, WordPress Architecture, ACF Architecture, or Frontend Plan created.*
