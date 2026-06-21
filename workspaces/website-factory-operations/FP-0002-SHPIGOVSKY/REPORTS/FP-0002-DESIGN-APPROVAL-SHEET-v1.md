# REPORT — FP-0002 DESIGN APPROVAL SHEET

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Document type:** Design Approval Sheet v1 (post–A1 Design Audit)  
**Date:** 2026-06-14  
**Upstream:** [FP-0002-DESIGN-AUDIT-v1.md](FP-0002-DESIGN-AUDIT-v1.md)  
**Method:** Conflict extraction · decision matrix · readiness gates · **no** code / workspace / HTML

**Authority applied:**

| Layer | Sources | Role in this sheet |
|-------|---------|-------------------|
| Critical | SOURCE-001 … SOURCE-024 | Visual SSOT — blocks, chrome, typography sampling |
| High | SOURCE-025 | IA / URL / menu targets |
| High (derived) | SOURCE-041 Production Standards v3 | Engineering tokens — **not** auto-winner vs PDF |
| Medium (derived) | SOURCE-033, SOURCE-034, SOURCE-036 | Prior inventories — cross-check only |

**Honesty rule:** Конфликты **не разрешены** в этом документе. Рекомендации — ориентиры для оператора, **не** принятые решения.

---

## Executive summary

На основании A1 Design Audit сформирован операторский пакет решений для FP-0002. Зафиксировано **12 конфликтов** (CF-001…CF-012), **22 решения оператора** (D-001…D-022), **7 категорий блокеров** до полноценной вёрстки.

| Dimension | Status |
|-----------|--------|
| PDF templates (11 types · 24 files) | READ — Home v2 canonical |
| Production URL graph (XLSX) | 52 nodes · до 4 уровней услуг |
| Conflicts registered | **12** — unresolved |
| Coordinator Approval Sheet v2 | **unsigned** (8 questions blank) |
| Pages without PDF | **27** production URLs (reuse / NONE / placeholders) |

---

## PHASE 1 — CONFLICT EXTRACTION

| ID | Описание | Источник A | Источник B | Влияние | Блокирует верстку |
|----|----------|------------|------------|---------|:-----------------:|
| **CF-001** | Дерево услуг: **3 уровня** в PDF-шаблонах vs **4 URL-уровня** под «Зависимости» (L4 sub-leaves) | PDF IA — SOURCE-005…010 (Service Hub / Section / Leaf templates) | XLSX — SOURCE-025 (PG-104…113: narcotic parent + L4 leaves) | Breadcrumbs (BLK-005), in-page anchor nav (BLK-006), глубина IA на 8 URL | **YES** — для L4 leaves и PG-104 (L3 section с L4 детьми) |
| **CF-002** | PG-009 mobile: inventory помечал mobile **отсутствующим**; файл **существует** | Page Inventory v1 (SOURCE-033) — «mobile missing» | PDF READ — SOURCE-020 `Статья - моб.pdf` (380×17833 px) | Статус PG-009 responsive; mobile block parity для статей | **NO** — desktop/mobile PDF есть; блокирует только **обновление документов**, не старт шаблона |
| **CF-003** | Имя файла **не соответствует** содержимому: `Блог конечная - моб.pdf` = blog hub mobile, не article | PDF filename — SOURCE-018 path | PDF content READ — archive layout, not single article | Traceability PG-008 mobile; риск ошибочного mapping при экспорте в workspace | **NO** — контент подтверждён audit; блокирует **операционную** ясность, не pixel work |
| **CF-004** | Генотипирование: секция/ссылки в PDF + URL `/uslugi/genotipirovanie/` в XLSX — **нет PDF страницы услуги** | PDF — top bar (BLK-001), home blocks (PG-001), program 01/04 | XLSX — SOURCE-025 PG-130 `/uslugi/genotipirovanie/` | Шаблон страницы, карточки-назначения, nav consistency | **YES** — для PG-130 и всех CTA «Генотипирование» с ожиданием landing |
| **CF-005** | «Специалисты» — ссылки в header/blocks; **нет** listing/profile PDF | PDF nav & blocks — SOURCE-001…022 | XLSX — SOURCE-025 PG-131…137 `/specyalisty/` | 7 production URLs без визуального SSOT | **YES** — для PG-131…137 |
| **CF-006** | About: **1 PDF** vs **6 subpages** в XLSX (`/o-centre/*`) | PDF — SOURCE-011/012 (single About) | XLSX — SOURCE-025 PG-139…144 | Шаблон для 6 about-subpages | **YES** — для PG-139…144 |
| **CF-007** | Legal: несколько документов в footer/hub PDF; **1 hub URL** в XLSX, sub-rows отсутствуют | PDF footer + Legal Hub — SOURCE-021/022, BLK-003 | XLSX — SOURCE-025 PG-151 (double slash in URL) | URL structure для политик/соглашений/ПДн/Cookies | **YES** — для legal sub-documents beyond hub |
| **CF-008** | Accent color: PDF **#B3261D** vs Coordinator **#B3261E** | PDF pixel sample — SOURCE-036 | Production Standards v3 — SOURCE-041 | CTA, buttons, accents — UI Demo tokens | **YES** — для token-accurate UI Demo и pixel-perfect CTA; **NO** — если оператор принимает SOURCE-041 для shell |
| **CF-009** | Body text: PDF **#3B3D3D** vs Coordinator **#475371** | PDF text sample — SOURCE-036 | Production Standards v3 — SOURCE-041 | Typography color system | **YES** — для pixel-perfect UI Demo; **NO** — при engineering SSOT override |
| **CF-010** | Border radius: PDF est. **6–8 px** vs Production **30/10/999** | PDF component sampling — SOURCE-036, SOURCE-060…063 | Production Standards v3 — SOURCE-041 | Buttons, forms, cards, FAQ accordion | **YES** — для UI Demo component board; **NO** — при явном выборе SOURCE-041 |
| **CF-011** | Horizontal padding: PDF cluster **~172/41 px** vs Production **40/20 px** | PDF layout metrics — SOURCE-036 | Production Standards v3 — SOURCE-041 | Container inset, section alignment | **PARTIAL blocker** — shell можно начать; pixel-match требует решения |
| **CF-012** | Mobile H2: PDF **~32 px** vs Coordinator mobile H2 **22 px** | PDF mobile spans — SOURCE-002,020… | Production Standards v3 — SOURCE-041 | Section titles on mobile breakpoints | **YES** — для mobile typography SSOT в UI Demo |

