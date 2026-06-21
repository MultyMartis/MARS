# REPORT — FP-0002 DESIGN AUDIT

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Document type:** A1 Design Audit (post–Source Discovery)  
**Date:** 2026-06-14  
**Upstream:** [FP-0002-SOURCE-DISCOVERY-REPORT-v1.md](FP-0002-SOURCE-DISCOVERY-REPORT-v1.md)  
**Method:** PDF binary READ (24/24) · XLSX READ (SOURCE-025) · cross-check derived inventories · **no** code / workspace / HTML

**Authority applied in this audit:**

| Layer | Sources | Role in audit |
|-------|---------|---------------|
| Critical | SOURCE-001 … SOURCE-024 | Visual SSOT — artboard, blocks, chrome, typography sampling |
| High | SOURCE-025 | IA / URL / menu targets |
| High (derived) | SOURCE-041 Production Standards v3 | Engineering tokens — **not** auto-winner vs PDF |
| Medium (derived) | SOURCE-033, SOURCE-034, SOURCE-036, SOURCE-060…063 | Prior PDF visual pass — cross-check only |

**PDF text-layer limitation (honesty):** Cyrillic labels in PDF text extraction are **partially garbled** (custom font encoding / Type3). Navigation labels and body copy for block naming rely on **prior visual intake** (Block Inventory v1) plus **machine-readable fragments** (phones, email, hours, Lorem markers). Garbled text is **not** treated as new design fact.

**Evidence artefacts (this session):** `REPORTS/_audit_extract_output.json` — 24 PDF metrics + partial text.

---

## Executive summary

Первый полноценный Design Audit после A0 Source Discovery. Аудит построен **одновременно** на PDF (24 макета), XLSX (52 URL-узла + спрос), и производных документах — **не** PDF-only.

| Dimension | Finding |
|-----------|---------|
| Design templates (PDF) | **11** типов экранов · **24** файла · Home v2 canonical |
| Production URL graph (XLSX) | **52** строки · до **4** уровней услуг |
| Unique blocks (PDF-derived) | **40** (SOURCE-034 — validated, not re-invented) |
| PDF ↔ XLSX conflicts | **12** зарегистрированы — **не разрешены** |
| Coordinator open items | Design Approval Sheet v2 — **unsigned** |

---

## PHASE 1 — DESIGN SOURCE MAP

### 1.1 Primary PDF sources (Critical)

| SOURCE-ID | File | Purpose | Desktop | Mobile | Pages / template | Analysis status |
|-----------|------|---------|---------|--------|------------------|-----------------|
| SOURCE-001 | `2026-06-11-home-v2/Главная страница (v2).pdf` | Home desktop **canonical v2** | ✓ | — | PG-001 | **READ** — 1437×16809 px · 1733 text spans |
| SOURCE-002 | `2026-06-11-home-v2/Главная страница - моб (v2).pdf` | Home mobile **canonical v2** | — | ✓ | PG-001 | **READ** — 380×22883 px · 12862 chars |
| SOURCE-003 | `Главная стр.pdf` | Home desktop v1 | ✓ | — | PG-001 | **READ** — **SUPERSEDED** by SOURCE-001 |
| SOURCE-004 | `Главная стр - моб.pdf` | Home mobile v1 | — | ✓ | PG-001 | **READ** — **SUPERSEDED** by SOURCE-002 |
| SOURCE-005 | `Услуги хаб.pdf` | Service catalog root | ✓ | — | PG-002 | **READ** — 1437×~9k px |
| SOURCE-006 | `Услуги хаб - моб.pdf` | Service hub mobile | — | ✓ | PG-002 | **READ** |
| SOURCE-007 | `Услуга подраздел.pdf` | Service section template | ✓ | — | PG-003 | **READ** — example: Зависимости |
| SOURCE-008 | `Услуга подраздел - моб.pdf` | Service section mobile | — | ✓ | PG-003 | **READ** |
| SOURCE-009 | `Услуга конечная.pdf` | Service leaf template | ✓ | — | PG-004 | **READ** — example: алкоголь |
| SOURCE-010 | `Услуга конечная - моб.pdf` | Service leaf mobile | — | ✓ | PG-004 | **READ** |
| SOURCE-011 | `О центре.pdf` | About (single screen) | ✓ | — | PG-005 | **READ** |
| SOURCE-012 | `О центре - моб.pdf` | About mobile | — | ✓ | PG-005 | **READ** — artboard 390 px width (1 file) |
| SOURCE-013 | `Контакты.pdf` | Contacts | ✓ | — | PG-006 | **READ** |
| SOURCE-014 | `Контакты - моб.pdf` | Contacts mobile | — | ✓ | PG-006 | **READ** |
| SOURCE-015 | `Отзывы.pdf` | Reviews archive | ✓ | — | PG-007 | **READ** |
| SOURCE-016 | `Отзывы - моб.pdf` | Reviews archive mobile | — | ✓ | PG-007 | **READ** |
| SOURCE-017 | `Блог хаб.pdf` | Blog archive desktop | ✓ | — | PG-008 | **READ** |
| SOURCE-018 | `Блог конечная - моб.pdf` | **Misnamed** — content = blog hub mobile | — | ✓ | PG-008 | **READ** — confirms archive, not single article |
| SOURCE-019 | `Статья.pdf` | Blog single desktop | ✓ | — | PG-009 | **READ** — 1437×11861 px |
| SOURCE-020 | `Статья - моб.pdf` | Blog single mobile | — | ✓ | PG-009 | **READ** — 380×17833 px · **file exists** (contradicts SOURCE-033 Partial) |
| SOURCE-021 | `Правовая инфа.pdf` | Legal hub | ✓ | — | PG-010 | **READ** |
| SOURCE-022 | `Правовая инфа - моб.pdf` | Legal hub mobile | — | ✓ | PG-010 | **READ** |
| SOURCE-023 | `404.pdf` | Error desktop | ✓ | — | PG-011 | **READ** |
| SOURCE-024 | `404 - моб.pdf` | Error mobile | — | ✓ | PG-011 | **READ** |

