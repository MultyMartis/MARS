# ATLAS Wave 5B Domain Relationship Register v1

**Status:** **attested** — canonical Domain-family relationship roster after Wave 5B attestation.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md)  
**Is not:** runtime export, database table, DNS registry, registrar export, Organization → Domain OWNS registry.

---

## 1. Purpose

Канонический **реестр аттестированных Domain-family relationships** после Wave 5B attestation act. Одна строка — одна attested Relationship record.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total attested (Domain family) | **4** |
| PRIMARY_DOMAIN (Domain → Website) | **4** |
| SECONDARY_DOMAIN | **0** |
| OWNS (Organization → Domain) | **0** |
| Lifecycle **active** | **4** |
| Lifecycle deferred / proposed | **0** |
| Relationship families | PRIMARY_DOMAIN only |

---

## 2. Attested roster — full table

| relationship_id | source_id | target_id | relationship_type | attestation_basis | evidence_tier | lifecycle_state | notes |
|-----------------|-----------|-----------|-------------------|-------------------|---------------|-----------------|-------|
| REL-0036 | DOM-0001 gktriumph.ru | WEB-0006 gktriumph.ru | **PRIMARY_DOMAIN** | E1 roster + co-terminous hostname; DOM-0001 active; WEB-0006 active; live URL; REL-0032 context | E1 | **active** | Apex corporate hostname |
| REL-0037 | DOM-0002 blog.gktriumph.ru | WEB-0007 blog.gktriumph.ru | **PRIMARY_DOMAIN** | E1 roster + FQDN match; DOM-0002 active; WEB-0007 active; distinct from DOM-0001 | E1 | **active** | Blog subdomain FQDN — not merged into apex |
| REL-0038 | DOM-0003 gruzotaxi-triumph.ru | WEB-0008 gruzotaxi-triumph.ru | **PRIMARY_DOMAIN** | E1 roster + live URL; DOM-0003 active; WEB-0008 active; REL-0034 context | E1 | **active** | Gruzotaxi landing apex |
| REL-0039 | DOM-0004 manipulator-triumph.ru | WEB-0009 manipulator-triumph.ru | **PRIMARY_DOMAIN** | E1 roster + live URL; DOM-0004 active; WEB-0009 active; REL-0035 context | E1 | **active** | Manipulator landing apex |

---

## 3. Attested roster — by domain (outbound PRIMARY_DOMAIN)

| domain_id | canonical_name | domain lifecycle | target_website | relationship_id | lifecycle_state |
|-----------|----------------|------------------|----------------|-----------------|-----------------|
| DOM-0001 | gktriumph.ru | **active** | WEB-0006 gktriumph.ru | REL-0036 | **active** |
| DOM-0002 | blog.gktriumph.ru | **active** | WEB-0007 blog.gktriumph.ru | REL-0037 | **active** |
| DOM-0003 | gruzotaxi-triumph.ru | **active** | WEB-0008 gruzotaxi-triumph.ru | REL-0038 | **active** |
| DOM-0004 | manipulator-triumph.ru | **active** | WEB-0009 manipulator-triumph.ru | REL-0039 | **active** |

Each Domain endpoint participates in **exactly one** attested relationship in this register.

---

## 4. Attested roster — by website (inbound PRIMARY_DOMAIN)

| website_id | canonical_name | website lifecycle | source_domain | relationship_id | lifecycle_state |
|------------|----------------|-------------------|---------------|-----------------|-----------------|
| WEB-0006 | gktriumph.ru | **active** | DOM-0001 gktriumph.ru | REL-0036 | **active** |
| WEB-0007 | blog.gktriumph.ru | **active** | DOM-0002 blog.gktriumph.ru | REL-0037 | **active** |
| WEB-0008 | gruzotaxi-triumph.ru | **active** | DOM-0003 gruzotaxi-triumph.ru | REL-0038 | **active** |
| WEB-0009 | manipulator-triumph.ru | **active** | DOM-0004 manipulator-triumph.ru | REL-0039 | **active** |

