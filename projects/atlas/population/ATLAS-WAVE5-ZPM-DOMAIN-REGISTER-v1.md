# ATLAS Wave 5 ZPM Domain Register v1

**Status:** **documented** — canonical Domain roster after Wave 5 ZPM population and attestation (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07 · **sync:** 2026-06-07 (ZPM documentation sync)  
**Organization anchor:** ORG-0005 **ЗПМ**  
**Parent:** [ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) · [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md)  
**Is not:** relationship registry, DNS export, registrar API dump, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Domain population** Wave 5 tranche **ZPM**. Одна строка — одна approved Domain record (one hostname = one entity).

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **active** | **1** (DOM-ZPM-01) |
| Deferred hostnames | **1** (`www.bzpm.ru` — policy TBD) |
| Attestation | **Complete** — AT-W5-ZPM-01 |
| Relationships in register | **0** (Wave 5B ZPM queue) |

---

## 2. Population roster — full table

| domain_id | canonical_name | hostname_class | primary_org_candidate | primary_website_candidate | evidence_tier | ownership confidence | registrar status | lifecycle_state | attestation_readiness | notes |
|-----------|----------------|----------------|----------------------|---------------------------|---------------|---------------------|------------------|-----------------|----------------------|-------|
| **DOM-ZPM-01** | bzpm.ru | apex | ORG-0005 ЗПМ *(display only)* | WEB-ZPM-01 bzpm.ru | **E1** | **context only — not attested** | **SAFE UNKNOWN** | **active** | AT-W5-ZPM-01 | Sole ZPM hostname anchor; singleton per COR-ZPM-WEB-10 |

**hostname_class** — intake metadata (not entity type); documents apex FQDN for steward review.

**Display-only fields** (`primary_org_candidate`, `primary_website_candidate`) — not structural edges until Wave 5B ZPM attestation.

---

## 3. Population roster — by lifecycle target

### 3.1 Active (1)

| domain_id | canonical_name | hostname_class | evidence_tier | attestation_readiness |
|-----------|----------------|----------------|---------------|----------------------|
| **DOM-ZPM-01** | bzpm.ru | apex | **E1** | AT-W5-ZPM-01 |

### 3.2 Deprecated (0)

*No Domain entities target **deprecated** lifecycle in ZPM tranche. PRJ-0010 holds historical delivery at Project layer only.*

---

## 4. Parallel Website index (informational — not Wave 5 edges)

| domain_id | canonical_name | primary_website_candidate | website lifecycle | website OWNS (Wave 4B ZPM) |
|-----------|----------------|---------------------------|-------------------|----------------------------|
| **DOM-ZPM-01** | bzpm.ru | WEB-ZPM-01 | **active** | REL-ZPM-WB-04 ORG-0005 → WEB-ZPM-01 |

Website **OWNS** edge does **not** substitute Domain **OWNS** or PRIMARY_DOMAIN ([ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) §6).

---

## 5. Ownership and registrar posture (register-level)

| domain_id | ownership confidence | registrar status | Domain OWNS edge | Website OWNS *(context — not domain proof)* |
|-----------|---------------------|------------------|------------------|---------------------------------------------|
| **DOM-ZPM-01** | **context only — not attested** | **SAFE UNKNOWN** | **none** | REL-ZPM-WB-04 ORG-0005 → WEB-ZPM-01 |

**Neutrality rule:** REL-ZPM-WB-04 attests ORG-0005 structural ownership of **Website** property — **not** domain registrant records. CC §17 **Bzpm.ru** cites hostname on org card — **not** registrar registrant.

---

## 6. Evidence index

| Evidence ref | Applies to | Role |
|--------------|------------|------|
| Operator-approved roster DOM-ZPM-01 | DOM-ZPM-01 | Primary intake authority |
| **EV-W1B-CC-01** §17 **Bzpm.ru** | DOM-ZPM-01 | E1 hostname string — **not** registrant proof |
| **EV-ZPM-OP-ACT-01** | DOM-ZPM-01 | E0 ongoing property context |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | DOM-ZPM-01 | Website endpoint pairing |
| [ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ACTIVE-ATTESTATION-v1.md) | DOM-ZPM-01 | WEB-ZPM-01 **active** |
| [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | DOM-ZPM-01 | Website-family context only |
| **COR-ZPM-WEB-10** | DOM-ZPM-01 | Singleton DOM model |
| Registrar WHOIS / registrar export | — | **Absent** — registrar remains SAFE UNKNOWN |

**Primary evidence paths:**

```text
E1 CC hostname — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx §17
E0 operator — EV-ZPM-OP-ACT-01
Attestation — AT-W4-ZPM-01 (WEB-ZPM-01 active)
```

---

## 7. Deferred hostnames (not in register)

| Hostname | Treatment | Target |
|--------|-----------|--------|
| `www.bzpm.ru` | Steward policy: separate DOM vs SECONDARY_DOMAIN | Wave 5B ZPM (SU-W4B-ZPM-02) |
| DOM-* for WEB-ZPM-02 (retired) | **Rejected** — not minted | COR-ZPM-WEB-01 |
| Core Triumph hostnames | Separate tranche — DOM-0001..0004 | Core Wave 5 |
| IDN / punycode variants | None identified | — |

---

## 8. Wave 5B ZPM relationship queue (not in this register)

| Candidate type | Count | Endpoints |
|----------------|-------|-----------|
| PRIMARY_DOMAIN | 1 | DOM-ZPM-01 → WEB-ZPM-01 |
| OWNS (Org → Domain) | 1 (proposed) | ORG-0005 → DOM-ZPM-01 — **evidence gate** |
| SECONDARY_DOMAIN / REDIRECTS_TO | TBD | `www.bzpm.ru` policy |
| OPERATES (Org → Website) | 0 | **Excluded** — SU-W4B-ZPM-01 |

---

## 9. Namespace cross-check

| domain_id namespace | Tranche | org anchor | Hostname | Conflict |
|---------------------|---------|------------|----------|----------|
| DOM-0001..0004 | Core Wave 5 — Triumph | ORG-0004 | gktriumph.ru, etc. | **None** — distinct hostnames |
| **DOM-ZPM-01** | **This register** | **ORG-0005 ЗПМ** | **bzpm.ru** | — |

**Duplicate hostname check:** No existing `DOM-*` with canonical_name `bzpm.ru` — **Pass**.

---

## 10. Foundation consistency

| Check | Result |
|-------|--------|
| One hostname = one Domain entity | **Pass** — singleton `bzpm.ru` |
| Single-domain model (no PRJ-0010 second DOM) | **Pass** — COR-ZPM-WEB-10 |
| No relationships in register | **Pass** |
| No DNS-level fields | **Pass** |
| Registrar SAFE UNKNOWN unless evidenced | **Pass** |
| DOM-ZPM-* id prefix — ZPM tranche namespace | **Pass** |
| Wave 5 after Wave 4B ZPM | **Pass** |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-ZPM-DOMAIN-ATTESTATION-v1.md) | Attestation act |
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | Website pairing |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | Core Triumph domain roster |
| [ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §3.5 | DOM-* assignment rules |

---

*ATLAS Wave 5 ZPM Domain Register v1 — DOM-ZPM-01 **active**; synced 2026-06-07 per AT-W5-ZPM-01.*
