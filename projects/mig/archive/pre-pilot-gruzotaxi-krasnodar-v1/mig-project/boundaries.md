# MIG — Boundaries

**Status:** **documented** — canonical ownership matrix (bootstrap v1).  
**Not:** enforcement engine, API policy, or automated boundary checker.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This sentence is the **default** dispute resolver between MIG and ORCA. If a task mixes capture with interpretation, **split** the work: MIG finishes acquisition and approval; ORCA starts only after handoff.

---

## MIG vs ORCA

| Concern | MIG | ORCA |
|---------|-----|------|
| SERP / competitor / local pack **capture** | **Owns** | Uses handoff — does not re-own capture discipline |
| Reviews, trust, offer, CTA **capture** | **Owns** (Website Acquisition) | Interprets patterns for PPC / intelligence |
| Landing **structuring** (blocks, typed observations, evidence) | **Owns** — [contracts/mig-landing-analysis-architecture-v1.md](contracts/mig-landing-analysis-architecture-v1.md) | Interprets meaning, positioning, prioritization |
| Snapshots & session manifests | **Owns** | References in analysis — does not replace MIG archive |
| Evidence grading (capture-time) | **Owns** | May apply **analysis-time** confidence — separate layer |
| Intent / semantic clustering | **Excluded** | **Owns** |
| Keyword **capture** (phrases, suggestions, Wordstat tables, frequency as returned) | **Owns** — [contracts/mig-keyword-intelligence-architecture-v1.md](contracts/mig-keyword-intelligence-architecture-v1.md) | **Interprets** — clustering, prioritization, PPC/SEO structure |
| Campaign / ad group architecture | **Excluded** | **Owns** |
| LRL, PPC exports, Commander packages | **Excluded** | **Owns** |
| Live PPC review loops, heuristics, pilots | **Excluded** | **Owns** |
| Handoff direction | MIG → ORCA only (approved packs) | ORCA does not push capture ownership upstream into MIG |

**Do not** migrate ORCA research ownership into MIG in bootstrap v1. **Do not** rewrite ORCA layers from this pack.

---

## MIG vs Website Factory

| Concern | MIG | Website Factory |
|---------|-----|-----------------|
| Market groundtruth capture | **Owns (R1)** | **Excluded** |
| Site strategy, blueprints, semantics, QA/HITL | **Excluded** | **Owns (R3)** |
| Content packs, production workflows | **Excluded** | **Owns** |
| Reference project methodology | **Excluded** | **Owns** |
| Consumption path | MIG → ORCA → (strategy) → Factory | Factory **does not** read raw MIG sessions by default |

Factory may use **interpreted** intelligence only through established downstream artifacts — not unapproved MIG dumps.

---

## MIG vs MetaBOT

| Concern | MIG | MetaBOT |
|---------|-----|---------|
| Market observation & snapshots | **Owns** | **Excluded** |
| n8n workflows, Telegram bot cluster | **Excluded** | **External execution** |
| SEO content generation, Intake/Worker graphs | **Excluded** | **Owns (external)** |
| In-repo docs | `projects/mig/` | `projects/metabot-seo-content-agent/` |

MIG documentation **must not** imply n8n ownership, bot runtime, or MetaBOT orchestration.

---

## MIG vs WPilot

| Concern | MIG | WPilot |
|---------|-----|--------|
| SERP / market capture | **Owns** | **Excluded** |
| WordPress admin, plugin bridge, hosting | **Excluded** | **Owns (external implementation)** |
| Handoff | **None direct** | Implementation layer after site/strategy decisions |

---

## MIG vs OCPilot

| Concern | MIG | OCPilot |
|---------|-----|---------|
| Market / SERP groundtruth | **Owns** | **Excluded** |
| OpenCart / ocStore baselines, archive intake | **Excluded** | **Owns (external implementation)** |
| Handoff | **None direct** | Implementation layer for OpenCart stores |

---

## MIG vs mars-runtime

| Concern | MIG | mars-runtime |
|---------|-----|----------------|
| Research acquisition discipline | **Owns (docs + human artifacts)** | **Excluded** |
| Runtime, adapters, orchestration experiments | **Excluded** | **Contracts + narrow R1 experiments only** |
| Proof of automation | **None claimed** | **None implied for MIG** |

`mars-runtime/` does **not** execute MIG sessions. Any future adapter sketch is **experimental** and **outside** MIG bootstrap scope until explicitly chartered and evidenced.

---

## Quick exclusion list (MIG does NOT own)

- Intent clustering · semantic clustering · keyword prioritization · semantic core · campaign architecture · LRL · PPC exports  
- Factory blueprints · content generation · CMS operations  
- Runtime orchestration · agents · automation · n8n  

---

## Handoff

Minimum approved pack: [contracts/mig-orca-handoff-contract-v0.md](contracts/mig-orca-handoff-contract-v0.md).
