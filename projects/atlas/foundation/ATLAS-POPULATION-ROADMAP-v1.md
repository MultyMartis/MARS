# ATLAS Population Roadmap v1

**Status:** **documented** — Phase 7 strategic population maturity roadmap.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-POPULATION-STRATEGY-v1.md](ATLAS-POPULATION-STRATEGY-v1.md) · [ATLAS-POPULATION-PRIORITIES-v1.md](ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md)  
**Is not:** implementation plan, sprint calendar, infrastructure timeline, hiring plan.

**Phase 1–6 constraint:** Roadmap references certification C0–C3 without altering certification rules.

---

## 1. Purpose

Map **population maturity progression** from empty registry discipline through **anchor graph** to **growth-ready** canonical reality — including **consumer readiness**, **expected risks**, and **review gates**.

This is a **strategic roadmap**, not an implementation schedule.

---

## 2. Maturity model overview

```text
Stage A ──► Anchor (orgs, people, participation)
Stage B ──► Structure (projects, web, domains)
Stage C ──► Graph (remaining relationships)
Stage D ──► Consumer reference readiness (C1+)
Stage E ──► Controlled growth & expansion discipline
```

Each stage maps to population **waves** and **certification posture**.

---

## 3. Stage A — Anchor reality

### 3.1 Scope

| Waves included | Primary deliverable |
|----------------|---------------------|
| Wave 1, 2, 2B | Operator orgs, persons, PERSON↔ORG participation |

### 3.2 Population maturity

| Dimension | Target state |
|-----------|--------------|
| Organizations | Core operator set **active** |
| People | Key participants **active** |
| Relationships | Participation edges **active** where evidenced |
| UNKNOWN | Explicit gaps documented — no placeholder orgs |

### 3.3 Consumer readiness implications

| Certification | Implication |
|---------------|-------------|
| **C0** | Consumers may **read** anchor ids for operator org/person |
| **C1** | Not yet — needs project/web identity |
| **C2+** | Blocked |

Consumers should **not** treat ATLAS as complete site graph.

### 3.4 Expected risks

| Risk | Mitigation |
|------|------------|
| PR-01 duplicate orgs | Slow Wave 1 attest |
| PR-09 homonyms | Identity review |
| Multi-hat without 2B | Defer person attest until edges queued |

### 3.5 Review gates (Stage A exit)

| Gate ID | Criterion |
|---------|-----------|
| **GA-01** | Core operator orgs **active** with E0–E1 trail |
| **GA-02** | No D1 unresolved in Organization/Person |
| **GA-03** | Wave 2B complete or explicitly deferred with owner sign-off |
| **GA-04** | No `org-unknown-*` canonical |
| **GA-05** | Owner/steward population halt not active |

**Exit:** Authorize Stage B.

---

## 4. Stage B — Structural containers and web presence

### 4.1 Scope

| Waves included | Primary deliverable |
|----------------|---------------------|
| Wave 3, 4, 5 | Projects, websites, domains |

### 4.2 Population maturity

| Dimension | Target state |
|-----------|--------------|
| Projects | Active pilots/packs referenced by consumers |
| Websites | Active properties with org **active** or **UNKNOWN** declared |
| Domains | Primary domains linked or **proposed** |

### 4.3 Consumer readiness implications

| Certification | Implication |
|---------------|-------------|
| **C0** | Continue read-only for partial graph |
| **C1** | Factory/ORCA/MIG may **reference** website/project ids in handoffs |
| **C2** | Partial — needs relationship graph for ownership claims |

### 4.4 Expected risks

| Risk | Mitigation |
|------|------------|
| PR-04 website without org | UNKNOWN + proposed links |
| PR-06 SERP conflation | Proposal-only MIG |
| Staging/prod URL duplication | Alias policy / separate proposed |

### 4.5 Review gates (Stage B exit)

| Gate ID | Criterion |
|---------|-----------|
| **GB-01** | Priority projects **active** or scoped proposed |
| **GB-02** | Consumer-facing websites **active** with evidence |
| **GB-03** | Domains for primary properties attested or deferred with rationale |
| **GB-04** | No active OWNS/BELONGS_TO to non-existent org |
| **GB-05** | Stage A gates still hold (no regression) |

**Exit:** Authorize Stage C.

---

## 5. Stage C — Complete structural graph

### 5.1 Scope

| Waves included | Primary deliverable |
|----------------|---------------------|
| Wave 6 (6A–6D) | ORG↔ORG, PROJECT links, WEBSITE/DOMAIN families |

### 5.2 Population maturity

| Dimension | Target state |
|-----------|--------------|
| Commercial structure | CLIENT_OF / VENDOR_OF where evidenced |
| Ownership | OWNS, PRIMARY_DOMAIN active |
| Grouping | BELONGS_TO project/website clusters |

