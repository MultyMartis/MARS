# REPORT — WF-R01 PROGRAM AUTHORITY PASS

**Program ID:** WF-R01 — FOUNDRY Registry Expansion Program  
**Дата:** 2026-06-19  
**Режим:** authority / program governance analysis — **без implementation**  
**База:** [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) · [wf-r01-1-v0-v1-binding-charter-design-v1.md](wf-r01-1-v0-v1-binding-charter-design-v1.md) · [roadmap.md](../projects/mars-website-factory/roadmap.md) · [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) · [website-factory-production-modes-charter-v1.md](../projects/mars-website-factory/website-factory-production-modes-charter-v1.md) · [website-factory-validation-architecture-charter-v1.md](../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md) · [website-factory-vl3-domains-charter-v1.md](../projects/mars-website-factory/website-factory-vl3-domains-charter-v1.md)

**Honesty boundary:** Этот pass определяет **program authority state** — human-operated governance semantics. **Не** runtime, **не** orchestration, **не** автоматический статус engine.

**Терминология:** **FOUNDRY** = **Website Factory** ecosystem (строка FOUNDRY как отдельный продукт/путь в repo **не найдена**).

---

## Executive Summary

WF-R01 **спроектирован** в `reports/foundry-registry-expansion-program-design-v1.md` (2026-06-19) и подпрограмма WF-R01.1 **спроектирована** в `reports/wf-r01-1-v0-v1-binding-charter-design-v1.md`. Оба артефакта — **design reports**, не charter acceptance.

**Вердикт Program Authority Pass:** WF-R01 находится в статусе **PROPOSAL** — не официальная программа FOUNDRY/Website Factory в каноне.

| Факт | Состояние |
|------|-----------|
| WF-A01 Production Modes | **Complete** — charter + implementation pass в roadmap |
| WF-A02 Validation Architecture + VL3 | **Complete** — charter + implementation passes в roadmap |
| WF-A03 Pixel Factory | **DEFERRED** — явный marker в roadmap |
| WF-R01 Registry Expansion | **PROPOSAL** — только reports/; **отсутствует** в roadmap и OPERATIONAL-INDEX |
| WF-R01.1 Binding Charter | **PROPOSAL** (design) — **нет** ACCEPTED charter artifact |

**Рекомендуемый следующий шаг:** human sign-off на Program Charter (перевод WF-R01 **PROPOSAL → CHARTERED**) + charter pass для roadmap/OPERATIONAL-INDEX registration — **до** старта WF-R01.2.

---

## Current Authority State

### Канон Website Factory (что считается «официальным»)

| Layer | Canonical location | WF-R01 presence |
|-------|-------------------|-----------------|
| **Roadmap — Factory architecture items (WF-Axx)** | `projects/mars-website-factory/roadmap.md` § Factory architecture items | **WF-R01 отсутствует** |
| **OPERATIONAL-INDEX — Core Run** | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | **Нет строки** Registry Expansion / v0→v1 binding |
| **Charter stack (WF-A01/A02)** | `website-factory-*-charter-v1.md` | WF-R01 **не** charter; **не** ссылается из charters |
| **Program design** | `reports/foundry-registry-expansion-program-design-v1.md` | **Единственный** program-level artifact |
| **Subprogram design** | `reports/wf-r01-1-v0-v1-binding-charter-design-v1.md` | Design only; future accepted artifact: `wf-r01-1-v0-v1-binding-charter-v1.md` (**не существует**) |
| **Foundation registry canon** | `workspaces/website-factory-reference-v1/` | v1 ACCEPTED; structural gaps OPEN — **не** результат WF-R01 execution |

### Что означает «официальная программа» в текущей дисциплине repo

По преcedent WF-A01 / WF-A02:

1. **Charter или architecture doc** в `projects/mars-website-factory/` или `reports/` с явным implementation pass.
2. **Registration в roadmap.md** — строка в таблице Factory architecture items со статусом.
3. **OPERATIONAL-INDEX visibility** — Core Run row для операторов.
4. **Human sign-off** — implementation pass report фиксирует Complete.

WF-R01 имеет только пункт **1 partial** (program design в reports/) без пунктов 2–4.

### Dual canon context (authority gap)

