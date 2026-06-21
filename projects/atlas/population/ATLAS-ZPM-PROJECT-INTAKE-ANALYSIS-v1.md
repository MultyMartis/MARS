# ATLAS ZPM Project Intake Analysis v1

**Status:** **documented** — Project intake analysis only (no population, no attestation).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004 ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»  
**Parent:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md)  
**Is not:** Project population, Project attestation, relationship creation, `PRJ-*` minting, Wave 3B execution.

**Governance applied:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-01..06.

**Explicit exclusions (this package):**

- No `PRJ-*` identifiers assigned
- No Project attestation
- No COMMISSIONED_BY / EXECUTES / BELONGS_TO edges
- No Website (`WEB-*`) or Domain (`DOM-*`) population

---

## 1. Purpose

Определить, **какие Project entities фактически существуют** для ORG-0005 ЗПМ **до** Wave 3 Population tranche ZPM — классификация кандидатов по evidence, без mint и без attestation.

**Operator evidence scope (binding for this analysis):**

| Block | Content |
|-------|---------|
| Historical website | `bzpm.ru` — создан Polygon ~5 лет назад; WP + The7 + Custom; **завершён и в production** |
| Current website project | `bzpm.ru` — клиент вернулся на **полную новую версию**; цель — каталог-платформа; **почти завершено**; Polygon; **active WIP** |
| Future possibilities | SEO; контекстная реклама; AI automation; OpenCartPilot maintenance — **возможности без старта** |

---

## 2. Evidence inventory

### 2.1 Cited sources