**Not on disk:** `Блог хаб - моб.pdf`, `Блог конечная.pdf` — do not register.

### 1.2 Structure / content (High)

| SOURCE-ID | File | Purpose | Analysis status |
|-----------|------|---------|-----------------|
| SOURCE-025 | `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` | URL tree · menu levels · Moscow search demand | **READ** — sheets `Структура` (53 rows) · `Спрос набросок` (53 rows) |

### 1.3 Supporting derived sources used (Medium — cross-check only)

| SOURCE-ID | Document | Used for |
|-----------|----------|----------|
| SOURCE-033 | FP-0002-PAGE-INVENTORY-v1.md | Template baseline — **reconciled** with XLSX |
| SOURCE-034 | FP-0002-BLOCK-INVENTORY-v1.md | Block IDs — **not extended** |
| SOURCE-036 | FP-0002-NUMERIC-DESIGN-RULES-v2.md | Design system numeric extraction |
| SOURCE-041 | FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md | Engineering SSOT — conflict register input |
| SOURCE-060…063 | `fp0002-numeric-extraction-v2*.json`, `fp0002-component-extraction.json` | Raw metrics evidence |

### 1.4 Empty / stale intake (Low — noted, not design input)

SOURCE-026…032 (empty README zones) · SOURCE-065/066 (stale «Empty» READMEs) · SOURCE-064 intake index.

---

## PHASE 2 — PAGE INVENTORY REBUILD

Inventory has **two layers** (by design):

1. **Template layer** — 11 PDF screen types (implementation patterns).
2. **Production URL layer** — 52 nodes from XLSX (deployment graph).

### 2.1 Template pages (PDF authority)

| PAGE-ID | URL (XLSX when known) | PAGE TYPE | AUTHORITY SOURCE | PDF files | Responsive |
|---------|----------------------|-----------|------------------|-----------|------------|
| FP-0002-PG-001 | `/` | Home | **PDF** SOURCE-001/002 (+ XLSX PG-100) | Home v2 pair | **Full pair** |
| FP-0002-PG-002 | `/uslugi/` | Service Hub | **PDF + XLSX** | SOURCE-005/006 | Full pair |
| FP-0002-PG-003 | `/uslugi/zavisimosti/` (example) | Service Section | **PDF + XLSX** | SOURCE-007/008 | Full pair |
| FP-0002-PG-004 | `…/lechenie-alkogolnoy-zavisimosti/` (example) | Service Leaf | **PDF + XLSX** | SOURCE-009/010 | Full pair |
| FP-0002-PG-005 | `/o-centre/` | About (single PDF) | **PDF + XLSX** | SOURCE-011/012 | Full pair |
| FP-0002-PG-006 | `/kontakty/` | Contacts | **PDF + XLSX** | SOURCE-013/014 | Full pair |
| FP-0002-PG-007 | `/otzyvy/` | Reviews Archive | **PDF + XLSX** | SOURCE-015/016 | Full pair |
| FP-0002-PG-008 | `/blog/` | Blog Archive | **PDF + XLSX** | SOURCE-017 + SOURCE-018‡ | Full pair‡ |
| FP-0002-PG-009 | `/blog/nazvanie-stati/` (placeholder) | Blog Single | **PDF + XLSX** | SOURCE-019/020 | **Full pair** (SOURCE-020 READ this audit) |
| FP-0002-PG-010 | `/pravovaya-informaciya-pilzovatelyu/` | Legal Hub | **PDF + XLSX** | SOURCE-021/022 | Full pair |
| FP-0002-PG-011 | — (system) | Error 404 | **PDF** | SOURCE-023/024 | Full pair |

‡ Mobile file misnamed `Блог конечная - моб.pdf`.

