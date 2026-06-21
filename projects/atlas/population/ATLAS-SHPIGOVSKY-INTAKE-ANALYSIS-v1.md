# ATLAS Shpigovsky Project Intake Analysis v1

**Status:** **documented** — Polygon client project intake analysis only (no population, no attestation).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Intake slug:** `shpigovsky`  
**Parent:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) · [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](../foundation/ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) · [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md)  
**Is not:** Organization population, Person population, Legal Entity minting, Project population, relationship creation, Website attestation, Domain population, `ORG-*` / `LE-*` / `PER-*` / `PRJ-*` / `WEB-*` / `DOM-*` / `REL-*` minting.

**Governance applied:** EFV-01..06 · CPV-01..05.

**Explicit exclusions (this package):**

- No `ORG-*` identifier assigned
- No `LE-*` identifier assigned
- No `PER-*` identifier assigned *(existing PER-0010 referenced only)*
- No `PRJ-*` identifier assigned
- No `WEB-*` or `DOM-*` identifiers assigned
- No Relationship edges (including CLIENT_OF, EXECUTES, EMPLOYEE extension)
- No attestation or population proposal

---

## 1. Operational context

**Delivery organization (attested anchor — reference only):** **ORG-0001** Веб-студия «Полигон».

**Channel classification:** **Polygon client delivery** — **not** an i-SEO project channel per operator statement.

| Role | Actor | Scope in this intake |
|------|-------|----------------------|
| Client acquisition | **Ольга Дягилева** *(PER-0010 — attested elsewhere)* | Brought client to Polygon |
| Client communications | **Ольга Дягилева** | Primary client-facing coordination |
| Project coordination | **Ольга Дягилева** | Delivery coordination |
| SEO supervision | **Ольга Дягилева** | SEO oversight on delivery *(not i-SEO vendor channel)* |
| Primary acceptance | **Ольга Дягилева** | First-pass acceptance of work |
| Frontend development | **Operator** *(steward intake)* | Technical execution |
| WordPress implementation | **Operator** | Technical execution |
| Technical delivery | **Operator** | End-to-end technical delivery |

**Planned ecosystem involvement *(operator — future consumer posture, not runtime proof)*:**

| System | Role signal |
|--------|-------------|
| **MARS** | Program / operational context |
| **Website Factory** | Site production workflow |
| **WordPress delivery** | Primary delivery stack |
| **ACF** | Possible implementation layer |
| **Custom programming** | Possible scope extension |
| **WP automation agents** | Possible future automation |

**Evidence:** **EV-SHPIG-OP-01** (operator intake statements, 2026-06-10).

**Boundary:** PER-0010 is **EMPLOYEE** of ORG-0003 i-SEO in attested graph (REL-0009) — this intake records **operational role on Polygon delivery** only; **no** new edges, **no** i-SEO project classification.

---

## 2. Delivery context

| Field | Value | Evidence |
|-------|-------|----------|
| Delivery org | **ORG-0001** Полигон | EV-SHPIG-OP-01 |
| Project class *(target)* | **client_delivery** | EV-SHPIG-OP-01; analog ZPM/Triumph website deliveries |
| Primary property | `https://shpigovsky.ru/` | EV-SHPIG-OP-01; EV-SHPIG-WEB-01 |
| Stack signal | WordPress; possible ACF; possible custom code | EV-SHPIG-OP-01 |
| i-SEO involvement | **Explicitly excluded** as project channel | EV-SHPIG-OP-01 |
| Delivery phase | **SAFE UNKNOWN** — operator describes roles and stack, not completion % or contract dates | EV-SHPIG-OP-01 |
| Consumer programs | MARS · Website Factory · future WP automation | EV-SHPIG-OP-01 — **planned**, not attested |

**Rule:** Operator role statements describe **who executes** — they do **not** mint EXECUTES or COMMISSIONED_BY edges in this pass.

---

## 3. Client acquisition path

```
Ольга Дягилева (PER-0010 — attested Person, i-SEO EMPLOYEE elsewhere)
        │
        │  client referral / acquisition (operator statement)
        ▼
Polygon delivery channel (ORG-0001 — attested Organization)
        │
        │  website + WordPress technical delivery (operator)
        ▼
shpigovsky.ru property (Website candidate — not WEB-*)
        │
        └── commissioning legal subject: ООО «Сознание» (website/policy signal — not attested ORG)
```

