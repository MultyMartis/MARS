# ATLAS Wave 5 ZPM Domain Active Attestation v1

**Status:** **attested** — first official Domain active attestation for Wave 5 ZPM tranche (ORG-0005).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) · [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) · [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md) · [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, database export, Wave 5B ZPM relationship attestation, DNS operations, registrar integration, Foundation amendment.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Projects PRJ-0009, PRJ-0010: **attested** — AT-W3-ZPM-01..02
- Wave 3B ZPM Project ↔ Organization: **COMPLETE** — AT-W3B-ZPM-01..02
- Wave 4 ZPM Website attestation: **COMPLETE** — AT-W4-ZPM-01 (WEB-ZPM-01 **active**)
- Wave 4B ZPM Website Relationships: **COMPLETE** — AT-W4B-ZPM-01..02 (REL-ZPM-WB-01/03/04 **active**)
- ZPM Website Model Correction: **EXECUTED** — COR-ZPM-WEB-01..12
- Wave 5 ZPM Domain attestation plan verdict: **READY FOR WAVE 5 ZPM DOMAIN ATTESTATION**

---

# REPORT — ATLAS Wave 5 ZPM Domain Active Attestation

**Attestation date:** 2026-06-07  
**Tranche:** **AT-W5-ZPM-01**  
**Promotion:** DOM-ZPM-01 — **proposed** → **active**

---

## 1. Attestation result

| domain_id | canonical_name | prior state | attested state | evidence_tier | tranche | result |
|-----------|----------------|-------------|----------------|---------------|---------|--------|
| **DOM-ZPM-01** | bzpm.ru | **proposed** | **active** | **E1** | AT-W5-ZPM-01 | **Attested** |

**Promotion count:** **1 / 1** Domain record attested  
**Active promoted:** **1** (DOM-ZPM-01)  
**Deprecated Domain promoted:** **0**  
**Relationships created:** **0**  
**Website entities modified:** **0**

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1): steward attestation under documented evidence discipline — **satisfied** for DOM-ZPM-01.

**Binding operator discipline (enforced):**

- **DOM-ZPM-01** — approved roster only; singleton apex hostname anchor for `bzpm.ru`.
- **Single-domain model** — one Domain entity; no dual-generation DOM-* for retired WEB-ZPM-02 (COR-ZPM-WEB-10).
- **Registrar / registrant** — **SAFE UNKNOWN**; not inferred from REL-ZPM-WB-04 Website OWNS, CC §17, or Project context.
- **No** PRIMARY_DOMAIN, OWNS, OPERATES, SECONDARY_DOMAIN, REDIRECTS_TO, POINTS_TO, CLIENT_OF, Person, or Organization structural edges in this act.

---

## 2. Pre-check — evidence inventory (mandatory)

