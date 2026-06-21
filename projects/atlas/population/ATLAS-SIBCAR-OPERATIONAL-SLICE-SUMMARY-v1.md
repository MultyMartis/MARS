# ATLAS SIBCAR Operational Slice Summary v1

**Status:** **documented** — executive summary (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Subject:** ORG-0006 **SIBCAR** operational expansion beyond Organization · Legal Entity · CLIENT_OF  
**Parent:** [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) · [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md)

---

## Verdict

```text
SIBCAR OPERATIONAL SLICE EXPANSION — PARTIALLY READY
```

Structural stack (Project → Website → Domain) can proceed for **TEST** property `sibcar.new-site.space` using **E0** OCPilot evidence and attested commercial anchor **REL-0041**. Production URL, registrar proof, and EAR published snapshot remain **BLOCKED** or deferred.

**No entities minted. No relationships created. No attestation performed.**

---

## 1. Attested baseline (complete)

| Layer | ID | Status |
|-------|-----|--------|
| Organization | ORG-0006 SIBCAR | **active** — AT-W1C-01 |
| Legal Entity | LE-0005 ООО «СибКар» | **active** — AT-W1C-01 |
| Commercial | REL-0041 ORG-0006 → ORG-0001 **CLIENT_OF** | **active** — AT-W6B-02 |

**Slice score today:** **2.0 / 7** (SUB-06). **Estimated after expansion:** **~5.0 / 7**.

---

## 2. Existing evidence inventory (condensed)

| Tier | Key artifacts |
|------|---------------|
| **E1** | EV-W1C-CC-01 — Counterparty Card `sibcar\Реквизиты.docx` |
| **E0 operational** | EV-W1C-02 site-passport · EV-W1C-03 project-access-brief · OCPilot INTAKE-COMPLETE · AUDIT-CHARTER |
| **Attestation** | AT-W1C-01 (org) · AT-W6B-02 (REL-0041) |
| **EAR design** | EV-EAR-01 acquisition options · EV-EAR-02 workflow example · pre-runtime-bridge freeze |
| **Gaps** | Production URL · corporate domain · EAR snapshot · Run 5 file-manifest |

---

## 3. Candidate Project roster

| Label | Name | Lifecycle | Roster | Readiness |
|-------|------|-----------|--------|-----------|
| **SIBCAR-INTAKE-CAND-A01** | Автосалон СИБКАР — OpenCart dealership | **active** | **Wave 3 — P0** | **PARTIAL** |

Single active engagement evidenced (rebranding, catalog, SEO prep, OCPilot pilot). No historical second delivery (unlike ZPM dual PRJ).

**Rejected:** OCPilot Run 5 as Atlas Project; SITE-001 as Project entity; BZPM merge.

---

## 4. Candidate Website roster

| Label | URL | Environment | Roster | Readiness |
|-------|-----|-------------|--------|-----------|
| **SIBCAR-INTAKE-WEB-01** | `https://sibcar.new-site.space/` | **TEST** | **Wave 4 — P0** | **PARTIAL** |
| SIBCAR-INTAKE-WEB-02 | **SAFE UNKNOWN** | PROD | Deferred | **BLOCKED** |

Site title «Автосалон СИБКАР» — Website display only; **not** ORG-0006 alias.

---

## 5. Candidate Domain roster

| Label | FQDN | Roster | Readiness |
|-------|------|--------|-----------|
| **SIBCAR-INTAKE-DOM-01** | `sibcar.new-site.space` | **Wave 5 — P0** | **PARTIAL** |
| SIBCAR-INTAKE-DOM-02 | **SAFE UNKNOWN** | Deferred | **BLOCKED** |

Domain OWNS likely **defer** — registrar E1 absent (ZPM precedent).

---

## 6. Candidate relationships (draft)

| Wave | Types | Count | Readiness |
|------|-------|-------|-----------|
| **3B** | COMMISSIONED_BY · EXECUTES | 2 | **PARTIAL** |
| **4B** | BELONGS_TO · OWNS | 2 | **PARTIAL** |
| **5B** | PRIMARY_DOMAIN · OWNS *(defer)* | 2 | **PARTIAL** / defer |
| **6B** | CLIENT_OF | 1 | **READY** ✓ — REL-0041 attested |

---

## 7. Evidence readiness

| Target | Classification |
|--------|----------------|
| Wave 3 Project | **PARTIAL** |
| Wave 3B Project ↔ Org | **PARTIAL** |
| Wave 4 Website (TEST) | **PARTIAL** |
| Wave 4 Website (PROD) | **BLOCKED** |
| Wave 4B Website rels | **PARTIAL** |
| Wave 5 Domain (TEST) | **PARTIAL** |
| Wave 5 Domain (PROD) | **BLOCKED** |
| Wave 5B Domain rels | **PARTIAL** |
| OCPilot SITE-001 linkage | **PARTIAL** |
| EAR SITE-001 linkage | **BLOCKED** |

---

## 8. Recommended execution sequence

| Step | Wave | Action | Readiness |
|------|------|--------|-----------|
| **1** | **Wave 3** | Mint 1 Project (SIBCAR-INTAKE-CAND-A01) + attestation | **PARTIAL** |
| **2** | **Wave 3B** | COMMISSIONED_BY + EXECUTES edges | **PARTIAL** |
| **3** | **Wave 4** | Mint TEST Website `sibcar.new-site.space` + attestation | **PARTIAL** |
| **4** | **Wave 4B** | BELONGS_TO + OWNS edges | **PARTIAL** |
| **5** | **Wave 5** | Mint TEST Domain + attestation | **PARTIAL** |
| **6** | **Wave 5B** | PRIMARY_DOMAIN; defer Domain OWNS if no registrar E1 | **PARTIAL** |
| — | **EAR → OCPilot** | Publish SITE-001 snapshot (parallel, non-Atlas) | **BLOCKED** |
| ✓ | **Wave 6B** | REL-0041 CLIENT_OF | **Complete** |

**Precedent:** ZPM tranche ORG-0005 (PRJ-0009/0010 → WEB-ZPM-01 → DOM-ZPM-01).

**Optional:** Wave 2C Person — Карандашов М.П. on CC; not blocking structural stack.

---

## 9. Duplicate review

**Pass.** SIBCAR distinct from BZPM, Triumph, operator orgs. SITE-001 remains separate entity class. REL-0041 complements (does not replace) project-level edges.

---

## 10. SAFE UNKNOWN (blocking summary)

| Topic | Blocks |
|-------|--------|
| Production public URL | PROD Website / Domain |
| Registrar E1 | Domain OWNS (may defer) |
| EAR published snapshot | OCPilot Run 5 resume |
| SU-W6B-04 project boundary narrative | Wave 3 attestation quality (not population proposal) |

---

## 11. Final recommendation

Proceed with **SIBCAR Wave 3 Project population proposal** as next Atlas documentation tranche, followed sequentially by 3B → 4 → 4B → 5 → 5B for TEST property only.

Parallel track: operator EAR Mode 0/1 acquisition for SITE-001 to unblock OCPilot Run 5 — **outside** Atlas graph mutations.

**Do not** mint production Website / Domain until URL and registrar evidence arrive.

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-AUDIT-v1.md) | Full audit |
| [ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md](ATLAS-SIBCAR-OPERATIONAL-SLICE-REGISTER-v1.md) | Tabular register |
| [ATLAS-NEXT-EXPANSION-DECISION-SUMMARY-v1.md](../audit/ATLAS-NEXT-EXPANSION-DECISION-SUMMARY-v1.md) | Program-level priority P1 Direction A |

---

*ATLAS SIBCAR Operational Slice Summary v1 — documentation only.*