---

## PHASE 2 — DECISION MATRIX

| ID | RESOLUTION TYPE | Обоснование |
|----|-----------------|-------------|
| CF-001 | **IA DECISION** | Структура URL и breadcrumb depth — не visual-only |
| CF-002 | **TECHNICAL DECISION** | Amend inventory / traceability; PDF уже READ |
| CF-003 | **TECHNICAL DECISION** | File rename + documentation — не design intent |
| CF-004 | **OPERATOR DECISION** + **DESIGN DECISION** | URL подтверждён XLSX; **формат страницы** без PDF |
| CF-005 | **OPERATOR DECISION** + **DESIGN DECISION** | Stub / defer / new design — product scope |
| CF-006 | **IA DECISION** + **DESIGN DECISION** | Reuse About template vs новые макеты |
| CF-007 | **IA DECISION** + **CONTENT DECISION** | Перечень legal URLs и контент sub-docs |
| CF-008 | **DESIGN DECISION** + **TECHNICAL DECISION** | Visual SSOT vs engineering token |
| CF-009 | **DESIGN DECISION** + **TECHNICAL DECISION** | Visual SSOT vs engineering token |
| CF-010 | **DESIGN DECISION** + **TECHNICAL DECISION** | Corner system for components |
| CF-011 | **TECHNICAL DECISION** | Engineering vs visual match |
| CF-012 | **DESIGN DECISION** + **TECHNICAL DECISION** | Mobile typography authority |

**SAFE UNKNOWN (не конфликт, но требует решения позже):**

| Topic | RESOLUTION TYPE |
|-------|-----------------|
| Font family (PDF Type3 — Inter in SOURCE-041 only) | **DESIGN DECISION** |
| Logo SVG/PNG (SOURCE-026 empty) | **CONTENT DECISION** |
| Modal «Заказать звонок» (M-06) | **DESIGN DECISION** |
| Mobile hamburger overlay | **DESIGN DECISION** |
| Hover / focus / error / loading states | **DESIGN DECISION** |
| Home v2 duplicate UTP/hero blocks | **CONTENT DECISION** |
| Accordion single vs multi-open | **DESIGN DECISION** |
| Review «Читать весь отзыв» (M-02) | **OPERATOR DECISION** |
| Search / language versions | **SAFE UNKNOWN** |
| XLSX placeholder rows (PG-114,115,123…125,135…137) | **CONTENT DECISION** + **IA DECISION** |

---

## PHASE 3 — HEADER READINESS

