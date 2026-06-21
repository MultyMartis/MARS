# ATLAS Corvonero Website Relationship Register v1

**Status:** **documented** — canonical Website-family relationship roster for Corvonero tranche (**active**; attestation complete; **corrected** 2026-06-21).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-21  
**Organization anchor:** ORG-0009 **Центр автоматизации «Корво Неро»**  
**Is not:** OPERATES edge, Person ↔ Website edges, active Org ↔ Website ownership edge.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Total in scope | **2** |
| Lifecycle **active** | **1** (REL-CORV-WB-01) |
| Lifecycle **deprecated** | **1** (REL-CORV-WB-02 — OWNS withdrawn) |
| Attestation | **Complete** — AT-CORV-REL-01; correction AT-CORV-REL-02 |

---

## 2. Relationship roster — full table

| relationship_id | source_id | target_id | relationship_type | evidence_tier | lifecycle_state | attestation | notes |
|-----------------|-----------|-----------|-------------------|---------------|-----------------|-------------|-------|
| REL-CORV-WB-01 | WEB-CORV-01 lk.corvonero.ru | PRJ-0013 Корво Неро — Яндекс Директ и посадочные страницы | **BELONGS_TO** | **E0** | **active** | AT-CORV-REL-01 | Landing surface grouped under Direct project |
| REL-CORV-WB-02 | ORG-0009 Центр автоматизации «Корво Неро» | WEB-CORV-01 lk.corvonero.ru | **OWNS** | **E0** | **deprecated** | AT-CORV-REL-01; **withdrawn** AT-CORV-REL-02 | **Correction:** OWNS asserted org-level property without attested site/Tilda owner — **invalid** per [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §5; no successor edge minted |

---

## 3. Org ↔ Website contextual note *(no active canonical edge)*

| Signal | Handling |
|--------|----------|
| Intake «site represents org» | **Documentation only** — not encoded as **OWNS** or **OPERATES** |
| Website owner field | **SAFE UNKNOWN** — unchanged on WEB-CORV-01 |
| Structural grouping path | WEB-CORV-01 ──**BELONGS_TO**──► PRJ-0013 ──**COMMISSIONED_BY**──► ORG-0009 |

**Contextual note:** WEB-CORV-01 используется как сайт Центра автоматизации «Корво Неро»; юридическое и техническое владение **SAFE UNKNOWN**.

---

## 4. Correction register

| correction_id | target | action | prior | post | attestation |
|---------------|--------|--------|-------|------|-------------|
| COR-CORV-WB-01 | REL-CORV-WB-02 | **Withdraw** OWNS edge | **active** | **deprecated** | AT-CORV-REL-02 |

**Rationale:** [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) §4.2 / §5 — wrong type for evidence tier; **OPERATES** not substituted (would assert unconfirmed operational control).

---

## 5. Excluded register

| Item | Reason |
|------|--------|
| ORG-0009 **OPERATES** WEB-CORV-01 | Operational control **not attested** |
| ORG-0001 **OPERATES** WEB-CORV-01 | Not attested |
| Person → Website **OWNS** | Site owner **SAFE UNKNOWN** |
| PRIMARY_DOMAIN / SECONDARY_DOMAIN | Domain-family — see domain relationship register |

---

*ATLAS Corvonero Website Relationship Register v1 — REL-CORV-WB-01 **active**; REL-CORV-WB-02 **deprecated** (OWNS withdrawn).*
