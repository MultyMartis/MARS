# ATLAS ZPM Website Model Correction Execution v1

**Status:** **executed** — population-layer correction applied 2026-06-07.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Execution authority:** Operator approval — PASS WITH CORRECTION  
**Source:** [ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md](ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md)  
**Is not:** attestation act, Foundation amendment, runtime registry write, database mutation.

---

# REPORT — ATLAS ZPM Website Model Correction Execution

**Execution date:** 2026-06-07  
**Scope:** WEB-ZPM-01 · WEB-ZPM-02 · PRJ-0009 · PRJ-0010 · ORG-0005 · hostname `bzpm.ru`  
**Layer:** Population documentation only — no Foundation modification.

---

## 1. Approved canonical model (binding)

```text
One hostname (bzpm.ru)
    → One Domain (Wave 5 ZPM — DOM-*)
    → One Website (WEB-ZPM-01 — active)

Multiple redesigns / rebuilds / delivery generations
    → Multiple Projects (PRJ-0009 active + PRJ-0010 deprecated)
    → NOT multiple Website entities
```

**Operator verdict:** PASS WITH CORRECTION

---

## 2. Corrections executed

| ID | Correction | Action taken | Result |
|----|------------|--------------|--------|
| **COR-ZPM-WEB-01** | Retire WEB-ZPM-02 | Removed from population roster; marked **rejected / not minted** | **Done** |
| **COR-ZPM-WEB-02** | Revoke ZPM-WEB-POL-01 | Superseded in Population §6; dual-generation policy removed | **Done** |
| **COR-ZPM-WEB-03** | Adopt Triumph single-property model | WEB-ZPM-01 sole `bzpm.ru` Website | **Done** |
| **COR-ZPM-WEB-04** | Re-route EV-ZPM-OP-HIST-01 | Evidence → PRJ-0010 only; not Website mint | **Done** |
| **COR-ZPM-WEB-05** | Cancel AT-W4-ZPM-02 | Attestation plan blocked for WEB-ZPM-02 | **Done** |
| **COR-ZPM-WEB-06** | Cancel REL-ZPM-WB-02 | Removed from Wave 4B queue | **Done** |
| **COR-ZPM-WEB-07** | Add REL-ZPM-WB-03 | WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** queued | **Done** |
| **COR-ZPM-WEB-08** | Retain REL-ZPM-WB-01 | WEB-ZPM-01 → PRJ-0009 **BELONGS_TO** retained | **Done** |
| **COR-ZPM-WEB-09** | Simplify OWNS | ORG-0005 → WEB-ZPM-01 only; WEB-ZPM-02 OWNS removed | **Done** |
| **COR-ZPM-WEB-10** | Resolve SU-W4-ZPM-03 | DOM-* `bzpm.ru` → WEB-ZPM-01 **PRIMARY_DOMAIN** singleton | **Done** |
| **COR-ZPM-WEB-11** | Reopen ZPM-WEB-D-01 | Verdict **Fail** — WEB-ZPM-02 retired | **Done** |
| **COR-ZPM-WEB-12** | Clarify EFV-03 scope | Valid at Project layer only; not Website cardinality | **Done** |

---

## 3. Documents updated (execution pass)

| # | Document | Change summary |
|---|----------|----------------|
| 1 | [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) | Single Website roster; §6 policy replaced; §10 relationships corrected |
| 2 | [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | WEB-ZPM-02 removed; counts updated; evidence re-indexed |
| 3 | [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) | AT-W4-ZPM-02 blocked; single-Website verdict; 4B queue updated |
| 4 | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-REGISTER-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-REGISTER-v1.md) | Correction action register *(this pass)* |
| 5 | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-SUMMARY-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-SUMMARY-v1.md) | Executive summary *(this pass)* |

**Documents unchanged (validated — no entity-level change required):**

- [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md)
- [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md)
- [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md)
- Wave 1B / 2 / 2B ZPM packages

---

## 4. Entities affected

| Entity | Prior state | Post-correction state | Action |
|--------|-------------|----------------------|--------|
| **WEB-ZPM-01** | **proposed** → **active** *(target)* | **Unchanged** — keep; attest via AT-W4-ZPM-01 | **Keep** |
| **WEB-ZPM-02** | **proposed** → **deprecated** *(target)* | **Retired** — not minted; id unused (IDP-03) | **Retire** |
| **PRJ-0009** | **active** *(attested)* | **Unchanged** | **Keep** |
| **PRJ-0010** | **deprecated** *(attested)* | **Unchanged** | **Keep** |
| **ORG-0005** | **active** *(attested)* | **Unchanged** | **Keep** |