| Step | Fact | Evidence | Edge created |
|------|------|----------|--------------|
| 1 | Client came through **Olga Dyagileva** | EV-SHPIG-OP-01 | **No** |
| 2 | Delivery organized under **Polygon (ORG-0001)** | EV-SHPIG-OP-01 | **No** |
| 3 | **Not** classified as i-SEO project | EV-SHPIG-OP-01 | **No** |
| 4 | Olga: comms, coordination, SEO supervision, acceptance | EV-SHPIG-OP-01 | **No** |
| 5 | Operator: frontend, WP, technical delivery | EV-SHPIG-OP-01 | **No** |

---

## 4. Known business facts from shpigovsky.ru

**Source tier:** **E2** — live public website capture (2026-06-10). **Not** Counterparty Card; **not** attested Organization identity.

### 4.1 Brand and positioning

| Fact | Source |
|------|--------|
| **Центр профилактики зависимостей Шпиговский Дом** — primary brand on homepage | EV-SHPIG-WEB-01 |
| **Центр профилактики зависимостей Сергея Шпиговского** — descriptive trade positioning | EV-SHPIG-WEB-01 |
| Page title / SEO signal: лечение алкоголизма и наркомании, зависимости, Москва | EV-SHPIG-WEB-01 |
| Institution type: **немедицинское, социально-психологическое учреждение**; works with medical institutions when needed | EV-SHPIG-WEB-01 |

### 4.2 Services and programs

| Area | Content |
|------|---------|
| Dependency types | ПАВ, алкоголь, азартные игры |
| Program levels | Нейродиагностика (вкл. генотипирование), психокоррекция, йога (Кундалини, гонг, йога-нидра), реабилитация |
| Formats | Личный приём в Москве, онлайн-консультация, гостевой визит в центр, выездные программы |
| Lead capture | Формы «Бесплатная консультация», «Оставить заявку» |

### 4.3 Contact and location

| Field | Value |
|-------|-------|
| URL | `https://shpigovsky.ru/` |
| Policy URL | `https://shpigovsky.ru/policy` |
| Email | `Info@shpigovsky.ru` |
| Phone | +7 (925) 183-64-64; +7 (995) 023-92-26 |
| Center address signal | Московская область, район ЖД станции Катуар |
| Moscow signal | Личный приём в Москве |
| Subpages observed | `/psy`, `/home`, `/policy` |

### 4.4 Legal operator signal *(website only — not CC)*

| Field | Value | Caveat |
|-------|-------|--------|
| Privacy policy operator | **ООО "Сознание"** | EV-SHPIG-WEB-02 |
| Footer copyright holder | **"ООО" Сознание** | EV-SHPIG-WEB-01 — formatting inconsistent |
| INN / KPP / OGRN | **Not published** on reviewed pages | EFV-04 |

### 4.5 Named specialists *(public staff page content)*

Homepage lists multiple specialists; **founder signal:**

| Name | Role signal |
|------|-------------|
| **Шпиговский Сергей Юрьевич** | аддиктолог, интервенционист |

**Rule:** Public staff listings are **Person candidates** only — not minted; may or may not equal contractual client contact.

---

## 5. Candidate organization

### 5.1 SHPIGOVSKY-INTAKE-CAND-O01 — ООО «Сознание» *(legal subject signal)*

| Field | Value |
|-------|-------|
| **Intake label** | SHPIGOVSKY-INTAKE-CAND-O01 |
| **org_slug** | `shpigovsky` *(folder slug — steward may split if CC shows distinct trade org)* |
| **Proposed display name** | **ООО «Сознание»** |
| **Proposed trade / brand aliases** | Шпиговский Дом; Центр профилактики зависимостей Сергея Шпиговского *(website — not attested without CC)* |
| **Class** | **Organization intake candidate** |
| **wave_tier (target)** | **W1-B class client** *(proposed — pending CC)* |
| **business_role (target)** | **CLIENT** *(Polygon delivery context)* |
| **legal_entity_id** | **SAFE UNKNOWN** — LE candidate pending CC |
| **org_id** | **None** — **INTAKE ONLY** |
| **lifecycle_state** | **intake** |
| **Evidence tier** | **E0** operator + **E2** website legal-name signal |
| **Attestation readiness** | **Not ready** — CC absent |

