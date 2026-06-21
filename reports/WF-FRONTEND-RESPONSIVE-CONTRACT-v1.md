# WF-FRONTEND-RESPONSIVE-CONTRACT-v1

**Document type:** Responsive implementation law — Phase F8  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22

**Authorities:** [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) · [frontend-production-invariants-v1.md](../projects/mars-website-factory/frontend-production-invariants-v1.md) · [WF-PR01-PILOT-READINESS-CONTRACT-v1.md §17](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md) · [FP-0002-v2-DESIGN-AUDIT-REPORT-v1.md](FP-0002-v2-DESIGN-AUDIT-REPORT-v1.md)

---

## 1. Desktop-first or mobile-first

**Decision: DESKTOP-FIRST**

| Field | Value |
|-------|-------|
| **Primary CSS strategy** | Base styles for desktop; mobile overrides via `max-width` |
| **Activation breakpoint** | **`min-width: 1024px`** for desktop grid activation |
| **Mobile band** | **`max-width: 1023px`** |
| **Authority** | Production Standards v3 · FP-0002 Start Sequence step 5 |
| **Rejected** | Generic mobile-first industry default without SSOT |
| **Rejected** | Ad-hoc `980px` / `981px` breakpoints |

**Factory note:** [frontend-production-authority-order-v1.md](../projects/mars-website-factory/frontend-production-authority-order-v1.md) — when agent preference conflicts with project SSOT, **desktop-first wins**.

---

## 2. Artboard references (non-CSS evidence)

| Viewport | Design artboard | Source |
|----------|-----------------|--------|
| Desktop | ~1437px width | PDF / FIG frames |
| Mobile | ~380px width | PDF mobile pairs / FIG mobile frames |
| Tablet | **SAFE UNKNOWN** | No dedicated tablet PDFs — conservative inference only with operator sheet |

---

## 3. Desktop build rules

| Rule | Requirement |
|------|-------------|
| Build order | Foundation desktop complete before mobile shell |
| Container | 1170px max; 40px page padding |
| Verification viewport | **≥1024px** minimum; spot-check **1440px** |
| Layout patterns | LP-* / WF-LAYOUT — no ad-hoc `%` splits (OL-04) |
| Section work | Pilot page desktop sections before mobile adaptation |
| QA | L1–L3 minimum before L4 mobile work |

---

## 4. Mobile adaptation rules

| Rule | Requirement |
|------|-------------|
| Start condition | Desktop **OPERATOR VISUAL ACCEPT** for same scope |
| Authority | FIG mobile frame → PDF mobile pair → **SAFE UNKNOWN** |
| Container padding | 20px mobile per v3 |
| Section gap mobile | 64px default where applied (v3) |
| Header | Condensed nav / menu pattern |
| Footer | Stack layout |
| Sticky BLK-004 | 56px bar; 48px touch targets if active |
| Forbidden | Invented mobile layout when source absent |
| Required sheet | Operator-approved responsive decision when mobile source missing |

---

## 5. Responsive QA

### 5.1 Mandatory viewports (minimum)

```text
1440 — desktop target
1024 — transition / desktop floor
768  — tablet check (conservative)
375–390 — mobile primary
320 — minimum supported width
```

Use project breakpoints from SSOT when they refine the list: 1440 · 1310 · 1199 · 1024 · 767 · 660 · 580 · 490 · 390 · 370 — **only where relevant to scoped block**.

### 5.2 Mandatory checks

```text
long text wrapping (RU — no word-break CSS)
button wrapping
form field overflow
menu / header collapse
horizontal overflow (scroll-x forbidden)
modal (if in scope)
neighbor stretch (FAQ)
```

### 5.3 QA sequence

```text
Foundation desktop QA → Operator accept
    ↓
Foundation mobile QA → Operator accept
    ↓
Page desktop QA (L4 includes desktop viewports)
    ↓
Operator accept
    ↓
Page mobile QA (L4 mobile viewports)
    ↓
Operator accept
```

**Forbidden:** Mobile QA before desktop operator accept for same scope.

---

## 6. Pilot slice PG-005 notes

| Field | Value |
|-------|-------|
| Desktop + mobile PDF | **FOUND** |
| FIG desktop/mobile frames | **FOUND** — 13 / 11 sections (composition PARTIAL — audit register) |
| Mobile naming | Resolve at page charter — not responsive invention |

---

## 7. Contract status

**RESPONSIVE CONTRACT LOCKED — YES**

---

*End of contract — v1.*
