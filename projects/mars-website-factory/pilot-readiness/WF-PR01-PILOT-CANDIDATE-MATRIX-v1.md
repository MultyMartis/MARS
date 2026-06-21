# WF-PR01 Pilot Candidate Evaluation Matrix v1

**Status:** **PUBLISHED**  
**Date:** 2026-06-22  
**Contract:** [WF-PR01-PILOT-READINESS-CONTRACT-v1.md](WF-PR01-PILOT-READINESS-CONTRACT-v1.md)  
**Honesty boundary:** Evaluation framework only. **Not** a pre-selected pilot project. **Not** scored candidates without concrete inputs.

---

## 1. Purpose

Provide a consistent method to evaluate whether a **real** project with **concrete inputs** is suitable for the **first** bounded WF-PR01 frontend pilot.

**Do not use this matrix to:**

- auto-select FP-0002, BZPM, SITE-002, or other existing workspaces;
- score hypothetical projects;
- bypass operator P0 approval.

---

## 2. Evaluation Matrix

| Criterion | Weight | Candidate requirement | Score (0–2) | Evidence path | Notes |
|-----------|--------|----------------------|-------------|---------------|-------|
| **Final visual source** | **Critical** | Desktop **and** mobile preferred; operator-approved final | | | 0=missing · 1=partial · 2=complete |
| **Exact text available** | **Critical** | Yes — approved copy, not draft lorem | | | |
| **Assets available** | **Critical** | Mostly complete — logos, photos, icons | | | |
| **Page scope** | High | 1–3 pages | | | |
| **Section count** | High | 5–12 main-page sections | | | |
| **Runtime complexity** | **Critical** | Low — static HTML/SCSS/JS | | | |
| **CMS dependency** | Medium | None or explicitly deferred | | | |
| **Deadline** | High | Compatible with operator capacity | | | |
| **Business value** | High | Real project value to operator/client | | | |
| **Visual challenge** | Medium | Enough to test system; not unbounded | | | |
| **Existing manual progress** | Medium | Must not be endangered by pilot reset | | | |
| **Rollback safety** | **Critical** | Separate workspace/branch; no foreign WIP | | | |

**Scoring guide:**

| Score | Meaning |
|-------|---------|
| **0** | Does not meet requirement |
| **1** | Partially meets — debt or operator waiver required |
| **2** | Fully meets |

**Critical criteria:** any **0** on a Critical row → candidate cannot be **RECOMMENDED** without explicit operator waiver documented in intake.

---

## 3. Verdict Rules

| Verdict | Conditions |
|---------|------------|
| **RECOMMENDED** | All Critical ≥ 1; majority Critical = 2; High criteria mostly ≥ 1; scope within first pilot class |
| **ACCEPTABLE** | All Critical ≥ 1; one or more High = 0 with documented mitigation |
| **RISKY** | Any Critical = 1 with major debt; or multiple High = 0; operator waiver required before P0 |
| **NOT SUITABLE FOR FIRST PILOT** | Any Critical = 0; or scope forbidden (ecommerce runtime, 20+ pages, missing visual authority with invention allowed, etc.) |

---

## 4. Disqualifiers (automatic NOT SUITABLE)

```text
no final visual source and operator allows invention
full ecommerce / checkout / account scope
20+ unique pages
large CMS integration required in pilot
complex SPA framework required
existing workspace would be destroyed without backup
foreign WIP cannot be isolated
operator declines rollback safety
```

---

## 5. Lesson-Informed Risk Flags

Use when scoring — sourced from real work, **not** auto-disqualifiers:

| Source | Risk flag |
|--------|-----------|
| FP-0002 | Large section count with weak text extract; false-green risk |
| FP-0002 | Figma component text not walked — hallucination risk |
| BZPM / catalog work | High block complexity — prefer simpler landing for **first** pilot |
| G3 corporate reference | Substitution-backed blocks — do not confuse with client pixel source |
| Deferred browser QA (G3) | Pilot must budget visual QA time |

---

## 6. Evaluation Record Template

```text
Candidate name:
Evaluation date:
Evaluator:
Inputs reviewed (paths):

Criterion scores: (attach table)

Critical failures:
High gaps:
Risk flags:

Verdict: RECOMMENDED | ACCEPTABLE | RISKY | NOT SUITABLE FOR FIRST PILOT

Operator decision:
Proceed to intake? Yes | No
Notes:
```

---

## 7. Relationship to Intake

1. Score candidate when operator proposes a **real** project with **concrete** materials.
2. If verdict is **RECOMMENDED** or **ACCEPTABLE**, proceed to [WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md](WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md).
3. If **RISKY**, document waivers in intake §9 and §10 before P0.
4. If **NOT SUITABLE**, stop — do not create workspace.

---

## 8. Evidence Paths

```text
projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md
projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md
projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md
reports/FP-0002-STRESS-TEST-FORENSIC-v1.md
```

---

*Matrix: `projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md` · v1 · 2026-06-22*
