# FP-0003 — Design-to-Frontend Contract v1

**Factory Project:** FP-0003 — OVERSEO  
**Domain:** overseo.ru  
**Date:** 2026-08-20  
**Wave:** DESIGN D1A — Hero master visual target  
**Status:** Project-specific contract for design → future Gulp implementation  

---

## Purpose

Ensure `overseo.ru` visual design targets can be implemented under **current** MARS Website Factory + Frontend Gulp Agent rules without structural rework.

This document is **concise and project-specific**. It does not reproduce the full Factory catalog.

Legend:

| Tag | Meaning |
|-----|---------|
| **CURRENT MARS STANDARD** | Verified from repository evidence |
| **FP-0003 OPERATOR OVERRIDE** | Explicit charter / operator decision |
| **RECOMMENDED PROJECT DECISION** | Project choice aligned with standards; not yet approved Production Standards SSOT |
| **SAFE UNKNOWN** | Not verified — must confirm before frontend |

---

## 1. Canvas & grid geometry

| Rule | Value | Class |
|------|-------|-------|
| Desktop design canvas width | **1920px** native | **FP-0003 OPERATOR OVERRIDE** |
| Primary content container max-width | **1300px** | **FP-0003 OPERATOR OVERRIDE** |
| Nominal outer free space at 1920 | **310px** left + **310px** right | **FP-0003 OPERATOR OVERRIDE** |
| Single primary container per page | **Yes** — no secondary page containers | **CURRENT MARS STANDARD** ([WF-GRID-DISCIPLINE-v1.md](../../../projects/mars-website-factory/../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md) WF-GRID-002, WF-GRID-006) |
| Full-bleed background ≠ full-bleed content | Backgrounds/decoration may span 1920; content aligns to container | **CURRENT MARS STANDARD** (WF-GRID-004) |
| Section owns vertical rhythm | Section padding, not child margin hacks | **CURRENT MARS STANDARD** ([frontend-section-spacing-rule-v1.md](../../../projects/mars-website-factory/frontend-section-spacing-rule-v1.md)) |

---

## 2. Container inner padding

| Rule | Value | Class |
|------|-------|-------|
| Container horizontal padding (desktop) | **50px** left + **50px** right | **RECOMMENDED PROJECT DECISION** — matches [gulp starter AGENTS.md](../../../workspaces/triumph-manipulator-landing-v2/AGENTS.md) container padding rule (desktop 50px) |
| Container horizontal padding (mobile/tablet ≤1024) | **10px** | **CURRENT MARS STANDARD** (gulp starter AGENTS.md) |
| Container horizontal padding (very small ≤370) | **5px** | **CURRENT MARS STANDARD** (gulp starter AGENTS.md) |
| Effective content column inside 1300 container | **1200px** max (1300 − 2×50) | **RECOMMENDED PROJECT DECISION** |

---

## 3. Spacing scale (production mapping)

**CURRENT MARS STANDARD:** [universal-style-scale-law-v1.md](../../../projects/mars-website-factory/universal-style-scale-law-v1.md) + [frontend-precision-governance-v1.md](../../../projects/mars-website-factory/frontend-precision-governance-v1.md)

### 3.1 Foundation tokens (FP-0003 v1 proposal)

| Token | Value | Class |
|-------|-------|-------|
| `--pad-x` | 50px | **RECOMMENDED PROJECT DECISION** |
| `--pad-y` | 50px | **RECOMMENDED PROJECT DECISION** |
| `--pad-gap` | 30px | **CURRENT MARS STANDARD** (example foundation) |
| `--pad-gap-line` | 15px | **CURRENT MARS STANDARD** |
| `--pad-gap-mini` | 5px | **CURRENT MARS STANDARD** |
| `--pad-box` | 20px | **CURRENT MARS STANDARD** |

### 3.2 Approved magnitude scale (normalization target)

Gap scale: **5 · 10 · 20 · 30 · 40 · 50 · 70**  
Padding/margin scale: **5 · 10 · 15 · 20 · 25 · 30 · 40 · 50 · 70 · 90**

Design values must map to this scale in future Production Standards — no random px (37, 53, 71, 94).

---

## 4. Radius system

| Token | Value | Class |
|-------|-------|-------|
| `--radius-main` | **24px** | **RECOMMENDED PROJECT DECISION** (calmer than 30px default example; single main radius) |
| `--radius-full` | **999px** | **CURRENT MARS STANDARD** |

**CURRENT MARS STANDARD:** Only `--radius-main` + `--radius-full` — no `--radius-small|medium|large` ([universal-style-scale-law-v1.md](../../../projects/mars-website-factory/universal-style-scale-law-v1.md)).

---

## 5. Typography system (roles)

| Role | Intended use | D1A render | Class |
|------|--------------|------------|-------|
| Display / hero | H1-level statement | Literata 400, 52px / 56px line | **RECOMMENDED PROJECT DECISION** |
| H2 | Section titles | Literata 400, 40px / 44px | **RECOMMENDED PROJECT DECISION** |
| H3 | Subsection | Literata 400, 28px / 32px | **RECOMMENDED PROJECT DECISION** |
| Body large | Lead / intro | Onest 400, 20px / 24px | **RECOMMENDED PROJECT DECISION** |
| Body | Default copy | Onest 400, 16px / 20px | **RECOMMENDED PROJECT DECISION** |
| Small / meta | Labels, nav | Onest 500, 13px / 17px | **RECOMMENDED PROJECT DECISION** |
| Navigation / action | Header CTAs | Onest 500, 12px / 16px, uppercase tracking 0.06em | **RECOMMENDED PROJECT DECISION** |

