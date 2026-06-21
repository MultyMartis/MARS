# ATLAS Dyakonov Contractor Intake Summary v1

**Status:** **documented** — executive summary (contractor intake analysis only).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Intake slug:** `dyakonov`  
**Parent:** [ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md](ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md) · [ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md](ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md)

---

## Verdict

**READY FOR EVIDENCE COLLECTION**

Contractor intake candidates documented at **E0** operator-direct evidence. **Population deferred.** No `ORG-*`, `LE-*`, `PER-*`, `PRJ-*`, `WEB-*`, `DOM-*`, or `REL-*` minting in this pass.

---

## 1. Contractor candidate

| Label | Display name | org_id | Evidence | Status |
|-------|--------------|--------|----------|--------|
| **DYAKONOV-INTAKE-CAND-O01** | **ИП Дьяконов** | **none** | **E0** | **INTAKE ONLY** |

| Label | Legal form | le_id | Status |
|-------|------------|-------|--------|
| **DYAKONOV-INTAKE-CAND-LE01** | **ИП** *(unverified)* | **none** | **INTAKE ONLY** |

| Label | Name signal | person_id | Status |
|-------|-------------|-----------|--------|
| **DYAKONOV-INTAKE-CAND-P01** | **Дьяконов** *(surname only)* | **none** | **INTAKE ONLY** |

**Organization anchor:** ORG-0001 Веб-студия «Полигон» *(unchanged — reference only)*

**Required CC path:**

```text
C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\dyakonov\
```

**Filesystem (2026-06-07):** folder **absent**.

---

## 2. Population path

| Path | Verdict |
|------|---------|
| Organization + Legal Entity | **Primary** — ИП precedent (LE-0001, LE-0002) |
| Person | **Secondary** — after CC; CONTRACTOR → ORG-0001 |
| Organization only | **Rejected** — ИП requires LE |
| Person only | **Rejected** — operator label is ИП business subject |

---

## 3. Classification

| Classification | Verdict |
|----------------|---------|
| **Contractor** | **Primary** — operator states «Polygon contractor»; developer role |
| Vendor (VENDOR_OF) | **Secondary / deferred** — Wave 6+ org-level commercial edge |
| Subcontractor | **Rejected** — no intermediary chain evidence |
| Representative | **Rejected** — no representation authority evidence |
| EMPLOYEE vs CONTRACTOR | **Open** — E0 favours CONTRACTOR; CC may refine |

**Target relationship:** `CONTRACTOR` (Person → ORG-0001)

---

## 4. Duplicate review

**No existing entity** found in Atlas population for Dyakonov / Дьяконов / ИП Дьяконов.

| Check | Result |
|-------|--------|
| vs ORG-0001..0006 | **Distinct** — no merge |
| vs LE-0001..0002 | **Distinct** — no merge |
| vs PER-0001..0013 | **Distinct** *(preliminary)* |
| ZPM (ORG-0005) intact | **Pass** |
| SIBCAR (ORG-0006) intact | **Pass** |
| INN/ОГРНИП identity close | **Open** — CC required |

---

## 5. Evidence inventory

| Tier | Sources |
|------|---------|
| **E0** | EV-DYAK-OP-01 (steward inputs); EV-DYAK-OP-02 (operator-direct contractor statement) |
| **E1+** | **None** — CC absent |

**Minimum evidence gate (blocks population):**

1. Counterparty Card (INN, ОГРНИП, legal name)
2. Legal form verification
3. Natural person full name
4. Duplicate review on CC-backed identifiers

---

## 6. SAFE UNKNOWN review

| Topic | Posture |
|-------|---------|
| Legal form / INN / ОГРНИП | **SAFE UNKNOWN** — **blocks** population |
| Natural person full name | **SAFE UNKNOWN** — Person not minted |
| Contacts | **SAFE UNKNOWN** |
| Websites / domains | **SAFE UNKNOWN** — none supplied |
| Project participation | **SAFE UNKNOWN** — deferred |
| Contractual scope | **SAFE UNKNOWN** — recommended for classification lock |

---

## 7. Explicit exclusions confirmed

- No `ORG-*` creation
- No `LE-*` creation
- No `PER-*` creation
- No `WEB-*` / `DOM-*` creation
- No Relationship creation
- No Project creation
- No graph changes
- No lifecycle changes
- No attestation
- No population

---

## 8. Final recommendation

1. **Accept** contractor intake candidates at **E0** — analysis complete.
2. **Collect** Counterparty Card in `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\dyakonov\`.
3. **Re-run** CPV inventory + EFV extraction before population proposal.
4. **Populate** via Organization + Legal Entity path, then Person + CONTRACTOR edge to ORG-0001.
5. **Do not** merge with any attested Organization, Legal Entity, or Person without CC-backed identifiers.

---

## Package index

| Document | Role |
|----------|------|
| [ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md](ATLAS-DYAKONOV-INTAKE-ANALYSIS-v1.md) | Full evidence analysis |
| [ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md](ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md) | Tabular register |

---

*ATLAS Dyakonov Contractor Intake Summary v1 — intake only.*
