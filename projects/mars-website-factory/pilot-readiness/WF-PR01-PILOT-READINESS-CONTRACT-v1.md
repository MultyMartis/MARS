# WF-PR01 Pilot Readiness Contract v1

**Status:** **PUBLISHED** · **WF-PR01-A COMPLETE**  
**Date:** 2026-06-22  
**Mode:** pilot-readiness-contract · first-pilot-launch-boundary · documentation-only  
**Honesty boundary:** Defines operational contract for the first bounded test-production frontend pilot. **Not** pilot workspace creation. **Not** pilot implementation. **Not** G4. **Not** production readiness. **Not** pixel-perfect guarantee. **Not** autonomous factory claim.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Programme** | **WF-PR01** — Website Factory Pilot Readiness |
| **Task** | **WF-PR01-A — Pilot Readiness Contract and First Pilot Launch Boundary** |
| **Task state** | **COMPLETE** |
| **Contract state** | **PUBLISHED** |
| **Pilot input** | **NOT SELECTED** |
| **Pilot workspace** | **NOT CREATED** |
| **Pilot implementation** | **NOT STARTED** |
| **G4** | **DEFERRED · NOT STARTED** |
| **Coverage** | **UNCHANGED** — RC **32/32** · RPC **29/32** · RSC **7/11** |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Stage ID** | **WF-PR01** |
| **Name** | **Website Factory Pilot Readiness** |
| **Parent** | **MARS Website Factory** |
| **Programme parent** | **WF-R01.3** — Reference Implementation Expansion (**OPEN · DESIGN · CONTINUES**) |
| **Authority** | [wf-r01-3-post-g3-lifecycle-decision-v1.md](../wf-r01-3-post-g3-lifecycle-decision-v1.md) |
| **Status** | **AUTHORIZED** · **WF-PR01-A COMPLETE** · **AWAITING PILOT INPUT** |

**WF-PR01 is not:**

- G4;
- production certification;
- autonomous factory programme;
- CMS integration programme;
- universal site-generation programme;
- WF-R01.3 programme closure.

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| Post-G3 lifecycle decision | [wf-r01-3-post-g3-lifecycle-decision-v1.md](../wf-r01-3-post-g3-lifecycle-decision-v1.md) | Authorizes WF-PR01; defers G4 |
| G3 gate closure | [wf-r01-3-g3-gate-closure-decision-v1.md](../wf-r01-3-g3-gate-closure-decision-v1.md) | Operator sign-off · G3 CLOSED |
| G3 formal evaluation | [wf-r01-3-g3-formal-evaluation-decision-v1.md](../wf-r01-3-g3-formal-evaluation-decision-v1.md) | Technical baseline |
| G3 operator report | [wf-r01-3-g3-operator-signoff-gate-closure-v1.md](../../reports/wf-r01-3-g3-operator-signoff-gate-closure-v1.md) | Closure sync |
| Frontend authority order | [frontend-production-authority-order-v1.md](../frontend-production-authority-order-v1.md) | Decision hierarchy |
| Production modes | [website-factory-production-modes-charter-v1.md](../website-factory-production-modes-charter-v1.md) | `PIXEL_PERFECT` \| `TEMPLATE_ART` |
| Pilot adoption flow (legacy lessons) | [pilot-adoption-flow-v1.md](../pilot-adoption-flow-v1.md) | **COMPLEMENTARY** — pre-WF-PR01 adoption pattern |
| FP-0002 forensic lessons | [FP-0002-STRESS-TEST-FORENSIC-v1.md](../../reports/FP-0002-STRESS-TEST-FORENSIC-v1.md) | **LEGACY** risk source — not first pilot selection |

---

## 4. Purpose

Prepare and launch **one bounded real-world frontend pilot** using the current Website Factory architecture, operator rules, and Gulp starter stack — without claiming general production readiness.

**Primary question answered by pilot:**

```text
Can Website Factory produce a useful frontend result from a real visual source
under operator approval gates and honest deviation recording?
```

**Principle:**

```text
Do not continue building Website Factory internals unless a missing capability
directly blocks the first pilot.
```

---

## 5. Scope

This contract covers:

- first pilot class boundary;
- pilot input authority;
- mandatory intake;
- visual, text, and asset fidelity rules;
- frontend stack and workspace contract;
- extraction, responsive, and implementation contracts;
- visual QA method;
- operator approval gates;
- Git/checkpoint policy;
- failure and rollback policy;
- pilot success and failure criteria;
- candidate selection method;
- launch sequence;
- single next authorized task.

