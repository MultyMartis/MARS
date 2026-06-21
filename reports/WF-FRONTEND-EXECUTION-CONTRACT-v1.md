# WF-FRONTEND-EXECUTION-CONTRACT-v1

**Document type:** Authoritative implementation law — FP-0002 v2  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Task:** WF-FRONTEND-EXECUTION-CONTRACT v1 · FP-0002 v2 PRE-IMPLEMENTATION FOUNDATION RECONCILIATION  
**Workspace:** `workspaces/fp-0002-shpigovsky-v2/` — **implementation-free** until foundation start authorized  
**Status:** **PUBLISHED** — documentation only; **no implementation authorized by this document alone**

---

## 1. Purpose

This document is the **single authoritative execution law** for all future frontend implementation in FP-0002 v2. It reconciles Website Factory governance, WF-PR01 pilot rules, Production Standards, legacy extraction, forensic findings, asset collision lessons, operator workflow patterns, and successful legacy process patterns — **without inventing new laws**.

**Classification used throughout:** ADOPT · ADOPT WITH MODIFICATION · REJECT · SUPERSEDED · REFERENCE ONLY

---

## 2. Child contracts (normative detail)

| Document | Phase | Role |
|----------|-------|------|
| [WF-FRONTEND-EXECUTION-SOURCE-REGISTER-v1.md](WF-FRONTEND-EXECUTION-SOURCE-REGISTER-v1.md) | F1 | All rule sources + status |
| [WF-FRONTEND-LEGACY-RULE-RECONCILIATION-v1.md](WF-FRONTEND-LEGACY-RULE-RECONCILIATION-v1.md) | F2 | Legacy rule disposition |
| [WF-FRONTEND-IMPLEMENTATION-SEQUENCE-v1.md](WF-FRONTEND-IMPLEMENTATION-SEQUENCE-v1.md) | F3 | Build order — locked |
| [WF-FRONTEND-VISUAL-AUTHORITY-CONTRACT-v1.md](WF-FRONTEND-VISUAL-AUTHORITY-CONTRACT-v1.md) | F4 | FIG → PDF → JPG → Operator |
| [WF-FRONTEND-TEXT-FIDELITY-CONTRACT-v1.md](WF-FRONTEND-TEXT-FIDELITY-CONTRACT-v1.md) | F5 | No rewrite / no invention |
| [WF-FRONTEND-ASSET-CONTRACT-v1.md](WF-FRONTEND-ASSET-CONTRACT-v1.md) | F6 | Brand Asset Law + manifest |
| [WF-FRONTEND-FOUNDATION-CONTRACT-v1.md](WF-FRONTEND-FOUNDATION-CONTRACT-v1.md) | F7 | Mandatory foundation elements |
| [WF-FRONTEND-RESPONSIVE-CONTRACT-v1.md](WF-FRONTEND-RESPONSIVE-CONTRACT-v1.md) | F8 | Desktop-first law |
| [WF-FRONTEND-VISUAL-QA-CONTRACT-v1.md](WF-FRONTEND-VISUAL-QA-CONTRACT-v1.md) | F9 | L1–L5 + verdicts |

---

## 3. Executive law summary

### 3.1 Decision hierarchy (production values)

```text
Project Production Standards (FP-0002 v3)
    ↓
Approved Operator Laws (OL-01–OL-07)
    ↓
Website Factory governance (shell-first, layout spec, mapping, QA)
    ↓
Layout Pattern Library
    ↓
Industry best practice (advisory)
    ↓
Agent preference (forbidden as override)
```

### 3.2 Visual evidence hierarchy (structure/content/assets)

```text
FIG (Шпиговский.fig)
    ↓
PDF pack (24 files)
    ↓
JPG mockup (Home desktop visual control only)
    ↓
Operator tie-breaker
```

### 3.3 Text law

**NO** rewrite · **NO** completion · **NO** guessing · **NO** marketing generation · **YES** text locks · **YES** SAFE UNKNOWN

### 3.4 Asset law

**NO** first-image=logo · **NO** frame-export hashes · **YES** Brand Asset Detection Chain · **YES** section manifest

### 3.5 Build law

**NO** legacy HTML/SCSS copy · **NO** full-page single-run builds · **NO** build PASS as fidelity PASS · **YES** block-by-block with operator gates · **YES** BUILT vs VERIFIED vocabulary

### 3.6 Responsive law

**Desktop-first** · breakpoint **1024/1023** · mobile after desktop operator accept

---

## 4. Implementation sequence (locked summary)

See full detail: [WF-FRONTEND-IMPLEMENTATION-SEQUENCE-v1.md](WF-FRONTEND-IMPLEMENTATION-SEQUENCE-v1.md)

```text
PREREQUISITES
  Execution contract · authority lock · standards re-ack · clean shell
  Group register · Layout Spec header/footer APPROVED
  Brand Asset Gate · text locks
    ↓
FOUNDATION
  Tokens/reset → Header desktop → Footer desktop
  Shell page + UI Foundation demo
  Design Calibration → Foundation QA desktop → Operator accept
  Mobile shell → Foundation QA mobile → Operator accept
    ↓
PILOT PAGE (PG-005)
  Discovery/locks/layout specs → Desktop block-by-block → Desktop QA → Operator accept
  Mobile adaptation → Mobile QA → Operator accept
    ↓
REMAINING PAGES (future charter — Home NOT first)
```

