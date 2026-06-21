# ATLAS Corvonero Domain Relationship Register v1

**Status:** **documented** — canonical Domain-family relationship roster for Corvonero tranche (**active**; attestation complete; **corrected** 2026-06-21).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Organization anchor:** ORG-0009 **Центр автоматизации «Корво Неро»**  
**Is not:** Org → Domain OWNS (registrar evidence absent).

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Total in scope | **2** |
| Lifecycle **active** | **1** (REL-CORV-DM-02) |
| Lifecycle **replaced** | **1** (REL-CORV-DM-01) |
| Attestation | **Complete** — AT-CORV-REL-01; correction AT-CORV-REL-02 |

---

## 2. Relationship roster — full table

| relationship_id | source_id | target_id | relationship_type | evidence_tier | lifecycle_state | attestation | notes |
|-----------------|-----------|-----------|-------------------|---------------|-----------------|-------------|-------|
| REL-CORV-DM-01 | DOM-CORV-01 corvonero.ru | WEB-CORV-01 lk.corvonero.ru | **SECONDARY_DOMAIN** | **E0** | **replaced** | AT-CORV-REL-01 | **Superseded** AT-CORV-REL-02 — apex zone is **not** alias hostname for subdomain site; `replaced_by` → REL-CORV-DM-02 |
| REL-CORV-DM-02 | DOM-CORV-01 corvonero.ru | WEB-CORV-01 lk.corvonero.ru | **POINTS_TO** | **E0** | **active** | AT-CORV-REL-02 | Apex DNS zone `corvonero.ru` hosts subdomain hostname `lk.corvonero.ru` where WEB-CORV-01 is served — **not** registrar proof; owner/registrant **SAFE UNKNOWN** |

---

## 3. Semantic mapping note

| Intake signal | Prior mapping | Corrected mapping | Rationale |
|---------------|---------------|-------------------|-----------|
| WEB **PART_OF** DOM | **SECONDARY_DOMAIN** (Domain → Website) | **POINTS_TO** (Domain → Website) | [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7 — **SECONDARY_DOMAIN** = alias / additional hostname; `corvonero.ru` is **apex zone**, not alias of `lk.corvonero.ru` |
| Site primary hostname | — | `lk.corvonero.ru` on WEB-CORV-01 | **PRIMARY_DOMAIN** not used — site FQDN is subdomain; separate DOM for `lk.*` **not** minted per intake charter |
| Apex vs subdomain direction | Domain → Website | **Unchanged** | Pair `Domain` → `Website` per taxonomy §7 |

**Final semantics:** DOM-CORV-01 (`corvonero.ru`, apex) ──**POINTS_TO**──► WEB-CORV-01 (`lk.corvonero.ru`) — structural DNS-zone / hostname association only; **no** ownership or alias claim.

---

## 4. Correction register

| correction_id | target | action | prior | post | attestation |
|---------------|--------|--------|-------|------|-------------|
| COR-CORV-DM-01 | REL-CORV-DM-01 | **Supersede** SECONDARY_DOMAIN | **active** | **replaced** → REL-CORV-DM-02 | AT-CORV-REL-02 |
| COR-CORV-DM-02 | REL-CORV-DM-02 | **Mint successor** POINTS_TO | — | **active** | AT-CORV-REL-02 |

---

## 5. Excluded register

| Item | Reason |
|------|--------|
| ORG-0009 → DOM-CORV-01 **OWNS** | Domain owner **SAFE UNKNOWN** — no WHOIS/registrar evidence |
| DOM for `lk.corvonero.ru` as separate FQDN entity | Intake charter — single apex DOM only |
| DOM-CORV-01 → WEB-CORV-01 **PRIMARY_DOMAIN** | Hostname mismatch — site FQDN is subdomain, not apex |
| DOM-CORV-01 → WEB-CORV-01 **SECONDARY_DOMAIN** *(active)* | **Withdrawn** — semantically incorrect for apex/subdomain case |

---

*ATLAS Corvonero Domain Relationship Register v1 — REL-CORV-DM-02 **active** (POINTS_TO); REL-CORV-DM-01 **replaced**.*
