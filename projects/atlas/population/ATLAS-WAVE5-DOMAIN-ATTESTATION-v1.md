# ATLAS Wave 5 Domain Attestation v1

**Status:** **documented** — Wave 5 Domain attestation sequence, evidence gates, readiness verdict.  
**Attestation authority note (FINDING-INT-03):** Core Triumph Domain lifecycle (DOM-0001..0004) is **active** in population registers and attested as PRIMARY_DOMAIN endpoints in [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md). No standalone `*-ACTIVE-ATTESTATION-v1.md` was filed for this tranche. **SAFE UNKNOWN:** whether discrete steward acts AT-W5-01..04 were executed as separate human steps before Wave 5B — not separately documented.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) · [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md)  
**Is not:** attestation runtime, signature platform, relationship attestation, Wave 5B execution, DNS automation.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Wave 4B Website Relationships: **COMPLETE**
- Population verdict: **READY FOR WAVE 5 DOMAIN POPULATION**

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 5 Domain, минимальные evidence gates, readiness по каждому hostname, missing evidence, candidate relationships для Wave 5B, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 5 attestation scope

| In scope | Out of scope |
|----------|--------------|
| Domain entity → **proposed** / **active** / **deprecated** | PRIMARY_DOMAIN Domain → Website |
| Evidence tier assignment per domain | OWNS / CUSTODIAN Organization → Domain |
| Lifecycle structural state (no DNS/registrar ops vocabulary) | SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO |
| Org/website **candidate** context (display) | Website → Domain edges |
| Registrar status = **SAFE UNKNOWN** unless E1 registrar evidence | Person → Domain |
| Wave 5B **queue preparation** | Foundation amendments |
| Operator org domains | Separate future tranche |
| `www.gktriumph.ru` hostname policy | Wave 5B steward decision |

Wave 5B relationship **active** attestation executes in a **separate pass** after Domain endpoints are **active**.

---

## 3. Attestation readiness by domain

| domain_id | Domain | Target state | Min tier | Readiness | Blocker |
|-----------|--------|--------------|----------|-----------|---------|
| DOM-0001 | gktriumph.ru | **active** | E1 | **Ready** | — |
| DOM-0002 | blog.gktriumph.ru | **active** | E1 | **Ready** | — |
| DOM-0003 | gruzotaxi-triumph.ru | **active** | E1 | **Ready** | — |
| DOM-0004 | manipulator-triumph.ru | **active** | E1 | **Ready** | — |

**Readiness legend:**

- **Ready** — steward may attest Domain to target lifecycle state now.
- All four domains: **Ready** — no conditional blockers for **entity** attestation.
- Domain **OWNS** and PRIMARY_DOMAIN remain **Wave 5B** — not blockers for Wave 5 entity attestation.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W5-01 — Main corporate apex

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify WEB-0006 **active** (Wave 4) | Steward | Wave 4 attestation |
| 2 | Verify REL-0032 ORG-0004 **OWNS** WEB-0006 (Wave 4B) | Steward | Wave 4B register |
| 3 | Propose DOM-0001 canonical name **gktriumph.ru** | Steward | Operator roster + live URL |
| 4 | Confirm separate entity from DOM-0002 (subdomain rule) | Steward | Population §3.2 |
| 5 | Assign E1; record ownership **candidate** ORG-0004 (indirect) | Steward | Population §3.1 |
| 6 | Set registrar status **SAFE UNKNOWN** | Steward | No registrar export in repo |
| 7 | Attest Domain **active** | Steward (delegated) or Owner | W5-LC-01 |
| 8 | Queue 5B: PRIMARY_DOMAIN → WEB-0006; www policy | Steward | Population §6 |

### 4.2 Tranche AT-W5-02 — Blog subdomain FQDN

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify WEB-0007 **active** | Steward | Wave 4 register |
| 2 | Propose DOM-0002 canonical name **blog.gktriumph.ru** | Steward | Operator roster + live URL |
| 3 | Confirm **not** merged into DOM-0001 | Steward | Operator modeling rule |
| 4 | Assign E1; indirect ownership candidate | Steward | REL-0033 context |
| 5 | Registrar **SAFE UNKNOWN** | Steward | — |
| 6 | Attest Domain **active** | Steward | W5-LC-01 |
| 7 | Queue 5B: PRIMARY_DOMAIN → WEB-0007 | Steward | Population §6.1 |

### 4.3 Tranche AT-W5-03 — Gruzotaxi landing apex

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify WEB-0008 **active**; REL-0030, REL-0034 | Steward | Wave 4/4B registers |
| 2 | Propose DOM-0003 canonical name **gruzotaxi-triumph.ru** | Steward | Operator roster + live URL |
| 3 | Assign E1; registrar **SAFE UNKNOWN** | Steward | EV-0005 context only |
| 4 | Attest Domain **active** | Steward | W5-LC-01 |
| 5 | Queue 5B: PRIMARY_DOMAIN → WEB-0008 | Steward | — |

### 4.4 Tranche AT-W5-04 — Manipulator landing apex

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify WEB-0009 **active**; REL-0031, REL-0035 | Steward | Wave 4/4B registers |
| 2 | Propose DOM-0004 canonical name **manipulator-triumph.ru** | Steward | Operator roster + live URL |
| 3 | Assign E1; registrar **SAFE UNKNOWN** | Steward | — |
| 4 | Attest Domain **active** | Steward | W5-LC-01 |
| 5 | Queue 5B: PRIMARY_DOMAIN → WEB-0009 | Steward | — |

---

## 5. Evidence gates

