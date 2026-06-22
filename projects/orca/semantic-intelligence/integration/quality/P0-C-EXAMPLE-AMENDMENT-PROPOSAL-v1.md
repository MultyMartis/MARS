# P0-C Example Library Amendment Proposal v1

**Proposal ID:** `p0-c-example-amendment-proposal-v1`  
**Status:** `PROPOSED — CONTROLLED AMENDMENT ONLY`  
**Target:** `semantic-intelligence/annotation/examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md`

---

## Amendment policy

- **Add only** freshly reviewed examples — no uncontrolled rewrite of existing ACC/REJ/ABS entries
- Each new example tagged — never promoted to gold
- Operator approval required before merge to checkpointed P0-C

---

## Proposed additions

### Triumph scenario-first commercial (DIAGNOSTIC EXAMPLE × 3)

| ID | Phrase (illustrative) | Tag | Notes |
|----|----------------------|-----|-------|
| `TRI-SF-01` | «настройка 1с под нашу торговлю» | DIAGNOSTIC EXAMPLE | Scenario-first — requires commercial evidence check |
| `TRI-SF-02` | «внедрение учёта для производства» | TRAINING ILLUSTRATION | Scoped implementation without explicit hire verb |
| `TRI-SF-03` | «сопровождение 1с ежемесячно» | REGRESSION CANDIDATE | Recurring service pattern |

### Corvonero career leakage (REGRESSION CANDIDATE × 2)

| ID | Phrase | Tag | Failure mode |
|----|--------|-----|--------------|
| `COR-CAR-01` | «работа программист 1с удалённо» | REGRESSION CANDIDATE | Legacy COMMERCIAL SERVICE false positive |
| `COR-CAR-02` | «вакансия 1с программист москва» | NOT GOLD LABEL | Must REJECT — career |

### Educational leakage (REGRESSION CANDIDATE × 2)

| ID | Phrase | Tag |
|----|--------|-----|
| `COR-EDU-01` | «курсы 1с с нуля» | REGRESSION CANDIDATE |
| `COR-EDU-02` | «обучение 1с бухгалтерия онлайн» | DIAGNOSTIC EXAMPLE |

### DIY leakage (REGRESSION CANDIDATE × 2)

| ID | Phrase | Tag |
|----|--------|-----|
| `COR-DIY-01` | «как настроить 1с самостоятельно» | REGRESSION CANDIDATE |
| `COR-DIY-02` | «инструкция установки 1с своими руками» | NOT GOLD LABEL |

### Short-head ambiguity (TRAINING ILLUSTRATION × 2)

| ID | Phrase | Tag |
|----|--------|-----|
| `AMB-SH-01` | «1с» | TRAINING ILLUSTRATION — ABSTAIN |
| `AMB-SH-02` | «crm» | DIAGNOSTIC EXAMPLE — ABSTAIN |

### Problem-query ambiguity (TRAINING ILLUSTRATION × 2)

| ID | Phrase | Tag |
|----|--------|-----|
| `AMB-PQ-01` | «1с не работает» | TRAINING ILLUSTRATION — ABSTAIN |
| `AMB-PQ-02` | «ошибка при проведении документа 1с» | REGRESSION CANDIDATE — ABSTAIN |

---

## Tag legend

| Tag | Meaning |
|-----|---------|
| `DIAGNOSTIC EXAMPLE` | Explains failure mode — not benchmark truth |
| `TRAINING ILLUSTRATION` | Annotator training only |
| `REGRESSION CANDIDATE` | Pilot / future regression — not gold until adjudicated |
| `NOT GOLD LABEL` | Explicit anti-authority marker |

---

## Not in this task

- Editing `orca-annotation-example-library-v1.json` counts
- Committing amended P0-C library
