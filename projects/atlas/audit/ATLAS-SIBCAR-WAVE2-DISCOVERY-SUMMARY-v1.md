# ATLAS SIBCAR Wave 2 Person Discovery Summary v1

**Status:** **documented** — Person discovery preparation summary (audit only; no registry modifications).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Scope:** ORG-0006 **SIBCAR** — Person and operational-role gap vs ZPM; anchors ORG-0006, LE-0005, PRJ-0011, REL-0041  
**Parent:** [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) · [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md)  
**Is not:** population pass, attestation act, entity creation, runtime export, git commit.

---

## Final verdict

```text
READY FOR OPERATOR DISCOVERY SESSION
```

SIBCAR slice имеет **полный structural stack** (ORG, LE, PRJ-0011, WEB-SIBCAR-01, REL-0041) **без** Person layer. Discovery package фиксирует **1** CC-backed кандидата и **12** пробелов operational roles относительно ZPM. Population **не авторизована** данным пакетом.

---

## 1. Person statistics (SIBCAR slice)

| Category | Count | Notes |
|----------|-------|-------|
| Attested Person (PER-*) | **0** | ZPM reference: **2** |
| E1 CC-backed candidates | **1** | Карандашов Максим Петрович |
| E0 operator-direct candidates | **0** documented | ZPM: PER-0014 |
| Person→Organization edges | **0** | ZPM: REL-ZPM-01, REL-ZPM-02 |
| `primary_contact_person_id` on ORG-0006 | **SAFE UNKNOWN** | ZPM: PER-0014 |

---

## 2. Known persons inventory (summary)

| ID / candidate | Name | Source | Role signals | Status |
|----------------|------|--------|--------------|--------|
| **CAND-SIBCAR-P01** → PER-0016 *(proposed)* | Карандашов Максим Петрович | EV-W1C-CC-01 §22, §24 | Руководитель; Главный бухгалтер; title exact **UNKNOWN** | **Wave 2 candidate** |
| **CAND-SIBCAR-P02** → PER-0017 *(conditional)* | **SAFE UNKNOWN** | EV-W2C-SIBCAR-OP-01 **TBD** | Operational contact *(if exists)* | **Not queued** |

**Org-level only:** email `info_sibcar@mail.ru` (§16); phone **UNKNOWN**; EDO id **UNKNOWN**.

---

## 3. Missing operational roles (summary)

| Gap | ZPM has | SIBCAR lacks |
|-----|---------|--------------|
| GENERAL_DIRECTOR edge | REL-ZPM-01 | REL-SIBCAR-01 *(not authored)* |
| REPRESENTATIVE edge | REL-ZPM-02 | REL-SIBCAR-02 *(conditional)* |
| Primary operational contact | PER-0014 designated | **SAFE UNKNOWN** |
| Org contact pointer | `primary_contact_person_id` | **Unset** |
| Operator mission evidence | EV-W2-ZPM-OP-01 | **Missing** |
| Wave 2C doc pack | 7 files attested | **0 files** |

**Not missing (by design):** Person↔Project, Person↔Website — excluded in Waves 3–4B attestation acts.

---

## 4. Required operator questions (summary)

**Blocking (4):**

1. **OQ-W2C-01** — Карандашов = единственный операционный контакт?
2. **OQ-W2C-02** — Точная должность на CC?
3. **OQ-W2C-03** — Кто принимает работу от Полигона?
4. **OQ-W2C-04** — Подтверждение PER-0016 для Карандашова?

**High (4):** телефон, мессенджер, email контакта, mapping org email.

**Medium (4):** второе E0-лицо, доверенное лицо, single-person model.

**Low (2):** Diadoc подписант, обновление CC.

Полный реестр: [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md) §5.

---

## 5. Recommended Wave 2 population sequence (summary)

| Phase | Actions |
|-------|---------|
| **A — Discovery** *(this package)* | Operator Q&A → **EV-W2C-SIBCAR-OP-01** |
| **B — Authoring** | Person Population / Register / Attestation plan; duplicate batch W2C-SIBCAR-D-* |
| **C — Person attestation** | AT-W2C-SIBCAR-01 PER-0016 first; optional AT-W2C-SIBCAR-02 second person |
| **D — Relationship pass** | REL-SIBCAR-01 (+ optional REL-SIBCAR-02); set `primary_contact_person_id` |
| **E — Sync** | Slice consistency audit; backup refresh |

**Prerequisites met:** ORG-0006 **active** (AT-W1C-01) · LE-0005 **active** · CC present · Wave 1C duplicate review **Pass**.

---

## 6. Anchor entity Person posture

| Entity | Lifecycle | Person relevance |
|--------|-----------|------------------|
| **ORG-0006** SIBCAR | **active** | Anchor; no PER-* linked |
| **LE-0005** ООО «СибКар» | **active** | Signatory name on LE — not Person entity |
| **PRJ-0011** OpenCart dealership | **active** | No Person↔Project edges |
| **REL-0041** CLIENT_OF | **active** | Commercial org↔org — not Person role |

---

## 7. Parity vs ZPM

| Metric | ZPM | SIBCAR |
|--------|-----|--------|
| Person entities | 2 active | 0 |
| Person→Org edges | 2 active | 0 |
| Parity checklist pass | 12/12 *(post-Wave 2B)* | **2/12** |
| Structural stack without Person | Required Person prereq | Person **optional** — documented delta |

**Interpretation:** SIBCAR may adopt **minimal single-person model** (PER-0016 only) or **ZPM two-person model** — operator decision via OQ-W2C-01 / OQ-W2C-14.

---

## 8. Findings summary

| Severity | Count | IDs |
|----------|-------|-----|
| **High** | 4 | SIBCAR-W2D-01..04 |
| **Medium** | 3 | SIBCAR-W2D-05..07 |
| **Low** | 2 | SIBCAR-W2D-08..09 |
| **Info** | 3 | SIBCAR-W2D-10..12 |

**Blocking contradictions:** **0** — structural SIBCAR graph consistent; Person layer simply absent.

---

## 9. Next actions (documentation track)

| Priority | Action | Owner |
|----------|--------|-------|
| **P0** | Operator discovery session — OQ-W2C-01..14 | Operator + Steward |
| **P0** | Record **EV-W2C-SIBCAR-OP-01** | Steward |
| **P1** | Decide single- vs two-person model | Operator |
| **P2** | Author Wave 2C Person doc pack *(separate task)* | Steward |
| **P3** | Parallel: Wave 5 DOM-SIBCAR-01 attestation *(orthogonal)* | Steward |

**Not in scope:** population, attestation, entity mint, graph changes, Foundation changes, commit, push.

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-AUDIT-v1.md) | Full audit |
| [ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md](ATLAS-SIBCAR-WAVE2-DISCOVERY-REGISTER-v1.md) | Discovery register |
| [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ORGANIZATION-POPULATION-v1.md) | §8 Candidate Persons |
| [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](../population/ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | Parity reference |

---

*ATLAS SIBCAR Wave 2 Person Discovery Summary v1 — audit only.*
