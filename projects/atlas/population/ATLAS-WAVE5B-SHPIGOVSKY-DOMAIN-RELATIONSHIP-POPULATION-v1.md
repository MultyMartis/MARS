# ATLAS Wave 5B Shpigovsky Domain Relationship Population v1

**Status:** **documented** — canonical Domain-family relationship population plan for Wave 5B Shpigovsky tranche (ORG-0008).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-WAVE5-SHPIGOVSKY-DOMAIN-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE5-SHPIGOVSKY-DOMAIN-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE5-SHPIGOVSKY-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-SHPIGOVSKY-DOMAIN-REGISTER-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act.

**Prerequisites (operator-confirmed):**

- Wave 5 Shpigovsky Domain attestation: **COMPLETE** — AT-W5-SHPIG-01 (DOM-SHPIG-01 **active**)
- Population verdict: **READY FOR WAVE 5B SHPIGOVSKY DOMAIN RELATIONSHIP POPULATION**

**Binding operator scope (critical):**

- **REL-SHPIG-DM-01** — PRIMARY_DOMAIN only; approved list.
- **ORG-0008 → DOM-SHPIG-01 OWNS** — **DO NOT CREATE** (registrar evidence absent; SAFE UNKNOWN).
- SECONDARY_DOMAIN / REDIRECTS_TO / CUSTODIAN — **не создавать**.

---

## 1. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **1** |
| Domain endpoints | **1** (DOM-SHPIG-01 **active**) |
| Website endpoints | **1** (WEB-SHPIG-01 **active**) |
| Relationship types | **PRIMARY_DOMAIN** |

### 1.1 Summary table

| relationship_id | source_id | target_id | relationship_type | attestation readiness |
|-----------------|-----------|-----------|-------------------|-----------------------|
| REL-SHPIG-DM-01 | DOM-SHPIG-01 shpigovsky.ru | WEB-SHPIG-01 shpigovsky.ru | **PRIMARY_DOMAIN** | **ready** |

---

## 2. Per-relationship analysis — REL-SHPIG-DM-01

| Field | Value |
|-------|-------|
| **relationship_id** | REL-SHPIG-DM-01 |
| **source_id** | DOM-SHPIG-01 shpigovsky.ru |
| **target_id** | WEB-SHPIG-01 shpigovsky.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | DOM-SHPIG-01 **active** (AT-W5-SHPIG-01); WEB-SHPIG-01 **active** (AT-W4-SHPIG-01); co-terminous apex hostname; E0/E2 evidence path |
| **evidence_tier** | **E0/E2** |
| **lifecycle_state (target)** | **active** |
| **notes** | Links hostname anchor to web property; does **not** attest registrar ownership |

---

## 3. Explicit exclusions (operator binding)

| Item | Treatment | Reason |
|------|-----------|--------|
| ORG-0008 → DOM-SHPIG-01 **OWNS** | **DO NOT CREATE** | Registrar evidence absent |
| ORG-0001 CUSTODIAN / OPERATES | **Excluded** | SAFE UNKNOWN |
| SECONDARY_DOMAIN `www.shpigovsky.ru` | **Deferred** | Hostname policy not evidenced |
| Person ↔ Domain | **Excluded** | Operator scope |

---

## 4. Target structural graph (post-5B)

```text
DOM-SHPIG-01 shpigovsky.ru
    └── PRIMARY_DOMAIN (REL-SHPIG-DM-01)
        ▼
WEB-SHPIG-01 shpigovsky.ru
    ├── OWNS ◄── ORG-0008 (REL-SHPIG-WB-02)  [Website-family]
    └── BELONGS_TO ──► PRJ-0012 (REL-SHPIG-WB-01)

(No ORG-0008 ──OWNS──► DOM-SHPIG-01 — registrar evidence absent)
```

---

*ATLAS Wave 5B Shpigovsky Domain Relationship Population v1 — documentation only.*