| HEADER ELEMENT | STATUS | SOURCE | ACTION REQUIRED |
|----------------|--------|--------|-----------------|
| **logo** | **PARTIAL** | PDF — brand mark visible (SOURCE-001…022); SOURCE-026 branding intake **empty** | Получить logo assets (SVG/PNG) или подтвердить raster-from-PDF workflow |
| **phones** | **CONFIRMED** | PDF text extraction — +7 (925) 183-64-64 · +7 (995) 023-92-26 (SOURCE-001) | None for copy |
| **navigation** | **CONFIRMED** | PDF BLK-002 + XLSX L1 URLs align — Услуги · О центре · Отзывы · Статьи · Контакты (SOURCE-001, SOURCE-025) | None for L1 items |
| **callback** | **PARTIAL** | PDF — «Заказать звонок» button **CONFIRMED**; modal **not in PDF** (M-06) | Operator: modal vs tel vs external (D-016) |
| **region** | **CONFIRMED** | PDF top bar — Москва · Московская область (SOURCE-001) | None for presence |
| **hours** | **PARTIAL** | PDF fragments — пн-пт 08:00–18:00, сб-вс 08:00–22:00 (top); footer пн-пт 09:00–19:00 **PARTIAL** exact strings | Operator: confirm final hours strings (top vs footer discrepancy) |
| **specialists** | **PARTIAL** | PDF link **CONFIRMED**; XLSX `/specyalisty/`; **no destination page PDF** (CF-005) | Operator: stub / URL / defer (D-005, D-020) |
| **genotyping** | **PARTIAL** | PDF top bar + XLSX `/uslugi/genotipirovanie/` **CONFIRMED** link; **no service page PDF** (CF-004) | Operator: page template + card destinations (D-004, D-015) |
| **desktop behavior** | **PARTIAL** | Dual-row header **CONFIRMED** (BLK-001 + BLK-002); sticky on scroll **UNKNOWN**; exact heights **UNKNOWN** (SOURCE-036) | Design decision: sticky yes/no; measure or accept estimated heights |
| **mobile behavior** | **PARTIAL** | Sticky bottom bar BLK-004 **CONFIRMED**; hamburger **implied**; menu overlay **UNKNOWN** | Design decision: mobile menu pattern; sticky bar labels (callback vs appointment) |

---

## PHASE 4 — FOOTER READINESS

| FOOTER ELEMENT | STATUS | SOURCE | ACTION REQUIRED |
|----------------|--------|--------|-----------------|
| **background band** | **CONFIRMED** | PDF BLK-003 — all main templates (SOURCE-001…022) | None |
| **multi-column layout** | **CONFIRMED** | PDF — multi-col desktop · stack mobile | None for structure |
| **column headings** | **PARTIAL** | PDF — placeholder column headers (garbled text layer) | Content decision: final column titles and link groups |
| **legal links** | **PARTIAL** | PDF — Политика конфиденциальности · Пользовательское соглашение **CONFIRMED** (partial text); PDn/Cookies on hub — **no XLSX sub-URLs** (CF-007) | IA decision: legal URL set (D-007) |
| **email** | **CONFIRMED** | PDF — Info@shpigovsky.ru (SOURCE-001) | None |
| **phone repeat** | **CONFIRMED** | PDF footer — same numbers as header | None |
| **copyright + credit** | **CONFIRMED** | PDF — © 2026 · Разработка: Overseo | None |
| **hours line** | **PARTIAL** | PDF — пн-пт 09:00–19:00 fragment; may differ from top bar | Operator: reconcile top bar vs footer hours |
| **vertical padding / column count** | **UNKNOWN** | SOURCE-036 — exact dimensions not measured | Measure from PDF or accept ESTIMATED values for shell |

*Note: Footer checklist uses structural elements from audit §7; mapped to task element list where applicable.*

---

## PHASE 5 — DESIGN SYSTEM READINESS

| Component | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| **Typography** | **PARTIAL** | Sizes CONFIRMED from PDF (SOURCE-036); font family **UNKNOWN**; mobile H2 **CONFLICT** CF-012; body 16/18 **CONFLICT** with SOURCE-041 | Font decision (D-013); resolve CF-012; weight values UNKNOWN |
| **Colors** | **PARTIAL** | PDF samples CONFIRMED; accent/text/page wash **CONFLICT** CF-008, CF-009 | Operator picks PDF vs Production SSOT (D-008, D-009) |
| **Buttons** | **PARTIAL** | Primary height 44 CONFIRMED; radius **CONFLICT** CF-010; header callback size UNKNOWN | Resolve CF-010; UI states UNKNOWN |
| **Forms** | **PARTIAL** | BLK-035 layout CONFIRMED; field metrics ESTIMATED; radius **CONFLICT** CF-010 | Resolve radius; error/success states **UNKNOWN** |
| **Cards** | **PARTIAL** | Grid/aspect CONFIRMED; radius **CONFLICT** CF-010 (8 PDF vs 30 Prod) | Resolve corner system |
| **Tables** | **N/A** | None in PDF pack | Not required for v1 UI Demo |
| **Alerts** | **UNKNOWN** | 404 block CONFIRMED; form error/success · toast **not in PDF** | Design decision for form feedback |
| **Accordion** | **PARTIAL** | BLK-034 FAQ pattern CONFIRMED; radius CONFLICT; open behavior **UNKNOWN** | Single vs multi-open decision |
| **Navigation** | **PARTIAL** | Dual-row header CONFIRMED; anchor chip row PARTIAL; mobile menu **UNKNOWN** | Mobile overlay pattern |
| **Modal patterns** | **UNKNOWN** | Callback button only — no overlay PDF (M-06); review expand (M-02) | D-016, D-019 |

