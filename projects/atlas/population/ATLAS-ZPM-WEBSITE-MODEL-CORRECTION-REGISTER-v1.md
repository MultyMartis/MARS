# ATLAS ZPM Website Model Correction Register v1

**Status:** **executed** — correction action register after population-layer sync 2026-06-07.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Parent:** [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-v1.md)  
**Is not:** entity registry, relationship registry, attestation act, runtime export.

---

## 1. Purpose

Канонический **реестр действий коррекции** ZPM Website Model. Одна строка — одно исполненное или отменённое correction action (COR-ZPM-WEB-*).

**Register summary:**

| Metric | Count |
|--------|-------|
| Total correction actions | **12** |
| Executed | **12** |
| Entity retirements | **1** (WEB-ZPM-02) |
| Relationship cancellations | **1** (REL-ZPM-WB-02) |
| Relationship additions *(queue)* | **1** (REL-ZPM-WB-03) |
| Documents synced | **3** (Wave 4 ZPM packages) |
| Foundation amendments | **0** |

---

## 2. Correction action roster — full table

| correction_id | target | action | prior state | post state | execution_status | blocking_cleared |
|---------------|--------|--------|-------------|------------|------------------|------------------|
| COR-ZPM-WEB-01 | WEB-ZPM-02 | **Retire** — do not mint/attest | proposed → deprecated *(planned)* | **rejected / not minted** | **executed** | AT-W4-ZPM-02 |
| COR-ZPM-WEB-02 | ZPM-WEB-POL-01 | **Revoke** dual-generation Website policy | active policy in Population §6 | **superseded** | **executed** | AUD-ZPM-WEB-03 |
| COR-ZPM-WEB-03 | WEB-ZPM-01 | **Adopt** Triumph single-property model | one of two Websites | **sole** `bzpm.ru` Website | **executed** | AUD-ZPM-WEB-01 |
| COR-ZPM-WEB-04 | EV-ZPM-OP-HIST-01 | **Re-route** evidence | WEB-ZPM-02 + PRJ-0010 | **PRJ-0010 only** | **executed** | — |
| COR-ZPM-WEB-05 | AT-W4-ZPM-02 | **Cancel** attestation tranche | planned P1 deprecated attest | **blocked** | **executed** | — |
| COR-ZPM-WEB-06 | REL-ZPM-WB-02 | **Cancel** relationship | queued WEB-ZPM-02 → PRJ-0010 | **removed from queue** | **executed** | — |
| COR-ZPM-WEB-07 | REL-ZPM-WB-03 | **Add** relationship draft | not present | WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** | **executed** | SU-W3B-ZPM-01 |
| COR-ZPM-WEB-08 | REL-ZPM-WB-01 | **Retain** relationship | queued | unchanged — ready | **executed** | — |
| COR-ZPM-WEB-09 | OWNS edges | **Simplify** org ownership | ORG-0005 → WEB-ZPM-01..02 | ORG-0005 → WEB-ZPM-01 only | **executed** | SU-W4-ZPM-02 |
| COR-ZPM-WEB-10 | DOM-* / PRIMARY_DOMAIN | **Resolve** SU-W4-ZPM-03 | ambiguous dual target | DOM-* → WEB-ZPM-01 singleton | **executed** | SU-W4-ZPM-03 |
| COR-ZPM-WEB-11 | ZPM-WEB-D-01 | **Reopen** duplicate review | Not duplicate — two records | **Fail** — WEB-ZPM-02 retired | **executed** | — |
| COR-ZPM-WEB-12 | EFV-03 label | **Clarify** scope | extended to Website cardinality | **Project layer only** | **executed** | AUD-ZPM-WEB-04 |

---

## 3. Entity disposition register

| entity_id | entity_class | canonical_name | lifecycle *(pre)* | lifecycle *(post)* | disposition | correction_ref |
|-----------|--------------|----------------|-------------------|-------------------|-------------|----------------|
| WEB-ZPM-01 | Website | bzpm.ru | **proposed** | **proposed** → **active** *(on AT-W4-ZPM-01)* | **Keep** | COR-ZPM-WEB-03 |
| WEB-ZPM-02 | Website | bzpm.ru (исходная версия) | **proposed** | *(not minted)* | **Retire** | COR-ZPM-WEB-01 |
| PRJ-0009 | Project | Каталог-платформа bzpm.ru | **active** | **active** | **Unchanged** | — |
| PRJ-0010 | Project | Сайт bzpm.ru (исходная версия) | **deprecated** | **deprecated** | **Unchanged** | — |
| ORG-0005 | Organization | ЗПМ | **active** | **active** | **Unchanged** | — |

