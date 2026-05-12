# MARS Website Factory — Reference Run Sequence v0

**Status:** **documentation only** — **human-driven** reference sequence (**R01–R15**). **Not** an automated pipeline.

**Version:** v0.

**Related:** [first-operational-runbook-v0.md](first-operational-runbook-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [workflow-map.md](workflow-map.md), [reporting-standard-v0.md](reporting-standard-v0.md), [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md).

**Legend (columns below):** each row is one **reference run step** aligned to a workflow v0 `stage_id`.

---

## R01 — Intake

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S01_INTAKE` |
| **Owner** | PM / engagement lead (human); Project Intake Agent **planned** per [agent-map.md](agent-map.md) — **not** claimed implemented. |
| **Inputs** | Client brief, stakeholder notes, constraints, compliance flags, prior exports (**optional**). |
| **Outputs** | Intake summary; scope draft (`scope_in` / `scope_out`); open questions list. |
| **Required artifacts** | Intake narrative; risk / sensitivity flags. |
| **QA** | Completeness: goals, audience, constraints, approval chain identified ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) S01). |
| **HITL** | **G1** — PM/lead confirms accuracy of intake and scope boundaries. |
| **Freeze behavior** | Intake is **not** a hard freeze of downstream semantics; it **anchors** scope narrative for checkpoints **C01**. |
| **Invalidation triggers** | Material change to goals, markets, or compliance posture → treat as **scope revision**; downstream steps **must not** proceed without acknowledgment ([dependency-invalidation-v0.md](dependency-invalidation-v0.md)). |
| **Reporting expectation** | Stage REPORT ([reporting-standard-v0.md](reporting-standard-v0.md) §4.1): created/updated files (if any), **SAFE UNKNOWN**, git status, runtime exclusions. |

---

## R02 — Classification

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S02_SITE_TYPE` |
| **Owner** | SEO / strategy lead + PM; Site Type Classifier Agent **planned**. |
| **Inputs** | Approved intake (R01); taxonomy notes; optional competitive set. |
| **Outputs** | `site_type_id` + rationale; registry row references; deltas vs defaults. |
| **Required artifacts** | Classification record citing [site-type-registry-v0.md](site-type-registry-v0.md). |
| **QA** | Consistency: **site_type_id** vs business model; no contradictions. |
| **HITL** | **G1** extension — lead confirms **site_type_id** when ambiguous or multi-site. |
| **Freeze behavior** | Classification is **soft-locked** for planning until **C02** (Strategy locked) per checkpoints doc. |
| **Invalidation triggers** | Registry mismatch, wrong site type, or new product line → reclassify; may ripple to strategy/IA/blueprint. |
| **Reporting expectation** | Stage REPORT + explicit registry citations; **SAFE UNKNOWN** if no row fits (park or propose registry change). |

---

## R03 — Strategy

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S03_STRATEGY` |
| **Owner** | Strategy operator + SEO operator ([operator-lane-model-v0.md](operator-lane-model-v0.md)); Marketing / SEO agents **planned**. |
| **Inputs** | Intake; **site_type_id**; brand guidelines (**optional**). |
| **Outputs** | Strategy memo; SEO hypothesis doc; CTA / conversion narrative; risks list. |
| **Required artifacts** | Strategy + SEO intent artifacts per [seo-intent-model-v0.md](seo-intent-model-v0.md), [conversion-intent-model-v0.md](conversion-intent-model-v0.md). |
| **QA** | Internal consistency: messaging vs audience vs site type; no orphan CTAs ([cta-semantics-v0.md](cta-semantics-v0.md)). |
| **HITL** | **G2** — marketing lead approves strategy + SEO hypotheses. |
| **Freeze behavior** | Post-**C02**, strategy baseline is **locked for IA** unless reopened via revision semantics. |
| **Invalidation triggers** | Conflicting SEO vs commercial goals → **NEED HUMAN APPROVAL** / **STRUCTURE CHANGE**; IA blocked until resolved. |
| **Reporting expectation** | Stage REPORT; semantic / artifact changes enumerated; HITL flags if escalation. |

---

## R04 — IA

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S04_IA` |
| **Owner** | UX operator + PM; Information Architecture Agent **planned**. |
| **Inputs** | Approved strategy; **site_type_id**; legacy URL map (**optional**). |
| **Outputs** | Sitemap; template list; URL/content requirements; navigation spec. |
| **Required artifacts** | IA pack consumable by blueprint stage. |
| **QA** | Reachability; critical journeys; no dead-end paths for declared CTAs. |
| **HITL** | **G3** (partial) — PM + tech lead on scope/size; major IA shifts may re-trigger **G2**. |
| **Freeze behavior** | **C03** — IA locked for blueprint batching. |
| **Invalidation triggers** | CTA flow impossible in IA → return to R03/R04; unknown CMS/stack → **SAFE UNKNOWN** documented. |
| **Reporting expectation** | Stage REPORT + navigation / URL evidence; blockers for blueprint called out. |

---

## R05 — Blueprint

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S05_BLUEPRINT` |
| **Owner** | UX operator (structure) + strategy/SEO alignment; Page Blueprint / UX agents **planned**. |
| **Inputs** | IA pack; strategy/SEO; **site_type_id**; [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md); [block-registry-v0.md](block-registry-v0.md). |
| **Outputs** | Blueprint set per URL/template; cross-page link graph notes. |
| **Required artifacts** | Blueprints meeting contract fields; valid `block_id` rows. |
| **QA** | Contract completeness; registry-valid blocks; CTA targets resolvable in IA. |
| **HITL** | **G3** — PM + tech lead approve blueprint batch before formal blueprint QA handoff. |
| **Freeze behavior** | Blueprint batch approved toward **C04**; immutable regions per [artifact-state-model-v0.md](artifact-state-model-v0.md). |
| **Invalidation triggers** | Registry mismatch, block drop, or IA change → blueprint revision; downstream design/frontend **stale** until rerun. |
| **Reporting expectation** | Stage REPORT + **Artifact changes** (`artifact_id` or contract anchors per [artifact-types-v0.md](artifact-types-v0.md)). |

---

## R06 — Blueprint QA

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S06_BLUEPRINT_QA` |
| **Owner** | QA operator (SEO + conversion lanes); Validator **planned** / depth **TBD**. |
| **Inputs** | Blueprint set; IA; strategy/SEO; [page-blueprint-qa-checklist-v0.md](page-blueprint-qa-checklist-v0.md). |
| **Outputs** | QA report; defect list; pass / fail / conditional recommendation ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)). |
| **Required artifacts** | QA result payload or equivalent structured narrative. |
| **QA** | Checklist categories satisfied or **explicit waiver** with HITL ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |
| **HITL** | Fail or high-risk → **NEED HUMAN APPROVAL** to waive or return to **R05**. |
| **Freeze behavior** | **Pass** (or approved waiver) required before **R07**; freezes **blueprint-approved baseline** for design handoff. |
| **Invalidation triggers** | Conditional pass with unresolved blockers → **do not** advance; silent waiver **forbidden**. |
| **Reporting expectation** | **QA REPORT** per [reporting-standard-v0.md](reporting-standard-v0.md) §4.3 (lane, categories, findings, severity, HITL flags). |

