# ATLAS Consumer Contracts v1

**Status:** **documented** — Phase 4 normative consumer interaction contract.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) · [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)  
**Is not:** API specification, SDK, OAuth, webhook design, service-level agreement (SLA), rate limits.

**Phase 1–3 constraint:** No changes to approved Phase 1–3 documents unless contradictions are discovered. None identified at Phase 4 authoring.

---

## 1. Purpose

Define **how consumer systems may interact with ATLAS** — permissions, prohibitions, responsibilities, and boundary rules — so architecture stays **consumer-agnostic** while known programs (MIG, ORCA, Website Factory, WPilot, OCPilot, HomeGateway) can be validated against the same contract.

---

## 2. Contract philosophy

### 2.1 ATLAS is upstream truth for structure

Consumers treat ATLAS as **read-mostly canonical** for:

- entity ids and classes;
- structural relationships;
- attested aliases (when exposed).

Consumers treat their own stores as **authoritative for operations** (tasks, content, ads, SERP packs, deploys).

### 2.2 Humility and anti-fork

**Rule CC-01:** If ATLAS has an active canonical id for a subject, consumer **must use it** in durable cross-system references.

**Rule CC-02:** If ATLAS has no canonical id, consumer **must not invent a parallel canonical registry** — propose to ATLAS or mark local-only foreign keys until attestation.

---

## 3. Permitted interactions

| Interaction | Definition | Preconditions |
|-------------|------------|---------------|
| **Read** | Retrieve canonical ids, names, relationships, lifecycle state | Respect disputed/deprecated semantics |
| **Reference** | Store ATLAS id on consumer records (pilot, site pack, campaign shell) | Id must be active or explicitly proposed with risk flag |
| **Classify** | Attach consumer metadata tags (“pilot-2026”, “scope-andrey”) | Tags are **non-canonical**; Business Scope is classification, not entity |
| **Suggest** | Submit proposals: new entity, alias, relationship, correction | Proposal channel only; no silent promotion |

### 3.1 Read depth (conceptual)

| Depth | Allowed data |
|-------|--------------|
| **L0 — Id lookup** | Resolve `ORG-*` → exists, state |
| **L1 — Display** | Canonical name + attested aliases |
| **L2 — Graph** | Relationships for planning handoffs |
| **L3 — Governance meta** | Attestation date, evidence tier (for operators) |

Consumers in automation roles typically need **L0–L2** only.

---

## 4. Prohibited interactions

| Prohibition | Rule ID | Rationale |
|-------------|---------|-----------|
| **Silent overwrite** of canonical fields | CC-P01 | Destroys trust |
| **Auto-merge** duplicate entities | CC-P02 | [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) IGV-D01 |
| **Auto-attest** proposals | CC-P03 | [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) |
| **Fork canonical org/person lists** | CC-P04 | One graph |
| **Write pipeline/deal/task fields into ATLAS** | CC-P05 | [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) |
| **Promote MIG evidence to canonical without human** | CC-P06 | Market ≠ business attestation |
| **Use display name as durable primary key** | CC-P07 | Phase 3 identity rules |

---

## 5. Consumer responsibilities

Every consumer **must**:

| Resp ID | Responsibility |
|---------|----------------|
| **CR-01** | Document which ATLAS ids it references in charters or config |
| **CR-02** | Handle **SAFE UNKNOWN** without inventing ATLAS ids |
| **CR-03** | Route structural corrections through **suggest/propose**, not direct canonical write |
| **CR-04** | Keep **high-churn data** local (metrics, drafts, deploy hashes) |
| **CR-05** | On import, produce **mapping proposals**, not canonical truth |
| **CR-06** | Respect **deprecated** ids — follow successor/redirect when provided |
| **CR-07** | Not require Business Scope for core consumer function |

Every consumer **should**:

| Resp ID | Responsibility |
|---------|----------------|
| **CR-S01** | Flag suspected duplicates to steward |
| **CR-S02** | Version consumer foreign keys when ATLAS merge occurs |
| **CR-S03** | Separate “operational case” (OPS) from “business entity” (ATLAS) |

---

## 6. Consumer boundary rules

### 6.1 Data placement matrix

