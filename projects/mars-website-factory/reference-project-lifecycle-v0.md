# MARS Website Factory — Reference Project Lifecycle v0

**Status:** **documentation only** — **project lifecycle semantics** aligned with factory stages; **not** a state machine implementation, scheduler, or persisted workflow engine.

**Version:** v0.

**Related:** [reference-project-model-v0.md](reference-project-model-v0.md), [stage-state-model-v0.md](stage-state-model-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md).

---

## 1. Lifecycle states (v0)

Conceptual **project-level** states for runbooks and reporting:

```text
created → intake → classified → strategy → blueprint → design → frontend → qa → approved → delivery → released → revision → archived
```

**IA alignment:** **Information architecture** work is **required** before blueprint freeze per [website-factory-workflow-v0.md](website-factory-workflow-v0.md). In this v0 **shorthand**, IA completion is an **entry condition** to **blueprint** (no separate `ia` state token) to keep the lifecycle list stable with charter text; if a project needs an explicit **`ia`** state for tooling, treat it as a **documentation extension** consistent with [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md).

---

## 2. Per-state semantics

For each state: **Entry** / **Exit** / **Blocking** / **Invalidation** / **QA** / **HITL**.

### 2.1 `created`

| Dimension | Content |
|-----------|---------|
| **Entry** | Project charter registered (`project_id` assigned in runbook or registry when adopted). |
| **Exit** | Intake kickoff scheduled; initial artifact folder / branch strategy named (**SAFE UNKNOWN** tooling). |
| **Blocking** | Missing accountable owner for HITL chain. |
| **Invalidation** | N/A (no downstream artifacts yet). |
| **QA** | None required beyond sanity checklist. |
| **HITL** | Sponsor acknowledges project_type (production vs sandbox vs demo). |

### 2.2 `intake`

| Dimension | Content |
|-----------|---------|
| **Entry** | Exit from `created`. |
| **Exit** | Intake baseline approved (**G1**); scope_in/out documented. |
| **Blocking** | UNKNOWN business model or compliance posture without **SAFE UNKNOWN** policy. |
| **Invalidation** | Any intake change **invalidates** strategy drafts not yet frozen. |
| **QA** | Intake completeness QA. |
| **HITL** | **G1** sign-off. |

### 2.3 `classified`

| Dimension | Content |
|-----------|---------|
| **Entry** | Intake exit; **site_type_id** candidate selected. |
| **Exit** | `site_type_id` confirmed against [site-type-registry-v0.md](site-type-registry-v0.md); edge cases documented. |
| **Blocking** | Conflicting site type hypotheses without human resolution. |
| **Invalidation** | Reclassification **invalidates** registry-dependent defaults in strategy and blueprint. |
| **QA** | Classification QA (consistency with intake). |
| **HITL** | Human approver for edge cases (workflow v0 Stage 2). |

### 2.4 `strategy`

| Dimension | Content |
|-----------|---------|
| **Entry** | Classification stable enough for hypotheses. |
| **Exit** | Strategy bundle frozen post-**G2**; IA can proceed in parallel only if charter allows — blueprint must not freeze until IA outputs per artifact tree are satisfied. |
| **Blocking** | Brand/compliance conflicts; missing approval chain. |
| **Invalidation** | Strategy changes **invalidate** IA/blueprint/design copy assumptions per [dependency-invalidation-v0.md](dependency-invalidation-v0.md). |
| **QA** | Strategy QA lane; escalation signals per [orchestration-signals-v0.md](orchestration-signals-v0.md). |
| **HITL** | **G2**. |

### 2.5 `blueprint`

| Dimension | Content |
|-----------|---------|
| **Entry** | Strategy **G2** met; **IA** outputs (sitemap/nav/URL policy) **complete** for in-scope pages. |
| **Exit** | Blueprint batch approved (**G3**); per-page freeze policy applied. |
| **Blocking** | Oversized scope without change control; missing parent/child graph for multi-page sites (see [multi-page-orchestration-v0.md](multi-page-orchestration-v0.md)). |
| **Invalidation** | Blueprint edits **invalidate** design/frontend/QA for touched pages. |
| **QA** | Blueprint checklist + matrix row **Blueprint**. |
| **HITL** | **G3** (PM + tech lead; client if contractually required). |

### 2.6 `design`

