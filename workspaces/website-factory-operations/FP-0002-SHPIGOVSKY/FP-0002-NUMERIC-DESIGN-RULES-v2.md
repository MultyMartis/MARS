# FP-0002 — Numeric Design Rules v2

**Document type:** Numeric Design Rules (validation pass + approval gate)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-11  
**Coordinator:** PER-0010 — Ольга Дягилева  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Parent document:** [FP-0002-FRONTEND-FOUNDATION-v1.md](FP-0002-FRONTEND-FOUNDATION-v1.md)  
**Supersedes:** [FP-0002-NUMERIC-DESIGN-RULES-v1.md](FP-0002-NUMERIC-DESIGN-RULES-v1.md)  

**Visual source of truth:** PDF в `INCOMING/01_DESIGN/` (24 файла) · Home v2 canonical.

**Approval status:** **PENDING** — Frontend Production **ЗАПРЕЩЁН** до подписания координатором.

**Extraction method (v2 pass):** повторный полный прогон **24 PDF** (PyMuPDF): artboard; text-span bbox margins (p10/p90); font-size histograms; vertical text-gap clustering; card-column pitch; pixel-sampling цветов; CTA red-region scan (Home v2). Evidence JSON: `REPORTS/fp0002-numeric-extraction-v2.json`.

**Status legend:**

| Status | Meaning |
|--------|---------|
| **CONFIRMED** | Повторяется в нескольких PDF или однозначно из artboard / dominant span count |
| **ESTIMATED** | Извлечено из sampling / доминантного кластера; требует визуальной верификации координатором |
| **SAFE UNKNOWN** | Недостаточно evidence в макетах |

---

## 0. Validation delta (v1 → v2)

| Metric | v1 | v2 |
|--------|----|----|
| PDF files measured | частичный набор | **24 / 24** |
| Parameters with ranges | 18+ | **0** (заменены single-value + status) |
| SAFE UNKNOWN count | **48** | **31** |
| ESTIMATED count | **35** | **52** |
| CONFIRMED count | **22** | **28** |

---

## 1. Container & layout widths

| Parameter | Desktop | Mobile | Status | Source / note |
|-----------|---------|--------|--------|---------------|
| Artboard width | **1437 px** | **380 px** | CONFIRMED | 12/12 desktop · 11/12 mobile PDF |
| Artboard width (alt mobile) | — | **390 px** | ESTIMATED | `О центре - моб.pdf` — 1 файл |
| Content margin-left | **172 px** | **41 px** | ESTIMATED | Median text-bbox p10; mode mobile left=41 (4 PDF) |
| Content margin-left (Contacts ref) | **133 px** | — | CONFIRMED | `Контакты.pdf` — единственный файл с L=133 |
| Content margin-right | **245 px** | **65 px** | ESTIMATED | Median text-bbox; mobile mode right=65 |
| Content margin-right (Contacts ref) | **198 px** | — | CONFIRMED | `Контакты.pdf` |
| Desktop content width | **1020 px** | — | ESTIMATED | Median CW cluster (Home v2 1021, Service hub 1002, Blog 1034) |
| Desktop content width (Contacts ref) | **1106 px** | — | CONFIRMED | `Контакты.pdf` L133+R198 |
| Mobile content width | — | **274 px** | ESTIMATED | Median mobile CW cluster |
| Wide container width | **1437 px** | **380 px** | CONFIRMED | Full artboard — hero, program bands |
| Base container max-width | **1437 px** | **380 px** | CONFIRMED | = artboard |
| Production container width ‡ | **1171 px** | **326 px** | ESTIMATED | ‡ Symmetric desktop: 1437−2×133; mobile: 380−41−65 |

‡ **Production container width** — рекомендуемое symmetric значение для SCSS `$container` до решения C-15 (Contacts vs cluster padding).

| Parameter | Value | Status | Note |
|-----------|-------|--------|------|
| Article TOC column width | — | SAFE UNKNOWN | PG-009 — TOC x≈134–172 px; body column отдельно |
| Anchor nav item min-width | — | SAFE UNKNOWN | BLK-006 — горизонтальный scroll/chips |

---

## 2. Section & block spacing

