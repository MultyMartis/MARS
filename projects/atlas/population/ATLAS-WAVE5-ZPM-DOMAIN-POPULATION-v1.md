# ATLAS Wave 5 ZPM Domain Population v1

**Status:** **documented** — Wave 5 ZPM canonical Domain population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004 ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md)  
**Is not:** runtime, API, automation, database schema, DNS operations, registrar integration, relationship attestation, Wave 5B-ZPM execution.

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
- Population verdict (4B-ZPM): **READY FOR WAVE 5 ZPM DOMAIN POPULATION**

**Binding operator correction (Wave 5 ZPM):**

- **Approved roster only:** **DOM-ZPM-01** (`bzpm.ru`) — singleton hostname anchor.
- **Single-domain model** — one Domain entity for `bzpm.ru`; no dual-generation DOM-* for retired WEB-ZPM-02 (COR-ZPM-WEB-10; SU-W4-ZPM-03 **resolved**).
- **Domain population now. Domain relationships later** (Wave 5B ZPM).
- **No** PRIMARY_DOMAIN, SECONDARY_DOMAIN, REDIRECTS_TO, POINTS_TO, OWNS, OPERATES, CLIENT_OF, CUSTODIAN edges in Wave 5 ZPM.
- **Registrar / registrant ownership** remains **SAFE UNKNOWN** — not inferred from Website OWNS, Project ownership, CC website field, or operator assumptions.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Domain** для Wave 5 tranche **ZPM** (ORG-0005): состав hostname anchor, lifecycle, evidence, org/website **display context only**, candidate relationships для Wave 5B ZPM, границы foundation.

**Normative scope Wave 5 ZPM:**

```text
Domain entity intake + attestation plan (1 record — DOM-ZPM-01)
Wave 5B ZPM (отдельный пакет): PRIMARY_DOMAIN, Organization ↔ Domain OWNS — только после active Domain endpoint
Wave 6: CLIENT_OF ORG-0005 → ORG-0001 and remaining org↔org
```

**Modeling rule (enforced):**

> Domain = **hostname identity anchor** ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5).  
> Website = **web property identity** ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4).  
> Co-terminous hostname string on WEB-ZPM-01 and DOM-ZPM-01 are **parallel identities**, linked only via **future** relationships — not merged records.

---

## 2. Domain roster (canonical)

Источник: operator-approved roster; [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md); [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md); [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) §11.

### 2.1 Summary table

| domain_id | canonical_name | lifecycle_state | primary_org_candidate | primary_website_candidate | evidence_tier | ownership confidence | registrar status | attestation readiness |
|-----------|----------------|-----------------|----------------------|---------------------------|---------------|---------------------|------------------|----------------------|
| **DOM-ZPM-01** | bzpm.ru | **active** | ORG-0005 ЗПМ *(display only)* | WEB-ZPM-01 bzpm.ru | **E1** | **context only — not attested** | **SAFE UNKNOWN** | **ready** |

**primary_org / primary_website** — display context from operator-approved knowledge and attested Website graph; structural edges **deferred** to Wave 5B ZPM.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Target **active** | **1** (DOM-ZPM-01) |
| Target **proposed** | **0** |
| Target **deprecated** | **0** |
| Relationships in this pass | **0** |

---

## 3. Per-domain analysis — DOM-ZPM-01

