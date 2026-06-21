# MARS Website Factory — Frontend Design QA Matrix v1

**Status:** **documented** — canonical **human-operated** QA framework for validating frontend implementation against **approved design source** before **Production PASS**.  
**Not:** automated pixel diff, Figma plugin, CI gate, computer vision, or runtime enforcement product.

**Purpose:** Provide a **single Factory-level matrix** that operators, Leads, and agents use to decide whether built HTML/CSS faithfully implements approved design evidence — without aesthetic improvisation, silent normalization, or undocumented drift.

**Authority order (canonical):** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md)

| Rank | Layer | Role in QA |
|------|-------|------------|
| **1** | **Project Production Standards** | Per-project SSOT — px, hex, type, spacing, layout zone bindings |
| **2** | **Approved Operator Laws (OL-01–OL-07)** | Spacing scale, layout pattern first, typography precision |
| **3** | **This matrix + peer Factory governance** | Domain checks, severity, verdict vocabulary |
| **4** | **Layout Pattern Library (LP-* / WF zones)** | Named patterns — WF-GRID, WF-LAYOUT |
| **5–6** | Industry Best Practice · Agent Preference | **Never** override ranks 1–4 |

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules) — register on Evolution Pack integration.

**Related (integration — not duplication):**

| Document | Role |
|----------|------|
| [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | Numeric/variance rules per PF-* domain — detail under this matrix |
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Pre-code mapping QA gate |
| [frontend-design-calibration-stage-v1.md](frontend-design-calibration-stage-v1.md) | Foundation token verification |
| [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) | Spacing/type normalization law |
| [production-standards-governance-v1.md](production-standards-governance-v1.md) | Standards Draft + Approval |
| [frontend-shell-first-start-protocol-v1.md](frontend-shell-first-start-protocol-v1.md) | Stage chain placement |
| [visual-reconciliation-layer.md](visual-reconciliation-layer.md) | Qualitative intent read — complements, does not replace PF-* |
| [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) | RU commercial mandatory widths |
| [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Operational routing surface |
| [frontend-compliance-decision-model-v1.md](frontend-compliance-decision-model-v1.md) | RAW VIOLATION → Compliance Verdict route for DQ-02a/DQ-02b findings |

**Honesty boundary:** This matrix is **human-operated governance**. It does **not** claim an in-repo QA engine, linter, or automated Production PASS unless a project explicitly adopts checklists as tooling.

---

## 1. Purpose

The Frontend Design QA Matrix answers:

> **Does this frontend implementation match the approved design source and project SSOT — within Factory precision law — before Production PASS?**

It applies at:

| Gate | Scope | Matrix usage |
|------|-------|----------------|
| **Foundation QA** | Shell + Foundation Demo Page | Domains DQ-01–DQ-09, DQ-12; subset of DQ-06–DQ-07 |
| **Page / block Production QA** | Home, inner pages, commercial blocks | Full matrix DQ-01–DQ-12 |
| **Pre–Production PASS** | Frozen slice or page ready for Lead sign-off | Full matrix + final verdict §6 |

**Production PASS** (Factory meaning): Lead-acknowledged closure where **Frontend Design QA Matrix final verdict** is **PASS** or **PASS WITH NOTES** (§6) and peer gates (build, mapping, calibration where applicable) are satisfied.

---

## 2. Scope

### 2.1 Supported design sources

All domains apply **regardless of source format**. Source type affects **evidence method**, not **pass bar**.

| Source type | Notes |
|-------------|-------|
| **Figma** | Preferred — frames, components, variables, export specs |
| **PDF** | Static artboards; measure from vector/raster layers |
| **PNG** | Raster export; watch compression and crop artifacts |
| **JPG** | Same as PNG — lower fidelity for fine type/spacing |
| **WebP** | Same as PNG — verify color profile |
| **Screenshot Pack** | Ordered viewport captures; may be only source |
| **Mixed Sources** | Requires explicit **source priority** in Production Decisions (C-12) |

**Authority for mixed sources:** [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) §2.

### 2.2 In scope

- Built static UI (`src/` → `dist/`) vs approved design evidence + **Project Production Standards**
- Token, layout, component, state, asset, responsive, content, business-intent, and basic accessibility fidelity
- REPORT evidence lines per domain

### 2.3 Out of scope

- Autonomous design reading or CV extraction
- Pixel-diff automation scores (unless project adopts tooling — **SAFE UNKNOWN** until documented)
- Forge overlay semantics alone without foundation/matrix cross-check
- SEO, conversion copy strategy, legal claims — separate QA lanes

---

## 3. QA Domains

Each domain uses **PASS** / **FAIL** criteria below. A domain **FAIL** with **Critical** severity (§5) blocks Production PASS unless waived by Lead with written record.

### DQ-01 — Typography

**Compare:** H1–H6, body, secondary tiers, weights, line-heights, letter-spacing (if in SSOT), font-family stack vs **Project Production Standards** type table and approved design source measurements (normalized per OL-05).

| Verdict | Criteria |
|---------|----------|
| **PASS** | Sizes match approved standards; weights match; line-heights match approved project rules (default Factory: `line-height = font-size + 4px` unless named exception in SSOT); no arbitrary type scale invented per block |
| **FAIL** | Any heading/body tier off SSOT without documented exception; forbidden arbitrary px/rem; agent-resized type for “better hierarchy”; RU projects violate [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md) |

**Detail authority:** [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) PF-01 · [frontend-precision-governance-v1.md](frontend-precision-governance-v1.md) §3.

---

### DQ-02a — Project SSOT Spacing Compliance

**Compare:** Margins, padding, gaps, section spacing tokens vs **Project Production Standards** spacing table and named inter-section tokens.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Values match approved project SSOT spacing table; inter-section spacing uses approved tokens ([frontend-section-spacing-rule-v1.md](frontend-section-spacing-rule-v1.md)); raw design values mapped with C-12 record |
| **FAIL** | Value not in project SSOT without documented exception; per-block one-off spacing vs SSOT; percentage padding outside project charter |

**Detail authority:** PF-03 · [production-standards-governance-v1.md](production-standards-governance-v1.md) C-12.

---

### DQ-02b — Operator Law Spacing Compliance

**Compare:** Margins, padding, gaps vs **Approved Operator Laws OL-01–OL-02** — **independent** of whether project SSOT approves the value.

| Verdict | Criteria |
|---------|----------|
| **PASS** | All gap/margin/padding values on OL-01 scale (or OL-02 percentage padding in allowed scope) |
| **FAIL** | Values such as `17px`, `23px`, `37px`, `64px` without OL scale membership **and** without valid Exception Registry when rank-1 SSOT overrides OL |
| **WAIVED** | Rank-1 SSOT intentionally overrides OL **and** complete Exception Registry per [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) §6 |

**Sources:** `src/scss/**` **and** `dist/*.css` — source-only review **insufficient** for PASS.

**Detail authority:** OL-01 · OL-02 · [website-factory-enforcement-pack-v1.md](website-factory-enforcement-pack-v1.md) §3.1 · PF-03.

**Note:** DQ-02a and DQ-02b are **separate checks**. Project SSOT PASS does **not** imply Operator Law PASS.

---

### DQ-03 — Container

**Compare:** Section shell vs inner container, `--container-max`, `--container-pad`, full-bleed bands vs content width.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Section ≠ container (WF-GRID-001); one page = one grid contract (WF-GRID-002); full-bleed backgrounds on section with content inside container (WF-GRID-004); local max-width/padding only with `WF-GRID-EXCEPTION` |
| **FAIL** | Container class on `<section>`; silent per-section container drift; shell bypass for column splits |

**Detail authority:** PF-02 · [WF-GRID-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md).

---

### DQ-04 — Grid

**Compare:** Page-level grid contract, alignment of header / hero / sections / footer inner edges (WF-GRID-005).

| Verdict | Criteria |
|---------|----------|
| **PASS** | All major blocks share same container grid; no horizontal misalignment at desktop review width; grid tokens match SSOT C-01 / C-11 |
| **FAIL** | Visible stair-step alignment; mixed container max-width without exception; grid contract broken on foundation or page |

**Detail authority:** PF-02 · PF-04 · WF-GRID-005.

---

### DQ-05 — Layout

**Compare:** Hero splits, card grids, trust strips, finance zones vs WF-LAYOUT + named LP-* patterns.

| Verdict | Criteria |
|---------|----------|
| **PASS** | **WF-GRID PASS** and **WF-LAYOUT PASS**; approved pattern used (fr/minmax/repeat or documented LP-*); collapse behavior documented for responsive; no default `%` column splits |
| **FAIL** | Ad-hoc `65% 35%` hero; layout assembled by eye; Design → HTML shortcut skipping WF-LAYOUT; FAQ 2-col grid accordion stretch ([frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §5) |

**Detail authority:** PF-04 · [WF-LAYOUT-DISCIPLINE-v1.md](../../workspaces/website-factory-reference-v1/frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md) · [frontend-layout-pattern-library-requirement-v1.md](frontend-layout-pattern-library-requirement-v1.md).

---

### DQ-06 — Components

**Compare:** Buttons, inputs, cards, nav, badges, icons vs design source component specs and SSOT control tokens.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Each implemented pattern matches chartered structure (Purpose, Hierarchy per mapping §5); variants (primary/secondary/outline) match standards; no starter/demo component substituting for design |
| **FAIL** | Missing required variant; wrong hierarchy inside component; generic template component used where design defines distinct treatment |

**Detail authority:** PF-05 · [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) §5.

---

### DQ-07 — States

**Compare:** Hover, focus-visible, active, disabled, error, success, open/closed (accordion, modal, details) vs source or SSOT state matrix.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Documented states present; absent states marked UNKNOWN in mapping — not invented; focus visible; native `<details>` SoT respected ([frontend-production-invariants-v1.md](frontend-production-invariants-v1.md) §4) |
| **FAIL** | Invented states not in source; hybrid native/custom accordion; missing error state where standards require; JS-only essential state without CSS fallback |

**Detail authority:** [ui-state-taxonomy.md](ui-state-taxonomy.md) · [state-behavioral-consistency-governance.md](state-behavioral-consistency-governance.md).

---

### DQ-08 — Assets

**Compare:** Logos, icons, photos, illustrations, favicon vs approved asset set — no unapproved placeholders.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Real assets or Lead-approved recreation; correct aspect ratio and crop; SVG/raster matches source intent; favicon wired per project |
| **FAIL** | Placeholder logo/icon/image in production path; wrong asset; **wrong client brand mark** (see [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md)); compressed artifact changing perceived weight; duplicated baked-in annotation ([semantic-iconography-governance.md](semantic-iconography-governance.md)) |

**Detail authority:** PF-07 · mapping L-07 · [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) (upstream selection).

---

### DQ-09 — Responsive

**Compare:** Breakpoint behavior vs source + SSOT + project handoff; overflow and collapse at required widths.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Project breakpoints only — no ad-hoc `981px`; no horizontal scroll; RU commercial: [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) widths tested; collapse matches documented intent ([responsive-intent-governance.md](responsive-intent-governance.md)) |
| **FAIL** | Untested RU preset when locale is RU commercial; desktop-only PASS claimed for full responsive scope; layout breaks at chartered width |

**Detail authority:** PF-06 · [responsive-collapse-taxonomy.md](responsive-collapse-taxonomy.md).

---

### DQ-10 — Content Fidelity

**Compare:** Copy, headings, lists, counts, CTA labels, legal micro-copy vs approved content / blueprint — not design pixels alone.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Text matches approved source; no lorem/AI filler in production path; entity counts correct; link targets and `tel:`/`mailto:` as chartered |
| **FAIL** | Wrong headline; missing bullet; placeholder copy; semantic QA failure on meaning |

**Note:** Semantic lane may own detailed copy QA; this domain blocks Production PASS when **visual implementation ships wrong content**.

---

### DQ-11 — Business Intent

**Compare:** CTA emphasis, trust placement, conversion narrative, commercial density vs design intent and [strategic-intent-governance.md](strategic-intent-governance.md).

| Verdict | Criteria |
|---------|----------|
| **PASS** | Primary CTA visually dominant per source; trust/proof positioned per charter; no beautification drift ([beautification-drift-governance.md](beautification-drift-governance.md)); visual reconciliation FINDINGS dispositioned |
| **FAIL** | Secondary action visually wins over primary; trust block overtakes hero focal path; SaaSification / fake premiumization without approval |

**Detail authority:** [visual-reconciliation-layer.md](visual-reconciliation-layer.md) · [design-intent-transfer-governance.md](design-intent-transfer-governance.md).

---

### DQ-12 — Accessibility Basic Check

**Compare:** Keyboard, focus, labels, contrast intent, tap targets vs [accessibility-intent-governance.md](accessibility-intent-governance.md) — **basic operational check**, not WCAG certification.

| Verdict | Criteria |
|---------|----------|
| **PASS** | Interactive controls are buttons/links with accessible names; focus visible; form labels associated; modal ESC + focus trap behavior sane; min tap targets per project policy |
| **FAIL** | Div-click CTAs without role; missing labels; focus clipped; modal under sticky blocking use; decorative ARIA theater |

**Scope note:** Full accessibility audit is **out of matrix v1 scope** unless project charter requires — mark **Observation** for deferred a11y depth.

---

## 4. Domain summary table

| ID | Domain | Primary authority |
|----|--------|-------------------|
| DQ-01 | Typography | Production Standards · OL-05 · PF-01 |
| DQ-02a | Project SSOT Spacing | Production Standards · PF-03 |
| DQ-02b | Operator Law Spacing | OL-01 · OL-02 · Enforcement Pack · PF-03 |
| DQ-03 | Container | WF-GRID · PF-02 |
| DQ-04 | Grid | WF-GRID · PF-02 |
| DQ-05 | Layout | WF-LAYOUT · LP-* · PF-04 |
| DQ-06 | Components | Mapping §5 · PF-05 |
| DQ-07 | States | UI state governance |
| DQ-08 | Assets | Mapping L-07 · PF-07 |
| DQ-09 | Responsive | RU preset · PF-06 |
| DQ-10 | Content Fidelity | Blueprint / content SSOT |
| DQ-11 | Business Intent | Visual reconciliation · beautification drift |
| DQ-12 | Accessibility Basic | Accessibility intent governance |

---

## 5. Severity model

Assign **one severity per finding**. Multiple Critical findings → final verdict **FAIL** (§6) unless Lead waiver.

| Severity | Meaning | Production PASS impact |
|----------|---------|---------------------------|
| **Critical** | Blocks user task, violates SSOT law, wrong layout chain, missing approved asset, RU typography law break, or authority inversion (agent preference over SSOT) | **Blocks PASS** — fix or documented Lead waiver |
| **Major** | Visible drift from source/SSOT; wrong spacing scale; misaligned grid; wrong component variant; responsive break at required width | **Blocks PASS** unless folded into **PASS WITH NOTES** with explicit Lead ack and fix plan |
| **Minor** | Small variance within PF acceptable band; cosmetic delta with no intent impact | May PASS WITH NOTES |
| **Observation** | Note for backlog; deferred check; informational | Does not block PASS |

**Forbidden severity rationale:** “Looks cleaner”, “looks more modern”, “industry standard prefers…”, “agent improved hierarchy” — **invalid**; reclassify as **Major** (beautification drift) or dismiss.

---

## 6. Final verdict model

After all applicable domains are evaluated:

| Verdict | Meaning | Production PASS |
|---------|---------|-----------------|
| **PASS** | All applicable domains **PASS**; no Critical/Major open findings | **Allowed** |
| **PASS WITH NOTES** | No Critical open; Major findings **explicitly waived** or scheduled with Lead ack; Minor/Observation listed | **Allowed** with documented notes |
| **FAIL** | Any Critical open; or any Major without waiver; or mandatory gate peer FAIL (build, mapping, calibration) | **Blocked** |

**Recommended REPORT block:**

```text
FRONTEND DESIGN QA MATRIX — PASS | PASS WITH NOTES | FAIL
DOMAIN SUMMARY — DQ-01: PASS | FAIL · DQ-02a: PASS | FAIL · DQ-02b: PASS | FAIL | WAIVED · … · DQ-12: PASS | FAIL | N/A
SEVERITY — Critical: (n) · Major: (n) · Minor: (n) · Observation: (n)
PIXEL FIDELITY AUDIT — PASS | PASS WITH NOTES | FAIL | N/A (see pixel-fidelity-audit-rules-v1.md)
WF GRID DISCIPLINE — PASS | FAIL
WF LAYOUT DISCIPLINE — PASS | FAIL
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial | FAIL | SAFE UNKNOWN | N/A
```

---

## 7. Gate placement in Factory chain

```text
Design source(s)
        ↓
DESIGN → FRONTEND MAPPING QA          ← mapping quality (pre-Approval)
        ↓
Production Standards Approval
        ↓
Shell → Visual Foundation
        ↓
Design Calibration                     ← token implementation vs SSOT
        ↓
Foundation QA                          ← matrix subset + discipline lines
        ↓
Page / block production
        ↓
Design Completeness Audit              ← entity presence (page/slice level)
        ↓
Frontend Design QA Matrix (full)       ← THIS MATRIX at slice/page level
        ↓
Pixel Fidelity Audit                   ← numeric variance (peer detail)
        ↓
Production PASS
```

| Stage | Matrix scope |
|-------|----------------|
| Mapping QA | Informs DQ domains in **Draft** — not full implementation matrix |
| Design Calibration | DQ-01, DQ-02a, DQ-02b, DQ-03, DQ-06 subset on demo page |
| Foundation QA | DQ-01–DQ-09, DQ-02a, DQ-02b, DQ-12 on foundation URL + shell |
| Page Production QA | Full DQ-01–DQ-12 after Design Completeness PASS |

---

## 8. Agent stop rules

| Condition | Action |
|-----------|--------|
| Value not on OL-01 scale and not in SSOT | **STOP** — map or escalate HITL |
| SSOT PASS assumed to cover Operator Law | **STOP** — run DQ-02a **and** DQ-02b separately |
| Layout without WF-GRID → WF-LAYOUT → LP-* | **STOP** — document chain |
| Claim Production PASS without matrix verdict | **STOP** — complete §6 REPORT |
| Aesthetic override cited as fix | **STOP** — cite rank 1–4 authority |
| RU commercial without preset widths | **STOP** — run [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) |

---

## 9. Relationship to peer QA surfaces

### 9.1 Scope disambiguation (do not confuse matrices)

| Document | Scope | When to use | Production PASS authority? |
|----------|-------|-------------|----------------------------|
| **This doc** — Frontend Design QA Matrix v1 | **Implementation fidelity** vs approved design + project SSOT — domains DQ-01–DQ-12 | Foundation subset (pre–Home) **or** full matrix (page/slice closure) | **Yes** — when combined with Completeness + PF per [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) §6 |
| [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md) | **Site-level lifecycle** — Intake → Strategy → IA → Blueprint → Design → Frontend → Delivery | Reference project runbooks; stage × lane posture (Required / Blocking / HITL) | **No** — routes HITL and stage gates; **not** pixel/design fidelity |
| [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md) | **Blueprint artifact** quality before design handoff | Pre-implementation IA/blueprint | **No** |
| [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | **Compact post-build smoke** — reference/client workspace | After build; adoption/bootstrap | **No** — points to reporting standard for full Production PASS |

**Rule:** If the task is **«does this HTML/CSS match design?»** → **this matrix**. If the task is **«which QA lanes apply at Strategy stage?»** → **reference-project-qa-matrix-v0**. If the task is **«is foundation ready before Home?»** → [frontend-foundation-qa-governance-v1.md](frontend-foundation-qa-governance-v1.md).

| Peer | Relationship |
|------|----------------|
| [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | Variance math and compare method — **detail** under DQ domains |
| [visual-reconciliation-layer.md](visual-reconciliation-layer.md) | Qualitative intent — feeds **DQ-11**; does not replace PF-* |
| [visual-regression-workflow-v1.md](visual-regression-workflow-v1.md) | Screenshot evidence — supports DQ-09, DQ-11 |
| [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Routes to compact passes — matrix is **authority** for Production PASS |
| [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md) | **Site-level** stage × lane matrix — complementary; integrate on Evolution Pack v2 |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-13 | v1 — Frontend Design QA Matrix: DQ-01–DQ-12, severity model, PASS / PASS WITH NOTES / FAIL verdict; Factory Production PASS gate. |
| 2026-06-14 | v1.1 — Enforcement Pack v1: DQ-02 split → DQ-02a (Project SSOT) · DQ-02b (Operator Law); compiled CSS source requirement. |