### 2.2 Production URL inventory (XLSX authority — SOURCE-025)

**Domain:** `https://shpigovsky.ru/`  
**Template mapping:** `TPL` = which PDF template applies · `NONE` = no PDF.

| PAGE-ID | URL | Label (XLSX) | PAGE TYPE | IA depth | AUTHORITY | TPL |
|---------|-----|--------------|-----------|----------|-----------|-----|
| FP-0002-PG-100 | `/` | Главная | Home | L0 | **XLSX** | PG-001 |
| FP-0002-PG-101 | `/uslugi/` | Услуги | Service Hub | L1 | **XLSX** | PG-002 |
| FP-0002-PG-102 | `/uslugi/zavisimosti/` | Зависимости и пристрастия | Service Section | L2 | **XLSX** | PG-003 |
| FP-0002-PG-103 | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Лечение алкогольной зависимости | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-104 | `/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/` | Лечение наркотической зависимости | Service Section | L3 | **XLSX** | PG-003† |
| FP-0002-PG-105 | `…/soli/` | Лечение солевой зависимости | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-106 | `…/matadon/` | Лечение метадоновой зависимости | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-107 | `…/geroin/` | Лечение героиновой зависимости | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-108 | `…/lekarstva/` | Лечение лекарственной зависимости | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-109 | `/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/` | Поведенческие зависимости | Service Section | L3 | **XLSX** | PG-003† |
| FP-0002-PG-110 | `…/ludomaniya/` | Лечение игровой зависимости | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-111 | `…/internet-zavisimost/` | Интернет-зависимость | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-112 | `…/sozavisimost/` | Лечение созависимости | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-113 | `…/shopogolizm/` | Зависимость от покупок | Service Sub-leaf | L4 | **XLSX** | PG-004† |
| FP-0002-PG-114 | `/` (placeholder) | Название | Service Leaf TBD | — | **XLSX** | NONE |
| FP-0002-PG-115 | `/` (placeholder) | Название | Service Leaf TBD | — | **XLSX** | NONE |
| FP-0002-PG-116 | `/uslugi/psihicheskoe-zdorovie/` | Психическое здоровье | Service Section | L2 | **XLSX** | PG-003 |
| FP-0002-PG-117 | `…/depressiya/` | Депрессия | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-118 | `…/ptsr/` | ПТСР | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-119 | `…/emotsionalnoe-vygoranie/` | Эмоциональное выгорание | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-120 | `…/trevozhnye-rasstroystva/` | Тревожные расстройства | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-121 | `…/rasstroystva-sna/` | Расстройства сна | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-122 | `…/travma/` | Травма | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-123…125 | `/` placeholders | Название ×3 | Service Leaf TBD | — | **XLSX** | NONE |
| FP-0002-PG-126 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | РПП | Service Section | L2 | **XLSX** | PG-003 |
| FP-0002-PG-127 | `…/anoreksiya/` | Нервная анорексия | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-128 | `…/buliniya/` | Нервная булимия | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-129 | `…/kompulsivnoe-pereedanie/` | Компульсивное переедание | Service Leaf | L3 | **XLSX** | PG-004 |
| FP-0002-PG-130 | `/uslugi/genotipirovanie/` | Генотипирование | Service Direction | L2 | **XLSX** | **NONE** (no PDF) |
| FP-0002-PG-131 | `/specyalisty/` | Специалисты | Specialists Archive | L1 | **XLSX** | **NONE** |
| FP-0002-PG-132…134 | `/specyalisty/{slug}/` | Специалист 1–3 | Specialist Single | L2 | **XLSX** | **NONE** |
| FP-0002-PG-135…137 | placeholders | Специалист 4–6 | Specialist Single TBD | — | **XLSX** | NONE |
| FP-0002-PG-138 | `/o-centre/` | О центре | About Hub | L1 | **XLSX + PDF** | PG-005 |
| FP-0002-PG-139 | `/o-centre/o-nas/` | О нас | About Subpage | L2 | **XLSX** | **NONE** |
| FP-0002-PG-140 | `/o-centre/programma-lecheniya/` | Программа лечения | About Subpage | L2 | **XLSX** | **NONE** |
| FP-0002-PG-141 | `/o-centre/galereya-o-dome/` | Галерея о доме | About Subpage | L2 | **XLSX** | **NONE** |
| FP-0002-PG-142 | `/o-centre/specialistam/` | Специалистам | About Subpage | L2 | **XLSX** | **NONE** |
| FP-0002-PG-143 | `/o-centre/rodstvennikam/` | Родственникам | About Subpage | L2 | **XLSX** | **NONE** |
| FP-0002-PG-144 | `/o-centre/intervyu-i-smi/` | Интервью и СМИ | About Subpage | L2 | **XLSX** | **NONE** |
| FP-0002-PG-145 | `/otzyvy/` | Отзывы | Reviews Archive | L1 | **XLSX + PDF** | PG-007 |
| FP-0002-PG-146 | `/blog/` | Статьи | Blog Archive | L1 | **XLSX + PDF** | PG-008 |
| FP-0002-PG-147…149 | `/blog/nazvanie-stati/` | Статья 1–3 | Blog Single (instances) | L2 | **XLSX** | PG-009 |
| FP-0002-PG-150 | `/kontakty/` | Контакты | Contacts | L1 | **XLSX + PDF** | PG-006 |
| FP-0002-PG-151 | `/pravovaya-informaciya-pilzovatelyu//` | Правовая информация | Legal Hub | L1 | **XLSX + PDF** | PG-010 |

