# REPORT — WEBSITE FACTORY VALIDATION ARCHITECTURE AUDIT

**Date:** 2026-06-17  
**Scope:** Audit only — **no implementation**, **no architecture design**, **no edits** to existing governance documents.  
**Task:** WF-A02 prerequisite — map current validation state before designing Validation Architecture.  
**Evidence base:** `projects/mars-website-factory/`, `workspaces/website-factory-reference-v1/`, `workspaces/website-factory-operations/`, `agents/`, `governance/`, `reports/` (WF-A01 pass, FP-0002 forensic, architecture alignment).

**Honesty boundary:** Website Factory validation in MARS is **documentation-first, human-operated**. No in-repo validation runtime, orchestration engine, automated visual diff product, or CI enforcement pipeline is evidenced. This audit distinguishes **documented gates** vs **exercised in execution cases** vs **absent**.

---

## Executive Summary

Website Factory обладает **одним из самых плотных governance-пакетов по QA** в репозитории (~294 файла в `projects/mars-website-factory/`, плюс frozen `production-qa/` в reference-v1, плюс Forge overlay checklists). При этом **исполняемая validation-архитектура отсутствует**: FP-0002 доказал, что `npm run build` PASS + agent self-attestation дают **false-green** (15/15 PASS в build log при 1 PASS / 12 PARTIAL / 2 FAIL forensic).

**WF-A01 (Production Modes Contract)** закрыл часть **vocabulary gap**: `PIXEL_PERFECT` | `TEMPLATE_ART`, QA router в документации, трёхуровневая модель **BUILT / VERIFIED / PRODUCTION PASS**. Это **задекларированный контракт**, не enforcement engine.

**Вердикт аудита:**

| Dimension | State |
|-----------|-------|
| **Governance coverage (docs)** | **High** — gates, matrices, laws, failure classes, reporting standard |
| **Executable validation** | **Absent** — no CI gates, no FIG↔HTML diff, no instance resolver product |
| **Human gate discipline** | **Partial** — exercised in FP-0002/FP-0001 cases; inconsistent; bypassable |
| **Mode-specific QA fork** | **Partial** — router documented post–WF-A01; not runtime-enforced |
| **FP-0002 failure classes** | **Mostly documented, rarely gated** — lessons promoted to laws; build still false-green |

**Главный пробел для WF-A02:** между **богатым human QA governance** и **отсутствующими machine-checkable validation layers** (Instance Resolver, Asset Identity Registry, Visual Y Ordering, Render Diff, Text Lock) нет **связующей Validation Architecture** — ordered checklist chain с blocking semantics и evidence model, пригодная к human ops **и** к будущему project-local tooling без mythology drift.

---

## Validation Inventory

Полный перечень validation-related артефактов Website Factory (по категориям). Статус: **Doc** = documented human-operated; **Exec** = exercised in execution case; **Auto** = automated in-repo (none found).

### A. QA entry surfaces and routers

| Artifact | Path | Status | Role |
|----------|------|--------|------|
| Operational QA entry v1 | `projects/mars-website-factory/operational-qa-entry-v1.md` | **Doc** + **Exec** | Single QA surface; Production Mode QA Router (WF-A01) |
| Reference workspace QA flow | `reference-workspace-qa-flow-v1.md` | Doc | ~15 min compact pass |
| RU landing QA preset | `ru-landing-qa-preset-v1.md` | Doc | Mandatory widths for RU commercial |
| Adoption validation flow | `adoption-validation-flow-v1.md` | Doc | Foundation/Forge/survivability compatibility |
| Visual regression workflow | `visual-regression-workflow-v1.md` | Doc | Human screenshot discipline — **not** diff engine |
| Production hardening rules | `production-hardening-rules-v1.md` | Doc | Pre-freeze checks |
| Pilot adoption flow | `pilot-adoption-flow-v1.md` | Doc | Controlled reuse validation |
| Freeze discipline | `freeze-discipline-v1.md` | Doc | Freeze gate semantics |
| QA validation model | `qa-validation-model.md` | Doc | Lanes; Validator Agent **planned** |
| Validation Runtime Model v0 | `validation-runtime-overview-v0.md` + 9 linked docs | Doc | Semantics only — **not** runtime |

### B. Frontend QA chain (2026-06 packs)