---

## 4. Relationship disposition register

| rel_id | source | target | type | prior_status | post_status | correction_ref |
|--------|--------|--------|------|--------------|-------------|----------------|
| REL-ZPM-WB-01 | WEB-ZPM-01 | PRJ-0009 | **BELONGS_TO** | queued | **retained — ready** | COR-ZPM-WEB-08 |
| REL-ZPM-WB-02 | WEB-ZPM-02 | PRJ-0010 | **BELONGS_TO** | queued | **cancelled** | COR-ZPM-WEB-06 |
| REL-ZPM-WB-03 | WEB-ZPM-01 | PRJ-0010 | **BELONGS_TO** | not present | **created — queued** | COR-ZPM-WEB-07 |
| *(TBD)* | ORG-0005 | WEB-ZPM-01 | **OWNS** | queued (dual) | **retained — single target** | COR-ZPM-WEB-09 |
| *(TBD)* | ORG-0005 | WEB-ZPM-02 | **OWNS** | queued | **cancelled** | COR-ZPM-WEB-09 |
| *(TBD)* | DOM-* bzpm.ru | WEB-ZPM-01 | **PRIMARY_DOMAIN** | ambiguous | **resolved — singleton** | COR-ZPM-WEB-10 |

---

## 5. Evidence re-index register

| evidence_ref | prior_routing | corrected_routing | correction_ref |
|--------------|---------------|-------------------|----------------|
| EV-ZPM-OP-ACT-01 | WEB-ZPM-01 · PRJ-0009 | **Unchanged** | — |
| EV-ZPM-OP-HIST-01 | WEB-ZPM-02 · PRJ-0010 | **PRJ-0010 only** | COR-ZPM-WEB-04 |
| EV-W1B-CC-01 §17 | Both websites (indirect) | **WEB-ZPM-01** org hostname corroboration | COR-ZPM-WEB-04 |

---

## 6. Attestation gate register

| gate / tranche | prior | corrected | correction_ref |
|----------------|-------|-----------|----------------|
| AT-W4-ZPM-01 | Proceed | **Proceed** — unchanged | — |
| AT-W4-ZPM-02 | Proceed | **Blocked** | COR-ZPM-WEB-05 |
| W4-ZPM-EG-03 | PRJ-0010 before WEB-ZPM-02 deprecated | **Obviated** | COR-ZPM-WEB-01 |
| W4-ZPM-EG-07 | EFV-03 no merge two Websites | **Single Website mint** | COR-ZPM-WEB-12 |
| W4-ZPM-LC-05 | PRJ-0010 + WEB-ZPM-02 deprecated pair | PRJ-0010 deprecated + WEB-ZPM-01 **active** | COR-ZPM-WEB-03 |

---

## 7. Document sync register

| document | sync_action | sync_status |
|----------|-------------|-------------|
| ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md | Full correction sync | **complete** |
| ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md | Full correction sync | **complete** |
| ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md | Full correction sync | **complete** |
| ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md | Created | **complete** |
| ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-REGISTER-v1.md | Created *(this)* | **complete** |
| ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-SUMMARY-v1.md | Created | **complete** |
| ATLAS-BACKUP-SNAPSHOT-v1.md | ZPM Website count refresh | **deferred** — next baseline pass |
| ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md | COR-ZPM-WEB finding note | **deferred** — next sync pass |

---

## 8. Audit finding clearance

| finding_id | severity | clearance |
|------------|----------|-----------|
| AUD-ZPM-WEB-01 | High | **Cleared** — WEB-ZPM-02 retired |
| AUD-ZPM-WEB-02 | High | **Cleared** — class separation restored |
| AUD-ZPM-WEB-03 | Medium | **Cleared** — Triumph precedent adopted |
| AUD-ZPM-WEB-04 | Medium | **Cleared** — EFV-03 scope corrected |
| AUD-ZPM-WEB-05 | Medium | **Cleared** — SU-W4-ZPM-03 resolved |
| AUD-ZPM-WEB-06 | Info | **N/A** — no action required |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Full execution record |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-SUMMARY-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-SUMMARY-v1.md) | Executive summary |
| [ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-DECISION-v1.md) | Operator decision authority |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Triumph REL-0027/0028 reference |

---

*ATLAS ZPM Website Model Correction Register v1 — executed 2026-06-07; population layer only.*