---

## R07 — Design Handoff

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S07_DESIGN_HANDOFF` |
| **Owner** | Design operator (lead); AI Designer Agent **planned** for pack assembly only. |
| **Inputs** | QA-passed blueprints; brand/tokens (**if** any); [design-handoff-contract-v0.md](design-handoff-contract-v0.md). |
| **Outputs** | Design handoff pack per page/template; open design questions. |
| **Required artifacts** | Handoff fields traceable to blueprint sections/blocks. |
| **QA** | Handoff completeness vs blueprint; unsupported visuals flagged (**SAFE UNKNOWN** if tooling TBD). |
| **HITL** | Design lead confirms pack before **R08**. |
| **Freeze behavior** | Handoff does **not** replace blueprint freeze; adds **design-input** baseline. |
| **Invalidation triggers** | Blueprint revision after handoff → handoff pack **stale**; must regenerate or amend with REPORT trail. |
| **Reporting expectation** | Stage REPORT + transfer notes ([artifact-transfer-prompt-rules-v0.md](artifact-transfer-prompt-rules-v0.md)). |

---

## R08 — Design

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S08_DESIGN_PRODUCTION` |
| **Owner** | Design operator; wireframe / design agents **planned**. |
| **Inputs** | Design handoff pack; brand; references. |
| **Outputs** | Wireframes; high-fidelity designs or spec exports (**format explicit per project**). |
| **Required artifacts** | Design artifacts per [design-layer-model.md](design-layer-model.md); tool-agnostic v0. |
| **QA** | Internal design review checklist (feeds **R09**). |
| **HITL** | **G4** / **G5** per [workflow-map.md](workflow-map.md) (UX/client; design lead/client). |
| **Freeze behavior** | No **frontend** baseline until **R09** closure freezes design for handoff. |
| **Invalidation triggers** | Inconsistency across templates; compliance/security issue → stop line ([website-factory-workflow-v0.md](website-factory-workflow-v0.md) S08). |
| **Reporting expectation** | Stage REPORT; asset paths / exports listed; **SAFE UNKNOWN** for Figma/export automation (**none** claimed). |

