# ATLAS Wave 5 ZPM Domain Attestation v1

**Status:** **documented** — Wave 5 ZPM Domain attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ**  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) · [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) · [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** attestation runtime, signature platform, relationship attestation, Wave 5B ZPM execution, DNS automation.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Projects PRJ-0009, PRJ-0010: **attested** — AT-W3-ZPM-01..02
- Wave 3B ZPM Project ↔ Organization: **COMPLETE** — AT-W3B-ZPM-01..02
- Wave 4 ZPM Website attestation: **COMPLETE** — AT-W4-ZPM-01 (WEB-ZPM-01 **active**)
- Wave 4B ZPM Website Relationships: **COMPLETE** — AT-W4B-ZPM-01..02
- Population verdict: **READY FOR WAVE 5 ZPM DOMAIN POPULATION**

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 5 ZPM Domain, минимальные evidence gates, readiness по hostname anchor, missing evidence, candidate relationships для Wave 5B ZPM, **ownership neutrality**, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 5 ZPM attestation scope

| In scope | Out of scope |
|----------|--------------|
| Domain entity → **proposed** / **active** / **deprecated** | PRIMARY_DOMAIN Domain → Website |
| Evidence tier assignment per domain | OWNS / CUSTODIAN Organization → Domain |
| Lifecycle structural state (no DNS/registrar ops vocabulary) | SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO |
| Org/website **candidate** context (display only) | Website → Domain edges |
| Registrar status = **SAFE UNKNOWN** unless E1 registrar evidence | OPERATES Organization → Website |
| Wave 5B ZPM **queue preparation** | CLIENT_OF Organization ↔ Organization |
| Singleton `bzpm.ru` — DOM-ZPM-01 only | Foundation amendments |
| Ownership neutrality — no registrant inference | DNS / registrar API modeling |
| `www.bzpm.ru` hostname policy | Wave 5B ZPM steward decision |

Wave 5B ZPM relationship **active** attestation executes in a **separate pass** after Domain endpoint is **active**.

---

## 3. Attestation readiness by domain

| domain_id | Domain | Target state | Min tier | Readiness | Blocker |
|-----------|--------|--------------|----------|-----------|---------|
| **DOM-ZPM-01** | bzpm.ru | **active** | E1 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Domain to target lifecycle state now.
- Domain **OWNS** and PRIMARY_DOMAIN remain **Wave 5B ZPM** — not blockers for Wave 5 entity attestation.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W5-ZPM-01 — ZPM apex hostname

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify WEB-ZPM-01 **active** (Wave 4 ZPM) | Steward | AT-W4-ZPM-01 |
| 2 | Verify Wave 4B ZPM complete — REL-ZPM-WB-01/03/04 **active** | Steward | AT-W4B-ZPM-01..02 |
| 3 | Confirm REL-ZPM-WB-04 Website OWNS **does not** substitute domain registrant | Steward | Population §6 |
| 4 | Propose DOM-ZPM-01 canonical name **bzpm.ru** | Steward | Operator roster + EV-W1B-CC-01 §17 |
| 5 | Confirm singleton model — no second DOM for PRJ-0010 / WEB-ZPM-02 | Steward | COR-ZPM-WEB-10 |
| 6 | Assign E1; record ownership **context only — not attested** for ORG-0005 | Steward | Population §6 |
| 7 | Set registrar status **SAFE UNKNOWN** | Steward | No registrar export in repo |
| 8 | Confirm no duplicate `bzpm.ru` DOM-* in core register | Steward | Wave 5 DOM-0001..0004 cross-check |
| 9 | Attest Domain **active** | Steward (delegated) or Owner | W5-ZPM-LC-01 |
| 10 | Queue 5B ZPM: PRIMARY_DOMAIN → WEB-ZPM-01; www policy | Steward | Population §8 |

---

## 5. Evidence gates

| Gate | Requirement | Wave 5 ZPM outcome |
|------|-------------|-------------------|
| **EG-W5-ZPM-01** | Hostname string attested (FQDN apex) | **Pass** — DOM-ZPM-01 |
| **EG-W5-ZPM-02** | Minimum E1 for operator primary domain ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5) | **Pass** — CC §17 + operator roster |
| **EG-W5-ZPM-03** | Matching Website **active** (typical case) | **Pass** — WEB-ZPM-01 |
| **EG-W5-ZPM-04** | No DNS record modeling in entity fields | **Pass** |
| **EG-W5-ZPM-05** | Registrar/registrant E1 for domain OWNS | **Not required** for Wave 5 entity attestation — deferred Wave 5B ZPM |
| **EG-W5-ZPM-06** | Single-domain model — one DOM per `bzpm.ru` | **Pass** — COR-ZPM-WEB-10 |
| **EG-W5-ZPM-07** | No registrant inference from Website OWNS / CC / Project | **Pass** — ownership neutrality |

