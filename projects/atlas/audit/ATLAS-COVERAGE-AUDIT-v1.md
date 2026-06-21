# ATLAS Coverage Audit v1

**Status:** **documented** — business-reality coverage audit (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Auditor posture:** Registry Steward review (documentation-level)  
**Parent:** [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](ATLAS-COVERAGE-AUDIT-REGISTER-v1.md) · [ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md](ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md)  
**Baseline:** [ATLAS-BACKUP-SNAPSHOT-v1.md](../population/ATLAS-BACKUP-SNAPSHOT-v1.md) · [ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md](ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md) · Wave 1D Makita tranche (ORG-0007)  
**Is not:** population pass, attestation act, entity creation, relationship creation, Foundation amendment, runtime export, git commit.

**Restrictions observed:** No entities created. No relationships created. No lifecycle changes. No graph mutations. No Foundation changes.

---

# REPORT — ATLAS Coverage Audit

## 0. Audit scope and method

### 0.1 In-scope business subjects

| Subject | Contour type | Primary evidence |
|---------|--------------|------------------|
| **Polygon** | Operator (Category A) | ORG-0001 · Wave 1 dataset |
| **MetaCode** | Operator (Category A) | ORG-0002 · Wave 1 dataset |
| **i-SEO** | Operator (Category A) | ORG-0003 · Wave 1 dataset |
| **Triumph** | Client (Category A) | ORG-0004 · Waves 1–6A |
| **ЗПМ (ZPM)** | Client (Category A) | ORG-0005 · Waves 1B–5 ZPM |
| **SIBCAR** | Client (Category A) | ORG-0006 · Wave 1C |
| **Makita Snab** | i-SEO client (Category B) | ORG-0007 · Wave 1D + intake |
| **Dyakonov** | Contractor intake (Category A path) | Intake package 2026-06-07 |
| **Moscow SERM** | Unresolved partner contour | PER-0002 · OOEP Category A |
| **Metallka** | Unresolved partner contour | PER-0003 · OOEP Category A |

### 0.2 Entity classes under review

```text
Organization · Legal Entity · Person · Project · Website · Domain · Commercial relationship
```

**Commercial relationship** = attested Organization ↔ Organization edge in Wave 6A family (primarily **CLIENT_OF**), plus documented deferred candidates.

### 0.3 Method

1. Inventory **known business reality** from Wave 1 dataset, population registers, intake packages, deferred queues, and [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](../population/ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) channel map.
2. Reconcile against **attested** entity and relationship registers (lifecycle **active** / **deprecated** where applicable).
3. Classify each subject × class cell: **fully represented** · **partially represented** · **intake only** · **absent**.
4. Compute aggregate coverage using two documented methods (§2).
5. Inventory missing entities and relationship candidates (§3–§4).
6. Rank population priorities P0–P2 (§5).
7. Review expansion-risk areas (§6).

**Evidence boundary:** Audit is documentation-only. External CC storage (`C:\AI MARS STORAGE\atlas\evidence\`) referenced from registers; filesystem not re-verified in this pass.

**Baseline note:** [ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md](ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md) counts **6** Organizations (pre–Wave 1D). This audit treats **ORG-0007 Makita Snab** (AT-W1D-01, 2026-06-07) as **in scope** and adjusts totals accordingly.

---

## 1. Current Atlas inventory (attested)

| Class | Total attested | **active** | **deprecated** | Register authority |
|-------|----------------|------------|----------------|-------------------|
| Organization | **7** | **7** | 0 | Wave 1 + 1B + 1C + **1D** |
| Legal Entity | **5** | **5** | 0 | Wave 1 + 1B + 1C |
| Person | **15** | **15** | 0 | Wave 2 + 2 ZPM |
| Project | **8** | **6** | **2** | Wave 3 + 3 ZPM |
| Website | **5** | **5** | 0 | Wave 4 + 4 ZPM |
| Domain | **5** | **5** | 0 | Wave 5 + 5 ZPM |
| Relationship | **45** | **45** | 0 | Waves 2B–6A |

**Deferred (documented, not counted as attested):** WEB-0001..0005 operator sites; PRJ-0002, PRJ-0003 (no evidence); Wave 5B ZPM **PRIMARY_DOMAIN**; Domain **OWNS** family (all orgs); Wave 6 **CLIENT_OF** for ЗПМ, SIBCAR, Makita, partner contours.

---

## 2. Coverage verdict

### 2.1 Final verdict

```text
ATLAS COVERAGE: PARTIAL — ~55% (entity-class aggregate)
```

Atlas **полностью** покрывает **клиентский контур Triumph** (delivery stack: org → project → website → domain → commercial vendor edge). Остальные контуры — **operator anchors**, **latent clients**, **partner isolates**, **intake** — имеют **материальные пробелы** в web-identity, commercial graph и downstream waves.

**Headline by class:**

| Class | Coverage vs known reality | Verdict |
|-------|---------------------------|---------|
| Organization | **7 / 10** known subjects | **70%** — strongest class |
| Legal Entity | **5 / 9** known subjects | **56%** — Makita + partners + Dyakonov deferred |
| Person | **15 / 17** named contacts | **88%** — partners isolated without org edges |
| Project | **8 / 10** current initiatives | **80%** — SIBCAR OCPilot + Makita SEO not minted |
| Website | **5 / 14** documented properties | **36%** — operator + Makita + SIBCAR gap |
| Domain | **5 / 14** hostname candidates | **36%** — mirrors website gap |
| Commercial relationship | **1 / 7+** documented org↔org edges | **14%** — critical structural undercoverage |

### 2.2 Method A — entity-class ratio (primary)

**Known universe** = documented references with steward-confirmed or intake-level evidence (excludes ZPM **future** held candidates FUT-01..04).

| Class | Known | Attested | Ratio |
|-------|-------|----------|-------|
| Organization | 10 | 7 | **70%** |
| Legal Entity | 9 | 5 | **56%** |
| Person | 17 | 15 | **88%** |
| Project | 10 | 8 | **80%** |
| Website | 14 | 5 | **36%** |
| Domain | 14 | 5 | **36%** |
| Commercial rel. | 7 | 1 | **14%** |
| **Simple mean** | — | — | **~55%** |

### 2.3 Method B — slice × class slot score (secondary)

10 subjects × 7 classes = **70 slots**. Scoring: full = 1.0 · partial = 0.5 · intake only = 0.25 · absent = 0.

| Subject | Slot score | % of 7 |
|---------|------------|--------|
| Triumph | 7.0 | **100%** |
| ЗПМ | 6.0 | **86%** |
| Polygon | 4.0 | **57%** |
| i-SEO | 3.0 | **43%** |
| SIBCAR | 2.0 | **29%** |
| MetaCode | 2.5 | **36%** |
| Dyakonov | 1.75 | **25%** |
| Makita Snab | 0.5 | **7%** |
| Moscow SERM | 0.5 | **7%** |
| Metallka | 0.5 | **7%** |
| **Total** | **27.75 / 70** | **~40%** |

Method A weights **entity inventory**; Method B weights **operating contours**. Both are reported; **Method A (~55%)** is the primary headline because it aligns with «percentage of known business subjects represented as entities.»

---

## 3. Coverage matrix (by business subject)

Legend: **F** fully represented · **P** partially represented · **I** intake only · **A** absent

| Subject | Org | LE | Person | Project | Website | Domain | Commercial | Slice verdict |
|---------|-----|----|----|---------|---------|--------|------------|---------------|
| **Polygon** | F | F | F | P | A | A | P | **Partial** |
| **MetaCode** | F | P | P | P | A | A | A | **Partial** |
| **i-SEO** | F | F | F | A | A | A | A | **Partial** |
| **Triumph** | F | F | F | F | F | F | F | **Full** |
| **ЗПМ** | F | F | F | F | F | P | P | **Partial** |
| **SIBCAR** | F | F | A | A | A | A | A | **Partial** |
| **Makita Snab** | P | A | A | A | A | A | A | **Partial** |
| **Dyakonov** | I | I | I | A | A | A | A | **Intake only** |
| **Moscow SERM** | A | A | P | A | A | A | A | **Partial** |
| **Metallka** | A | A | P | A | A | A | A | **Partial** |

### 3.1 Per-slice notes

**Polygon** — ORG-0001 + LE-0001 + PER-0001 (REL-0001 OWNER) attested. Execution role on Triumph/ZPM projects via Wave 3B **EXECUTES**. Operator websites WEB-0001 `polygon-ws.ru`, WEB-0002 `polygon-ws.com` **deferred**. Commercial: inbound **CLIENT_OF** only from Triumph (REL-0016); ЗПМ / SIBCAR edges **not minted**.

**MetaCode** — ORG-0002 attested; shares LE-0001 IP context with Polygon. PER-0001 **OWNER** (REL-0002). PRJ-0001 MARS lists MetaCode as execution display context — no dedicated MetaCode project portfolio. WEB-0003 `metacode-agency.com`, WEB-0004 `metacode-agency.ru` **deferred**. No commercial edges.

**i-SEO** — ORG-0003 + LE-0002 + seven attested persons (REL-0006..0012). WEB-0005 `i-seo.su` **deferred**. No Project entities for SEO delivery; Makita Snab (ORG-0007) is a separate org with **no** CLIENT_OF edge to i-SEO. Category B Makita path does not substitute i-SEO operator web identity.

**Triumph** — Full Wave 1–6A client stack: ORG-0004, LE-0003, PER-0004..0006, PRJ-0004..0008, WEB-0006..0009, DOM-0001..0004, REL-0016 **CLIENT_OF** → Polygon. Only contour at **full** coverage.

**ЗПМ** — ORG-0005 (renamed from BZPM), LE-0004, PER-0014..0015, PRJ-0009..0010, WEB-ZPM-01, DOM-ZPM-01, nine ZPM-specific relationships attested. **Gaps:** REL **CLIENT_OF** ORG-0005 → ORG-0001 (SU-REL-04); Wave 5B **PRIMARY_DOMAIN** for DOM-ZPM-01 **deferred** per backup snapshot; Domain **OWNS** registrant **SAFE UNKNOWN** (ME-W5-ZPM-01).

**SIBCAR** — ORG-0006 + LE-0005 attested at E1 (AT-W1C-01). **No** Person, Project, Website, Domain, or commercial edges. OCPilot SITE-001 / `sibcar.new-site.space` documented as **candidates**, not minted.

**Makita Snab** — ORG-0007 attested at E0 Category B (AT-W1D-01). Legal entity, Person (Артём), two websites, two domains, SEO projects, i-SEO commercial edge — **all absent**. Prior intake label MAKITA-INTAKE-CAND-O01 superseded by ORG-0007 for Organization layer only.

**Dyakonov** — Intake package complete (EV-DYAK-OP-01..02). DYAKONOV-INTAKE-CAND-O01 / LE01 / P01 at **E0**; CC folder **absent**. Target **CONTRACTOR** edge to ORG-0001 **not created**.

**Moscow SERM** — PER-0002 Фатюткин attested with **SAFE UNKNOWN** primary org (SU-PER-01). CC path `moscow-serm\` mapped Category A; Organization **not populated**. Wave 2B partner isolation by design.

**Metallka** — PER-0003 Лиматов attested with **SAFE UNKNOWN** primary org (SU-PER-02). CC path `metallka\` mapped Category A; Organization **not populated**. Same isolation posture as Moscow SERM.

---

## 4. Missing entities inventory

References appearing in Atlas documentation **without** a minted canonical entity (`ORG-*`, `LE-*`, `PER-*`, `PRJ-*`, `WEB-*`, `DOM-*`).

### 4.1 Organizations

| Reference | Documented name / slug | Evidence | Blocking factor |
|-----------|------------------------|----------|-----------------|
| Moscow SERM contour | Moscow SERM · `moscow-serm` | E0 PER-0002; OOEP Category A | CC path expected; org wave not executed |
| Metallka contour | Metallka · `metallka` | E0 PER-0003; OOEP Category A | CC path expected; org wave not executed |
| DYAKONOV-INTAKE-CAND-O01 | ИП Дьяконов · `dyakonov` | E0 intake | CC absent |

### 4.2 Legal entities

| Reference | Parent contour | Evidence | Blocking factor |
|-----------|----------------|----------|-----------------|
| Makita LE (LE-0006 candidate) | ORG-0007 | Category B — LE deferred by rule | E1+ CC or E2 registry extract |
| DYAKONOV-INTAKE-CAND-LE01 | Dyakonov | E0 intake | CC absent |
| Moscow SERM LE | Moscow SERM | **SAFE UNKNOWN** | Org not populated |
| Metallka LE | Metallka | **SAFE UNKNOWN** | Org not populated |

### 4.3 Persons

| Reference | Context | Evidence | Blocking factor |
|-----------|---------|----------|-----------------|
| Артём (Makita contact) | ORG-0007 operational | E0 EV-MAKITA-OP-01 | Full legal name **SAFE UNKNOWN** |
| DYAKONOV-INTAKE-CAND-P01 | Dyakonov | E0 intake | CC absent |
| Moscow SERM staff beyond PER-0002 | Partner contour | **SAFE UNKNOWN** | Org not populated |
| Metallka staff beyond PER-0003 | Partner contour | **SAFE UNKNOWN** | Org not populated |

### 4.4 Projects

| Reference | Contour | Evidence | Blocking factor |
|-----------|---------|----------|-----------------|
| SIBCAR OCPilot engagement | ORG-0006 · SITE-001 | E1 CC + OCPilot site-passport | Wave 3 not executed for SIBCAR |
| Makita SEO (makita-snab.ru + makita-land.ru) | ORG-0007 · i-SEO service | E0 EV-MAKITA-OP-01..03 | No PRJ-* mint; org-only Wave 1D |
| PRJ-0002, PRJ-0003 | Wave 1 dataset placeholders | No evidence | Explicitly excluded |
| ZPM-INTAKE-FUT-01..04 | ORG-0005 future | Held — no start evidence | **Not current reality** — excluded from coverage numerator |

### 4.5 Websites

| Reference | URL / hostname | Contour | Status |
|-----------|----------------|---------|--------|
| WEB-0001 | `polygon-ws.ru` | Polygon | **Deferred** — dataset |
| WEB-0002 | `polygon-ws.com` | Polygon | **Deferred** |
| WEB-0003 | `metacode-agency.com` | MetaCode | **Deferred** |
| WEB-0004 | `metacode-agency.ru` | MetaCode | **Deferred** |
| WEB-0005 | `i-seo.su` | i-SEO | **Deferred** |
| MAKITA-INTAKE-WEB-C01 | `makita-snab.ru` | Makita | **Candidate** — Wave 4 |
| MAKITA-INTAKE-WEB-C02 | `makita-land.ru` | Makita | **Candidate** |
| SIBCAR TEST site | `sibcar.new-site.space` | SIBCAR | **Candidate** — OCPilot |

### 4.6 Domains

Hostname candidates mirroring §4.5 website inventory (operator ×5, Makita ×2, SIBCAR ×1). **None minted** except Triumph (DOM-0001..0004) and ZPM (DOM-ZPM-01).

---

## 5. Missing relationship inventory

Relationship candidates **known** from registers and deferred queues **without** attested `REL-*` rows.

### 5.1 Commercial (Organization ↔ Organization)

| Candidate | Source → Target | Type | Documented in | Priority signal |
|-----------|-----------------|------|---------------|-----------------|
| REL-0016 *(attested)* | ORG-0004 → ORG-0001 | **CLIENT_OF** | Wave 6A | **Present** |
| SU-REL-04 | ORG-0005 → ORG-0001 | **CLIENT_OF** | Integrity register | Active client with full stack |
| SU-REL-06 | ORG-0006 → ORG-0001 | **CLIENT_OF** | SIBCAR org register §5 | W1-C client |
| Makita → i-SEO | ORG-0007 → ORG-0003 | **CLIENT_OF** *(proposed)* | Makita intake / ORG-0007 register §6 | Category B SEO client |
| Moscow SERM → vendor | TBD → ORG-0001 or ORG-0002 | **CLIENT_OF** / **PARTNER_OF** | Wave 6A deferred §5 | Partner contour |
| Metallka → vendor | TBD → ORG-0001 or ORG-0002 | **CLIENT_OF** / **PARTNER_OF** | Wave 6A deferred §5 | Partner contour |
| ORG-0002 MetaCode commercial | — | — | Wave 6A deferred §5 | No approved candidate |

### 5.2 Person ↔ Organization (deferred / blocked)

| Candidate | Type | Blocker |
|-----------|------|---------|
| PER-0002 → Moscow SERM org | EMPLOYEE / OWNER / PARTNER | Org not populated |
| PER-0003 → Metallka org | EMPLOYEE / OWNER / PARTNER | Org not populated |
| Артём → ORG-0007 | REPRESENTATIVE / CONTACT | Person not minted |
| Dyakonov → ORG-0001 | **CONTRACTOR** | Intake — CC required |
| REL-0003 PER-0001 MANAGER ORG-0003 | MANAGER | Rejected / deferred (SU-REL-09) |

### 5.3 Domain / Website family (deferred)

| Candidate | Type | Scope |
|-----------|------|-------|
| DOM-ZPM-01 → WEB-ZPM-01 | **PRIMARY_DOMAIN** | Wave 5B ZPM — **deferred** |
| ORG-* → DOM-* | **OWNS** | All domains — registrant **SAFE UNKNOWN** |
| ORG-0001 → WEB-0006..0009 | **OPERATES** | SU-WEB-01 — steward choice |
| WEB-0006 → PRJ-0006 | **BELONGS_TO** | SEO project on main site — Wave 4B review |

### 5.4 Person ↔ Project

| Candidate | Documented in | Status |
|-----------|---------------|--------|
| PER-* ↔ PRJ-* participation edges | Wave 3 register §4 | **Deferred** — SU-REL-10 |

---

## 6. Priority queue (next population candidates)

Ranked by **business importance** (consumer handoff, commercial clarity, partner isolation resolution, active engagement). **Documentation-only ranking** — not a population authorization.

### P0 — Resolve structural blind spots on active revenue / partner contours

| Rank | Target | Rationale |
|------|--------|-----------|
| P0-1 | **Moscow SERM Organization** (+ LE, PER-0002 edge) | Category A channel; CC folder mapped; PER-0002 isolated since Wave 2; blocks partner 2B and commercial graph |
| P0-2 | **Metallka Organization** (+ LE, PER-0003 edge) | Same posture as P0-1 |
| P0-3 | **ORG-0005 CLIENT_OF ORG-0001** | Full ZPM stack attested except commercial edge; SU-REL-04 Medium |
| P0-4 | **SIBCAR Wave 3 Project** (OCPilot SITE-001) + **Wave 4 Website** | Active OpenCart engagement documented; org-only coverage insufficient for OCPilot consumer |

### P1 — Complete partial client / contractor contours

| Rank | Target | Rationale |
|------|--------|-----------|
| P1-1 | **Makita Wave 4 Websites** (×2) + **Wave 5 Domains** + Person Артём | ORG-0007 exists; i-SEO SEO service on both sites is operational reality |
| P1-2 | **Makita CLIENT_OF i-SEO** (Wave 6 extension) | Closes i-SEO channel client commercial graph |
| P1-3 | **Dyakonov CC collection → Org + LE + Person + CONTRACTOR** | Polygon contractor; Category A path; CC gate explicit |
| P1-4 | **ORG-0006 CLIENT_OF ORG-0001** | W1-C client commercial parity with Triumph |
| P1-5 | **Operator websites WEB-0001..0005** | Operator web identity gap; dataset-backed; lower consumer urgency than clients |

### P2 — Refinement and low-urgency expansion

| Rank | Target | Rationale |
|------|--------|-----------|
| P2-1 | **Wave 5B ZPM PRIMARY_DOMAIN** + Domain OWNS when registrar E1 available | DOM-ZPM-01 minted; family edge deferred |
| P2-2 | **Makita Legal Entity** when E1+ evidence appears | Category B allows org-without-LE; not blocking org active |
| P2-3 | **PRJ-0001 COMMISSIONED_BY** resolution | Internal MARS project; SU-PRJ-01/02 Low |
| P2-4 | **Person ↔ Project edges** | SU-REL-10; enrichment not anchor |
| P2-5 | **ORG-0002 MetaCode commercial edges** | No approved candidate in Wave 6A |

---

## 7. Expansion risk review

Areas where Atlas expansion would currently produce **low-value documentation growth** (documentation volume without proportional business-reality gain).

| Risk ID | Area | Risk description | Mitigation |
|---------|------|------------------|------------|
| **EXP-COV-01** | Register sync without population | Repeated register/snapshot refresh passes (ZPM-C-01..09 pattern) inflate doc count without new entities | Batch sync with population waves; avoid standalone sync-only sprints |
| **EXP-COV-02** | Full Person contact register | Expanding [ATLAS-WAVE2-PERSON-REGISTER-v1.md](../population/ATLAS-WAVE2-PERSON-REGISTER-v1.md) to all PER-* before consumer need | Maintain PER-0011 pattern — contact rows on maintenance trigger only |
| **EXP-COV-03** | ZPM future projects (FUT-01..04) | Minting SEO/Direct/AI/OCPilot projects without start evidence | Hold per [ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md](../population/ATLAS-ZPM-PROJECT-INTAKE-SUMMARY-v1.md) |
| **EXP-COV-04** | MARS program registry as Atlas Projects | Conflating `registry/project-registry.md` rows with `PRJ-*` | Maintain E-17 exclusion in Wave 3 register §5 |
| **EXP-COV-05** | ORCA / MIG pilot cross-refs for Makita | ORCA Makita pilot is **excluded** org evidence (W1D-D-07); expanding pilot docs into Atlas | Keep pilot boundary; use ORG-0007 + Wave 4 only |
| **EXP-COV-06** | Patronymic / contact SAFE UNKNOWN closure | SU-PER-04 Low — bulk Person field completion | Defer until CPV maintenance or consumer contract requires |
| **EXP-COV-07** | MetaCode standalone LE split | Splitting LE-0001 from Polygon without legal/business driver | Document share context; no LE mint without CC evidence |
| **EXP-COV-08** | i-SEO client catalog breadth | Category B allows many E0 orgs; indiscriminate intake | Apply OOEP + enrichment gate per Makita precedent; prioritize sites with active delivery |
| **EXP-COV-09** | Inverse VENDOR_OF mirrors | Wave 6A explicitly rejected ORG-0001 VENDOR_OF ORG-0004 | Do not mint symmetric edges for documentation completeness |
| **EXP-COV-10** | Domain OWNS without registrar E1 | Minting OWNS edges while SU-DOM-01..05 open | Wait for E1 registrar evidence per Wave 5B neutrality register |

---

## 8. Validation checklist

| Constraint | Status |
|------------|--------|
| No new entities | **Pass** |
| No new relationships | **Pass** |
| No lifecycle changes | **Pass** |
| No graph mutations | **Pass** |
| No Foundation changes | **Pass** |
| No attestation acts | **Pass** |
| No population execution | **Pass** |

---

## 9. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](ATLAS-COVERAGE-AUDIT-REGISTER-v1.md) | Tabular coverage + missing inventory register |
| [ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md](ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md) | Executive summary |
| [ATLAS-INTEGRITY-SNAPSHOT-SUMMARY-v1.md](ATLAS-INTEGRITY-SNAPSHOT-SUMMARY-v1.md) | Prior integrity baseline |
| [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](../population/ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | Category A/B channel rules |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](../population/ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Commercial deferred queue |

---

*ATLAS Coverage Audit v1 — audit only; no commit.*
