# ATLAS Wave 4 Shpigovsky Website Active Attestation v1

**Status:** **attested** — first official Website active attestation for Wave 4 Shpigovsky tranche (ORG-0008).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-REGISTER-v1.md) · [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ATTESTATION-v1.md) · [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-SHPIGOVSKY-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3B-SHPIGOVSKY-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-SHPIGOVSKY-PROJECT-RELATIONSHIP-ATTESTATION-v1.md)  
**Is not:** runtime, API, database export, Wave 4B-SHPIG relationship attestation, Domain entities, Person ↔ Website edges, Foundation amendment.

---

# REPORT — ATLAS Wave 4 Shpigovsky Website Active Attestation

**Attestation date:** 2026-06-10  
**Tranche:** **AT-W4-SHPIG-01**  
**Promotion:** WEB-SHPIG-01 — **proposed** → **active**

---

## 1. Attestation result

Настоящий акт фиксирует **каноническую attestation** класса **Website** для Wave 4 tranche **Shpigovsky**: WEB-SHPIG-01 переведён в **active** canonical state.

### 1.1 Attestation tranche executed — AT-W4-SHPIG-01

| Step | Action | Evidence ref | Status |
|------|--------|--------------|--------|
| 1 | Verify ORG-0008 **active** | AT-W1D-SHPIG-01 | **Done** |
| 2 | Verify PRJ-0012 **active** | AT-W3-SHPIG-01 | **Done** |
| 3 | Verify REL-SHPIG-PJ-01..02 **active** | AT-W3B-SHPIG-01 | **Done** |
| 4 | Verify ORG-0005..0007 unchanged | Prior registers | **Done** |
| 5 | Duplicate scan SHPIG-WEB-D-01..05 | Register §4 | **Done** |
| 6 | Propose WEB-SHPIG-01 canonical name **shpigovsky.ru** | EV-SHPIG-WEB-01 | **Done** |
| 7 | Assign website_kind **corporate_website** | Operator scope | **Done** |
| 8 | Assign **E0/E2** | EV-SHPIG-OP-01; EV-SHPIG-WEB-01..02 | **Done** |
| 9 | Attest Website **active** | Steward (delegated) | **Done** |
| 10 | Queue 4B-SHPIG: REL-SHPIG-WB-01, REL-SHPIG-WB-02 | Population §5 | **Queued** |

### 1.2 Attestation results summary

| website_id | canonical_name | prior state | attested state | evidence_tier | tranche |
|------------|----------------|-------------|----------------|---------------|---------|
| WEB-SHPIG-01 | shpigovsky.ru | **proposed** | **active** | **E0/E2** | AT-W4-SHPIG-01 |

**Promotion count:** **1 / 1** Website record attested  
**Relationships created:** **0**  
**Domain entities created:** **0**

---

## 2. Attested entity record — WEB-SHPIG-01

| Field | Value |
|-------|-------|
| **website_id** | WEB-SHPIG-01 |
| **canonical_name** | shpigovsky.ru |
| **website_kind** | **corporate_website** |
| **url** | `https://shpigovsky.ru/` |
| **environment** | **production** |
| **primary organization** *(display)* | ORG-0008 ООО «Сознание» |
| **primary project** *(display)* | PRJ-0012 Сайт shpigovsky.ru |
| **evidence_tier** | **E0/E2** |
| **lifecycle_state (attested)** | **active** |

---

## 3. Validation results

| Check | Result |
|-------|--------|
| ORG-0008 **active** | **Pass** |
| PRJ-0012 **active** | **Pass** |
| REL-SHPIG-PJ-01..02 **active** | **Pass** |
| ZPM / SIBCAR / Makita unchanged | **Pass** |
| No Domain minted | **Pass** |
| No Person creation | **Pass** |
| No Foundation changes | **Pass** |
| EIR-W01 single property model | **Pass** |

---

## 4. Attestation verdict

```text
READY FOR WAVE 4B SHPIGOVSKY WEBSITE RELATIONSHIP POPULATION
```

**Supersedes:** **READY FOR WAVE 4 SHPIGOVSKY WEBSITE ATTESTATION** — [ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-SHPIGOVSKY-WEBSITE-ATTESTATION-v1.md) §4.

---

*ATLAS Wave 4 Shpigovsky Website Active Attestation v1 — documentation only.*