Аудиты и WF-R01.1 design фиксируют **dual canon** (v0 vs v1). Это **не** блокирует PROPOSAL status, но объясняет **зачем** нужна программа: канон v1 ACCEPTED в Foundation, операционные Wave 4–6 артефакты **всё ещё цитируют v0**. Program authority pass **не** разрешает drift — только классифицирует program state.

---

## Program Status

### Program Authority Model (derived — не formalized in repo)

Formal Program Authority Model **не обнаружен** в `governance/` или Website Factory pack. Модель ниже **выведена** из precedent WF-Axx и program design discipline:

| Status | Definition | Entry signal | Exit / transition |
|--------|------------|--------------|---------------------|
| **PROPOSAL** | Program/subprogram **designed** in reports; **not** registered in roadmap or OPERATIONAL-INDEX; **no** human ACCEPTED charter | Program design report published | Human sign-off → CHARTERED |
| **CHARTERED** | Program **registered** in roadmap; scope/exit criteria **accepted**; execution **not started** on subprograms beyond design | Roadmap row + program charter ACCEPTED | First subprogram execution gate passed → ACTIVE |
| **ACTIVE** | At least one subprogram **in execution** under accepted gates | WF-R01.1 P1 ACCEPTED or equivalent | All program exit criteria → COMPLETE |
| **COMPLETE** | Program exit criteria met; completion REPORT published | Exit criteria § below | — |
| **DEFERRED** | Explicit operator decision to pause; preconditions documented | Human charter / roadmap marker | Preconditions met → CHARTERED or ACTIVE |

### WF-R01 classification

| Criterion | Evidence | Result |
|-----------|----------|--------|
| Program design exists | `foundry-registry-expansion-program-design-v1.md` | ✓ |
| Registered in roadmap | `roadmap.md` — **only WF-A01, A02, A03** | ✗ |
| OPERATIONAL-INDEX row | **Absent** | ✗ |
| Program charter ACCEPTED | **No** accepted program charter artifact | ✗ |
| Subprogram WF-R01.1 ACCEPTED | Design only; B1 **not** satisfied | ✗ |
| Execution started (R01.2+) | Task explicitly forbids R01.2 | ✗ |

**WF-R01 status: PROPOSAL**

### Subprogram WF-R01.1 status

| Phase (from R01.1 design) | State |
|----------------------------|-------|
| P0 — Charter design | **Done** — `wf-r01-1-v0-v1-binding-charter-design-v1.md` |
| P1 — Charter ACCEPTED | **Not done** — no `wf-r01-1-v0-v1-binding-charter-v1.md` |
| P2–P5 — Banner, STOP, cutover, audit | **Not started** |

**WF-R01.1 status: PROPOSAL** (design complete; **not** program entry gate satisfied)

### Условия запуска программы (PROPOSAL → CHARTERED → ACTIVE)

| Gate | Requirement | Current |
|------|-------------|---------|
| **G0** | WF-A01 **Complete** | ✓ |
| **G1** | WF-A02 **Complete** (incl. VL3 Pass 02) | ✓ |
| **G2** | Program design reviewed (this pass) | ✓ (this document) |
| **G3** | Human sign-off: WF-R01 **accepted as chartered program** | **Pending** |
| **G4** | Roadmap registration (WF-R01 row) | **Pending** — recommendation only |
| **G5** | OPERATIONAL-INDEX Core Run row | **Pending** — recommendation only |
| **G6** | WF-R01.1 binding charter **ACCEPTED** (B1) | **Pending** |
| **G7** | Metrics baseline M1–M10 recorded (R01.X) | **Pending** |

**Program ACTIVE** = G0–G7 satisfied **and** at least one subprogram beyond design-only execution started (typically R01.1 P2+ or R01.2 after R01.1 exit).

**Explicit:** WF-R01 **must not** auto-start from WF-A02 completion alone — program design and WF-A03 deferred marker both require **human charter** before execution.

---

## Program Relationships

### WF-A01 / WF-A02 / WF-R01 / WF-A03