---

## 6. Out of Scope

**WF-PR01-A does not create and this contract does not authorize:**

| Item | State |
|------|-------|
| Frontend workspace | **NOT CREATED** |
| HTML / SCSS / JavaScript | **NOT CREATED** |
| Gulp project for pilot | **NOT CREATED** |
| Real page inventory for a project | **NOT CREATED** |
| Real block inventory for a project | **NOT CREATED** |
| Real visual extraction | **NOT PERFORMED** |
| Pilot implementation | **NOT STARTED** |
| CMS integration | **NOT STARTED** |
| G4 implementation | **NOT STARTED** |
| Production readiness claim | **NOT CLAIMED** |
| Registry / Coverage Model mutation | **NOT AUTHORIZED** |
| Reference block creation | **NOT AUTHORIZED** |
| Scaffold / manifest / blueprint mutation | **NOT AUTHORIZED** |

---

## 7. Entry State

| Field | Value |
|-------|-------|
| **Gate G3** | **CLOSED** · **PASS WITH RECORDED NON-BLOCKING DEBT** |
| **WF-R01.3.5** | **COMPLETE** |
| **WF-R01.3 parent** | **OPEN** · **DESIGN** · **CONTINUES** |
| **G4** | **DEFERRED · NOT STARTED** |
| **RC** | **32/32** |
| **RPC** | **29/32** |
| **RSC** | **7/11** |
| **SC** | **LANDING PASS · CATALOG PASS · PROMO PASS** · corporate accepted with G3 debt · ECOMMERCE staging accepted for G3 |
| **PC** | **LANDING PASS · CATALOG PASS · PROMO PASS** · ECOMMERCE **not accrued** |
| **Browser QA** | **Deferred** — pilot must address honestly |
| **Production readiness** | **NOT CLAIMED** |

---

## 8. First Pilot Class

### Preferred class

```text
Corporate landing page
Service landing page
Small corporate frontend
One primary page with shared header/footer/modal components
```

### Recommended volume

| Dimension | Limit |
|-----------|-------|
| **Pages** | **1 primary page** or **1 primary + ≤2 closely related secondary pages** |
| **Sections on main page** | **5–12** |
| **Visual sources** | Desktop + mobile preferred |
| **Tablet** | Optional conservative inference between desktop and mobile |

### Forbidden first pilot scope

```text
full ecommerce runtime
cart/checkout backend
personal account
large multi-language site
complex React/Vue application
large CMS integration
20+ unique pages
incomplete visual source with free invention allowed
```

### Lessons applied (not auto-selected projects)

| Source | Lesson |
|--------|--------|
| FP-0002 | False-green build without FIG verification; text hallucination; image collision; section order drift |
| BZPM / reference slices | Reference blocks are **not** ready-made design — require adaptation to project visual source |
| G3 corporate pilot | Substitution-backed reference slices acceptable for factory gates — **not** for real client pixel fidelity without operator waiver |

---

## 9. Pilot Input Authority

### Acceptable visual inputs

```text
Figma file or Figma export
PNG/JPG screenshots
PDF layouts
Desktop + mobile visual references
Existing approved website screenshots (when operator declares them final authority)
```

### Preferred for first pilot

```text
approved desktop source
approved mobile source
exact texts
available images/assets
known fonts
known interaction expectations
```

### Input authority hierarchy

| Rank | Authority |
|------|-----------|
| **1** | Operator-approved final layout |
| **2** | Operator-approved source assets |
| **3** | Exact supplied text |
| **4** | Existing Website Factory rules (governance, operator laws, production mode) |
| **5** | Explicit **SAFE UNKNOWN** — operator decision required |

**Forbidden:** replacing unknown inputs with invented content, stock imagery, lorem ipsum, or reference-block demo copy.

**Production mode:** must be declared per [website-factory-production-modes-charter-v1.md](../website-factory-production-modes-charter-v1.md) before implementation — **`PIXEL_PERFECT`** expected for first bounded pilot unless operator explicitly selects **`TEMPLATE_ART`**.

---

## 10. Intake Contract

Before any pilot workspace or implementation:

1. Operator supplies or selects **real** pilot input.
2. Operator completes [WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md](WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md).
3. Intake is reviewed at gate **P0 — Pilot Input Approved**.

**Template path:** [WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md](WF-PR01-PILOT-INTAKE-TEMPLATE-v1.md)

**Rule:** intake template is **not** pre-filled with a fictitious project in WF-PR01-A.

