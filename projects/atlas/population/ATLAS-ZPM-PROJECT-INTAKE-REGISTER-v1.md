# ATLAS ZPM Project Intake Register v1

**Status:** **documented** — intake register for ORG-0005 Project candidates (pre-population).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md](ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** canonical Project registry, attested export, `PRJ-*` assignment.

**Organization:** ORG-0005 **ЗПМ** · LE-0004 ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Historical project candidates | **1** |
| Current active project candidates | **1** |
| Future candidates (hold) | **4** |
| Rejected candidates | **7+** |
| **Recommended Wave 3 roster** | **2** |
| `PRJ-*` assigned | **0** *(intake only)* |

---

## 2. Historical project candidates

| intake_label | proposed_canonical_name | commissioning_org | execution_org | related_property | target_lifecycle | evidence_tier | evidence_ref | intake_verdict | wave_3_roster |
|--------------|-------------------------|-------------------|---------------|------------------|------------------|---------------|--------------|----------------|---------------|
| ZPM-INTAKE-CAND-H01 | Сайт bzpm.ru (исходная версия) | ORG-0005 ЗПМ | ORG-0001 Полигон | `bzpm.ru` *(WEB candidate)* | **deprecated** | **E0** | EV-ZPM-OP-HIST-01 | **Accept** | **Yes — P1** |

**Notes:** Completed delivery ~5 years ago; WP + The7 + Custom; production. CC §17 corroborates org website hostname only.

---

## 3. Current active project candidates

| intake_label | proposed_canonical_name | commissioning_org | execution_org | related_property | target_lifecycle | evidence_tier | evidence_ref | intake_verdict | wave_3_roster |
|--------------|-------------------------|-------------------|---------------|------------------|------------------|---------------|--------------|----------------|---------------|
| ZPM-INTAKE-CAND-A01 | Каталог-платформа bzpm.ru | ORG-0005 ЗПМ | ORG-0001 Полигон | `bzpm.ru` *(WEB candidate)* | **active** | **E0** | EV-ZPM-OP-ACT-01 | **Accept** | **Yes — P0** |

**Notes:** Full new version; catalog platform goal; almost complete; technical/design/UX refinements remain; Polygon active WIP.

---

## 4. Future candidates

| intake_label | description | evidence_ref | start_evidence | intake_verdict | wave_3_roster |
|--------------|-------------|--------------|----------------|----------------|---------------|
| ZPM-INTAKE-FUT-01 | SEO (ZPM / bzpm.ru) | EV-ZPM-OP-FUT-01 | **None** | **Future Candidate — hold** | **No** |
| ZPM-INTAKE-FUT-02 | Контекстная реклама | EV-ZPM-OP-FUT-01 | **None** | **Future Candidate — hold** | **No** |
| ZPM-INTAKE-FUT-03 | AI automation (ZPM) | EV-ZPM-OP-FUT-01 | **None** | **Future Candidate — hold** | **No** |
| ZPM-INTAKE-FUT-04 | OpenCartPilot-assisted maintenance | EV-ZPM-OP-FUT-01 | **None** | **Future Candidate — hold** | **No** |

---

## 5. Rejected candidates

| rejected_label | description | rejection_class | basis |
|----------------|-------------|-----------------|-------|
| REJ-ZPM-PRJ-01 | BZPM / SITE-001 OpenCart dealership | Identity pollution | COR-W1B-03; EFV-02 |
| REJ-ZPM-PRJ-02 | OCPilot read-only audit | MARS program / no project | Wave 3 §5.1; W1B §11 superseded |
| REJ-ZPM-PRJ-03 | MARS `ocpilot`, `ear-runtime`, … | E-17 excluded | [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) §5.1 |
| REJ-ZPM-PRJ-04 | Single merged bzpm.ru Project (hist+current) | Inference | EFV-03 |
| REJ-ZPM-PRJ-05 | `bzpm.ru` hostname alone | Class boundary | Website ≠ Project |
| REJ-ZPM-PRJ-06 | ORG-0005 as Project | Class boundary | Entity taxonomy §3 |
| REJ-ZPM-PRJ-07 | Dataset v0.4 draft rows | No evidence | Projects sheet — no ZPM rows |

---

## 6. Recommended Wave 3 roster

| roster_priority | intake_label | proposed_canonical_name | population_slice | target_lifecycle | evidence_tier | attestation_readiness *(population)* |
|-----------------|--------------|-------------------------|--------------------|------------------|---------------|--------------------------------------|
| **P0** | ZPM-INTAKE-CAND-A01 | Каталог-платформа bzpm.ru | client_delivery | **active** | E0 | **ready (E0)** |
| **P1** | ZPM-INTAKE-CAND-H01 | Сайт bzpm.ru (исходная версия) | client_delivery | **deprecated** | E0 | **ready (E0)** |

**Prerequisites satisfied:**

| Prerequisite | Status |
|--------------|--------|
| ORG-0005 **active** | **Pass** — AT-W1B-01 |
| Wave 2 ZPM Persons **active** | **Pass** — PER-0014, PER-0015 |
| Wave 2B ZPM relationships **active** | **Pass** — AT-W2B-ZPM-01 |
| Evidence-first intake complete | **Pass** — this register |

---

## 7. Duplicate review index

| review_id | verdict | register impact |
|-----------|---------|-----------------|
| ZPM-PRJ-D-01 | **Not duplicate** — H01 vs A01 | Both on roster |
| ZPM-PRJ-D-02 | **Distinct** — A01 vs FUT-01 | Future held |
| ZPM-PRJ-D-03 | **Class boundary** | WEB deferred Wave 4 |
| ZPM-PRJ-D-04 | **Distinct org** vs Triumph | No collision |
| ZPM-PRJ-D-05 | **Reject** SITE-001 | Not on roster |
| ZPM-PRJ-D-06 | **Open — low** naming | Steward at population |

**Duplicate review summary:** **Pass**

---

## 8. SAFE UNKNOWN index

| id | topic | blocks_intake |
|----|-------|---------------|
| SU-ZPM-PRJ-01 | Historical contract dates | **No** |
| SU-ZPM-PRJ-02 | Formal acceptance docs (E1 path) | **No** |
| SU-ZPM-PRJ-03 | Deployment replace vs coexistence | **No** — Wave 4 |
| SU-ZPM-PRJ-04 | Final canonical name strings | **No** |
| SU-ZPM-PRJ-05 | OCPilot scope if FUT-04 approved | **No** |
| SU-ZPM-PRJ-06 | Person ↔ Project edges | **No** — out of scope |
| SU-ZPM-PRJ-07 | CLIENT_OF commercial edge | **No** — Wave 6 |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md](ATLAS-ZPM-PROJECT-INTAKE-ANALYSIS-v1.md) | Full analysis |
| [ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md](ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md) | Summary |

---

*ATLAS ZPM Project Intake Register v1 — pre-population intake only.*