```
WF-A01  Production Modes Contract          ✅ Complete (2026-06-17)
WF-A02  Validation Architecture             ✅ Complete (2026-06-17/18)
        + VL3 Domains Pass 02
   ↓
WF-R01  Registry Expansion Program         ◆ PROPOSAL (not in roadmap)
   ↓
[Parallel] VL3 adoption on PIXEL greenfield  ← WF-A02 discipline; not blocked on R01
   ↓
WF-A03  Pixel Factory Expansion             ⏸ DEFERRED (roadmap official)
```

### Является ли WF-A02 → WF-R01 → WF-A03 официальной последовательностью?

| Source | Sequence claim | Official? |
|--------|----------------|-----------|
| **roadmap.md** (canonical) | WF-A03 start = WF-A01 **AND** WF-A02 complete; **no WF-R01** | WF-R01 **not** in chain |
| **foundry-registry-expansion-program-design-v1.md** (proposal) | WF-A02 → **WF-R01** → WF-A03; A03 deferred until R01 Gate 2+ **recommended** | **Proposed**, not registered |
| **WF-A03 deferred marker** (roadmap) | Auto-start **forbidden**; Research Pass required | **Official** |

**Verdict:** Последовательность WF-A02 → WF-R01 → WF-A03 — **proposed architecture**, **не** официальный канон. Официальный канон сегодня: WF-A01 ✓ → WF-A02 ✓ → WF-A03 **DEFERRED** (without WF-R01 precondition).

**Relationship semantics (when CHARTERED):**

| Program | Relationship to WF-R01 |
|---------|------------------------|
| **WF-A01** | **Upstream authority.** TEMPLATE_ART SSOT = Block Registry v1; WF-R01 closes implementation cliff and v0 drift — **enables honest TEMPLATE_ART** beyond LANDING-only. WF-R01 **does not amend** Production Modes charter. |
| **WF-A02** | **Orthogonal validation plane.** VL1 consumes Site Type + Block Registry; WF-R01 **expands vocabulary** WF-A02 validates against. WF-R01 **explicitly excludes** machine-enforced validation automation. |
| **WF-A03** | **Downstream deferred.** Program design: A03 **after** R01 Gate 2+ **or** explicit operator waiver. Roadmap **does not yet** encode R01 precondition. |

### WF-R01 subprogram dependency chain (from program design — proposal scope)

```
WF-R01.1  v0→v1 Binding          ← program entry gate (blocks all)
   ↓
WF-R01.2  Structural Blocks      ← blocks catalog honesty, R01.3 structural partials
   ↓ (parallel after R01.1)
WF-R01.3  Reference Expansion    ‖  R01.4  Commercial Patterns
                               ‖  R01.5  SEO Content Slice
                               ‖  R01.6  Registry Hygiene
                               ‖  R01.8  Execution Case Feed
   ↓
WF-R01.7  Template-Art Multi-Site-Type  ← requires R01.2 + R01.3 Gate 2 minimum
```

---

## Conflict Analysis (WF-R01 vs WF-A01 / WF-A02 / VL3)

### Production Modes Charter (WF-A01)

| Aspect | Assessment |
|--------|------------|
| **Scope boundary** | WF-R01 = registry/reference/docs; WF-A01 = fidelity contracts — **no scope overlap conflict** |
| **TEMPLATE_ART SSOT** | Charter §4.2 rank 3: Site Type + Block Registry. WF-R01 **strengthens** this SSOT — **aligned intent** |
| **Terminology drift** | Production Modes charter uses `site_type_id` in places; v1 canon uses `site_type_code`. WF-R01.1 binding **resolves** — charter pass **recommended**, not conflict |
| **LANDING-only reality** | Capability audit + WF-R01.7 interim policy **extends** WF-A01 honesty — WF-A01 does not claim multi-type Template-Art readiness |
| **Machine enforcement** | Both: human-operated — **aligned** |

**Verdict:** **No governance conflict.** **Terminology harmonization** needed via WF-R01.1 charter pass (link, not replace WF-A01).

### Validation Architecture Charter (WF-A02)

| Aspect | Assessment |
|--------|------------|
| **VL1 inputs** | Site Type Registry + Block Registry — WF-R01 **feeds** VL1 with expanded/honest vocabulary |
| **False-green** | WF-R01 M2 reference coverage metrics **complement** WF-A02 false-green closure — **aligned** |
| **Automation** | WF-R01 excludes CI/machine gates; WF-A02 explicit non-goals match — **aligned** |
| **Lifecycle** | WF-R01 does not alter BUILT/VERIFIED/PRODUCTION PASS — **no conflict** |

