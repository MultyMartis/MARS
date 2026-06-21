# ATLAS Coverage Audit Register v1

**Status:** **documented** — tabular coverage audit register (audit only).  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Parent:** [ATLAS-COVERAGE-AUDIT-v1.md](ATLAS-COVERAGE-AUDIT-v1.md) · [ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md](ATLAS-COVERAGE-AUDIT-SUMMARY-v1.md)  
**Is not:** population register, attested export, runtime registry, git commit.

---

## 1. Register summary

| Metric | Value |
|--------|-------|
| Business subjects in scope | **10** |
| Entity classes reviewed | **7** |
| Attested Organizations (current) | **7** (ORG-0001..0007) |
| Attested Legal Entities | **5** (LE-0001..0005) |
| Attested Persons | **15** (PER-0001..0015) |
| Attested Projects | **8** (PRJ-0001, 0004..0010) |
| Attested Websites | **5** (WEB-0006..0009, WEB-ZPM-01) |
| Attested Domains | **5** (DOM-0001..0004, DOM-ZPM-01) |
| Attested commercial org↔org edges | **1** (REL-0016) |
| **Aggregate coverage (Method A)** | **~55%** |
| **Slice slot coverage (Method B)** | **~40%** |
| Missing entity references inventoried | **§3** — **35 rows** |
| Missing relationship candidates | **§4** — **18 rows** |
| Priority queue items | **P0: 4 · P1: 5 · P2: 5** |

---

## 2. Coverage matrix register

**Codes:** **F** = fully represented · **P** = partially represented · **I** = intake only · **A** = absent

### 2.1 Master matrix

| subject_id | subject_name | org | le | person | project | website | domain | commercial | slice_verdict | slice_score |
|------------|--------------|-----|----|----|---------|---------|--------|------------|---------------|-------------|
| SUB-01 | Polygon | F | F | F | P | A | A | P | **Partial** | 4.0/7 |
| SUB-02 | MetaCode | F | P | P | P | A | A | A | **Partial** | 2.5/7 |
| SUB-03 | i-SEO | F | F | F | A | A | A | A | **Partial** | 3.0/7 |
| SUB-04 | Triumph | F | F | F | F | F | F | F | **Full** | 7.0/7 |
| SUB-05 | ЗПМ (ZPM) | F | F | F | F | F | P | P | **Partial** | 6.0/7 |
| SUB-06 | SIBCAR | F | F | A | A | A | A | A | **Partial** | 2.0/7 |
| SUB-07 | Makita Snab | P | A | A | A | A | A | A | **Partial** | 0.5/7 |
| SUB-08 | Dyakonov | I | I | I | A | A | A | A | **Intake only** | 1.75/7 |
| SUB-09 | Moscow SERM | A | A | P | A | A | A | A | **Partial** | 0.5/7 |
| SUB-10 | Metallka | A | A | P | A | A | A | A | **Partial** | 0.5/7 |

### 2.2 Attested entity bindings (where present)

| subject_id | org_id | le_id | person_ids | project_ids | website_ids | domain_ids | commercial_rel |
|------------|--------|-------|------------|-------------|-------------|------------|----------------|
| SUB-01 | ORG-0001 | LE-0001 | PER-0001 | PRJ-0004..0010 *(EXECUTES)* | — | — | REL-0016 *(inbound vendor)* |
| SUB-02 | ORG-0002 | LE-0001 *(shared)* | PER-0001 | PRJ-0001 *(display)* | — | — | — |
| SUB-03 | ORG-0003 | LE-0002 | PER-0007..0013 | — | — | — | — |
| SUB-04 | ORG-0004 | LE-0003 | PER-0004..0006 | PRJ-0004..0008 | WEB-0006..0009 | DOM-0001..0004 | REL-0016 |
| SUB-05 | ORG-0005 | LE-0004 | PER-0014..0015 | PRJ-0009..0010 | WEB-ZPM-01 | DOM-ZPM-01 | — *(SU-REL-04 deferred)* |
| SUB-06 | ORG-0006 | LE-0005 | — | — | — | — | — *(SU-REL-06 deferred)* |
| SUB-07 | ORG-0007 | — | — *(Артём signal)* | — | — | — | — |
| SUB-08 | — | — | — | — | — | — | — |
| SUB-09 | — | — | PER-0002 | — | — | — | — |
| SUB-10 | — | — | PER-0003 | — | — | — | — |

---

## 3. Missing entities inventory register

### 3.1 Organizations