| Artifact | Path | Status | Role |
|----------|------|--------|------|
| Frontend QA reporting standard v1 | `frontend-qa-reporting-standard-v1.md` | **Doc** | Layer A–F vocabulary; **BUILT/VERIFIED/PRODUCTION PASS** (Layer F) |
| Frontend Design QA Matrix v1 | `frontend-design-qa-matrix-v1.md` | Doc | DQ-01–DQ-12 domains |
| Pixel fidelity audit rules v1 | `pixel-fidelity-audit-rules-v1.md` | Doc | PF-* human audit |
| Frontend design completeness | `frontend-design-completeness-governance-v1.md` | Doc | Entity comparison (MATCH/PARTIAL/MISSING) |
| Foundation QA governance | `frontend-foundation-qa-governance-v1.md` | Doc | Pre–Home gate rollup |
| Design calibration stage | `frontend-design-calibration-stage-v1.md` | Doc | Token vs standards |
| Shell first start protocol | `frontend-shell-first-start-protocol-v1.md` | Doc | Phase chain + gates |
| Operator visual approval law | `operator-visual-approval-law-v1.md` | Doc | TECHNICAL PASS ≠ OPERATOR APPROVAL |
| Enforcement pack v1 | `website-factory-enforcement-pack-v1.md` | Doc | EG-01–EG-05; ROOT COMPLIANCE |
| Compliance decision model | `frontend-compliance-decision-model-v1.md` | Doc | RAW VIOLATION → gate verdict |
| Failure attribution model | `frontend-failure-attribution-model-v1.md` | Doc | Post-escape investigation |
| Production standards governance | `production-standards-governance-v1.md` | Doc | Draft + Approval gate |
| Design → Frontend Mapping QA | `design-source-to-frontend-mapping-governance-v1.md` | Doc | Pre-shell mapping gate |
| Production modes charter | `website-factory-production-modes-charter-v1.md` | **Doc** (WF-A01) | Mode-specific QA rules + anti-generative-fill |

### C. Composition / extract validation (PIXEL path)

| Artifact | Path | Status | Role |
|----------|------|--------|------|
| Source Discovery v1 | `website-factory-source-discovery-v1.md` | **Doc** + **Exec** (FP-0002) | Phase A0 inventory gate |
| Group decomposition law | `group-decomposition-law-v1.md` | Doc | GROUP-ID register before Layout Spec |
| Layout spec law | `layout-spec-law-v1.md` | **Doc** + **Exec** (FP-0002 header) | Composition gate before HTML |
| Asset identity collision failure class | `failures/asset-identity-collision-v1.md` | Doc | Brand detection chain — **not** engine |
| FP-0002 lessons | `FP-0002-*-lesson-v1.md` (3 files) | Doc | Forensic-derived discipline |
| Visual reconciliation layer | `visual-reconciliation-layer.md` | Doc | Human hierarchy read — **not** CV |

### D. Blueprint / architecture QA (reference-v1 doctrine)

| Artifact | Path | Status | Role |
|----------|------|--------|------|
| Production QA system + gates | `workspaces/website-factory-reference-v1/production-qa/` (9 files) | Doc | GATE_ARCHITECTURE_COMPLETE … GATE_FRONTEND_HANDOFF_APPROVED |
| Page blueprint QA checklist v0 | `page-blueprint-qa-checklist-v0.md` | Doc | 12 categories — Validator-oriented |
| Generation gates v1 | `reference-v1/generation-contracts/GENERATION-GATES-v1.md` | Doc | Upstream of production QA |
| Block registry + site type registry | `reference-v1/registry/`, `block-registry/` | Doc | Compatibility semantics |

### E. Forge overlay QA

| Artifact | Path | Status | Role |
|----------|------|--------|------|
| Forge QA checklist | `agents/mars-forge/qa-checklist.md` | Doc | Extended human checklists (40+ layers) |
| Foundation Lite checklist | `agents/mars-forge/foundation-lite-checklist.md` | Doc | Compact foundations pass |
| Forge operational modes | `agents/mars-forge/forge-operational-modes-v1.md` | Doc | Lite/Standard/Critical — **task risk**, not production mode |
| Frontend Gulp QA checklist | `agents/frontend-gulp-agent/qa-checklist.md` | Doc | Build/a11y/SEO companion |

### F. Cross-program gates

| Artifact | Path | Status | Role |
|----------|------|--------|------|
| P0 Visual Gates v1 | `governance/P0-VISUAL-GATES-v1.md` | Doc | AUTOMATED_PASS vs VISUAL_ACCEPT; HITL hard stop |
| Survivability enforcement | `projects/mars-survivability/contracts/website-factory-enforcement-v1.md` | Doc | Safe production rules |

