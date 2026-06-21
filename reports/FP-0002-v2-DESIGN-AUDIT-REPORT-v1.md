# REPORT — FP-0002 v2 DESIGN AUDIT START

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Task:** FP-0002 v2 DESIGN AUDIT START (P1)  
**Workspace:** `workspaces/fp-0002-shpigovsky-v2/` — **unchanged** (zero skeleton only)  
**Legacy workspace:** `workspaces/fp-0002-shpigovsky-frontend/` — **not modified**

**Deliverables produced:**

- [FP-0002-v2-PAGE-INVENTORY-v1.md](FP-0002-v2-PAGE-INVENTORY-v1.md)
- [FP-0002-v2-BLOCK-INVENTORY-v1.md](FP-0002-v2-BLOCK-INVENTORY-v1.md)
- [FP-0002-v2-ASSET-INVENTORY-v1.md](FP-0002-v2-ASSET-INVENTORY-v1.md)
- [FP-0002-v2-TYPOGRAPHY-AUDIT-v1.md](FP-0002-v2-TYPOGRAPHY-AUDIT-v1.md)
- [FP-0002-v2-DESIGN-SYSTEM-SNAPSHOT-v1.md](FP-0002-v2-DESIGN-SYSTEM-SNAPSHOT-v1.md)
- [FP-0002-v2-PILOT-PAGE-RECOMMENDATION-v1.md](FP-0002-v2-PILOT-PAGE-RECOMMENDATION-v1.md)
- This report

---

## Executive summary

v2 design audit **completed** without implementation. All primary sources on disk are **readable**. FIG decode (2026-06-22) confirms **11/11** page template pairs — **stronger** than v1 PDF-only inventory. Authority chain **FIG → PDF → JPG → Operator** applied for this pass per operator instruction.

**P1 readiness:** **PASS WITH RECORDED DEVIATIONS** — Discovery may start for pilot slice **PG-005** with deviation register below.

---

# PHASE A1 — AUTHORITY VALIDATION

| Layer | Source | EXISTS | READABLE | Discovery | Build | Text | Structure | Assets |
|-------|--------|--------|----------|-----------|-------|------|-----------|--------|
| **PRIMARY** | `Шпиговский.fig` (~141 MB) | ✓ | ✓ ZIP+kiwi | ✓ | ✓ | ✓ 1971/1983 TEXT | ✓ 7953 nodes | ✓ 166 images |
| **SECONDARY** | 24× PDF (+ Home v2 folder) | ✓ | ✓ `%PDF` magic | ✓ | ✓ | ✓ (not OCR) | ✓ artboards | partial raster |
| **VISUAL CONTROL** | `HOME-PAGE-FULL-MOCKUP.jpg` | ✓ | ✓ JPEG | Home only | QA tie-break | partial | partial | Home desktop |
| **OPERATOR** | Human | — | — | conflicts | conflicts | locks | IA gaps | drops |

### Authority validation notes

- **FIG** supersedes v1 «PDF-only / Figma absent» PROJECT DECISION for v2 work.
- **JPG** covers **Home desktop only** — cannot replace FIG/PDF for other templates.
- **XLSX** (`INCOMING/02_CONTENT/`) — IA/SEO; **not** visual authority (referenced in prior audits only).
- **Standalone brand/font/favicon intake:** **MISSING** — FIG + Production Standards close gap partially.

**AUTHORITY VALIDATED — YES** (for this pass)

---

# PHASE A2 — PAGE INVENTORY v2

See [FP-0002-v2-PAGE-INVENTORY-v1.md](FP-0002-v2-PAGE-INVENTORY-v1.md).

| Summary | Count |
|---------|-------|
| Page types | **11** |
| READY | **9** |
| PARTIAL | **1** (PG-008 PDF mobile naming) |
| BLOCKED | **0** |
| SAFE UNKNOWN | **0** page types |

**Key correction:** PG-009 **READY** (mobile PDF found — v1 Partial obsolete).

---

# PHASE A3 — DESKTOP ↔ MOBILE PAIRING

