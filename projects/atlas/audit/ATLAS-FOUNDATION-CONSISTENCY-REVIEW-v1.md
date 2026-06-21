# ATLAS Foundation Consistency Review v1

**Status:** Cross-phase consistency review (documentation only).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent audit:** [ATLAS-FOUNDATION-AUDIT-v1.md](ATLAS-FOUNDATION-AUDIT-v1.md)  
**Authoritative reconciliation layer:** [ATLAS-LIFECYCLE-CROSSWALK-v1.md](../foundation/ATLAS-LIFECYCLE-CROSSWALK-v1.md)

---

## 1. Review method

1. Map **stable concepts** across Phases 1–7.
2. Classify duplicates as **intentional layering**, **harmful duplication**, or **missing canonical source**.
3. Record **contradictions** with severity and resolution (amendment vs crosswalk vs ecosystem fix).
4. Verify **vocabulary stability** for lifecycle, identity, relationships, attestation, canonical posture.

**Rule applied:** Phase 5+ crosswalk and state registry **supersede interpretation** of earlier phase enum fragments where listed.

---

## 2. Vocabulary stability matrix

### 2.1 Lifecycle vocabulary

| Term | Phase introduced | Authoritative definition | Stable? |
|------|------------------|-------------------------|---------|
| `proposed` | Phase 2 (relationships); unified Phase 5 | [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) §3.1 | **Yes** |
| `active` | Phase 2/3/4 fragments; unified Phase 5 | State Registry §3.2; SC-L01 | **Yes** |
| `disputed` | Phase 2+ | State Registry §3.3 | **Yes** |
| `deprecated` | Phase 1 implied; Phase 2+ | State Registry §3.4 | **Yes** |
| `archived` | Phase 2 relationships; universal Phase 5 | State Registry §3.5 | **Yes** |
| `merged` | Phase 3 `merged_into`; normative Phase 5 | Crosswalk §6.1 | **Yes** (code alias) |
| `split_source` | Phase 3 `split_from` | Crosswalk §6.2 | **Yes** (code alias) |
| `replaced` | Phase 2 relationships | State Registry §4.3 | **Yes** |
| **SAFE UNKNOWN** | Phase 1+ | **Not a state** — posture | **Yes** |

**Semantic drift (documentation only):** Phase 1/4 partial lists — **resolved by crosswalk**, not contradiction.

### 2.2 Identity vocabulary

| Term | Stable meaning across phases? | Notes |
|------|------------------------------|-------|
| Stable opaque id | Yes | Phase 3 identifier model |
| `ORG-*`, `PER-*`, etc. | Yes | Namespace rules consistent |
| Alias | Yes | Phase 3 alias model |
| Merge / split | Yes | IGV + lifecycle facets |
| Identity lifecycle = entity record | Yes | Phase 5 §5; no shadow state machine |

### 2.3 Relationship vocabulary

| Term | Stable? | Notes |
|------|---------|-------|
| Relationship as MVP entity | Yes | Phase 1 taxonomy + Phase 2 model |
| OWNER, CLIENT_OF, … | Yes | Phase 2 taxonomy — **Phase 1 text stale** |
| Participation ≠ ownership | Yes | CR-parallel, RM-01, SC-R03 |
| Slot / supersession | Yes | Phase 2 lifecycle + Phase 5 **replaced** |
| FORMER_* types | Yes | Taxonomy prefix, **not** lifecycle state |

### 2.4 Attestation vocabulary

| Term | Stable? | Canonical source |
|------|---------|------------------|
| Proposal vs canonical | Yes | Attestation Model §2 |
| Evidence E0–E3 | Yes | Attestation §3.2 (unified from Phase 2) |
| Steward vs owner authority | Yes | Matrices align across IGV, GV, POP-GV |
| Attestation ≠ ops approval | Yes | RA-D08, Attestation §2.2 |

### 2.5 Canonical posture