**Verdict:** **No conflict.** WF-R01 is **upstream registry truth** for validation inputs.

### VL3 Domains Charter (WF-A02 Pass 02)

| Aspect | Assessment |
|--------|------------|
| **Primary mode** | VL3 = PIXEL_PERFECT composition/extract — **orthogonal** to registry expansion |
| **FP-0002** | Parallel track for VL3 adoption; program design assigns **not** primary block source for R01 — **aligned** |
| **Block registry in VL3** | VL3 validates composition against design SSOT, not block_id catalog expansion — **orthogonal** |

**Verdict:** **No conflict.** Parallel execution permitted.

### Cross-cutting risk (not charter conflict)

| Risk | Severity | Note |
|------|----------|------|
| Operators treat PROPOSAL as ACTIVE | **High** | Program design depth may imply false authority |
| TEMPLATE_ART on CATALOG before R01.2 | **Critical** | WF-A01 allows Template-Art; WF-R01.7 interim policy **not yet** in OPERATIONAL-INDEX |
| v0 ID creep during «informal» R01 work | **Critical** | Without CHARTERED + R01.1 ACCEPTED, expansion **multiplies** drift |

---

## Exit Criteria

### Program-level exit (WF-R01 → COMPLETE)

Derived from [foundry-registry-expansion-program-design-v1.md](foundry-registry-expansion-program-design-v1.md) § Success Metrics — **proposed** until program CHARTERED:

WF-R01 считается **COMPLETE** when **all** true:

| # | Criterion | Metric / artifact |
|---|-----------|-------------------|
| E1 | WF-R01.1 binding charter **ACCEPTED** + B6 zero new v0 IDs post-T_cutover | B1–B6 |
| E2 | WF-R01.2 structural blocks **ACCEPTED** in registry v1.1 | M3 = 3/3 |
| E3 | Reference partial coverage **≥ 63%** (Gate 2) + catalog scaffold partials exist | M2 ≥ 20/32 |
| E4 | WF-R01.4 commercial pattern catalog v0 **published** | M5 ≥ 4 pattern_id |
| E5 | WF-R01.5 SEO content slice **published** | M6 ≥ 6 page types |
| E6 | WF-R01.7 Template-Art readiness matrix **ACCEPTED** | M7 ≥ 2/5 pilot-ready |
| E7 | WF-R01.8 execution case lesson index **published** | M9 ≥ 4 cases |
| E8 | Roadmap updated: WF-R01 **Complete** + WF-A03 preconditions re-evaluated | R01.X |
| E9 | Program completion REPORT published in `reports/` | Human sign-off |

**Not required for exit:** WF-A03 start; 100% reference coverage (Gate 4); ECOMMERCE legal E1–E4; machine validation automation.

### Subprogram WF-R01.1 exit (prerequisite for R01.2)

| ID | Criterion | Status |
|----|-----------|--------|
| B1 | Binding charter **ACCEPTED** | **Not met** |
| B2 | v0→v1 mapping table published | **Met** in design doc |
| B3 | STOP rule in OPERATIONAL-INDEX Core Run | **Not met** |
| B4 | Onboarding cites v1 only | **Not met** |
| B5 | Legacy banner on v0 registries | **Not met** |
| B6 | Zero new v0 IDs post-T_cutover | **Not met** (T_cutover unset) |
| B7 | Curated library v2 plan | **Not met** |
| B8 | Agent card authority path documented | **Not met** |

**WF-R01.1 exit: not satisfied** — design-only.

---

## Required Deliverables

### Before WF-R01 program ACTIVE (charter pass bundle)

| # | Deliverable | Owner | Blocks |
|---|-------------|-------|--------|
| D0 | **This pass** — `wf-r01-program-authority-pass-v1.md` | Done | Authority clarity |
| D1 | Human ACCEPTED **Program Charter** (or accepted program design elevation) | Operator | PROPOSAL → CHARTERED |
| D2 | `roadmap.md` — WF-R01 row + WF-A03 precondition update | Charter pass | Canon registration |
| D3 | `OPERATIONAL-INDEX.md` — Core Run row (Registry Expansion / v0→v1) | Charter pass | Operator visibility |
| D4 | Metrics baseline M1–M10 recorded | R01.X | Gate measurement |

