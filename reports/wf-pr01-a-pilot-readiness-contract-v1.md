# REPORT — WF-PR01-A Pilot Readiness Contract and First Pilot Launch Boundary v1

**Status:** **PUBLISHED** · **WF-PR01-A COMPLETE** · **AWAITING PILOT INPUT**  
**Date:** 2026-06-22  
**Mode:** pilot-readiness-contract · documentation-only  
**Honesty boundary:** Records WF-PR01-A completion and pilot readiness contract publication. **Not** pilot workspace. **Not** pilot implementation. **Not** G4. **Not** production readiness.

**Canonical artefacts:**

- [WF-PR01-PILOT-READINESS-CONTRACT-v1.md](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md)
- [WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md)
- [WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md)

---

## 1. Result

| Field | Value |
|-------|-------|
| **Task** | **WF-PR01-A — Pilot Readiness Contract and First Pilot Launch Boundary** |
| **Status** | **COMPLETE** |
| **Readiness decision** | **WF-PR01-A COMPLETE — READY TO SELECT FIRST PILOT INPUT** |
| **WF-PR01 identity** | **Website Factory Pilot Readiness** · **AUTHORIZED** · **WF-PR01-A COMPLETE** |
| **First pilot class** | Bounded corporate/landing · 1–3 pages · 5–12 sections · desktop+mobile preferred |
| **Input authority** | Operator-approved layout → assets → exact text → Factory rules → SAFE UNKNOWN |
| **Intake template** | **PUBLISHED** — empty template, no fictitious project |
| **Fidelity contract** | Visual + text + Russian typography rules **PUBLISHED** |
| **Asset policy** | Supplied assets first; FA Pro controlled use; no stock/fake logos |
| **Frontend stack** | HTML · SCSS · JS · jQuery · Gulp · gulp-file-include |
| **Workspace contract** | `workspaces/wf-pilot-<NNNN>-<slug>-frontend/` after P0 only |
| **Extraction contract** | Minimal inventory required before full implementation |
| **Responsive contract** | Desktop+mobile authority; missing mobile needs decision sheet |
| **Visual QA** | L1–L5 levels; PASS / PASS WITH DEVIATIONS / REWORK / BLOCKED BY SOURCE |
| **Operator gates** | P0–P6; P1+P2 and P3+P4 merge allowed with evidence |
| **Git policy** | Selective commits; checkpoint phases; no `git add .` / force push |
| **Rollback policy** | Stop conditions + return to last approved checkpoint |
| **Success criteria** | Operator-acceptable desktop/mobile; honest deviations; editable result |
| **Failure criteria** | Hallucination, scope explosion, false-green, input violation |
| **Candidate matrix** | **PUBLISHED** — score only with concrete inputs |
| **Launch sequence** | 10-step minimal sequence **PUBLISHED** |
| **Pilot state** | **AWAITING PILOT INPUT** |
| **G4 state** | **DEFERRED · NOT STARTED** |
| **Coverage** | **UNCHANGED** — RC **32/32** · RPC **29/32** · RSC **7/11** |
| **Next task** | **WF-PR01-B — First Pilot Intake and Candidate Approval** |

---

## 2. Git Safety

| Check | Result |
|-------|--------|
| **Branch** | `mars/post-cycle8-live-tests` — **confirmed** |
| **HEAD contains** | `03941f7` · `1f20237` — **confirmed** |
| **G3 closure on remote** | **present** (prior push baseline) |
| **Staged files before commit** | **none** |
| **Foreign WIP** | **present · excluded from selective commit** |

---

## 3. Authority Reviewed