| Rule set | Consistent? |
|----------|-------------|
| CR-01–CR-10 (Phase 1) | Yes — CR-10 = SAFE UNKNOWN |
| C-01–C-06 (Phase 4) | Yes — requires **active** + attest |
| LC-P-03, LC-INV-01/02 (Phase 5) | Yes — one active canonical per subject/slot |
| POP-P-06 disputed block | Yes — aligns with LC-P-04 |

---

## 3. Duplicate concept analysis

### 3.1 Attestation

| Location | Role |
|----------|------|
| Phase 1 Reality | Principle: human attestation |
| Phase 2 Relationship Governance | Relationship attest + evidence tiers |
| Phase 3 Identity Governance | Entity promote, merge, split |
| Phase 4 Attestation Model | **Authoritative unified trust model** |
| Phase 7 Population | Population attest execution context |

**Classification:** **Intentional layering** — Phase 4 generalizes without weakening GV-01/IGV-01.  
**Canonical source:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md).

### 3.2 SAFE UNKNOWN

| Location | Role |
|----------|------|
| Reality CR-10, §7 | Core prohibition on invention |
| Attestation AT-UK-* | Blocks promotion |
| Lifecycle LG-SU-* | Slot/subject posture |
| State Registry §7 | Not a record state |
| Population §6–7 | Intake deferral |
| Consumer Semantic Contract | Consumer halt rules |

**Classification:** **Intentional reinforcement** — same rule at different layers.  
**Canonical source:** Posture definition in [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) §7; normative rules in Reality CR-10 + Attestation §7.

### 3.3 Ownership (disambiguation)

| Meaning | Where | Conflict? |
|---------|-------|-----------|
| **OWNER** relationship type | Phase 2 taxonomy | No |
| **Program owner** governance role | IGV, Attestation, POP | No |
| **Registry ownership** (ATLAS program) | Entity Registry Model §3 | No |
| **CRM account owner** | Excluded — consumer-local | No |
| **Business Scope as ownership** | Forbidden RA-BS01, CA-P07 | No |

**Classification:** Homonyms **adequately separated**.

### 3.4 Canonical / active

| Term | Meaning |
|------|---------|
| **canonical** (adjective) | Meets C-01–C-06 |
| **active** (lifecycle code) | Attested current structural truth |
| **Canonical for forward structure** | Lifecycle matrix — only **active** (+ rules) |

**Classification:** **Harmless duplication** — `active` operationalizes “canonical now.”

### 3.5 Dispute

| Mechanism | Docs |
|-----------|------|
| Lifecycle `disputed` | Phase 5 |
| Relationship dispute resolution | Phase 2 RG |
| Identity duplicate/dispute | Phase 3 IGV |
| Consumer challenge | Phase 6 CG |
| Population POP §8 | Phase 7 |

**Classification:** **Intentional layering** — same state, domain-specific resolution paths.

### 3.6 Evidence tiers

Defined in Phase 2 RG §3.1, **repeated and extended** in Phase 4 Attestation §3.2 and Phase 7 Evidence Requirements.

**Classification:** **Intentional** — Phase 4 is canonical; Phase 7 applies to population waves.

---

## 4. Cross-phase contradiction log

| ID | Phases | Claim A | Claim B | Resolution | Severity |
|----|--------|---------|---------|------------|----------|
| **X-01** | 1 vs 2 | Relationship types “future” (Reality §5.2, Taxonomy §6) | Full taxonomy in Phase 2 | Crosswalk + footnote amendment | P2 doc drift |
| **X-02** | 3 vs 5 | Code `merged_into` | Code `merged` | Crosswalk §6.1 synonym | P3 |
| **X-03** | 3 vs 5 | Code `split_from` | Code `split_source` | Crosswalk §6.2 synonym | P3 |
| **X-04** | 4 vs 5 | RA-05 lists 4 states | State registry 6 core + facets | RA-05 non-exhaustive; crosswalk §7 | P3 |
| **X-05** | 4 ER vs 3 | ER §4.1 shorter state list | Identity §7.1 fuller list | Phase 5 complete registry | P3 |
| **X-06** | Ecosystem | OPS entity class names | ATLAS MVP six entities | OPS map required | **P1** |