### G. Reporting and STOP mechanisms

| Mechanism | Where | Type |
|-----------|-------|------|
| **STOP** on undeclared production mode | Charter §5, Source Discovery A0.5, onboarding step 0 | **Doc** — blocking language |
| **STOP** on NOT READ sources | Source Discovery §5 | Doc |
| **STOP** on missing Layout Spec | `layout-spec-law-v1.md` | Doc |
| **STOP** on generative fill (PIXEL) | Charter §7, PF §0.4 | Doc |
| **HITL PENDING = Hard Stop** | P0-02, operator visual approval law | Doc |
| **SAFE UNKNOWN** | Pack-wide; `safe-unknown-boundary.md` | Doc — escalation, not auto-block |
| **ROOT COMPLIANCE FAIL blocks PRODUCTION PASS** | Enforcement pack §6 | Doc |
| **FAIL blocks PRODUCTION PASS** | Frontend QA reporting §2 | Doc |
| **Exception Registry** | Authority order + enforcement pack | Doc — waiver path |

### H. Execution-case validation artifacts (LOC-ZONE)

| Case | Examples | Status |
|------|----------|--------|
| FP-0002 | Design Audit, Mapping QA Record, forensic REPORTS, FIG discovery tests, stress test forensic | **Exec** — ad-hoc scripts + human review |
| FP-0001 Triumph | MOC manifests, `TEMPLATE_ART` mode display | Partial enrollment |
| SITE-001 (OCPilot) | Parallel WFV3 compliance audits | Related — not WF pack native |

### I. Planned / absent agents

| Agent | Registry status | Validation role |
|-------|-----------------|-----------------|
| Validator Agent | **planned** | Structural/policy cross-cut |
| Frontend QA Agent | **planned** | Depth — **not** operational pack |
| Design QA, SEO QA, Conversion QA | **planned** | Cards only |

**Inventory summary:** **~80+ named validation documents**; **0 automated validation products** in-repo; **1 stress-test forensic** proving governance–execution gap.

---

## Validation Layer Map

For each Factory layer: what is checked, implementation status.

### Discovery Validation

**What is checked:**

| Check | Authority | Mechanism |
|-------|-----------|-----------|
| Full intake inventory (SOURCE-NNN) | Source Discovery A0 | Human register |
| Authority classification per source | Source Discovery §3 | Human |
| READ / PARTIALLY READ / NOT READ status | Source Discovery §5 | Human — **NOT READ blocks** Phase A |
| Production mode branch | A0.5 + charter | Human — **undeclared blocks** |
| Structural vs visual source conflicts | Design Audit (Phase A) | Human REPORT |
| Source confidence / ambiguity | `source-confidence-model.md`, `source-interpretation-governance.md` | Doc discipline |

| Status | Assessment |
|--------|------------|
| **Implemented** | Source Discovery A0 as **documented mandatory gate**; exercised in FP-0002 |
| **Partial** | No automated folder crawl; no checksum sync; mode gate **new** (WF-A01) — retroactive on FP-0002 |
| **Absent** | Machine-readable source inventory schema; CI validation of intake completeness |

---

### Blueprint Validation

**What is checked:**

| Check | Authority | Mechanism |
|-------|-----------|-----------|
| Commercial logic, SEO, CTA, trust | `page-blueprint-qa-checklist-v0.md` | Human 12-category walk |
| Block compatibility (`block_id`) | Blueprint checklist §8 + Block Registry | Human |
| Site type alignment | Site Type Registry v1 | Human |
| Architecture completeness | `PRODUCTION-QA-GATES-v1` GATE_ARCHITECTURE_COMPLETE | Human (reference-v1) |
| Page-block validation semantics | `page-block-validation/` (reference-v1) | Doc |
| Semantic QA rules | `semantic-qa-rules-v0.md` | Doc |

| Status | Assessment |
|--------|------------|
| **Implemented** | Blueprint QA checklist + production QA architecture gates **as documentation** |
| **Partial** | Validator Agent **planned** — no operational router; TEMPLATE_ART weights blueprint higher (charter) but no separate enforcement |
| **Absent** | Automated blueprint linter; blocking integration with frontend workspace bootstrap |

---

### Design Validation

**What is checked:**