| miss_id | reference_label | display_name | cc_slug | evidence_tier | intake_ref | blocking_factor | priority |
|---------|-----------------|--------------|---------|---------------|------------|-----------------|----------|
| MISS-O-01 | Moscow SERM contour | Moscow SERM | `moscow-serm` | E0 | PER-0002 | Category A — org wave not executed | **P0** |
| MISS-O-02 | Metallka contour | Metallka | `metallka` | E0 | PER-0003 | Category A — org wave not executed | **P0** |
| MISS-O-03 | DYAKONOV-INTAKE-CAND-O01 | ИП Дьяконов | `dyakonov` | E0 | Dyakonov intake | CC absent | **P1** |

### 3.2 Legal entities

| miss_id | reference_label | bound_contour | le_id_candidate | evidence_tier | blocking_factor | priority |
|---------|-----------------|---------------|-----------------|---------------|-----------------|----------|
| MISS-LE-01 | Makita legal subject | ORG-0007 | LE-0006 *(candidate)* | — | Category B — E1+ required | **P2** |
| MISS-LE-02 | DYAKONOV-INTAKE-CAND-LE01 | Dyakonov | — | E0 | CC absent | **P1** |
| MISS-LE-03 | Moscow SERM LE | Moscow SERM | — | **SAFE UNKNOWN** | Org not populated | **P0** |
| MISS-LE-04 | Metallka LE | Metallka | — | **SAFE UNKNOWN** | Org not populated | **P0** |

### 3.3 Persons

| miss_id | reference_label | display_signal | contour | person_id_candidate | blocking_factor | priority |
|---------|-----------------|----------------|---------|---------------------|-----------------|----------|
| MISS-P-01 | Makita contact | Артём *(given name)* | ORG-0007 | — | Full name **SAFE UNKNOWN** | **P1** |
| MISS-P-02 | DYAKONOV-INTAKE-CAND-P01 | Дьяконов *(surname)* | Dyakonov | — | CC absent | **P1** |
| MISS-P-03 | Moscow SERM staff | Beyond PER-0002 | Moscow SERM | — | Org not populated | **P2** |
| MISS-P-04 | Metallka staff | Beyond PER-0003 | Metallka | — | Org not populated | **P2** |

### 3.4 Projects

| miss_id | reference_label | contour | evidence_ref | prj_id | blocking_factor | priority |
|---------|-----------------|---------|--------------|--------|-----------------|----------|
| MISS-PRJ-01 | SIBCAR OCPilot engagement | ORG-0006 · SITE-001 | EV-W1C-01; site-passport | — | Wave 3 not executed | **P0** |
| MISS-PRJ-02 | Makita SEO dual-site | ORG-0007 | EV-MAKITA-OP-01..03 | — | Org-only Wave 1D | **P1** |
| MISS-PRJ-03 | PRJ-0002 | Wave 1 dataset | No evidence | PRJ-0002 | Explicitly excluded | — |
| MISS-PRJ-04 | PRJ-0003 | Wave 1 dataset | No evidence | PRJ-0003 | Explicitly excluded | — |

### 3.5 Websites

| miss_id | reference_label | url | contour | web_id_reserved | status | priority |
|---------|-----------------|-----|---------|-----------------|--------|----------|
| MISS-WEB-01 | polygon-ws.ru | `https://polygon-ws.ru` | Polygon | WEB-0001 | **Deferred** | **P1** |
| MISS-WEB-02 | polygon-ws.com | `https://polygon-ws.com` | Polygon | WEB-0002 | **Deferred** | **P1** |
| MISS-WEB-03 | metacode-agency.com | `https://metacode-agency.com` | MetaCode | WEB-0003 | **Deferred** | **P1** |
| MISS-WEB-04 | metacode-agency.ru | `https://metacode-agency.ru` | MetaCode | WEB-0004 | **Deferred** | **P1** |
| MISS-WEB-05 | i-seo.su | `https://i-seo.su` | i-SEO | WEB-0005 | **Deferred** | **P1** |
| MISS-WEB-06 | makita-snab.ru | `https://makita-snab.ru` | Makita | — | **Candidate** | **P1** |
| MISS-WEB-07 | makita-land.ru | `https://makita-land.ru` | Makita | — | **Candidate** | **P1** |
| MISS-WEB-08 | sibcar.new-site.space | `https://sibcar.new-site.space` | SIBCAR | — | **Candidate** | **P0** |

### 3.6 Domains

| miss_id | fqdn | contour | dom_id_reserved | status | priority |
|---------|------|---------|-----------------|--------|----------|
| MISS-DOM-01 | polygon-ws.ru | Polygon | — | **Deferred** | **P1** |
| MISS-DOM-02 | polygon-ws.com | Polygon | — | **Deferred** | **P1** |
| MISS-DOM-03 | metacode-agency.com | MetaCode | — | **Deferred** | **P1** |
| MISS-DOM-04 | metacode-agency.ru | MetaCode | — | **Deferred** | **P1** |
| MISS-DOM-05 | i-seo.su | i-SEO | — | **Deferred** | **P1** |
| MISS-DOM-06 | makita-snab.ru | Makita | — | **Candidate** | **P1** |
| MISS-DOM-07 | makita-land.ru | Makita | — | **Candidate** | **P1** |
| MISS-DOM-08 | sibcar.new-site.space | SIBCAR | — | **Candidate** | **P0** |