---

## 5. Relationships affected

| rel_id | Prior queue status | Post-correction status | Action |
|--------|-------------------|------------------------|--------|
| **REL-ZPM-WB-01** | WEB-ZPM-01 → PRJ-0009 **BELONGS_TO** | **Retained** — ready after AT-W4-ZPM-01 | **Keep** |
| **REL-ZPM-WB-02** | WEB-ZPM-02 → PRJ-0010 **BELONGS_TO** | **Cancelled** — source Website retired | **Remove** |
| **REL-ZPM-WB-03** | *(not present)* | WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** | **Create** *(draft queue)* |
| ORG-0005 → WEB-ZPM-01 **OWNS** | Queued | **Retained** — single target | **Keep** |
| ORG-0005 → WEB-ZPM-02 **OWNS** | Queued | **Cancelled** | **Remove** |
| DOM-* → WEB-ZPM-01 **PRIMARY_DOMAIN** | Ambiguous (SU-W4-ZPM-03) | **Resolved** — singleton | **Clarify** |

**Unchanged:** REL-ZPM-PJ-01..04 (Wave 3B); REL-ZPM-01..02 (Wave 2B).

---

## 6. Relationship graph — before correction

```text
ORG-0005 ЗПМ
    ├── OWNS ──► WEB-ZPM-01 bzpm.ru (proposed → active)
    └── OWNS ──► WEB-ZPM-02 bzpm.ru исходная версия (proposed → deprecated)

WEB-ZPM-01 ──BELONGS_TO──► PRJ-0009 Каталог-платформа (active)
WEB-ZPM-02 ──BELONGS_TO──► PRJ-0010 Сайт исходная версия (deprecated)

WEB-ZPM-01 ──X──► PRJ-0010  (explicitly rejected — generation mismatch)

Wave 5B (ambiguous):
    DOM-* bzpm.ru ──?──► WEB-ZPM-01 or WEB-ZPM-02
```

---

## 7. Relationship graph — after correction

```text
ORG-0005 ЗПМ
    └── OWNS ──► WEB-ZPM-01 bzpm.ru (proposed → active)

WEB-ZPM-01 ──BELONGS_TO──► PRJ-0009 Каталог-платформа bzpm.ru (active)     [REL-ZPM-WB-01]
WEB-ZPM-01 ──BELONGS_TO──► PRJ-0010 Сайт bzpm.ru исходная версия (deprecated) [REL-ZPM-WB-03]

WEB-ZPM-02 — RETIRED (not in graph)

Wave 3B (unchanged):
    PRJ-0009/0010 ──COMMISSIONED_BY──► ORG-0005
    ORG-0001 ──EXECUTES──► PRJ-0009/0010

Wave 5B ZPM (resolved):
    DOM-* bzpm.ru ──PRIMARY_DOMAIN──► WEB-ZPM-01
```

**Triumph analog (attested reference):**

```text
WEB-0006 gktriumph.ru ──BELONGS_TO──► PRJ-0004 (deprecated)
WEB-0006 gktriumph.ru ──BELONGS_TO──► PRJ-0006 (active)
```

---

## 8. Cross-wave validation

| Wave / artifact | Validation | Result |
|-----------------|------------|--------|
| **Wave 3 ZPM** | PRJ-0009 **active** · PRJ-0010 **deprecated** | **Pass** — no change required |
| **Wave 3B ZPM** | REL-ZPM-PJ-01..04 **active** | **Pass** — no change required |
| **Wave 4 ZPM** | Single Website WEB-ZPM-01; AT-W4-ZPM-02 blocked | **Pass** — docs synced |
| **Wave 4B ZPM** | REL-ZPM-WB-01 + REL-ZPM-WB-03; REL-ZPM-WB-02 cancelled | **Pass** — queue corrected |
| **Wave 5 ZPM** | DOM-* `bzpm.ru` planned; SU-W4-ZPM-03 resolved | **Pass** — unambiguous target |
| **Wave 5B ZPM** | PRIMARY_DOMAIN → WEB-ZPM-01 singleton | **Pass** — cardinality resolved |
| **Backup Snapshot** | WEB-ZPM-* not yet counted in baseline | **Pass** — note for next refresh (1 Website) |
| **Integrity Snapshot** | Pre–Wave 4 ZPM baseline; no WEB-ZPM rows | **Pass** — consistent; correction documented |
| **Relationship graph** | No attested ZPM Website edges yet | **Pass** — proposed queue only |