| PAGE ID | Desktop | Mobile | Section count D/M (FIG) | Composition match | Order match | Missing layout | Naming conflicts |
|---------|---------|--------|-------------------------|-------------------|-------------|----------------|------------------|
| PG-001 | ✓ | ✓ | 15 / 15 | **YES** (roles) | **NO** † | — | `преимущества` vs `Комфорт, приватность` |
| PG-002 | ✓ | ✓ | 12 / — | YES | PARTIAL | — | duplicate `3- Услуги` frames |
| PG-003 | ✓ | ✓ | 14 / — | YES | PARTIAL | — | — |
| PG-004 | ✓ | ✓ | 14 / — | YES | PARTIAL | — | — |
| PG-005 | ✓ | ✓ | **13 / 11** | **PARTIAL** | PARTIAL | — | **HIGH** — see below |
| PG-006 | ✓ | ✓ | 5 / — | YES | YES | — | — |
| PG-007 | ✓ | ✓ | 4 / — | YES | YES | — | — |
| PG-008 | ✓ | PDF ‡ | 7 / FIG ✓ | YES | YES | PDF `Блог хаб - моб.pdf` | ‡ misnamed PDF |
| PG-009 | ✓ | ✓ | 17 / — | YES | YES | — | — |
| PG-010 | ✓ | ✓ | 4 / — | YES | YES | — | — |
| PG-011 | ✓ | ✓ | 4 / — | YES | YES | — | — |

† PG-001: FIG `Слово спецу` layer index vs y-position conflict (known SECTION-10).

**PG-005 naming conflicts (FIG):**

| # | Desktop frame | Mobile frame | Issue |
|---|---------------|--------------|-------|
| 1 | `2 - Дом - вступление` | `Кого мы лечим` | Label mismatch — same narrative role suspected |
| 2 | `3- Услуги` | `Подход` | Label mismatch |
| 3 | — | `Зависимости и пристрастия` | **Mobile-only** top-level section name |
| 4 | `Программа центра` ×2 | `Программа центра` ×1 | Desktop duplicate frames |
| 5 | `преимущества` | `Комфорт, приватность` | Label mismatch |

---

# PHASE A4 — PAGE COMPLEXITY MATRIX

| PAGE ID | Sections | Unique blocks | Forms | Carousels | Modals | Complex interactive | Content volume | Complexity |
|---------|----------|---------------|-------|-----------|--------|---------------------|----------------|------------|
| PG-001 | 15 | 15 | 1 (BLK-035) | review cards | 0 | FAQ accordion | Very high | **VERY HIGH** |
| PG-002 | 12 | 12 | 1 | — | 0 | FAQ | High | **HIGH** |
| PG-003 | 14 | 14 | 1 | review | 0 | FAQ | High | **HIGH** |
| PG-004 | 14 | 14 | 1 | review | 0 | FAQ | High | **HIGH** |
| PG-005 | 13 | 13 | 0–1 † | review | 0 | FAQ partial | High | **MEDIUM** |
| PG-006 | 5 | 5 | 0 | — | 0 | — | Low | **LOW** |
| PG-007 | 4 | 4 | 0 | listing | 0 | pagination | Medium | **MEDIUM** |
| PG-008 | 7 | 7 | 0 | — | 0 | pagination | Medium | **MEDIUM** |
| PG-009 | 17 | 17 | 0 | — | 0 | TOC | Very high | **HIGH** |
| PG-010 | 4 | 4 | 0 | — | 0 | — | Low | **LOW** |
| PG-011 | 4 | 4 | 0 | — | 0 | — | Minimal | **LOW** |

† PG-005: BLK-035 not in v1 About map; FIG shows `Поле ввода` instances — **SAFE UNKNOWN** if form on About.

**Carousel definition:** review slider / arrow instances — not Swiper-proven; static PDF.

**Modal:** M-06 «Заказать звонок» — **no overlay mockup** project-wide.

---

# PHASE A5 — BLOCK INVENTORY v2

See [FP-0002-v2-BLOCK-INVENTORY-v1.md](FP-0002-v2-BLOCK-INVENTORY-v1.md).

| Tier | Count |
|------|-------|
| SHARED | 19 |
| SEMI-SHARED | 12 |
| UNIQUE | 9 |
| **Total Block IDs** | **40** |

v1 block catalogue **validated** — no new Block IDs required for confirmed PDF/FIG templates.

---

# PHASE A6 — ASSET INVENTORY v2

See [FP-0002-v2-ASSET-INVENTORY-v1.md](FP-0002-v2-ASSET-INVENTORY-v1.md).

| Class | Status |
|-------|--------|
| Logos | FOUND in FIG · MISSING standalone |
| Photos | FOUND in FIG |
| Icons | FOUND in FIG |
| Illustrations | FOUND in FIG |
| Backgrounds | FOUND in FIG / CSS |
| Videos | MISSING file · SAFE UNKNOWN |
| Favicons | MISSING |
| **ASSET_IDENTITY_COLLISION** | **COL-001** legacy `d3ac7d00` — **REJECT** legacy img |

---

# PHASE A7 — TYPOGRAPHY AUDIT

See [FP-0002-v2-TYPOGRAPHY-AUDIT-v1.md](FP-0002-v2-TYPOGRAPHY-AUDIT-v1.md).

**FIG-primary summary:**

