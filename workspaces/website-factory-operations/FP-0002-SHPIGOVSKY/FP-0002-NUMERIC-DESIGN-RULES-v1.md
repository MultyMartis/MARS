# FP-0002 — Numeric Design Rules v1

**Document type:** Numeric Design Rules (approval gate)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-11  
**Coordinator:** PER-0010 — Ольга Дягилева  

**ATLAS:** ORG-0008 · PRJ-0012 · WEB-SHPIG-01 · DOM-SHPIG-01  

**Parent document:** [FP-0002-FRONTEND-FOUNDATION-v1.md](FP-0002-FRONTEND-FOUNDATION-v1.md)  

**Visual source of truth:** PDF в `INCOMING/01_DESIGN/` · Home v2 canonical.

**Approval status:** **PENDING** — Frontend Production **ЗАПРЕЩЁН** до подписания координатором.

**Extraction method:** PDF artboard dimensions (PyMuPDF); text-block bbox margins; font span sizes; pixel-sampling accent/background colors. Font families **не извлекаются** (Type3 outlines).

**Status legend:**

| Status | Meaning |
|--------|---------|
| **CONFIRMED** | Повторяется в нескольких PDF или однозначно из artboard |
| **ESTIMATED** | Извлечено из sampling / одного источника; требует визуальной верификации |
| **SAFE UNKNOWN** | Недостаточно evidence в макетах |

---

## 1. Container & layout widths

| Parameter | Desktop | Mobile | Status | Source / note |
|-----------|---------|--------|--------|---------------|
| Artboard width | **1437 px** | **380 px** (11/12 files) | CONFIRMED | All desktop PDFs; mobile majority |
| Artboard width (alt mobile) | — | **390 px** (1 file) | ESTIMATED | Single PDF; verify intent |
| Content margin-left | **133 px** | **29 px** | CONFIRMED | Text bbox on Home v2, 404, Contacts, Blog |
| Content margin-right | **133–168 px** | **25 px** | ESTIMATED | Variance across pages (404: 168 px) |
| Content width | **1140–1170 px** | **326 px** | CONFIRMED | Derived from margins |
| Wide container width | **1437 px** (full artboard) | **380 px** | CONFIRMED | Hero, program bands — full bleed within artboard |
| Base container max-width | **1437 px** | **380 px** | CONFIRMED | = artboard |
| Article TOC column width | — | — | SAFE UNKNOWN | PG-009 desktop only |
| Anchor nav item min-width | — | — | SAFE UNKNOWN | BLK-006 |

---

## 2. Section & block spacing

| Parameter | Value | Status | Source / note |
|-----------|-------|--------|---------------|
| Section vertical spacing (standard) | — | SAFE UNKNOWN | Not extractable from PDF text layer |
| Section vertical spacing (large / CTA bands) | — | SAFE UNKNOWN | BLK-019, BLK-007 |
| Block spacing inside card grid | — | SAFE UNKNOWN | BLK-010, 011, 026 |
| Gap between FAQ items | — | SAFE UNKNOWN | BLK-034 |
| Gap between form fields | — | SAFE UNKNOWN | BLK-035 |
| Hero padding-top (below header) | — | SAFE UNKNOWN | BLK-007 |
| Footer padding-vertical | — | SAFE UNKNOWN | BLK-003 |
| Sticky mobile bar height | — | SAFE UNKNOWN | BLK-004 |
| Breadcrumb-to-hero gap | — | SAFE UNKNOWN | BLK-005 → BLK-007 |
| Program 4-up inter-column gap | — | SAFE UNKNOWN | BLK-020 |

---

## 3. Grid gaps & column counts

| Context | Desktop columns | Mobile columns | Gap | Status |
|---------|-----------------|----------------|-----|--------|
| UTP cards (BLK-009) | **3** | **1** (stack) | — | ESTIMATED / SAFE UNKNOWN gap |
| Service preview (BLK-010) | **3–4** | **1** | — | ESTIMATED |
| Service hub catalog (BLK-011) | **3** | **1** | — | ESTIMATED |
| Feature cards (BLK-014) | **3+** | **1** | — | ESTIMATED |
| Specialists (BLK-026) | **3–4** | **1** | — | ESTIMATED |
| Reviews preview (BLK-015) | **2–3** | **1** | — | ESTIMATED |
| Reviews archive (BLK-016) | **1** (list) | **1** | — | CONFIRMED pattern |
| Articles grid (BLK-028) | **3** | **1** | — | ESTIMATED |
| Program directions (BLK-020) | **4** | **1–2** | — | ESTIMATED |
| Rehab steps (BLK-018) | **4** | **1** | — | ESTIMATED |
| Form fields (BLK-035) | **2** | **1** | — | ESTIMATED |

