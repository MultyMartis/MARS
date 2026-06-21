# ATLAS ZPM Website Model Decision v1

**Status:** **documented** — binding operator decision record (population governance).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Decision authority:** Operator  
**Audit basis:** [ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md](ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md)  
**Correction package:** [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md)  
**Is not:** attestation act, register write, Foundation amendment.

---

# REPORT — ATLAS ZPM Website Model Operator Decision

**Decision date:** 2026-06-07  
**Scope:** WEB-ZPM-01 · WEB-ZPM-02 · PRJ-0009 · PRJ-0010 · ORG-0005 · hostname `bzpm.ru`

---

## 1. Decision statement

**Canonical ATLAS interpretation (operator-approved):**

> **Website** = real web property identity.  
> **Not** Website = delivery generation / rebuild lineage.

**Approved structural model:**

```text
Domain (bzpm.ru)
    ↓
Website (WEB-ZPM-01 — single active property)
    ↓
Projects
    ├── PRJ-0009 Каталог-платформа bzpm.ru (active)
    └── PRJ-0010 Сайт bzpm.ru исходная версия (deprecated)
```

**Binding rule:** Historical redesigns, rebuilds, and platform migrations **must** be represented by **Projects**. They **must not** automatically create new **Website** entities.

---

## 2. Question and answer

| Question | Operator answer |
|----------|-----------------|
| Can one hostname have **1 Website entity** and **multiple historical Projects**? | **YES** — this is the **preferred model**. |
| Should `bzpm.ru` historical original site be a separate Website (WEB-ZPM-02)? | **NO** — PRJ-0010 is sufficient. |
| Should current catalog platform be the sole Website for `bzpm.ru`? | **YES** — WEB-ZPM-01. |

---

## 3. Decision on audit objects

| Object | Decision | Lifecycle target | Rationale |
|--------|----------|------------------|-----------|
| **WEB-ZPM-01** | **Keep** | **active** | Sole real web property for `bzpm.ru` |
| **WEB-ZPM-02** | **Retire** | *(not attested)* | Duplicates PRJ-0010 at wrong entity class |
| **PRJ-0009** | **Keep** | **active** | Current catalog-platform delivery |
| **PRJ-0010** | **Keep** | **deprecated** | Historical delivery — correct layer |
| **ORG-0005** | **Keep** | **active** | Unchanged client anchor |

---

## 4. Precedent alignment

This decision **aligns** ZPM with the attested Triumph registry pattern:

| Client | Hostname | Websites | Projects on same property |
|--------|----------|----------|---------------------------|
| Триумф ORG-0004 | `gktriumph.ru` | **1** — WEB-0006 **active** | PRJ-0004 **deprecated** + PRJ-0006 **active** |
| ЗПМ ORG-0005 | `bzpm.ru` | **1** — WEB-ZPM-01 **active** | PRJ-0010 **deprecated** + PRJ-0009 **active** |

**Source:** [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) — REL-0027, REL-0028.

The prior ZPM «dual-generation Website» policy ([ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) §6) is **superseded** by this decision.

---

## 5. Foundation alignment (no amendment required)

| Foundation rule | Decision alignment |
|-----------------|-------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4 Website — registered web property | **Aligned** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-W01 — one website per business web property identity | **Aligned** |
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §3 Project — initiative container | **Aligned** — generations in Project layer |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) — BELONGS_TO multi-project allowed | **Aligned** — Triumph precedent |
| EIR-D01 + Wave 5B PRIMARY_DOMAIN singleton | **Aligned** — one DOM → one WEB |

**Foundation amendment:** **Not required.** Prior ZPM Wave 4 documentation was **non-conformant** with existing Foundation — correction is at population layer only.

---

## 6. Relationship decisions (Wave 4B-ZPM target)