### Before WF-R01.2 start (explicit — task forbids R01.2 now)

| # | Deliverable | Source | Rationale |
|---|-------------|--------|-----------|
| **R1** | WF-R01 status ≥ **CHARTERED** (prefer **ACTIVE** with R01.1 in flight) | This pass G3–G5 | R01.2 expands registry — **forbidden** under PROPOSAL-only authority |
| **R2** | WF-R01.1 binding charter **ACCEPTED** (`wf-r01-1-v0-v1-binding-charter-v1.md`) | R01.1 B1 | Canonical namespace — **hard dependency** in program design |
| **R3** | v0→v1 mapping table **published** in accepted charter | R01.1 B2 | Design exists; needs ACCEPTED artifact |
| **R4** | STOP rule live in OPERATIONAL-INDEX | R01.1 B3 | Prevents mixed IDs during v1.1 work |
| **R5** | T_cutover date recorded | R01.1 cutover policy | B6 audit anchor |
| **R6** | Program design scope reaffirmed: **no new site types** in R01.2 without separate charter | Program design § Registry Expansion | Task constraint alignment |

**Not required before R01.2:** R01.3 partials; R01.4/R01.5 slices; 100% BLOCK-CONTRACT hygiene (R01.6 parallel); WF-A03 Research Pass.

### Artifact path expectations (accepted vs design)

| Artifact | Design (exists) | Accepted (required for execution) |
|----------|-----------------|-----------------------------------|
| Program | `foundry-registry-expansion-program-design-v1.md` | Program charter ACCEPTED + roadmap row |
| WF-R01.1 | `wf-r01-1-v0-v1-binding-charter-design-v1.md` | `wf-r01-1-v0-v1-binding-charter-v1.md` |
| WF-R01.2 | Scope in program design only | **Not designed in separate report** — out of scope this task |

---

## Roadmap Impact

**Recommendations only — no implementation in this task.**

### roadmap.md

| Change | Rationale |
|--------|-----------|
| Add **Factory architecture items** row: **WF-R01** Registry Expansion Program | Align canon with proposed next major direction |
| Set status **CHARTERED** after human sign-off (initially **PROPOSAL** until G3) | Honest status progression |
| Update **WF-A03 deferred marker** Start condition: add «WF-R01 Gate 2+ **recommended** OR explicit operator waiver» | Encode proposed chain without auto-starting A03 |
| Add changelog entry 2026-06-19 | Traceability |
| Cross-link `reports/foundry-registry-expansion-program-design-v1.md` | Single program SoT |

**Proposed row (illustrative):**

| ID | Name | Status | Notes |
|----|------|--------|-------|
| **WF-R01** | Registry Expansion Program | **PROPOSAL** → CHARTERED on sign-off | Program design v1; subprograms R01.1–R01.8; **not** runtime |
| **WF-A03** | Pixel Factory Expansion | **DEFERRED** | Start: WF-A01+A02 complete; **recommended** WF-R01 Gate 2+; Research Pass required |

### OPERATIONAL-INDEX.md

| Change | Rationale |
|--------|-----------|
| Add **Core Run** row: **Registry Expansion (WF-R01)** | Single operator entry — program design § Risks mitigation |
| Sub-links: binding charter (when ACCEPTED), BLOCK-REGISTRY-v1, reference-v1, STOP rule | Avoid governance bloat |
| Add **v0 legacy banner** pointer when R01.1 P2 complete | XD-02 mitigation |
| Optional Wave note: curated-library v2 plan | XD-04 mitigation |

**Proposed Core Run row (illustrative):**

| Concern | Where to start |
|---------|----------------|
| **Registry Expansion / v0→v1 binding (WF-R01)** | Accepted binding charter · v1 = SSOT for new `site_type_code` / `block_id` · **STOP** on mixed IDs · program design `reports/foundry-registry-expansion-program-design-v1.md` |

### Governance references