† L3 section with L4 children — PDF templates show **3 visible levels**; XLSX adds intermediate parent + sub-leaves.

### 2.3 Pages without PDF (XLSX-only register)

| Category | Count | PAGE-IDs | Notes |
|----------|-------|----------|-------|
| Service sub-leaves L4 | 8 | PG-105…113 | Reuse PG-004 template — **RESOLUTION REQUIRED** for breadcrumbs/anchor depth |
| Genotyping | 1 | PG-130 | Top bar + home section in PDF; **no service page PDF** |
| Specialists hub + profiles | 7 | PG-131…137 | Nav links in PDF; **no listing/single PDF** |
| About subpages | 6 | PG-139…144 | Single About PDF only |
| Placeholder rows | 5 | PG-114,115,123…125,135…137 | Label «Название» / «Специалист N» |
| Review single | 0 URL | — | CTA in PDF; **no URL in XLSX** |
| Legal sub-docs | 0 URL | — | Footer links in PDF; expansion **PROJECT DECISION** |

---

## PHASE 3 — NAVIGATION AUDIT

### 3.1 Header navigation

#### Top bar (BLK-001)

| Item | PDF | XLSX | Both | Notes |
|------|:---:|:----:|:----:|-------|
| Region: Москва | ✓ | — | PDF | Text fragment: hours cluster «пн-пт» |
| Region: Московская область | ✓ | — | PDF | |
| Генотипирование | ✓ | ✓ | **Both** | PDF top bar · XLSX `/uslugi/genotipirovanie/` |
| Working hours (Москва / МО) | ✓ | — | PDF | e.g. пн-пт 08:00–18:00, сб-вс 08:00–22:00 — **PARTIAL** exact strings |
| Специалисты | ✓ | ✓ | **Both** | PDF link · XLSX `/specyalisty/` — **no destination PDF** |
| Phone +7 (925) 183-64-64 | ✓ | — | PDF | **CONFIRMED** text extraction |
| Phone +7 (995) 023-92-26 | ✓ | — | PDF | **CONFIRMED** text extraction |

#### Main navigation (BLK-002)

| Item | PDF | XLSX | Both | Target URL (XLSX) |
|------|:---:|:----:|:----:|-------------------|
| Logo / «Центр» (brand home) | ✓ | ✓ | **Both** | `/` |
| Услуги | ✓ | ✓ | **Both** | `/uslugi/` |
| О центре | ✓ | ✓ | **Both** | `/o-centre/` |
| Отзывы | ✓ | ✓ | **Both** | `/otzyvy/` |
| Статьи | ✓ | ✓ | **Both** | `/blog/` |
| Контакты | ✓ | ✓ | **Both** | `/kontakty/` |
| Заказать звонок (CTA button) | ✓ | — | PDF | Modal **not in PDF** (M-06) |

**Not in main nav (XLSX-only top-level):** `/specyalisty/` (top bar only in PDF) · `/pravovaya-informaciya-pilzovatelyu/` (footer/legal utility).

#### Mobile header / sticky (BLK-004)

| Item | PDF | XLSX | Status |
|------|:---:|:----:|--------|
| Sticky bottom bar (3 actions) | ✓ | — | **CONFIRMED** on mobile PDFs |
| Phone · Callback · Appointment labels | ✓ | — | **PARTIAL** — icons/labels from visual intake |
| Hamburger / condensed header | ✓ | — | **PARTIAL** — pattern visible, menu overlay **not provided** |

### 3.2 Footer navigation (BLK-003)

| Item | PDF | XLSX | Source |
|------|:---:|:----:|--------|
| Multi-column link groups | ✓ | — | PDF — **PARTIAL** (placeholder column headers) |
| Info@shpigovsky.ru | ✓ | — | PDF — **CONFIRMED** |
| Политика конфиденциальности | ✓ | — | PDF — **CONFIRMED** (text layer partial) |
| Пользовательское соглашение | ✓ | — | PDF — **CONFIRMED** (text layer partial) |
| Политика ПДн / Cookies (sub-docs) | ✓ | — | PDF list on legal hub — **no separate URLs in XLSX** |
| Copyright © 2026 | ✓ | — | PDF — **CONFIRMED** |
| Разработка: Overseo | ✓ | — | PDF — **CONFIRMED** |
| Режим работы footer line | ✓ | — | PDF — пн-пт 09:00–19:00 **PARTIAL** |