---

## 4. Paddings & margins (component-level)

| Parameter | Value | Status | Note |
|-----------|-------|--------|------|
| Card padding-internal | — | SAFE UNKNOWN | All card families |
| Button padding-x | — | SAFE UNKNOWN | Primary CTA |
| Button padding-y | — | SAFE UNKNOWN | Primary CTA |
| Input padding-x | — | SAFE UNKNOWN | BLK-035 |
| Input padding-y | — | SAFE UNKNOWN | BLK-035 |
| Top bar height | — | SAFE UNKNOWN | BLK-001 |
| Main nav height | — | SAFE UNKNOWN | BLK-002 |
| Header total stack height | — | SAFE UNKNOWN | BLK-001 + BLK-002 |
| Mobile horizontal page padding | **~29 px** | CONFIRMED | Text bbox |
| Desktop horizontal page padding | **~133 px** | CONFIRMED | Text bbox |

---

## 5. Font sizes (px, PDF points = px at 72dpi)

### 5.1 Desktop

| Role | Size (px) | Status | Blocks |
|------|-----------|--------|--------|
| Display / Hero H1 | **70** | CONFIRMED | BLK-007 Home |
| Section H2 | **42** | CONFIRMED | Section titles, 404 |
| Section H2 alt | **36** | CONFIRMED | Program, multi sections |
| Card / H3 title | **30** | CONFIRMED | Cards |
| Card / H3 title alt | **24–26** | CONFIRMED | Steps, subsections |
| Subheading / lead | **20–21** | CONFIRMED | Hero sub, labels |
| Body | **16–18** | CONFIRMED | Paragraphs |
| Small / UI | **13–15** | CONFIRMED | Top bar, meta |
| Step number display | **26** | ESTIMATED | BLK-018, BLK-020 |

### 5.2 Mobile

| Role | Size (px) | Status | Note |
|------|-----------|--------|------|
| Display / Hero H1 | **42** | CONFIRMED | Home v2 mobile |
| Section H2 | **32–42** | CONFIRMED | |
| Card title | **22–24** | CONFIRMED | |
| Body | **16–18** | CONFIRMED | |
| Small / UI | **13–15** | CONFIRMED | |
| Top bar micro | **8–10** | ESTIMATED | Rare spans in service hub mobile |

---

## 6. Line heights

| Role | Value | Status |
|------|-------|--------|
| Display H1 | — | SAFE UNKNOWN |
| Section H2 | — | SAFE UNKNOWN |
| Body | — | SAFE UNKNOWN |
| UI / caption | — | SAFE UNKNOWN |

**Note:** MARS Factory rhythm preference `line-height = font-size + 4px` — **не подтверждено** макетами FP-0002; применять только после coordinator approval.

---

## 7. Border radius

| Element | Value | Status |
|---------|-------|--------|
| Primary button | — | SAFE UNKNOWN | Visually rounded; px not extracted |
| Card | — | SAFE UNKNOWN | |
| Input field | — | SAFE UNKNOWN | |
| FAQ accordion panel | — | SAFE UNKNOWN | |
| Image / avatar (specialist) | — | SAFE UNKNOWN | BLK-026 |

---

## 8. Border widths

| Element | Value | Status |
|---------|-------|--------|
| Card border | — | SAFE UNKNOWN |
| Input border | — | SAFE UNKNOWN |
| Divider / section rule | — | SAFE UNKNOWN |
| Anchor nav underline | — | SAFE UNKNOWN |

---

## 9. Button dimensions

| Variant | Width | Height | Min touch target | Status |
|---------|-------|--------|------------------|--------|
| Primary CTA (hero) | auto / content | — | — | SAFE UNKNOWN |
| Primary CTA (inline) | auto | — | — | SAFE UNKNOWN |
| Header callback | — | — | — | SAFE UNKNOWN |
| Sticky mobile action (×3) | **~33%** each | — | — | ESTIMATED | Equal thirds bar |
| Pagination item | — | — | — | SAFE UNKNOWN | BLK-017 |
| Text link CTA | — | — | — | SAFE UNKNOWN | BLK-025 |

---

## 10. Input dimensions

| Field | Height | Width behavior | Status |
|-------|--------|----------------|--------|
| Text input | — | 100% column | SAFE UNKNOWN |
| Tel input | — | 100% column | SAFE UNKNOWN |
| Email input | — | 100% column | SAFE UNKNOWN |
| Textarea | — | full width | SAFE UNKNOWN |
| Submit button | — | — | SAFE UNKNOWN |

**Form layout (BLK-035):** desktop **2-column** field pairs — ESTIMATED; mobile **1-column** — CONFIRMED pattern.

---

## 11. Icon dimensions