---

## 6. Evidence basis (attestation package)

| Ref | Tier | Role | Domain attestation use |
|-----|------|------|------------------------|
| Operator-approved roster | intake | DOM-ZPM-01 mint authority | **Yes** |
| **EV-W1B-CC-01** §17 | E1 | Hostname string on CC | **Yes** — not registrant |
| **EV-ZPM-OP-ACT-01** | E0 | Ongoing property | Context only |
| **AT-W4-ZPM-01** | attestation | WEB-ZPM-01 **active** | **Yes** |
| **AT-W4B-ZPM-01..02** | attestation | Website graph complete | Prerequisite — not domain OWNS basis |
| **AT-W1B-01** | attestation | ORG-0005 **active** | Org endpoint — not domain registrant |
| **COR-ZPM-WEB-10** | correction | Singleton DOM | **Yes** |

**Explicitly excluded as domain registrant evidence:**

| Ref | Reason |
|-----|--------|
| REL-ZPM-WB-04 Website OWNS | Website property ≠ domain registrant |
| PRJ-0009 / PRJ-0010 lifecycle | Project layer |
| EV-W1B-CC-01 §17 alone | Website field — not registrar export |
| Operator assumption ORG-0005 owns domain | Not attested without registrar E1 |

---

## 7. Ownership neutrality review

| Topic | Attestation posture |
|-------|---------------------|
| Current registrar | **SAFE UNKNOWN** — steward records; no inference |
| Current registrant | **SAFE UNKNOWN** — steward records; no inference |
| ORG-0005 on `primary_org_candidate` | **Display context only — not attested** |
| REL-ZPM-WB-04 | Website-family edge — **does not** promote to domain OWNS in this act |
| Wave 5B proposed ORG-0005 → DOM-ZPM-01 OWNS | **Queued** — requires registrar E1 (SU-ZPM-PRJ-08) |

**Distinction (SU-W4B-06 analog — ZPM):**

```text
REL-ZPM-WB-04  ORG-0005 ──OWNS──► WEB-ZPM-01     [attested Wave 4B — website property]
(proposed 5B)  ORG-0005 ──OWNS──► DOM-ZPM-01     [requires domain-level E1 — NOT inferred]
```

---

## 8. Missing evidence (non-blocking for Wave 5 ZPM entity attestation)

| ID | Gap | Severity | Wave impact |
|----|-----|----------|-------------|
| **ME-W5-ZPM-01** | Registrar WHOIS / registrant export for DOM-ZPM-01 | Medium for domain OWNS | Wave 5B ZPM — blocks **active** ORG→Domain OWNS, not Domain entity |
| **ME-W5-ZPM-02** | `www.bzpm.ru` hostname policy | Low | Wave 5B ZPM SECONDARY_DOMAIN or new DOM |
| **ME-W5-ZPM-03** | Live URL probe formal log (SU-W4-ZPM-01) | Low | E0/E1 sufficient via CC + attestation chain |
| **ME-W5-ZPM-04** | ORG-0001 CUSTODIAN/OPERATES on domain | Low | SAFE UNKNOWN — SU-W4B-ZPM-01 |

---