**Singleton check:** Each Website has **exactly one** canonical active PRIMARY_DOMAIN — **Pass**.

---

## 5. Attested roster — by relationship type

| relationship_type | Count | relationship_ids |
|-------------------|-------|------------------|
| **PRIMARY_DOMAIN** | 4 | REL-0036, REL-0037, REL-0038, REL-0039 |

---

## 6. Ownership neutrality register (non-edges)

| domain_id | registrar status | Domain OWNS edge | Website OWNS (Wave 4B) | Notes |
|-----------|------------------|------------------|------------------------|-------|
| DOM-0001 | **SAFE UNKNOWN** | **none** | REL-0032 ORG-0004 → WEB-0006 | Website ownership ≠ domain registrant |
| DOM-0002 | **SAFE UNKNOWN** | **none** | REL-0033 ORG-0004 → WEB-0007 | Same posture |
| DOM-0003 | **SAFE UNKNOWN** | **none** | REL-0034 ORG-0004 → WEB-0008 | Same posture |
| DOM-0004 | **SAFE UNKNOWN** | **none** | REL-0035 ORG-0004 → WEB-0009 | Same posture |

PRIMARY_DOMAIN edges **do not** encode ownership. Organization → Domain **OWNS** remains **unattested** — proposed only pending registrar E1.

---

## 7. Deferred register (not in attested set)

| Item | Reason | Target |
|------|--------|--------|
| ORG-0004 → DOM-* **OWNS** | No registrar/registrant E1 — must not infer from Website OWNS | **Proposed** — Wave 6+ |
| ORG-0001 **CUSTODIAN** / **OPERATES** Domain | No steward decision | **SAFE UNKNOWN** |
| `www.gktriumph.ru` **SECONDARY_DOMAIN** | No hostname-policy evidence | Steward policy — Wave 6 |
| **REDIRECTS_TO** / **POINTS_TO** | Out of 5B scope | Future if evidenced |
| DNS record relationships | Out of ATLAS scope | **Excluded** |
| Registrar relationships | Out of scope | **Excluded** |
| REL-0016 **CLIENT_OF** ORG-0004 → ORG-0001 | Org ↔ Org out of 5B scope | **Wave 6** |
| Person → Domain / Person → Website | Not in approved list | Future expansion |
| Operator org domain edges | Separate tranche | Future wave |

---

## 8. Evidence index (attestation references)

| Ref | Artifact | Relationships supported |
|-----|----------|-------------------------|
| Operator-approved roster DOM-0001..0004 | Wave 5 population | REL-0036..0039 |
| Co-terminous hostname match | DOM-* ↔ WEB-* canonical_name | All four |
| Live URL probe | `https://gktriumph.ru` etc. | All four |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | DOM-0001..0004 **active** | All four |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | WEB-0006..0009 **active** | All four |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | REL-0032..0035 OWNS context | Indirect — not domain OWNS |
| EV-0005 Triumph CC | `triumph/…2024.xlsx` | Client context — **not** registrar proof |
| ATLAS-WAVE1-DATASET-v0.4.xlsx (Websites) | Hostname context | Supporting |
| Registrar WHOIS / export | — | **Absent** |

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 9. Endpoint cross-reference (Domain + Website graph)

| Website | PRIMARY_DOMAIN (inbound) | OWNS (Wave 4B) | BELONGS_TO (Wave 4B) |
|---------|--------------------------|----------------|----------------------|
| WEB-0006 | DOM-0001 (REL-0036) | ORG-0004 (REL-0032) | PRJ-0004, PRJ-0006 |
| WEB-0007 | DOM-0002 (REL-0037) | ORG-0004 (REL-0033) | PRJ-0007 |
| WEB-0008 | DOM-0003 (REL-0038) | ORG-0004 (REL-0034) | PRJ-0005 |
| WEB-0009 | DOM-0004 (REL-0039) | ORG-0004 (REL-0035) | PRJ-0008 |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md) | Formal attestation act |
| [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | Domain endpoints |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Website endpoints |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website-family graph |