**Operator memory verified:** Header → Footer → UI Foundation → Desktop → Desktop QA → Mobile → Mobile QA → Remaining pages — **ADOPTED WITH MODIFICATION** (Factory prerequisite gates inserted).

---

## 5. WF-PR01 gate mapping

| Gate | FP-0002 v2 mapping | Status |
|------|-------------------|--------|
| **P0** Pilot input approved | WF-PR01-B intake; operator sign-off pending | **PARTIAL** |
| **P1** Inventory approved | P1 design audit complete | **PASS WITH DEVIATIONS** |
| **P2** Foundation approved | Not started | **NOT STARTED** |
| **P3** Desktop structure | Not started | **NOT STARTED** |
| **P4** Mobile structure | Not started | **NOT STARTED** |
| **P5** Visual QA reviewed | Not started | **NOT STARTED** |
| **P6** Pilot final | Not started | **NOT STARTED** |

---

## 6. Legacy disposition summary

| Category | ADOPT | ADOPT W/ MOD | REJECT | REF ONLY |
|----------|-------|--------------|--------|----------|
| Extraction totals | 22 | 24 | 18 | 14 |

**Hard REJECT classes for v2:** legacy HTML/SCSS/dist copy · generative text · frame-export images · first-image logo · false-green PASS · stress-test partials · Triumph demo · ui-demo M1/M2 residue

**Full table:** [WF-FRONTEND-LEGACY-RULE-RECONCILIATION-v1.md](WF-FRONTEND-LEGACY-RULE-RECONCILIATION-v1.md)

---

## 7. Phase F10 — Implementation readiness

### Can implementation begin immediately after this document?

**NO**

### What is still missing?

| # | Missing artefact | Blocks |
|---|------------------|--------|
| 1 | Operator sign-off: **Visual Authority APPROVED** | All implementation |
| 2 | Operator sign-off: **P0 Pilot Input Approved** (WF-PR01) | Foundation start |
| 3 | Production Standards v3 **v2 re-acknowledgment** against FIG audit | Token wiring |
| 4 | **Layout Spec — Header** + **OPERATOR APPROVED** | Header HTML |
| 5 | **Layout Spec — Footer** + **OPERATOR APPROVED** | Footer HTML |
| 6 | **Group Register** — header/footer scopes | Layout Spec |
| 7 | **Brand Asset Gate PASS** — logo node/hash | Header asset wire |
| 8 | **Text lock files** — header/footer | Shell copy |
| 9 | **Foundation implementation task** authorization | All SCSS/HTML |
| 10 | Page-scoped locks/manifests for PG-005 | Pilot page sections |

### What IS complete

| Item | Status |
|------|--------|
| P0 zero skeleton | **COMPLETE** |
| P1 design audit + inventories | **COMPLETE** |
| Execution contract package (this task) | **COMPLETE** |
| Source availability | **COMPLETE** |
| Legacy rule extraction | **COMPLETE** |

### Next authorized task

```text
FP-0002 v2 FOUNDATION START
```

**Scope of next task (expected):** Prerequisites rows 3–8 above + Implementation Sequence steps 1–11 only — **not** PG-005 page sections until P2 operator foundation accept.

---

## 8. Hard restrictions (reconfirmed)

This contract and all child documents **do not authorize:**

- HTML / SCSS / JS creation (except as explicitly opened by a future foundation-start task)
- Header / Footer / Hero build in this pass
- Layout Spec creation in this pass
- Discovery continuation beyond P1 inventories
- Workspace skeleton modification
- Build changes · commit · push

---

## 9. Contract checklist

| Item | Status |
|------|--------|
| RULE SOURCES RECONCILED | **YES** |
| LEGACY KNOWLEDGE RECONCILED | **YES** |
| IMPLEMENTATION ORDER LOCKED | **YES** |
| VISUAL AUTHORITY LOCKED | **YES** (operator sign-off pending) |
| TEXT FIDELITY LOCKED | **YES** |
| ASSET CONTRACT LOCKED | **YES** |
| FOUNDATION CONTRACT LOCKED | **YES** |
| RESPONSIVE CONTRACT LOCKED | **YES** |
| VISUAL QA CONTRACT LOCKED | **YES** |
| IMPLEMENTATION READY | **NO** |
| NEXT TASK | **FP-0002 v2 FOUNDATION START** |

---

## 10. UNKNOWN / honesty

| Topic | Status |
|-------|--------|
| Operator P0 final approval date | **SAFE UNKNOWN** |
| Favicon source file | **SAFE UNKNOWN** — FIG extract or client drop |
| PG-005 desktop/mobile section composition parity | **PARTIAL** — audit deviation register |
| Tablet responsive authority | **SAFE UNKNOWN** — no tablet PDFs |
| Blog hub PDF mobile naming (PG-008) | **PARTIAL** — reconcile at page charter |

---

*End of execution contract — v1.*
