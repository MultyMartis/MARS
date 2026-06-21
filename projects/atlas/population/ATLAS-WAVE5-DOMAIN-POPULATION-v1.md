# ATLAS Wave 5 Domain Population v1

**Status:** **documented** — Wave 5 canonical Domain population plan (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-WEBSITE-ATTESTATION-v1.md) · [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx)  
**Is not:** runtime, API, automation, database schema, DNS operations, registrar integration, relationship attestation, Wave 5B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization relationships: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization relationships: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Wave 4B Website Relationships: **COMPLETE**
- Population verdict: **READY FOR WAVE 5 DOMAIN POPULATION**

**Binding operator correction (Wave 5):**

- **Approved roster only:** DOM-0001..0004 (Triumph client hostnames).
- **Every hostname is a separate Domain entity** — do **not** collapse subdomains into parent apex.
- **Domain population now. Domain relationships later** (Wave 5B).
- **No PRIMARY_DOMAIN, SECONDARY_DOMAIN, REDIRECTS_TO, POINTS_TO, OWNS, CUSTODIAN** edges in Wave 5.
- **Registrar / registrant ownership** remains **SAFE UNKNOWN** unless explicit registrar evidence exists (none in current package).

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Domain** для Wave 5: состав hostname anchors, lifecycle, evidence, org/website context (display candidates only), candidate relationships для Wave 5B, границы foundation.

**Normative scope Wave 5:**

```text
Domain entity intake + attestation plan
Wave 5B (отдельный пакет): PRIMARY_DOMAIN, Organization ↔ Domain OWNS/CUSTODIAN — только после active Domain endpoints
Wave 6: remaining org↔org (REL-0016 CLIENT_OF) and cross-links not covered in 5B
```

**Modeling rule (enforced):**

> Domain = **hostname identity anchor** ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5).  
> Website = **web property identity** ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4).  
> Co-terminous hostname strings on WEB-* and DOM-* are **parallel identities**, linked only via **future** relationships — not merged records.

---

## 2. Population roster (canonical)

Источник: operator-approved roster; [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md); [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md); [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) (лист `Websites` — hostname context only).

### 2.1 Summary table

| domain_id | canonical_name | lifecycle_state | primary_org_candidate | primary_website_candidate | evidence_tier | ownership confidence | registrar status | attestation readiness |
|-----------|----------------|-----------------|----------------------|---------------------------|---------------|---------------------|------------------|----------------------|
| DOM-0001 | gktriumph.ru | **active** | ORG-0004 Триумф | WEB-0006 gktriumph.ru | **E1** | **candidate** ORG-0004 (indirect) | **SAFE UNKNOWN** | **ready** |
| DOM-0002 | blog.gktriumph.ru | **active** | ORG-0004 Триумф | WEB-0007 blog.gktriumph.ru | **E1** | **candidate** ORG-0004 (indirect) | **SAFE UNKNOWN** | **ready** |
| DOM-0003 | gruzotaxi-triumph.ru | **active** | ORG-0004 Триумф | WEB-0008 gruzotaxi-triumph.ru | **E1** | **candidate** ORG-0004 (indirect) | **SAFE UNKNOWN** | **ready** |
| DOM-0004 | manipulator-triumph.ru | **active** | ORG-0004 Триумф | WEB-0009 manipulator-triumph.ru | **E1** | **candidate** ORG-0004 (indirect) | **SAFE UNKNOWN** | **ready** |

**primary_org / primary_website** — display context from operator-approved knowledge and attested Website graph; structural edges **deferred** to Wave 5B.

**ownership confidence (Wave 5):**

| Level | Meaning in this pass |
|-------|----------------------|
| **candidate ORG-0004 (indirect)** | ORG-0004 attested **OWNS** matching Website (REL-0032..0035); hostname serves that property — **not** domain-registrar attestation |
| **SAFE UNKNOWN** | Registrant, billing account, registrar console — no E1 registrar evidence in repo |

---

## 3. Per-domain analysis

### 3.1 DOM-0001 — gktriumph.ru