| Role | Desktop | Mobile |
|------|---------|--------|
| H1 | 70 / 42 px | **CONFIRMED** |
| H2 | 36 px (+42 alt) | 32 / 22 — **conflict with Production 22** |
| H3 | 30 / 24 / 22 | 22–24 |
| H4 | 20 px | ESTIMATED |
| Body | 16 / 18 / 15 | 16 |
| Small | 14 px | 14 |
| Caption | 13 / 12 px | 13 |

**Font:** Inter dominant — **CONFIRMED** in FIG.

---

# PHASE A8 — DESIGN SYSTEM SNAPSHOT v1

See [FP-0002-v2-DESIGN-SYSTEM-SNAPSHOT-v1.md](FP-0002-v2-DESIGN-SYSTEM-SNAPSHOT-v1.md).

Snapshot captured **without code**. Key conflicts documented: **radius**, **text color**, **page padding**, **mobile H2**.

---

# PHASE A9 — PILOT PAGE RECOMMENDATION REVIEW

See [FP-0002-v2-PILOT-PAGE-RECOMMENDATION-v1.md](FP-0002-v2-PILOT-PAGE-RECOMMENDATION-v1.md).

**RECOMMENDED: FP-0002-PG-005 «О центре»** — prior conclusion **holds** after v2 FIG verification.

---

# PHASE A10 — P1 READINESS

| Gate | Status |
|------|--------|
| Sources readable | **PASS** |
| Page inventory | **PASS** |
| Block inventory | **PASS** |
| Asset strategy | **PASS WITH DEVIATION** — extract from FIG; no standalone pack |
| Typography hierarchy | **PASS WITH DEVIATION** — Production vs FIG conflicts logged |
| Design system snapshot | **PASS** |
| Pilot page selected | **PASS** — PG-005 |
| v2 skeleton untouched | **PASS** |
| Legacy workspace untouched | **PASS** |

### Recorded deviations (non-blocking)

| ID | Deviation |
|----|-----------|
| DEV-01 | PG-008 PDF mobile filename gap — use FIG `Блог хаб - моб` until PDF renamed |
| DEV-02 | PG-005 FIG D/M section label mismatch |
| DEV-03 | Home v1 PDFs still on disk — exclude from Discovery |
| DEV-04 | Production Standards vs FIG/PDF numeric conflicts (radius, colors, padding) |
| DEV-05 | No standalone favicon/font files |
| DEV-06 | Legacy asset collision — mandatory new manifest |
| DEV-07 | PG-001 SECTION-10 y-order — not in pilot scope |

### Verdict

**P1 READY — PASS WITH RECORDED DEVIATIONS**

Discovery authorized for **PG-005** pilot slice in `workspaces/fp-0002-shpigovsky-v2/`.

---

## Changed files (this task)

**Created:**

- `reports/FP-0002-v2-PAGE-INVENTORY-v1.md`
- `reports/FP-0002-v2-BLOCK-INVENTORY-v1.md`
- `reports/FP-0002-v2-ASSET-INVENTORY-v1.md`
- `reports/FP-0002-v2-TYPOGRAPHY-AUDIT-v1.md`
- `reports/FP-0002-v2-DESIGN-SYSTEM-SNAPSHOT-v1.md`
- `reports/FP-0002-v2-PILOT-PAGE-RECOMMENDATION-v1.md`
- `reports/FP-0002-v2-DESIGN-AUDIT-REPORT-v1.md`

**Audit tooling (scratch, operations tree — not v2 deliverable):**

- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/audit_page_sections.mjs`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/audit_typography.mjs`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/audit_complexity.mjs`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_audit_page_sections_v2.json`

**Not modified:** v2 skeleton, legacy frontend, governance docs.

---

## Git status

Commit / push **not performed** (per task restriction).

---

## UNKNOWN / SECURITY

| Signal | Notes |
|--------|-------|
| **SAFE UNKNOWN** | Libertinus Serif production scope; video source URL; modal M-06 behavior |
| **SECURITY RISK** | None identified in audit pass |

---

## Final checklist

| Check | Result |
|-------|--------|
| AUTHORITY VALIDATED | **YES** |
| PAGE INVENTORY COMPLETE | **YES** |
| BLOCK INVENTORY COMPLETE | **YES** |
| ASSET INVENTORY COMPLETE | **YES** |
| TYPOGRAPHY AUDIT COMPLETE | **YES** |
| DESIGN SYSTEM SNAPSHOT COMPLETE | **YES** |
| PILOT PAGE RECOMMENDATION COMPLETE | **YES** |
| P1 READY | **YES** |
| NEXT TASK | **FP-0002 v2 DISCOVERY START** |

**STOP.**