### 3.3 Service navigation (in-page)

| Pattern | PDF | XLSX | Source |
|---------|:---:|:----:|--------|
| Breadcrumbs (BLK-005) | ✓ | ✓ | **Both** — depth varies; XLSX up to 4 levels |
| In-page anchor nav (BLK-006) | ✓ | — | PDF on G-SERVICE + About |
| Service hub category cards | ✓ | ✓ | **Both** — XLSX lists more categories/leaves than PDF examples |
| «Все специалисты» / specialist cards | ✓ | ✓ | PDF blocks · XLSX `/specyalisty/` |

### 3.4 Utility navigation

| Item | PDF | XLSX | Source |
|------|:---:|:----:|--------|
| Legal hub | ✓ | ✓ | **Both** |
| 404 recovery CTA «На главную» | ✓ | — | PDF |
| Pagination (reviews/blog) | ✓ | — | PDF |
| Search | — | — | **UNKNOWN** — not in PDF or XLSX |

---

## PHASE 4 — BLOCK INVENTORY

Blocks taken **only** from confirmed PDF materials via SOURCE-034 (prior visual pass validated against 24 PDF READ metrics). **No new blocks invented.**

### 4.1 Global blocks

| BLOCK-ID | NAME | PAGE(S) | SOURCE |
|----------|------|---------|--------|
| FP-0002-BLK-001 | Header — Top Bar | PG-001…010 | SOURCE-001…022 |
| FP-0002-BLK-002 | Header — Main Navigation | PG-001…010 | SOURCE-001…022 |
| FP-0002-BLK-003 | Site Footer | PG-001…010 | SOURCE-001…022 |
| FP-0002-BLK-004 | Mobile Sticky CTA Bar | PG-001…010 mobile | SOURCE-002,004,006… |

### 4.2 Navigation blocks

| BLOCK-ID | NAME | PAGE(S) | SOURCE |
|----------|------|---------|--------|
| FP-0002-BLK-005 | Breadcrumbs | PG-002…010 | SOURCE-005…022 |
| FP-0002-BLK-006 | In-Page Anchor Navigation | PG-002…005 | SOURCE-005…012 |

### 4.3 Page-specific blocks (by template)

| PAGE-ID | BLOCK-IDs (scroll order) | SOURCE PDFs |
|---------|---------------------------|-------------|
| PG-001 Home v2 | 001,002,007,009,022,010,014,015,018,019,020,021,023,024,026,027,034,035,003 (+004 mob) | SOURCE-001/002 |
| PG-002 Service Hub | 001,002,005,006,007,011,014,020,018,022,023,026,015,034,035,019,003 | SOURCE-005/006 |
| PG-003 Service Section | 001,002,005,006,007,012,020,018,022,023,026,015,034,035,019,003 | SOURCE-007/008 |
| PG-004 Service Leaf | 001,002,005,006,007,013,020,018,022,023,026,015,034,035,019,003 | SOURCE-009/010 |
| PG-005 About | 001,002,005,006,007,036,037,038,020,018,022,023,026,015,019,003 | SOURCE-011/012 |
| PG-006 Contacts | 001,002,005,039,018,003 | SOURCE-013/014 |
| PG-007 Reviews | 001,002,005,016,018,017,003 | SOURCE-015/016 |
| PG-008 Blog Hub | 001,002,005,007,028,017,022,019,025,003 | SOURCE-017/018 |
| PG-009 Article | 001,002,005,029,030,031,032,033,019,003 (+004 mob) | SOURCE-019/020 |
| PG-010 Legal | 001,002,005,040,003 | SOURCE-021/022 |
| PG-011 404 | 008,003 | SOURCE-023/024 |

**Full block catalogue:** 40 IDs — see SOURCE-034 §2.1. XLSX-only URLs **reuse** template blocks; no new BLOCK-IDs until PDF or approved charter.

---

## PHASE 5 — DESIGN SYSTEM EXTRACTION

**Purpose:** UI Demo preparation · **audit only** · values tagged CONFIRMED / ESTIMATED / UNKNOWN.

### 5.1 Typography (from PDF — SOURCE-036)

| Role | Desktop (px) | Mobile (px) | Weight | Status | Evidence |
|------|--------------|-------------|--------|--------|----------|
| Display / Hero H1 | 70 | 42 | UNKNOWN | CONFIRMED | SOURCE-001 span sizes |
| Section H2 | 36 (dominant) | 32 / 22 cluster | UNKNOWN | CONFIRMED / PARTIAL | PDF; mobile H2 **conflicts** coordinator 22px (SOURCE-041) |
| Section H2 alt | 42 | 42 | UNKNOWN | CONFIRMED | 404, service heroes |
| Card / H3 | 30 | 22–24 | UNKNOWN | CONFIRMED | |
| Body | 16 (count) / 18 (2nd) | 16 | UNKNOWN | CONFIRMED | Coordinator elevates 18 desktop — **see CONFLICT register** |
| Small / UI | 14 | 14 | — | CONFIRMED | |
| Caption / breadcrumb | 13 | 13 | — | CONFIRMED | |
| Button label | 16 | 16 | — | ESTIMATED | |
| Line-height ratio | ~1.22 dominant | ~1.22 | — | CONFIRMED | PDF derived |