| Field | Value |
|-------|-------|
| **domain_id** | DOM-0001 |
| **canonical_name** | gktriumph.ru |
| **lifecycle_state** | **active** — live apex hostname for primary Triumph corporate web property |
| **primary_org_candidate** | ORG-0004 ООО «Триумф» |
| **primary_website_candidate** | WEB-0006 gktriumph.ru |
| **evidence_tier** | **E1** |
| **evidence_sources** | Operator-approved roster; live `https://gktriumph.ru`; [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) WEB-0006 **active**; REL-0032 ORG-0004 **OWNS** WEB-0006 (Wave 4B); EV-0005 Triumph CC; dataset Websites sheet |
| **ownership confidence** | **candidate ORG-0004 (indirect)** — website structural ownership attested; domain registrant **not** attested |
| **registrar status** | **SAFE UNKNOWN** — no registrar export or registrant attestation in evidence package |
| **open questions** | `www.gktriumph.ru` — separate DOM vs SECONDARY_DOMAIN vs redirect policy (**deferred** Wave 5B); apex vs www not assumed ([ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D02) |
| **readiness assessment** | **Ready** — hostname identity E1; Website endpoint attested |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Identity review** | One `DOM-*` per apex hostname; id stable across registrar transfer ([ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §3.5) — **Pass** |
| **Hostname review** | FQDN `gktriumph.ru` (apex); punycode N/A; not collapsed with `blog.gktriumph.ru` — **Pass** |
| **Ownership review** | Business **candidate** ORG-0004 via Website graph only; domain **OWNS** edge **not created** ([ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3) — **Pass** |
| **Relationship readiness** | WEB-0006 **active**; PRIMARY_DOMAIN candidate documented for Wave 5B — **Pass** |
| **Lifecycle review** | Live production hostname → **active** ([ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md)) — **Pass** |

---

### 3.2 DOM-0002 — blog.gktriumph.ru

| Field | Value |
|-------|-------|
| **domain_id** | DOM-0002 |
| **canonical_name** | blog.gktriumph.ru |
| **lifecycle_state** | **active** — live subdomain hostname for Triumph blog property |
| **primary_org_candidate** | ORG-0004 Триумф |
| **primary_website_candidate** | WEB-0007 blog.gktriumph.ru |
| **evidence_tier** | **E1** |
| **evidence_sources** | Operator-approved roster; live `https://blog.gktriumph.ru`; WEB-0007 **active**; REL-0033 ORG-0004 **OWNS** WEB-0007; REL-0029 BELONGS_TO PRJ-0007; dataset Websites sheet |
| **ownership confidence** | **candidate ORG-0004 (indirect)** |
| **registrar status** | **SAFE UNKNOWN** |
| **open questions** | Subdomain under `gktriumph.ru` zone — DNS zone operator **not modeled**; subdomain is **independent Domain entity** per operator rule |
| **readiness assessment** | **Ready** |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Identity review** | Separate `DOM-*` from DOM-0001 — **Pass** (operator rule + EIR-D01) |
| **Hostname review** | Full FQDN `blog.gktriumph.ru`; not alias of apex domain record — **Pass** |
| **Ownership review** | Same indirect candidate posture as DOM-0001; no domain OWNS — **Pass** |
| **Relationship readiness** | WEB-0007 **active**; distinct from WEB-0006 (EIR-W01) — **Pass** |
| **Lifecycle review** | Live blog hostname → **active** — **Pass** |

---

### 3.3 DOM-0003 — gruzotaxi-triumph.ru

| Field | Value |
|-------|-------|
| **domain_id** | DOM-0003 |
| **canonical_name** | gruzotaxi-triumph.ru |
| **lifecycle_state** | **active** — live hostname for Gruzotaxi landing |
| **primary_org_candidate** | ORG-0004 Триумф |
| **primary_website_candidate** | WEB-0008 gruzotaxi-triumph.ru |
| **evidence_tier** | **E1** |
| **evidence_sources** | Operator-approved roster; live `https://gruzotaxi-triumph.ru`; WEB-0008 **active**; REL-0034 ORG-0004 **OWNS** WEB-0008; REL-0030 BELONGS_TO PRJ-0005; EV-0005 Triumph CC; MIG pilot prep `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` (proposal support — AT-E-03) |
| **ownership confidence** | **candidate ORG-0004 (indirect)** |
| **registrar status** | **SAFE UNKNOWN** |
| **open questions** | MIG analytics reference hostname — confirms identity only, not registrar |
| **readiness assessment** | **Ready** |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Identity review** | Separate apex domain from Triumph main zone — **Pass** |
| **Hostname review** | Standalone FQDN; not subdomain of `gktriumph.ru` — **Pass** |
| **Ownership review** | Indirect candidate only — **Pass** |
| **Relationship readiness** | WEB-0008 **active** — **Pass** |
| **Lifecycle review** | Live landing hostname → **active** — **Pass** |

---

### 3.4 DOM-0004 — manipulator-triumph.ru

| Field | Value |
|-------|-------|
| **domain_id** | DOM-0004 |
| **canonical_name** | manipulator-triumph.ru |
| **lifecycle_state** | **active** — live hostname for Manipulator landing |
| **primary_org_candidate** | ORG-0004 Триумф |
| **primary_website_candidate** | WEB-0009 manipulator-triumph.ru |
| **evidence_tier** | **E1** |
| **evidence_sources** | Operator-approved roster; live `https://manipulator-triumph.ru`; WEB-0009 **active**; REL-0035 ORG-0004 **OWNS** WEB-0009; REL-0031 BELONGS_TO PRJ-0008; EV-0005 Triumph CC; `projects/triumph-manipulator-landing/` (MARS program — **not** duplicate Domain) |
| **ownership confidence** | **candidate ORG-0004 (indirect)** |
| **registrar status** | **SAFE UNKNOWN** |
| **open questions** | Route-level paths (`*.html`) — page-level; out of Domain scope |
| **readiness assessment** | **Ready** |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Identity review** | Standalone `DOM-*` for landing hostname — **Pass** |
| **Hostname review** | Apex FQDN; Website Factory delivery does not substitute Domain id — **Pass** |
| **Ownership review** | Indirect candidate only — **Pass** |
| **Relationship readiness** | WEB-0009 **active** — **Pass** |
| **Lifecycle review** | Live landing hostname → **active** — **Pass** |

---

## 4. Lifecycle decisions

| Rule | Application in Wave 5 |
|------|------------------------|
| Live hostname serving attested production Website → **active** | **DOM-0001..0004** — operator-approved |
| Parked domain without site | **Not applicable** — all four have live WEB-* endpoints |
| Hostname retired / sold | **Not applicable** — no deprecation in roster |
| DNS record content | **Excluded** — identity only ([ATLAS-REALITY-MODEL-v1.md](../foundation/ATLAS-REALITY-MODEL-v1.md) CR-06) |
| Domain without attested org at **active** | **Allowed** — org link deferred as **edge**; candidate ORG-0004 on display fields only ([ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3) |

---

## 5. Explicit exclusions

### 5.1 Out of approved Wave 5 roster

| Hostname / item | Treatment | Reason |
|-----------------|-----------|--------|
| `www.gktriumph.ru` | **Deferred** | Not in approved roster; www policy → Wave 5B |
| Operator org domains (polygon-ws.ru, etc.) | **Deferred** | Separate steward tranche |
| WEB-0001..0005 hostnames | **Deferred** | Operator org sites — Wave 4 exclusion carries |
| DNS A/CNAME/MX records | **Excluded** | Hosting ops — not ATLAS |
| SSL certificate metadata | **Excluded** | Ops tooling |
| Registrar billing / expiry automation | **Excluded** | Finance / registrar console |

### 5.2 Relationship and edge exclusions (Wave 5B+)

| Item | Treatment | Target wave |
|------|-----------|-------------|
| PRIMARY_DOMAIN Domain → Website | **Deferred** | **Wave 5B** |
| SECONDARY_DOMAIN / REDIRECTS_TO / POINTS_TO | **Deferred** | **Wave 5B** |
| OWNS Organization → Domain | **Deferred** | **Wave 5B** (requires registrar E1 if attested) |
| CUSTODIAN Organization/Person → Domain | **Deferred** | **Wave 5B** |
| Website → Domain | **Deferred** | **Wave 5B** |
| REL-0016 CLIENT_OF ORG-0004 → ORG-0001 | **Deferred** | **Wave 6** |
| ORG-0001 OPERATES (Website or Domain) | **Deferred** | SAFE UNKNOWN — SU-W4B-01 |

### 5.3 Rejected candidates

| Candidate | Treatment | Reason |
|-----------|-----------|--------|
| Collapse `blog.gktriumph.ru` into DOM-0001 | **Rejected** | Operator rule: every hostname = separate Domain |
| Merge Domain with Website record | **Rejected** | Parallel identity classes ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4–5) |
| Infer registrar OWNS from Website OWNS alone | **Rejected** | SU-W4B-06; registrant ≠ website owner without attestation |
| `gktriumph.ru` as alias on WEB-0007 | **Rejected** | Hostname on `DOM-*` ([ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4–6.5) |

---

## 6. Candidate relationships for Wave 5B

**Not attested in Wave 5.** Prepared for separate Wave 5B population pass.

### 6.1 Domain → Website PRIMARY_DOMAIN

| Draft candidate | source_domain | target_website | Type | Notes |
|-----------------|---------------|----------------|------|-------|
| *(TBD rel_id)* | DOM-0001 gktriumph.ru | WEB-0006 | **PRIMARY_DOMAIN** | 1:1 hostname ↔ property; Wave 4 §6.3 queue |
| *(TBD rel_id)* | DOM-0002 blog.gktriumph.ru | WEB-0007 | **PRIMARY_DOMAIN** | Subdomain hostname — still primary for WEB-0007 |
| *(TBD rel_id)* | DOM-0003 gruzotaxi-triumph.ru | WEB-0008 | **PRIMARY_DOMAIN** | Landing |
| *(TBD rel_id)* | DOM-0004 manipulator-triumph.ru | WEB-0009 | **PRIMARY_DOMAIN** | Landing |

**Cardinality:** At most one canonical active PRIMARY_DOMAIN per Website ([ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) §4).

### 6.2 Organization → Domain OWNS / CUSTODIAN

| Draft candidate | source_organization | target_domain | Type | Evidence gate |
|-----------------|---------------------|---------------|------|---------------|
| *(TBD rel_id)* | ORG-0004 Триумф | DOM-0001..0004 | **OWNS** | **E1 registrar or CC registrant** — not attested in Wave 5 |
| *(TBD)* | ORG-0001 Полигон | DOM-* | **CUSTODIAN** | **SAFE UNKNOWN** — no steward decision |

**Distinction (SU-W4B-06 resolution):**

```text
REL-0032..0035  ORG-0004 ──OWNS──► WEB-*     [attested Wave 4B — website property]
(proposed 5B)   ORG-0004 ──OWNS──► DOM-*     [requires domain-level E1 — not inferred]
```

### 6.3 Secondary hostname policy

| Hostname | Candidate treatment | Prerequisite |
|----------|---------------------|--------------|
| `www.gktriumph.ru` | Separate **DOM-*** mint **or** SECONDARY_DOMAIN → WEB-0006 **or** REDIRECTS_TO | Steward hostname policy attestation (EIR-D02) |

---

## 7. Dataset reconciliation notes

| Item | Treatment in Wave 5 |
|------|---------------------|
| Dataset Websites sheet hostnames | Context for WEB-* — DOM-* minted on operator roster, not auto-import |
| No Domains sheet in v0.4 dataset | Expected — first Domain register is Wave 5 |
| Co-terminous WEB/DOM canonical_name strings | Intentional parallel ids — linked in Wave 5B only |
| MIG / MARS program paths | Support identity context — not registrar evidence |

---

## 8. Foundation consistency

| Foundation doc | Wave 5 alignment |
|----------------|------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §5 Domain | Hostname identity anchor — not DNS ops — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | One id per hostname; subdomain separate; parked optional — **yes** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.5 | Hostname on DOM-*; www policy attested — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | **active** for all four — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.5 | E1 operator primary domain — **yes** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) Wave 5 | After Website; before bulk 6C cross-links — **yes** |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | No edges without Domain endpoints — **yes** (edges deferred) |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7–9 | PRIMARY_DOMAIN / OWNS families documented — **not created** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | DOM exists; domain OWNS SAFE UNKNOWN — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **yes** |

**Cross-population validation:**

| Prior wave doc | Check | Result |
|----------------|-------|--------|
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Matching WEB-0006..0009 **active** | **Pass** |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | OWNS/BELONGS_TO context for candidates | **Pass** |
| Wave 1 Organization register | ORG-0004 **active** | **Pass** |

**No new entity types.** **No foundation modifications.**

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | Canonical domain roster table |
| [ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Website endpoint candidates |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Indirect ownership context |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
