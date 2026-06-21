# ATLAS Next Expansion Decision Register v1

**Status:** **documented** — tabular expansion-direction decision register (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Parent:** [ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md](ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md) · [ATLAS-NEXT-EXPANSION-DECISION-SUMMARY-v1.md](ATLAS-NEXT-EXPANSION-DECISION-SUMMARY-v1.md)  
**Is not:** population register, attested export, runtime registry, git commit.

---

## 1. Register summary

| Metric | Value |
|--------|-------|
| Directions evaluated | **4** (A–D) |
| Attested baseline entities | **41** (7 org + 5 LE + 15 per + 8 prj + 5 web + 5 dom + 1 commercial rel) |
| Attested baseline coverage | **~55%** aggregate |
| Attainable relationship edges (C, now) | **3** |
| Attainable entity units (A+B, est.) | **~18–23** |
| Attainable entity units (D, est.) | **~6–10** *(high uncertainty)* |
| **Recommended lead direction** | **C** — ZPM CLIENT_OF |
| **Recommended second direction** | **A** — SIBCAR structural stack |

---

## 2. Direction decision register (master)

| dir_id | direction | anchor_state | orgs_Δ | le_Δ | persons_Δ | projects_Δ | websites_Δ | domains_Δ | rels_Δ | total_units_Δ | effort | evidence | business_value | priority |
|--------|-----------|--------------|--------|------|-----------|------------|------------|-----------|--------|---------------|--------|----------|----------------|----------|
| **DIR-A** | SIBCAR expansion | ORG-0006 **active**; LE-0005 **active**; OCPilot SITE-001 | 0 | 0 | 0–1 | 1 | 1 | 1 | 4–6 | **7–10** | **Medium** | **High** | **High** | **P1** |
| **DIR-B** | Makita expansion | ORG-0007 **active** E0; 2 sites; contact Артём; no LE | 0 | 0 | 1 | 1 | 2 | 2 | 5–7 | **11–13** | **Medium–High** | **Medium** | **Medium–High** | **P2** |
| **DIR-C** | Commercial graph | REL-0016 only; 6 deferred candidates | 0 | 0 | 0 | 0 | 0 | 0 | 3 *(now)* | **3** | **Low** | **High** *(lead)* | **High** | **P0** |
| **DIR-D** | New contours | PER-0002 Moscow SERM; PER-0003 Metallka; no org | 2 | 0–2 | 0 | 0 | 0 | 0 | 4–6 | **6–10** | **High** | **Low–Medium** | **Medium** | **P3** |

**Δ notation:** estimated new attested units if direction is executed in next phase; **not** minted in this audit.

---

## 3. Direction A — SIBCAR expansion register

### 3.1 Current state

| field | value |
|-------|-------|
| org_id | ORG-0006 |
| le_id | LE-0005 |
| lifecycle | **active** — AT-W1C-01 |
| evidence_tier | **E1** — EV-W1C-CC-01 |
| ocpilot_ref | SITE-001 |
| website_candidate | `sibcar.new-site.space` |
| slice_score | **2.0 / 7** |
| primary_gap | Project, Website, Domain, commercial, optional Person |

### 3.2 Coverage gain breakdown

| class | count | candidate_labels | wave |
|-------|-------|------------------|------|
| Organization | 0 | — | — |
| Legal Entity | 0 | — | — |
| Person | 0–1 | SIBCAR contact *(CC thin)* | Wave 2C |
| Project | 1 | OCPilot OpenCart engagement | Wave 3 |
| Website | 1 | `sibcar.new-site.space` TEST | Wave 4 |
| Domain | 1 | `sibcar.new-site.space` | Wave 5 |
| Relationships | 4–6 | COMMISSIONED_BY, EXECUTES, BELONGS_TO, OWNS, Person→Org?, CLIENT_OF* | Wave 3B/4B/6 |

*\*CLIENT_OF counted under DIR-C execution unit C-02.*

### 3.3 Scoring

| criterion | rating | notes |
|-----------|--------|-------|
| Effort | **Medium** | ~6–8 wave packages; templates exist |
| Evidence readiness | **High** | E1 CC + OCPilot site-passport + project-access-brief |
| Business value | **High** | OCPilot consumer; E1 legal contour |
| Priority | **P1** | After DIR-C lead act |

---

## 4. Direction B — Makita expansion register

### 4.1 Current state

| field | value |
|-------|-------|
| org_id | ORG-0007 |
| le_id | **none** — SAFE UNKNOWN |
| lifecycle | **active** — AT-W1D-01 |
| evidence_tier | **E0** — EV-MAKITA-OP-01..03 |
| website_candidates | makita-snab.ru; makita-land.ru |
| contact_signal | Артём; +7 926 022-30-91 |
| vendor_context | ORG-0003 i-SEO *(informational)* |
| slice_score | **0.5 / 7** |
| primary_gap | LE, Person, Project, Website ×2, Domain ×2, commercial |

### 4.2 Coverage gain breakdown

| class | count | candidate_labels | wave |
|-------|-------|------------------|------|
| Organization | 0 | — | — |
| Legal Entity | 0 | LE deferred | — |
| Person | 1 | Артём *(given name only)* | Wave 2 |
| Project | 1 | Dual-site SEO engagement | Wave 3 |
| Website | 2 | makita-snab.ru; makita-land.ru | Wave 4 |
| Domain | 2 | makita-snab.ru; makita-land.ru | Wave 5 |
| Relationships | 5–7 | OWNS ×2, BELONGS_TO, Person→Org, COMMISSIONED_BY/EXECUTES, CLIENT_OF* | Wave 3B/4B/6 |

*\*CLIENT_OF = execution unit C-03.*

### 4.3 Scoring

| criterion | rating | notes |
|-----------|--------|-------|
| Effort | **Medium–High** | Dual-site doubles Wave 4/5 surface; partial Person name |
| Evidence readiness | **Medium** | E0 only; CC absent |
| Business value | **Medium–High** | i-SEO channel; no CMS consumer urgency |
| Priority | **P2** | After DIR-A structural stack |

---

## 5. Direction C — Commercial graph register

### 5.1 Current state

| field | value |
|-------|-------|
| attested_edges | REL-0016 (ORG-0004 → ORG-0001) |
| commercial_coverage | **14%** (1/7) |
| precedent | Wave 6A attestation chain |
| deferred_count | 6 (MREL-C-02..06) |
| attainable_now | 3 edges |

### 5.2 Executable unit register

| unit_id | source | target | type | evidence_ref | evidence_tier | attested | effort | priority | sequence |
|---------|--------|--------|------|--------------|---------------|----------|--------|----------|----------|
| **C-01** | ORG-0005 ЗПМ | ORG-0001 Полигон | **CLIENT_OF** | SU-REL-04; Wave 3B-ZPM; EV-W1B-CC-01 | **E1** | **No** | **Low** | **P0** | **1** |
| **C-02** | ORG-0006 SIBCAR | ORG-0001 Полигон | **CLIENT_OF** | SIBCAR register §5; EV-W1C-CC-01 | **E1** | **No** | **Low–Medium** | **P2** | **7** |
| **C-03** | ORG-0007 Makita | ORG-0003 i-SEO | **CLIENT_OF** | Makita register §6; EV-MAKITA-OP-01..03 | **E0** | **No** | **Low–Medium** | **P2** | **6** |
| **C-04** | Moscow SERM org | ORG-0001 or ORG-0002 | **CLIENT_OF** / **PARTNER_OF** | Wave 6A deferred | — | **No** | **High** | **P3** | **Blocked** |
| **C-05** | Metallka org | ORG-0001 or ORG-0002 | **CLIENT_OF** / **PARTNER_OF** | Wave 6A deferred | — | **No** | **High** | **P3** | **Blocked** |

### 5.3 Coverage gain (attainable now)

| class | count |
|-------|-------|
| All entity classes | **0** |
| Relationships | **3** |
| Commercial class uplift | **14% → ~43%** |

### 5.4 Scoring

| criterion | rating | notes |
|-----------|--------|-------|
| Effort | **Low** | REL-0016 template per edge |
| Evidence readiness | **High** (C-01); **Medium** (C-02, C-03) | Lead with ZPM |
| Business value | **High** | Critical commercial gap |
| Priority | **P0** (lead); **P2** (follow-on) | Sequence per §6 |

---

## 6. Direction D — New contours register

### 6.1 Contour state register

| contour_id | display_name | person_attested | org_attested | le_attested | cc_slug | evidence_tier | slice_score |
|------------|--------------|-----------------|--------------|-------------|---------|---------------|-------------|
| **D-01** | Moscow SERM | PER-0002 **active** | **Absent** | **SAFE UNKNOWN** | `moscow-serm` | E0 | **0.5 / 7** |
| **D-02** | Metallka | PER-0003 **active** | **Absent** | **SAFE UNKNOWN** | `metallka` | E0 | **0.5 / 7** |

### 6.2 Coverage gain breakdown (both contours)

| class | count | notes |
|-------|-------|-------|
| Organization | 2 | Greenfield Category A waves |
| Legal Entity | 0–2 | Discovery required |
| Person | 0 | Already attested |
| Project | 0 | No candidates |
| Website | 0 | No candidates |
| Domain | 0 | No candidates |
| Relationships | 4–6 | Person→Org ×2; commercial ×2 |

### 6.3 Scoring

| criterion | rating | notes |
|-----------|--------|-------|
| Effort | **High** | Org discovery + LE unknown + commercial type review |
| Evidence readiness | **Low–Medium** | Person E0 only |
| Business value | **Medium** | Partner anchoring; no program consumer |
| Priority | **P3** | Evidence-gated |

---

## 7. Recommended execution order register

| seq | priority | direction | execution_unit | entity_classes_touched | prerequisite |
|-----|----------|-----------|----------------|------------------------|--------------|
| **1** | **P0** | **C** | C-01 ZPM CLIENT_OF | Commercial rel | None — stack complete |
| **2** | **P1** | **A** | SIBCAR Wave 3 Project | Project + rels | None |
| **3** | **P1** | **A** | SIBCAR Wave 4 Website | Website + rels | Seq 2 |
| **4** | **P1** | **A** | SIBCAR Wave 5 Domain | Domain | Seq 3 |
| **5** | **P2** | **B** | Makita Wave 4 Websites ×2 | Website ×2 + rels | None |
| **6** | **P2** | **B** | Makita Wave 5 Domains ×2 | Domain ×2 | Seq 5 |
| **7** | **P2** | **B** | Makita Person + Project | Person, Project + rels | Seq 5–6 |
| **8** | **P2** | **C** | C-03 Makita CLIENT_OF i-SEO | Commercial rel | Seq 5–7 |
| **9** | **P2** | **C** | C-02 SIBCAR CLIENT_OF | Commercial rel | Seq 2–4 |
| **10** | **P3** | **D** | Moscow SERM Organization wave | Org, LE?, Person edge | CC or E1 discovery |
| **11** | **P3** | **D** | Metallka Organization wave | Org, LE?, Person edge | CC or E1 discovery |

---

## 8. Comparative scoring matrix

| direction | coverage_gain | effort | evidence | business_value | coverage/effort_ratio | **final_priority** |
|-----------|---------------|--------|----------|----------------|----------------------|-------------------|
| **C** (lead C-01) | Medium *(class-critical)* | **Low** | **High** | **High** | **Best** | **P0** |
| **A** | **High** *(multi-class)* | Medium | **High** | **High** | **Strong** | **P1** |
| **B** | **High** *(volume)* | Medium–High | Medium | Medium–High | Moderate | **P2** |
| **D** | Medium *(org only)* | **High** | Low–Medium | Medium | **Weak** | **P3** |

---

## 9. Evidence index (decision references)

| ref | artifact | directions |
|-----|----------|------------|
| EV-W1C-CC-01 | `sibcar\Реквизиты.docx` | A, C-02 |
| EV-W1C-02/03 | OCPilot site-passport; project-access-brief | A |
| EV-W1B-CC-01 | `bzpm\Реквизиты.docx` | C-01 |
| EV-MAKITA-OP-01..03 | Steward operational inputs | B, C-03 |
| REL-0016 | Wave 6A attested CLIENT_OF | C *(precedent)* |
| SU-REL-04 | ZPM commercial deferral | C-01 |
| PER-0002/0003 | Wave 2 attestation | D |

---

## 10. Validation register

| check_id | criterion | result |
|----------|-----------|--------|
| VAL-01 | No entities created | **Pass** |
| VAL-02 | No relationships created | **Pass** |
| VAL-03 | No graph mutations | **Pass** |
| VAL-04 | No Foundation changes | **Pass** |
| VAL-05 | Directions A–D separate evaluation | **Pass** |
| VAL-06 | Single execution order | **Pass** — §7 |
| VAL-07 | Current Atlas state as authority | **Pass** |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md](ATLAS-NEXT-EXPANSION-DECISION-AUDIT-v1.md) | Full decision audit |
| [ATLAS-NEXT-EXPANSION-DECISION-SUMMARY-v1.md](ATLAS-NEXT-EXPANSION-DECISION-SUMMARY-v1.md) | Executive summary |
| [ATLAS-COVERAGE-AUDIT-REGISTER-v1.md](ATLAS-COVERAGE-AUDIT-REGISTER-v1.md) | Missing inventory source |

---

*ATLAS Next Expansion Decision Register v1 — audit only; no commit.*
