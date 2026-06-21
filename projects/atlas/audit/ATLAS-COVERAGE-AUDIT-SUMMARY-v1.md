# ATLAS Coverage Audit Summary v1

**Status:** **documented** — business-reality coverage audit summary (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Parent:** [ATLAS-COVERAGE-AUDIT-v1.md](ATLAS-COVERAGE-AUDIT-v1.md) · [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](ATLAS-COVERAGE-AUDIT-REGISTER-v1.md)  
**Is not:** population pass, attestation act, runtime export, git commit.

---

## Final verdict

```text
ATLAS COVERAGE: PARTIAL — ~55% of known business reality represented
```

Atlas **полностью** покрывает контур **Triumph** (единственный subject со статусом **Full** по всем семи классам). Контур **ЗПМ** близок к полноте (**86%** slice score). **Operator web-identity**, **commercial graph**, **latent clients** (SIBCAR, Makita assets), и **partner contours** (Moscow SERM, Metallka) создают системный пробел: **Website / Domain ~36%**, **Commercial ~14%**.

**Validation:** No entities created. No relationships created. No lifecycle changes. No graph mutations. No Foundation changes.

---

## 1. Entity statistics (attested)

| Class | Total | **active** | **deprecated** |
|-------|-------|------------|----------------|
| Organization | **7** | **7** | 0 |
| Legal Entity | **5** | **5** | 0 |
| Person | **15** | **15** | 0 |
| Project | **8** | **6** | **2** |
| Website | **5** | **5** | 0 |
| Domain | **5** | **5** | 0 |
| Commercial rel. (org↔org) | **1** | **1** | 0 |

**Note:** ORG-0007 Makita Snab (Wave 1D) postdates Integrity Snapshot baseline (6 orgs).

---

## 2. Coverage by class

| Class | Known | Attested | Coverage |
|-------|-------|----------|----------|
| Organization | 10 | 7 | **70%** |
| Legal Entity | 9 | 5 | **56%** |
| Person | 17 | 15 | **88%** |
| Project | 10 | 8 | **80%** |
| Website | 14 | 5 | **36%** |
| Domain | 14 | 5 | **36%** |
| Commercial relationship | 7 | 1 | **14%** |
| **Aggregate (mean)** | — | — | **~55%** |

---

## 3. Coverage matrix (compact)

| Subject | Verdict | Strongest class | Critical gap |
|---------|---------|-----------------|--------------|
| **Triumph** | **Full** | All seven classes | — |
| **ЗПМ** | Partial | Org → Domain stack | CLIENT_OF; Wave 5B PRIMARY_DOMAIN |
| **Polygon** | Partial | Org, LE, Person | Operator websites; outbound commercial |
| **i-SEO** | Partial | Person roster (×7) | Website, projects, commercial |
| **MetaCode** | Partial | Org | Websites, commercial, dedicated LE |
| **SIBCAR** | Partial | Org + LE (E1) | Project, Website, Person, commercial |
| **Makita Snab** | Partial | Org only (E0) | LE, Person, sites, domains, commercial |
| **Dyakonov** | **Intake only** | Intake analysis | All canonical IDs |
| **Moscow SERM** | Partial | PER-0002 only | Organization + all downstream |
| **Metallka** | Partial | PER-0003 only | Organization + all downstream |

---

## 4. Missing inventory (counts)

| Category | Count |
|----------|-------|
| Missing Organization references | **3** |
| Missing Legal Entity references | **4** |
| Missing Person references | **4** |
| Missing Project references | **2** *(current reality; excl. PRJ-0002/0003)* |
| Missing Website references | **8** |
| Missing Domain references | **8** |
| Missing commercial relationship candidates | **6** |
| Missing non-commercial relationship candidates | **12** |

Full rows: [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](ATLAS-COVERAGE-AUDIT-REGISTER-v1.md) §3–§4.

---

## 5. Priority queue

### P0 — Structural blind spots

1. **Moscow SERM Organization** + LE + PER-0002 edge  
2. **Metallka Organization** + LE + PER-0003 edge  
3. **ORG-0005 CLIENT_OF ORG-0001** (ЗПМ commercial)  
4. **SIBCAR Project + Website** (OCPilot SITE-001)

### P1 — Partial contour completion

1. **Makita** Websites (×2) + Domains (×2) + Person Артём  
2. **Makita CLIENT_OF i-SEO**  
3. **Dyakonov** CC → Org + LE + Person + CONTRACTOR  
4. **SIBCAR CLIENT_OF ORG-0001**  
5. **Operator WEB-0001..0005**

### P2 — Refinement

1. ZPM Wave 5B **PRIMARY_DOMAIN**  
2. Makita LE when E1+ evidence appears  
3. PRJ-0001 COMMISSIONED_BY  
4. Person ↔ Project edges  
5. MetaCode commercial edges  

---

## 6. Expansion risk (top signals)

| Risk | Posture |
|------|---------|
| Register sync without population | Couple to waves — avoid doc-only sprints |
| ZPM future projects without evidence | Hold FUT-01..04 |
| MARS program registry → PRJ-* | Maintain E-17 exclusion |
| Indiscriminate i-SEO Category B intake | OOEP gate per Makita precedent |
| Domain OWNS without registrar E1 | Defer until E1 |

Full register: [ATLAS-COVERAGE-AUDIT-v1.md](ATLAS-COVERAGE-AUDIT-v1.md) §7.

---

## 7. Recommended next population targets

**Immediate (P0):** Partner org contours (**Moscow SERM**, **Metallka**) — unlock two isolated Persons and commercial graph expansion. **ЗПМ CLIENT_OF** — one edge, high value on fully attested stack. **SIBCAR OCPilot** — Project + Website for active consumer engagement.

**Near-term (P1):** **Makita** asset layer (sites, domains, contact Person, i-SEO commercial). **Dyakonov** after CC placement. **Operator websites** when steward prioritizes operator web-identity.

**Defer (P2):** Domain OWNS family, Person↔Project enrichment, MetaCode commercial — low consumer urgency or evidence-gated.

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-COVERAGE-AUDIT-v1.md](ATLAS-COVERAGE-AUDIT-v1.md) | Full audit report |
| [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](ATLAS-COVERAGE-AUDIT-REGISTER-v1.md) | Tabular register |
| [ATLAS-INTEGRITY-SNAPSHOT-SUMMARY-v1.md](ATLAS-INTEGRITY-SNAPSHOT-SUMMARY-v1.md) | Prior integrity gate |
| [ATLAS-BACKUP-SNAPSHOT-v1.md](../population/ATLAS-BACKUP-SNAPSHOT-v1.md) | Point-in-time baseline |

---

*ATLAS Coverage Audit Summary v1 — audit only; no commit.*