---

## PHASE 6 — PAGE READINESS

### 6.1 Template layer (11 PDF screen types)

| PAGE-ID | URL (when known) | DESIGN STATUS | Notes |
|---------|------------------|---------------|-------|
| FP-0002-PG-001 | `/` | **READY** | Home v2 canonical — SOURCE-001/002; v1 superseded |
| FP-0002-PG-002 | `/uslugi/` | **READY** | Full pair SOURCE-005/006 |
| FP-0002-PG-003 | `/uslugi/zavisimosti/` (example) | **READY** | Full pair SOURCE-007/008 |
| FP-0002-PG-004 | `…/lechenie-alkogolnoy-zavisimosti/` (example) | **READY** | Full pair SOURCE-009/010 |
| FP-0002-PG-005 | `/o-centre/` | **READY** | Full pair SOURCE-011/012 |
| FP-0002-PG-006 | `/kontakty/` | **READY** | Full pair; breadcrumb error in mock — D-018 |
| FP-0002-PG-007 | `/otzyvy/` | **READY** | Full pair; review single not in pack |
| FP-0002-PG-008 | `/blog/` | **PARTIAL** | Desktop READY; mobile via misnamed file CF-003 — content confirmed |
| FP-0002-PG-009 | `/blog/nazvanie-stati/` | **READY** | Full pair — SOURCE-019/020 (amends old «Partial» — CF-002) |
| FP-0002-PG-010 | `/pravovaya-informaciya-pilzovatelyu/` | **READY** | Full pair; sub-pages expansion TBD |
| FP-0002-PG-011 | — (system 404) | **READY** | Full pair SOURCE-023/024 |

### 6.2 Production URL layer (XLSX — SOURCE-025)

**Legend:** TPL = PDF template · **PDF-only** = template has PDF · **XLSX-only** = no dedicated PDF · **Placeholder** = URL TBD