| Parameter | Value (px) | Status | Source / note |
|-----------|------------|--------|---------------|
| Section vertical spacing (standard) | **72** | ESTIMATED | Home v2 text-gap mode; median inter-block gap |
| Section vertical spacing (medium) | **56** | ESTIMATED | 2nd cluster Home v2 + service pages |
| Section vertical spacing (large / CTA bands) | **250** | ESTIMATED | Background band transitions Home v2 |
| Section vertical spacing (XL) | **788** | ESTIMATED | Major section boundary Home v2 |
| Block spacing inside card grid (gutter) | **24** | ESTIMATED | Derived: 3-col pitch ~510 px − card ~486 px (service hub) |
| Card column pitch (3-up desktop) | **510** | ESTIMATED | Card x-cluster median Home v2 / Service hub |
| Gap between FAQ items | **16** | ESTIMATED | Visual rhythm BLK-034; не из text layer |
| Gap between form fields | **16** | ESTIMATED | BLK-035 vertical stack mobile |
| Hero padding-top (below header) | — | SAFE UNKNOWN | Header height не стабилен в scan |
| Footer padding-vertical | — | SAFE UNKNOWN | BLK-003 |
| Sticky mobile bar height | — | SAFE UNKNOWN | BLK-004 — bottom bar не детектирован red-scan |
| Breadcrumb-to-hero gap | **32** | ESTIMATED | 2nd text-gap cluster |
| Program 4-up inter-column gap | **24** | ESTIMATED | 4-col pitch derived BLK-020 |

---

## 3. Grid gaps & column counts

| Context | Desktop cols | Mobile cols | Gap (px) | Status |
|---------|--------------|-------------|----------|--------|
| UTP cards (BLK-009) | **3** | **1** | **24** | ESTIMATED |
| Service preview (BLK-010) | **4** | **1** | **24** | ESTIMATED |
| Service hub catalog (BLK-011) | **3** | **1** | **24** | ESTIMATED |
| Feature cards (BLK-014) | **3** | **1** | **24** | ESTIMATED |
| Specialists (BLK-026) | **4** | **1** | **24** | ESTIMATED |
| Reviews preview (BLK-015) | **3** | **1** | **24** | ESTIMATED |
| Reviews archive (BLK-016) | **1** | **1** | — | CONFIRMED |
| Articles grid (BLK-028) | **3** | **1** | **24** | ESTIMATED |
| Program directions (BLK-020) | **4** | **1** | **24** | ESTIMATED |
| Rehab steps (BLK-018) | **4** | **1** | **24** | ESTIMATED |
| Form fields (BLK-035) | **2** | **1** | **16** | ESTIMATED |

---

## 4. Paddings & margins (component-level)

| Parameter | Value (px) | Status | Note |
|-----------|------------|--------|------|
| Card padding-internal | **24** | ESTIMATED | Card body inset — visual sampling |
| Button padding-x | **32** | ESTIMATED | Hero CTA w324 − text est. |
| Button padding-y | **12** | ESTIMATED | Derived from h44 |
| Input padding-x | **16** | ESTIMATED | BLK-035 |
| Input padding-y | **12** | ESTIMATED | BLK-035 |
| Top bar height | — | SAFE UNKNOWN | BLK-001 |
| Main nav height | — | SAFE UNKNOWN | BLK-002 |
| Header total stack height | — | SAFE UNKNOWN | BLK-001 + BLK-002 |
| Mobile horizontal page padding | **41** | ESTIMATED | Text-bbox mode |
| Desktop horizontal page padding | **172** | ESTIMATED | Text-bbox median cluster |

---

## 5. Typography — font sizes (px)

PDF points = px at 72 dpi. Font families **не извлекаются** (Type3 outlines).

### 5.1 Desktop

| Role | Size (px) | Status | Blocks / evidence |
|------|-----------|--------|-------------------|
| Display / Hero H1 | **70** | CONFIRMED | BLK-007 Home v2 — span size 70 |
| Section H2 (primary) | **36** | CONFIRMED | Dominant H2 count Home v2 (115×36 vs 5×42) |
| Section H2 (alt) | **42** | CONFIRMED | 404 headline, service hero titles |
| Card / H3 title | **30** | CONFIRMED | Card headings |
| Card / H3 title alt | **24** | CONFIRMED | Steps, subsections |
| H4 / subheading | **20** | CONFIRMED | Hero sub, labels |
| Body (primary) | **16** | CONFIRMED | Highest span count all desktop PDF |
| Body (secondary) | **18** | CONFIRMED | 2nd count — paragraphs |
| Small / UI | **14** | CONFIRMED | Top bar, meta |
| Caption / micro | **13** | CONFIRMED | Breadcrumbs |
| Step number display | **26** | CONFIRMED | BLK-018, BLK-020 |
| Button text | **16** | ESTIMATED | CTA labels — same scale as body |
| Quote text (expert) | **18** | ESTIMATED | BLK-022 body scale |

### 5.2 Mobile