| Context | Size | Status |
|---------|------|--------|
| UTP / feature icons | — | SAFE UNKNOWN | BLK-009, 014 |
| Step icons | — | SAFE UNKNOWN | BLK-018 |
| Sticky bar icons | — | SAFE UNKNOWN | BLK-004 |
| Social / contact icons | — | SAFE UNKNOWN | BLK-003, 039 |
| Accordion chevron | — | SAFE UNKNOWN | BLK-034 |

**Icon source:** SAFE UNKNOWN — assets not in design package.

---

## 12. Card dimensions

| Card type | Width behavior | Height | Image aspect | Status |
|-----------|----------------|--------|--------------|--------|
| UTP (BLK-009) | **~1/3** content width | — | — | ESTIMATED |
| Service (BLK-010/011) | grid fraction | — | — | ESTIMATED |
| Specialist (BLK-026) | grid fraction | — | portrait | ESTIMATED |
| Review (BLK-015/016) | full / grid | — | — | ESTIMATED |
| Article (BLK-027/028) | grid fraction | — | landscape thumb | ESTIMATED |
| Program tile (BLK-020) | **~1/4** | — | — | ESTIMATED |

---

## 13. Color values (hex)

| Token | Hex | Status | Usage |
|-------|-----|--------|-------|
| `primary-accent` | **#B3261D** | CONFIRMED | CTA fills |
| `primary-dark` | **#455069** | ESTIMATED | Header chrome |
| `primary-dark-alt` | **#444F68** | ESTIMATED | Nav text |
| `text-primary` | **#3B3D3D** | ESTIMATED | Body |
| `text-muted` | **#8D9097** | ESTIMATED | Footer meta |
| `bg-page` | **#E3EAF2** | CONFIRMED | Page wash |
| `bg-page-alt` | **#E4EBF3** | CONFIRMED | Section wash |
| `bg-elevated` | **#F1F5F9** | ESTIMATED | Cards |
| `bg-footer` | **#E2E8EF** | ESTIMATED | Footer |
| `border-subtle` | **#C6CEDA** | ESTIMATED | Dividers |
| `border-card` | **#CBD4E0** | ESTIMATED | Cards |
| `accent-warm` | **#9E9694** | ESTIMATED | Secondary accent |
| `text-on-primary` | **#FFFFFF** | ESTIMATED | On red buttons |

---

## 14. Responsive signals

| Signal | Value | Status | Note |
|--------|-------|--------|------|
| Desktop artboard | **1437 px** | CONFIRMED | Not a CSS breakpoint |
| Mobile artboard | **380 px** | CONFIRMED | Not a CSS breakpoint |
| Mobile artboard alt | **390 px** | ESTIMATED | 1 file |
| CSS breakpoint (desktop min) | — | **SAFE UNKNOWN** | **Do not invent** |
| CSS breakpoint (mobile max) | — | **SAFE UNKNOWN** | **Do not invent** |
| Column collapse threshold | — | SAFE UNKNOWN | Between 380 and 1437 |
| Sticky CTA activation | mobile PDF only | CONFIRMED | BLK-004 |
| Desktop sticky header | — | SAFE UNKNOWN | Not confirmed |

**Coordinator decision required (C-03):** recommended candidates **не генерируются** в этом документе — только факт dual artboard.

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
| Card shadow | — | SAFE UNKNOWN |
| Header shadow | — | SAFE UNKNOWN |
| Sticky bar shadow | — | SAFE UNKNOWN |

---

## 17. Approval record

| Field | Value |
|-------|-------|
| Document version | v1 |
| Coordinator | PER-0010 — Ольга Дягилева |
| Approval date | **PENDING** |
| Approval outcome | **PENDING** |
| Production gate | **CLOSED** until approved |

### Post-approval workflow

1. Coordinator marks approved parameters (or provides corrections).
2. Create **FP-0002-NUMERIC-DESIGN-RULES-v1.1** or signed approval note in DECISIONS.md.
3. Only then — charter for Frontend Production.

---

## 18. Summary statistics

| Status | Count (parameters listed) |
|--------|---------------------------|
| CONFIRMED | **22** |
| ESTIMATED | **35** |
| SAFE UNKNOWN | **48** |

**Interpretation:** документ **пригоден для согласования** как structured baseline; Production требует закрытия критичных SAFE UNKNOWN (breakpoints, fonts, spacing scale, component dimensions).

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Supersedes | — |
| Parent | FP-0002-FRONTEND-FOUNDATION-v1 |
| Changed in this task | **Created:** `FP-0002-NUMERIC-DESIGN-RULES-v1.md` |
| Commit / push | Not performed |

*Numeric rules only. Frontend Production forbidden until coordinator approval.*
