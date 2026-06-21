# ATLAS Wave 5 SIBCAR Domain Register v1

**Status:** **documented** — canonical Domain roster after Wave 5 SIBCAR population (**proposed**; attestation pending).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0006 **SIBCAR**  
**Parent:** [ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md) · [ATLAS-WAVE5-SIBCAR-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-ATTESTATION-v1.md)  
**Is not:** relationship registry, DNS export, registrar API dump, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Domain population** Wave 5 tranche **SIBCAR**. Одна строка — одна approved Domain record (one TEST hostname = one entity).

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **proposed** *(pending attestation)* | **1** (DOM-SIBCAR-01) |
| Lifecycle target **active** | **1** (DOM-SIBCAR-01) |
| Production domain candidates | **0** *(blocked — ME-W1C-02)* |
| Attestation | **Pending** — AT-W5-SIBCAR-01 |
| Relationships in register | **0** (Wave 5B SIBCAR queue) |

---

## 2. Population roster — full table

| domain_id | canonical_name | hostname_class | environment | primary_org_candidate | primary_website_candidate | evidence_tier | ownership confidence | registrar status | lifecycle_state | lifecycle_target | attestation_readiness | notes |
|-----------|----------------|----------------|-------------|----------------------|---------------------------|---------------|---------------------|------------------|-----------------|------------------|----------------------|-------|
| **DOM-SIBCAR-01** | sibcar.new-site.space | hosting_subdomain | **TEST** | ORG-0006 SIBCAR *(display only)* | WEB-SIBCAR-01 sibcar.new-site.space | **E0** | **context only — not attested** | **SAFE UNKNOWN** | **proposed** | **active** | **ready** | Sole SIBCAR TEST hostname anchor; operator `new-site.space` namespace |

**hostname_class** — intake metadata (not entity type); documents third-level FQDN on operator hosting namespace.

**Display-only fields** (`primary_org_candidate`, `primary_website_candidate`) — not structural edges until Wave 5B SIBCAR attestation.

---

## 3. Population roster — by lifecycle target

### 3.1 Active target (1 — pending attestation)

| domain_id | canonical_name | hostname_class | environment | evidence_tier | lifecycle_state | attestation_readiness |
|-----------|----------------|----------------|-------------|---------------|-----------------|----------------------|
| **DOM-SIBCAR-01** | sibcar.new-site.space | hosting_subdomain | **TEST** | **E0** | **proposed** → **active** | **ready** |

### 3.2 Deprecated (0)

*No Domain entities target **deprecated** lifecycle in SIBCAR tranche.*

### 3.3 Blocked (0 minted — 1 deferred)

| intake context | canonical_name | disposition | reason |
|----------------|----------------|-------------|--------|
| Production corporate domain | *(unknown)* | **rejected / not minted** | ME-W1C-02 — production public URL **SAFE UNKNOWN** |

---

## 4. Parallel Website index (informational — not Wave 5 edges)

| domain_id | canonical_name | primary_website_candidate | website lifecycle | website_kind | website OWNS (Wave 4B SIBCAR) |
|-----------|----------------|---------------------------|-------------------|--------------|-------------------------------|
| **DOM-SIBCAR-01** | sibcar.new-site.space | WEB-SIBCAR-01 | **active** | test_deployment | REL-SIBCAR-WB-02 ORG-0006 → WEB-SIBCAR-01 |

Website **OWNS** edge does **not** substitute Domain **OWNS** or PRIMARY_DOMAIN ([ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md) §6).

**Project context (display only):**

| domain_id | primary_project_context | project lifecycle | BELONGS_TO (Wave 4B) |
|-----------|------------------------|-------------------|----------------------|
| **DOM-SIBCAR-01** | PRJ-0011 Автосалон СИБКАР — OpenCart dealership | **active** | REL-SIBCAR-WB-01 WEB-SIBCAR-01 → PRJ-0011 |

---

## 5. Ownership and registrar posture (register-level)

| domain_id | ownership confidence | registrar status | Domain OWNS edge | Website OWNS *(context — not domain proof)* |
|-----------|---------------------|------------------|------------------|---------------------------------------------|
| **DOM-SIBCAR-01** | **context only — not attested** | **SAFE UNKNOWN** | **none** | REL-SIBCAR-WB-02 ORG-0006 → WEB-SIBCAR-01 |

**Neutrality rule:** REL-SIBCAR-WB-02 attests ORG-0006 structural ownership of **Website** property — **not** domain registrant records. CC (EV-W1C-CC-01) cites org anchor only — **no** website / domain field (ME-W1C-05).

**TEST posture:** `sibcar.new-site.space` is operator TEST deployment identity on hosting namespace — **not** corporate production domain registrant proof.

---

## 6. Evidence index