| PAGE-ID | URL | DESIGN STATUS | Source basis |
|---------|-----|---------------|--------------|
| FP-0002-PG-100 | `/` | **READY** | PDF + XLSX |
| FP-0002-PG-101 | `/uslugi/` | **READY** | PDF + XLSX |
| FP-0002-PG-102 | `/uslugi/zavisimosti/` | **READY** | PDF + XLSX |
| FP-0002-PG-103 | `…/lechenie-alkogolnoy-zavisimosti/` | **READY** | PDF + XLSX |
| FP-0002-PG-104 | `…/lechenie-narkoticheskoy-zavisimosti/` | **PARTIAL** | XLSX L3 section + L4 children — **CF-001**; reuse PG-003† |
| FP-0002-PG-105 | `…/soli/` | **PARTIAL** | **XLSX-only** L4 — reuse PG-004† — **CF-001** |
| FP-0002-PG-106 | `…/matadon/` | **PARTIAL** | **XLSX-only** L4 — **CF-001** |
| FP-0002-PG-107 | `…/geroin/` | **PARTIAL** | **XLSX-only** L4 — **CF-001** |
| FP-0002-PG-108 | `…/lekarstva/` | **PARTIAL** | **XLSX-only** L4 — **CF-001** |
| FP-0002-PG-109 | `…/lechenie-povedencheskoy-zavisimosti/` | **PARTIAL** | XLSX L3 — reuse PG-003† — **CF-001** |
| FP-0002-PG-110 | `…/ludomaniya/` | **PARTIAL** | **XLSX-only** L4 — **CF-001** |
| FP-0002-PG-111 | `…/internet-zavisimost/` | **PARTIAL** | **XLSX-only** L4 — **CF-001** |
| FP-0002-PG-112 | `…/sozavisimost/` | **PARTIAL** | **XLSX-only** L4 — **CF-001** |
| FP-0002-PG-113 | `…/shopogolizm/` | **PARTIAL** | **XLSX-only** L4 — **CF-001** |
| FP-0002-PG-114 | `/` (placeholder) | **UNKNOWN** | **XLSX-only** — label «Название» |
| FP-0002-PG-115 | `/` (placeholder) | **UNKNOWN** | **XLSX-only** — label «Название» |
| FP-0002-PG-116 | `/uslugi/psihicheskoe-zdorovie/` | **READY** | XLSX + PG-003 template |
| FP-0002-PG-117 | `…/depressiya/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-118 | `…/ptsr/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-119 | `…/emotsionalnoe-vygoranie/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-120 | `…/trevozhnye-rasstroystva/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-121 | `…/rasstroystva-sna/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-122 | `…/travma/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-123 | `/` (placeholder) | **UNKNOWN** | **XLSX-only** |
| FP-0002-PG-124 | `/` (placeholder) | **UNKNOWN** | **XLSX-only** |
| FP-0002-PG-125 | `/` (placeholder) | **UNKNOWN** | **XLSX-only** |
| FP-0002-PG-126 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | **READY** | XLSX + PG-003 template |
| FP-0002-PG-127 | `…/anoreksiya/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-128 | `…/buliniya/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-129 | `…/kompulsivnoe-pereedanie/` | **READY** | XLSX + PG-004 template |
| FP-0002-PG-130 | `/uslugi/genotipirovanie/` | **UNKNOWN** | **XLSX-only** — no PDF — **CF-004** |
| FP-0002-PG-131 | `/specyalisty/` | **UNKNOWN** | **XLSX-only** — **CF-005** |
| FP-0002-PG-132 | `/specyalisty/{slug}/` | **UNKNOWN** | **XLSX-only** — **CF-005** |
| FP-0002-PG-133 | `/specyalisty/{slug}/` | **UNKNOWN** | **XLSX-only** — **CF-005** |
| FP-0002-PG-134 | `/specyalisty/{slug}/` | **UNKNOWN** | **XLSX-only** — **CF-005** |
| FP-0002-PG-135 | placeholder | **UNKNOWN** | **XLSX-only** placeholder |
| FP-0002-PG-136 | placeholder | **UNKNOWN** | **XLSX-only** placeholder |
| FP-0002-PG-137 | placeholder | **UNKNOWN** | **XLSX-only** placeholder |
| FP-0002-PG-138 | `/o-centre/` | **READY** | PDF + XLSX |
| FP-0002-PG-139 | `/o-centre/o-nas/` | **UNKNOWN** | **XLSX-only** — **CF-006** |
| FP-0002-PG-140 | `/o-centre/programma-lecheniya/` | **UNKNOWN** | **XLSX-only** — **CF-006** |
| FP-0002-PG-141 | `/o-centre/galereya-o-dome/` | **UNKNOWN** | **XLSX-only** — **CF-006** |
| FP-0002-PG-142 | `/o-centre/specialistam/` | **UNKNOWN** | **XLSX-only** — **CF-006** |
| FP-0002-PG-143 | `/o-centre/rodstvennikam/` | **UNKNOWN** | **XLSX-only** — **CF-006** |
| FP-0002-PG-144 | `/o-centre/intervyu-i-smi/` | **UNKNOWN** | **XLSX-only** — **CF-006** |
| FP-0002-PG-145 | `/otzyvy/` | **READY** | PDF + XLSX |
| FP-0002-PG-146 | `/blog/` | **PARTIAL** | PDF + XLSX — mobile filename CF-003 |
| FP-0002-PG-147 | `/blog/nazvanie-stati/` | **READY** | PDF + XLSX — PG-009 template |
| FP-0002-PG-148 | `/blog/nazvanie-stati/` | **READY** | XLSX instance — PG-009 template |
| FP-0002-PG-149 | `/blog/nazvanie-stati/` | **READY** | XLSX instance — PG-009 template |
| FP-0002-PG-150 | `/kontakty/` | **READY** | PDF + XLSX |
| FP-0002-PG-151 | `/pravovaya-informaciya-pilzovatelyu//` | **READY** | PDF hub; sub-docs **UNKNOWN** — CF-007; URL typo |

### 6.3 Summary counts

| Category | Count | PAGE-IDs |
|----------|-------|----------|
| **READY** (PDF-backed or clear template reuse) | **25** | PG-100…103, 116…122, 126…129, 138, 145…150, 147…149 |
| **PARTIAL** (template reuse + open IA/conflict) | **12** | PG-104…113, 146 |
| **UNKNOWN** (no PDF · placeholders · missing design) | **15** | PG-114,115,123…125,130…137,139…144 |
| **PDF-only** (no XLSX production row) | **1** | PG-011 (404 system) |

† Reuse PG-003/004 assumes operator accepts template extrapolation — **not** auto-approved.

---

## PHASE 7 — BLOCKERS BEFORE WORKSPACE

Только реальные блокеры старта. Без теории и улучшений.

