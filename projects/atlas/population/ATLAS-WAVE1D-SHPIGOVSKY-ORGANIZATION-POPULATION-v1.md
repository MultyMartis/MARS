# ATLAS Wave 1D Shpigovsky Organization Population v1

**Status:** **documented** — Wave 1D canonical Organization population for ООО «Сознание» / Shpigovsky (normative for operators).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Parent:** [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) · [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) · [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Companion:** [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md)  
**Supersedes (population posture):** [ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md](ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md) · [ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md](ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md) — «INTAKE ONLY / AWAITING CC» hold lifted for Organization layer.  
**Is not:** runtime, API, automation, database schema, Legal Entity population, relationship creation.

**Wave 1 prerequisite:** Organizations ORG-0001..0007 — **unchanged** (operator-confirmed).

**Wave 1D intent:**

Perform **Operational Organization Evidence Path (OOEP)** intake for **ООО «Сознание»** as a **Category A** Polygon client Organization — Organization **active** at **E1/E2 operational-public** tier; Legal Entity **deferred**; Counterparty Card **not required** for Organization layer per approved OOEP Category A extension.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Organization** для Wave 1D tranche **Shpigovsky (ООО «Сознание»)**: identity, operational-public evidence, brand/organization separation, duplicate review, attestation, и explicit deferrals (Legal Entity, Person, Website, Domain, Project, Relationship).

**Normative scope Wave 1D:**

```text
Organization entity population + attestation (single org: ООО «Сознание»)
Legal Entity population — DEFERRED (SAFE UNKNOWN)
Wave 2 (future): Person ↔ Organization — only after explicit Person wave decision
Wave 3+ (future): Project — only after commercial evidence
Wave 4 / 5 (future): Website / Domain — candidate assets listed; no mint
Wave 6+ (future): CLIENT_OF edges — only after commercial review
```

**Binding evidence context:**

- **EV-SHPIG-OP-01** — operator intake statements (2026-06-10) — **E0**.
- **EV-SHPIG-WEB-01** — live public capture `https://shpigovsky.ru/` (2026-06-10) — **E2**.
- **EV-SHPIG-WEB-02** — live public capture `https://shpigovsky.ru/policy` (2026-06-10) — **E2**.
- **ORG-0008** — canonical Organization id (next after ORG-0007 Makita Snab).
- **No CC** — `shpigovsky\` folder absent — Category A operational-public path authorized per [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) (Polygon client; E1/E2 public evidence sufficient; LE deferred).

---

## 2. Population roster (canonical)

Источник: operational evidence EV-SHPIG-OP-01; public website evidence EV-SHPIG-WEB-01..02; duplicate review vs attested Wave 1 orgs ORG-0001..0007.  
**Не** в [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) — Wave 1D post-dataset expansion tranche.

### 2.1 Summary table

| org_id | canonical_name | wave_tier | classification | legal_entity_id | lifecycle (target) | evidence_tier | attestation readiness |
|--------|----------------|-----------|----------------|-----------------|-------------------|---------------|----------------------|
| ORG-0008 | ООО «Сознание» | **W1-D** | **Polygon client** | **SAFE UNKNOWN** | **active** | **E1/E2** *(operational-public)* | **ready** |

**Wave tier:** W1-D — Category A Polygon client; Operational Organization Evidence Path with public website corroboration.

---

## 3. Organization identity analysis

### 3.1 ORG-0008 — ООО «Сознание»

| Field | Value |
|-------|-------|
| **org_id** | ORG-0008 |
| **canonical_name** | **ООО «Сознание»** |
| **lifecycle_state** | **active** |
| **wave_tier** | W1-D |
| **classification** | **Polygon client** |
| **business_role** | **CLIENT** — operational counterparty (Polygon delivery context) |
| **legal_entity_id** | **SAFE UNKNOWN** — LE-* not created |
| **primary_contact_person_id** | **SAFE UNKNOWN** — PER-* not minted |
| **primary_website (display candidate)** | **SAFE UNKNOWN** — candidate: `shpigovsky.ru` |
| **primary_domain (display candidate)** | **SAFE UNKNOWN** — candidate: `shpigovsky.ru` |
| **edo_enabled** | **SAFE UNKNOWN** |
| **brand_notes** | **Шпиговский Дом** = brand; **ООО «Сознание»** = organization — **no** separate Organization for brand |
| **notes** | Category A Polygon; Website Factory ecosystem; WordPress delivery; i-SEO project channel **excluded** |

### 3.2 Required SAFE UNKNOWN fields (Legal Entity layer)

| Field | Value |
|-------|-------|
| Legal entity | **SAFE UNKNOWN** |
| INN | **SAFE UNKNOWN** |
| KPP | **SAFE UNKNOWN** |
| OGRN | **SAFE UNKNOWN** |
| Legal signatory | **SAFE UNKNOWN** |
| EDO | **SAFE UNKNOWN** |
| Ownership structure | **SAFE UNKNOWN** |
| Contract data | **SAFE UNKNOWN** |
| Internal contacts | **SAFE UNKNOWN** |

### 3.3 Brand vs organization separation

| Signal | Resolution | Evidence |
|--------|------------|----------|
| **Шпиговский Дом** | **Brand** — display/trade positioning on website | EV-SHPIG-WEB-01 |
| **ООО «Сознание»** | **Organization** — canonical_name for ORG-0008 | EV-SHPIG-WEB-02 |
| Separate org for brand | **Prohibited** | Steward policy — brand notes only |
| «Центр профилактики зависимостей Сергея Шпиговского» | **Brand positioning** — not attested alias | EV-SHPIG-WEB-01 |

**Alias policy (EFV-01):** Trade names on website recorded as **brand_notes** only — **not** attested Organization aliases without CC.

### 3.4 Operational context signals *(informational — no REL-* mint)*

| Signal | Value | Evidence |
|--------|-------|----------|
| Acquisition | **Ольга Дягилева** (PER-0010 — attested reference only) | EV-SHPIG-OP-01 |
| Client comms / coordination / SEO supervision / acceptance | **Ольга Дягилева** | EV-SHPIG-OP-01 |
| Technical delivery | **Operator** (steward) — frontend, WordPress | EV-SHPIG-OP-01 |
| Delivery org *(reference)* | **ORG-0001** Полигон | EV-SHPIG-OP-01 |
| i-SEO project channel | **Excluded** | EV-SHPIG-OP-01 |
| Ecosystem | Website Factory; MARS; WordPress; possible ACF | EV-SHPIG-OP-01 |

### 3.5 Identity disambiguation (evidence-only)

| Signal | Resolution | Evidence |
|--------|------------|----------|
| **ООО «Сознание»** vs **ORG-0001..0007** | **Distinct** | SHPIG-D-01..07; no identifier collision |
| **shpigovsky.ru** vs existing WEB-* hosts | **No collision** | SHPIG-D-08 |
| **Шпиговский Дом** vs org identity | **Brand subordinate to ORG-0008** | Brand notes policy |
| Repository prior references | **Net-new** | Intake §9.4 — zero prior Atlas population |

---

## 4. Legal entity analysis — DEFERRED

| Check | Result |
|-------|--------|
| CC present | **No** — `shpigovsky\` folder absent |
| LE-* creation | **Prohibited** — STOP-OOER-02; Organization-only wave |
| Legal entity **active** path | **Blocked** until E1+ CC or E2 registry extract with identifiers |
| Organization **active** at E1/E2 operational-public | **Authorized** — layer separation per OOEP Category A extension |
| E2 legal-name signal | **ООО "Сознание"** on privacy policy — supports Organization canonical_name; **does not** authorize LE-* mint without INN/OGRN |

**Gap register (Legal Entity — non-blocking for Organization active):**

| Gap ID | Topic | Severity |
|--------|-------|----------|
| **ME-W1D-SHPIG-01** | Legal entity form confirmation beyond E2 signal | **Deferred** |
| **ME-W1D-SHPIG-02** | INN / KPP / OGRN | **Deferred** |
| **ME-W1D-SHPIG-03** | Legal vs trade name mapping (Сознание ↔ Шпиговский Дом) | **Deferred** |
| **ME-W1D-SHPIG-04** | CC folder absent | **Expected** — operational-public path |
| **ME-W1D-SHPIG-05** | Contract data | **Deferred** |
| **ME-W1D-SHPIG-06** | Ownership structure | **Deferred** |

---

## 5. Evidence basis

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-SHPIG-OP-01** | Operator intake statements (2026-06-10) | **E0** | Polygon channel, acquisition path, role split, stack, i-SEO exclusion |
| **EV-SHPIG-WEB-01** | Live capture `https://shpigovsky.ru/` | **E2** | Brand, services, contacts, footer legal-name signal |
| **EV-SHPIG-WEB-02** | Live capture `https://shpigovsky.ru/policy` | **E2** | Privacy policy operator **ООО "Сознание"** |
| OOEP | [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | governance | Category A operational-public path |

**Population evidence tier:** **E1/E2 operational-public** — E0 operator delivery context + E2 public website legal-operator corroboration.

**Operational signals satisfied (≥2 required):**

1. Active work — Polygon delivery; WordPress technical execution *(EV-SHPIG-OP-01)*  
2. Known website — `https://shpigovsky.ru/` *(EV-SHPIG-OP-01, EV-SHPIG-WEB-01)*  
3. Confirmed business relationship — Polygon client delivery; not i-SEO project *(EV-SHPIG-OP-01)*  
4. Public legal-operator signal — **ООО "Сознание"** on policy page *(EV-SHPIG-WEB-02)*  
5. Acquisition / coordination path — Olga Dyagileva → Polygon channel *(EV-SHPIG-OP-01)*  

---

## 6. Service context *(informational — no REL-* mint)*

| Service | Provider / actor | Scope | Atlas edge |
|---------|----------------|-------|------------|
| **Website delivery** | ORG-0001 Полигон *(reference)* | WordPress; possible ACF; custom code | **None** — deferred Wave 3B |
| **SEO supervision** | PER-0010 Ольга Дягилева *(reference)* | Oversight on delivery — not i-SEO vendor channel | **None** |
| **Technical execution** | Operator (steward) | Frontend; WordPress; technical delivery | **None** |

**Operational boundaries:**

| In scope (documented) | Out of scope (deferred) |
|-----------------------|-------------------------|
| Polygon client delivery channel | Commercial CLIENT_OF edge |
| Public website identity signal | Contract / accounting data |
| Website Factory ecosystem posture | LE-* population |
| Brand notes (Шпиговский Дом) | PER-* mint from website staff |

---

## 7. Duplicate review

| Review ID | Pair | Verdict | Basis |
|-----------|------|---------|-------|
| **W1D-SHPIG-D-01** | Shpigovsky vs ORG-0001 Полигон | **Distinct — Pass** | Vendor ≠ client subject |
| **W1D-SHPIG-D-02** | Shpigovsky vs ORG-0002 MetaCode | **Distinct — Pass** | No overlap |
| **W1D-SHPIG-D-03** | Shpigovsky vs ORG-0003 i-SEO | **Distinct — Pass** | Channel excluded |
| **W1D-SHPIG-D-04** | Shpigovsky vs ORG-0004 Триумф | **Distinct — Pass** | No overlap |
| **W1D-SHPIG-D-05** | Shpigovsky vs ORG-0005 ЗПМ | **Distinct — Pass** | No overlap |
| **W1D-SHPIG-D-06** | Shpigovsky vs ORG-0006 SIBCAR | **Distinct — Pass** | No overlap |
| **W1D-SHPIG-D-07** | Shpigovsky vs ORG-0007 Макита Снаб | **Distinct — Pass** | No overlap |
| **W1D-SHPIG-D-08** | `shpigovsky.ru` vs existing WEB-* | **No collision — Pass** | SHPIG-D-08 |
| **W1D-SHPIG-D-09** | INN/OGRN legal-identity close | **Open — expected** | CC absent — LE deferred |

**Explicit validations (mission-required):**

| Claim | Verdict | Evidence |
|-------|---------|----------|
| ORG-0001..0007 unchanged | **Confirmed** | No merge; no modification in this package |
| Makita (ORG-0007) intact | **Confirmed** | W1D-SHPIG-D-07 |
| ZPM (ORG-0005) intact | **Confirmed** | W1D-SHPIG-D-05 |
| SIBCAR (ORG-0006) intact | **Confirmed** | W1D-SHPIG-D-06 |
| No merge operations | **Confirmed** | Duplicate review |
| No LE creation | **Confirmed** | §4 |
| No relationships | **Confirmed** | §6 |
| No projects | **Confirmed** | §9 |
| No graph redesign | **Confirmed** | Organization-only tranche |
| No Foundation changes | **Confirmed** | §8 |

---

## 8. Steward checklist (population)

| ID | Check | Result |
|----|-------|--------|
| W1D-SHPIG-S-01 | Category A classification (Polygon client) | **Pass** |
| W1D-SHPIG-S-02 | OOEP operational-public signals ≥2 | **Pass** |
| W1D-SHPIG-S-03 | EFV rules applied — no project merge | **Pass** |
| W1D-SHPIG-S-04 | Legal entity fields **SAFE UNKNOWN** | **Pass** |
| W1D-SHPIG-S-05 | Duplicate batch W1D-SHPIG-D-01..09 | **Pass** |
| W1D-SHPIG-S-06 | ORG-0008 identifier slot | **Pass** — next after ORG-0007 |
| W1D-SHPIG-S-07 | No LE-* / PER-* / WEB-* / DOM-* / PRJ-* / REL-* mint | **Pass** |
| W1D-SHPIG-S-08 | No Foundation modification | **Pass** |
| W1D-SHPIG-S-09 | Brand/org separation — no second Organization for Шпиговский Дом | **Pass** |
| W1D-SHPIG-S-10 | Prior intake-only hold superseded for Organization layer | **Pass** |
| W1D-SHPIG-S-11 | i-SEO project channel excluded | **Pass** |

---

## 9. Candidate assets only — no mint

### 9.1 Website candidates

| Candidate | URL | web_id | Status |
|-----------|-----|--------|--------|
| shpigovsky.ru (homepage) | https://shpigovsky.ru/ | **none** | Wave 4 candidate — EV-SHPIG-WEB-01 |
| shpigovsky.ru (policy) | https://shpigovsky.ru/policy | **none** | Wave 4 candidate — EV-SHPIG-WEB-02 |
| shpigovsky.ru (psy) | https://shpigovsky.ru/psy | **none** | Wave 4 candidate — EV-SHPIG-WEB-01 |
| shpigovsky.ru (home) | https://shpigovsky.ru/home | **none** | Wave 4 candidate — EV-SHPIG-WEB-01 |

**Do not mint WEB entities.**

### 9.2 Domain candidates

| Candidate | FQDN | dom_id | Status |
|-----------|------|--------|--------|
| shpigovsky.ru | shpigovsky.ru | **none** | Wave 5 candidate |

**Do not mint DOM entities.**

### 9.3 Deferred entity classes

| Class | Status |
|-------|--------|
| LE-* | **Not created** — SAFE UNKNOWN until E1+ CC |
| PER-* | **Not created** — PER-0010 referenced only; website staff not minted |
| PRJ-* | **Not created** — future Wave 3 |
| REL-* | **Not created** — future Wave 6+ |

---

## 10. Attestation readiness

| Dimension | Assessment |
|-----------|------------|
| Operational-public evidence | **Complete** — EV-SHPIG-OP-01; EV-SHPIG-WEB-01..02 |
| OOEP gates | **Pass** |
| Duplicate review | **Pass** |
| Organization **active** | **Ready** — see attestation package |
| Legal Entity | **Deferred** — SAFE UNKNOWN |
| Wave 2 Person | **Not in scope** |
| Wave 3 Project | **Deferred** |
| Wave 4 / 5 Website / Domain | **Deferred** — candidates only |

See [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md).

---

## 11. Package lineage

```text
Wave 1 (ORG-0001..0004) ──COMPLETE──► Wave 1 Attestation ──COMPLETE
        │
        ▼
Wave 1B ЗПМ (ORG-0005 active) ──► Wave 1C SIBCAR (ORG-0006 active)
        │
        ▼
Wave 1D Makita (ORG-0007 active)
        │
        ▼
Shpigovsky Intake (INTAKE ONLY) ──► superseded for Organization layer
        │
        ▼
Wave 1D Shpigovsky Organization Population (THIS PACKAGE) ──► ORG-0008 active
        │
        ▼
Future: CC arrival ──► Legal Entity wave (LE-* TBD)
Future: Wave 2 Person / Wave 3 Project / Wave 4–6 assets & edges
```

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md) | Canonical register row |
| [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-ATTESTATION-v1.md) | Attestation sequence and verdict |
| [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | Category A operational-public path |
| [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) | Prior intake evidence source |

---

*ATLAS Wave 1D Shpigovsky Organization Population v1 — documentation only.*
