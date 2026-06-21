# ATLAS Wave 5 SIBCAR Domain Attestation v1

**Status:** **documented** — Wave 5 SIBCAR Domain attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR**  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md) · [ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md) · [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** attestation runtime, signature platform, relationship attestation, Wave 5B SIBCAR execution, DNS automation, Domain attestation act *(pending steward execution)*.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Organization ORG-0006: **active** — AT-W1C-01
- Wave 6B Commercial REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF**: **active** — AT-W6B-02
- Wave 3 SIBCAR Project PRJ-0011: **attested** — AT-W3-SIBCAR-01
- Wave 3B SIBCAR Project ↔ Organization: **COMPLETE** — AT-W3B-SIBCAR-01
- Wave 4 SIBCAR Website attestation: **COMPLETE** — AT-W4-SIBCAR-01 (WEB-SIBCAR-01 **active**)
- Wave 4B SIBCAR Website Relationships: **COMPLETE** — AT-W4B-SIBCAR-01..02
- Population verdict: **READY FOR WAVE 5 SIBCAR DOMAIN POPULATION**

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 5 SIBCAR Domain, минимальные evidence gates, readiness по TEST hostname anchor, missing evidence, candidate relationships для Wave 5B SIBCAR, **ownership neutrality**, duplicate review, **SAFE UNKNOWN** inventory, и **итоговый verdict** пакета.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

---

## 2. Wave 5 SIBCAR attestation scope

| In scope | Out of scope |
|----------|--------------|
| Domain entity → **proposed** / **active** / **deprecated** | PRIMARY_DOMAIN Domain → Website |
| Evidence tier assignment per domain | OWNS / CUSTODIAN Organization → Domain |
| Lifecycle structural state (no DNS/registrar ops vocabulary) | SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO |
| Org/website **candidate** context (display only) | Website → Domain edges *(except future 5B)* |
| Environment **TEST** — deployment identity | OPERATES Organization → Website |
| Registrar status = **SAFE UNKNOWN** unless E1 registrar evidence | CLIENT_OF Organization ↔ Organization |
| Wave 5B SIBCAR **queue preparation** | Person ↔ Domain edges |
| Singleton `sibcar.new-site.space` — DOM-SIBCAR-01 only | Foundation amendments |
| Ownership neutrality — no registrant inference | DNS / registrar API modeling |
| Production domain deferral (ME-W1C-02) | Production DOM-* mint |

Wave 5B SIBCAR relationship **active** attestation executes in a **separate pass** after Domain endpoint is **active**.

---

## 3. Domain roster (attestation view)

| domain_id | canonical_name | environment | lifecycle_state | lifecycle_target | evidence_tier | attestation_readiness |
|-----------|----------------|-------------|-----------------|------------------|---------------|----------------------|
| **DOM-SIBCAR-01** | sibcar.new-site.space | **TEST** | **proposed** | **active** | **E0** | **ready** |

**Readiness legend:**

- **Ready** — steward may attest Domain to target lifecycle state now.
- Domain **OWNS** and PRIMARY_DOMAIN remain **Wave 5B SIBCAR** — not blockers for Wave 5 entity attestation.

---

## 4. Lifecycle analysis

| Rule | Application |
|------|-------------|
| TEST deployment hostname with attested Website → target **active** | DOM-SIBCAR-01 — WEB-SIBCAR-01 **active** (AT-W4-SIBCAR-01) |
| Population state **proposed** | Pending AT-W5-SIBCAR-01 steward act |
| Production corporate domain | **Not minted** — ME-W1C-02 |
| DNS / registrar ops vocabulary | **Excluded** from lifecycle fields |
| TEST posture unchanged by Domain mint | `environment` **TEST**; `hosting_subdomain` class |

**Layer crosswalk at attestation:**

```text
ORG-0006 SIBCAR [active]
    └── OWNS (REL-SIBCAR-WB-02) [active]
        ▼
WEB-SIBCAR-01 sibcar.new-site.space [active · test_deployment · TEST]
    └── BELONGS_TO (REL-SIBCAR-WB-01) [active]
        ▼
PRJ-0011 [active]

DOM-SIBCAR-01 sibcar.new-site.space [proposed → active]  ← THIS WAVE (entity only)
    └── PRIMARY_DOMAIN → WEB-SIBCAR-01  [queued Wave 5B — NOT CREATED]
```

---

## 5. Evidence basis

| Ref | Tier | Role | Domain attestation use |
|-----|------|------|------------------------|
| Operator-approved roster | intake | DOM-SIBCAR-01 mint authority | **Yes** |
| **EV-W1C-02** | E0 | OCPilot SITE-001; TEST URL | **Yes** — not registrant |
| **EV-W1C-03** | E0 | project-access-brief; same TEST URL | Context |
| **EV-OCP-01..04** | E0 | Engagement corroboration | Context |
| **EV-W1C-CC-01** | E1 | Org anchor only — **no** website field | Org endpoint — not domain registrant |
| **AT-W4-SIBCAR-01** | attestation | WEB-SIBCAR-01 **active** | **Yes** |
| **AT-W4B-SIBCAR-01..02** | attestation | Website graph complete | Prerequisite — not domain OWNS basis |
| **AT-W1C-01** | attestation | ORG-0006 **active** | Org endpoint — not domain registrant |
| **AT-W3-SIBCAR-01** | attestation | PRJ-0011 **active** | Project context only |

**Explicitly excluded as domain registrant evidence:**

| Ref | Reason |
|-----|--------|
| REL-SIBCAR-WB-02 Website OWNS | Website property ≠ domain registrant |
| PRJ-0011 lifecycle | Project layer |
| EV-W1C-CC-01 alone | No website field — ME-W1C-05 |
| Operator assumption ORG-0006 owns domain | Not attested without registrar E1 |
| REL-0041 CLIENT_OF | Commercial edge — not domain ownership |

**Primary evidence paths:**

```text
E0 OCPilot — EV-W1C-02 (SITE-001; TEST URL https://sibcar.new-site.space/)
E0 OCPilot — EV-W1C-03 (PRJ-0011 Business Goal + Planned Work)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx (org anchor only)
Attestation — AT-W4-SIBCAR-01 (WEB-SIBCAR-01 active)
```

---

## 6. Ownership neutrality review

| Topic | Attestation posture |
|-------|---------------------|
| Current registrar | **SAFE UNKNOWN** — steward records; no inference |
| Current registrant | **SAFE UNKNOWN** — steward records; no inference |
| `new-site.space` parent zone operator | **SAFE UNKNOWN** — SU-W5-SIBCAR-01 |
| ORG-0006 on `primary_org_candidate` | **Display context only — not attested** |
| REL-SIBCAR-WB-02 | Website-family edge — **does not** promote to domain OWNS in this act |
| Production corporate domain registrant | **SAFE UNKNOWN** — ME-W1C-02 |
| TEST subdomain registrant ORG-0006 | **SAFE UNKNOWN** — SU-W4-SIBCAR-02 |

**Distinction (enforced):**

```text
REL-SIBCAR-WB-02  ORG-0006 ──OWNS──► WEB-SIBCAR-01     [attested Wave 4B — website property]
(queued 5B)       DOM-SIBCAR-01 ──PRIMARY_DOMAIN──► WEB-SIBCAR-01  [NOT created in Wave 5]
(future only)     ORG-0006 ──OWNS──► DOM-SIBCAR-01     [requires E1 registrar — NOT in approved 5B queue]
```

---

## 7. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **SIBCAR-DOM-D-01** | DOM-SIBCAR-01 vs WEB-SIBCAR-01 | **Class boundary** — parallel identities | No |
| **SIBCAR-DOM-D-04** | vs DOM-ZPM-01 | **Distinct** | No |
| **SIBCAR-DOM-D-05** | vs DOM-0001..0004 | **Distinct** | No |
| **SIBCAR-DOM-D-06** | vs production domain | **Blocked** — not minted | No |
| **SIBCAR-DOM-D-08** | Singleton TEST hostname | **Pass** | No |

**Verdict:** **Pass** — no hostname conflicts; production candidate excluded.

---

## 8. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact |
|----|-------|----------|-------------|
| **SU-SIBCAR-PRJ-01** | Production public URL | Medium | Production DOM-* deferred |
| **ME-W1C-02** | Production public URL | Medium | No production Domain minted |
| **ME-W1C-05** | Corporate domain not on CC | Low | E0 OCPilot path used |
| **SU-W4-SIBCAR-02** | TEST subdomain registrant | Low | Ownership neutrality — non-blocking |
| **SU-W4-SIBCAR-01** | Live URL probe | Low | E0 sufficient |
| **SU-W5-SIBCAR-01** | `new-site.space` parent zone registrant | Low | Not modeled |
| **SU-W5-SIBCAR-02** | ORG-0001 OPERATES on TEST property | Low | Not blocking Domain entity |
| **W1C-D-05** | Display alias disambiguation | Low | Non-blocking |
| **EV-OCP-GAP-01** | Credential channel | Low | Cross-program |

**Missing evidence (non-blocking for Wave 5 SIBCAR entity attestation):**

| ID | Gap | Severity | Wave impact |
|----|-----|----------|-------------|
| **ME-W5-SIBCAR-01** | Registrar WHOIS / registrant export | Medium for domain OWNS | Not in approved 5B queue |
| **ME-W5-SIBCAR-02** | PRIMARY_DOMAIN not minted | Low | Wave 5B SIBCAR by design |
| **ME-W5-SIBCAR-03** | Production corporate domain unknown | Medium | Deferred — ME-W1C-02 |
| **ME-W5-SIBCAR-04** | No CC website field | Low | E0 OCPilot sufficient |

**Blocking gaps remaining:** **None**

---

## 9. Wave 5B queue

| Draft candidate | source | target | Type | Evidence gate | Create in Wave 5? |
|-----------------|--------|--------|------|---------------|-------------------|
| *(TBD rel_id)* | DOM-SIBCAR-01 sibcar.new-site.space | WEB-SIBCAR-01 | **PRIMARY_DOMAIN** | DOM-SIBCAR-01 **active** + WEB-SIBCAR-01 **active** | **No** — queue only |

**Not in Wave 5B candidate roster (operator-approved):**

| Item | Treatment |
|------|-----------|
| OWNS ORG-0006 → DOM-SIBCAR-01 | **Excluded** — no registrar E1 |
| OPERATES ORG-0001 → WEB-SIBCAR-01 | **Excluded** — SAFE UNKNOWN |
| CLIENT_OF ORG-0006 → ORG-0001 | **Excluded** — REL-0041 already attested |
| Person ↔ Domain | **Excluded** |
| Production DOM-* | **Excluded** — ME-W1C-02 |
| SECONDARY_DOMAIN / REDIRECTS_TO | **Excluded** — no secondary hostname |

---

## 10. Attestation sequence

### 10.1 Tranche AT-W5-SIBCAR-01 — SIBCAR TEST hostname

| Step | Action | Attestor | Evidence ref |
|------|--------|----------|--------------|
| 1 | Verify WEB-SIBCAR-01 **active** (Wave 4 SIBCAR) | Steward | AT-W4-SIBCAR-01 |
| 2 | Verify Wave 4B SIBCAR complete — REL-SIBCAR-WB-01/02 **active** | Steward | AT-W4B-SIBCAR-01..02 |
| 3 | Confirm REL-SIBCAR-WB-02 Website OWNS **does not** substitute domain registrant | Steward | Population §6 |
| 4 | Propose DOM-SIBCAR-01 canonical name **sibcar.new-site.space** | Steward | Operator roster + EV-W1C-02 |
| 5 | Confirm singleton model — no production DOM-* | Steward | ME-W1C-02 |
| 6 | Assign **E0**; set environment **TEST**; hostname_class **hosting_subdomain** | Steward | EV-W1C-02..03 |
| 7 | Record ownership **context only — not attested** for ORG-0006 | Steward | Population §6 |
| 8 | Set registrar status **SAFE UNKNOWN** | Steward | No registrar export; ME-W1C-05 |
| 9 | Confirm no duplicate `sibcar.new-site.space` DOM-* in core / ZPM registers | Steward | Register §9 |
| 10 | Attest Domain **proposed** → **active** | Steward (delegated) or Owner | W5-SIBCAR-LC-01 |
| 11 | Queue 5B SIBCAR: PRIMARY_DOMAIN → WEB-SIBCAR-01 | Steward | Population §9 |

**Not executed in this tranche (by scope restriction):**

| Step | Action | Reason |
|------|--------|--------|
| Create PRIMARY_DOMAIN edge | **Excluded** | Wave 5B SIBCAR — separate pass |
| Create OWNS Org → Domain edge | **Excluded** | Not in approved queue; no registrar E1 |
| Create OPERATES edge | **Excluded** | SAFE UNKNOWN |
| Re-attest REL-0041 CLIENT_OF | **Excluded** | Already attested Wave 6B |
| Mint production DOM-* | **Blocked** | ME-W1C-02 |
| Create Person ↔ Domain edges | **Excluded** | Operator scope |

---

## 11. Evidence gates

| Gate | Requirement | Wave 5 SIBCAR outcome |
|------|-------------|----------------------|
| **EG-W5-SIBCAR-01** | TEST hostname string attested (FQDN) | **Pass** — DOM-SIBCAR-01 |
| **EG-W5-SIBCAR-02** | Minimum E0 for TEST deployment hostname | **Pass** — EV-W1C-02..03 |
| **EG-W5-SIBCAR-03** | Matching Website **active** | **Pass** — WEB-SIBCAR-01 |
| **EG-W5-SIBCAR-04** | No DNS record modeling in entity fields | **Pass** |
| **EG-W5-SIBCAR-05** | Registrar/registrant E1 for domain OWNS | **Not required** — OWNS not in approved 5B queue |
| **EG-W5-SIBCAR-06** | Single-domain model — one DOM per TEST hostname | **Pass** |
| **EG-W5-SIBCAR-07** | No registrant inference from Website OWNS / CC / Project | **Pass** — ownership neutrality |
| **EG-W5-SIBCAR-08** | TEST posture — not production domain assumption | **Pass** |
| **EG-W5-SIBCAR-09** | No PRIMARY_DOMAIN / OWNS Domain / OPERATES / CLIENT_OF created | **Pass** |
| **EG-W5-SIBCAR-10** | Duplicate review complete | **Pass** — SIBCAR-DOM-D-01..09 |

---

## 12. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PRIMARY_DOMAIN DOM-SIBCAR-01 → WEB-SIBCAR-01 | **Excluded** — Wave 5B SIBCAR *(queued)* |
| OWNS / CUSTODIAN Org/Person → Domain | **Excluded** — not in approved 5B queue |
| SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Excluded** |
| OPERATES ORG-0001 → WEB-SIBCAR-01 | **Excluded** — SAFE UNKNOWN |
| CLIENT_OF ORG-0006 → ORG-0001 | **Excluded** — REL-0041 already attested Wave 6B |
| Person ↔ Domain | **Excluded** |
| DNS A/CNAME/MX/TXT modeling | **Excluded** |
| Registrar API integration | **Excluded** |
| Production DOM-* | **Excluded** — ME-W1C-02 |
| Infer registrant from Website OWNS / CC / Project | **Excluded** |
| Foundation documents | **Not modified** |

---

## 13. Foundation consistency review

| Foundation doc | Attestation alignment |
|----------------|----------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5 | Domain = hostname anchor — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | One id per hostname; production not assumed — **Pass** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.5 | TEST hostname policy documented — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Domain **proposed** → **active** — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5 | E0 TEST path — **Pass** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | DOM may exist; domain OWNS UNKNOWN — **Pass** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) Wave 5 | Ordering after Website 4B — **Pass** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7–9 | Families documented — edges not created — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation path — **Pass** |
| [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | No registrant inference — **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | WEB-SIBCAR-01 attested **active** | **Pass** |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Website-family graph complete | **Pass** |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 **active** | **Pass** |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | No `sibcar.new-site.space` duplicate | **Pass** |
| [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md) | ZPM tranche structural precedent | **Pass** |

**Foundation modified:** **No**  
**Wave 1C / 3 / 3B / 4 / 4B SIBCAR modified:** **No**  
**Core Wave 5 Triumph modified:** **No**  
**ZPM Wave 5 modified:** **No**  
**New entity types:** **No**  
**Domain relationships created:** **No**  
**Domain attestation act executed:** **No** — pending AT-W5-SIBCAR-01

---

## 14. Readiness verdict

### 14.1 Wave 5 SIBCAR Domain attestation readiness

| Criterion | Status |
|-----------|--------|
| Wave 5 SIBCAR Domain population documented (DOM-SIBCAR-01) | **Pass** |
| Singleton TEST hostname entity | **Pass** |
| Target lifecycle **active** | **Pass** |
| Matching WEB-SIBCAR-01 **active** | **Pass** |
| Environment **TEST** declared | **Pass** |
| PRIMARY_DOMAIN candidate documented (1) — queue only | **Pass** |
| No premature Domain relationships | **Pass** |
| Registrar posture SAFE UNKNOWN documented | **Pass** |
| Ownership neutrality — no registrant inference | **Pass** |
| No DNS-level modeling | **Pass** |
| No production domain assumption | **Pass** |
| No duplicate hostname with core / ZPM registers | **Pass** |
| Foundation unchanged | **Pass** |

### 14.2 Verdict options

| Verdict | Meaning |
|---------|---------|
| **NOT READY** | Domain intake cannot proceed to attestation |
| **PARTIALLY READY** | Subset only — **not applicable** (singleton roster) |
| **READY FOR WAVE 5 SIBCAR DOMAIN ATTESTATION** | Population complete; steward attestation act may proceed |
| **READY FOR WAVE 5B SIBCAR DOMAIN RELATIONSHIP POPULATION** | *(after attestation act)* Domain entity **active** |

### 14.3 Verdict (population phase — this document)

```text
READY FOR WAVE 5 SIBCAR DOMAIN ATTESTATION
```

**Conditions:**

1. Steward executes attestation tranche **AT-W5-SIBCAR-01** to promote DOM-SIBCAR-01 from population draft (**proposed**) to canonical **active**.
2. After attestation act, verdict upgrades to **READY FOR WAVE 5B SIBCAR DOMAIN RELATIONSHIP POPULATION**.
3. Wave 5B SIBCAR (**PRIMARY_DOMAIN** DOM-SIBCAR-01 → WEB-SIBCAR-01) may proceed **only after** Domain attestation — one PRIMARY_DOMAIN per Website.
4. **No** Organization → Domain OWNS in approved Wave 5B queue — registrar E1 absent.
5. Production corporate domain remains **deferred** until public URL evidence (ME-W1C-02).
6. OPERATES for ORG-0001 remains **SAFE UNKNOWN** — not blocking PRIMARY_DOMAIN queue.
7. REL-0041 CLIENT_OF remains **already attested** — not re-minted.
8. TEST deployment posture maintained — hostname is operator TEST identity; not production registrant proof.

### 14.4 Population attestation verdict (pre-execution)

```text
WAVE 5 SIBCAR DOMAIN POPULATION — DOCUMENTED
1 / 1 Domain entity proposed (DOM-SIBCAR-01) — ready for steward attestation
0 Domain relationships created (Wave 5B SIBCAR queue: 1 PRIMARY_DOMAIN only)
Wave 5B SIBCAR Domain relationship population — READY TO START (after Domain attestation act)
```

---

## 15. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1C SIBCAR (ORG-0006, LE-0005) ──► AT-W1C-01 (COMPLETE)
        │
        ├── Wave 6B Commercial (REL-0041) ──► AT-W6B-02 (COMPLETE)
        │
        ├── Wave 3 SIBCAR Project (PRJ-0011) ──► AT-W3-SIBCAR-01 (COMPLETE)
        │
        ├── Wave 3B SIBCAR Project Relationship (REL-SIBCAR-PJ-01..02) ──► AT-W3B-SIBCAR-01 (COMPLETE)
        │
        ├── Wave 4 SIBCAR Website (WEB-SIBCAR-01 TEST) ──► AT-W4-SIBCAR-01 (COMPLETE)
        │
        ├── Wave 4B SIBCAR Website Relationship (REL-SIBCAR-WB-01..02) ──► AT-W4B-SIBCAR-01..02 (COMPLETE)
        │
        └── Wave 5 SIBCAR Domain Population (DOM-SIBCAR-01) ──► THIS PACKAGE
                    │
                    └──► AT-W5-SIBCAR-01 Domain attestation (NEXT)
                              │
                              └──► Wave 5B SIBCAR PRIMARY_DOMAIN (AFTER)
```

---

## 16. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md) | Domain roster |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Prerequisite wave |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | Website prerequisite |
| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | ORG-0006 active basis |
| [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md) | ZPM tranche precedent |
| [ATLAS-POPULATION-READINESS-CHECKLIST-v1.md](../foundation/ATLAS-POPULATION-READINESS-CHECKLIST-v1.md) | W5 check IDs |

---

*ATLAS Wave 5 SIBCAR Domain Attestation v1 — documentation only; population phase — attestation act pending AT-W5-SIBCAR-01.*