| # | Blocker | Blocks what | Evidence |
|---|---------|-------------|----------|
| B-01 | **Design token conflicts unresolved** (CF-008…CF-012) | UI Demo · pixel-accurate component board · mobile typography | Design Audit §5, §8 |
| B-02 | **Coordinator Approval Sheet v2 unsigned** (8 questions blank) | Content/navigation decisions for genotyping, callback, specialists, home duplicates | FP-0002-DESIGN-APPROVAL-SHEET-v2.md |
| B-03 | **Logo / branding assets missing** (SOURCE-026 empty) | Production-ready header logo implementation | Design Audit §6.2 |
| B-04 | **IA conflicts open** (CF-001, CF-004, CF-005, CF-006, CF-007) | Production URL pages without PDF (27 URLs) · L4 breadcrumbs | Design Audit §2.3, §8 |
| B-05 | **Modal / mobile menu patterns not designed** (M-06, hamburger overlay) | Callback CTA behavior · mobile nav completion | Design Audit §5.10, §6.1 |
| B-06 | **UI interaction states not in PDF** (hover, focus, form error) | Accessible production polish · form validation UX | Design Audit §5.12 |
| B-07 | **XLSX placeholder rows** (5 URLs) | Cannot deploy named production pages | SOURCE-025 PG-114,115,123…125,135…137 |

**Not blockers for Workspace creation (scaffold only):**

- PDF pack complete (24/24 READ)
- Block inventory sufficient (40 blocks — SOURCE-034)
- XLSX READ
- CF-002, CF-003 — documentation/ops only

---

## PHASE 8 — OPERATOR DECISIONS REQUIRED

### IA & structure

**D-001** — *CF-001: 4-level service URLs under «Зависимости»*  
- **Вопрос:** Как строить breadcrumbs и in-page anchor nav для L4 leaves (соли, героин, …)?  
- **Вариант A:** Flatten — L4 leaves показывают 3-level trail (скрыть промежуточный L3 narcotic parent в UI)  
- **Вариант B:** Full 4-level trail — добавить уровень в BLK-005/BLK-006  
- **Рекомендация:** Вариант B — соответствует XLSX IA; требует расширения anchor row  
- **Причина:** XLSX — authority для URL; PDF показывает max 3 visible levels

**D-002** — *CF-004: страница генотипирования*  
- **Вопрос:** Какой шаблон для `/uslugi/genotipirovanie/` (PG-130)?  
- **Вариант A:** Reuse Service Leaf (PG-004) с адаптацией контента  
- **Вариант B:** Reuse Service Section (PG-003)  
- **Вариант C:** Отложить URL — временно anchor на главную / stub  
- **Рекомендация:** Не выбирать без input дизайнера — **SAFE UNKNOWN** между A/B; C только если launch defer  
- **Причина:** Нет PDF; PROJECT DECISION подтверждает направление, не layout

**D-003** — *CF-005: специалисты без PDF*  
- **Вопрос:** Стратегия для `/specyalisty/` и profile URLs?  
- **Вариант A:** Заказать/new design PDF  
- **Вариант B:** Reuse card patterns from Home/Services (BLK-015/018) as interim listing  
- **Вариант C:** Stub page / defer links (D-020)  
- **Рекомендация:** A для production quality; C для v1 если scope cut  
- **Причина:** Nav links live in PDF — dead links unacceptable without C

**D-004** — *CF-006: About subpages (×6)*  
- **Вопрос:** Шаблон для PG-139…144?  
- **Вариант A:** Reuse single About PDF (PG-005) для всех subpages  
- **Вариант B:** Reuse Service Section template (PG-003)  
- **Вариант C:** Новые макеты от дизайнера  
- **Рекомендация:** A или B — operator must pick; C if content diverges strongly  
- **Причина:** XLSX defines URLs; PDF has one About screen only

**D-005** — *CF-007: legal sub-documents*  
- **Вопрос:** URL structure для политик beyond hub?  
- **Вариант A:** Single hub page with anchors for all docs  
- **Вариант B:** Separate URLs per document (expand XLSX)  
- **Вариант C:** Hub only in v1 — footer links → hub sections  
- **Рекомендация:** B long-term; C acceptable for v1 launch  
- **Причина:** Footer lists multiple docs; XLSX has one hub row + URL typo

**D-006** — *XLSX URL normalization*  
- **Вопрос:** Исправить `specyalisty` typo и double slash in PG-151?  
- **Вариант A:** Fix to `specialisty` + single slash before production  
- **Вариант B:** Keep as client provided until redirect strategy defined  
- **Рекомендация:** A — unless live site already indexed under typo  
- **Причина:** Operational hygiene; **SAFE UNKNOWN** on live SEO impact

### Design tokens (UI Demo gate)