**Claim → evidence:**

- «Website operator ООО "Сознание"» → **EV-SHPIG-WEB-02** → policy §1
- «Polygon client delivery; not i-SEO project» → **EV-SHPIG-OP-01**
- «Trade brand Шпиговский Дом on shpigovsky.ru» → **EV-SHPIG-WEB-01**

**EFV-01 note:** Trade names on website **≠** attested Organization aliases until CC or steward alias review.

---

## 6. Candidate project

### 6.1 SHPIGOVSKY-INTAKE-CAND-PRJ-A01 — Сайт shpigovsky.ru (Polygon delivery)

| Field | Value |
|-------|-------|
| **Intake label** | SHPIGOVSKY-INTAKE-CAND-PRJ-A01 |
| **Proposed canonical name** | **Сайт shpigovsky.ru** *(steward may refine: «Шпиговский Дом — сайт»)* |
| **Class** | **Active project candidate** *(lifecycle target **active** — operator describes ongoing technical delivery roles)* |
| **Population slice** | **client_delivery** |
| **Commissioning org** | SHPIGOVSKY-INTAKE-CAND-O01 *(proposed)* |
| **Execution org** | **ORG-0001** Полигон *(reference — attested)* |
| **Related property** | `shpigovsky.ru` — Website candidate; **not** Project substitute |
| **Technology context** | WordPress; possible ACF; possible custom programming |
| **Delivery state** | **SAFE UNKNOWN** — roles defined; completion / WIP boundary not stated |
| **Evidence** | **E0** EV-SHPIG-OP-01 |
| **CC corroboration** | **None** |
| **prj_id** | **None** — **INTAKE ONLY** |
| **Attestation readiness** | **Hold** — Organization anchor + CC recommended before population |

**Future candidates *(hold — no Project mint)*:**

| Intake label | Description | Verdict |
|--------------|-------------|---------|
| SHPIGOVSKY-INTAKE-FUT-01 | WP automation agents | **Future Candidate** — EV-SHPIG-OP-01 possibility only |
| SHPIGOVSKY-INTAKE-FUT-02 | Extended SEO program as separate initiative | **Future Candidate** — SEO supervision ≠ separate approved project |

---

## 7. Candidate websites/domains

### 7.1 Website assets *(not WEB-*)*

| intake_label | hostname | url | org_binding | web_id | evidence_ref |
|--------------|----------|-----|-------------|--------|--------------|
| SHPIGOVSKY-INTAKE-WEB-C01 | `shpigovsky.ru` | https://shpigovsky.ru/ | SHPIGOVSKY-INTAKE-CAND-O01 *(proposed)* | **none** | EV-SHPIG-OP-01; EV-SHPIG-WEB-01 |
| SHPIGOVSKY-INTAKE-WEB-C02 | `shpigovsky.ru` | https://shpigovsky.ru/policy | same | **none** | EV-SHPIG-WEB-02 |
| SHPIGOVSKY-INTAKE-WEB-C03 | `shpigovsky.ru` | https://shpigovsky.ru/psy | same | **none** | EV-SHPIG-WEB-01 |
| SHPIGOVSKY-INTAKE-WEB-C04 | `shpigovsky.ru` | https://shpigovsky.ru/home | same | **none** | EV-SHPIG-WEB-01 |

### 7.2 Domain assets *(not DOM-*)*

| intake_label | registrable_domain | derived_from | dom_id | evidence_ref |
|--------------|-------------------|--------------|--------|--------------|
| SHPIGOVSKY-INTAKE-DOM-C01 | `shpigovsky.ru` | SHPIGOVSKY-INTAKE-WEB-C01 | **none** | EV-SHPIG-OP-01; EV-SHPIG-WEB-01 |

**Rule:** Single hostname — one Domain candidate; multiple URL paths ≠ multiple domains (EFV-03).

---

## 8. Candidate persons

### 8.1 Referenced attested Person *(no mint, no new edges)*