| Draft rel_id | Decision | Status |
|--------------|----------|--------|
| **REL-ZPM-WB-01** WEB-ZPM-01 → PRJ-0009 **BELONGS_TO** | **Approve** | Queue after WEB-ZPM-01 attestation |
| **REL-ZPM-WB-02** WEB-ZPM-02 → PRJ-0010 **BELONGS_TO** | **Cancel** | COR-ZPM-WEB-06 |
| **REL-ZPM-WB-03** WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** | **Approve** *(new)* | Historical grouping — analog REL-0027 |
| ORG-0005 → WEB-ZPM-01 **OWNS** | **Approve** | Single property ownership |
| ORG-0005 → WEB-ZPM-02 **OWNS** | **Cancel** | Target retired |
| DOM-* → WEB-ZPM-01 **PRIMARY_DOMAIN** | **Approve** | Wave 5B — singleton |

**Explicit rejection retained:** Cross-property edges that treat delivery generation as Website identity (WEB-ZPM-02 mint, generation-paired 1:1 Website↔Project) — **rejected**.

---

## 7. Attestation authorization

| Tranche | Authorization |
|---------|---------------|
| **AT-W4-ZPM-01** — WEB-ZPM-01 → **active** | **Authorized** after population docs reflect this decision |
| **AT-W4-ZPM-02** — WEB-ZPM-02 → **deprecated** | **Not authorized** — COR-ZPM-WEB-05 |

**Gate:** Do **not** execute Wave 4 ZPM Website attestation for WEB-ZPM-02. Single-Website attestation path only.

---

## 8. Downstream authorization summary

| Wave | Authorization |
|------|---------------|
| **Wave 4 ZPM** | Single Website (WEB-ZPM-01) |
| **Wave 4B ZPM** | Multi-Project BELONGS_TO on WEB-ZPM-01; no WEB-ZPM-02 edges |
| **Wave 5 ZPM** | Single DOM-* for `bzpm.ru` |
| **Wave 5B ZPM** | PRIMARY_DOMAIN → WEB-ZPM-01 only |
| **Wave 3 / 3B ZPM** | **No change** — PRJ-0009/0010 remain canonical |
| **Backup / Integrity** | Refresh on next sync pass — document COR-ZPM-WEB-* |

---

## 9. Final verdict

```text
PASS WITH CORRECTION
```

| Component | Verdict |
|-----------|---------|
| Operator model | **Approved** |
| Audit findings | **Confirmed** — WEB-ZPM-02 is non-conformant |
| PRJ-0009 · PRJ-0010 · ORG-0005 | **Pass without correction** |
| WEB-ZPM-01 | **Pass without correction** |
| WEB-ZPM-02 | **Fail** — retire per correction package |
| Corrections executed | **No** — decision and package only |
| Foundation change | **Not required** |

---

## 10. Decision lineage

```text
Operator decision (2026-06-07)
    │
    ├──► ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1 (findings)
    │
    ├──► ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1 (COR-ZPM-WEB-01..12)
    │
    └──► THIS DOCUMENT (binding decision record)
              │
              └──► Future: Wave 4 ZPM doc sync + AT-W4-ZPM-01 execution
```

**Supersedes:**

| Prior policy | Source | Disposition |
|--------------|--------|-------------|
| ZPM-WEB-POL-01 dual-generation Website | Wave 4 ZPM population §6 | **Superseded** |
| «Do not merge WEB-ZPM-01 + WEB-ZPM-02» | Wave 4 ZPM attestation | **Superseded** — WEB-ZPM-02 not minted |
| READY FOR WAVE 4 ZPM WEBSITE ATTESTATION (2 websites) | Wave 4 ZPM attestation §15 | **Superseded** — single Website path |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md](ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md) | Full audit findings |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md) | Executable correction spec |
| [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) | Prior policy — pending sync |
| [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) | Triumph reference §3.1, §6.3 |

---

*ATLAS ZPM Website Model Decision v1 — operator decision record; no entities or registers modified.*
