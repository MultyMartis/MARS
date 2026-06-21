# Groundtruth Ownership Rule v1

**Status:** **documented** — formal ecosystem rule (approved audit verdict).  
**Not:** schema, registry entry, automation spec, runtime policy, or enforcement engine.

**Verdict (normative):**

> **MIG = Groundtruth Owner (R1)**  
> **ORCA = Interpretation Owner (R2)**

**Canonical boundary:**

> **MIG acquires reality. ORCA interprets reality.**

---

## 1. Purpose

This rule exists to **eliminate ambiguity** about who owns market reality in the MARS ecosystem.

The Groundtruth Ownership Audit identified **Dual Groundtruth Path** as a **P0 risk**: two parallel lanes can both claim to be the source of market truth. That ambiguity breaks handoff discipline, duplicates capture work, and lets interpretation masquerade as acquisition.

This document **records the approved verdict**. It does **not** redesign MIG, ORCA, Website Factory, MetaBOT, or any runtime. It states **who owns what** and **which relationships are allowed or forbidden**.

---

## 2. Definitions

| Term | Meaning |
|------|---------|
| **Groundtruth** | Evidence-grade market reality: what was observed, captured, or recorded about SERP, competitors, offers, keywords, landings, and related surfaces — **before** strategic interpretation, clustering, or campaign architecture. |
| **Interpretation** | Human-supervised analysis that assigns meaning to groundtruth: intent, semantic clustering, prioritization, PPC structure, campaign planning, and export-oriented artifacts. Interpretation **depends on** groundtruth; it does **not** replace it. |
| **Acquisition** | The act of obtaining and preserving market reality: capture, normalization, grading, session binding, and production of an approved groundtruth product. **Acquisition ownership belongs to MIG (R1).** |
| **Consumption** | The act of reading, referencing, or building upon **approved** groundtruth without re-owning capture discipline. ORCA, Website Factory, and MetaBOT may consume groundtruth only through **allowed** paths defined below. Consumption is **not** acquisition. |

---

## 3. Ownership

### MIG owns (R1 — Groundtruth)

MIG is the **sole Groundtruth Owner** for:

- market reality **acquisition**
- SERP **capture**
- competitor **capture**
- offer **capture**
- keyword **discovery** (phrases, suggestions, frequency tables as returned — capture-time)
- **evidence collection**
- **Research Pack** production (approved groundtruth product bound to a research session)

MIG **does not** own intent clustering, semantic core design, campaign architecture, or PPC export artifacts.

### ORCA owns (R2 — Interpretation)

ORCA is the **Interpretation Owner** for:

- **interpretation** of approved groundtruth
- **semantic clustering**
- **PPC architecture**
- **campaign planning**
- **export artifacts** (Commander packages, semantic packs, LRL-oriented outputs — as interpretation/transport products, not groundtruth SoT)

ORCA **does not** own groundtruth acquisition, SERP capture discipline, or Research Pack production as SoT.

**Dispute resolver:** If work mixes capture with interpretation, **split** it. MIG finishes acquisition and human approval; ORCA starts only after handoff.

---

## 4. Allowed Relationships

| From | To | Relationship |
|------|-----|--------------|
| **MIG** | **ORCA** | Approved groundtruth handoff (Research Pack or equivalent approved product). Direction: **MIG → ORCA only**. |
| **MIG** | **Website Factory** | Indirect via interpreted downstream artifacts — not raw unapproved session dumps by default. |
| **MIG** | **MetaBOT** | No implied orchestration or n8n ownership; MIG docs do not claim MetaBOT runtime. Market observation remains MIG acquisition when chartered. |

ORCA may hand off **interpreted** artifacts to Website Factory. That handoff does **not** transfer groundtruth ownership to ORCA or Factory.

---

## 5. Prohibited Relationships

The following are **not allowed** as normative ecosystem posture:

| Prohibition | Rationale |
|-------------|-----------|
| **ORCA must not become Groundtruth SoT** | ORCA interprets reality; it does not define acquisition ownership. |
| **Shared Groundtruth ownership is not allowed** | MIG and ORCA must not co-own capture discipline or compete as parallel truth authorities. |
| **Parallel Groundtruth SoT is not allowed** | No second lane — including legacy ORCA research trees, raw packs, or operator capture folders — may be treated as **normative** groundtruth ownership alongside MIG. |

**Dual Groundtruth Path** (MIG capture + ORCA-side parallel capture both treated as authoritative) remains a **P0 risk** and is **out of policy** for new work.

ORCA **must not** push capture ownership upstream into MIG by rewriting R1 scope from the interpretation lane.

---

## 6. Legacy Exception

### Triumph-era ORCA research paths

Before MIG R1 formalization, ORCA accumulated **Triumph-era** research material and operator workflows that include capture-like steps:

- ORCA **Research Layer** project-local storage (`serp/`, `competitors/`, `keywords/`, raw packs under `incoming/orca/`)
- Triumph Manipulator PPC pack research, semantic packs, battle-pilot evidence, and calibration cases
- Methodology and snapshot contracts under `projects/orca/research/`

These paths **may remain operational** for existing Triumph work, pilots, and human-supervised PPC sessions.

**Clarification (normative vs legacy):**

| Statement | Meaning |
|-----------|---------|
| Legacy paths **may remain operational** | Operators may continue using frozen Triumph workflows without immediate migration. |
| Legacy paths are **not normative ownership** | They do **not** establish ORCA as Groundtruth Owner for the ecosystem. |
| New groundtruth work | **MIG owns acquisition**; ORCA consumes **approved** handoffs. |

Legacy ORCA capture folders are **interpretation-lane artifacts** or **historical evidence**, not a second Groundtruth SoT. When Triumph-era material conflicts with MIG groundtruth, **MIG-approved Research Pack** wins for market reality; ORCA applies interpretation on top.

---

## 7. Future Direction

The **preferred model** for new work (documentation intent only — no automation implied):

```text
Research Request
  → Research Session
  → Research Pack
  → ORCA
```

| Stage | Owner | Role |
|-------|-------|------|
| Research Request | MIG intake | Bounded question and capture charter |
| Research Session | MIG (R1) | Acquisition unit — manifests, captures, grading |
| Research Pack | MIG (R1) | Approved groundtruth product |
| ORCA | ORCA (R2) | Interpretation, clustering, PPC architecture, exports |

This direction **does not** describe runtime, pipelines, APIs, or automation. It states the **ownership chain** humans should follow to avoid Dual Groundtruth Path.

---

## Related (non-normative detail)

Pack-level matrices and handoff fields live in project contracts — this rule does **not** replace them:

- MIG boundaries: [projects/mig/boundaries.md](../../projects/mig/boundaries.md)
- MIG → ORCA handoff: [projects/mig/contracts/mig-orca-handoff-contract-v0.md](../../projects/mig/contracts/mig-orca-handoff-contract-v0.md)
- Research Pack contract: [projects/mig/contracts/mig-research-pack-contract-v0.md](../../projects/mig/contracts/mig-research-pack-contract-v0.md)
- ORCA evidence discipline: [projects/orca/evidence/evidence-discipline-model-v1.md](../../projects/orca/evidence/evidence-discipline-model-v1.md)

---

## Changelog

| Version | Date | Notes |
|---------|------|--------|
| v1 | 2026-06-04 | Formal rule from approved Groundtruth Ownership Audit verdict. |
