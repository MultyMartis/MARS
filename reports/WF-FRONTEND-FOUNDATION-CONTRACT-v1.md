# WF-FRONTEND-FOUNDATION-CONTRACT-v1

**Document type:** Foundation prerequisites — Phase F7  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22

**Authorities:** [frontend-visual-foundation-contract-v1.md](../projects/mars-website-factory/frontend-visual-foundation-contract-v1.md) · [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) · [frontend-shell-first-start-protocol-v1.md](../projects/mars-website-factory/frontend-shell-first-start-protocol-v1.md)

---

## 1. Purpose

Define what **must exist** in the v2 workspace before **any pilot page section** (PG-005) implementation begins.

Foundation complete = Implementation Sequence steps **1–11** + operator visual accept on foundation.

---

## 2. Foundation element matrix

| Element | Status | Evidence | Notes |
|---------|--------|----------|-------|
| **Production Standards v3** | **MANDATORY** | Approved doc + v2 re-ack | Rank-1 SSOT |
| **SCSS abstracts / tokens** | **MANDATORY** | `_tokens.scss` or equivalent wired | Re-validate vs FIG — do not copy legacy file |
| **Base reset + typography defaults** | **MANDATORY** | `base/` layer | Inter, colors, LH law |
| **Container tokens** | **MANDATORY** | `--container-max: 1170px`, pad 40/20 | v3 §C-01 |
| **Spacing scale** | **MANDATORY** | OL-01 mapped tokens | 4px base from normalization |
| **Radius tokens** | **MANDATORY** | 30 / 10 / 999 tiers | v3 lead correction |
| **Section spacing tokens** | **MANDATORY** | same-bg / band gaps | frontend-section-spacing-rule |
| **Header desktop** | **MANDATORY** | Partial + SCSS + brand gate PASS | Layout Spec APPROVED |
| **Footer desktop** | **MANDATORY** | Partial + SCSS | Layout Spec APPROVED |
| **Shell page entry** | **MANDATORY** | Foundation slug — not Home | Clean shell → built shell |
| **Logo wired** | **MANDATORY** | Brand Asset Gate PASS | C-09 row complete |
| **Favicon** | **OPTIONAL** at foundation | **SAFE UNKNOWN** until drop/extract | Does not block foundation if documented |
| **Typography demo (H1–H6, body)** | **MANDATORY** | On foundation page in `main` | Visual Foundation Contract §3.1 |
| **Buttons (primary/secondary/outline/disabled)** | **MANDATORY** | Visible samples | §3.3 |
| **Inputs + textarea** | **MANDATORY** | Labeled fields | §3.2 |
| **Checkbox + radio** | **MANDATORY** | Form samples | §3.2 |
| **Select** | **OPTIONAL** | Required if project uses selects | Else N/A + Lead ack |
| **Validation state sample** | **MANDATORY** | Error state on one field | §3.2 |
| **Cards** | **MANDATORY** | At least one surface | §3.4 |
| **Lists + blockquote** | **MANDATORY** | ul/ol/quote | §3.1 |
| **Tables** | **OPTIONAL** | N/A if project unused | FP-0002 uses tables sparingly |
| **FAQ accordion demo** | **MANDATORY** | One-open behavior | production-invariants |
| **Alerts** | **MANDATORY** | Info + error samples | §3.4 |
| **Spacing labeled samples** | **MANDATORY** | same-bg + band labels | §3.4 |
| **Image sample** | **MANDATORY** | Real asset with alt | §3.5 |
| **Video wrapper** | **NOT REQUIRED** at foundation | Defer to page charter | Home has video block |
| **Design Calibration PASS** | **MANDATORY** | Recorded verdict | Before Foundation QA |
| **Foundation QA REPORT** | **MANDATORY** | Per reporting standard | Desktop + mobile |
| **Operator Visual Accept** | **MANDATORY** | Both foundation viewports | operator-visual-approval-law |
| **Mobile header/footer/base** | **MANDATORY** | ≤1023px pass | After desktop foundation accept |
| **Sticky bar BLK-004** | **OPTIONAL** | Implement if in scope charter | 56px bar per v3 |
| **Home hero** | **NOT REQUIRED** | Forbidden at foundation | HEADER ≠ HERO |
| **Page sections (PG-005)** | **NOT REQUIRED** | Blocked until foundation close | — |

---

## 3. Gates before page work

| Gate ID | Requirement |
|---------|-------------|
| G-FC-01 | Production Standards approved + v2 re-ack |
| G-FC-02 | Layout Spec Header + Footer **OPERATOR APPROVED** |
| G-FC-03 | Brand Asset Gate **PASS** |
| G-FC-04 | Text locks — header + footer |
| G-FC-05 | Visual Foundation Contract §3 — all **MANDATORY** rows rendered |
| G-FC-06 | Design Calibration **PASS** |
| G-FC-07 | Foundation QA technical **PASS** |
| G-FC-08 | **OPERATOR VISUAL ACCEPT** — foundation desktop + mobile |
| G-FC-09 | No PG-005 section partials in codebase |
| G-FC-10 | Enforcement gates — Operator Law, Compiled CSS, ROOT COMPLIANCE |

---

## 4. Optional vs not required — summary

| Category | Items |
|----------|-------|
| **MANDATORY** | Tokens, base, header, footer, shell page, UI demo composition, calibration, foundation QA, operator accept, mobile shell |
| **OPTIONAL** | Favicon (document UNKNOWN), select demo if unused, sticky bar, tables |
| **NOT REQUIRED** | Home hero, PG-005 sections, inner pages, video wrapper at foundation |

---

## 5. Contract status

**FOUNDATION CONTRACT LOCKED — YES**

---

*End of contract — v1.*