| Ref | Artifact | Tier | Role in this analysis |
|-----|----------|------|------------------------|
| **EV-W1B-CC-01** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx` | **E1** | Org identity; CC §17 **Bzpm.ru** — org website pointer; **не** границы Project |
| **EV-ZPM-OP-HIST-01** | Operator statement — historical `bzpm.ru` delivery | **E0** | Completed website initiative (~5 years; WP + The7 + Custom; production) |
| **EV-ZPM-OP-ACT-01** | Operator statement — current catalog rebuild | **E0** | Active delivery; catalog platform goal; almost complete; Polygon executes |
| **EV-ZPM-OP-FUT-01** | Operator statement — future possibilities only | **E0** | Explicit **no approved project** / no start evidence |
| **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0005 endpoint **active** |
| **AT-W2B-ZPM-01** | [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) | attestation | Person endpoints **active**; vendor context ORG-0001 Полигон |

### 2.2 Evidence-first pre-check

| EFV rule | Application |
|----------|-------------|
| **EFV-02** | OCPilot SITE-001, EAR Connected track, `sibcar.new-site.space` — **не** использованы как Project evidence |
| **EFV-03** | Hostname `bzpm.ru` **не** доказывает один Project; два operator-described delivery phases → **два** intake-кандидата |
| **EFV-04** | CC прочитан; org website §17 corroborates property, **не** substitute для project boundaries |
| **EFV-06** | Каждый verdict ниже: **claim → evidence ref → field quote** |

**Dataset note:** [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) Projects sheet — **нет** строк ZPM/BZPM. Intake опирается на operator evidence, не на draft dataset rows.

---

## 3. Classification — historical project candidates

### 3.1 ZPM-INTAKE-CAND-H01 — Исходный сайт bzpm.ru

| Field | Value |
|-------|-------|
| **Intake label** | ZPM-INTAKE-CAND-H01 |
| **Proposed canonical name** | **Сайт bzpm.ru (исходная версия)** *(steward may refine at population)* |
| **Class** | **Historical project candidate** → target lifecycle **deprecated** |
| **Population slice** | **client_delivery** |
| **Commissioning org** | ORG-0005 ЗПМ |
| **Execution org** | ORG-0001 Веб-студия «Полигон» *(operator: Polygon created)* |
| **Related property** | `bzpm.ru` — **Website candidate** (Wave 4), not Project substitute |
| **Technology context** | WordPress + The7 + Custom development |
| **Delivery verdict** | **Completed** — in production |
| **Approximate age** | ~5 years *(operator estimate — not contract-dated)* |
| **Evidence** | **E0** EV-ZPM-OP-HIST-01 |
| **CC corroboration** | **Indirect only** — EV-W1B-CC-01 §17 names org website **Bzpm.ru**; does **not** name delivery phase or completion |
| **Attestation readiness** | **Ready for population proposal** at **E0** — steward-known completed client delivery (analog: PRJ-0004 Triumph redesign) |
| **Lifecycle rationale** | Completed delivery → **deprecated** project container; live site persists under future **WEB-*** (Wave 4), not under active project |

**Claim → evidence:**

- «Polygon создал сайт ~5 лет назад, проект завершён, в production» → **EV-ZPM-OP-HIST-01** → operator historical block
- «Стек WP + The7 + Custom» → **EV-ZPM-OP-HIST-01** → operator historical block

---

## 4. Classification — current active project candidates

### 4.1 ZPM-INTAKE-CAND-A01 — Каталог-платформа bzpm.ru

| Field | Value |
|-------|-------|
| **Intake label** | ZPM-INTAKE-CAND-A01 |
| **Proposed canonical name** | **Каталог-платформа bzpm.ru** *(steward may refine: «Новая версия сайта bzpm.ru»)* |
| **Class** | **Current active project candidate** → target lifecycle **active** |
| **Population slice** | **client_delivery** |
| **Commissioning org** | ORG-0005 ЗПМ |
| **Execution org** | ORG-0001 Полигон *(operator: Polygon; active WIP)* |
| **Goal (operator)** | Transform website into **full catalog platform** |
| **Delivery state** | **Almost completed** — remaining: technical refinements, design improvements, UX polishing |
| **Status** | **Active work in progress** |
| **Related property** | Same hostname `bzpm.ru` — **same Website entity candidate** as H01; **different Project initiative** |
| **Evidence** | **E0** EV-ZPM-OP-ACT-01 |
| **CC corroboration** | **None** for project scope — CC does not describe catalog rebuild |
| **Attestation readiness** | **Ready for population proposal** at **E0** — operator-confirmed ongoing client delivery |
| **Lifecycle rationale** | Ongoing initiative with residual work → **active** (analog: PRJ-0005..0008 Triumph) |

**Claim → evidence:**

- «Клиент вернулся на полную новую версию» → **EV-ZPM-OP-ACT-01**
- «Цель — каталог-платформа; почти завершено; Polygon; active WIP» → **EV-ZPM-OP-ACT-01**

**Scope boundary:** Remaining tasks (technical / design / UX) are **operator narrative**, not ATLAS task objects ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 — no sprints/% complete).

---

## 5. Classification — future candidates

**Rule:** Possibilities without approved project entity and without start evidence → **Future Candidate** only. **Do not** mint Project rows.

| Intake label | Description | Evidence | Verdict |
|--------------|-------------|----------|---------|
| ZPM-INTAKE-FUT-01 | SEO (ZPM / bzpm.ru) | EV-ZPM-OP-FUT-01 — possibility only | **Future Candidate** — hold |
| ZPM-INTAKE-FUT-02 | Контекстная реклама | EV-ZPM-OP-FUT-01 | **Future Candidate** — hold |
| ZPM-INTAKE-FUT-03 | AI automation (ZPM account) | EV-ZPM-OP-FUT-01 | **Future Candidate** — hold |
| ZPM-INTAKE-FUT-04 | OpenCartPilot-assisted maintenance | EV-ZPM-OP-FUT-01 | **Future Candidate** — hold |

**Distinction from active catalog project:** Future SEO/advertising are **separate initiatives** if ever approved — not subtasks of ZPM-INTAKE-CAND-A01 unless steward attests combined scope (no such evidence now).

---

## 6. Classification — rejected candidates

| Candidate | Source | Rejection basis |
|-----------|--------|-----------------|
| BZPM / SITE-001 OpenCart dealership support | [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) §11 | **COR-W1B-03** — SIBCAR/SITE-001 ≠ ORG-0005 evidence; identity pollution |
| OCPilot read-only audit (Run 5+) | Same §11 | No approved ATLAS Project; MARS/OCPilot program context |
| `ocpilot`, `ear-runtime`, `wpilot`, `mig`, … | Wave 3 §5.1 | MARS program registry — **E-17 excluded** |
| **Single merged** «bzpm.ru website» Project (hist + current) | Inference | **EFV-03** — two distinct delivery phases; forbidden merge |
| `bzpm.ru` hostname **alone** | CC §17 / URL | Website class candidate — **not** auto-Project |
| ORG-0005 ЗПМ as Project | Class smell | Organization ≠ initiative ([ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3) |
| Wave 1 dataset draft rows | Dataset v0.4 | No ZPM Project rows — not evidence to mint |

---

## 7. Duplicate review

| review_id | Signal | Analysis | Verdict | Blocking |
|-----------|--------|----------|---------|----------|
| **ZPM-PRJ-D-01** | CAND-H01 vs CAND-A01 — same hostname `bzpm.ru` | Two **sequential client deliveries** on one property; Triumph analog PRJ-0004 (deprecated) + ongoing site | **Not duplicate** — **two Project candidates** | No |
| **ZPM-PRJ-D-02** | CAND-A01 vs FUT-01 SEO | SEO not started; no scope overlap attested | **Distinct class** — future vs active | No |
| **ZPM-PRJ-D-03** | CAND-H01 vs future WEB-* | Project vs Website class boundary | **Class boundary** — not duplicate org/project | No |
| **ZPM-PRJ-D-04** | ZPM candidates vs Triumph PRJ-0004..0008 | Different commissioning org ORG-0005 vs ORG-0004 | **Distinct org context** | No |
| **ZPM-PRJ-D-05** | W1B §11 SITE-001 project vs CAND-A01 | SIBCAR narrative revoked | **Reject SITE-001** — not duplicate of catalog project | No |
| **ZPM-PRJ-D-06** | Canonical name collision «Сайт bzpm.ru» ×2 | Steward must disambiguate names at population (version suffix) | **Open — low** — naming hygiene only | No |

**Duplicate review summary:** **Pass** — two attested-intake projects recommended; no merge required.

---

## 8. SAFE UNKNOWN review

| ID | Topic | Impact | Posture |
|----|-------|--------|---------|
| **SU-ZPM-PRJ-01** | Historical project **contract / act dates** | Lifecycle precision | **SAFE UNKNOWN** — use operator «~5 years» as narrative only |
| **SU-ZPM-PRJ-02** | Historical project **formal acceptance** document | E1 upgrade path | **SAFE UNKNOWN** — E0 sufficient for population **proposal** |
| **SU-ZPM-PRJ-03** | Whether historical and current deliveries share **one production deployment** vs replace-in-place | Wave 4 WEB-* modeling | **SAFE UNKNOWN** — Website intake decides; does not block Project intake |
| **SU-ZPM-PRJ-04** | Exact **canonical name** strings at attestation | Display only | Steward choice between proposed names |
| **SU-ZPM-PRJ-05** | OpenCartPilot maintenance — product scope if ever approved | FUT-04 | **SAFE UNKNOWN** — no OCPilot charter cited for ORG-0005 |
| **SU-ZPM-PRJ-06** | Related people on Project (PER-0014, PER-0015) | Informational only | Deferred — Person ↔ Project not Wave 3 scope |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Commercial edge | **Wave 6** — not prerequisite for Project intake |

---

## 9. Recommended Wave 3 roster (ZPM tranche)

**Verdict:** **READY FOR ZPM WAVE 3 PROJECT POPULATION PROPOSAL** — **2** Project records.

| Priority | Intake label | Proposed canonical name | Target lifecycle | Evidence | Population slice |
|----------|--------------|-------------------------|------------------|----------|------------------|
| **P0** | ZPM-INTAKE-CAND-A01 | Каталог-платформа bzpm.ru | **active** | E0 EV-ZPM-OP-ACT-01 | client_delivery |
| **P1** | ZPM-INTAKE-CAND-H01 | Сайт bzpm.ru (исходная версия) | **deprecated** | E0 EV-ZPM-OP-HIST-01 | client_delivery |

**Ordering note:** Active catalog project **P0** — current operational truth. Historical deprecated **P1** — structural backfill for graph completeness (Triumph PRJ-0004 pattern).

**Deferred to later waves (not in this roster):**

| Item | Wave |
|------|------|
| `WEB-*` for `bzpm.ru` | Wave 4 |
| `DOM-*` for `bzpm.ru` | Wave 5 |
| COMMISSIONED_BY / EXECUTES (ORG-0005, ORG-0001) | Wave 3B |
| WEB → Project BELONGS_TO | Wave 4B |
| Future candidates FUT-01..04 | Separate intake when approved |

---

## 10. Final recommendation

1. **Accept** two Project intake candidates for ORG-0005: one **deprecated** historical delivery, one **active** catalog-platform delivery.
2. **Reject** all SIBCAR/SITE-001-derived project proposals per **COR-W1B-03** and identity correction.
3. **Hold** SEO, advertising, AI automation, and OpenCartPilot maintenance as **Future Candidates** — no Project rows until operator supplies start evidence.
4. **Do not** merge historical and current work into a single Project.
5. **Proceed** to Wave 3 ZPM Project Population package (separate execution) — mint `PRJ-*` only in that pass with steward attestation; **not in this analysis**.

**Stop conditions (not triggered):**

| Stop | Condition | Status |
|------|-----------|--------|
| STOP-EFV-01 | Alias/project from hostname alone | **Clear** — operator delivery narrative cited |
| STOP-EFV-02 | Duplicate Pass without evidence | **Clear** — duplicate review completed |
| STOP-EFV-03 | CC contradicts proposal | **Clear** — CC supports org + domain; no project contradiction |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-ZPM-PROJECT-INTAKE-REGISTER-v1.md](ATLAS-ZPM-PROJECT-INTAKE-REGISTER-v1.md) | Tabular intake register |
| [ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md](ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md) | Executive summary |
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | SIBCAR rejection basis |
| [ATLAS-WAVE3-PROJECT-POPULATION-v1.md](ATLAS-WAVE3-PROJECT-POPULATION-v1.md) | Global Wave 3 methodology |

---

*ATLAS ZPM Project Intake Analysis v1 — analysis only; no canonical Project records created.*