**Font family:** **UNKNOWN** from PDF (Type3). Coordinator: **Inter** (SOURCE-041) — **not** in PDF intake file.

### 5.2 Layout & spacing

| Parameter | Desktop | Mobile | Status | Source |
|-----------|---------|--------|--------|--------|
| Artboard width | 1437 px | 380 px (390 alt ×1) | CONFIRMED | 24/24 PDF |
| Content width (median) | ~1020 px | ~274 px | ESTIMATED | SOURCE-036 |
| Container (production) | 1170 px | — | Coordinator | SOURCE-041 — **not PDF-measured** |
| Page padding-x | 172 median / 133 Contacts | 41 | ESTIMATED | PDF; Production 40/20 — **CONFLICT** |
| Section gap standard | 72 / 56 / 250 / 788 clusters | 64 (production token) | ESTIMATED | PDF + Factory rule |
| Card grid gap | 24 | 24 | ESTIMATED | |
| Column counts | 3-up / 4-up desktop → 1 col mobile | CONFIRMED | Mobile PDF pairs |

### 5.3 Colors

| Token | PDF sample | Coordinator (SOURCE-041) | Status |
|-------|------------|--------------------------|--------|
| Accent / CTA | #B3261D | #B3261E | **CONFLICT** |
| Text primary | #3B3D3D | #475371 | **CONFLICT** |
| Page wash | #E3EAF2 / #E4EBF3 | rgba(218,229,240,0.7) | **CONFLICT** (layer vs solid) |
| Footer chrome | #455069 | fallback tokens | PARTIAL |

### 5.4 Buttons

| Variant | Height | Padding-x | Radius (PDF est.) | Radius (Production) | Status |
|---------|--------|-----------|-------------------|---------------------|--------|
| Primary CTA | 44 | 32 | 6 ESTIMATED | 30 px | **CONFLICT** |
| Header callback | UNKNOWN | — | — | 40×30 | PARTIAL |
| Sticky mobile (×3) | bar ~56 | flex thirds | — | 48 touch | PARTIAL |
| Pagination cell | 40×40 | — | ESTIMATED | 10 | ESTIMATED |

### 5.5 Forms (BLK-035)

| Field | Height | Padding | Border | Radius PDF / Prod | Status |
|-------|--------|---------|--------|-------------------|--------|
| Text / tel / email | 48 | 16×12 | 1 px | 6 / **10** | ESTIMATED + **CONFLICT** |
| Textarea | ~120–128 | 16 | 1 px | 6 / **10** | ESTIMATED |
| Layout | 2-col desktop | 1-col mobile | — | CONFIRMED | |

### 5.6 Cards

| Type | Grid | Image aspect | Border | Radius | Status |
|------|------|--------------|--------|--------|--------|
| UTP / Feature / Service / Article / Specialist / Review | 3 or 4 → 1 | 16:10 service | 1 px #CBD4E0 | 8 PDF / **30** Prod | ESTIMATED + **CONFLICT** |
| Shadow | none (flat) | — | — | CONFIRMED | |

### 5.7 Tables

**None** detected in PDF pack — **N/A** for UI Demo table component.

### 5.8 Alerts / system messages

| Type | In PDF? | Status |
|------|---------|--------|
| 404 message block | ✓ BLK-008 | CONFIRMED |
| Form error / success | ✗ | **UNKNOWN** |
| Toast / banner alerts | ✗ | **UNKNOWN** |

### 5.9 Menus

| Component | Desktop | Mobile | Status |
|-----------|---------|--------|--------|
| Dual-row header | ✓ | condensed | CONFIRMED |
| Anchor chip row (BLK-006) | horizontal | scroll — **exact control UNKNOWN** | PARTIAL |
| Footer columns | multi-col | stack | PARTIAL (placeholder labels) |
| Mobile menu overlay | **not provided** | **UNKNOWN** |

### 5.10 Modals

| Modal | In PDF? | Status |
|-------|---------|--------|
| «Заказать звонок» | ✗ (button only) | **UNKNOWN** (M-06) |
| Review expand | ✗ | **UNKNOWN** (M-02) |

### 5.11 Accordions (BLK-034 FAQ)

| Parameter | Value | Status |
|-----------|-------|--------|
| Pattern | single accordion family | CONFIRMED |
| Item gap | 16 px | ESTIMATED |
| Panel radius | 8 PDF / **30** Prod | **CONFLICT** |
| Chevron | ~16 px | ESTIMATED |
| Open behavior (single vs multi) | — | **UNKNOWN** — Approval Sheet v2 §7 open |

