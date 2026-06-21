# FP-0002 — Header Mini-Audit (Phase C.1)

**Date:** 2026-06-14  
**Scope:** Header only — pre-implementation audit  
**Evidence:** `REPORTS/_audit_extract_output.json` · `REPORTS/FP-0002-DESIGN-AUDIT-v1.md` · `REPORTS/FP-0002-DESIGN-APPROVAL-SHEET-v1.md`  
**PDF on disk:** **NOT AVAILABLE** at `INCOMING/01_DESIGN/` (folder empty except README) — audit uses prior READ session artefacts only.

---

## 1. PDF sources with header chrome

| SOURCE-ID | Desktop PDF | Header present | Notes |
|-----------|-------------|----------------|-------|
| SOURCE-001 | `2026-06-11-home-v2/Главная страница (v2).pdf` | ✓ | Canonical reference — full BLK-001+002 |
| SOURCE-003 | `Главная стр.pdf` | ✓ | **SUPERSEDED** by SOURCE-001 |
| SOURCE-005 | `Услуги хаб.pdf` | ✓ | Same chrome |
| SOURCE-007 | `Услуга подраздел.pdf` | ✓ | Same chrome |
| SOURCE-009 | `Услуга конечная.pdf` | ✓ | Same chrome |
| SOURCE-011 | `О центре.pdf` | ✓ | Same chrome |
| SOURCE-013 | `Контакты.pdf` | ✓ | Same chrome |
| SOURCE-015 | `Отзывы.pdf` | ✓ | Same chrome |
| SOURCE-017 | `Блог хаб.pdf` | ✓ | Same chrome |
| SOURCE-019 | `Статья.pdf` | ✓ | Same chrome + breadcrumb below |
| SOURCE-021 | `Правовая инфа.pdf` | ✓ | Same chrome |
| SOURCE-023 | `404.pdf` | **PARTIAL** | Minimal / error chrome — not shell SSOT |

**Mobile PDFs (SOURCE-002,004,006…):** header present but **out of scope** for Phase C.1.

---

## 2. Differences between desktop PDF headers

| Aspect | Standard templates (001,005,007,009,011,013,015,017,019,021) | Inner pages with breadcrumbs (017,019,021…) | 404 (023) |
|--------|----------------------------------------------------------------|---------------------------------------------|-----------|
| BLK-001 top bar | Full: regions, hours, genotyping, specialists, 2 phones | Same chrome | **UNKNOWN** — minimal extraction |
| BLK-002 main nav | Logo + 5 nav + CTA | Same + breadcrumb row **below** header (BLK-005, not header) | Different/error layout |
| Breadcrumb in header zone | No | Yes — page title trail only on inner pages | N/A |

**Conclusion:** Shell header SSOT = **standard dual-row** pattern on SOURCE-001 and matching desktop templates. No PDF shows different L1 nav labels on desktop.

---

## 3. Logo

| Item | Status |
|------|--------|
| Brand mark (graphic) | **PARTIAL** — visible in PDF; no SVG/PNG in `INCOMING/03_BRANDING/` |
| Text «Центр профилактики и лечения зависимостей» | **CONFIRMED** — PDF text-layer decode (SOURCE-001) |
| Text «(Шпиговский дом)» | **CONFIRMED** — PDF text-layer decode `(?83>2A:89 4><` |
| Text «Лечение и профилактика» | **PARTIAL** — in header text extraction; exact placement vs logo **UNKNOWN** |

---

## 4. Phones

| Number | PDF | Implementation |
|--------|-----|----------------|
| +7 (925) 183-64-64 | **CONFIRMED** | `tel:+79251836464` |
| +7 (995) 023-92-26 | **CONFIRMED** | `tel:+79950239226` |

---

## 5. Top bar (BLK-001)

| Element | PDF text | URL (XLSX check) |
|---------|----------|------------------|
| Москва, | **CONFIRMED** (comma in PDF) | — |
| Московская область | **CONFIRMED** | — |
| пн-пт: 08:00-18:00, сб-вс 08:00-22:00 | **CONFIRMED** machine fragments | — |
| Генотипирование | **CONFIRMED** | `/uslugi/genotipirovanie/` |
| Специалисты | **CONFIRMED** | `/specyalisty/` |

---

## 6. Main navigation (BLK-002)

| Label | PDF | URL (XLSX) |
|-------|-----|------------|
| Услуги | **CONFIRMED** (visual intake + audit) | `/uslugi/` |
| О центре | **CONFIRMED** | `/o-centre/` |
| Отзывы | **CONFIRMED** | `/otzyvy/` |
| Статьи | **CONFIRMED** | `/blog/` |
| Контакты | **CONFIRMED** | `/kontakty/` |

---

## 7. CTA

| Element | PDF | Notes |
|---------|-----|-------|
| «Заказать звонок» | **CONFIRMED** button label | Modal **not in PDF** (M-06) — `type="button"` only |

---

## 8. Heights

| Parameter | Status |
|-----------|--------|
| Top bar height | **UNKNOWN** (SOURCE-036) |
| Main nav row height | **UNKNOWN** |
| Total header stack | **UNKNOWN** |
| Engineering placeholders used in SCSS | `min-height: 36px` top · `min-height: 72px` main |

---

## 9. Spacing / layout

| Parameter | PDF evidence | Production v3 (D-021 Variant A) |
|-----------|--------------|----------------------------------|
| Container max | ~1170px content | **1170px** |
| Page padding-x | ~172px median cluster | **40px** (`space-8`) |
| Top bar / nav gaps | **UNKNOWN** exact | Engineering `16–24px` |

---

## 10. Behavior

| Behavior | Status |
|----------|--------|
| Dual-row static header | **CONFIRMED** |
| Sticky on scroll | **UNKNOWN** |
| Mobile burger / drawer | Present in mobile PDF — **not implemented** (Phase C.1 scope) |
| Callback modal | **UNKNOWN** (M-06) |

---

## 11. Known (summary)

- Dual-row header BLK-001 + BLK-002 on all main desktop templates.
- Nav IA aligns PDF ↔ XLSX for L1 items.
- Two phones and top-bar utility links confirmed.
- CTA label «Заказать звонок» confirmed.

---

## 12. UNKNOWN

- PDF files **not on disk** for live re-verification in this session.
- Logo raster/SVG asset.
- Exact pixel heights and sticky behavior.
- Placement of «Лечение и профилактика» in chrome.
- Whether hours repeat per region or once (implemented: **once**, per text-layer order).
- CTA click behavior.
- Hover/focus visual spec from PDF.
- Capitalization of «дом» in «(Шпиговский дом)» — text layer lowercase.

---

*Mini-audit complete — implementation follows this document + Production Standards v3 engineering tokens.*