| Gate | Requirement | Wave 5 outcome |
|------|-------------|----------------|
| **EG-W5-01** | Hostname string attested (FQDN) | **Pass** — all four |
| **EG-W5-02** | Minimum E1 for operator primary domain ([ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5) | **Pass** — live URL + roster |
| **EG-W5-03** | Matching Website **active** (typical case) | **Pass** — WEB-0006..0009 |
| **EG-W5-04** | No DNS record modeling in entity fields | **Pass** |
| **EG-W5-05** | Registrar/registrant E1 for domain OWNS | **Not required** for Wave 5 entity attestation — deferred Wave 5B |
| **EG-W5-06** | Subdomain = separate Domain (operator rule) | **Pass** — DOM-0002 |

---

## 6. Missing evidence (non-blocking for Wave 5 entity attestation)

| ID | Gap | Severity | Wave impact |
|----|-----|----------|-------------|
| **ME-W5-01** | Registrar WHOIS / registrant export for DOM-0001..0004 | Medium for domain OWNS | Wave 5B — blocks **active** ORG→Domain OWNS, not Domain entity |
| **ME-W5-02** | `www.gktriumph.ru` hostname policy | Low | Wave 5B SECONDARY_DOMAIN or new DOM |
| **ME-W5-03** | Expiry date metadata (optional) | Low | Future optional field |
| **ME-W5-04** | ORG-0001 CUSTODIAN/OPERATES on domains | Low | SAFE UNKNOWN — SU-W4B-01 carries |

---

## 7. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PRIMARY_DOMAIN DOM → WEB | **Excluded** — Wave 5B |
| OWNS / CUSTODIAN Org/Person → Domain | **Excluded** — Wave 5B |
| SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Excluded** — Wave 5B |
| Website → Domain | **Excluded** — Wave 5B |
| DNS A/CNAME/MX/TXT modeling | **Excluded** — out of ATLAS scope |
| Registrar API integration | **Excluded** — no implementation |
| Collapsing blog subdomain into apex Domain | **Excluded** — rejected |

---

## 8. Foundation consistency check

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5 | Domain = hostname anchor — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | One id per hostname; www not assumed — **Pass** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.5 | Punycode/www policy — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Domain **active** state — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5 | E1 at active — **Pass** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | DOM may exist; domain OWNS UNKNOWN — **Pass** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) Wave 5 | Ordering after Website — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7–9 | Families documented — edges not created — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation path — **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md) | WEB-0006..0009 attested **active** | **Pass** |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Website-family graph complete | **Pass** |
| Wave 1 Organization attestation | ORG-0004 **active** | **Pass** |

**Foundation modified:** **No**  
**Wave 1–4B modified:** **No**  
**New entity types:** **No**  
**Domain relationships created:** **No**

---

## 9. Remaining SAFE UNKNOWN items

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-W5-01** | Domain registrant / registrar account for DOM-0001..0004 | Medium | Blocks Wave 5B **active** domain OWNS — not Domain entity |
| **SU-W5-02** | `www.gktriumph.ru` — separate DOM vs alias edge | Low | Wave 5B hostname policy |
| **SU-W5-03** | ORG-0001 technical custodian on DNS | Low | Not blocking PRIMARY_DOMAIN |
| **SU-W5-04** | Distinction Website OWNS vs Domain OWNS (SU-W4B-06) | **Resolved at population** — separate edge families |

---

## 10. Wave 5B readiness assessment

### 10.1 Criteria

| Criterion | Status |
|-----------|--------|
| Wave 5 Domain population documented (DOM-0001..0004) | **Pass** |
| All four hostnames independent entities | **Pass** |
| All four target lifecycle **active** | **Pass** |
| Matching WEB-0006..0009 **active** | **Pass** |
| PRIMARY_DOMAIN candidates documented (4) | **Pass** |
| No premature Domain relationships | **Pass** |
| Registrar posture SAFE UNKNOWN documented | **Pass** |
| No DNS-level modeling | **Pass** |
| Foundation unchanged | **Pass** |

### 10.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Domain intake cannot proceed to relationship pass |
| **PARTIALLY READY** | Wave 5B may start for subset only |
| **READY FOR WAVE 5B DOMAIN RELATIONSHIP POPULATION** | Domain entities ready; relationship pass may proceed |

### 10.3 Verdict

```text
READY FOR WAVE 5B DOMAIN RELATIONSHIP POPULATION
```

**Conditions:**

1. Steward executes attestation tranches AT-W5-01..04 to promote four domains from population draft to canonical **active** before Wave 5B **active** relationship promotion.
2. Wave 5B **Phase A** (PRIMARY_DOMAIN DOM → WEB) may proceed after Domain attestation act — one PRIMARY_DOMAIN per Website.
3. Wave 5B **Phase B** (ORG-0004 OWNS DOM-*) requires **E1 registrar/registrant evidence** — **not** inferred from Website OWNS alone.
4. `www.gktriumph.ru` policy resolved in Wave 5B — not blocking four-domain roster.
5. OPERATES / CUSTODIAN for ORG-0001 remains **SAFE UNKNOWN** — not blocking PRIMARY_DOMAIN.
6. Draft dataset flags **do not substitute** for steward attestation acts.

---

## 11. Population attestation verdict (pre-execution)

```text
WAVE 5 DOMAIN POPULATION — DOCUMENTED
4 / 4 Domain entities ready for steward attestation
0 Domain relationships created (Wave 5B queue: 4 PRIMARY_DOMAIN + proposed domain OWNS)
Wave 5B Domain relationship population — READY TO START (after Domain attestation act)
```

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | Domain roster |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Prerequisite wave |
| [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](../foundation/ATLAS-POPULATION-READINESS-CHECKLIST-v1.md) | W5 check IDs |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | EV-0005 evidence path |