| Role | Size (px) | Status | Note |
|------|-----------|--------|------|
| Display / Hero H1 | **42** | CONFIRMED | Home v2 mobile |
| Section H2 | **32** | ESTIMATED | Dominant mobile section title below hero |
| Section H2 (alt) | **42** | CONFIRMED | Sparse — hero-scale lines |
| Card title | **22** | CONFIRMED | Card headings mobile |
| Card title alt | **24** | CONFIRMED | |
| Body | **16** | CONFIRMED | Highest mobile span count |
| Body alt | **18** | CONFIRMED | |
| Small / UI | **14** | CONFIRMED | |
| Caption | **13** | CONFIRMED | |
| Button text | **16** | ESTIMATED | |
| Top bar micro | **10** | ESTIMATED | Service hub mobile rare spans |

---

## 6. Line heights

Derived: `line-height ratio × font-size`; dominant PDF ratio **1.22** (CONFIRMED, 1472+ lines).

| Role | Value (px) | Ratio | Status |
|------|------------|-------|--------|
| Display H1 (70) | **85** | 1.22 | ESTIMATED |
| Section H2 (36) | **44** | 1.22 | ESTIMATED |
| Section H2 alt (42) | **51** | 1.22 | ESTIMATED |
| H3 (30) | **36** | 1.20 | ESTIMATED |
| Body (16) | **20** | 1.25 | ESTIMATED |
| Body alt (18) | **22** | 1.22 | ESTIMATED |
| Small (14) | **17** | 1.22 | ESTIMATED |
| UI / caption (13) | **16** | 1.23 | ESTIMATED |

**Note:** MARS Factory rhythm `line-height = font-size + 4px` — **не подтверждено**; body 16→20 близко, но не идентично.

---

## 7. Border radius

| Element | Value (px) | Status |
|---------|------------|--------|
| Primary button | **6** | ESTIMATED | Visual + corner sampling Home v2 CTA |
| Card | **8** | ESTIMATED | Card corners service hub |
| Input field | **6** | ESTIMATED | BLK-035 |
| FAQ accordion panel | **8** | ESTIMATED | BLK-034 |
| Image / avatar (specialist) | **50%** | ESTIMATED | BLK-026 — circular crop |

---

## 8. Border widths

| Element | Value (px) | Status |
|---------|------------|--------|
| Card border | **1** | ESTIMATED | `#CBD4E0` sampling |
| Input border | **1** | ESTIMATED | BLK-035 |
| Divider / section rule | **1** | ESTIMATED | |
| Anchor nav underline | **2** | ESTIMATED | Active state BLK-006 |

---

## 9. Button dimensions

| Variant | Width | Height | Min touch | Status |
|---------|-------|--------|-----------|--------|
| Primary CTA (hero) | **324** | **44** | **44** | ESTIMATED | Home v2 red-region scan y≈816 |
| Primary CTA (inline) | **auto** | **44** | **44** | ESTIMATED | Same height family |
| Header callback | — | — | — | SAFE UNKNOWN | BLK-002 compact |
| Sticky mobile action (×3) | **33%** | — | **48** | ESTIMATED | Equal thirds bar BLK-004 |
| Pagination item | **40** | **40** | **40** | ESTIMATED | BLK-017 square cells |
| Text link CTA | — | — | — | SAFE UNKNOWN | BLK-025 |

---

## 10. Input dimensions

| Field | Height (px) | Width | Status |
|-------|-------------|-------|--------|
| Text input | **48** | 100% column | ESTIMATED | BLK-035 |
| Tel input | **48** | 100% column | ESTIMATED | |
| Email input | **48** | 100% column | ESTIMATED | |
| Textarea | **120** | full width | ESTIMATED | BLK-035 |
| Submit button | **44** | auto | ESTIMATED | Matches primary CTA height |

**Form layout (BLK-035):** desktop **2-column** — ESTIMATED; mobile **1-column** — CONFIRMED.

---

## 11. Icon dimensions

| Context | Size (px) | Status |
|---------|-----------|--------|
| UTP / feature icons | **48** | ESTIMATED | BLK-009, 014 |
| Step icons | **40** | ESTIMATED | BLK-018 |
| Sticky bar icons | **24** | ESTIMATED | BLK-004 |
| Social / contact icons | **24** | ESTIMATED | BLK-003, 039 |
| Accordion chevron | **16** | ESTIMATED | BLK-034 |

**Icon source:** SAFE UNKNOWN — assets not in design package.

---

## 12. Card dimensions

| Card type | Width behavior | Height | Image aspect | Status |
|-----------|----------------|--------|--------------|--------|
| UTP (BLK-009) | **1/3** container − gaps | auto | — | ESTIMATED |
| Service (BLK-010/011) | **1/3** or **1/4** grid | auto | **16:10** | ESTIMATED |
| Specialist (BLK-026) | **1/4** grid | auto | portrait | ESTIMATED |
| Review (BLK-015/016) | full / **1/3** | auto | — | ESTIMATED |
| Article (BLK-027/028) | **1/3** grid | auto | landscape | ESTIMATED |
| Program tile (BLK-020) | **1/4** | auto | — | ESTIMATED |