| Field | Value |
|-------|-------|
| **domain_id** | DOM-ZPM-01 |
| **canonical_name** | bzpm.ru |
| **hostname_class** | apex |
| **lifecycle_state** | **active** — live apex hostname for sole ZPM web property |
| **primary_org_candidate** | ORG-0005 ЗПМ *(display context only — not domain registrant attestation)* |
| **primary_website_candidate** | WEB-ZPM-01 bzpm.ru |
| **evidence_tier** | **E1** |
| **evidence_sources** | Operator-approved roster; [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) WEB-ZPM-01 **active**; EV-W1B-CC-01 §17 **Bzpm.ru** (hostname string on CC — **not** registrant proof); EV-ZPM-OP-ACT-01 (operator — ongoing property); COR-ZPM-WEB-10 singleton DOM model |
| **ownership confidence** | **context only — not attested** — ORG-0005 may appear as display candidate; **no** domain-level OWNS attestation |
| **registrar status** | **SAFE UNKNOWN** — no registrar export, WHOIS registrant attestation, or billing-account evidence in package |
| **open questions** | `www.bzpm.ru` — separate DOM vs SECONDARY_DOMAIN vs redirect policy (**deferred** Wave 5B ZPM — SU-W4B-ZPM-02); apex vs www not assumed ([ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D02) |
| **readiness assessment** | **Ready** — hostname identity E1; Website endpoint attested |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Identity review** | One `DOM-*` per apex hostname; id stable across registrar transfer ([ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §3.5) — **Pass** |
| **Hostname review** | FQDN `bzpm.ru` (apex); punycode N/A; not collapsed with `www.bzpm.ru` — **Pass** |
| **Ownership review** | ORG-0005 on display fields only; domain **OWNS** edge **not created**; Website OWNS (REL-ZPM-WB-04) **does not** substitute domain registrant ([ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3) — **Pass** |
| **Relationship readiness** | WEB-ZPM-01 **active**; PRIMARY_DOMAIN candidate documented for Wave 5B ZPM — **Pass** |
| **Lifecycle review** | Live production hostname → **active** ([ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md)) — **Pass** |
| **Duplicate hostname review** | No existing `DOM-*` for `bzpm.ru` in core Wave 5 register (DOM-0001..0004 are Triumph hostnames only) — **Pass** |

---

## 4. Lifecycle analysis

| Rule | Application in Wave 5 ZPM |
|------|---------------------------|
| Live hostname serving attested production Website → **active** | **DOM-ZPM-01** — operator-approved; WEB-ZPM-01 **active** |
| Parked domain without site | **Not applicable** — WEB-ZPM-01 attested **active** |
| Hostname retired / sold | **Not applicable** — no deprecation in roster |
| Historical delivery generation (PRJ-0010) | **Does not** mint second Domain — Project-layer only; single Website model (COR-ZPM-WEB-01) |
| DNS record content | **Excluded** — identity only ([ATLAS-REALITY-MODEL-v1.md](../foundation/ATLAS-REALITY-MODEL-v1.md) CR-06) |
| Domain without attested org **OWNS** at **active** | **Allowed** — org link deferred as **edge**; candidate ORG-0005 on display fields only |

**Lifecycle crosswalk:**

| Layer | Entity | Hostname | Lifecycle | Notes |
|-------|--------|----------|-----------|-------|
| Project | PRJ-0009 | *(initiative)* | **active** | Catalog-platform delivery |
| Project | PRJ-0010 | *(initiative)* | **deprecated** | Historical site delivery — not Domain |
| Website | WEB-ZPM-01 | bzpm.ru | **active** | Sole web property |
| Domain | DOM-ZPM-01 | bzpm.ru | **active** *(target)* | Hostname anchor — this pass |

---

## 5. Evidence basis

**Governance:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-01..06 · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01.

| Ref | Artifact | Tier | Role in Domain population |
|-----|----------|------|---------------------------|
| **Operator-approved roster** | DOM-ZPM-01 `bzpm.ru` | intake authority | Primary mint authority |
| **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` §17 **Bzpm.ru** | **E1** | Hostname string corroboration — **not** registrant / billing proof |
| **EV-ZPM-OP-ACT-01** | Operator — current catalog rebuild | **E0** | Ongoing client property context |
| **AT-W4-ZPM-01** | [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | attestation | WEB-ZPM-01 **active** — co-terminous endpoint |
| **AT-W4B-ZPM-01..02** | [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | attestation | Website-family graph complete — **not** domain registrant basis |
| **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0005 **active** — org endpoint only |
| **COR-ZPM-WEB-10** | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | correction | Singleton DOM-* → WEB-ZPM-01 |

**Evidence routing discipline:**

| Claim | Permitted evidence | Forbidden inference |
|-------|-------------------|---------------------|
| Hostname `bzpm.ru` exists as Domain anchor | Operator roster; CC §17 hostname field; attested WEB-ZPM-01 | DNS zone file contents |
| Domain lifecycle **active** | Live property + WEB-ZPM-01 **active** | Project lifecycle alone |
| Registrant = ORG-0005 | **None attested** | REL-ZPM-WB-04 Website OWNS; CC §17 website field; operator assumption |

**Primary evidence paths:**

```text
E1 CC hostname — EV-W1B-CC-01 §17 Bzpm.ru (string only — not registrant)
E0 operator — EV-ZPM-OP-ACT-01 (property context)
Attestation — AT-W4-ZPM-01 (WEB-ZPM-01 active)
CC path — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx
```

**Absent evidence (expected):**

| Item | Status |
|------|--------|
| Registrar WHOIS export | **Absent** |
| Registrant billing account | **Absent** |
| DNS A/CNAME/MX records | **Excluded** — not modeled |

---

## 6. Ownership neutrality review

**Binding operator discipline (Wave 5 ZPM):**

| Topic | Posture |
|-------|---------|
| Current registrar | **SAFE UNKNOWN** |
| Current registrant | **SAFE UNKNOWN** |
| ORG-0005 domain ownership | **Proposed display context only — not attested** |
| REL-ZPM-WB-04 ORG-0005 **OWNS** WEB-ZPM-01 | Website structural ownership — **does not** prove domain registrant |
| PRJ-0009 / PRJ-0010 commissioning | Project context — **does not** prove domain registrant |
| EV-W1B-CC-01 §17 **Bzpm.ru** | Org card website field — **does not** prove registrar registrant |
| OPERATES ORG-0001 → property | **SAFE UNKNOWN** — not created |

**Distinction (enforced):**

```text
REL-ZPM-WB-04  ORG-0005 ──OWNS──► WEB-ZPM-01     [attested Wave 4B — website property]
(proposed 5B)  ORG-0005 ──OWNS──► DOM-ZPM-01     [requires domain-level E1 registrar — NOT inferred]
```

**EFV application:**

| Rule | Application |
|------|-------------|
| **EFV-01** | Hostname stem `bzpm.ru` supports Domain candidate — not org alias proof |
| **EFV-03** | Website / Project naming does not establish domain registrant |
| **EFV-06** | Ownership fields remain **SAFE UNKNOWN** without registrar cite |

**Ownership confidence levels (Wave 5 ZPM register):**

| Level | Meaning |
|-------|---------|
| **context only — not attested** | ORG-0005 appears as display candidate from approved tranche context — **no** domain OWNS edge |
| **SAFE UNKNOWN** | Registrant, billing account, registrar console — no E1 registrar evidence |

---

## 7. Deferred items

### 7.1 Out of approved Wave 5 ZPM roster

| Hostname / item | Treatment | Reason |
|-----------------|-----------|--------|
| `www.bzpm.ru` | **Deferred** | Not in approved roster; www policy → Wave 5B ZPM (SU-W4B-ZPM-02) |
| DOM-* for retired WEB-ZPM-02 | **Rejected** | COR-ZPM-WEB-01 — historical delivery at Project layer |
| Core Triumph DOM-0001..0004 | **Separate tranche** | ORG-0004 — already populated |
| DNS A/CNAME/MX records | **Excluded** | Hosting ops — not ATLAS |
| SSL certificate metadata | **Excluded** | Ops tooling |
| Registrar billing / expiry automation | **Excluded** | Finance / registrar console |

### 7.2 Relationship and edge exclusions (Wave 5B ZPM+)

| Item | Treatment | Target wave |
|------|-----------|-------------|
| PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01 | **Deferred** | **Wave 5B ZPM** |
| SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Deferred** | **Wave 5B ZPM** |
| OWNS Organization → Domain | **Deferred** | **Wave 5B ZPM** (requires registrar E1) |
| CUSTODIAN Organization/Person → Domain | **Deferred** | **Wave 5B ZPM** |
| OPERATES ORG-0001 → WEB-ZPM-01 / DOM-* | **Deferred** | SAFE UNKNOWN — SU-W4B-ZPM-01 |
| REL-0016 CLIENT_OF ORG-0005 → ORG-0001 | **Deferred** | **Wave 6** |
| Website ↔ Domain (other families) | **Deferred** | **Wave 5B ZPM** |

### 7.3 Rejected candidates

| Candidate | Treatment | Reason |
|-----------|-----------|--------|
| Merge Domain with Website record | **Rejected** | Parallel identity classes ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4–5) |
| Infer registrar OWNS from REL-ZPM-WB-04 alone | **Rejected** | Website OWNS ≠ domain registrant |
| Infer registrant from CC §17 website field | **Rejected** | Operator ownership discipline |
| Second DOM-* for PRJ-0010 historical generation | **Rejected** | Single-domain model — COR-ZPM-WEB-10 |
| Mint DOM-* before Wave 4B complete | **Rejected** | Wave ordering — 4B now **complete** |

---

## 8. Candidate relationships for Wave 5B ZPM

**Not attested in Wave 5 ZPM.** Prepared for separate Wave 5B ZPM population pass.

### 8.1 Domain → Website PRIMARY_DOMAIN

| Draft candidate | source_domain | target_website | Type | Notes |
|-----------------|---------------|----------------|------|-------|
| *(TBD rel_id)* | DOM-ZPM-01 bzpm.ru | WEB-ZPM-01 | **PRIMARY_DOMAIN** | 1:1 hostname ↔ property; unambiguous — no WEB-ZPM-02; COR-ZPM-WEB-10 |

**Cardinality:** At most one canonical active PRIMARY_DOMAIN per Website ([ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) §4).

### 8.2 Organization → Domain OWNS / CUSTODIAN

| Draft candidate | source_organization | target_domain | Type | Evidence gate |
|-----------------|---------------------|---------------|------|---------------|
| *(TBD rel_id)* | ORG-0005 ЗПМ | DOM-ZPM-01 | **OWNS** | **E1 registrar or registrant export** — **not attested** in Wave 5 ZPM |
| *(TBD)* | ORG-0001 Полигон | DOM-ZPM-01 | **CUSTODIAN** | **SAFE UNKNOWN** — no steward decision |

### 8.3 Secondary hostname policy

| Hostname | Candidate treatment | Prerequisite |
|----------|---------------------|--------------|
| `www.bzpm.ru` | Separate **DOM-*** mint **or** SECONDARY_DOMAIN → WEB-ZPM-01 **or** REDIRECTS_TO | Steward hostname policy attestation (EIR-D02; SU-W4B-ZPM-02) |

---

## 9. Dataset and namespace reconciliation

| Item | Treatment in Wave 5 ZPM |
|------|-------------------------|
| No Domains sheet in v0.4 dataset | Expected — ZPM DOM-* minted on operator roster |
| Co-terminous WEB-ZPM-01 / DOM-ZPM-01 `bzpm.ru` | Intentional parallel ids — linked in Wave 5B ZPM only |
| Core Wave 5 DOM-0001..0004 | Triumph tranche — **no hostname collision** with `bzpm.ru` |
| DOM-ZPM-01 namespace | ZPM tranche suffix — distinct from numeric DOM-000* core roster |
| MIG / program paths | Out of scope — not registrar evidence |

**Duplicate hostname entity check:**

| Hostname | Existing DOM-* | New DOM-* | Verdict |
|----------|----------------|-----------|---------|
| `bzpm.ru` | **none** | DOM-ZPM-01 | **Pass** — no duplicate |
| `gktriumph.ru` | DOM-0001 | — | Separate tranche — no conflict |

---

## 10. Foundation consistency review

| Foundation doc | Wave 5 ZPM alignment |
|----------------|---------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5 Domain | Hostname identity anchor — not DNS ops — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | One id per hostname; www not assumed; parked optional — **Pass** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4–6.5 | Hostname on DOM-*; www policy deferred — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | **active** for DOM-ZPM-01 — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5 | E1 hostname identity path — **Pass** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) Wave 5 | After Website 4B; ZPM tranche after 4B-ZPM — **Pass** |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | No edges without Domain endpoints — **Pass** (edges deferred) |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7–9 | Families documented — **not created** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | DOM may exist; domain OWNS SAFE UNKNOWN — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **Pass** |
| [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | No registrant inference from CC / website / project — **Pass** |

**Cross-population validation:**

| Prior wave doc | Check | Result |
|----------------|-------|--------|
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | WEB-ZPM-01 **active** | **Pass** |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website-family context — no Domain edges | **Pass** |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Verdict **READY FOR WAVE 5 ZPM DOMAIN POPULATION** | **Pass** |
| Wave 1B Organization attestation | ORG-0005 **active** | **Pass** |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | No `bzpm.ru` duplicate | **Pass** |

**Verification checklist (operator request):**

| Check | Result |
|-------|--------|
| Domain taxonomy | **Pass** |
| EIR-D01 one hostname = one Domain | **Pass** |
| Hostname identity rules (EIR-D02 www deferred) | **Pass** |
| Wave ordering — Wave 5 after Wave 4B ZPM | **Pass** |
| Single-domain model | **Pass** |
| No duplicate hostname entities | **Pass** |
| No DNS modelling | **Pass** |
| No registrar modelling | **Pass** |

**No new entity types.** **No foundation modifications.**

---

## 11. Readiness verdict

```text
READY FOR WAVE 5 ZPM DOMAIN ATTESTATION
```

**Conditions:**

1. Steward executes attestation tranche AT-W5-ZPM-01 to promote DOM-ZPM-01 from population draft to canonical **active**.
2. Wave 5B ZPM **Phase A** (PRIMARY_DOMAIN DOM-ZPM-01 → WEB-ZPM-01) may proceed after Domain attestation act.
3. Wave 5B ZPM **Phase B** (ORG-0005 OWNS DOM-ZPM-01) requires **E1 registrar/registrant evidence** — **not** inferred from REL-ZPM-WB-04.
4. `www.bzpm.ru` policy resolved in Wave 5B ZPM — not blocking singleton roster.
5. OPERATES for ORG-0001 remains **SAFE UNKNOWN** — not blocking Domain entity population.

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) | Canonical domain roster table |
| [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | Website endpoint candidate |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website-family context (not domain OWNS) |
| [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) | Core Triumph Wave 5 precedent |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 5 ZPM Domain Population v1 — documentation only; entity population — no relationships created.*