---

## 11. Visual Fidelity Contract

Visual source is authority for:

- section order;
- layout hierarchy;
- proportions;
- typography hierarchy;
- alignment;
- spacing relationships;
- visible assets;
- decorative elements;
- desktop/mobile behaviour where shown.

**Factory must not:**

- add new sections;
- reorder sections without operator approval;
- change texts;
- replace images;
- invent decorative elements;
- simplify complex elements without recording debt;
- treat missing mobile layout as permission for arbitrary responsive design.

**If information is absent:**

```text
SAFE UNKNOWN
OPERATOR DECISION REQUIRED
```

**Reference blocks:** may inform structure or survivability patterns only — **not** substitute for project visual source without adaptation and operator approval.

---

## 12. Text Fidelity Contract

Supplied text must be reproduced **exactly** unless operator authorizes editing.

| Rule | Requirement |
|------|-------------|
| Meaning | Do not alter |
| Length | Do not shorten or expand marketing copy |
| Data | Do not replace real data with fictional content |
| Placeholders | Do not use lorem ipsum |
| Structure | Preserve headings and order |
| Contact data | Preserve phones, links, signatures |
| Missing text | Record as **UNKNOWN** — do not invent |

### Russian typography

Short prepositions, conjunctions, and service words must bind to the following word with `&nbsp;` where project rules require it.

Examples:

```html
в&nbsp;Краснодаре
и&nbsp;т.д.
```

Do not modify text inside attributes in ways that break accessibility or form data.

**FP-0002 lesson:** generative paraphrase and invented review/article bodies are **pilot failure** class defects.

---

## 13. Asset Policy

### Priority

| Rank | Source |
|------|--------|
| **1** | Supplied project assets |
| **2** | Approved shared MARS assets |
| **3** | Operator-approved generated assets |
| **4** | Explicit placeholders marked as placeholders |

### Icons

- Use shared **Font Awesome Pro 5.15.4** only when project authority allows.
- Do not publish or broadly commit the whole vendor library.
- Follow controlled/local shared dependency policy.

### Forbidden

- substituting images with random stock assets;
- using web images without approval;
- creating fake logos;
- embedding watermarks;
- committing unavailable proprietary fonts as binaries.

**FP-0002 lesson:** image hash collision and orphan exports require asset inventory and reference verification before PASS.

---

## 14. Frontend Stack

First pilot uses the current operator stack:

```text
HTML
SCSS
JavaScript
jQuery where needed
Gulp
gulp-file-include
```

### Source structure

```text
src/pages
src/partials/sections
src/partials/components
src/scss
src/js
src/img
src/fonts
```

### Build output

```text
dist
```

### Rules

| Rule | Requirement |
|------|-------------|
| `dist` | Never edit manually |
| `@@include` paths | Relative to `src` per current Gulp contract |
| Include paths | No `../` in canonical include paths when Gulp contract requires paths from `src` |
| Include parameters | Valid JSON in double quotes, one line |
| Frameworks | Not introduced without operator authorization |

**Bootstrap path:** copy/adapt from [workspaces/_template-client-v1/](../../workspaces/_template-client-v1/) or existing MARS workspace convention after intake approval — **not** in WF-PR01-A.

---

## 15. Workspace Contract

Pilot workspace is created **only after** operator-approved pilot input and completed intake.

### Naming policy

```text
workspaces/wf-pilot-<NNNN>-<slug>-frontend/
```

or existing canonical MARS workspace convention when operator declares equivalence.

### Required contents (after creation)

```text
README
pilot intake (completed)
source evidence index
page inventory
block inventory
numeric/layout rules
frontend source
build output
QA reports
operator decisions
logs
```

Bulk assets may live outside repo per approved storage policy (`C:\AI MARS STORAGE` supporting layer).

---

## 16. Extraction Contract

Before full implementation, produce a **minimal production-useful** inventory — not a multi-week research programme.

### Required artefacts

```text
Page Inventory
Section Inventory
Shared Component Inventory
Block Mapping
Asset Inventory
Text Inventory
Desktop Numeric Rules
Mobile Numeric Rules
Responsive Decisions
SAFE UNKNOWN Register
```

### Blockers — do not start full implementation until defined

```text
container
main breakpoints
section order
typography hierarchy
key spacing rules
shared header/footer contract
```

Extraction discipline aligns with [implementation-extraction-discipline-v1.md](../implementation-extraction-discipline-v1.md) and [design-source-to-frontend-mapping-governance-v1.md](../design-source-to-frontend-mapping-governance-v1.md).