| Location | Recommendation |
|----------|----------------|
| `projects/mars-website-factory/registries.md` | Charter pass: v1 authority for new work; v0 legacy banner (R01.1 B5) |
| `agents/registry.md` §4.1 | Note WF-R01 program; agent cards cite v1 (R01.1 B8) |
| `website-factory-production-modes-charter-v1.md` | Minor: harmonize `site_type_id` → `site_type_code` in TEMPLATE_ART §4 — **link** to binding charter, not rewrite scope |
| `reports/` index / README if exists | Link program authority pass + program design |

### What **not** to change in charter pass

- WF-A01 / WF-A02 / VL3 charter **scope** — no expansion
- Block Registry v1 **entries** — no R01.2 blocks until subprogram chartered
- Reference workspace `src/` — no R01.3 partials
- WF-A03 deferred **non-goals** list — unchanged

---

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| **False authority** — operators treat design reports as ACTIVE program | **Critical** | This pass; roadmap status PROPOSAL until sign-off |
| **Premature R01.2** — registry expansion without binding | **Critical** | Hard gate: R01.1 ACCEPTED before R01.2 |
| **Informal execution** — reference partials added without program gates | **High** | CHARTERED + M2 metrics in every wave REPORT |
| **WF-A03 early start** — visual layer before registry cliff closed | **Medium** | Roadmap precondition update (recommended) |
| **Governance bloat** — 8 subprograms overwhelm OPERATIONAL-INDEX | **Medium** | Single Core Run row; subprogram detail in program design only |
| **v0 creep** during PROPOSAL phase | **High** | Do not start R01.2+; accelerate R01.1 ACCEPTED |
| **TEMPLATE_ART false completeness** on CATALOG | **Critical** | R01.7 interim LANDING-only — **not yet** in OPERATIONAL-INDEX |
| **Terminology drift** WF-A01 `site_type_id` vs v1 `site_type_code` | **Medium** | R01.1 charter pass cross-link |
| **Operator COMPLETE never signed** | **Low** | Timeboxed phases; E9 completion REPORT |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| **FOUNDRY** as named product/path | **Not found** — Website Factory scope |
| **Formal Program Authority Model** in governance | **Not documented** — model in this pass is **derived** |
| **Human owner** WF-R01 sign-off | **Not fixed** in repo |
| **Calendar date** for program CHARTERED / ACTIVE | **Pending** human decision |
| **Accepted program charter filename/location** | **Not defined** — design suggests elevation of program design or separate charter |
| **WF-R01.2 separate design report** | **Does not exist** — scope only in program design |
| **Whether Knowledge Center mirror is fresh** | **UNKNOWN** (out-of-git) |
| **OCPilot SITE-001** v1 binding | **Not verified** |
| **BZPM W3 blueprint delivery** | **UNKNOWN** |
| **Operator waiver path** for WF-A03 before R01 Gate 2 | **Not chartered** |
| **WF-A04+** naming (Blueprint Machine Layer) | **SAFE UNKNOWN** |

---

## Recommended Next Step

1. **Human review** of this Program Authority Pass — confirm **PROPOSAL** classification and proposed authority model.
2. **Human sign-off** to elevate WF-R01 **PROPOSAL → CHARTERED** (explicit ACCEPTED marker on program design or publish program charter v1).
3. **Charter pass** (separate task): roadmap + OPERATIONAL-INDEX registration per § Roadmap Impact — **no registry content changes**.
4. **WF-R01.1 execution**: publish ACCEPTED `wf-r01-1-v0-v1-binding-charter-v1.md`; complete B3–B8 via charter pass P2–P5.
5. **Only after B1 satisfied:** authorize WF-R01.2 design/charter work — **not** in current task scope.

**STOP AFTER REPORT — NO IMPLEMENTATION — NO DOCUMENT CHANGES (кроме этого артефакта)**

---

*Authority pass artifact: `reports/wf-r01-program-authority-pass-v1.md`*  
*Evidence: foundry-registry-expansion-program-design-v1.md, wf-r01-1-v0-v1-binding-charter-design-v1.md, mars-website-factory roadmap.md, OPERATIONAL-INDEX.md, WF-A01/A02/VL3 charters.*
