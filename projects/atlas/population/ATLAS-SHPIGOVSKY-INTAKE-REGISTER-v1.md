# ATLAS Shpigovsky Intake Register v1

**Status:** **documented** — Polygon client project intake register (pre-population).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Intake slug:** `shpigovsky`  
**Parent:** [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** canonical Organization registry, Project registry, attested export, `ORG-*` / `LE-*` / `PER-*` / `PRJ-*` / `WEB-*` / `DOM-*` / `REL-*` assignment.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Organization intake candidates | **1** |
| Legal Entity intake candidates *(proposed)* | **1** |
| Project intake candidates | **1** |
| Future project candidates | **2** |
| Person intake candidates *(reference)* | **2** |
| Attested Person references *(no mint)* | **1** (PER-0010) |
| Website asset candidates | **4** *(paths on one host)* |
| Domain asset candidates | **1** |
| Relationships created | **0** |
| `ORG-*` assigned | **0** |
| `LE-*` assigned | **0** |
| `PER-*` assigned | **0** |
| `PRJ-*` assigned | **0** |
| Counterparty Card files | **0** |
| Evidence tier (intake) | **E0** + **E2** (website) |

---

## 2. Operational context register *(informational — no edges)*

| Field | Value | evidence_ref |
|-------|-------|--------------|
| Delivery organization | **ORG-0001** Веб-студия «Полигон» *(attested reference)* | EV-SHPIG-OP-01 |
| Project channel | **Polygon client delivery** | EV-SHPIG-OP-01 |
| i-SEO project classification | **Excluded** | EV-SHPIG-OP-01 |
| Acquisition | **Ольга Дягилева** (PER-0010) | EV-SHPIG-OP-01 |
| Olga roles | Client comms; coordination; SEO supervision; primary acceptance | EV-SHPIG-OP-01 |
| Operator roles | Frontend; WordPress; technical delivery | EV-SHPIG-OP-01 |
| Planned consumers | MARS; Website Factory; WP delivery; ACF; custom code; WP automation *(future)* | EV-SHPIG-OP-01 |

**No REL-* created.**

---

## 3. Delivery context register

| Field | Value | evidence_ref |
|-------|-------|--------------|
| Population slice | **client_delivery** | EV-SHPIG-OP-01 |
| Primary hostname | `shpigovsky.ru` | EV-SHPIG-OP-01; EV-SHPIG-WEB-01 |
| Stack | WordPress; possible ACF; possible custom programming | EV-SHPIG-OP-01 |
| Execution org | ORG-0001 Полигон | EV-SHPIG-OP-01 |
| Delivery phase | **SAFE UNKNOWN** | EV-SHPIG-OP-01 |

---

## 4. Client acquisition path register

| step | event | actor | edge_created |
|------|-------|-------|--------------|
| 1 | Client referral to Polygon | PER-0010 Ольга Дягилева | **No** |
| 2 | Delivery under Polygon org | ORG-0001 | **No** |
| 3 | Technical execution | Operator (steward) | **No** |
| 4 | Property target | shpigovsky.ru | **No** |

---

## 5. Known business facts register *(from shpigovsky.ru — E2)*

| fact_id | category | value | evidence_ref |
|---------|----------|-------|--------------|
| BF-SHPIG-01 | brand | Центр профилактики зависимостей **Шпиговский Дом** | EV-SHPIG-WEB-01 |
| BF-SHPIG-02 | positioning | Профилактика и лечение зависимостей (алкоголь, ПАВ, игры) | EV-SHPIG-WEB-01 |
| BF-SHPIG-03 | institution | Немедицинское социально-психологическое учреждение | EV-SHPIG-WEB-01 |
| BF-SHPIG-04 | legal signal | **ООО "Сознание"** — privacy policy operator | EV-SHPIG-WEB-02 |
| BF-SHPIG-05 | location | МО, район ЖД станции Катуар; приём в Москве | EV-SHPIG-WEB-01 |
| BF-SHPIG-06 | email | Info@shpigovsky.ru | EV-SHPIG-WEB-01; EV-SHPIG-WEB-02 |
| BF-SHPIG-07 | phones | +7 (925) 183-64-64; +7 (995) 023-92-26 | EV-SHPIG-WEB-01 |
| BF-SHPIG-08 | founder signal | Шпиговский Сергей Юрьевич — аддиктолог | EV-SHPIG-WEB-01 |

---

## 6. Organization intake candidates

| intake_label | org_slug | proposed_display_name | wave_tier *(target)* | business_role *(target)* | legal_entity | org_id | evidence_tier | evidence_ref | lifecycle | intake_verdict |
|--------------|----------|----------------------|----------------------|--------------------------|--------------|--------|---------------|--------------|-----------|----------------|
| SHPIGOVSKY-INTAKE-CAND-O01 | shpigovsky | **ООО «Сознание»** | W1-B *(proposed)* | CLIENT | SHPIGOVSKY-INTAKE-CAND-LE01 *(proposed)* | **none** | **E0+E2** | EV-SHPIG-OP-01; EV-SHPIG-WEB-02 | **intake** | **Hold — CC required** |

**Proposed trade aliases *(not attested):* Шпиговский Дом; Центр Сергея Шпиговского.

**CC requirement:**

| Field | Value |
|-------|-------|
| Required path | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\shpigovsky\` |
| Filesystem state (2026-06-10) | **Absent** |
| CPV status | Inventory complete — **0** non-placeholder files |

---

## 7. Legal Entity intake candidates *(not minted)*

| intake_label | proposed_legal_form | proposed_legal_name | INN | OGRN | le_id | org_binding | evidence_ref | intake_verdict |
|--------------|--------------------|--------------------|-----|------|-------|-------------|--------------|----------------|
| SHPIGOVSKY-INTAKE-CAND-LE01 | **ООО** *(E2 signal)* | **ООО «Сознание»** | **SAFE UNKNOWN** | **SAFE UNKNOWN** | **none** | SHPIGOVSKY-INTAKE-CAND-O01 | EV-SHPIG-WEB-02 | **Hold** — CC required |

---

## 8. Project intake candidates

| intake_label | proposed_name | class | slice | commissioning | execution | prj_id | evidence_ref | lifecycle *(target)* | intake_verdict |
|--------------|---------------|-------|-------|---------------|-----------|--------|--------------|----------------------|----------------|
| SHPIGOVSKY-INTAKE-CAND-PRJ-A01 | **Сайт shpigovsky.ru** | active delivery | client_delivery | SHPIGOVSKY-INTAKE-CAND-O01 | ORG-0001 | **none** | EV-SHPIG-OP-01 | **active** *(pending steward)* | **Hold** — org anchor + CC |

**Future candidates:**

| intake_label | description | verdict |
|--------------|-------------|---------|
| SHPIGOVSKY-INTAKE-FUT-01 | WP automation agents | **Hold** |
| SHPIGOVSKY-INTAKE-FUT-02 | Separate SEO initiative | **Hold** |

---

## 9. Candidate Website assets

| intake_label | hostname | url | org_binding | web_id | evidence_ref | intake_verdict |
|--------------|----------|-----|-------------|--------|--------------|----------------|
| SHPIGOVSKY-INTAKE-WEB-C01 | shpigovsky.ru | https://shpigovsky.ru/ | SHPIGOVSKY-INTAKE-CAND-O01 | **none** | EV-SHPIG-WEB-01 | **Candidate — Wave 4** |
| SHPIGOVSKY-INTAKE-WEB-C02 | shpigovsky.ru | https://shpigovsky.ru/policy | same | **none** | EV-SHPIG-WEB-02 | **Candidate — Wave 4** |
| SHPIGOVSKY-INTAKE-WEB-C03 | shpigovsky.ru | https://shpigovsky.ru/psy | same | **none** | EV-SHPIG-WEB-01 | **Candidate — Wave 4** |
| SHPIGOVSKY-INTAKE-WEB-C04 | shpigovsky.ru | https://shpigovsky.ru/home | same | **none** | EV-SHPIG-WEB-01 | **Candidate — Wave 4** |

**Explicit:** Do **not** mint `WEB-*` at intake.

---

## 10. Candidate Domain assets

| intake_label | domain | derived_from | dom_id | evidence_ref | intake_verdict |
|--------------|--------|--------------|--------|--------------|----------------|
| SHPIGOVSKY-INTAKE-DOM-C01 | shpigovsky.ru | SHPIGOVSKY-INTAKE-WEB-C01 | **none** | EV-SHPIG-WEB-01 | **Candidate — Wave 5** |

**Explicit:** Do **not** mint `DOM-*` at intake.

---

## 11. Person register

### 11.1 Attested reference *(no new mint)*

| person_id | canonical_name | intake_role | evidence_ref |
|-----------|----------------|-------------|--------------|
| PER-0010 | Дягилева Ольга | Acquisition; comms; coordination; SEO supervision; acceptance | EV-SHPIG-OP-01 |

### 11.2 Person intake candidates *(not minted)*

| intake_label | proposed_name | role_signal | person_id | evidence_ref | intake_verdict |
|--------------|---------------|-------------|-----------|--------------|----------------|
| SHPIGOVSKY-INTAKE-CAND-P01 | Шпиговский Сергей Юрьевич | Founder / аддиктолог | **none** | EV-SHPIG-WEB-01 | **Hold** |
| SHPIGOVSKY-INTAKE-CAND-P02 | Operator *(steward)* | Technical delivery | **none** | EV-SHPIG-OP-01 | **N/A** at intake |

---

## 12. Evidence index

| Ref | Artifact | Tier |
|-----|----------|------|
| EV-SHPIG-OP-01 | Operator intake statements (2026-06-10) | **E0** |
| EV-SHPIG-WEB-01 | Live capture homepage | **E2** |
| EV-SHPIG-WEB-02 | Live capture `/policy` | **E2** |
| *(pending)* | Counterparty Card — `…\shpigovsky\` | **E1+ expected** |

---

## 13. Duplicate review index

| review_id | compare | verdict | merge? |
|-----------|---------|---------|--------|
| SHPIG-D-01 | vs ORG-0001 Полигон | **Distinct** — vendor not client subject | **No** |
| SHPIG-D-02 | vs ORG-0002 MetaCode | **Distinct** | **No** |
| SHPIG-D-03 | vs ORG-0003 i-SEO | **Distinct** — channel excluded | **No** |
| SHPIG-D-04 | vs ORG-0004 Триумф | **Distinct** | **No** |
| SHPIG-D-05 | vs ORG-0005 ЗПМ | **Distinct** | **No** |
| SHPIG-D-06 | vs ORG-0006 SIBCAR | **Distinct** | **No** |
| SHPIG-D-07 | vs ORG-0007 Макита Снаб | **Distinct** | **No** |
| SHPIG-D-08 | `shpigovsky.ru` vs existing WEB-* hosts | **No collision** | **No** |
| INN/OGRN cross-check | CC absent | **Open** | Blocks **Pass** |

**Integrity:** ORG-0001..0007 **unchanged** · No merge **Pass**

---

## 14. SAFE UNKNOWN index

| id | topic | blocks_intake |
|----|-------|---------------|
| SU-SHPIG-01 | INN / KPP / OGRN | **Yes** |
| SU-SHPIG-02 | Legal vs trade name mapping | **Yes** |
| SU-SHPIG-03 | Contractual client contact | **No** |
| SU-SHPIG-04 | Delivery phase / completion | **No** |
| SU-SHPIG-05 | Client representative for Polygon | **No** |
| SU-SHPIG-06 | SEO scope boundaries | **No** |
| SU-SHPIG-07 | ACF / custom scope | **No** |
| SU-SHPIG-08 | Domain registrant | **No** |
| SU-SHPIG-09 | CLIENT_OF commercial edge | **No** |
| SU-SHPIG-10 | EXECUTES project edge | **No** |
| SU-SHPIG-11 | Olga role edges beyond PER-0010 | **No** |
| SU-SHPIG-12 | Greenfield vs redesign | **No** |
| SU-SHPIG-13 | WP automation scope | **No** |

---

## 15. Recommended population path register

| order | wave | action | blocked_by |
|-------|------|--------|------------|
| 1 | Pre | CC folder `shpigovsky\` | SU-SHPIG-01..02 |
| 2 | W1 | ORG-* + LE-* mint | CC |
| 3 | W2 | Client PER-* *(optional)* | CC contacts |
| 4 | W3 | PRJ-* mint | Org anchor |
| 5 | W3B | EXECUTES / COMMISSIONED_BY | PRJ + ORG |
| 6 | W4 | WEB-* for shpigovsky.ru | Org binding |
| 7 | W5 | DOM-* | Registrar evidence |
| 8 | W6 | CLIENT_OF → ORG-0001 | Commercial sign-off |

---

## 16. Readiness summary

| Gate | Status |
|------|--------|
| Intake register complete | **Pass** |
| EFV / CPV applied | **Pass** |
| CC folder inventory | **Pass** — documented absent |
| Organization population | **Blocked** |
| Project population | **Blocked** |
| **Overall** | **PARTIALLY READY** |

---

## 17. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) | Full analysis |
| [ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md](ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md) | Summary |

---

*ATLAS Shpigovsky Intake Register v1 — pre-population intake only.*