**D-007** — *CF-008: accent color SSOT*  
- **Вопрос:** #B3261D (PDF) или #B3261E (Production Standards)?  
- **Вариант A:** PDF pixel sample  
- **Вариант B:** Production Standards v3  
- **Рекомендация:** A for pixel-perfect; B for engineering consistency  
- **Причина:** Δ1 hex — visible on large CTA surfaces

**D-008** — *CF-009: body text color SSOT*  
- **Вопрос:** #3B3D3D (PDF) или #475371 (Production Standards)?  
- **Вариант A:** PDF  
- **Вариант B:** Production Standards  
- **Рекомендация:** Operator visual compare on Home PDF export  
- **Причина:** Measurable contrast difference

**D-009** — *CF-010: corner radius system*  
- **Вопрос:** PDF ~6–8 px или Production 30/10/999?  
- **Вариант A:** PDF-derived (6–8 cards, 6 buttons)  
- **Вариант B:** Production Standards (30 primary, 10 forms)  
- **Рекомендация:** Explicit pick before UI Demo — **cannot dual-SSOT**  
- **Причина:** Affects every card, button, FAQ, form field

**D-010** — *CF-011: horizontal page padding*  
- **Вопрос:** PDF ~172/41 px или Production 40/20?  
- **Вариант A:** Match PDF artboard extraction  
- **Вариант B:** Production container 1170 + 40/20 padding  
- **Рекомендация:** B for engineering; A only if pixel audit mandates  
- **Причина:** PDF median includes artboard margins, not just container

**D-011** — *CF-012: mobile section H2 size*  
- **Вопрос:** ~32 px (PDF) или 22 px (Production Standards)?  
- **Вариант A:** PDF mobile spans  
- **Вариант B:** Coordinator 22 px rule  
- **Рекомендация:** Side-by-side on Service mobile PDF before pick  
- **Причина:** Direct mobile layout impact

**D-012** — *Font family*  
- **Вопрос:** Какой шрифт использовать? (PDF Type3 — name UNKNOWN)  
- **Вариант A:** Files from designer  
- **Вариант B:** Inter (SOURCE-041)  
- **Вариант C:** Google Fonts — operator specifies  
- **Рекомендация:** A if available; else B as documented interim with designer sign-off  
- **Причина:** Typography is foundational for UI Demo

### Content & behavior (Coordinator Sheet v2 alignment)

**D-013** — *Home v2 duplicate UTP/hero blocks*  
- **Вопрос:** Артефакт экспорта или задуманный контент?  
- **Вариант A:** Артефакт — оставить один блок  
- **Вариант B:** Задумка — воспроизвести как в макете  
- **Рекомендация:** Verify with PER-0010 / designer — audit flags SAFE UNKNOWN  
- **Причина:** Affects PG-001 block count and content entry

**D-014** — *Genotyping card on Home — destination*  
- **Вопрос:** Куда ведёт карточка «Генотипирование» на главной?  
- **Вариант A:** `/uslugi/genotipirovanie/`  
- **Вариант B:** Anchor on same page  
- **Вариант C:** External URL  
- **Рекомендация:** A if D-002 resolves page template; else B interim  
- **Причина:** Links must not 404 at launch

**D-015** — *«Заказать звонок» behavior*  
- **Вопрос:** Что происходит при клике?  
- **Вариант A:** Modal form (reuse BLK-035 patterns)  
- **Вариант B:** `tel:` dial  
- **Вариант C:** External service  
- **Рекомендация:** A — CTA label implies form; design overlay TBD  
- **Причина:** No modal PDF — minimum viable pattern needed

**D-016** — *Blog article mobile*  
- **Вопрос:** Mobile SSOT для статей после подтверждения SOURCE-020?  
- **Вариант A:** SOURCE-020 `Статья - моб.pdf` as canonical (amends CF-002)  
- **Вариант B:** Wait for designer re-export  
- **Вариант C:** Extrapolate from desktop  
- **Рекомендация:** A — file READ in audit; update Page Inventory  
- **Причина:** CF-002 resolved by A1 READ

**D-017** — *Contacts breadcrumb error*  
- **Вопрос:** Исправить breadcrumb на PG-006?  
- **Вариант A:** Fix to logical trail (Контакты)  
- **Вариант B:** Reproduce mock error  
- **Рекомендация:** A  
- **Причина:** Known mock defect — Page Inventory notes it

**D-018** — *«Читать весь отзыв» in v1*  
- **Вопрос:** Implement in first release?  
- **Вариант A:** Implement (modal or page — TBD)  
- **Вариант B:** Defer — hide or disable link  
- **Рекомендация:** B unless review single designed  
- **Причина:** No review single PDF/URL (M-02)