---

## R09 — Design QA

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S09_DESIGN_QA` |
| **Owner** | QA operator (design lane); Design QA Agent **planned**. |
| **Inputs** | Design outputs; design handoff; blueprints. |
| **Outputs** | Design QA report; bounded change requests. |
| **Required artifacts** | QA findings with evidence references. |
| **QA** | Fidelity vs approved blueprint + handoff; brand/a11y **intent** checks. |
| **HITL** | **G5** closure — design lead / client approves **frozen** design for frontend. |
| **Freeze behavior** | Approved design baseline → **C05**; unlocks **R10**. |
| **Invalidation triggers** | Ambiguous “approved” vs iterating → **NEED HUMAN APPROVAL** before freeze. |
| **Reporting expectation** | **QA REPORT** §4.3 + freeze recommendation; HITL flags. |

---

## R10 — Frontend Handoff

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S10_FRONTEND_HANDOFF` |
| **Owner** | Frontend operator + tech lead; Gulp Frontend Agent naming as **legacy-bridge** ([agents/registry.md](../../agents/registry.md)). |
| **Inputs** | Frozen design; blueprints; [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md); build conventions (**if** any). |
| **Outputs** | Frontend handoff spec; asset list; responsive notes. |
| **Required artifacts** | Spec fields mapping blocks/sections to implementation anchors. |
| **QA** | Completeness; unsupported component flagged. |
| **HITL** | Tech lead approves handoff before **R11**. |
| **Freeze behavior** | Couples to frozen design; handoff revision follows **revision-semantics-v0.md**. |
| **Invalidation triggers** | Unsupported stack request → **STRUCTURE CHANGE** / **UNKNOWN** — explicit human decision. |
| **Reporting expectation** | Stage REPORT + **SAFE UNKNOWN** for CI/build if unknown. |

---

## R11 — Frontend Production

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S11_FRONTEND_PRODUCTION` |
| **Owner** | Frontend operator (human-implemented Phase 1 default). |
| **Inputs** | Frontend handoff; design exports; copy deck. |
| **Outputs** | Source files (`src/...`); build instructions; PR/change bundle per project norms. |
| **Required artifacts** | Static implementation per [frontend-production-model.md](frontend-production-model.md), [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md). |
| **QA** | Local build outcome **if** run — no false CI claims ([safe-unknown-boundary.md](safe-unknown-boundary.md)). |
| **HITL** | **G6** — tech + design sign-off on alignment to frozen design. |
| **Freeze behavior** | **C06** candidate — frontend freeze for QA/validation entry (**project policy**). |
| **Invalidation triggers** | Design freeze break or blueprint semantic change → frontend rework; delivery candidate invalidated ([artifact-routing-rules-v0.md](artifact-routing-rules-v0.md)). |
| **Reporting expectation** | **Frontend implementation REPORT** §4.2 — verification results honest; no `dist/` hand edits. |

---

## R12 — Frontend QA

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S12_FRONTEND_QA` |
| **Owner** | QA operator (frontend lane); Frontend QA / Validator **planned**. |
| **Inputs** | Built pages; handoff; QA checklists ([qa-validation-model.md](qa-validation-model.md)). |
| **Outputs** | Frontend QA report; defect backlog. |
| **Required artifacts** | Severity-tagged findings. |
| **QA** | Blocker list empty or **HITL-waived** ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |
| **HITL** | Blocker waivers → **NEED HUMAN APPROVAL** + **SECURITY RISK** if applicable. |
| **Freeze behavior** | Fail cycles return to **R11** until pass or approved exception path. |
| **Invalidation triggers** | Frontend QA fail may **invalidate** delivery candidate per bus semantics (**documentation rule**, not an engine). |
| **Reporting expectation** | **QA REPORT** §4.3; recommendation pass/fail/conditional. |

