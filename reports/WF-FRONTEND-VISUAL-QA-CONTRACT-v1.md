# WF-FRONTEND-VISUAL-QA-CONTRACT-v1

**Document type:** Visual QA law — Phase F9  
**Project:** FP-0002 v2 — Shpigovsky.ru  
**Date:** 2026-06-22

**Authorities:** [WF-PR01-PILOT-READINESS-CONTRACT-v1.md §19](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md) · [frontend-design-qa-matrix-v1.md](../projects/mars-website-factory/frontend-design-qa-matrix-v1.md) · [pixel-fidelity-audit-rules-v1.md](../projects/mars-website-factory/pixel-fidelity-audit-rules-v1.md) · [operator-visual-approval-law-v1.md](../projects/mars-website-factory/operator-visual-approval-law-v1.md) · [frontend-qa-reporting-standard-v1.md](../projects/mars-website-factory/frontend-qa-reporting-standard-v1.md)

---

## 1. Mandatory QA levels

| Level | Focus | Minimum evidence |
|-------|-------|------------------|
| **L1 — Structure** | Section order, major blocks, DOM hierarchy, shell zones | Source frame map vs built HTML outline; y-order decisions logged |
| **L2 — Typography** | Families, sizes, weights, heading hierarchy | DevTools vs SSOT table; RU typography gate |
| **L3 — Spacing** | Margins, padding, gaps, container | SSOT + OL-01 compliance; `dist/*.css` |
| **L4 — Responsive** | Desktop vs mobile vs approved intermediate | Viewport list; overflow check |
| **L5 — Deviation Register** | All deltas with evidence | Structured register — every non-PASS item |

**Factory matrix mapping:** L1 ≈ DQ structure/layout · L2 ≈ DQ-01 · L3 ≈ DQ-02a/b + DQ-03 · L4 ≈ DQ responsive domains · L5 ≈ C-12 + L5 register.

---

## 2. Comparison inputs (required)

```text
approved visual source (FIG frame / PDF / export)
built page at stated viewport
screenshot or operator observation
diff / deviation record
text lock hash match (PIXEL_PERFECT)
asset manifest hash match (PIXEL_PERFECT)
```

**Forbidden:** QA from build log alone; agent self-attestation without evidence.

---

## 3. Verdict vocabulary — exact meanings

| Verdict | Meaning | Next action |
|---------|---------|-------------|
| **PASS** | All mandatory levels L1–L4 PASS; L5 empty or notes only; text/asset VERIFIED | May proceed to **operator visual review** — not automatic progression |
| **PASS WITH RECORDED DEVIATIONS** | No critical blockers; all deviations in L5 with evidence + operator ack on debt | May proceed with documented debt; P5 review |
| **REWORK REQUIRED** | Critical fail — generative fill, wrong brand asset, missing mandatory sections, false structure | Fix scope only; re-run QA |
| **BLOCKED BY SOURCE** | SAFE UNKNOWN or source conflict prevents honest verification | **STOP** implementation — operator resolves source |

**Additional gate vocabulary (Factory):**

| Term | Meaning |
|------|---------|
| **BUILT** | Gulp exit 0 — **not** QA PASS |
| **VERIFIED** | FIG/text/asset diff gates PASS |
| **TECHNICAL PASS** | Matrix/enforcement PASS — **≠ operator visual accept** |
| **OPERATOR VISUAL ACCEPT** | Required after technical QA per operator-visual-approval-law |

---

## 4. Severity and blocking

| Severity | Examples | Blocks PASS? |
|----------|----------|--------------|
| **Critical** | Generative text; wrong logo; invented sections; collision hash in slot | **YES** → REWORK |
| **Major** | SSOT spacing/type off without exception; container drift | **YES** unless WAIVED |
| **Minor** | Documented micro-delta within PF band | PASS WITH DEVIATIONS |
| **Source** | Missing mobile authority; unreadable copy | **BLOCKED BY SOURCE** |

---

## 5. False-green prevention (mandatory)

From stress-test FAIL-001/018 — **ADOPTED**:

| Check | When |
|-------|------|
| Text lock diff per section | Before section VERIFIED |
| Image hash checklist per section | Before section VERIFIED |
| INSTANCE component walk audit | Before INSTANCE-heavy sections |
| Build log says **BUILT** not **PASS** | Every build REPORT |
| Post-build forensic on pilot slice | Before P5 |
| Operator visual review block | Every visual stage close |

---

## 6. REPORT mandatory lines

```text
VISUAL QA L1 — PASS | FAIL | SAFE UNKNOWN
VISUAL QA L2 — PASS | FAIL | SAFE UNKNOWN
VISUAL QA L3 — PASS | FAIL | WAIVED | SAFE UNKNOWN
VISUAL QA L4 — PASS | FAIL | BLOCKED BY SOURCE | SAFE UNKNOWN
VISUAL QA L5 — DEVIATIONS: <n> | NONE
TEXT FIDELITY — PASS | FAIL | SAFE UNKNOWN
ASSET MANIFEST — VERIFIED | FAIL | PENDING
BUILD STATUS — BUILT | FAIL
QA VERDICT — PASS | PASS WITH RECORDED DEVIATIONS | REWORK REQUIRED | BLOCKED BY SOURCE
OPERATOR VISUAL ACCEPT — ACCEPT | REVISE | PENDING
OPERATOR ACTION REQUIRED — YES | NO
```

**Rule:** `QA VERDICT — PASS` with `OPERATOR VISUAL ACCEPT — PENDING` is allowed for **technical** closeout only — **forbidden** as stage authorization.

---

## 7. Foundation vs page QA

| Stage | Levels required | Operator gate |
|-------|-----------------|---------------|
| Foundation close | L1–L4 on foundation URL + enforcement rollup | **OPERATOR VISUAL ACCEPT** |
| Per block (max 2–3 sections) | L1–L3 minimum + text/asset VERIFIED | **OPERATOR VISUAL ACCEPT** per delivery |
| Pilot page desktop close | L1–L5 full | P3 + operator |
| Pilot page mobile close | L1–L5 full | P4 + operator |
| Pilot final | L5 consolidated | P5 + P6 |

---

## 8. Contract status

**VISUAL QA CONTRACT LOCKED — YES**

---

*End of contract — v1.*