### 5.12 Interaction states

| State | In PDF pack? | Status |
|-------|--------------|--------|
| Hover | ✗ | **UNKNOWN** |
| Focus | ✗ | **UNKNOWN** |
| Active nav / anchor | underline ~2 px ESTIMATED | PARTIAL |
| Disabled | ✗ | **UNKNOWN** |
| Loading | ✗ | **UNKNOWN** |

---

## PHASE 6 — HEADER AUDIT

### 6.1 Composition

| Element | Desktop | Mobile | Status |
|---------|---------|--------|--------|
| Top bar row (region, genotyping, hours, specialists, phones) | ✓ | compressed | **CONFIRMED** structure · **PARTIAL** copy |
| Main row (logo, primary nav, callback CTA) | ✓ | hamburger implied | **CONFIRMED** · mobile menu sheet **UNKNOWN** |
| Dual-row stack | ✓ | ✓ | **CONFIRMED** |
| Sticky header on scroll | — | — | **UNKNOWN** |
| Header total height | — | — | **UNKNOWN** (SOURCE-036 SAFE UNKNOWN) |

### 6.2 Element checklist

| Element | Status | Evidence |
|---------|--------|----------|
| Logo / brand mark | **PARTIAL** | Visible in PDF; **no** SVG/PNG in SOURCE-026 branding intake |
| Primary menu items (6) | **CONFIRMED** | PDF + aligns with XLSX L1 URLs |
| Top bar: Генотипирование | **CONFIRMED** | PDF + XLSX URL |
| Top bar: Специалисты | **CONFIRMED** link · **UNKNOWN** destination page design |
| Phones (2 numbers) | **CONFIRMED** | Text extraction |
| Hours strings | **PARTIAL** | Fragments in PDF text |
| «Заказать звонок» button | **CONFIRMED** presence · **UNKNOWN** behavior |
| Callback vs «Записаться» in sticky bar | **PARTIAL** | BLK-004 mobile — labels from visual intake |

---

## PHASE 7 — FOOTER AUDIT

| Element | Desktop | Mobile | Status |
|---------|---------|--------|--------|
| Background band | ✓ | ✓ | **CONFIRMED** |
| Multi-column layout | ✓ | stack | **CONFIRMED** |
| Column headings | placeholders | placeholders | **PARTIAL** |
| Legal links (policy, terms, PDn) | ✓ | ✓ | **CONFIRMED** · sub-page URLs **UNKNOWN** |
| Email Info@shpigovsky.ru | ✓ | ✓ | **CONFIRMED** |
| Phone repeat | ✓ | ✓ | **CONFIRMED** |
| Copyright + Overseo credit | ✓ | ✓ | **CONFIRMED** |
| Vertical padding / exact columns count | — | — | **UNKNOWN** |

---

## PHASE 8 — DESIGN CONFLICT REGISTER

**Rule:** No automatic resolution. Operator / coordinator decision required.

| CONFLICT-ID | SOURCE A | SOURCE B | DESCRIPTION | RESOLUTION REQUIRED |
|-------------|----------|----------|-------------|---------------------|
| CF-001 | PDF IA (SOURCE-005…010) | XLSX (SOURCE-025) | Service tree **3 template levels** vs **4 URL levels** under зависимости | Choose breadcrumb/anchor model for L4 leaves |
| CF-002 | PDF Page Inventory (SOURCE-033) | PDF READ (SOURCE-020) | PG-009 marked «mobile missing» — **Статья - моб.pdf exists** (380×17833) | Update inventory status · confirm as canonical mobile SSOT |
| CF-003 | PDF filename | PDF content (SOURCE-018) | `Блог конечная - моб.pdf` is **blog hub**, not article | Rename file + update traceability |
| CF-004 | PDF top bar / home | XLSX | Genotyping: home section + top link vs `/uslugi/genotipirovanie/` — **no service page PDF** | Page template + card destination |
| CF-005 | PDF nav / blocks | XLSX | «Специалисты» linked everywhere · **no** listing/profile PDF | Stub vs remove vs new design |
| CF-006 | PDF (SOURCE-011) | XLSX | Single About PDF vs **6** `/o-centre/*` subpages | Reuse template vs new designs |
| CF-007 | PDF footer / legal hub | XLSX | Multiple legal docs linked · **one** hub URL in XLSX · no sub-rows | Legal URL structure |
| CF-008 | PDF pixel accent #B3261D | Coordinator (SOURCE-041) #B3261E | Accent hex Δ1 | Pick SSOT for UI Demo |
| CF-009 | PDF text #3B3D3D | Coordinator #475371 | Body text color | Pick SSOT for UI Demo |
| CF-010 | PDF radius est. 6–8 px | Production Standards 30/10/999 | Corner system | UI Demo follows which layer? |
| CF-011 | PDF padding cluster ~172/41 | Production 40/20 | Horizontal inset | Engineering vs visual match |
| CF-012 | PDF mobile H2 ~32 px | Coordinator mobile H2 22 px | Section title mobile | Typography SSOT for Demo |