---

## 4. Missing relationship inventory register

### 4.1 Commercial (Organization ↔ Organization)

| miss_rel_id | source | target | type | documented_in | attested | priority |
|-------------|--------|--------|------|---------------|----------|----------|
| MREL-C-01 | ORG-0004 Триумф | ORG-0001 Полигон | **CLIENT_OF** | Wave 6A | **Yes** — REL-0016 | — |
| MREL-C-02 | ORG-0005 ЗПМ | ORG-0001 Полигон | **CLIENT_OF** | SU-REL-04 | **No** | **P0** |
| MREL-C-03 | ORG-0006 SIBCAR | ORG-0001 Полигон | **CLIENT_OF** | SIBCAR register §5 | **No** | **P1** |
| MREL-C-04 | ORG-0007 Makita | ORG-0003 i-SEO | **CLIENT_OF** | Makita register §6 | **No** | **P1** |
| MREL-C-05 | Moscow SERM org | ORG-0001 or ORG-0002 | **CLIENT_OF** / **PARTNER_OF** | Wave 6A deferred | **No** | **P0** |
| MREL-C-06 | Metallka org | ORG-0001 or ORG-0002 | **CLIENT_OF** / **PARTNER_OF** | Wave 6A deferred | **No** | **P0** |

### 4.2 Person ↔ Organization

| miss_rel_id | source | target | type | blocker | priority |
|-------------|--------|--------|------|---------|----------|
| MREL-P-01 | PER-0002 | Moscow SERM org | TBD | Org not populated | **P0** |
| MREL-P-02 | PER-0003 | Metallka org | TBD | Org not populated | **P0** |
| MREL-P-03 | Артём (unminted) | ORG-0007 | REPRESENTATIVE | Person not minted | **P1** |
| MREL-P-04 | Dyakonov (unminted) | ORG-0001 | **CONTRACTOR** | CC absent | **P1** |
| MREL-P-05 | PER-0001 | ORG-0003 | MANAGER | Rejected REL-0003 | **P2** |

### 4.3 Domain / Website family

| miss_rel_id | source | target | type | scope | priority |
|-------------|--------|--------|------|-------|----------|
| MREL-D-01 | DOM-ZPM-01 | WEB-ZPM-01 | **PRIMARY_DOMAIN** | Wave 5B ZPM deferred | **P2** |
| MREL-D-02 | ORG-0004 | DOM-0001..0004 | **OWNS** | Registrant SAFE UNKNOWN | **P2** |
| MREL-D-03 | ORG-0005 | DOM-ZPM-01 | **OWNS** | ME-W5-ZPM-01 | **P2** |
| MREL-D-04 | ORG-0001 | WEB-0006..0009 | **OPERATES** | SU-WEB-01 | **P2** |
| MREL-D-05 | WEB-0006 | PRJ-0006 | **BELONGS_TO** | Wave 4B review | **P2** |

### 4.4 Person ↔ Project

| miss_rel_id | scope | documented_in | priority |
|-------------|-------|---------------|----------|
| MREL-PP-01 | PER-* ↔ PRJ-* participation | Wave 3 register §4; SU-REL-10 | **P2** |

---

## 5. Entity-class coverage register

| class | known_count | attested_count | ratio | verdict |
|-------|-------------|----------------|-------|---------|
| Organization | 10 | 7 | **70%** | Partial |
| Legal Entity | 9 | 5 | **56%** | Partial |
| Person | 17 | 15 | **88%** | Strong |
| Project | 10 | 8 | **80%** | Partial |
| Website | 14 | 5 | **36%** | Weak |
| Domain | 14 | 5 | **36%** | Weak |
| Commercial relationship | 7 | 1 | **14%** | Critical gap |
| **Mean** | — | — | **~55%** | **Partial** |

**Known count methodology:** documented references with current-reality evidence; excludes ZPM FUT-01..04 held future candidates and PRJ-0002/0003 no-evidence placeholders.

---

## 6. Priority queue register

### 6.1 P0

| queue_id | target | entity_classes | business_rationale |
|----------|--------|----------------|-------------------|
| PQ-P0-01 | Moscow SERM Organization population | Org, LE, Person edge | Partner isolation; Category A; PER-0002 blocked |
| PQ-P0-02 | Metallka Organization population | Org, LE, Person edge | Partner isolation; Category A; PER-0003 blocked |
| PQ-P0-03 | REL ORG-0005 CLIENT_OF ORG-0001 | Commercial | Full ZPM stack minus commercial edge |
| PQ-P0-04 | SIBCAR Project + Website (OCPilot) | Project, Website | Active engagement; org-only insufficient |