| Check | Authority | Mechanism |
|-------|-----------|-----------|
| Design Audit (post-A0) | Source Discovery Phase A | Human REPORT |
| Design → Frontend Mapping QA | `design-source-to-frontend-mapping-governance-v1.md` | Human gate — pre-Shell |
| Production Standards Draft + Approval | `production-standards-governance-v1.md` | Human HITL |
| Group Decomposition Gate | `group-decomposition-law-v1.md` | Human GROUP-ID register |
| Layout Spec Gate | `layout-spec-law-v1.md` | Human APPROVED spec before HTML |
| Assembly Spec / order | FP-0002 practice + forensic FAIL-007 | **Partial** — anomaly documented, rule absent |
| Brand Asset Detection chain | `failures/asset-identity-collision-v1.md` | Doc procedure — **not** engine |
| Design calibration | `frontend-design-calibration-stage-v1.md` | Human token verify |
| GATE_DESIGN_COMPLETE | reference-v1 production-qa | Human architectural |

| Status | Assessment |
|--------|------------|
| **Implemented** | Mapping QA, Standards Approval, Group/Layout laws as **canonical human gates** |
| **Partial** | FIG extract quality (flat TEXT); INSTANCE subtree visibility; assembly order policy; brand chain **documented not gated** |
| **Absent** | Component Detection / Structure Extraction **product**; Layout Measurement automation; Visual Y Ordering layer |

---

### Frontend Validation

**What is checked:**

| Check | Authority | Mechanism |
|-------|-----------|-----------|
| `npm run build` | Gulp pipeline | **Auto** — compile only |
| Foundation QA | `frontend-foundation-qa-governance-v1.md` | Human rollup |
| Frontend Design QA Matrix (DQ-*) | `frontend-design-qa-matrix-v1.md` | Human |
| Pixel Fidelity Audit (PF-*) | `pixel-fidelity-audit-rules-v1.md` | Human DevTools + side-by-side |
| Design Completeness Audit | `frontend-design-completeness-governance-v1.md` | Human entity compare |
| Enforcement gates EG-01–EG-05 | `website-factory-enforcement-pack-v1.md` | Human compiled CSS / inline / ROOT |
| Compact operational pass | `operational-qa-entry-v1.md` | Human ~15 min |
| Block-by-block approval | Client `AGENTS.md` pixel-perfect workflow | Human HITL |
| Operator Visual Review | `operator-visual-approval-law-v1.md` | Human — mandatory for visual close |
| P0 Technical vs Visual PASS | `governance/P0-VISUAL-GATES-v1.md` | Human cross-program |
| Forge extended checklists | `agents/mars-forge/qa-checklist.md` | Human — Tier 3 |

| Status | Assessment |
|--------|------------|
| **Implemented** | Extensive **human-operated** gate chain; reporting standard with Layer A–F |
| **Partial** | Build PASS ≠ content fidelity (FP-0002); PF-* optional skip; compact pass ≠ Production PASS; **BUILT/VERIFIED split declared but not wired to build logs** |
| **Absent** | `frontend_qa_agent` runtime; mandatory pre-PASS FIG/text checklist **automation**; Render Diff; Text Lock diff; false-green prevention in pipeline |

---

### Release Validation

**What is checked:**

| Check | Authority | Mechanism |
|-------|-----------|-----------|
| WF v0 S13 delivery stage | `website-factory-workflow-v0.md` | Doc stage |
| Delivery lifecycle semantics | `delivery-lifecycle-v0.md` | Doc |
| Visual regression (pre-release slice) | `visual-regression-workflow-v1.md` | Human screenshots |
| Freeze discipline | `freeze-discipline-v1.md` | Human |
| Production readiness checklist | Forge `production-readiness-checklist.md` | Human |
| GATE_PRODUCTION_QA_PASS | reference-v1 | Human architectural |
| Hosting/deploy | Per-project | **SAFE UNKNOWN** |

| Status | Assessment |
|--------|------------|
| **Implemented** | Release/freeze **documentation** and human checklists |
| **Partial** | No unified release gate rollup across LOC-ZONE + workspace; deploy pipeline unknown per project |
| **Absent** | Automated release validation; CI deploy gates; staging URL verification product |

---

### Production Validation

**What is checked:**

| Check | Authority | Mechanism |
|-------|-----------|-----------|
| PRODUCTION PASS / FINAL VERDICT | `frontend-qa-reporting-standard-v1.md` §6 | Human REPORT |
| BUILT → VERIFIED → PRODUCTION PASS | Charter §9 + reporting §1.1 (Layer F) | **Doc vocabulary** (WF-A01) |
| Production mode acceptance rules | Charter §3.6 / §4.6 | Doc |
| ROOT COMPLIANCE | Enforcement pack | Human |
| Production QA contract (FULL_SITE) | `PRODUCTION-QA-CONTRACT-v1.md` | Human |
| FP-0002 forensic (post-hoc) | `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md` | **Exec** — manual stress test |

