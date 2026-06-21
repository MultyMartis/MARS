# FP-0002 v3 — EXECUTION CHARTER v1

**Document type:** Execution charter (PDF-first hard reset)  
**Date:** 2026-06-22  
**Workspace:** `workspaces/fp-0002-shpigovsky-v3/`  
**Status:** **ACTIVE** — foundation phase complete · header implementation **FORBIDDEN** until operator gate

---

## Mission

Полный перезапуск frontend FP-0002 без переноса HTML/SCSS/JS/partials/assets/reports из v1/v2. Forensic workspaces остаются reference-only.

---

## Source authority stack

| Priority | Layer | Role |
|----------|-------|------|
| **1 — PRIMARY** | PDF (`INCOMING/01_DESIGN/`) | Тексты, телефоны, email, CTA, адреса, юридическая информация, названия разделов, визуальная композиция |
| **2 — SECONDARY** | FIG (`INCOMING/01_DESIGN/Шпиговский.fig`) | Размеры, сетки, координаты, spacing, группы, структура, экспорт изображений |
| **3 — REFERENCE** | JPG (`INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`) | Визуальная сверка — **не** text authority |
| **FINAL** | Operator | Разрешение конфликтов PDF ↔ FIG ↔ engineering |

### Conflict rule

**Если PDF и FIG конфликтуют — ВСЕГДА ПОБЕЖДАЕТ PDF.**

FIG **не является** authority для:

- текстов
- телефонов
- email
- CTA
- адресов
- логотипов
- названий разделов
- юридической информации

---

## Brand SSOT

| Asset | Path | Status |
|-------|------|--------|
| **Logo (ONLY)** | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/03_BRANDING/logo.svg` | **SSOT — APPROVED for wire** |

**REJECT:**

- Skinerica raster from FIG slot `1:880`
- PNG exports from FIG
- Legacy raster logo exports from v1/v2 workspaces
- Any logo not matching `logo.svg` path above

---

## Forensic reference (read-only)

| Workspace | Role |
|-----------|------|
| `workspaces/fp-0002-shpigovsky-frontend/` | Forensic evidence — **do not copy code** |
| `workspaces/fp-0002-shpigovsky-v2/` | Forensic evidence — **do not copy code** |

---

## Engineering law (foundation)

| Rule | Value |
|------|-------|
| Stack | HTML · SCSS · JS · gulp-file-include |
| Methodology | **Desktop-first** |
| Breakpoint | **1024px** (`min-width: 1024px`) |
| Container | **1170px** max · **40px / 20px** horizontal padding |
| Typography law | **Forbidden** without Lead approval: `letter-spacing`, `word-break`, `overflow-wrap`, `hyphens` |
| Token SSOT | `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` |

---

## Phase gates

| Phase | Deliverable | Status (2026-06-22) |
|-------|-------------|---------------------|
| P1 | New workspace v3 | **DONE** |
| P2 | Source audit + brand SSOT | **DONE** |
| P3 | This charter | **DONE** |
| P4 | Foundation SCSS (tokens, container, type, buttons, forms, cards, utilities) | **DONE** |
| P5 | `desktop-foundation.html` | **DONE** |
| P6 | Header source registry (no markup) | **DONE** |
| P7 | Header desktop build | **BLOCKED** — await operator **READY FOR HEADER DISCOVERY** → Layout/Assembly approval |
| P8 | Footer / Hero / pages | **BLOCKED** |

---

## Forbidden until explicit charter

- Header HTML/SCSS
- Footer HTML/SCSS
- Hero HTML/SCSS
- Home / About / Genotyping page builds
- Copying v1/v2 implementation files

---

## Downstream documents

| Document | Path |
|----------|------|
| Header source registry | `workspaces/fp-0002-shpigovsky-v3/reports/FP-0002-v3-HEADER-SOURCE-REGISTRY-v1.md` |
| Production Standards | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` |
| Design Audit (PDF) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-DESIGN-AUDIT-v1.md` |
| Header Layout Spec v2 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HEADER-LAYOUT-SPEC-v2.md` |

---

## Verdict (this charter)

**READY FOR HEADER DISCOVERY** — foundation prepared; header markup forbidden; operator must confirm PDF-first conflict resolutions before build.

**STOP.**