### 5.3 Consumer readiness implications

| Certification | Implication |
|---------------|-------------|
| **C1** | Stable for handoff reference |
| **C2** | Ownership and client structure queries supported |
| **C3** | Requires ongoing governance discipline — not automatic at Stage C |

### 5.4 Expected risks

| Risk | Mitigation |
|------|------------|
| PR-03 early wrong OWNER | Wave 6 only after endpoints |
| Conflicting CLIENT_OF | **disputed** workflow |
| Relationship import bulk | STOP-06 if unreviewed |

### 5.5 Review gates (Stage C exit)

| Gate ID | Criterion |
|---------|-----------|
| **GC-01** | Wave 6A–6D complete for **priority** graph (not every historical edge) |
| **GC-02** | No disputed **active** OWNER/CLIENT_OF |
| **GC-03** | Endpoint review after any merges in Stages A–B |
| **GC-04** | Population stop triggers clear |

**Exit:** Authorize Stage D.

---

## 6. Stage D — Consumer reference readiness

### 6.1 Scope

**Stabilization** — not new entity classes. Focus:

- certification uplift targets;
- consumer mapping tables (conceptual);
- dispute backlog burn-down.

### 6.2 Population maturity

| Dimension | Target state |
|-----------|--------------|
| Graph | **Priority** ecosystem reality canonical |
| Proposed backlog | Bounded with steward SLA (ops doc) |
| UNKNOWN | Enumerated gaps with owners |

### 6.3 Consumer readiness implications

| Certification | Implication |
|---------------|-------------|
| **C1** | Default target for production consumers |
| **C2** | ORCA/Factory ownership-sensitive flows |
| **C3** | Only after sustained attestation quality |

### 6.4 Expected risks

| Risk | Mitigation |
|------|------------|
| PR-08 consumer pressure | Certification gates |
| Cache drift vs ATLAS | UNKNOWN until reconcile |
| Premature C3 | Certification review |

### 6.5 Review gates (Stage D exit)

| Gate ID | Criterion |
|---------|-----------|
| **GD-01** | Consumer certification checklist pass ([ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md)) |
| **GD-02** | Mapping proposals triaged |
| **GD-03** | No STOP trigger active |

**Exit:** Authorize Stage E.

---

## 7. Stage E — Controlled growth

### 7.1 Scope

Ongoing population after initial anchor:

- new client orgs;
- new pilots;
- deprecation/supersession;
- expansion requests per [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md).

### 7.2 Population maturity

| Dimension | Target state |
|-----------|--------------|
| Throughput | Sustainable steward intake |
| Quality | Stable duplicate/dispute rates |
| Expansion | Governed — not ad-hoc fields |

### 7.3 Consumer readiness implications

Consumers at **C1+** participate in **propose** flows; ATLAS remains attestor.

### 7.4 Expected risks

| Risk | Mitigation |
|------|------------|
| PR-07 agent flood | POP-C-02, STOP-03 |
| Registry pollution | Wave discipline + halt rules |
| Expansion creep | Separate expansion review |

### 7.5 Review gates (ongoing)

| Gate ID | Cadence |
|---------|---------|
| **GE-01** | Quarterly population quality review |
| **GE-02** | Annual certification revalidation |
| **GE-03** | Expansion impact before new types |

---

## 8. Roadmap ↔ wave mapping

| Stage | Waves | Certification focus |
|-------|-------|---------------------|
| **A** | 1, 2, 2B | C0 read anchors |
| **B** | 3, 4, 5 | C1 reference projects/sites |
| **C** | 6 | C2 structural queries |
| **D** | Stabilization | C1–C2 production |
| **E** | Ongoing | C3 selective |

---

## 9. Dependencies on future packages (non-blocking)

| Package | Roadmap interaction |
|---------|---------------------|
| **ATLAS Operational Model** | Steward roster, SLA, intake queues — **enables** Stage A execution |
| **Business Scope Foundation** | Optional consumer tags — **does not** gate Stages A–C |
| **Registry Readiness Audit** | May precede Stage A kickoff — validation only |
| **Implementation Planning** | After ops + audit — technical channels |

Population roadmap **does not require** Business Scope or implementation to be **defined**.

---

## 10. Strategic checkpoints summary

| Checkpoint | Question answered |
|------------|-------------------|
| After Stage A | Can we name operator businesses and who participates? |
| After Stage B | Can we reference pilots and web properties safely? |
| After Stage C | Is structural graph trustworthy for ownership/client queries? |
| After Stage D | Are consumers certified to rely on references? |
| Stage E | Is growth sustainable without pollution? |

---

## 11. Non-deliverables

No dates, no resource estimates, no tooling selection.

---

*ATLAS Population Roadmap v1 — Phase 7 Foundation. Documentation only.*
