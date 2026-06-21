# ATLAS Corvonero Relationship Attestation v1

**Status:** **documented** — consolidated attestation act for Corvonero relationship population (**corrected** 2026-06-21).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Is not:** Agreement attestation, Person edges, runtime activation.

---

## 1. Attestation scope

| Family | Relationships | Target lifecycle |
|--------|---------------|------------------|
| Commercial Org ↔ Org | REL-0042 | **active** |
| Project ↔ Org | REL-CORV-PJ-01 | **active** |
| Website ↔ Project | REL-CORV-WB-01 | **active** |
| Org ↔ Website | REL-CORV-WB-02 | **deprecated** *(OWNS withdrawn)* |
| Domain ↔ Website | REL-CORV-DM-02 | **active** |
| Domain ↔ Website *(historical)* | REL-CORV-DM-01 | **replaced** |

**Entity prerequisites:** ORG-0009, PRJ-0013, WEB-CORV-01, DOM-CORV-01, ORG-0003 — all **active** or attested in same pass.

---

## 2. Attestation acts

| attestation_id | relationships | evidence | verdict |
|----------------|---------------|----------|---------|
| **AT-CORV-REL-01** | REL-0042; REL-CORV-PJ-01; REL-CORV-WB-01; REL-CORV-WB-02; REL-CORV-DM-01 | EV-CORVONERO-OP-01; EV-CORVONERO-OP-02; endpoint attestation AT-CORV-ORG-01, AT-CORV-PRJ-01, AT-CORV-WEB-01, AT-CORV-DOM-01 | **superseded in part** by AT-CORV-REL-02 |
| **AT-CORV-REL-02** | REL-CORV-WB-02 **deprecated**; REL-CORV-DM-01 **replaced**; REL-CORV-DM-02 **active** | EV-CORVONERO-OP-01; EV-CORVONERO-OP-02; [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5, §7; [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) §4.2 | **complete** |

---

## 3. Taxonomy validation

| Relationship | Approved family | Result |
|--------------|-----------------|--------|
| CLIENT_OF | §2 Org ↔ Org | **Pass** |
| COMMISSIONED_BY | §3.2 Project → Org | **Pass** |
| BELONGS_TO | §6 Website → Project | **Pass** |
| OWNS *(REL-CORV-WB-02)* | §5 Org → Website | **Withdrawn** — owner SAFE UNKNOWN; edge **deprecated** |
| POINTS_TO *(REL-CORV-DM-02)* | §7 Domain → Website | **Pass** |
| SECONDARY_DOMAIN *(REL-CORV-DM-01)* | §7 Domain → Website | **Superseded** — incorrect alias semantics |

**New relationship types minted:** **0**

---

## 4. Excluded edges (confirmed)

| Edge | Reason |
|------|--------|
| ORG-0009 → ORG-0001 | Operator restriction |
| ORG-0009 → WEB-CORV-01 **OWNS** *(active)* | **Withdrawn** — REL-CORV-WB-02 deprecated |
| ORG-0009 → WEB-CORV-01 **OPERATES** | Operational control not attested |
| EXECUTES_PPC_FOR | Not in v1 taxonomy |
| ORG → DOM OWNS | Registrant SAFE UNKNOWN |
| Person ↔ Project | PPC executor — documentation note only |

---

*ATLAS Corvonero Relationship Attestation v1 — AT-CORV-REL-01 partial; AT-CORV-REL-02 **complete**.*