---

## 17. Responsive Contract

### When desktop and mobile layouts exist

```text
desktop source and mobile source are both authority;
intermediate states are inferred conservatively.
```

### When mobile layout is absent

```text
mobile implementation requires explicit operator-approved responsive decision sheet.
```

### Mandatory checks (project viewports may refine)

```text
1440 / desktop target
1024 transition
768 / tablet or project-specific breakpoint
375–390 mobile
long text wrapping
button wrapping
forms
menus
modal
horizontal overflow
```

Do not apply universal breakpoints mechanically when the design requires project-specific values.

---

## 18. Implementation Contract

Implementation proceeds **section by section** under operator gates.

Each section receives:

```text
source reference
expected content
assets
layout rules
responsive rules
implementation path
validation state
```

### Forbidden

- redesigning sections without approval;
- changing approved structure;
- adding filler content;
- using reference blocks as finished design without adaptation;
- declaring success from build PASS alone.

**Build PASS ≠ visual PASS** — see [operator-visual-approval-law-v1.md](../operator-visual-approval-law-v1.md).

---

## 19. Visual QA Contract

### Levels

| Level | Focus |
|-------|-------|
| **L1** | Structural comparison — section order, major blocks, DOM hierarchy |
| **L2** | Typography comparison — families, sizes, weights, hierarchy |
| **L3** | Spacing and sizing comparison |
| **L4** | Responsive comparison — desktop vs mobile vs approved intermediate |
| **L5** | Visual deviation register — recorded deltas with evidence |

### Comparison inputs

```text
source visual
built page screenshot
difference / deviation evidence
```

### Verdicts (allowed)

```text
PASS
PASS WITH RECORDED DEVIATIONS
REWORK REQUIRED
BLOCKED BY SOURCE
```

**Forbidden:** claiming pixel-perfect percentage without measurable methodology.

Minimum target viewports are set in the pilot intake contract.

Browser QA deferred at G3 must be addressed honestly in pilot — not silently assumed PASS.

---

## 20. Operator Approval Gates

| Gate | Name | Purpose |
|------|------|---------|
| **P0** | Pilot Input Approved | Intake complete; sources and scope bounded |
| **P1** | Inventory and Numeric Rules Approved | Extraction artefacts reviewed |
| **P2** | Frontend Foundation Approved | Workspace, shell, tokens, build baseline |
| **P3** | Desktop Structure Approved | Desktop sections operator-acceptable |
| **P4** | Mobile Structure Approved | Mobile/responsive operator-acceptable |
| **P5** | Visual QA Reviewed | Deviation register reviewed |
| **P6** | Pilot Final Decision | PASS / PASS WITH DEBT / REWORK / FAIL |

### Acceleration (first pilot only)

Allowed merges **with evidence preserved**:

```text
P1 + P2
P3 + P4
```

### Forbidden merges

```text
P0 with implementation
P5 with automatic success declaration
```

**Law:** TECHNICAL PASS ≠ OPERATOR APPROVAL — [operator-visual-approval-law-v1.md](../operator-visual-approval-law-v1.md).

---

## 21. Git Policy

### Before major new phase

```text
check current status
selectively commit stable pilot scope
push
then continue
```

Do not commit after every minor edit.

### Mandatory checkpoints

```text
pilot intake / inventory
frontend foundation
first full desktop build
desktop + mobile implementation
visual QA / final pilot result
```

### Forbidden

```text
git add .
git add -A
git commit -a (without selective review)
force push
mixing foreign WIP
```

Pilot work uses isolated branch or workspace scope; foreign WIP from other programmes must not contaminate pilot commits.

---

## 22. Failure and Rollback Policy

### Stop pilot when

```text
visual input conflict
missing critical mobile authority
unrecoverable include/build failure
systematic text hallucination
systematic section omission
foreign workspace contamination
uncontrolled rewrite of approved implementation
inability to separate source and dist
false-green PASS without visual evidence
```

### Rollback

```text
return to last approved Git checkpoint
record failure cause
do not hide failed attempt
create remediation decision
```

Do not force-push to recover. Do not delete failure evidence.

---

## 23. Pilot Success Criteria

First pilot is successful **only if**:

```text
all approved sections are present
supplied text is preserved
desktop implementation is operator-acceptable
mobile implementation is operator-acceptable
build passes
no critical horizontal overflow
forms/interactions meet the bounded contract
visual deviations are explicitly recorded
operator can continue editing the project normally
the workflow exposes errors instead of masking them
```

