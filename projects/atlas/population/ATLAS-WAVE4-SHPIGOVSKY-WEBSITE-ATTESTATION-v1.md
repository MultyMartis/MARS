# ATLAS Wave 4 Shpigovsky Website Attestation v1

**Status:** **documented** — Wave 4 Shpigovsky Website attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Organization anchor:** ORG-0008 **ООО «Сознание»**  
**Parent:** [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-REGISTER-v1.md) · [ATLAS-WAVE3B-SHPIGOVSKY-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SHPIGOVSKY-PROJECT-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** attestation runtime, executed attestation act, relationship attestation, Wave 4B-SHPIG execution.

**Prerequisites (operator-confirmed):**

- Wave 1D Shpigovsky Organization ORG-0008: **active** — AT-W1D-SHPIG-01
- Wave 3 Shpigovsky Project PRJ-0012: **active** — AT-W3-SHPIG-01
- Wave 3B Shpigovsky Project ↔ Organization: **COMPLETE** — AT-W3B-SHPIG-01
- Wave 4 Shpigovsky Population: **COMPLETE** — WEB-SHPIG-01 minted **proposed**

---

## 1. Website roster (attestation set)

| website_id | canonical_name | website_kind | url | evidence_tier | target lifecycle |
|------------|----------------|--------------|-----|---------------|------------------|
| WEB-SHPIG-01 | shpigovsky.ru | **corporate_website** | `https://shpigovsky.ru/` | **E0/E2** | **active** |

---

## 2. Attestation readiness

| website_id | Target state | Min tier | Readiness | Blocker |
|------------|--------------|----------|-----------|---------|
| WEB-SHPIG-01 | **active** | E0/E2 | **Ready** | — |

---

## 3. Attestation sequence — AT-W4-SHPIG-01

| Step | Action | Evidence ref |
|------|--------|--------------|
| 1 | Verify ORG-0008 **active** | AT-W1D-SHPIG-01 |
| 2 | Verify PRJ-0012 **active** | AT-W3-SHPIG-01 |
| 3 | Verify REL-SHPIG-PJ-01..02 **active** | AT-W3B-SHPIG-01 |
| 4 | Verify ORG-0005..0007 unchanged | Prior registers |
| 5 | Duplicate scan SHPIG-WEB-D-01..05 | Register §4 |
| 6 | Propose WEB-SHPIG-01 canonical name **shpigovsky.ru** | EV-SHPIG-WEB-01 |
| 7 | Assign website_kind **corporate_website** | Operator scope |
| 8 | Attest Website **active** | Steward |
| 9 | Queue 4B-SHPIG: REL-SHPIG-WB-01, REL-SHPIG-WB-02 | Population §5 |

---

## 4. Final verdict

```text
READY FOR WAVE 4 SHPIGOVSKY WEBSITE ATTESTATION
```

**Conditions:**

1. Execute **AT-W4-SHPIG-01** (WEB-SHPIG-01 **active**) — single P0 tranche.
2. Wave 4B-SHPIG relationship **active** promotion requires Website attestation act — separate pass.
3. Do **not** mint DOM-* or PRIMARY_DOMAIN in this package.

---

*ATLAS Wave 4 Shpigovsky Website Attestation v1 — attestation act superseded by ACTIVE-ATTESTATION upon execution.*
