# ATLAS Wave 5 SIBCAR Domain Population v1

**Status:** **documented** — Wave 5 SIBCAR canonical Domain population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR** · LE-0005 ООО «СибКар»  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md)  
**Is not:** runtime, API, automation, database schema, DNS operations, registrar integration, relationship attestation, Wave 5B-SIBCAR execution, Domain attestation act.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1C SIBCAR Organization ORG-0006: **active** — AT-W1C-01
- Wave 6B Commercial REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF**: **active** — AT-W6B-02
- Wave 3 SIBCAR Project PRJ-0011: **attested** — AT-W3-SIBCAR-01
- Wave 3B SIBCAR Project ↔ Organization: **COMPLETE** — AT-W3B-SIBCAR-01
- Wave 4 SIBCAR Website attestation: **COMPLETE** — AT-W4-SIBCAR-01 (WEB-SIBCAR-01 **active**)
- Wave 4B SIBCAR Website Relationships: **COMPLETE** — AT-W4B-SIBCAR-01..02 (REL-SIBCAR-WB-01/02 **active**)
- Population verdict (4B-SIBCAR): **READY FOR WAVE 5 SIBCAR DOMAIN POPULATION**

**Binding operator discipline (Wave 5 SIBCAR):**

- **Approved roster only:** **DOM-SIBCAR-01** (`sibcar.new-site.space`) — singleton TEST hostname anchor.
- **Single-domain model** — one Domain entity for TEST deployment hostname; no production DOM-* mint (ME-W1C-02).
- **Domain population now. Domain relationships later** (Wave 5B SIBCAR).
- **No** PRIMARY_DOMAIN, SECONDARY_DOMAIN, REDIRECTS_TO, POINTS_TO, OWNS, OPERATES, CLIENT_OF, CUSTODIAN edges in Wave 5 SIBCAR.
- **Registrar / registrant ownership** remains **SAFE UNKNOWN** — not inferred from Website OWNS, Project ownership, CC, or operator assumptions.
- **Hostname strictly as TEST deployment identity** — operator/hosting namespace subdomain; **not** corporate production domain.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Domain** для Wave 5 tranche **SIBCAR** (ORG-0006): состав TEST hostname anchor, lifecycle, evidence, org/website **display context only**, candidate relationships для Wave 5B SIBCAR, границы foundation.

**Normative scope Wave 5 SIBCAR:**

```text
Domain entity intake + attestation plan (1 record — DOM-SIBCAR-01 TEST)
Wave 5B SIBCAR (отдельный пакет): PRIMARY_DOMAIN DOM-SIBCAR-01 → WEB-SIBCAR-01 — только после active Domain endpoint
Production corporate domain — deferred until public URL evidence (ME-W1C-02)
```

**Modeling rule (enforced):**

> Domain = **hostname identity anchor** ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5).  
> Website = **web property identity** ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4).  
> Co-terminous hostname string on WEB-SIBCAR-01 and DOM-SIBCAR-01 are **parallel identities**, linked only via **future** PRIMARY_DOMAIN — not merged records.

---

## 2. Domain roster (canonical)

Источник: operator-approved roster; [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md); [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md); [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) §11.

### 2.1 Summary table

| domain_id | canonical_name | environment | lifecycle_state | lifecycle_target | primary_org_candidate | primary_website_candidate | evidence_tier | ownership confidence | registrar status | attestation readiness |
|-----------|----------------|-------------|-----------------|------------------|----------------------|---------------------------|---------------|---------------------|------------------|----------------------|
| **DOM-SIBCAR-01** | sibcar.new-site.space | **TEST** | **proposed** | **active** | ORG-0006 SIBCAR *(display only)* | WEB-SIBCAR-01 sibcar.new-site.space | **E0** | **context only — not attested** | **SAFE UNKNOWN** | **ready** |

**primary_org / primary_website** — display context from operator-approved knowledge and attested Website graph; structural edges **deferred** to Wave 5B SIBCAR.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **proposed** *(pending attestation)* | **1** (DOM-SIBCAR-01) |
| Lifecycle target **active** | **1** (DOM-SIBCAR-01) |
| Production domain candidates | **0** *(blocked — ME-W1C-02)* |
| Relationships in this pass | **0** |