| Data class | ATLAS | Consumer |
|------------|-------|----------|
| Organization exists | Canonical | — |
| CRM deal stage | — | CRM / consumer |
| Website identity | Canonical | — |
| Last deploy git sha | — | WPilot / CI |
| Domain hostname identity | Canonical | — |
| Live DNS records | — | Hosting/DNS tools |
| Person exists | Canonical | — |
| WordPress user login | — | WPilot |
| Project container | Canonical | — |
| Sprint tasks | — | PM tools |
| SERP capture pack | — | MIG |
| Ad group structure | — | ORCA / ads |
| Generated contract PDF | — | Future doc system |
| Contract references org id | Pointer in doc metadata | ATLAS read |

### 6.2 Caching

Consumers **may cache** ATLAS reads for performance. Cache is **not canonical**. On conflict, follow [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) §8.3.

**Rule CC-CACHE-01:** Cache TTL and invalidation are **consumer-local** — ATLAS does not define sync in Phase 4.

---

## 7. Proposal contract (future-facing)

When proposal channels exist (manual intake first):

| Field (conceptual) | Required |
|--------------------|----------|
| Proposer system id | Yes |
| Entity/relationship candidate | Yes |
| Evidence ref or note | Recommended |
| Consumer foreign key | Optional |
| Suggested display name | Optional |

**Outcome:** ATLAS creates **proposed** record; steward attests or rejects.

Consumers **never** receive “auto-approved” responses for structural creates.

---

## 8. Known consumer profiles (examples)

Architecture treats all consumers **equally** under §3–6. Profiles illustrate **typical** read/suggest patterns — not special rights.

### 8.1 MIG (market groundtruth)

| Typical read | `ORG-*`, `WEB-*` for pilot subject |
| Typical suggest | New competitor org/website candidates from research |
| Must not | Store SERP packs in ATLAS; auto-attest market discovery as canonical org |
| Boundary | Market reality (MIG) ≠ business reality (ATLAS) |

### 8.2 ORCA (interpretation / campaigns)

| Typical read | Project, Website, Organization for pilot shell |
| Typical suggest | Structural links for campaign subject |
| Must not | Canonical ad groups, budgets, performance metrics |
| Boundary | Interpretation consumes ATLAS; does not redefine org |

### 8.3 Website Factory (site production)

| Typical read | Client Organization, Project, Website, Domain |
| Typical suggest | New website/domain when pack created |
| Must not | CMS content, product catalog as ATLAS entities |
| Boundary | Factory **produces** sites; ATLAS **identifies** them |

### 8.4 WPilot / OCPilot (CMS operations)

| Typical read | `WEB-*`, `ORG-*` for site context |
| Typical suggest | Alias for site title; flag wrong org link |
| Must not | Posts, orders, users as canonical entities |
| Boundary | Operational CMS state stays in pilot systems |

### 8.5 HomeGateway (operator cockpit)

| Typical read | Broad L1–L2 graph for navigation |
| Typical suggest | Intake forms → proposals (UX future) |
| Must not | Become alternate registry UI that writes canonical without attestation |
| Boundary | Cockpit **navigates** reality; ATLAS **holds** it |

### 8.6 Future secretary / document / contract / reporting systems

| Typical read | Organization, Person, Project ids for templates |
| Typical suggest | Corrections when generated doc exposes wrong party |
| Must not | Store signed PDFs as canonical core; own signature workflow |
| Boundary | **Document authority** is consumer; **party identity** is ATLAS |

---

## 9. Architectural decisions (consumer lens)

| Question | Decision |
|----------|----------|
| Can consumers create reality? | **No** — only **propose**; stewards **create canonical** |
| Can consumers propose reality? | **Yes** — §3 Suggest |
| Who owns attestation? | ATLAS roles — not consumers ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)) |
| Can ATLAS become operational authority? | **No** — consumers execute ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) RA-D08) |

---

## 10. Violation handling

| Violation type | Response |
|----------------|----------|
| Silent overwrite detected | Governance incident; rollback canonical; steward review |
| Parallel registry discovered | Merge plan required; consumer keys remapped |
| Boundary field in proposal | Reject per [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) |
| Repeated auto-attest attempts | Block integration until contract remediation |

Phase 4 does not define technical enforcement — **human governance** first.

---

## 11. Non-deliverables

No API routes, auth scopes, or SDK method lists.

---

*ATLAS Consumer Contracts v1 — Phase 4 Foundation. Documentation only.*