## 9. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01 | **Excluded** — Wave 5B ZPM |
| OWNS / CUSTODIAN Org/Person → Domain | **Excluded** — Wave 5B ZPM |
| SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Excluded** — Wave 5B ZPM |
| OPERATES ORG-0001 → WEB-ZPM-01 | **Excluded** — SAFE UNKNOWN |
| CLIENT_OF ORG-0005 → ORG-0001 | **Excluded** — Wave 6 |
| DNS A/CNAME/MX/TXT modeling | **Excluded** — out of ATLAS scope |
| Registrar API integration | **Excluded** — no implementation |
| Second DOM-* for historical PRJ-0010 generation | **Excluded** — rejected |
| Infer registrant from Website OWNS / CC / Project | **Excluded** — ownership discipline |

---

## 10. Deferred items

| Item | Reason | Target |
|------|--------|--------|
| PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01 | Domain endpoint pending attestation act | **Wave 5B ZPM** |
| ORG-0005 OWNS DOM-ZPM-01 | Registrar E1 absent | **Wave 5B ZPM** |
| `www.bzpm.ru` policy | Not in approved roster | **Wave 5B ZPM** |
| OPERATES ORG-0001 | SAFE UNKNOWN | Future governance |
| REL-0016 CLIENT_OF | Commercial org edge | **Wave 6** |

---

## 11. Candidate Wave 5B ZPM relationships

| Draft candidate | source | target | Type | Evidence gate |
|-----------------|--------|--------|------|---------------|
| *(TBD rel_id)* | DOM-ZPM-01 bzpm.ru | WEB-ZPM-01 | **PRIMARY_DOMAIN** | DOM-ZPM-01 **active** + WEB-ZPM-01 **active** |
| *(TBD rel_id)* | ORG-0005 ЗПМ | DOM-ZPM-01 | **OWNS** | **E1 registrar/registrant** — ME-W5-ZPM-01 |
| *(TBD)* | `www.bzpm.ru` | WEB-ZPM-01 | SECONDARY_DOMAIN or REDIRECTS_TO | Steward policy — ME-W5-ZPM-02 |

**Not in Wave 5B candidate roster:** DOM entities for retired WEB-ZPM-02; PRIMARY_DOMAIN to nonexistent Website; OPERATES (unless steward opens separate review).

---