### 6.2 P1

| queue_id | target | entity_classes | business_rationale |
|----------|--------|----------------|-------------------|
| PQ-P1-01 | Makita Websites ×2 + Domains ×2 | Website, Domain | ORG-0007 operational; dual-site SEO reality |
| PQ-P1-02 | Makita Person (Артём) + i-SEO CLIENT_OF | Person, Commercial | Contact signal exists; channel closure |
| PQ-P1-03 | Dyakonov CC → Org + LE + Person + CONTRACTOR | Org, LE, Person, Rel | Polygon contractor; Category A |
| PQ-P1-04 | SIBCAR CLIENT_OF ORG-0001 | Commercial | W1-C client parity |
| PQ-P1-05 | Operator WEB-0001..0005 | Website, Domain | Operator web identity gap |

### 6.3 P2

| queue_id | target | entity_classes | business_rationale |
|----------|--------|----------------|-------------------|
| PQ-P2-01 | ZPM Wave 5B PRIMARY_DOMAIN | Relationship | DOM-ZPM-01 minted; edge deferred |
| PQ-P2-02 | Makita LE when E1+ appears | Legal Entity | Category B — not blocking org |
| PQ-P2-03 | PRJ-0001 COMMISSIONED_BY | Project rel | Internal MARS; Low severity |
| PQ-P2-04 | Person ↔ Project edges | Relationship | SU-REL-10 enrichment |
| PQ-P2-05 | MetaCode commercial edges | Commercial | No approved Wave 6A candidate |

---

## 7. Expansion risk register

| risk_id | area | severity | low_value_signal | recommended_posture |
|---------|------|----------|------------------|---------------------|
| EXP-COV-01 | Register sync without population | Medium | Doc inflation (ZPM-C pattern) | Couple sync to population waves |
| EXP-COV-02 | Full Person contact register | Low | PER-* contact rows before need | Maintenance-triggered only |
| EXP-COV-03 | ZPM future projects FUT-01..04 | Medium | Projects without start evidence | Hold per intake summary |
| EXP-COV-04 | MARS program registry → PRJ-* | High | E-17 boundary violation | Exclude per Wave 3 §5 |
| EXP-COV-05 | ORCA Makita pilot → Atlas org evidence | Medium | W1D-D-07 exclusion breach | Keep pilot boundary |
| EXP-COV-06 | Patronymic SAFE UNKNOWN bulk close | Low | SU-PER-04 cosmetic | Defer |
| EXP-COV-07 | MetaCode standalone LE split | Low | No CC driver for split | Document share only |
| EXP-COV-08 | Indiscriminate i-SEO Category B intake | Medium | Registry noise | OOEP gate per Makita |
| EXP-COV-09 | Inverse VENDOR_OF mirrors | Low | Wave 6A rejected pattern | Do not mint |
| EXP-COV-10 | Domain OWINS without registrar E1 | Medium | SU-DOM false precision | Wait for E1 |

---

## 8. Source register index

| Register | Path | Audit role |
|----------|------|------------|
| Backup snapshot | [ATLAS-BACKUP-SNAPSHOT-v1.md](../population/ATLAS-BACKUP-SNAPSHOT-v1.md) | Entity baseline |
| Integrity snapshot | [ATLAS-INTEGRITY-SNAPSHOT-REGISTER-v1.md](ATLAS-INTEGRITY-SNAPSHOT-REGISTER-v1.md) | SAFE UNKNOWN + deferred |
| Wave 1D Makita Org | [ATLAS-WAVE1D-MAKITA-ORGANIZATION-REGISTER-v1.md](../population/ATLAS-WAVE1D-MAKITA-ORGANIZATION-REGISTER-v1.md) | ORG-0007 |
| Wave 1C SIBCAR Org | [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | ORG-0006 |
| Wave 2 attestation | [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](../population/ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | PER-0002, 0003 isolation |
| Wave 4 Website | [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](../population/ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | WEB deferred queue |
| Wave 6A Commercial | [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](../population/ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Commercial deferred |
| Makita intake | [ATLAS-MAKITA-INTAKE-REGISTER-v1.md](../population/ATLAS-MAKITA-INTAKE-REGISTER-v1.md) | Pre-W1D candidates |
| Dyakonov intake | [ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md](../population/ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md) | Contractor intake |
| OOEP | [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](../population/ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | Category A/B channels |

---

*ATLAS Coverage Audit Register v1 — audit only.*
