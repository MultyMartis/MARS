# FP-0002 v2 — Typography Audit v1

**Document type:** Typography Audit (FIG-primary)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Primary source:** `Шпиговский.fig` — TEXT nodes decoded 2026-06-22  
**Secondary cross-check:** `FP-0002-NUMERIC-DESIGN-RULES-v2.md` (PDF extraction)  
**Production overlay (reference):** `FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md` — **not** auto-applied in audit

**Rule:** Values tagged **CONFIRMED** only when FIG node counts support; else **ESTIMATED** or **SAFE UNKNOWN**. No guessing.

---

## 1. Font families (FIG)

| Family | Styles seen | Node count | Role | Status |
|--------|-------------|------------|------|--------|
| **Inter** | Light, Medium, Regular, Thin, Bold | **1870** | Primary UI + body | **CONFIRMED** |
| Libertinus Serif | SemiBold, Bold | **52** | Accent / display snippets | **CONFIRMED** (presence) · **SAFE UNKNOWN** (production scope) |
| Roboto | Regular | 33 | Sparse | **SAFE UNKNOWN** — residue |
| Rubik, Manrope, Prata, Raleway | Various | ≤10 each | Sparse | **SAFE UNKNOWN** |

**Production decision (documented elsewhere):** Inter as `font-family-primary` — **aligns with FIG dominant family**.

---

## 2. Font weights (FIG → role mapping)

| Weight (FIG style) | Approx. CSS | Usage | Status |
|--------------------|-------------|-------|--------|
| Inter Light | 300 | Body paragraphs (dominant) | **CONFIRMED** |
| Inter Regular | 400 | UI labels | **CONFIRMED** |
| Inter Medium | 500 | Headings, nav, buttons | **CONFIRMED** |
| Inter Thin | 100 | Rare | **ESTIMATED** |
| Inter Bold | 700 | Rare (2 nodes) | **ESTIMATED** |

---

## 3. Desktop typography hierarchy (FIG fontSize histogram + PDF cross-check)

| Role | FIG dominant size (px) | PDF v2 evidence | Weight | Status |
|------|------------------------|-----------------|--------|--------|
| **H1 / Display** | **70** (hero), **42** (inner heroes) | 70 Home hero CONFIRMED | Medium | **CONFIRMED** |
| **H2** | **36** (71 nodes), **42** (42 nodes) | 36 dominant H2 | 500 | **CONFIRMED** |
| **H3** | **30** (5), **24** (24), **22** (61) | 30 card titles | 500 | **CONFIRMED** / card context |
| **H4** | **20** (141 nodes) | 20 subheads | 500 | **CONFIRMED** |
| **Body** | **16** (574), **18** (325), **15** (284) | 16 highest count; 18 second | 300 Light | **CONFIRMED** — dual body scale |
| **Small** | **14** (265) | 14 UI | 400 | **CONFIRMED** |
| **Caption** | **13** (40), **12** (24) | 13 breadcrumbs | 400 | **CONFIRMED** |

---

## 4. Mobile typography hierarchy (FIG + PDF)

| Role | Size (px) | Status | Notes |
|------|-----------|--------|-------|
| **H1 / Display** | **42** | **CONFIRMED** | Home mobile PDF + FIG |
| **H2** | **32** (14 nodes), **22** (61 nodes) | **CONFIRMED** | **Conflict:** Production Standards v3 = **22px** mobile H2; PDF cluster includes **32px** |
| **H3 / Card title** | **22–24** | **CONFIRMED** | |
| **Body** | **16** dominant | **CONFIRMED** | |
| **Small** | **14** | **CONFIRMED** | |
| **Caption** | **13** | **CONFIRMED** | |
| **Micro / top bar** | **10** | **ESTIMATED** | Rare mobile spans |

---

## 5. Line heights

| Source | Finding | Status |
|--------|---------|--------|
| PDF derived ratio | ~**1.22** dominant | **CONFIRMED** (PDF) |
| FIG auto lineHeight | Per-node; not summarized in this pass | **SAFE UNKNOWN** global token |
| Production Standards v3 | Body LH 28/24 px for 18/16 | **REFERENCE** — coordinator tier |

---

## 6. Typography variables (FIG Internal Only Canvas)

| Variable set | Names sampled | Status |
|--------------|---------------|--------|
| Typography / Typography Primitives | `Body/Size Medium`, scale tokens `40/60/80/100` | **FOUND** (structure) |
| Resolved values in export | Partial — 16 VARIABLE nodes | **PARTIAL** — full token binding = Discovery task |

---

## 7. Conflicts & SAFE UNKNOWN

| ID | Topic | Status |
|----|-------|--------|
| T-01 | Mobile H2: FIG/PDF **32px** vs Production **22px** | **SAFE UNKNOWN** — operator pick at Discovery |
| T-02 | Default body: FIG **16** count vs Production **18** desktop default | **SAFE UNKNOWN** |
| T-03 | Libertinus Serif — required in CSS or FIG-only accent | **SAFE UNKNOWN** |
| T-04 | Letter-spacing / tracking | **SAFE UNKNOWN** — forbidden in v2 SCSS per charter unless FIG proves |
| T-05 | PDF Type3 — families not extractable from PDF alone | FIG closes gap for Inter |

---

## 8. Audit completeness

Typography audit **complete for P1** at hierarchy level. Pixel-level per-block type specs = **Discovery** phase output (text-lock files).

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 (v2 audit pass) |
| Method | `audit_typography.mjs` on FIG, 2026-06-22 |