| Status | Assessment |
|--------|------------|
| **Implemented** | Production PASS semantics and mode acceptance rules **documented** |
| **Partial** | Vocabulary reformed (WF-A01) but **build tooling still emits legacy PASS**; VERIFIED requires evidence operators may skip |
| **Absent** | Production validation runtime; automated PRODUCTION PASS engine; ROC enrollment automation for FP-* |

---

## FP-0002 Findings Coverage

Mapping FP-0002 forensic failures to current validation state.

### Instance Resolver

| Question | Answer |
|----------|--------|
| **Validation exists?** | **Partial** |
| **What exists** | `group-decomposition-law-v1.md` (GROUP-IDs); Discovery names INSTANCE types; FP-0002 `FIG-AUTO-GROUP-REGISTER-TEST` artifacts; charter SAFE UNKNOWN: «INSTANCE subtree invisible → STOP section build» |
| **What is absent** | Operational **Instance Resolver** walking INSTANCE subtrees before generation; gate blocking build when instance count ≠ HTML card count; FAIL-006, FAIL-008, FAIL-014 root cause **ungated** |
| **Verdict** | **Partial** — law + lessons; **no blocking validation** |

### Asset Identity

| Question | Answer |
|----------|--------|
| **Validation exists?** | **Partial** |
| **What exists** | `failures/asset-identity-collision-v1.md` + Brand Asset Detection chain (§7); forbidden first-image-as-logo; PF-07; DQ-08; registry token `ASSET_IDENTITY_COLLISION` |
| **What is absent** | Automated hash dedup registry; frame-export pollution fix (FAIL-004); asset manifest `section → nodeId → src`; pre-wire **blocking** brand gate |
| **Verdict** | **Partial** — failure class + procedure; **FP-0002 collision occurred despite docs** |

### Visual Ordering

| Question | Answer |
|----------|--------|
| **Validation exists?** | **Absent** (as validation layer) |
| **What exists** | FAIL-007 documented; Discovery flagged SECTION-10 `y=2389` anomaly; charter requires ASSEMBLY DECISION record |
| **What is absent** | Assembly rule: `bounds.y` primary, layer index fallback; automated order diff; gate blocking silent layer-index default |
| **Verdict** | **Absent** — anomaly **documented only** |

### Frontend QA

| Question | Answer |
|----------|--------|
| **What really exists?** | **Partial** — rich human governance |
| **Evidence** | 12+ frontend QA docs; enforcement pack; compliance + attribution models; operator visual law |
| **Gap** | False-green demonstrated: build log 15/15 PASS vs forensic 1/12/2; agent self-attestation; no mandatory pre-PASS content checklist in pipeline |
| **WF-A01 impact** | Layer F BUILT/VERIFIED/PRODUCTION PASS **documented** — **not** enforced in `full-build-run.log` pattern |
| **Verdict** | **Partial** — governance **exists**; **validation discipline failed** under stress |

### Render Validation

| Question | Answer |
|----------|--------|
| **What really exists?** | **Partial** (human only) |
| **Human** | Visual regression workflow; visual reconciliation; PF-* side-by-side; operator visual approval |
| **Absent** | Automated `fig_extract ↔ dist` comparison; screenshot diff (Percy/Chromatic class); CI render gate; text lock diff |
| **Charter** | PIXEL_PERFECT: Render Diff **required for VERIFIED** — manual or project-scripted; tooling **SAFE UNKNOWN** |
| **Verdict** | **Absent** (automation); **Partial** (human methodology) |

---

## Acceptance Gates Assessment

### BUILT / VERIFIED / PRODUCTION PASS separation

| Aspect | State |
|--------|-------|
| **Declared?** | **Yes** — WF-A01 Pass 01 |
| **Where** | `frontend-qa-reporting-standard-v1.md` §1.1 Layer F; `website-factory-production-modes-charter-v1.md` §9; `operational-qa-entry-v1.md` router |
| **Enforced in build pipeline?** | **No** — FP-0002 `full-build-run.log` still uses unconditional section PASS |
| **Enforced in REPORT law?** | **Yes (documentation)** — migration table maps legacy build PASS → BUILT |
| **Operator discipline?** | **Partial** — depends on REPORT compliance |