---

## PHASE 9 — IMPLEMENTATION ROADMAP

Adapted Website Factory sequence for FP-0002 **actual** scope:

| Step | Phase | Scope for FP-0002 | Gate |
|------|-------|-------------------|------|
| **A0** | Source Discovery | ✅ Complete — SOURCE-001…025 registered | Done |
| **A1** | Design Audit | ✅ This document | Conflicts logged — operator review |
| **A1b** | Coordinator sign-off | Design Approval Sheet v2 (8 questions) | Blocks content decisions CF-004…007 |
| **A1c** | IA charter | Reconcile CF-001, CF-006, CF-007 · normalize URL typos (`specyalisty`, double slash) | Before production URL commit |
| **B** | Workspace | Gulp client copy · `src/assets/design/` PDF exports | After A1b minimum |
| **C** | Desktop Shell | BLK-001…005 · header/footer · **no Home body** | Shell-first protocol (SOURCE-041 PD-17) |
| **D** | UI Demo | Component board: typography, buttons, forms, cards, FAQ, pagination — tokens from **resolved** conflicts | After CF-008…012 closed |
| **E** | Operator Page Choice | Pick first production page(s) — demand sheet favors alcohol/narcotic leaves | SEO optional input only |
| **F** | Production Pages | Template rollout PG-001…011 · XLSX URL fill · placeholders for NONE templates | Per-page approval |
| **G** | Completion | Legal expansion · specialists · genotyping page · review single | Missing PDF track |
| **H** | Mobile | PG-009 mobile now **has** PDF — parity pass all templates | After desktop sign-off |

**Recommended first production path (from XLSX + PDF, not decided here):** Home (PG-001) → Shell (C) → Service hub (PG-002) → High-demand leaf (PG-103 alcohol) — **operator must confirm**.

---

## PHASE 10 — READINESS

| Gate | Verdict | Reasons |
|------|---------|---------|
| **READY FOR WORKSPACE** | **YES** | All Critical PDF READ · XLSX READ · block/template inventory sufficient to scaffold · branding intake still empty (non-blocking for workspace **creation**) |
| **READY FOR DESKTOP SHELL** | **YES** with conditions | Header/footer structure **CONFIRMED** · heights **UNKNOWN** · conflicts CF-008…012 open but shell can use Production Standards **if** operator accepts engineering SSOT |
| **READY FOR UI DEMO** | **NO** | Accent/text/radius conflicts unresolved · hover/focus **UNKNOWN** · icon/logo assets missing · coordinator Approval Sheet **unsigned** |
| **READY FOR WORKSPACE** (duplicate check) | **YES** | Same as above |

---

## Git status (this task)

| Action | Path |
|--------|------|
| **Created** | `REPORTS/FP-0002-DESIGN-AUDIT-v1.md` |
| **Created (evidence)** | `REPORTS/_audit_extract_output.json` — PDF metrics + partial text layer |
| **Modified** | none else |
| **Commit / push** | not performed |

---

## SAFE UNKNOWN (summary)

- Logo / icon SVG sources (SOURCE-026 empty)
- Header/footer exact dimensions and sticky behavior
- Modal «Заказать звонок» (M-06)
- Review «Читать весь отзыв» behavior (M-02)
- Mobile hamburger menu overlay
- UI interaction states (hover, focus, error, loading)
- Home v2 duplicate UTP/hero blocks — artifact vs intent (Approval Sheet §2)
- Final placeholder row URLs in XLSX (Название / Специалист 4–6)
- SEO priority for genotyping (no demand rows in XLSX)
- Figma / PNG exports — **none** (PDF-only project)

---

DESIGN AUDIT COMPLETE — **YES**

PAGE INVENTORY READY — **YES** (dual-layer template + XLSX; CF-002 amendment pending)

HEADER READY FOR IMPLEMENTATION — **PARTIAL** (structure yes · metrics/assets/behavior gaps)

FOOTER READY FOR IMPLEMENTATION — **PARTIAL** (structure yes · column content placeholders · legal sub-URLs open)

UI DEMO READY — **NO** (conflicts + unsigned coordinator sheet + missing assets)

WORKSPACE READY — **YES**

CONFLICTS FOUND — **YES** (12 items — CF-001…CF-012)

UNKNOWN ITEMS:

- Header stack heights · sticky behavior · mobile menu overlay
- Logo/asset files (branding intake empty)
- Modal callback · review expand · form validation states
- Hover/focus/active/disabled visual specs
- Home v2 duplicate blocks intent
- Legal sub-document URL set
- Specialist listing/profile templates
- Genotyping standalone page design
- About subpage designs (×6)
- Search / language versions
- Coordinator Design Approval Sheet v2 — all 8 answers blank
