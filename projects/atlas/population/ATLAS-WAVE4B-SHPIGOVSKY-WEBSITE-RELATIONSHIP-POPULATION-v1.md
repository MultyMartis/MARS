# ATLAS Wave 4B Shpigovsky Website Relationship Population v1

**Status:** **documented** — canonical Website-family relationship population plan for Wave 4B Shpigovsky tranche (ORG-0008).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-REGISTER-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 5 execution.

**Prerequisites (operator-confirmed):**

- Wave 4 Shpigovsky Website attestation: **COMPLETE** — AT-W4-SHPIG-01 (WEB-SHPIG-01 **active**)
- Population verdict: **READY FOR WAVE 4B SHPIGOVSKY WEBSITE RELATIONSHIP POPULATION**

**Binding operator scope:**

- **REL-SHPIG-WB-01, REL-SHPIG-WB-02** — approved list only.
- **OPERATES** ORG-0001 → WEB-SHPIG-01 — **не создавать** (SAFE UNKNOWN).
- Domain / PRIMARY_DOMAIN — **не создавать**.

---

## 1. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **2** |
| Website endpoints | **1** (WEB-SHPIG-01 **active**) |
| Relationship types | **BELONGS_TO**, **OWNS** |

### 1.1 Summary table

| relationship_id | source_id | target_id | relationship_type | attestation readiness |
|-----------------|-----------|-----------|-------------------|-----------------------|
| REL-SHPIG-WB-01 | WEB-SHPIG-01 shpigovsky.ru | PRJ-0012 Сайт shpigovsky.ru | **BELONGS_TO** | **ready** |
| REL-SHPIG-WB-02 | ORG-0008 ООО «Сознание» | WEB-SHPIG-01 shpigovsky.ru | **OWNS** | **ready** |

---

## 2. Structural graph (target)

```text
ORG-0008 ООО «Сознание»
    └── OWNS (REL-SHPIG-WB-02)
        ▼
WEB-SHPIG-01 shpigovsky.ru  [corporate_website · production]
    └── BELONGS_TO (REL-SHPIG-WB-01)
        ▼
PRJ-0012 Сайт shpigovsky.ru
```

---

## 3. Evidence basis

| Ref | Tier | Relationships |
|-----|------|---------------|
| EV-SHPIG-OP-01 | E0 | REL-SHPIG-WB-01, REL-SHPIG-WB-02 |
| EV-SHPIG-WEB-01 | E2 | REL-SHPIG-WB-01, REL-SHPIG-WB-02 |
| AT-W4-SHPIG-01 | attestation | Both edges |
| AT-W3-SHPIG-01 | attestation | REL-SHPIG-WB-01 |
| AT-W1D-SHPIG-01 | attestation | REL-SHPIG-WB-02 |

---

## 4. Explicit exclusions

| Item | Treatment |
|------|-----------|
| ORG-0001 OPERATES WEB-SHPIG-01 | **Excluded** — SAFE UNKNOWN |
| DOM-* / PRIMARY_DOMAIN | **Excluded** — Waves 5 / 5B |
| Person → Website | **Excluded** |
| CLIENT_OF | **Deferred** — Wave 6 |

---

*ATLAS Wave 4B Shpigovsky Website Relationship Population v1 — documentation only.*