| Evidence ref | Applies to | Role |
|--------------|------------|------|
| Operator-approved roster DOM-SIBCAR-01 | DOM-SIBCAR-01 | Primary intake authority |
| **EV-W1C-02** | DOM-SIBCAR-01 | E0 TEST URL — SITE-001 site-passport — **not** registrant proof |
| **EV-W1C-03** | DOM-SIBCAR-01 | E0 project-access-brief — same TEST URL |
| **EV-OCP-01..04** | DOM-SIBCAR-01 | E0 engagement corroboration |
| **EV-W1C-CC-01** | DOM-SIBCAR-01 | E1 org anchor only — **no** website field |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | DOM-SIBCAR-01 | Website endpoint pairing |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-ACTIVE-ATTESTATION-v1.md) | DOM-SIBCAR-01 | WEB-SIBCAR-01 **active** |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | DOM-SIBCAR-01 | Website-family context only |
| Registrar WHOIS / registrar export | — | **Absent** — registrar remains SAFE UNKNOWN |

**Primary evidence paths:**

```text
E0 OCPilot — EV-W1C-02 (SITE-001; TEST URL https://sibcar.new-site.space/)
E0 OCPilot — EV-W1C-03 (PRJ-0011 Business Goal + Planned Work)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\sibcar\Реквизиты.docx (org anchor only)
Attestation — AT-W4-SIBCAR-01 (WEB-SIBCAR-01 active)
```

---

## 7. Deferred hostnames (not in register)

| Hostname / item | Treatment | Target |
|-----------------|-----------|--------|
| Production corporate domain | **Blocked** — URL unknown | Deferred — ME-W1C-02 |
| SIBCAR-INTAKE-WEB-02 production Website | **Not minted** | Wave 4 — blocked |
| Core Triumph hostnames | Separate tranche — DOM-0001..0004 | Core Wave 5 |
| DOM-ZPM-01 `bzpm.ru` | Separate tranche — ORG-0005 | ZPM Wave 5 |
| `new-site.space` parent zone | **Not modeled** | SU-W5-SIBCAR-01 |
| IDN / punycode variants | None identified | — |

---

## 8. Wave 5B SIBCAR relationship queue (not in this register)

| Candidate type | Count | Endpoints | Create in Wave 5? |
|----------------|-------|-----------|-------------------|
| **PRIMARY_DOMAIN** | **1** | DOM-SIBCAR-01 → WEB-SIBCAR-01 | **No** — queue only |
| OWNS (Org → Domain) | 0 | — | **Excluded** — not in approved queue |
| OPERATES (Org → Website) | 0 | — | **Excluded** — SU-W5-SIBCAR-02 |
| CLIENT_OF | 0 | — | **Excluded** — REL-0041 already attested |
| Person ↔ Domain | 0 | — | **Excluded** |
| SECONDARY_DOMAIN / REDIRECTS_TO | 0 | — | **Excluded** |

---

## 9. Namespace cross-check

| domain_id namespace | Tranche | org anchor | Hostname | Conflict |
|---------------------|---------|------------|----------|----------|
| DOM-0001..0004 | Core Wave 5 — Triumph | ORG-0004 | gktriumph.ru, etc. | **None** — distinct hostnames |
| DOM-ZPM-01 | ZPM Wave 5 | ORG-0005 ЗПМ | bzpm.ru | **None** — distinct org / hostname |
| **DOM-SIBCAR-01** | **This register** | **ORG-0006 SIBCAR** | **sibcar.new-site.space** | — |

**Duplicate hostname check:** No existing `DOM-*` with canonical_name `sibcar.new-site.space` — **Pass**.

---

## 10. Foundation consistency

| Check | Result |
|-------|--------|
| One hostname = one Domain entity | **Pass** — singleton `sibcar.new-site.space` |
| TEST deployment identity — not production assumption | **Pass** |
| No relationships in register | **Pass** |
| No DNS-level fields | **Pass** |
| Registrar SAFE UNKNOWN unless evidenced | **Pass** |
| DOM-SIBCAR-* id prefix — SIBCAR tranche namespace | **Pass** |
| Wave 5 after Wave 4B SIBCAR | **Pass** |
| No PRIMARY_DOMAIN / OWNS Domain in register | **Pass** |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-POPULATION-v1.md) | Source population plan |
| [ATLAS-WAVE5-SIBCAR-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-SIBCAR-DOMAIN-ATTESTATION-v1.md) | Attestation act |
| [ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SIBCAR-WEBSITE-REGISTER-v1.md) | Website pairing |
| [ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-SIBCAR-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website-family context |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | Core Triumph domain roster |
| [ATLAS-IDENTIFIER-MODEL-v1.md](../foundation/ATLAS-IDENTIFIER-MODEL-v1.md) §3.5 | DOM-* assignment rules |

---

*ATLAS Wave 5 SIBCAR Domain Register v1 — DOM-SIBCAR-01 **proposed**; attestation pending AT-W5-SIBCAR-01.*