---

## 9. Impact assessment

| Area | Impact | Severity |
|------|--------|----------|
| Website entity count | 2 → 1 | **Structural** — resolved |
| Attestation path | 2 tranches → 1 tranche | **Process** — simplified |
| Wave 4B BELONGS_TO | 2 edges same Website (multi-Project) | **Aligned** — Triumph precedent |
| Wave 5/5B Domain | Singleton PRIMARY_DOMAIN | **Resolved** — SU-W4-ZPM-03 closed |
| Project layer | None | **No impact** |
| Organization layer | None | **No impact** |
| Evidence routing | EV-ZPM-OP-HIST-01 re-indexed | **Documentation** — low |
| Foundation | None | **No amendment** |

**Timing advantage:** WEB-ZPM-01/02 were **proposed** only — correction applied **before** Website attestation act; no attested entity deprecation required.

---

## 10. Foundation consistency

| Foundation rule | Post-correction alignment |
|-----------------|---------------------------|
| EIR-W01 — one website per business web property identity | **Aligned** |
| ATLAS-ENTITY-TAXONOMY §3 Project / §4 Website class separation | **Aligned** |
| ATLAS-RELATIONSHIP-MODEL — multi-Project BELONGS_TO | **Aligned** — REL-0027/0028 precedent |
| EIR-D01 + Wave 5B PRIMARY_DOMAIN singleton | **Aligned** |
| EFV-03 — Organization equivalence (not Website cardinality) | **Aligned** — COR-ZPM-WEB-12 |
| IDP-03 — retired id not reused | **Aligned** — WEB-ZPM-02 unused |

**Foundation amendment:** **Not required.**

---

## 11. SAFE UNKNOWN disposition (post-correction)

| ID | Prior status | Post-correction |
|----|--------------|-----------------|
| SU-ZPM-PRJ-03 | SAFE UNKNOWN | **Resolved structurally** |
| SU-W3B-ZPM-01 | SAFE UNKNOWN | **Resolved** — multi-BELONGS_TO on WEB-ZPM-01 |
| SU-W4-ZPM-03 | SAFE UNKNOWN | **Resolved** — single DOM → WEB-ZPM-01 |
| SU-W4-ZPM-02 | SAFE UNKNOWN | **Obviated** — no deprecated Website |
| SU-ZPM-PRJ-01/02 | SAFE UNKNOWN | **Unchanged** |

---

## 12. Final verdict

```text
ZPM WEBSITE MODEL CORRECTION COMPLETE

READY FOR WAVE 4B ZPM WEBSITE RELATIONSHIPS
```

| Criterion | Result |
|-----------|--------|
| Operator decision executed | **Yes** |
| WEB-ZPM-02 retired | **Yes** |
| WEB-ZPM-01 retained | **Yes** |
| Wave 4 ZPM docs synced | **Yes** |
| Wave 4B queue corrected | **Yes** |
| Cross-wave validation | **Pass** |
| Foundation consistency | **Pass** — no amendment |
| Attestation authorization | AT-W4-ZPM-01 **authorized**; AT-W4-ZPM-02 **blocked** |

**Next authorized step:** Steward executes **AT-W4-ZPM-01** (WEB-ZPM-01 → **active**), then Wave 4B-ZPM population with REL-ZPM-WB-01 + REL-ZPM-WB-03.

---

## 13. Execution lineage

```text
Operator decision (2026-06-07) — PASS WITH CORRECTION
    │
    ├── ATLAS-ZPM-WEBSITE-MODEL-AUDIT-v1 (findings)
    ├── ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1 (COR-ZPM-WEB-01..12)
    ├── ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1 (binding record)
    │
    └── THIS DOCUMENT (execution — population docs synced)
              │
              ├── ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-REGISTER-v1
              ├── ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-SUMMARY-v1
              │
              └──► AT-W4-ZPM-01 → Wave 4B-ZPM (REL-ZPM-WB-01, REL-ZPM-WB-03)
```

---

*ATLAS ZPM Website Model Correction Execution v1 — population layer; executed 2026-06-07; no commit.*