| Dimension | Content |
|-----------|---------|
| **Entry** | Approved blueprint (for in-scope pages). |
| **Exit** | Design frozen post-**G5** for in-scope surfaces. |
| **Blocking** | Attempt to skip blueprint handoff; missing trust/CTA system alignment for site-level patterns. |
| **Invalidation** | Design changes **invalidate** matched frontend and dependent QA. |
| **QA** | Design QA. |
| **HITL** | **G5**. |

### 2.7 `frontend`

| Dimension | Content |
|-----------|---------|
| **Entry** | Design freeze for relevant scope **or** explicit waiver documented (rare; governance-heavy). |
| **Exit** | Frontend ready for QA freeze / RC tagging per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). |
| **Blocking** | Unapproved design drift; build breaks without triage owner. |
| **Invalidation** | Code/asset changes **invalidate** page/cluster QA as per dependency map examples. |
| **QA** | Automated checks if present (**SAFE UNKNOWN**); human QA always for gate. |
| **HITL** | **G6**. |

### 2.8 `qa`

| Dimension | Content |
|-----------|---------|
| **Entry** | Frontend candidate exists for validation scope. |
| **Exit** | QA outcome recorded: pass, conditional pass, fail, waiver path per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md). |
| **Blocking** | **Fail** with undeclared blockers; fake “pass” without evidence (**forbidden**). |
| **Invalidation** | New upstream edits force **return** to relevant stage and QA **reset** for affected scope. |
| **QA** | Full matrix application for scope; site-level vs page-level per QA matrix doc. |
| **HITL** | Escalation for waivers; **G7** readiness review. |

### 2.9 `approved`

| Dimension | Content |
|-----------|---------|
| **Entry** | QA exit allows delivery packaging. |
| **Exit** | **Release approval** recorded; export bundle pinned. |
| **Blocking** | Missing release approver; self-approval (**forbidden**). |
| **Invalidation** | **Approval invalidation** if critical defects found pre-publish — return to `qa` or `frontend` per [approval-semantics-v0.md](approval-semantics-v0.md). |
| **QA** | Pre-delivery validation slice. |
| **HITL** | **Release authority** distinct from authors. |

### 2.10 `delivery`

| Dimension | Content |
|-----------|---------|
| **Entry** | `approved` exit. |
| **Exit** | Handoff completed to hosting/ops **or** publish executed per charter. |
| **Blocking** | Missing export manifest; secrets handling not cleared (**SECURITY RISK** path). |
| **Invalidation** | Operational rollback does **not** erase lineage — document **revision**. |
| **QA** | Smoke / monitoring charter if defined (**SAFE UNKNOWN**). |
| **HITL** | Ops / client acceptance per contract (**not** autonomous). |

### 2.11 `released`

| Dimension | Content |
|-----------|---------|
| **Entry** | Delivery exit; live state reached. |
| **Exit** | None — steady state until **revision** or **archive** triggered. |
| **Blocking** | N/A. |
| **Invalidation** | Post-release defects → `revision` with traceability. |
| **QA** | Optional post-release audits. |
| **HITL** | Change board for hotfixes. |

### 2.12 `revision`

| Dimension | Content |
|-----------|---------|
| **Entry** | Change request after any prior state ≥ `strategy`. |
| **Exit** | Re-enter appropriate craft state (`strategy` … `qa`) per [revision-semantics-v0.md](revision-semantics-v0.md); re-approve as scope demands. |
| **Blocking** | Silent edits without invalidation analysis (**forbidden**). |
| **Invalidation** | Per revision scope — may be partial. |
| **QA** | **QA reset** for impacted matrix rows. |
| **HITL** | Revision approval + reopen authority per HITL governance doc. |

### 2.13 `archived`

| Dimension | Content |
|-----------|---------|
| **Entry** | Project closed or superseded by another `project_id`. |
| **Exit** | N/A (terminal for this id). |
| **Blocking** | Legal hold without archive policy — escalate. |
| **Invalidation** | Archived artifacts are **not** operational truth for new delivery. |
| **QA** | Retention audit if required. |
| **HITL** | Sponsor sign-off on archive. |

---

## 3. SAFE UNKNOWN

- **Exact** state persistence format (DB, JSON, Git tags) — **unknown**.
- **Automatic** transition triggers — **not** claimed; transitions are **human-authorized** in v0.

---

## 4. Changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-12 | Initial **Reference Project Lifecycle v0**. |