| person_id | canonical_name | role in this intake | evidence_ref |
|-----------|----------------|---------------------|--------------|
| **PER-0010** | Дягилева Ольга | Acquisition; client comms; coordination; SEO supervision; primary acceptance | EV-SHPIG-OP-01 |

**Note:** Patronymic **SAFE UNKNOWN** in attested graph (ME-W2-01) — unchanged by this intake.

### 8.2 Person intake candidates *(not minted)*

| intake_label | proposed_name | role_signal | contacts | person_id | evidence_ref | intake_verdict |
|--------------|---------------|-------------|----------|-----------|--------------|----------------|
| SHPIGOVSKY-INTAKE-CAND-P01 | **Шпиговский Сергей Юрьевич** | Founder / аддиктолог; possible client-side authority | **SAFE UNKNOWN** | **none** | EV-SHPIG-WEB-01 | **Hold** — public listing only |
| SHPIGOVSKY-INTAKE-CAND-P02 | **Operator** *(steward)* | Frontend; WordPress; technical delivery | **SAFE UNKNOWN** | **none** | EV-SHPIG-OP-01 | **N/A** — executor known operationally; Person not required at intake |

**Rule:** Do **not** mint Person from website staff blocks without CC or steward identity confirmation.

---

## 9. Evidence inventory

### 9.1 Counterparty Card — filesystem inventory (CPV-01)