**Assessment:** Separation is **задекларировано**, **не внедрено** в executable tooling. Operators **must** use Layer F in REPORTs; nothing prevents calling BUILT «production-ready» without VERIFIED unless peer review catches it.

### Gate verdict layers (A–E) vs lifecycle (F)

| Layer | Declared | Operational |
|-------|----------|-------------|
| A — Gate verdict (PASS/FAIL/…) | Yes | Human REPORT |
| B — Sub-check | Yes | Human |
| C — Entity status (completeness) | Yes | Human |
| D — SAFE UNKNOWN signals | Yes | Human escalation |
| E — Operator visual ACCEPT | Yes | Human mandatory |
| F — BUILT/VERIFIED/PRODUCTION PASS | Yes (WF-A01) | **Doc only** — no build integration |

### Orthogonal acceptance dimensions

| Dimension | Relationship to PRODUCTION PASS |
|-----------|--------------------------------|
| Forge mode (Lite/Standard/Critical) | Orthogonal — task risk |
| Production mode (PIXEL/TEMPLATE) | Defines VERIFIED criteria |
| ROOT COMPLIANCE | Blocks PRODUCTION PASS if FAIL |
| P0 VISUAL_ACCEPT | Cross-program — blocks wave chaining |

---

## QA Router Assessment

### PIXEL_PERFECT vs TEMPLATE_ART — real differences?

| Dimension | PIXEL_PERFECT | TEMPLATE_ART | Enforced? |
|-----------|---------------|--------------|-----------|
| PF-* audit | **Mandatory** | **N/A** (waived) | **Doc** |
| Render Diff | **Required for VERIFIED** | **Waived** | **Doc** |
| Mapping QA | **Full** FIG extract | **Reduced** token/brand | **Doc** |
| Group Decomposition / Layout Spec | **Mandatory** | Optional (wireframe SSOT) | **Doc** |
| Blueprint QA weight | Secondary | **Primary** | **Doc** |
| Content contract | FIG-led + supplement | **Mandatory** before build | **Doc** |
| Generative fill | **Forbidden** | Allowed in bounds | **Doc** — FP-0002 proved bypass |
| Block provenance | Mapping record | `block_id` audit | **Doc** |
| VERIFIED means | Diff + PF-* + side-by-side | Semantic matrix + provenance | **Doc** |

**Assessment:** **Real differences exist in charter and QA router** — not merely labels. They are **documentation contracts** routed by human reading passport `production_mode`. **No runtime router**, **no automated checklist engine**, **no CI fork**. Undeclared mode → **STOP** language exists but is **not machine-enforced**.

**Evidence of router adoption:** FP-0002 passport retroactively `PIXEL_PERFECT`; FP-0001 MOC shows `TEMPLATE_ART`. Operators **can** route correctly; FP-0002 stress test ran **before** full WF-A01 enforcement in build path.

---

## Validation Coverage Matrix

| Layer | Validation Coverage | Risk | Priority (WF-A02) |
|-------|---------------------|------|-------------------|
| **Intake / mode gate** | Partial — WF-A01 blocking doc; no runtime | High — wrong path / undeclared mode | **A** |
| **Source Discovery** | Partial — human A0; exercised FP-0002 | Medium — late source discovery | **B** |
| **Blueprint / architecture** | Partial — checklists; no Validator agent | Medium — IA drift before frontend | **B** |
| **Design extract / mapping** | Partial — gates exist; extract immature | **Critical** — generative fill, false completeness | **A** |
| **Composition (Group/Layout/Assembly)** | Partial — laws; assembly order absent | High — FAIL-007 class | **A** |
| **Instance / component resolution** | Absent as gate | **Critical** — FAIL-006/008/014 | **A** |
| **Asset identity** | Partial — failure class only | **Critical** — brand collision | **A** |
| **Build (compile)** | Implemented — gulp | Low for compile; **High** if confused with PASS | **A** (vocabulary wire) |
| **Frontend human QA** | Partial — dense docs; false-green | **Critical** | **A** |
| **Enforcement (compiled CSS)** | Partial — EG gates human | Medium — M2-class escape | **B** |
| **Pixel fidelity (PF-*)** | Partial — human audit | High in PIXEL mode | **B** |
| **Render / text diff** | Absent (auto); Partial (human) | **Critical** — content drift undetected | **A** |
| **Visual ordering** | Absent | High — silent wrong order | **A** |
| **Operator visual accept** | Implemented (doc) | Medium — skipped under pressure | **B** |
| **Release / freeze** | Partial | Medium | **C** |
| **Production PASS rollup** | Partial — Layer F new | High — false production claims | **A** |