---

## R13 — Final Validation

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S13_FINAL_VALIDATION` |
| **Owner** | QA operator + Validator observer role; cross-lane evidence assembly. |
| **Inputs** | All prior **approved** artifacts; deployment checklist (**if** any). |
| **Outputs** | Final validation report; go / no-go recommendation. |
| **Required artifacts** | Cross-lane evidence set per [validation-evidence-model-v0.md](validation-evidence-model-v0.md). |
| **QA** | End-to-end consistency; legal pages when required; registry alignment. |
| **HITL** | **G7** prep — ops/client inputs on go/no-go. |
| **Freeze behavior** | Does not relax prior freezes; aggregates verdicts. |
| **Invalidation triggers** | Late registry mismatch → **park**; may require targeted fixes **R05–R12** with **STRUCTURE CHANGE** if scope shifts. |
| **Reporting expectation** | **Validation REPORT** §4.5 ([reporting-standard-v0.md](reporting-standard-v0.md)); Validator status honest (**planned** / not invoked / out of scope). |

---

## R14 — HITL Approval

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S14_HITL_APPROVAL` |
| **Owner** | HITL reviewer(s) per policy; **no** autonomous agent. |
| **Inputs** | Final validation report; risk summary; rollback notes. |
| **Outputs** | Signed approval record (**format TBD** per workflow v0); release tag **intent**. |
| **Required artifacts** | Audit trail: prior **G*** satisfied or waived with evidence. |
| **QA** | N/A as automated gate — this **is** governance QA of the chain. |
| **HITL** | **Mandatory** — stage is HITL. |
| **Freeze behavior** | Authorizes delivery packaging only after **C07** alignment. |
| **Invalidation triggers** | Missing approver role → **UNKNOWN**; **do not deliver**. |
| **Reporting expectation** | HITL decision recorded in governance channel + summary in delivery REPORT; **no** silent approval ([reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md)). |

---

## R15 — Delivery Package

| Dimension | Content |
|-----------|---------|
| **Maps to** | `WF_V0_S15_DELIVERY` |
| **Owner** | Ops / PM; human packaging — **no** dedicated delivery agent in v0. |
| **Inputs** | Approved artifacts; build output; runbooks. |
| **Outputs** | Delivery package per [reference-delivery-package-v0.md](reference-delivery-package-v0.md); handoff narrative. |
| **Required artifacts** | Manifest/checksums if policy requires; **no** false “live” claim. |
| **QA** | Smoke on **target** environment **if** known; otherwise **SAFE UNKNOWN**. |
| **HITL** | **G7** when **public** deploy. |
| **Freeze behavior** | Post-delivery revision follows [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md) — **human** process. |
| **Invalidation triggers** | Hosting unknown → document **SAFE UNKNOWN**; rollback is **manual** play ([reference-run-failure-recovery-v0.md](reference-run-failure-recovery-v0.md)). |
| **Reporting expectation** | **Delivery REPORT** (see [reference-run-reporting-v0.md](reference-run-reporting-v0.md)); includes runtime exclusions and push status per [reporting-standard-v0.md](reporting-standard-v0.md). |

---

*End of Reference Run Sequence v0.*