**CURRENT MARS STANDARD:** Line-height default **font-size + 4px** unless Production Standards document exception ([frontend-precision-governance-v1.md](../../../projects/mars-website-factory/frontend-precision-governance-v1.md)).

**SAFE UNKNOWN:** Final licensed webfont files for Literata / Onest WOFF2 bundle — render uses Google Fonts CDN for design prototype only.

---

## 6. Color system (FP-0003 v1)

Preserving Olga mint / violet / turquoise DNA with calmer execution.

| Role | Hex | Class |
|------|-----|-------|
| Surface hero wash | `#EEF6F2` | **RECOMMENDED PROJECT DECISION** |
| Surface white | `#FAFCFB` | **RECOMMENDED PROJECT DECISION** |
| Brand mint | `#A8D5C5` | **RECOMMENDED PROJECT DECISION** |
| Brand violet | `#8B7EC8` | **RECOMMENDED PROJECT DECISION** (calmer than candy purple) |
| Brand turquoise | `#5BAFA0` | **RECOMMENDED PROJECT DECISION** |
| Text primary | `#1E2A28` | **RECOMMENDED PROJECT DECISION** |
| Text muted | `#4A5C58` | **RECOMMENDED PROJECT DECISION** |
| Dark neutral (future dark sections) | `#1A2220` | **RECOMMENDED PROJECT DECISION** |

Operator note: speedometer candy colors from Olga JPG are **not** production targets — final stats block will use calmer gauge palette in later screens.

---

## 7. Layout model

| Rule | Detail | Class |
|------|--------|-------|
| Hero desktop layout | CSS Grid: header row + 2-column editorial body (7fr text / 5fr visual) inside container | **RECOMMENDED PROJECT DECISION** |
| Header layout | Flexbox: logo · nav · actions | **CURRENT MARS STANDARD** |
| Decorative layers | Absolute positioned within section root only | **CURRENT MARS STANDARD** |
| Absolute positioning | Decoration only — not primary text flow | **FP-0003 OPERATOR OVERRIDE** (charter implementability rule) |

Main responsive split for future implementation: **desktop ≥1025px** · **mobile/tablet ≤1024px** (gulp starter AGENTS.md).

---

## 8. SCSS & architecture (future frontend)

| Rule | Class |
|------|-------|
| One project SCSS entry (`src/scss/style.scss`) | **CURRENT MARS STANDARD** ([one-project-scss-file-law-v1.md](../../../projects/mars-website-factory/one-project-scss-file-law-v1.md)) |
| Physical padding/margin properties | **CURRENT MARS STANDARD** |
| No selector-named spacing tokens | **CURRENT MARS STANDARD** |
| No `--button-letter-spacing` | **CURRENT MARS STANDARD** |
| `data-*` hooks for JS behavior | **CURRENT MARS STANDARD** |
| Russian no mid-word splitting | **CURRENT MARS STANDARD** ([russian-no-word-splitting-typography-v1.md](../../../projects/mars-website-factory/russian-no-word-splitting-typography-v1.md)) |
| Local WOFF2 font delivery in production | **CURRENT MARS STANDARD** ([font-and-layout-stability-law-v1.md](../../../projects/mars-website-factory/font-and-layout-stability-law-v1.md)) |

---

## 9. Design render boundary

| Statement | Status |
|-----------|--------|
| `DESIGN/v1/render/` is design prototype only | **FP-0003 OPERATOR OVERRIDE** |
| Production Gulp workspace `fp-0003-overseo-v1` | **NOT CREATED** |
| Design PNG = approved visual target candidate | **Awaiting operator approval** |

---

## 10. Screen 01 — Hero (D1A)

| Field | Value |
|-------|-------|
| Export | `DESIGN/v1/exports/SCREEN-01-HERO-DESKTOP-v1.png` |
| Canvas | 1920 × **820px** (content-driven) |
| Hero section vertical padding | 50px top / 70px bottom (maps to `--pad-y` / scale 70) |
| Header height region | ~88px |
| Metadata | `DESIGN/v1/implementation-pack/SCREEN-01-HERO-METADATA-v1.md` |

---

## 11. SAFE UNKNOWN

| Item | Notes |
|------|-------|
| Original vector logo master | Recreated typographic mark in render — **VECTOR LOGO SOURCE — SAFE UNKNOWN** |
| Final photographic / macro asset | Hero visual labeled **PLACEHOLDER VISUAL — REQUIRES FINAL ASSET** |
| Literata / Onest licensing bundle for production WOFF2 | Candidate fonts only in D1A render |
| Approved Production Standards SSOT document | Not yet authored — this contract precedes formal PS approval |

---

*Contract v1 — documentation for design wave D1A. Not Production Standards SSOT until operator approves.*