**Governance:** [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01 · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-01..06.

**Folder verified:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` — **exists**.

| # | Ref | Source | Tier | Role |
|---|-----|--------|------|------|
| 1 | **Operator-approved roster** | DOM-ZPM-01 `bzpm.ru` | intake | Primary mint authority |
| 2 | **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` §17 **Bzpm.ru** | **E1** | Hostname string corroboration — **not** registrant proof |
| 3 | **EV-ZPM-OP-ACT-01** | Operator — current catalog rebuild | **E0** | Ongoing client property context |
| 4 | **AT-W4-ZPM-01** | [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | attestation | WEB-ZPM-01 **active** — co-terminous endpoint |
| 5 | **AT-W4B-ZPM-01..02** | [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | attestation | Website-family graph complete — **not** domain OWNS basis |
| 6 | **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0005 **active** — org endpoint only |
| 7 | **COR-ZPM-WEB-10** | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | correction | Singleton DOM model |

**Inventory verdict:**

| Check | Result |
|-------|--------|
| Operator roster recorded | **Pass** — DOM-ZPM-01 singleton |
| CC inventory cited (reuse AT-W1B-01) | **Pass** — EV-W1B-CC-01 §17 hostname string |
| WEB-ZPM-01 endpoint **active** | **Pass** — AT-W4-ZPM-01 |
| Wave 4B ZPM Website graph complete | **Pass** — AT-W4B-ZPM-01..02 |
| REL-ZPM-WB-04 Website OWNS **not** used as domain registrant proof | **Pass** — ownership neutrality |
| EFV-06 registrar posture SAFE UNKNOWN | **Pass** — no registrar export in package |
| Singleton DOM model (COR-ZPM-WEB-10) | **Pass** — no second DOM for PRJ-0010 |

**Primary evidence paths:**

```text
E1 CC hostname — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx §17 Bzpm.ru (string only — not registrant)
E0 operator — EV-ZPM-OP-ACT-01 (property context)
Attestation — AT-W4-ZPM-01 (WEB-ZPM-01 active)
```

---

## 3. Prerequisite endpoint verification

| Endpoint | Required state | Source act | Verified |
|----------|----------------|------------|----------|
| **ORG-0005** ЗПМ | **active** | AT-W1B-01 | **Pass** |
| **WEB-ZPM-01** bzpm.ru | **active** | AT-W4-ZPM-01 | **Pass** |
| **PRJ-0009** | **active** | AT-W3-ZPM-01 | **Pass** |
| **PRJ-0010** | **deprecated** | AT-W3-ZPM-02 | **Pass** |
| **REL-ZPM-WB-01, REL-ZPM-WB-03, REL-ZPM-WB-04** | **active** | AT-W4B-ZPM-01..02 | **Pass** |

**Verdict:** **Pass** — all prerequisite endpoints attested before Domain promotion.

---

## 4. Duplicate and hostname uniqueness review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **ZPM-DOM-D-01** | DOM-ZPM-01 vs second DOM for PRJ-0010 / WEB-ZPM-02 | **Fail** — second DOM rejected | No *(resolved — COR-ZPM-WEB-10)* |
| **ZPM-DOM-D-02** | vs co-terminous WEB-ZPM-01 | **Not duplicate** — parallel identity classes | No |
| **ZPM-DOM-D-03** | vs core Wave 5 DOM-0001..0004 (Triumph) | **Distinct org** ORG-0005 vs ORG-0004 | No |
| **ZPM-DOM-D-04** | `bzpm.ru` hostname uniqueness across all DOM-* | **Pass** — no existing DOM for apex | No |
| **ZPM-DOM-D-05** | `www.bzpm.ru` collapsed into DOM-ZPM-01 | **Not assumed** — EIR-D02; deferred Wave 5B | No |
| **ZPM-DOM-D-06** | DOM-ZPM-* vs DOM-000* namespace | **Pass** — tranche separation | No |

**Hostname conflict cross-check:**

| Hostname | domain_id | org anchor | Conflict |
|----------|-----------|------------|----------|
| `gktriumph.ru` | DOM-0001 *(Triumph)* | ORG-0004 | **None** — distinct client |
| `blog.gktriumph.ru` | DOM-0002 *(Triumph)* | ORG-0004 | **None** |
| `gruzotaxi-triumph.ru` | DOM-0003 *(Triumph)* | ORG-0004 | **None** |
| `manipulator-triumph.ru` | DOM-0004 *(Triumph)* | ORG-0004 | **None** |
| `bzpm.ru` | **DOM-ZPM-01** *(this act)* | ORG-0005 ЗПМ | — |
| `bzpm.ru` | *(second DOM)* | — | **Rejected** — COR-ZPM-WEB-10 |

**Verdict:** **Pass** — hostname uniqueness satisfied; no duplicate Domain entities; single-domain model honored.

---

## 5. Verification gates

| Gate ID | Rule | Status |
|---------|------|--------|
| **EG-W5-ZPM-01** | Hostname string attested (FQDN apex `bzpm.ru`) | **Pass** — DOM-ZPM-01 |
| **EG-W5-ZPM-02** | Minimum E1 for operator primary domain | **Pass** — CC §17 + operator roster |
| **EG-W5-ZPM-03** | Matching Website **active** (WEB-ZPM-01) | **Pass** — AT-W4-ZPM-01 |
| **EG-W5-ZPM-04** | No DNS record modeling in entity fields | **Pass** |
| **EG-W5-ZPM-05** | Registrar/registrant E1 for domain OWNS | **Not required** — deferred Wave 5B ZPM |
| **EG-W5-ZPM-06** | Single-domain model — one DOM per `bzpm.ru` | **Pass** — COR-ZPM-WEB-10 |
| **EG-W5-ZPM-07** | No registrant inference from Website OWNS / CC / Project | **Pass** — ownership neutrality |
| **W5-ZPM-VG-01** | Wave ordering — Wave 5 after Wave 4B ZPM | **Pass** |
| **W5-ZPM-VG-02** | Domain taxonomy — hostname anchor only ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5) | **Pass** |
| **W5-ZPM-VG-03** | EIR-D01 one hostname = one Domain | **Pass** |
| **W5-ZPM-VG-04** | No duplicate `bzpm.ru` in core register DOM-0001..0004 | **Pass** |
| **W5-ZPM-VG-05** | Human attest mandatory | **Pass** — this act |
| **W5-ZPM-VG-06** | No relationship edges in this package | **Pass** — scope restriction |
| **W5-ZPM-VG-07** | Registrar posture SAFE UNKNOWN documented | **Pass** |

**Operator-requested validation crosswalk:**

| Check | Result |
|-------|--------|
| AT-W5-ZPM-01 tranche executed | **Pass** |
| Hostname uniqueness | **Pass** — §4 |
| Single-domain model | **Pass** — COR-ZPM-WEB-10 |
| No duplicate DOM entities | **Pass** — singleton roster |
| Wave ordering | **Pass** — 4B ZPM complete before Domain |
| Domain taxonomy | **Pass** — §5 W5-ZPM-VG-02 |
| Ownership neutrality | **Pass** — §7 |
| Registrar SAFE UNKNOWN | **Pass** — §8 |

**Verdict:** **Pass** — all gates satisfied for Domain lifecycle promotion.

---

## 6. Attestation tranche executed

### 6.1 AT-W5-ZPM-01 — ZPM apex hostname

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify WEB-ZPM-01 **active** (Wave 4 ZPM) | Steward | AT-W4-ZPM-01 | **Done** |
| 2 | Verify Wave 4B ZPM complete — REL-ZPM-WB-01/03/04 **active** | Steward | AT-W4B-ZPM-01..02 | **Done** |
| 3 | Confirm REL-ZPM-WB-04 Website OWNS **does not** substitute domain registrant | Steward | Population §6 | **Done** |
| 4 | Propose DOM-ZPM-01 canonical name **bzpm.ru** | Steward | Operator roster + EV-W1B-CC-01 §17 | **Done** |
| 5 | Confirm singleton model — no second DOM for PRJ-0010 / WEB-ZPM-02 | Steward | COR-ZPM-WEB-10 | **Done** |
| 6 | Assign **E1**; record ownership **context only — not attested** for ORG-0005 | Steward | Population §6 | **Done** |
| 7 | Set registrar status **SAFE UNKNOWN** | Steward | No registrar export in repo | **Done** |
| 8 | Confirm no duplicate `bzpm.ru` DOM-* in core register | Steward | [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | **Done** |
| 9 | Duplicate scan ZPM-DOM-D-01..06 | Steward | Register §9 | **Done** |
| 10 | Attest Domain **active** | Steward (delegated) | W5-ZPM-LC-01 | **Done** |
| 11 | Queue 5B ZPM: PRIMARY_DOMAIN → WEB-ZPM-01; www policy | Steward | Population §8 | **Queued** |

**Not executed in this tranche (by scope restriction):**

| Step | Action | Reason |
|------|--------|--------|
| Create PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01 | **Excluded** | Wave 5B ZPM |
| Create OWNS ORG-0005 → DOM-ZPM-01 | **Excluded** | Wave 5B ZPM — registrar E1 gate |
| Create CUSTODIAN / OPERATES edges | **Excluded** | SAFE UNKNOWN |
| Create SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Excluded** | Wave 5B ZPM |
| Create CLIENT_OF ORG-0005 → ORG-0001 | **Excluded** | Wave 6 |
| Create Person ↔ Domain edges | **Excluded** | Operator scope |
| Create Organization ↔ Domain structural edges | **Excluded** | Wave 5B ZPM |
| Mint DOM-* for `www.bzpm.ru` | **Excluded** | Deferred — SU-W4B-ZPM-02 |
| Model DNS / registrar records | **Excluded** | Out of ATLAS scope |

---

## 7. Domain promotion summary

### 7.1 DOM-ZPM-01 — bzpm.ru

| Field | Value |
|-------|-------|
| **domain_id** | DOM-ZPM-01 |
| **canonical_name** | bzpm.ru |
| **hostname_class** | apex |
| **primary_org_candidate** *(display only)* | ORG-0005 ЗПМ |
| **primary_website_candidate** *(display only)* | WEB-ZPM-01 bzpm.ru |
| **attestation_basis** | E1 operator roster + EV-W1B-CC-01 §17 hostname string; WEB-ZPM-01 **active** co-terminous endpoint; singleton model COR-ZPM-WEB-10; duplicate review **Pass** |
| **evidence_tier** | **E1** |
| **ownership confidence** | **context only — not attested** |
| **registrar status** | **SAFE UNKNOWN** |
| **lifecycle_state (prior)** | **proposed** |
| **lifecycle_state (attested)** | **active** |
| **notes** | Parallel identity to WEB-ZPM-01 — not merged. Domain OWNS and PRIMARY_DOMAIN deferred Wave 5B ZPM. `www.bzpm.ru` policy deferred. |

### 7.2 Promotion ledger

| Entity class | id | prior | attested | count |
|--------------|-----|-------|----------|-------|
| Domain | DOM-ZPM-01 | **proposed** | **active** | 1 |
| Website | WEB-ZPM-01 | **active** | **active** *(unchanged)* | — |
| Organization | ORG-0005 | **active** | **active** *(unchanged)* | — |
| Project | PRJ-0009 | **active** | **active** *(unchanged)* | — |
| Project | PRJ-0010 | **deprecated** | **deprecated** *(unchanged)* | — |
| Relationship | REL-ZPM-WB-* | **active** | **active** *(unchanged)* | — |
| Relationship | Domain-family | — | *(not created)* | 0 |

**Distinction (enforced):**

```text
REL-ZPM-WB-04  ORG-0005 ──OWNS──► WEB-ZPM-01     [attested Wave 4B — website property]
(proposed 5B)  ORG-0005 ──OWNS──► DOM-ZPM-01     [requires domain-level E1 — NOT inferred]
(queued 5B)    DOM-ZPM-01 ──PRIMARY_DOMAIN──► WEB-ZPM-01   [after this act]
```

---

## 8. Ownership neutrality review

| Topic | Attestation posture |
|-------|---------------------|
| Current registrar | **SAFE UNKNOWN** — steward records; no inference |
| Current registrant | **SAFE UNKNOWN** — steward records; no inference |
| ORG-0005 on `primary_org_candidate` | **Display context only — not attested** |
| REL-ZPM-WB-04 Website OWNS | Website-family edge — **does not** promote to domain OWNS in this act |
| EV-W1B-CC-01 §17 **Bzpm.ru** | Org card website field — **does not** prove registrar registrant |
| PRJ-0009 / PRJ-0010 commissioning | Project context — **does not** prove domain registrant |
| Wave 5B proposed ORG-0005 → DOM-ZPM-01 OWNS | **Queued** — requires registrar E1 (ME-W5-ZPM-01; SU-ZPM-PRJ-08) |

**Verdict:** **Pass** — ownership neutrality discipline satisfied; no registrant inference in this act.

---

## 9. Explicit exclusions (not attested in this package)

| Item | Treatment |
|------|-----------|
| PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01 | **Queued** — Wave 5B ZPM |
| OWNS / CUSTODIAN Organization → Domain | **Queued** — Wave 5B ZPM |
| SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Queued** — Wave 5B ZPM |
| OPERATES ORG-0001 → WEB-ZPM-01 / DOM-* | **Excluded** — SAFE UNKNOWN |
| CLIENT_OF ORG-0005 → ORG-0001 | **Deferred** — Wave 6 |
| Person ↔ Domain edges | **Not created** |
| Organization ↔ Domain structural edges | **Not created** — Wave 5B ZPM |
| DOM-* for retired WEB-ZPM-02 / PRJ-0010 generation | **Rejected** — COR-ZPM-WEB-10 |
| DNS A/CNAME/MX/TXT modeling | **Excluded** — out of ATLAS scope |
| Registrar API integration | **Excluded** — no implementation |
| Infer registrant from REL-ZPM-WB-04 / CC / Project | **Excluded** — ownership discipline |
| Foundation documents | **Not modified** |

---

## 10. Remaining SAFE UNKNOWN

| ID | Topic | Severity | Wave impact | Status |
|----|-------|----------|-------------|--------|
| **SU-W5-ZPM-01** | Domain registrant / registrar account for DOM-ZPM-01 | Medium | Blocks Wave 5B ZPM **active** domain OWNS — not Domain entity | **Open** |
| **SU-W5-ZPM-02** | `www.bzpm.ru` — separate DOM vs alias edge | Low | Wave 5B ZPM hostname policy | **Open** |
| **SU-W5-ZPM-03** | ORG-0001 technical custodian on DNS | Low | Not blocking PRIMARY_DOMAIN | **Open** |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Low | Wave 5B ZPM domain OWNS gate | **Open** |
| **SU-W4B-ZPM-01** | ORG-0001 OPERATES WEB-ZPM-01 | Low | Not blocking Domain attestation | **Open** |
| **SU-W4-ZPM-01** | Live URL probe for `bzpm.ru` | Low | E0/E1 sufficient via CC + attestation chain | **Unchanged** |
| **SU-W4-ZPM-03** | Single DOM-* vs dual generation | Low | **Resolved** — DOM-ZPM-01 singleton |
| **ME-W5-ZPM-01** | Registrar WHOIS / registrant export | Medium | Wave 5B ZPM domain OWNS | **Expected** |
| **ME-W5-ZPM-02** | `www.bzpm.ru` hostname policy | Low | Wave 5B ZPM | **Expected** |

**Blocking gaps remaining:** **None** for Domain entity **active** attestation.

---

## 11. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** — 1 Domain record attested |
| No Foundation modification | **Pass** |
| No Wave 1 / 2 / 2B / 3 / 3B / 4 / 4B ZPM record modification | **Pass** |
| WEB-ZPM-01 endpoint **active** honored | **Pass** |
| EIR-D01 one hostname = one Domain | **Pass** |
| EIR-D02 www not assumed | **Pass** — `www.bzpm.ru` deferred |
| EFV-06 ownership SAFE UNKNOWN without registrar cite | **Pass** |
| Domain taxonomy — hostname anchor only | **Pass** |
| No relationship edges created | **Pass** |
| Co-terminous WEB-ZPM-01 / DOM-ZPM-01 not merged | **Pass** |
| ATLAS-ATTESTATION-MODEL contract followed | **Pass** |
| Documentation only | **Pass** |

**Cross-population validation:**

| Prior population | Check | Result |
|------------------|-------|--------|
| [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | WEB-ZPM-01 attested **active** | **Pass** |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Website-family graph complete | **Pass** |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | No `bzpm.ru` duplicate | **Pass** |
| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | ORG-0005 **active** | **Pass** |

---

## 12. Readiness verdict

```text
READY FOR WAVE 5B ZPM DOMAIN RELATIONSHIP POPULATION
```

**Conditions met:**

1. DOM-ZPM-01 **active** — sole ZPM apex hostname anchor for `bzpm.ru` attested at **E1** under operator roster + EV-W1B-CC-01 §17.
2. Pre-check inventory, prerequisite endpoints, duplicate review, verification gates, and ownership neutrality — **all Pass**.
3. Singleton model honored — no second DOM for PRJ-0010 / WEB-ZPM-02 (COR-ZPM-WEB-10).
4. Wave 5B ZPM **Phase A** candidate PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01 **ready** — both endpoints now attested **active**.
5. Wave 5B ZPM **Phase B** (ORG-0005 OWNS DOM-ZPM-01) remains **evidence-gated** — requires E1 registrar/registrant export; **not** inferred from REL-ZPM-WB-04.
6. No PRIMARY_DOMAIN, OWNS, OPERATES, SECONDARY_DOMAIN, REDIRECTS_TO, POINTS_TO, CLIENT_OF, Person, or Organization structural edges created in this package.

**Supersedes prior verdict:**

| Prior verdict | Source | Disposition |
|---------------|--------|-------------|
| **READY FOR WAVE 5 ZPM DOMAIN ATTESTATION** | [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md) §14.3 | **Superseded** — DOM-ZPM-01 now attested **active** |
| **READY FOR WAVE 5 ZPM DOMAIN POPULATION** | [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) §12 | **Superseded** — Wave 5 ZPM population + attestation complete |

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NOT READY** | All gates pass |
| **READY FOR WAVE 5 ZPM DOMAIN ATTESTATION** | Superseded — attestation act complete |
| **READY FOR WAVE 5 ZPM DOMAIN POPULATION** | Superseded — population + attestation complete |

**Downstream:** Execute Wave 5B ZPM Domain relationship population in a **separate pass** — Phase A: PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01; Phase B: ORG-0005 OWNS DOM-ZPM-01 *(registrar E1 gate)*.

---

## 13. Attestation verdict

```text
WAVE 5 ZPM DOMAIN ACTIVE ATTESTATION — COMPLETE
1 / 1 Domain entity attested active
0 Domain relationships created (Wave 5B ZPM queue: 1 PRIMARY_DOMAIN + proposed domain OWNS)
Wave 5B ZPM Domain relationship population — READY TO START
```

---

## 14. Wave 5B ZPM queue (post-attestation)

| Draft candidate | source | target | Type | prerequisite | readiness |
|-----------------|--------|--------|------|--------------|-----------|
| *(TBD rel_id)* | DOM-ZPM-01 bzpm.ru | WEB-ZPM-01 | **PRIMARY_DOMAIN** | Both endpoints **active** | **ready** |
| *(TBD rel_id)* | ORG-0005 ЗПМ | DOM-ZPM-01 | **OWNS** | E1 registrar/registrant — ME-W5-ZPM-01 | **blocked** until evidence |
| `www.bzpm.ru` | TBD | WEB-ZPM-01 | SECONDARY_DOMAIN or REDIRECTS_TO | Steward policy — SU-W4B-ZPM-02 | **deferred** |

**Excluded from Wave 5B candidate roster (unless steward opens review):**

| Item | Reason |
|------|--------|
| OPERATES ORG-0001 → WEB-ZPM-01 | SAFE UNKNOWN — SU-W4B-ZPM-01 |
| CLIENT_OF ORG-0005 → ORG-0001 | Wave 6 |
| DOM-* for retired WEB-ZPM-02 | COR-ZPM-WEB-01 |

---

## 15. Package lineage

```text
Wave 1 (ORG-0001..0004) ──► Wave 1 Attestation (COMPLETE)
        │
        ├── Wave 1B BZPM (ORG-0005, LE-0004) ──► AT-W1B-01 (COMPLETE)
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
        └── Wave 5 ZPM Domain (DOM-ZPM-01) ──► AT-W5-ZPM-01 (THIS ACT)
                    │
                    └──► Wave 5B ZPM Domain Relationship Population (NEXT)
```

---

## 16. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) | Domain roster |
| [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md) | Attestation sequence (superseded §14.3 verdict) |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Prerequisite wave |
| [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | Website endpoint prerequisite |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | Core Triumph domain roster — no collision |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Singleton DOM model basis |

---

*ATLAS Wave 5 ZPM Domain Active Attestation v1 — documentation only.*