## 12. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5 | Domain = hostname anchor — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | One id per hostname; www not assumed — **Pass** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.5 | Punycode/www policy deferred — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Domain **active** state — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5 | E1 at active — **Pass** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | DOM may exist; domain OWNS UNKNOWN — **Pass** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) Wave 5 | Ordering after Website 4B — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7–9 | Families documented — edges not created — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation path — **Pass** |
| [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | No registrant inference — **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | WEB-ZPM-01 attested **active** | **Pass** |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Website-family graph complete | **Pass** |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 **active** | **Pass** |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | No `bzpm.ru` duplicate | **Pass** |

**Foundation modified:** **No**  
**Wave 1B–4B ZPM modified:** **No**  
**Core Wave 5 Triumph modified:** **No**  
**New entity types:** **No**  
**Domain relationships created:** **No**

---

## 13. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W5-ZPM-01** | Domain registrant / registrar account for DOM-ZPM-01 | Medium | Blocks Wave 5B ZPM **active** domain OWNS — not Domain entity |
| **SU-W5-ZPM-02** | `www.bzpm.ru` — separate DOM vs alias edge | Low | Wave 5B ZPM hostname policy |
| **SU-W5-ZPM-03** | ORG-0001 technical custodian on DNS | Low | Not blocking PRIMARY_DOMAIN |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | Open — Wave 5B ZPM domain OWNS gate |
| **SU-W4B-ZPM-01** | ORG-0001 OPERATES WEB-ZPM-01 | Low | Not blocking Domain population |

---

## 14. Wave 5B ZPM readiness assessment

### 14.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 5 ZPM Domain population documented (DOM-ZPM-01) | **Pass** |
| Singleton hostname entity — no dual-generation DOM | **Pass** |
| Target lifecycle **active** | **Pass** |
| Matching WEB-ZPM-01 **active** | **Pass** |
| PRIMARY_DOMAIN candidate documented (1) | **Pass** |
| No premature Domain relationships | **Pass** |
| Registrar posture SAFE UNKNOWN documented | **Pass** |
| Ownership neutrality — no registrant inference | **Pass** |
| No DNS-level modeling | **Pass** |
| No duplicate hostname with core DOM-0001..0004 | **Pass** |
| Foundation unchanged | **Pass** |

### 14.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Domain intake cannot proceed to attestation or relationship pass |
| **PARTIALLY READY** | Subset only — **not applicable** (singleton roster) |
| **READY FOR WAVE 5 ZPM DOMAIN ATTESTATION** | Population complete; steward attestation act may proceed |
| **READY FOR WAVE 5B ZPM DOMAIN RELATIONSHIP POPULATION** | *(after attestation act)* Domain entity **active**; relationship pass may proceed |

### 14.3 Verdict (population phase — this document)

```text
READY FOR WAVE 5 ZPM DOMAIN ATTESTATION
```

**Conditions:**

1. Steward executes attestation tranche **AT-W5-ZPM-01** to promote DOM-ZPM-01 from population draft to canonical **active**.
2. After attestation act, verdict upgrades to **READY FOR WAVE 5B ZPM DOMAIN RELATIONSHIP POPULATION**.
3. Wave 5B ZPM **Phase A** (PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01) may proceed after Domain attestation — one PRIMARY_DOMAIN per Website.
4. Wave 5B ZPM **Phase B** (ORG-0005 OWNS DOM-ZPM-01) requires **E1 registrar/registrant evidence** — **not** inferred from REL-ZPM-WB-04.
5. `www.bzpm.ru` policy resolved in Wave 5B ZPM — not blocking singleton roster.
6. OPERATES for ORG-0001 remains **SAFE UNKNOWN** — not blocking PRIMARY_DOMAIN.

---

## 15. Population attestation verdict (pre-execution)

```text
WAVE 5 ZPM DOMAIN POPULATION — DOCUMENTED
1 / 1 Domain entity ready for steward attestation
0 Domain relationships created (Wave 5B ZPM queue: 1 PRIMARY_DOMAIN + proposed domain OWNS)
Wave 5B ZPM Domain relationship population — READY TO START (after Domain attestation act)
```

---

## 16. Package lineage

```text
Wave 1B BZPM (ORG-0005) ──► AT-W1B-01 (COMPLETE)
        │
        ├── Wave 2/2B ZPM Person ──► AT-W2-ZPM-01..02 / AT-W2B-ZPM-01..02 (COMPLETE)
        │
        ├── Wave 3/3B ZPM Project ──► AT-W3-ZPM-01..02 / AT-W3B-ZPM-01..02 (COMPLETE)
        │
        ├── ZPM Website Model Correction ──► COR-ZPM-WEB-01..12 (EXECUTED)
        │
        ├── Wave 4 ZPM Website (WEB-ZPM-01) ──► AT-W4-ZPM-01 (COMPLETE)
        │
        ├── Wave 4B ZPM Website Relationship ──► AT-W4B-ZPM-01..02 (COMPLETE)
        │
        └── Wave 5 ZPM Domain Population (DOM-ZPM-01) ──► THIS PACKAGE
                    │
                    └──► AT-W5-ZPM-01 Domain attestation (NEXT)
                              │
                              └──► Wave 5B ZPM Domain relationships (AFTER)
```

---

## 17. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) | Domain roster |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Prerequisite wave |
| [ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md) | Core Triumph Wave 5 precedent |
| [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](../foundation/ATLAS-POPULATION-READINESS-CHECKLIST-v1.md) | W5 check IDs |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | EV-W1B-CC-01 evidence path |

---

*ATLAS Wave 5 ZPM Domain Attestation v1 — documentation only; population phase — attestation act pending AT-W5-ZPM-01.*