---

## 3. Per-domain analysis — DOM-SIBCAR-01

| Field | Value |
|-------|-------|
| **domain_id** | DOM-SIBCAR-01 |
| **canonical_name** | sibcar.new-site.space |
| **hostname_class** | **hosting_subdomain** — third-level FQDN on operator `new-site.space` namespace |
| **environment** | **TEST** — explicitly declared in EV-W1C-02; not production public URL |
| **lifecycle_state** | **proposed** — population draft pending steward attestation AT-W5-SIBCAR-01 |
| **lifecycle_target** | **active** — TEST deployment hostname serving attested WEB-SIBCAR-01 |
| **primary_org_candidate** | ORG-0006 SIBCAR *(display context only — not domain registrant attestation)* |
| **primary_website_candidate** | WEB-SIBCAR-01 sibcar.new-site.space |
| **primary_project_context** | PRJ-0011 Автосалон СИБКАР — OpenCart dealership *(display only — not Domain edge)* |
| **evidence_tier** | **E0** |
| **evidence_sources** | Operator-approved roster; [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) WEB-SIBCAR-01 **active**; EV-W1C-02 (OCPilot SITE-001 TEST URL); EV-W1C-03 (project-access-brief); EV-OCP-01..04; AT-W4B-SIBCAR-01..02 (Website-family graph complete) |
| **ownership confidence** | **context only — not attested** — ORG-0006 may appear as display candidate; **no** domain-level OWNS attestation |
| **registrar status** | **SAFE UNKNOWN** — no registrar export, WHOIS registrant attestation, or billing-account evidence; CC silent on website (ME-W1C-05) |
| **open questions** | Production corporate domain — **SAFE UNKNOWN** (ME-W1C-02); TEST subdomain registrant — **SAFE UNKNOWN** (SU-W4-SIBCAR-02) |
| **readiness assessment** | **Ready** — TEST hostname identity E0; Website endpoint attested **active** |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Identity review** | One `DOM-*` per TEST hostname; id stable across hosting changes ([ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §3.5) — **Pass** |
| **Hostname review** | FQDN `sibcar.new-site.space` (hosting subdomain); not collapsed with production domain — **Pass** |
| **Ownership review** | ORG-0006 on display fields only; domain **OWNS** edge **not created**; Website OWNS (REL-SIBCAR-WB-02) **does not** substitute domain registrant ([ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3) — **Pass** |
| **Relationship readiness** | WEB-SIBCAR-01 **active**; PRIMARY_DOMAIN candidate documented for Wave 5B SIBCAR — **Pass** |
| **Lifecycle review** | TEST deployment hostname with attested Website → target **active** ([ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md)) — **Pass** |
| **Duplicate hostname review** | No existing `DOM-*` for `sibcar.new-site.space` in core Wave 5 register or ZPM tranche — **Pass** |

---

## 4. Lifecycle analysis

| Rule | Application in Wave 5 SIBCAR |
|------|------------------------------|
| TEST deployment hostname serving attested Website → target **active** | **DOM-SIBCAR-01** — operator-approved; WEB-SIBCAR-01 **active** |
| Production corporate domain without evidence | **Not minted** — ME-W1C-02; SIBCAR-INTAKE-WEB-02 blocked |
| Hostname retired / sold | **Not applicable** — no deprecation in roster |
| DNS record content | **Excluded** — identity only ([ATLAS-REALITY-MODEL-v1.md](../foundation/ATLAS-REALITY-MODEL-v1.md) CR-06) |
| Domain without attested org **OWNS** at **active** | **Allowed** — org link deferred as **edge**; candidate ORG-0006 on display fields only |
| TEST vs production posture | **Enforced** — `environment` **TEST**; not production registrant proof |

**Lifecycle crosswalk:**

| Layer | Entity | Hostname | Lifecycle | Notes |
|-------|--------|----------|-----------|-------|
| Project | PRJ-0011 | *(initiative)* | **active** | OpenCart dealership client delivery |
| Website | WEB-SIBCAR-01 | sibcar.new-site.space | **active** | Sole TEST web property — `test_deployment` |
| Domain | DOM-SIBCAR-01 | sibcar.new-site.space | **proposed** → **active** *(target)* | TEST hostname anchor — this pass |

---

## 5. Evidence basis

**Governance:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-01..06 · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01.

| Ref | Artifact | Tier | Role in Domain population |
|-----|----------|------|---------------------------|
| **Operator-approved roster** | DOM-SIBCAR-01 `sibcar.new-site.space` | intake authority | Primary mint authority |
| **EV-W1C-02** | OCPilot [site-passport.md](../../../projects/ocpilot/sites/site-001/site-passport.md) — SITE-001; TEST URL | **E0** | Hostname string corroboration — **not** registrant / billing proof |
| **EV-W1C-03** | OCPilot [project-access-brief.md](../../../projects/ocpilot/sites/site-001/project-access-brief.md) | **E0** | Same TEST URL; business goal context |
| **EV-OCP-01..04** | Intake complete; SITE-001 registry; pilot narrative | **E0** | Engagement corroboration |
| **EV-W1C-CC-01** | `sibcar/Реквизиты.docx` | **E1** | Org anchor ORG-0006 / LE-0005 only — **no** website field on CC |
| **AT-W4-SIBCAR-01** | [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | attestation | WEB-SIBCAR-01 **active** — co-terminous endpoint |
| **AT-W4B-SIBCAR-01..02** | [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | attestation | Website-family graph complete — **not** domain registrant basis |
| **AT-W1C-01** | [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0006 **active** — org endpoint only |
| **AT-W3-SIBCAR-01** | [ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SIBCAR-PROJECT-ACTIVE-ATTESTATION-v1.md) | attestation | PRJ-0011 **active** — project context only |

**Evidence routing discipline:**

| Claim | Permitted evidence | Forbidden inference |
|-------|-------------------|---------------------|
| Hostname `sibcar.new-site.space` exists as TEST Domain anchor | Operator roster; EV-W1C-02 TEST URL; attested WEB-SIBCAR-01 | DNS zone file contents; production domain assumption |
| Domain lifecycle target **active** | TEST deployment + WEB-SIBCAR-01 **active** | Project lifecycle alone; registrar WHOIS |
| Registrant = ORG-0006 | **None attested** | REL-SIBCAR-WB-02 Website OWNS; CC; operator assumption |
| `new-site.space` parent zone ownership | **None attested** | Hosting subdomain treated as deployment identity only |

**Primary evidence paths:**

```text
E0 OCPilot — EV-W1C-02 (SITE-001; TEST URL https://sibcar.new-site.space/)
E0 OCPilot — EV-W1C-03 (PRJ-0011 Business Goal + Planned Work)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx (org anchor only — no website field)
Attestation — AT-W4-SIBCAR-01 (WEB-SIBCAR-01 active)
```

**Absent evidence (expected):**

| Item | Status |
|------|--------|
| Registrar WHOIS export | **Absent** |
| Registrant billing account | **Absent** |
| CC website / domain field | **Absent** — ME-W1C-05 |
| Production corporate domain URL | **Absent** — ME-W1C-02 |
| DNS A/CNAME/MX records | **Excluded** — not modeled |

---

## 6. Ownership neutrality review

**Binding operator discipline (Wave 5 SIBCAR):**

| Topic | Posture |
|-------|---------|
| Current registrar | **SAFE UNKNOWN** |
| Current registrant | **SAFE UNKNOWN** |
| `new-site.space` zone operator / parent registrant | **SAFE UNKNOWN** — not modeled |
| ORG-0006 domain ownership | **Proposed display context only — not attested** |
| REL-SIBCAR-WB-02 ORG-0006 **OWNS** WEB-SIBCAR-01 | Website structural ownership — **does not** prove domain registrant |
| PRJ-0011 commissioning | Project context — **does not** prove domain registrant |
| EV-W1C-CC-01 | Org card — **no** website field — **does not** prove registrar registrant |
| OPERATES ORG-0001 → property | **SAFE UNKNOWN** — not created |
| REL-0041 CLIENT_OF ORG-0006 → ORG-0001 | **Already attested** Wave 6B — **not** re-minted; **not** domain ownership proof |

**Distinction (enforced):**

```text
REL-SIBCAR-WB-02  ORG-0006 ──OWNS──► WEB-SIBCAR-01     [attested Wave 4B — website property]
(proposed 5B)     DOM-SIBCAR-01 ──PRIMARY_DOMAIN──► WEB-SIBCAR-01  [queued — not created]
(proposed future) ORG-0006 ──OWNS──► DOM-SIBCAR-01     [requires domain-level E1 registrar — NOT inferred]
```

**EFV application:**

| Rule | Application |
|------|-------------|
| **EFV-01** | Hostname stem `sibcar` supports Domain candidate — not org alias proof |
| **EFV-03** | Website / Project naming does not establish domain registrant |
| **EFV-04** | CC silent on website — does not block TEST Domain at E0 OCPilot path |
| **EFV-06** | Ownership fields remain **SAFE UNKNOWN** without registrar cite |

**Ownership confidence levels (Wave 5 SIBCAR register):**

| Level | Meaning |
|-------|---------|
| **context only — not attested** | ORG-0006 appears as display candidate from approved tranche context — **no** domain OWNS edge |
| **SAFE UNKNOWN** | Registrant, billing account, registrar console, parent zone — no E1 registrar evidence |

---

## 7. Duplicate review

| review_id | Signal | Verdict | Blocking |
|-----------|--------|---------|----------|
| **SIBCAR-DOM-D-01** | DOM-SIBCAR-01 vs WEB-SIBCAR-01 | **Class boundary** — parallel identities; PRIMARY_DOMAIN at 5B | No |
| **SIBCAR-DOM-D-02** | DOM-SIBCAR-01 vs PRJ-0011 | **Class boundary** — complementary | No |
| **SIBCAR-DOM-D-03** | DOM-SIBCAR-01 vs ORG-0006 | **Class boundary** — OWNS deferred | No |
| **SIBCAR-DOM-D-04** | vs DOM-ZPM-01 `bzpm.ru` | **Distinct org / hostname** | No |
| **SIBCAR-DOM-D-05** | vs core DOM-0001..0004 Triumph | **Distinct org / hostname** | No |
| **SIBCAR-DOM-D-06** | vs production corporate domain | **Blocked** — ME-W1C-02; not minted | No |
| **SIBCAR-DOM-D-07** | vs ORG-0005 BZPM / `bzpm.ru` | **Distinct** — COR-W1B-03; EFV-02 | No |
| **SIBCAR-DOM-D-08** | `sibcar.new-site.space` singleton | **Pass** — one DOM per TEST hostname | No |
| **SIBCAR-DOM-D-09** | SITE-001 OCPilot crosswalk | **Pass** — documentation only; not Domain substitute | No |

**Hostname cross-check:**

| Hostname | domain_id | website_id | org anchor | Conflict |
|----------|-----------|------------|------------|----------|
| `sibcar.new-site.space` | **DOM-SIBCAR-01** *(this pass)* | WEB-SIBCAR-01 | ORG-0006 SIBCAR | — |
| `bzpm.ru` | DOM-ZPM-01 | WEB-ZPM-01 | ORG-0005 ЗПМ | **None** — distinct org / hostname |
| `gktriumph.ru` | DOM-0001 | WEB-0006 | ORG-0004 | **None** — distinct client |

**Verdict:** **Pass** — one TEST Domain; production candidate blocked; no hostname conflicts.

---

## 8. SAFE UNKNOWN inventory

| ID | Topic | Severity | Wave impact | Status |
|----|-------|----------|-------------|--------|
| **SU-SIBCAR-PRJ-01** | Production public URL | Medium | Production DOM-* deferred | **Unchanged** |
| **ME-W1C-02** *(carry-forward)* | Production public URL | Medium | No production Domain minted | **Unchanged** |
| **ME-W1C-05** *(carry-forward)* | Corporate domain not on CC | Low | Wave 5 DOM-* — E0 OCPilot path used | **Acknowledged** |
| **SU-W4-SIBCAR-02** | TEST subdomain registrant ORG-0006 | Low | Wave 5 SIBCAR DOM-* | **Open** — ownership neutrality |
| **SU-W4-SIBCAR-01** | Live URL probe for TEST hostname | Low | E0 OCPilot sufficient | **Unchanged** |
| **SU-W4-SIBCAR-03** | OWNS without registrar E1 | Low | Website OWNS attested — not domain proof | **Acknowledged** |
| **W1C-D-05** *(carry-forward)* | «Автосалон СИБКАР» vs «СибКар» CC alias | Low | Display disambiguation | **Unchanged** |
| **SU-SIBCAR-PRJ-06** | PROD migration (FUT-03) | Medium | Future production WEB/DOM | **Unchanged** |
| **EV-OCP-GAP-01** | Credential channel confirmation | Low | EAR / OCPilot execution | **Unchanged** |
| **SU-W5-SIBCAR-01** | `new-site.space` parent zone registrant | Low | Hosting namespace — not modeled | **New** — non-blocking |
| **SU-W5-SIBCAR-02** | ORG-0001 OPERATES on TEST property | Low | Separate governance | **New** — non-blocking |

**Missing evidence register (non-blocking):**

| ID | Gap | Severity | Mitigation |
|----|-----|----------|------------|
| **ME-W5-SIBCAR-01** | Registrar WHOIS / registrant export | Medium for domain OWNS | Wave 5B+ if domain OWNS ever proposed — not in approved 5B queue |
| **ME-W5-SIBCAR-02** | PRIMARY_DOMAIN not minted | Low | Wave 5B SIBCAR by design |
| **ME-W5-SIBCAR-03** | Production corporate domain unknown | Medium | Deferred — ME-W1C-02 |
| **ME-W5-SIBCAR-04** | No CC website field | Low | E0 OCPilot path sufficient |

**Blocking gaps remaining:** **None**

---

## 9. Wave 5B queue

**Not attested in Wave 5 SIBCAR.** Prepared for separate Wave 5B SIBCAR population pass.

### 9.1 Domain → Website PRIMARY_DOMAIN

| Draft candidate | source_domain | target_website | Type | Notes |
|-----------------|---------------|----------------|------|-------|
| *(TBD rel_id)* | DOM-SIBCAR-01 sibcar.new-site.space | WEB-SIBCAR-01 | **PRIMARY_DOMAIN** | 1:1 TEST hostname ↔ property; unambiguous singleton; **do not create in Wave 5** |

**Cardinality:** At most one canonical active PRIMARY_DOMAIN per Website ([ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) §4).

### 9.2 Explicitly excluded from Wave 5B queue (this tranche)

| Item | Treatment | Reason |
|------|-----------|--------|
| OWNS Organization → DOM-SIBCAR-01 | **Excluded** | No registrar E1; not in operator-approved 5B queue |
| CUSTODIAN Organization/Person → Domain | **Excluded** | SAFE UNKNOWN |
| OPERATES ORG-0001 → WEB-SIBCAR-01 / DOM-* | **Excluded** | SAFE UNKNOWN — SU-W5-SIBCAR-02 |
| CLIENT_OF ORG-0006 → ORG-0001 | **Excluded** | Already attested Wave 6B — not re-minted |
| SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Excluded** | No secondary hostname in roster |
| Person ↔ Domain edges | **Excluded** | Operator scope |
| Production DOM-* | **Excluded** | ME-W1C-02 |

---

## 10. Deferred items

### 10.1 Out of approved Wave 5 SIBCAR roster

| Hostname / item | Treatment | Reason |
|-----------------|-----------|--------|
| Production corporate domain | **Deferred** | ME-W1C-02 — URL **SAFE UNKNOWN** |
| SIBCAR-INTAKE-WEB-02 production Website | **Blocked** | No production URL evidence |
| Core Triumph DOM-0001..0004 | **Separate tranche** | ORG-0004 — already populated |
| DOM-ZPM-01 `bzpm.ru` | **Separate tranche** | ORG-0005 |
| DNS A/CNAME/MX records | **Excluded** | Hosting ops — not ATLAS |
| Registrar billing / expiry automation | **Excluded** | Finance / registrar console |

### 10.2 Rejected candidates

| Candidate | Treatment | Reason |
|-----------|-----------|--------|
| Merge Domain with Website record | **Rejected** | Parallel identity classes ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4–5) |
| Infer registrar OWNS from REL-SIBCAR-WB-02 alone | **Rejected** | Website OWNS ≠ domain registrant |
| Infer registrant from CC / Project / operator assumption | **Rejected** | Operator ownership discipline |
| Treat TEST subdomain as production apex domain | **Rejected** | TEST deployment identity only |
| Mint DOM-* before Wave 4B complete | **Rejected** | Wave ordering — 4B now **complete** |

---

## 11. Foundation consistency review

| Foundation doc | Wave 5 SIBCAR alignment |
|----------------|-------------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5 Domain | Hostname identity anchor — not DNS ops — **Pass** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | One id per hostname; production domain not assumed — **Pass** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4–6.5 | Hostname on DOM-*; TEST posture documented — **Pass** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | **proposed** → target **active** — **Pass** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5 | E0 TEST deployment path — **Pass** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) Wave 5 | After Website 4B; SIBCAR tranche after 4B-SIBCAR — **Pass** |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | No edges without Domain endpoints — **Pass** (edges deferred) |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7–9 | Families documented — **not created** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | DOM may exist; domain OWNS SAFE UNKNOWN — **Pass** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **Pass** |
| [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | No registrant inference from CC / website / project — **Pass** |

**Cross-population validation:**

| Prior wave doc | Check | Result |
|----------------|-------|--------|
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | WEB-SIBCAR-01 **active** | **Pass** |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website-family context — no Domain edges | **Pass** |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) | Verdict **READY FOR WAVE 5 SIBCAR DOMAIN POPULATION** | **Pass** |
| Wave 1C Organization attestation | ORG-0006 **active** | **Pass** |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | No `sibcar.new-site.space` duplicate | **Pass** |
| [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) | No hostname collision with `bzpm.ru` | **Pass** |

**Verification checklist (operator request):**

| Check | Result |
|-------|--------|
| Domain taxonomy | **Pass** |
| EIR-D01 one hostname = one Domain | **Pass** |
| TEST deployment identity — not production assumption | **Pass** |
| Wave ordering — Wave 5 after Wave 4B SIBCAR | **Pass** |
| Single-domain model (TEST only) | **Pass** |
| No duplicate hostname entities | **Pass** |
| No DNS modelling | **Pass** |
| No registrar modelling | **Pass** |
| No PRIMARY_DOMAIN created | **Pass** |
| No OWNS Domain created | **Pass** |
| No OPERATES / CLIENT_OF / Person edges | **Pass** |

**No new entity types.** **No foundation modifications.**

---

## 12. Readiness verdict

```text
READY FOR WAVE 5 SIBCAR DOMAIN ATTESTATION
```

**Conditions:**

1. Steward executes attestation tranche **AT-W5-SIBCAR-01** to promote DOM-SIBCAR-01 from population draft (**proposed**) to canonical **active**.
2. Wave 5B SIBCAR (**PRIMARY_DOMAIN** DOM-SIBCAR-01 → WEB-SIBCAR-01) may proceed **only after** Domain attestation act.
3. **No** Organization → Domain OWNS in approved Wave 5B queue — registrar E1 absent; ownership remains **SAFE UNKNOWN**.
4. Production corporate domain remains **deferred** until public URL evidence arrives (ME-W1C-02).
5. OPERATES for ORG-0001 remains **SAFE UNKNOWN** — not blocking Domain entity population.
6. REL-0041 CLIENT_OF remains **already attested** — not re-minted.
7. TEST deployment posture on hostname **unchanged** — Domain population does not imply production registrant proof.

---

## 13. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-REGISTER-v1.md) | Canonical domain roster table |
| [ATLAS-WAVE5-SIBCAR-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | Website endpoint candidate |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website-family context (not domain OWNS) |
| [ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) | ZPM tranche structural precedent |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 5 SIBCAR Domain Population v1 — documentation only; entity population — no relationships created.*
