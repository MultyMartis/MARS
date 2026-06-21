# ATLAS Wave 1B BZPM Identity Correction v1

**Status:** **documented** — binding operator correction (population layer).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Trigger:** Counterparty Card discovered at `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\` after Wave 1B population assumed alias equivalence without CC review.  
**Parent:** [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Supersedes (partial):** alias and duplicate-review conclusions in [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) §7–§8, [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) alias rows.

**Is not:** attestation execution, registry write, Foundation amendment.

---

## 1. Prior incorrect conclusion

| Source | Claim | Verdict recorded |
|--------|-------|------------------|
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-POPULATION-v1.md) §3.1, §7 | BZPM / SIBCAR / Автосалон СИБКАР / СИБКАР → **one Organization** (alias cluster on ORG-0005) | **W1B-D-01 Pass** |
| Same package §3.1 | BZPM = operator codename; SIBCAR = client trade / site brand → **aliases** | Narrative inference from OCPilot SITE-001 + EAR docs |
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) | Proposed aliases: Автосалон СИБКАР, SIBCAR, СИБКАР on ORG-0005 | **proposed** |

**Error class:** Identity pollution — **U-merge-by-context** (project/site naming treated as org equivalence without CC).

---

## 2. Evidence that contradicts prior conclusion

**Evidence ref:** `EV-W1B-CC-01`  
**Path:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx`  
**Format:** DOCX — «Анкета Участника аукциона / Сведения об Участнике»  
**Tier at review:** **E1** (structured requisites with INN/OGRN/legal name)

| CC field | Value | Cited in CC |
|----------|-------|-------------|
| Legal name | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | §1–§2 |
| INN | 2221237587 | §3, §23 |
| KPP | 222101001 | §3, §23 |
| OGRN | 1172225049787 | §3, §23 |
| Website | **Bzpm.ru** | §17 |
| Trade / site strings | **No** «SIBCAR», «СИБКАР», «Автосалон» | Absent in CC |

**Contradiction:** CC describes a **food machinery plant** (Barnaul, Altai) with domain **bzpm.ru**. It contains **zero** mention of SIBCAR, automotive dealership, or SITE-001 test hostname. Prior alias cluster **cannot** stand on CC evidence.

---

## 3. Binding corrections (enforced)

| ID | Correction | Applies to |
|----|------------|------------|
| **COR-W1B-01** | **Revoke** proposed aliases **Автосалон СИБКАР**, **SIBCAR**, **СИБКАР** from ORG-0005 until separate E1+ evidence cites them for the **same** INN/OGRN subject | ORG-0005 alias register |
| **COR-W1B-02** | **Downgrade** duplicate review **W1B-D-01** from **Pass** → **Fail** (reopened) | Population + register packages |
| **COR-W1B-03** | **Do not** treat OCPilot SITE-001 site title or `sibcar.new-site.space` as proof of alias equivalence with ORG-0005 | All Wave 1B+ BZPM tranches |
| **COR-W1B-04** | **Bind** LE-0004 to CC legal subject: ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ», INN 2221237587, OGRN 1172225049787 — fields **proposed from CC**, not **active** until attestation | LE-0004 |
| **COR-W1B-05** | **SIBCAR / Автосалон СИБКАР** identity → **SAFE UNKNOWN** Organization (no id assigned in this correction); requires **own** CC or E2 path | Future intake |
| **COR-W1B-06** | Relationship between ORG-0005 (BZPM / OOO ЗПМ per CC) and any future SIBCAR Organization → **SAFE UNKNOWN**; no CLIENT_OF / alias bridge without evidence | Wave 6+ |

---

## 4. What remains valid from Wave 1B package

| Item | Status |
|------|--------|
| ORG-0005 slot as **proposed** W1-B CLIENT | **Valid** — identifier reservation |
| ORG-0005 canonical_name **BZPM** as operator label pending steward rename review | **Valid but review required** — CC supports **Bzpm.ru** stem, not «автосалон» narrative |
| ORG-0005 vs ORG-0004 distinct | **Valid** — unchanged |
| ORG-0005 vs SITE-001 class boundary | **Valid** — Website ≠ Organization |
| ME-W1B-01 (CC missing) | **Resolved** — CC present; replaced by identity correction gate |

---

## 5. Steward actions (documentation queue)

| Step | Action | Blocker cleared |
|------|--------|-----------------|
| 1 | Update register alias table per COR-W1B-01 | Partial |
| 2 | Repopulate LE-0004 row from EV-W1B-CC-01 | Partial |
| 3 | Re-run duplicate review with INN/OGRN | Required before **active** |
| 4 | Obtain CC or E2 for SIBCAR subject if SITE-001 org binding needed | Separate tranche |
| 5 | Apply [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) on future intakes | Ongoing |

---

## 6. Attestation impact

| Gate | Before correction | After correction |
|------|-------------------|------------------|
| ORG-0005 **active** | Blocked (ME-W1B-01) | Still **blocked** — identity correction + steward attestation sequence required |
| Alias attest | Would have included SIBCAR cluster | **Forbidden** until COR-W1B-01 satisfied |
| Wave 2B-BZPM Person queue | Not authorized | Not authorized |

---

*ATLAS Wave 1B BZPM Identity Correction v1 — documentation only.*