**Target path:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\shpigovsky\`

**Filesystem check:** 2026-06-10 — **folder does not exist**.

| # | File | Path | Role |
|---|------|------|------|
| — | *(none)* | `…\counterparty-cards\shpigovsky\` | **Folder absent** |

**Existing CC folders (context):** `bzpm`, `i-seo`, `metacode`, `metallka`, `moscow-serm`, `polygon`, `sibcar`, `triumph` — **no** `shpigovsky`.

**CPV verdict:** Inventory **complete** — **zero** non-placeholder files.

### 9.2 Evidence register

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-SHPIG-OP-01** | Operator intake statements (2026-06-10) | **E0** | Acquisition path, Polygon delivery, role split, stack signals, i-SEO exclusion, ecosystem plan |
| **EV-SHPIG-WEB-01** | Live capture `https://shpigovsky.ru/` (2026-06-10) | **E2** | Brand, services, contacts, footer legal-name signal, staff listing |
| **EV-SHPIG-WEB-02** | Live capture `https://shpigovsky.ru/policy` (2026-06-10) | **E2** | Privacy policy operator **ООО "Сознание"**; site URL binding |
| *(pending)* | Counterparty Card — `…\shpigovsky\` | **E1+ expected** | INN, OGRN, legal identity, contractual contacts |

### 9.3 Evidence-first pre-check

| Rule | Application |
|------|-------------|
| **EFV-01** | «Сознание» / «Шпиговский Дом» — **proposed names** only until CC |
| **EFV-02** | No ORCA/MIG/pilot context used as identity source |
| **EFV-03** | `shpigovsky.ru` → Website/Domain candidates; hostname ≠ auto-Project |
| **EFV-04** | CC **absent** — INN/OGRN **SAFE UNKNOWN** despite website legal name |
| **EFV-05** | Duplicate review **cannot** close on INN/OGRN |
| **EFV-06** | All claims cite EV-SHPIG-* or repository search |

### 9.4 Repository search — Shpigovsky references

| Search term | Result |
|-------------|--------|
| `shpigovsky` / `Шпиговск` | **Zero** matches in `C:\AI MARS` |
| `Сознание` (org context) | **No** Atlas Organization entity |
| `shpigovsky.ru` | **No** Atlas Website/Domain entity |
| `ORG-*` for Shpigovsky | **None** — intake only |

**Conclusion:** **Net-new** intake candidate; no existing Atlas population collision on name or hostname.

---

## 10. SAFE UNKNOWN inventory

| id | topic | blocks_intake |
|----|-------|---------------|
| SU-SHPIG-01 | INN, KPP, OGRN for ООО «Сознание» | **Yes** — active Organization attestation |
| SU-SHPIG-02 | Legal vs trade name mapping (Сознание ↔ Шпиговский Дом) | **Yes** |
| SU-SHPIG-03 | Contractual client contact vs public staff listing | **No** — Person deferred |
| SU-SHPIG-04 | Project delivery phase (WIP vs completed vs pre-contract) | **No** — blocks **active** lifecycle certainty |
| SU-SHPIG-05 | Primary client-side representative for Polygon comms | **No** |
| SU-SHPIG-06 | SEO scope boundaries (supervision vs deliverable package) | **No** |
| SU-SHPIG-07 | ACF / custom programming scope approval | **No** |
| SU-SHPIG-08 | DOMAIN registrant and hosting ownership | **No** — Wave 5 |
| SU-SHPIG-09 | COMMERCIAL edge SHPIGOVSKY CLIENT_OF ORG-0001 | **No** — Wave 6 |
| SU-SHPIG-10 | EXECUTES edge ORG-0001 → Project | **No** — Wave 3B after PRJ mint |
| SU-SHPIG-11 | Olga Dyagileva role edge beyond existing PER-0010 ↔ ORG-0003 | **No** — operational narrative only |
| SU-SHPIG-12 | Historical site version / redesign vs greenfield | **No** |
| SU-SHPIG-13 | WP automation agent scope and approval | **No** — future |

---

## 11. Recommended Atlas population path

**Ordered waves — proposal only; no execution in this pass.**

| Step | Wave | Action | Prerequisite |
|------|------|--------|--------------|
| **1** | Pre-wave | Place Counterparty Card in `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\shpigovsky\` | Operator / client docs |
| **2** | CPV + EFV | Re-run inventory; extract INN/OGRN; close SU-SHPIG-01..02 | CC present |
| **3** | **Wave 1** *(or next org tranche)* | Mint **ORG-*** for client Organization; mint **LE-*** for ООО «Сознание» if CC confirms | Duplicate review Pass on legal identifiers |
| **4** | **Wave 2** | Mint client **PER-*** if CC names representatives *(optional if org-only contact)* | Identity from CC |
| **5** | **Wave 3** | Mint **PRJ-*** from SHPIGOVSKY-INTAKE-CAND-PRJ-A01; lifecycle **active** pending steward confirmation | ORG anchor active |
| **6** | **Wave 3B** | Propose EXECUTES / COMMISSIONED_BY edges: ORG-0001 executes; client org commissions | Project + org endpoints |
| **7** | **Wave 4** | Mint **WEB-*** for `shpigovsky.ru`; optional path-level records | Website evidence + org binding |
| **8** | **Wave 5** | Mint **DOM-*** for `shpigovsky.ru` | Registrar evidence if required |
| **9** | **Wave 6** | Mint **CLIENT_OF** client org → ORG-0001 | Commercial reality sign-off |

**Integrity checks during population:**

- **Do not** classify as i-SEO project or route through ORG-0003 EXECUTES without steward charter.
- **Do not** merge with ORG-0001..0007 on hostname or trade name alone.
- **Do not** auto-bind PER-0010 new EMPLOYEE/CONTRACTOR edges to client org without evidence.

**Readiness verdict:**

| Gate | Status |
|------|--------|
| Intake analysis | **Complete** |
| Organization candidate defined | **Yes** — SHPIGOVSKY-INTAKE-CAND-O01 |
| Project candidate defined | **Yes** — SHPIGOVSKY-INTAKE-CAND-PRJ-A01 |
| CC present | **No** |
| Population proposal | **Blocked** |
| Active attestation | **Blocked** |

**Overall verdict:** **PARTIALLY READY**

---

## 12. Validation checklist

| Check | Result |
|-------|--------|
| ORG-0001..0007 intact | **Pass** — no merge proposed |
| No Organization entities minted | **Pass** |
| No Project entities minted | **Pass** |
| No Website entities minted | **Pass** |
| No Domain entities minted | **Pass** |
| No Relationships created | **Pass** |
| EFV applied | **Pass** |
| CPV inventory performed | **Pass** — folder absent documented |
| Atlas graph unchanged | **Pass** |

---

## 13. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md](ATLAS-SHPIGOVSKY-INTAKE-REGISTER-v1.md) | Tabular register |
| [ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md](ATLAS-SHPIGOVSKY-INTAKE-SUMMARY-v1.md) | Executive summary |

---

*ATLAS Shpigovsky Project Intake Analysis v1 — intake only; documentation only.*