**Contradictions requiring Phase 1–4 foundation rewrite:** **None** (per Phase 5 crosswalk §6.6).

---

## 5. Authority and governance consistency

| Question | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Phase 6 | Phase 7 | Consistent? |
|----------|---------|---------|---------|---------|---------|---------|---------|-------------|
| Who attests **active**? | Human (design) | Steward/Owner | Steward/Owner | Steward/Owner | Lifecycle gates attest | Consumer cannot | Steward/Owner | **Yes** |
| Can agents auto-attest? | No | No | No | No | No | No | No | **Yes** |
| Who approves split? | — | — | Owner only | — | — | — | Owner only | **Yes** |
| Consumer write canonical? | No | No | No | No | No | No | No | **Yes** |
| Dispute escalation | Human owner | RG | IGV | Attestation | LG | CG | POP | **Yes** (paths differ by domain) |

---

## 6. Phase-to-phase dependency integrity

```text
Phase 1 ──must not be violated by──► Phases 2–7
         ▲
         └── Boundaries + MVP entity set respected in all later phases

Phase 2 ──adds types without──► new entities (constraint met)

Phase 3 ──does not redefine──► relationship endpoints (EIR-R01)

Phase 4 ──organizes without──► new entity types (RA intro)

Phase 5 ──unifies without──► editing Phase 1–4 (crosswalk only)

Phase 6 ──extends Phase 4 contracts──► not replace

Phase 7 ──uses Phase 1–6──► no taxonomy expansion in strategy
```

**Dependency violations found:** **None.**

---

## 7. Consumer semantic consistency (Phase 6 vs upstream)

| Upstream rule | Consumer contract | Match? |
|---------------|-------------------|--------|
| Lifecycle codes | SC-L01–L03 | Yes |
| CLIENT_OF / OWNER | SC-R01–R03 | Yes |
| SAFE UNKNOWN not `proposed` | CA-D05, SC §6 | Yes |
| merged/replaced redirect | CA-R03 | Yes |
| Ops lifecycle separate | CA-D01, Mapping Rules | Yes |

---

## 8. Population consistency (Phase 7 vs upstream)

| Upstream | Population rule | Match? |
|----------|-----------------|--------|
| EIR-R02 endpoints | POP-P-03 | Yes |
| CR-10 no placeholder org | POP-P-04, PR-02 | Yes |
| Wave order vs relationships | POP-P-05, Priorities §4 | Yes |
| AT-E-03 MIG | PR-06 | Yes |
| LC disputed | POP-P-06 | Yes |
| RA-BS01 scope | POP-P-08 | Yes |

---

## 9. Intentional vs harmful duplication — summary

| Type | Count | Action |
|------|-------|--------|
| Intentional layering | 6 domains | Keep; index canonical sources (GAP-03) |
| Harmful duplication | 0 | — |
| Missing canonical index | 1 | Add foundation index |
| Ecosystem vocabulary fork | 1 (OPS) | Amend OPS docs |

---

## 10. Consistency verdict

| Criterion | Result |
|-----------|--------|
| Definitions stable (with Phase 5 authority) | **Pass** |
| Concepts stable | **Pass** |
| Lifecycle vocabulary stable | **Pass** |
| Identity vocabulary stable | **Pass** (code aliases documented) |
| Relationship vocabulary stable | **Pass** (Phase 1 narrative stale) |
| Cross-phase logical contradictions | **None material** |
| Semantic drift | **Present but managed** via crosswalk |

**Consistency review conclusion:** Architecture is **internally consistent as one system** when Phase 5 crosswalk is treated as mandatory interpretation layer. **Documentation staleness** in Phase 1–2 and **OPS ecosystem mapping** are the primary consistency risks outside the crosswalk.

---

*ATLAS Foundation Consistency Review v1 — documentation only.*