**D-019** — *Specialists nav links in v1*  
- **Вопрос:** Куда ведут «Специалисты» / «Все специалисты»?  
- **Вариант A:** `/specyalisty/` (requires D-003)  
- **Вариант B:** Stub  
- **Вариант C:** Remove links until design ready  
- **Рекомендация:** C or B if D-003 = defer; A only with listing template  
- **Причина:** CF-005 — no destination design

**D-020** — *Accordion FAQ open behavior*  
- **Вопрос:** Single-open или multi-open?  
- **Вариант A:** Single-open (starter default)  
- **Вариант B:** Multi-open  
- **Рекомендация:** A unless PDF interaction spec provided  
- **Причина:** Not visible in static PDF

**D-021** — *Design token authority for Shell vs UI Demo*  
- **Вопрос:** Desktop Shell (header/footer) follows PDF or Production Standards while conflicts open?  
- **Вариант A:** Production Standards v3 for shell — fast start  
- **Вариант B:** Block shell until D-007…D-011 resolved  
- **Рекомендация:** A with documented delta list — operator accepts visual drift risk  
- **Причина:** Audit allows shell with conditions (§10)

**D-022** — *XLSX placeholder rows*  
- **Вопрос:** Deploy placeholder URLs in v1?  
- **Вариант A:** Exclude from v1 sitemap until named  
- **Вариант B:** Keep as draft/noindex placeholders  
- **Рекомендация:** A  
- **Причина:** PG-114,115,123…125,135…137 have `/` and label «Название»

---

## PHASE 9 — FINAL RECOMMENDATION

### Можно ли начинать новый Workspace?

**YES WITH DECISIONS**

Workspace **scaffold** (Gulp client copy, `src/assets/design/` PDF placement) не заблокирован — все Critical PDF READ, block inventory достаточен (Design Audit §10).

**Решения оператора до meaningful layout work:**

| Priority | Decision IDs | Topic |
|----------|--------------|-------|
| **P0 — before UI Demo** | D-007, D-008, D-009, D-010, D-011, D-012 | Token SSOT (CF-008…012 + font) |
| **P0 — before production pages without PDF** | D-001, D-002, D-003, D-004, D-005 | IA + missing templates |
| **P1 — before launch** | D-013…D-019, D-022 | Content, CTA behavior, placeholders |
| **P1 — shell start** | D-021 | Accept Production Standards drift vs PDF for header/footer |
| **P2 — documentation** | D-006, D-016 | URL hygiene · inventory amend CF-002 |

### Gate summary

| Gate | Verdict | Rationale |
|------|---------|-----------|
| Design Approval Sheet complete | **YES** | This document |
| Operator sign-off | **NO** | D-001…D-022 pending |
| Workspace scaffold | **YES WITH DECISIONS** | D-021 for token layer |
| Desktop Shell | **YES WITH DECISIONS** | Structure confirmed; metrics/assets gaps |
| UI Demo | **NO** | D-007…D-012 + unsigned coordinator sheet |
| First production page | **YES WITH DECISIONS** | Template-ready pages (PG-001…011) OK; token pick required for fidelity |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 (REPORTS track — post A1 Audit) |
| Supersedes | — (first REPORTS-track Approval Sheet) |
| Related | FP-0002-DESIGN-APPROVAL-SHEET-v2.md (coordinator form — parallel, unsigned) |
| Changed in this task | **Created:** `REPORTS/FP-0002-DESIGN-APPROVAL-SHEET-v1.md` |
| Commit / push | Not performed |

---

DESIGN APPROVAL READY — **NO**

WORKSPACE READY — **YES WITH DECISIONS**

UI DEMO READY — **NO**

HEADER READY — **NO**

FOOTER READY — **NO**

OPERATOR DECISIONS REQUIRED — **22**

BLOCKERS FOUND — **YES**

UNKNOWN ITEMS:

- Logo / icon SVG sources (SOURCE-026 empty)
- Header stack heights · sticky-on-scroll behavior
- Mobile hamburger menu overlay pattern
- Modal «Заказать звонок» layout (M-06)
- Review «Читать весь отзыв» behavior (M-02)
- UI interaction states (hover, focus, error, loading)
- Home v2 duplicate UTP/hero blocks intent
- Legal sub-document URL set beyond hub
- Specialist listing/profile page designs
- Genotyping standalone page layout
- About subpage designs (×6)
- Search / language versions
- Font family name from PDF (Type3)
- Accordion single vs multi-open (pending D-020)
- XLSX placeholder row final URLs (PG-114,115,123…125,135…137)
- SEO impact of URL typo fixes (`specyalisty`, double slash)
- Coordinator Design Approval Sheet v2 — 8 answers blank