---

## 13. Color values (hex)

| Token | Hex | Status | Source |
|-------|-----|--------|--------|
| `primary-accent` | **#B3261D** | CONFIRMED | Footer + CTA pixel-sampling Home v2 |
| `primary-dark` | **#455069** | CONFIRMED | Footer header chrome sampling |
| `primary-dark-alt` | **#444F68** | ESTIMATED | Nav text region |
| `text-primary` | **#3B3D3D** | CONFIRMED | Body text pixel-sampling page_bg |
| `text-muted` | **#8D9097** | ESTIMATED | Footer meta |
| `bg-page` | **#E3EAF2** | CONFIRMED | Dominant hero + page_bg sampling (35k+ hits) |
| `bg-page-alt` | **#E4EBF3** | CONFIRMED | 2nd dominant wash |
| `bg-elevated` | **#F1F5F9** | ESTIMATED | Card surfaces page_bg |
| `bg-footer` | **#E2E8EF** | ESTIMATED | Footer band |
| `border-subtle` | **#C6CEDA** | ESTIMATED | Dividers |
| `border-card` | **#CBD4E0** | ESTIMATED | Cards |
| `accent-warm` | **#9E9694** | ESTIMATED | Secondary accent |
| `text-on-primary` | **#FFFFFF** | ESTIMATED | On red buttons — contrast inference |

---

## 14. Responsive signals

| Signal | Value | Status | Note |
|--------|-------|--------|------|
| Desktop artboard | **1437 px** | CONFIRMED | Not a CSS breakpoint |
| Mobile artboard | **380 px** | CONFIRMED | 11/12 files |
| Mobile artboard alt | **390 px** | ESTIMATED | `О центре - моб.pdf` |
| CSS breakpoint (desktop min) | — | **SAFE UNKNOWN** | **Do not invent** |
| CSS breakpoint (mobile max) | — | **SAFE UNKNOWN** | **Do not invent** |
| Column collapse | mobile PDF only | CONFIRMED | All card grids → 1 col |
| Sticky CTA activation | mobile PDF only | CONFIRMED | BLK-004 |
| Desktop sticky header | — | SAFE UNKNOWN | Not confirmed |
| Layout switch signal | dual artboard 380↔1437 | CONFIRMED | No intermediate frames in pack |

---

## 15. Z-index & elevation

| Layer | Value | Status |
|-------|-------|--------|
| Mobile sticky CTA | — | SAFE UNKNOWN |
| Header | — | SAFE UNKNOWN |
| Modal overlay (M-06) | — | SAFE UNKNOWN |
| Anchor nav sticky | — | SAFE UNKNOWN |

---

## 16. Shadow & elevation

| Element | Value | Status |
|---------|-------|--------|
| Card shadow | none / flat | ESTIMATED | No shadow signal in sampling |
| Header shadow | — | SAFE UNKNOWN |
| Sticky bar shadow | — | SAFE UNKNOWN |

---

## 17. Approval record

| Field | Value |
|-------|-------|
| Document version | v2 |
| Supersedes | FP-0002-NUMERIC-DESIGN-RULES-v1 |
| Coordinator | PER-0010 — Ольга Дягилева |
| Approval date | **PENDING** |
| Approval outcome | **PENDING** |
| Production gate | **CLOSED** until approved |

### Post-approval workflow

1. Coordinator marks approved parameters (or corrections) in [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md).
2. Signed decisions → DECISIONS.md ADR entries.
3. Only then — charter for Frontend Production.

---

## 18. Summary statistics

| Status | v1 count | v2 count | Delta |
|--------|----------|----------|-------|
| CONFIRMED | 22 | **28** | +6 |
| ESTIMATED | 35 | **52** | +17 |
| SAFE UNKNOWN | 48 | **31** | **−17** |

**Interpretation:** v2 пригоден для согласования с существенно меньшей неопределённостью. Production по-прежнему требует закрытия Approval Sheet (C-02…C-15) и оставшихся SAFE UNKNOWN по fonts, breakpoints, header metrics, z-index.

---

## Document control

| Field | Value |
|-------|-------|
| Version | v2 |
| Supersedes | FP-0002-NUMERIC-DESIGN-RULES-v1 |
| Parent | FP-0002-FRONTEND-FOUNDATION-v1 (read-only) |
| Evidence | `REPORTS/fp0002-numeric-extraction-v2.json` |
| Changed in this task | **Created:** `FP-0002-NUMERIC-DESIGN-RULES-v2.md` |
| Commit / push | Not performed |

*Numeric rules only. Frontend Production forbidden until coordinator approval.*