| Document | Role |
|----------|------|
| [wf-r01-3-g3-gate-closure-decision-v1.md](../projects/mars-website-factory/wf-r01-3-g3-gate-closure-decision-v1.md) | G3 CLOSED · WF-R01.3.5 COMPLETE |
| [wf-r01-3-post-g3-lifecycle-decision-v1.md](../projects/mars-website-factory/wf-r01-3-post-g3-lifecycle-decision-v1.md) | PROCEED TO PILOT READINESS |
| [wf-r01-3-g3-formal-evaluation-decision-v1.md](../projects/mars-website-factory/wf-r01-3-g3-formal-evaluation-decision-v1.md) | G3-F technical baseline |
| [wf-r01-3-g3-operator-signoff-gate-closure-v1.md](wf-r01-3-g3-operator-signoff-gate-closure-v1.md) | Operator sign-off sync |
| [roadmap.md](../projects/mars-website-factory/roadmap.md) | Programme sync target |
| [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Operator entry sync target |
| [pilot-adoption-flow-v1.md](../projects/mars-website-factory/pilot-adoption-flow-v1.md) | **COMPLEMENTARY** legacy adoption pattern |
| [frontend-production-authority-order-v1.md](../projects/mars-website-factory/frontend-production-authority-order-v1.md) | Authority hierarchy |
| [FP-0002-STRESS-TEST-FORENSIC-v1.md](FP-0002-STRESS-TEST-FORENSIC-v1.md) | **LEGACY** lesson source |

---

## 4. Duplicate Contract Check

| Search term | Finding | Classification |
|-------------|---------|----------------|
| `WF-PR01-PILOT-READINESS-CONTRACT` | None prior | **NEW** |
| `pilot readiness contract` | Post-G3 pointers only | **POST-G3 POINTER** |
| `first pilot launch boundary` | Lifecycle §8 recommendation only | **POST-G3 POINTER** |
| `pilot intake contract` | pilot-adoption-flow (Wave 6) | **COMPLEMENTARY** — pre-WF-PR01 |
| `pilot success criteria` | MIG / legal / EAR pilots | **LEGACY / PROJECT-SPECIFIC** |
| `WF-PR01-A` | Forward pointers in G3 closure | **ROADMAP POINTER** |

**Result:** No **ACCEPTED PILOT READINESS CONTRACT** existed. Proceed.

---

## 5. WF-PR01 Identity

| Field | Value |
|-------|-------|
| **Programme** | **WF-PR01** |
| **Name** | **Website Factory Pilot Readiness** |
| **Parent** | **MARS Website Factory** |
| **Authority** | WF-R01.3 Post-G3 Lifecycle Decision |
| **Status** | **AUTHORIZED** · **WF-PR01-A COMPLETE** · **AWAITING PILOT INPUT** |

---

## 6. First Pilot Boundary

Bounded corporate or landing frontend · 1 primary page (+ ≤2 secondary) · 5–12 sections · desktop + mobile visual sources · HTML/SCSS/JS/Gulp · no CMS · no ecommerce runtime · no payment · no complex application logic in first pass.

---

## 7. Pilot Input Authority

Hierarchy: operator-approved layout → approved assets → exact text → Factory rules → SAFE UNKNOWN. No invention for missing inputs.

---

## 8. Intake Contract

[WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md) published with mandatory fields. **Not** filled with fictitious project.

---

## 9. Visual Fidelity Contract

Visual source controls section order, hierarchy, typography, spacing, assets, and shown responsive behaviour. No section invention, reorder, or simplification without debt record.

---

## 10. Text Fidelity Contract

Exact text reproduction; Russian `&nbsp;` typography rules; UNKNOWN for missing copy; FP-0002 hallucination class forbidden.

---

## 11. Asset Policy

Supplied assets first; controlled FA Pro; no stock/fake logos/watermarks; asset inventory required.

---

## 12. Frontend Stack

HTML · SCSS · JS · jQuery · Gulp · gulp-file-include · `src/` structure · `dist` build-only.

---

## 13. Workspace Contract

Created only after P0; naming `workspaces/wf-pilot-<NNNN>-<slug>-frontend/`; required README, intake, inventories, QA, logs.

---

## 14. Extraction Contract

Page/section/component/block/asset/text inventories + numeric rules + UNKNOWN register before full implementation.

---

## 15. Responsive Contract

Desktop + mobile both authority when present; missing mobile requires decision sheet; overflow and form/menu/modal checks mandatory.

---

## 16. Implementation Contract

Section-by-section under gates; no filler; reference blocks require adaptation; build PASS ≠ visual PASS.

---

## 17. Visual QA Contract

L1–L5 comparison levels; screenshot evidence; allowed verdicts without fake pixel-perfect scores.

---

## 18. Operator Approval Gates

P0–P6 defined; P1+P2 and P3+P4 merge allowed; P0 cannot merge with implementation; P5 cannot auto-declare success.

---

## 19. Git Policy

Selective staging; phase checkpoints; foreign WIP exclusion; force push forbidden.

---

## 20. Failure and Rollback Policy

Stop on input conflict, hallucination, false-green, contamination; rollback to last approved checkpoint with recorded cause.

---

## 21. Pilot Success Criteria

Operator-acceptable desktop/mobile; preserved text; build pass; recorded deviations; normal editability; honest error exposure.

---

## 22. Pilot Failure Criteria

Input violation, scope explosion, false-green, systematic omission, operator REWORK/FAIL, missing mobile authority.

---

## 23. Candidate Matrix

[WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md](../projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md) with Critical/High weights and four verdict classes. No projects scored without inputs.

---

## 24. Launch Sequence

10-step sequence from operator input through P6 pilot result.

---

## 25. Readiness Decision

```text
WF-PR01-A COMPLETE — READY TO SELECT FIRST PILOT INPUT
PILOT READINESS CONTRACT PUBLISHED
AWAITING PILOT INPUT
```

---

## 26. Next Authorized Task

```text
WF-PR01-B — First Pilot Intake and Candidate Approval
```

Executes only after operator supplies concrete real pilot input.

---

## 27. Files Created

| File |
|------|
| `projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md` |
| `projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md` |
| `projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md` |
| `reports/wf-pr01-a-pilot-readiness-contract-v1.md` |

---

## 28. Files Modified

| File |
|------|
| `projects/mars-website-factory/roadmap.md` |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` |

---

## 29. Validation

| Check | Result |
|-------|--------|
| WF-PR01 identity confirmed | **PASS** |
| Authority chain intact | **PASS** |
| Bounded pilot class | **PASS** |
| Intake template published (empty) | **PASS** |
| Visual/text/asset fidelity | **PASS** |
| Russian typography rules | **PASS** |
| Frontend stack fixed | **PASS** |
| Workspace contract | **PASS** |
| Extraction/responsive/QA contracts | **PASS** |
| Operator gates P0–P6 | **PASS** |
| Git/rollback policies | **PASS** |
| Success/failure criteria | **PASS** |
| Candidate matrix | **PASS** |
| Launch sequence | **PASS** |
| One next task only | **PASS** |
| No pilot workspace | **PASS** |
| No implementation | **PASS** |
| No G4 start | **PASS** |
| Coverage unchanged | **PASS** |
| No production-ready claim | **PASS** |

---

## 30. Documentation State

| Surface | State |
|---------|-------|
| Pilot Readiness Contract | **PUBLISHED** |
| Intake template | **PUBLISHED** |
| Candidate matrix | **PUBLISHED** |
| roadmap.md | Synced — WF-PR01-A **COMPLETE** |
| OPERATIONAL-INDEX.md | Synced |

---

## 31. Git Result

| Field | Value |
|-------|-------|
| **Commit** | *(populated after commit)* |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Push** | *(populated after push)* |
| **Files committed** | 6 — contract · intake · matrix · report · roadmap · OPERATIONAL-INDEX |
| **Foreign WIP** | **Excluded** |
| **Force push** | **Not used** |

---

## 32. Drift and Risks

| Risk | Mitigation |
|------|------------|
| Pilot Readiness = production-ready | Contract §4–6 honesty boundary |
| FP-0002 false-green repeat | Visual QA L1–L5; build ≠ visual PASS |
| Reference block misuse | Visual source authority; adaptation required |
| Premature workspace | P0 gate; WF-PR01-B prerequisite |
| G4 accidentally started | Explicit DEFERRED state preserved |
| Foreign WIP in commit | Selective staging only |

---

## 33. Final Status

```text
WF-PR01-A COMPLETE
PILOT READINESS CONTRACT PUBLISHED
AWAITING PILOT INPUT
G4 DEFERRED · NOT STARTED
COVERAGE UNCHANGED
NEXT: WF-PR01-B
```

---

## 34. Next Task

**WF-PR01-B — First Pilot Intake and Candidate Approval** — requires concrete real pilot input from operator.

**Remaining entry question:**

```text
Какой конкретный реальный проект или макет запускается первым?
```

---

## 35. Exact Evidence Paths

```text
projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md
projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md
projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md
reports/wf-pr01-a-pilot-readiness-contract-v1.md
projects/mars-website-factory/wf-r01-3-post-g3-lifecycle-decision-v1.md
projects/mars-website-factory/wf-r01-3-g3-gate-closure-decision-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 36. Stop Confirmation

```text
Pilot Readiness contract: PUBLISHED
Pilot input: NOT SELECTED
Pilot intake: NOT COMPLETED
Pilot workspace: NOT CREATED
Pilot implementation: NOT STARTED
G4 implementation: NOT STARTED
Coverage accrual: NONE
Production readiness: NOT CLAIMED
```

---

*Report: `reports/wf-pr01-a-pilot-readiness-contract-v1.md` · v1 · 2026-06-22*
