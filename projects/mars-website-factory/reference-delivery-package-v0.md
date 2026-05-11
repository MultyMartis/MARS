# MARS Website Factory — Reference Delivery Package v0

**Status:** **documentation only** — **package semantics** for handoff and release; **not** a build pipeline, registry service, or deployment automation claim.

**Version:** v0.

**Related:** [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [frontend-artifact-model-v0.md](frontend-artifact-model-v0.md), [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md).

---

## 1. Package types

### 1.1 Blueprint package

| Facet | Content |
|--------|---------|
| **Purpose** | Handoff bundle from **Strategy + IA** into **Design/Frontend** planning — canonical page definitions. |
| **Required artifacts** | Approved blueprints for in-scope pages; sitemap/nav excerpt; `site_type_id` row rationale. |
| **Required approvals** | **G3** for included pages. |
| **Required QA** | Blueprint matrix row **pass** or **conditional** with listed debt. |
| **Freeze behavior** | Package **pinned** at approval timestamp; later edits = **revision**. |
| **Revision triggers** | IA URL change; objective change; block palette change; scope add/remove pages. |

### 1.2 Design package

| Facet | Content |
|--------|---------|
| **Purpose** | Visual intent frozen for frontend implementation. |
| **Required artifacts** | Comps/specs per [design-handoff-contract-v0.md](design-handoff-contract-v0.md); tokens; component notes. |
| **Required approvals** | **G5**. |
| **Required QA** | Design QA lane verdict for scope. |
| **Freeze behavior** | **Frozen** per surface; partial packages allowed with explicit page list. |
| **Revision triggers** | Brand change; accessibility remediation; blueprint deltas. |

### 1.3 Frontend package

| Facet | Content |
|--------|---------|
| **Purpose** | Implementable / buildable **source** snapshot (not hand-edited `dist/` per [frontend-prompt-discipline-v0.md](frontend-prompt-discipline-v0.md)). |
| **Required artifacts** | Source tree, build instructions, dependency manifest, data attributes contract for JS. |
| **Required approvals** | **G6** merge / file-set approval. |
| **Required QA** | Frontend matrix row; security spot-check if policy demands. |
| **Freeze behavior** | RC tag in runbook; reproducible build hash if tooling supports it (**SAFE UNKNOWN**). |
| **Revision triggers** | Code change; asset swap; dependency upgrade affecting risk posture. |

### 1.4 QA package

| Facet | Content |
|--------|---------|
| **Purpose** | Evidence bundle attached to a **delivery candidate**. |
| **Required artifacts** | QA payloads per [qa-result-payloads-v0.md](qa-result-payloads-v0.md); trace to page IDs; waivers. |
| **Required approvals** | QA lead sign-off; **waiver authority** for any blocker turned waiver. |
| **Required QA** | Self-meta: QA bundle internally consistent (no contradictory verdicts). |
| **Freeze behavior** | Frozen when referenced by **delivery candidate** id. |
| **Revision triggers** | Any upstream change in **invalidation** scope. |

### 1.5 Export package

| Facet | Content |
|--------|---------|
| **Purpose** | Static **export** for hosting handoff (HTML/CSS/JS/assets + manifest). |
| **Required artifacts** | Built artifacts per charter; checksum/manifest; license/third-party notices. |
| **Required approvals** | **Release** chain per HITL governance (not authors-only). |
| **Required QA** | Pre-delivery validation + QA package reference. |
| **Freeze behavior** | **Immutable** after publish id unless rollback playbook says otherwise. |
| **Revision triggers** | Hotfix release = new export id + new QA linkage. |

### 1.6 Release candidate (RC)

| Facet | Content |
|--------|---------|
| **Purpose** | Named snapshot **candidate** for final gates — not yet “released”. |
| **Required artifacts** | Frontend package + QA package + known defects list. |
| **Required approvals** | Pre-release review meeting outcome (human). |
| **Required QA** | **Blocking** items cleared or **waived**. |
| **Freeze behavior** | RC **frozen** for comparison; superseded by RC+n on regressions. |
| **Revision triggers** | Failed smoke, security finding, scope creep. |

### 1.7 Delivery candidate

| Facet | Content |
|--------|---------|
| **Purpose** | The **union** of artifacts authorized to enter **delivery** state per [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md). |
| **Required artifacts** | Export package + QA package + approval record + rollback notes. |
| **Required approvals** | **Release approval** (distinct role). |
| **Required QA** | QA package attached; **no fake delivery acceptance**. |
| **Freeze behavior** | Candidate id pinned until released or rejected. |
| **Revision triggers** | Any **approval invalidation** or **blocking** QA regression. |

---

## 2. SAFE UNKNOWN

- Exact archive format (zip, tarball, OCI) — **charter**.
- Automated publishing hooks — **not** claimed by Website Factory v0 docs.

---

## 3. Changelog

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-12 | Initial **Reference Delivery Package v0**. |