### Pilot success does not require

```text
G4 completion
100% autonomy
all site types
CMS integration
universal pixel-perfect score
zero manual corrections
Website Factory production-ready declaration
```

---

## 24. Pilot Failure Criteria

Pilot **fails** or must **stop** when any critical condition holds:

| Condition | Example |
|-----------|---------|
| Input authority violated | Invented copy, stock images, fake logos |
| Scope explosion | Unapproved pages, ecommerce runtime, CMS coupling |
| False-green closure | Build PASS claimed without visual QA evidence |
| Unrecoverable build/include failure | Broken include graph, manual `dist` edits |
| Systematic omission | Missing sections, wrong section order without waiver |
| Operator rejection at P3/P4/P5/P6 | REWORK or FAIL verdict |
| Foreign contamination | Mixed unrelated WIP in pilot scope |
| Missing mobile authority | Mobile invented without decision sheet |

Failure is recorded honestly. Failure does **not** invalidate G3 closure or reference expansion baseline.

---

## 25. Candidate Selection

Use [WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md](WF-PR01-PILOT-CANDIDATE-MATRIX-v1.md) to evaluate candidates **only when concrete inputs exist**.

### Verdict classes

```text
RECOMMENDED
ACCEPTABLE
RISKY
NOT SUITABLE FOR FIRST PILOT
```

**Rule:** do not score projects without real visual sources, texts, and scope declaration.

**Rule:** FP-0002, BZPM, SITE-002, and other existing workspaces are **lesson sources only** — not automatic first pilot selections.

**Remaining entry question after WF-PR01-A:**

```text
Какой конкретный реальный проект или макет запускается первым?
```

---

## 26. Launch Sequence

Minimal sequence:

```text
1. Operator supplies/selects real pilot input.
2. Create completed Pilot Intake.
3. Perform rapid source/inventory extraction.
4. Operator approves P0/P1 (P2 merge allowed with evidence).
5. Create isolated frontend workspace.
6. Create frontend foundation.
7. Implement desktop and mobile.
8. Run build and visual QA.
9. Record deviations and corrections.
10. Operator issues pilot result:
    PASS
    PASS WITH DEBT
    REWORK
    FAIL
```

No new programme gates without operator necessity.

---

## 27. Readiness Decision

```text
WF-PR01-A COMPLETE — READY TO SELECT FIRST PILOT INPUT
```

| Field | Value |
|-------|-------|
| **Operational contract** | **PUBLISHED** |
| **Intake template** | **PUBLISHED** |
| **Candidate matrix** | **PUBLISHED** |
| **Blocker** | **NONE** |
| **Pilot state** | **AWAITING PILOT INPUT** |

---

## 28. Next Authorized Task

**Single next task:**

```text
WF-PR01-B — First Pilot Intake and Candidate Approval
```

| Field | Value |
|-------|-------|
| **Prerequisite** | Operator supplies concrete real pilot input |
| **Creates workspace?** | **No** until P0 approved under completed intake |
| **Starts in WF-PR01-A?** | **No** |

---

## 29. Debt and Risks

| Risk | Mitigation in this contract |
|------|----------------------------|
| Pilot mistaken for production-ready | Bounded purpose; success criteria exclude factory completion |
| G4 debt forgotten | G4 **DEFERRED**; coverage **UNCHANGED** |
| False-green build (FP-0002) | Visual QA levels; build ≠ visual PASS |
| Text hallucination | Text fidelity contract; UNKNOWN register |
| Reference block misuse | Visual source authority; adaptation required |
| Premature workspace | P0 gate; intake mandatory |
| Browser QA gap from G3 | Explicit pilot QA obligation |
| Foreign WIP contamination | Git selective commit policy |

Carried G3 debt (substitution, RSC 7/11, ECOMMERCE PC, DELIVERY, etc.) remains **OPEN** — not resolved by pilot readiness publication.

---

## 30. Evidence Paths

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

## 31. Decision

```text
WF-PR01-A COMPLETE
PILOT READINESS CONTRACT PUBLISHED
AWAITING PILOT INPUT
G4 DEFERRED · NOT STARTED
COVERAGE UNCHANGED
PRODUCTION READINESS NOT CLAIMED
```

---

*Canonical contract: `projects/mars-website-factory/pilot-readiness/WF-PR01-PILOT-READINESS-CONTRACT-v1.md` · v1 · 2026-06-22*
