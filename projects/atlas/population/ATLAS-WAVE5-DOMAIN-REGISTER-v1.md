# ATLAS Wave 5 Domain Register v1

**Status:** **documented** — canonical Domain roster after Wave 5 population (pending steward attestation act).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) · [ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md)  
**Is not:** relationship registry, DNS export, registrar API dump, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Domain population** Wave 5. Одна строка — одна approved Domain record (one hostname = one entity).

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **4** |
| Target **active** | **4** (DOM-0001..0004) |
| Target **proposed** | **0** |
| Target **deprecated** | **0** |
| Deferred hostnames | **1+** (`www.gktriumph.ru` — policy TBD) |
| Attestation readiness **ready** | **4** |
| Relationships in register | **0** (Wave 5B) |

---

## 2. Population roster — full table

| domain_id | canonical_name | hostname_class | primary_org_candidate | primary_website_candidate | evidence_tier | ownership confidence | registrar status | lifecycle_state | attestation_readiness | notes |
|-----------|----------------|----------------|----------------------|---------------------------|---------------|---------------------|------------------|-----------------|----------------------|-------|
| DOM-0001 | gktriumph.ru | apex | ORG-0004 Триумф | WEB-0006 gktriumph.ru | E1 | candidate ORG-0004 (indirect) | **SAFE UNKNOWN** | **active** | **ready** | Main corporate hostname |
| DOM-0002 | blog.gktriumph.ru | subdomain FQDN | ORG-0004 Триумф | WEB-0007 blog.gktriumph.ru | E1 | candidate ORG-0004 (indirect) | **SAFE UNKNOWN** | **active** | **ready** | **Not** merged into DOM-0001 |
| DOM-0003 | gruzotaxi-triumph.ru | apex | ORG-0004 Триумф | WEB-0008 gruzotaxi-triumph.ru | E1 | candidate ORG-0004 (indirect) | **SAFE UNKNOWN** | **active** | **ready** | Gruzotaxi landing |
| DOM-0004 | manipulator-triumph.ru | apex | ORG-0004 Триумф | WEB-0009 manipulator-triumph.ru | E1 | candidate ORG-0004 (indirect) | **SAFE UNKNOWN** | **active** | **ready** | Manipulator landing |

**hostname_class** — intake metadata (not entity type); documents apex vs full FQDN for steward review.

---

## 3. Population roster — by hostname_class

### 3.1 Apex hostnames (3)

| domain_id | canonical_name | lifecycle_state | evidence_tier | attestation_readiness |
|-----------|----------------|-----------------|---------------|----------------------|
| DOM-0001 | gktriumph.ru | **active** | E1 | **ready** |
| DOM-0003 | gruzotaxi-triumph.ru | **active** | E1 | **ready** |
| DOM-0004 | manipulator-triumph.ru | **active** | E1 | **ready** |

### 3.2 Subdomain FQDN (1)

| domain_id | canonical_name | lifecycle_state | evidence_tier | attestation_readiness |
|-----------|----------------|-----------------|---------------|----------------------|
| DOM-0002 | blog.gktriumph.ru | **active** | E1 | **ready** |

**Policy note:** DOM-0002 is a **separate Domain entity** from DOM-0001 per operator modeling rule — not a child record or alias of the apex domain.

---

## 4. Parallel Website index (informational — not Wave 5 edges)

| domain_id | canonical_name | primary_website_candidate | website lifecycle | website OWNS (Wave 4B) |
|-----------|----------------|---------------------------|-------------------|------------------------|
| DOM-0001 | gktriumph.ru | WEB-0006 | **active** | REL-0032 ORG-0004 → WEB-0006 |
| DOM-0002 | blog.gktriumph.ru | WEB-0007 | **active** | REL-0033 ORG-0004 → WEB-0007 |
| DOM-0003 | gruzotaxi-triumph.ru | WEB-0008 | **active** | REL-0034 ORG-0004 → WEB-0008 |
| DOM-0004 | manipulator-triumph.ru | WEB-0009 | **active** | REL-0035 ORG-0004 → WEB-0009 |

Website **OWNS** edges do **not** substitute Domain **OWNS** or PRIMARY_DOMAIN ([ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) §6.2).

---

## 5. Ownership and registrar posture (register-level)

| domain_id | ownership confidence | registrar status | Domain OWNS edge |
|-----------|---------------------|------------------|------------------|
| DOM-0001 | candidate ORG-0004 (indirect via WEB-0006) | **SAFE UNKNOWN** | **none** |
| DOM-0002 | candidate ORG-0004 (indirect via WEB-0007) | **SAFE UNKNOWN** | **none** |
| DOM-0003 | candidate ORG-0004 (indirect via WEB-0008) | **SAFE UNKNOWN** | **none** |
| DOM-0004 | candidate ORG-0004 (indirect via WEB-0009) | **SAFE UNKNOWN** | **none** |

**Indirect basis:** REL-0032..0035 attest ORG-0004 structural ownership of **Website** properties — not registrant records.

---

## 6. Evidence index

| Evidence ref | Applies to | Role |
|--------------|------------|------|
| Operator-approved roster DOM-0001..0004 | All | Primary intake authority |
| Live URL probe | DOM-0001..0004 | E1 hostname existence |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | All | Website endpoint pairing |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | All | Indirect org context (Website OWNS) |
| EV-0005 Triumph CC | DOM-0001, 0003, 0004 | Client context — **not** registrar proof |
| ATLAS-WAVE1-DATASET-v0.4.xlsx (Websites) | All | Draft hostname context |
| Registrar WHOIS / registrar export | — | **Absent** — registrar remains SAFE UNKNOWN |

---

## 7. Deferred hostnames (not in register)

| Hostname | Treatment | Target |
|--------|-----------|--------|
| `www.gktriumph.ru` | Steward policy: separate DOM vs SECONDARY_DOMAIN | Wave 5B |
| Operator org domains | Out of Triumph pilot roster | Future wave |
| IDN / punycode variants | None identified | — |

---

## 8. Wave 5B relationship queue (not in this register)

| Candidate type | Count | Endpoints |
|----------------|-------|-----------|
| PRIMARY_DOMAIN | 4 | DOM-0001..0004 → WEB-0006..0009 |
| OWNS (Org → Domain) | 4 (proposed) | ORG-0004 → DOM-* — **evidence gate** |
| SECONDARY_DOMAIN / REDIRECTS_TO | TBD | `www.gktriumph.ru` policy |

---

## 9. Foundation consistency

| Check | Result |
|-------|--------|
| One hostname = one Domain entity | **Pass** — 4 distinct FQDNs |
| No subdomain collapse | **Pass** — DOM-0002 separate from DOM-0001 |
| No relationships in register | **Pass** |
| No DNS-level fields | **Pass** |
| Registrar SAFE UNKNOWN unless evidenced | **Pass** |
| DOM-* id prefix per identifier model | **Pass** |

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md) | Attestation act |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Website pairing |
| [ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §3.5 | DOM-* assignment rules |