---

## Reusable Components

Механизмы, **уже существующие** и пригодные для переиспользования в WF-A02 **без** mythology drift:

1. **Operational QA entry** — single router surface; extend with validation layer map pointer.
2. **Frontend QA reporting standard** — Layer A–F vocabulary; Layer F lifecycle (post–WF-A01).
3. **Production modes charter** — mode-specific VERIFIED definition; anti-generative-fill policy.
4. **Source Discovery A0** — intake gate pattern (inventory + READ status + STOP).
5. **Design → Frontend Mapping QA** — pre-code gate template.
6. **Group Decomposition + Layout Spec laws** — composition gate chain pattern.
7. **Enforcement pack EG-01–EG-05 + ROOT COMPLIANCE** — compiled-output validation pattern.
8. **Compliance decision model + failure attribution model** — verdict routing + post-escape investigation.
9. **Pixel fidelity audit rules + Design QA Matrix** — human audit domain catalog.
10. **Operator visual approval law + P0 visual gates** — TECHNICAL vs VISUAL separation.
11. **Factory failure classes** (`ASSET_IDENTITY_COLLISION`, group aggregation) — taxonomy for validation findings.
12. **Validation Runtime Model v0** — semantic vocabulary (evidence, waiver, escalation) — **not** code.
13. **reference-v1 production-qa gates** — upstream architectural gate catalog.
14. **FP-0002 forensic + lessons** — empirical failure register and recommended upgrades (#1–#8).
15. **Visual regression workflow** — human baseline discipline (extend toward diff charter).
16. **Forge Foundation Lite + compact pass** — proportional depth pattern.
17. **LOC-ZONE passport fields** — `production_mode`, `mode_history[]` as validation context SoT.

---

## Missing Components

Требуют **проектирования с нуля** (или project-local tooling charter) в WF-A02:

1. **Validation Architecture overview doc** — ordered layer chain linking existing gates + gaps (WF-A02 deliverable target).
2. **Instance Resolver validation layer** — gate + evidence model before INSTANCE-heavy sections.
3. **Asset Identity Registry / manifest validation** — `section → nodeId → hash → src` binding gate.
4. **Visual Y Ordering / Assembly Decision validation** — bounds.y policy + conflict record requirement.
5. **Text Lock validation** — anti-paraphrase diff (FIG extract ↔ HTML); `section-NN.lock.json` SSOT pattern.
6. **Render Diff validation layer** — FIG↔dist charter (manual minimum + optional scripted path).
7. **False-green prevention** — build log vocabulary wire (BUILT vs VERIFIED); mandatory pre-report checklist.
8. **Mode-aware validation matrix** — single crosswalk: which gates apply per `production_mode` (charter exists scattered).
9. **Validation evidence schema** — machine-readable REPORT blocks (optional — human-first).
10. **frontend_qa_agent operational_doc_pack** — mode-specific routable checklists (planned card → pack).
11. **Automated validation runtime** — explicitly **out of WF-A02** unless separately chartered (WF-A03 deferred layers).
12. **CI / visual diff SaaS integration** — project-scoped only; not Factory global product.

---

## Risks

| Risk | Severity | Evidence |
|------|----------|----------|
| **False-green production** | **Critical** | FP-0002: build PASS vs forensic FAIL; Layer F not in build tooling |
| **Governance without enforcement** | **Critical** | Dense pack; stress test bypassed gates |
| **PIXEL path without extract validation** | **Critical** | Generative fill despite charter (FAIL-002/003) |
| **Asset identity collision recurrence** | **Critical** | Documented class; no pre-wire gate |
| **Mode router documentation-only** | **High** | WF-A01 complete; operators may ignore step 0 |
| **Doctrine vs operations drift** | **Medium** | reference-v1 frozen vs 2026-06 enforcement packs |
| **Governance fatigue** | **Medium** | 80+ validation docs; Tier 3 skipped until incident |
| **Context truncation at scale** | **High** | FP-0002 memory analysis — 15 sections already HIGH risk |
| **Planned agent mythology** | **Medium** | Validator/Frontend QA cards imply existence |
| **WF-A02 scope creep into WF-A03** | **High** | Vision/render automation deferred — must stay boundary-clear |

---

## SAFE UNKNOWN

| Item | Unknown | What would verify |
|------|---------|-------------------|
| Full AI Website Factory Research text in repo | External summary only | Canonical copy in repo |
| Whether operators adopt Layer F in all REPORTs post–WF-A01 | Not measured | Audit sample of FP-* REPORTs after Pass 01 |
| Project-local FIG diff scripts | Recommended by FP-0002; not standardized | WF-A02 tooling template + pilot |
| `section-NN.lock.json` adoption | Recommended; not Factory-standard artifact yet | First PIXEL project using lock files |
| OCPilot SITE-001 ↔ WF production mode crosswalk | Parallel audits exist | Dedicated crosswalk doc |
| Hybrid `page_mode_map` validation | Design only | Pilot on mixed-scope project |
| reference-v1 production-qa gates vs mars-website-factory pack alignment | Two planes | Consolidation map update |
| Automated visual diff tooling (Percy/Chromatic/Playwright) | Per-project | Explicit project CI charter |
| FP-0002 ROC enrollment | Deferred | LOC-ZONE catalog update |
| Build log migration to BUILT vocabulary | Not started | Workspace script change + WF-A02 wire spec |

---

## Recommended Scope For WF-A02

**Goal:** Design **Validation Architecture** — connect existing human gates, FP-0002 gaps, and production mode router into **ordered, blocking, evidence-backed** validation chain. **Not** WF-A03 automation product.

### Priority A — mandatory

1. **Validation Architecture charter** — single doc: layer order, blocking semantics, evidence types, mode fork crosswalk.
2. **False-green closure spec** — wire BUILT/VERIFIED/PRODUCTION PASS to build/report tooling expectations (human-enforced minimum).
3. **PIXEL_PERFECT validation layer checklist** — map Instance Resolver, Asset Identity, Visual Ordering, Text Lock, Render Diff (manual floor) to gates.
4. **Mode validation matrix** — one table: gate × `PIXEL_PERFECT` × `TEMPLATE_ART` × STOP conditions.
5. **Pre-PRODUCTION-PASS mandatory evidence list** — per mode; closes FAIL-001/018.
6. **Anti-generative-fill validation gate** — PIXEL: missing extract → UNKNOWN/STOP; not paraphrase.
7. **Asset Identity validation gate spec** — brand chain before logo wire; hash dedup rules.

### Priority B — desirable

1. **TEMPLATE_ART validation layer checklist** — blueprint + content + provenance emphasis.
2. **Assembly Decision validation** — bounds.y vs layer index policy + record shape.
3. **`section-NN.lock.json` SSOT spec** — machine-readable per-section contract (human-generated).
4. **Validation evidence model v1** — extend Validation Runtime v0 with WF-specific evidence classes.
5. **frontend_qa_agent operational_doc_pack** — mode-aware routable checklists (still human-operated).
6. **FP-0002 findings → validation token registry** — link FAIL-* to expected gate + attribution.
7. **Staged build validation** — max 2–3 sections/run gate for context survivability.

### Priority C — defer (WF-A03 or project-local)

1. Automated vision / CV layer.
2. Pixel QA Runtime / Screenshot Engine / Agent Runtime.
3. Factory-wide CI visual diff SaaS.
4. Validation orchestration engine / LangGraph.
5. Validator Agent **runtime** implementation.
6. ROC enrollment automation.

---

## Appendix — Key evidence documents

| Document | Role in this audit |
|----------|-------------------|
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Navigation SoT |
| `website-factory-production-modes-charter-v1.md` | Mode QA + lifecycle |
| `operational-qa-entry-v1.md` | QA router |
| `frontend-qa-reporting-standard-v1.md` | Layer A–F |
| `website-factory-source-discovery-v1.md` | Discovery gate |
| `design-source-to-frontend-mapping-governance-v1.md` | Mapping QA |
| `group-decomposition-law-v1.md` / `layout-spec-law-v1.md` | Composition gates |
| `pixel-fidelity-audit-rules-v1.md` / `frontend-design-qa-matrix-v1.md` | Frontend QA |
| `website-factory-enforcement-pack-v1.md` | Compiled output gates |
| `failures/asset-identity-collision-v1.md` | Asset failure class |
| `validation-runtime-overview-v0.md` | Validation semantics |
| `workspaces/website-factory-reference-v1/production-qa/` | Architectural QA |
| `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md` | Empirical gap proof |
| `reports/website-factory-production-modes-implementation-pass-01.md` | WF-A01 state |
| `reports/website-factory-architecture-alignment-v1.md` | Prior gap analysis |

---

**STOP AFTER REPORT** — No implementation. No new architecture beyond this audit map. No edits to existing governance documents.

*End of audit — WF-A02 prerequisite complete.*
