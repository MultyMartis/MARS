# ATLAS Dyakonov Contractor Intake Analysis v1

**Status:** **documented** — Contractor intake analysis only (no population, no attestation).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Intake slug:** `dyakonov`  
**Parent:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) · [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](../foundation/ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) · [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md)  
**Is not:** Organization population, Person population, Legal Entity minting, relationship creation, Project creation, attestation, `ORG-*` / `LE-*` / `PER-*` / `PRJ-*` / `WEB-*` / `DOM-*` / `REL-*` minting.

**Governance applied:** EFV-01..06 · CPV-01..05.

**Explicit exclusions (this package):**

- No `ORG-*` identifier assigned
- No `LE-*` identifier assigned
- No `PER-*` identifier assigned
- No `PRJ-*` identifier assigned
- No `WEB-*` or `DOM-*` identifiers assigned
- No Relationship edges (including CONTRACTOR, VENDOR_OF, EMPLOYEE)
- No attestation or population proposal

---

## 1. Purpose

Выполнить **Evidence-First Contractor Intake** для контрагента **ИП Дьяконов** — классификация кандидата, определение пути population, inventory evidence, duplicate review, и readiness verdict **до** любой population wave.

**Operator evidence scope (binding for this analysis):**

| Block | Content |
|-------|---------|
| Candidate label | **ИП Дьяконов** |
| Business role | **Polygon contractor** |
| Operational role | **Programmer / developer** |
| Organization anchor | **ORG-0001** Веб-студия «Полигон» |
| Evidence source | **Operator-direct statement** (steward intake) |

---

## 2. Repository search — Dyakonov references

### 2.1 Atlas population history

| Search term | Result |
|-------------|--------|
| `Dyakonov` / `Дьяконов` | **No** Organization, Person, Legal Entity, Project, Website, or Domain entity in Atlas population registers |
| `ИП Дьяконов` | **No** matches in `projects/atlas/` |
| `ORG-*` for Dyakonov | **None** — candidate is intake-only |
| `PER-*` for Dyakonov | **None** |
| `LE-*` for Dyakonov | **None** |

**Conclusion:** **No existing entity** in Atlas population. Intake candidate only.

### 2.2 Non-Atlas references *(not contractor evidence)*

| Location | Content | EFV-02 treatment |
|----------|---------|------------------|
| Full repository grep | **Zero** matches for `Дьяконов` / `Dyakonov` | **N/A** — no collateral references |

**Rule:** Absence in repo **corroborates** that intake is net-new; it does **not** substitute for identity evidence (EFV-03, EFV-06).

---

## 3. Evidence inventory

### 3.1 Counterparty Card — filesystem inventory (CPV-01)

**Target path:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\dyakonov\`

**Filesystem check:** 2026-06-07 — **folder does not exist**.

| # | File | Path | Format | Size | Role |
|---|------|------|--------|------|------|
| — | *(none)* | `…\counterparty-cards\dyakonov\` | — | — | **Folder absent** |

**Existing CC folders at storage root (for context):** `polygon`, `metacode`, `i-seo`, `triumph`, `moscow-serm`, `metallka`, `bzpm`, `sibcar` — **no** `dyakonov`.

**CPV verdict:** Inventory **complete** — **zero** non-placeholder files. CC absence blocks identity extraction and active attestation; intake correctly stops at evidence collection.

**Required future path (explicit):**

```text
C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\dyakonov\
```

### 3.2 Steward-supplied operational evidence (E0)

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-DYAK-OP-01** | Steward intake inputs (2026-06-07) | **E0** | Candidate label, business role, operational role, organization anchor |
| **EV-DYAK-OP-02** | Operator-direct statement — contractor of Polygon | **E0** | Commercial posture signal — **no edge created** |

**Not in evidence set:**

- Counterparty Card / requisites (INN, ОГРНИП, legal name)
- Contract, act, or invoice
- Full natural-person name (given name, patronymic, surname)
- Contact channels (phone, email, messenger)
- Website / domain
- Project participation scope
- Engagement dates or deliverable scope

### 3.3 Evidence-first pre-check

| Rule | Application |
|------|-------------|
| **EFV-01** | «ИП Дьяконов» recorded as **proposed display label** only — **not** attested alias without CC |
| **EFV-02** | No project or pilot context used as identity source |
| **EFV-03** | No website/domain candidates inferred — none supplied |
| **EFV-04** | CC **absent** — all legal-entity fields remain **SAFE UNKNOWN** |
| **EFV-05** | Duplicate review **cannot** close on INN/ОГРНИП — CC not reviewed |
| **EFV-06** | All claims below cite EV-DYAK-OP-01/02 or search result |

---

## 4. Required analysis

### 4.1 Future population path — decision

| Path | Applicability | Verdict |
|------|---------------|---------|
| **Organization path only** | Would mint `ORG-*` without `LE-*` binding | **Insufficient** — ИП precedent requires Legal Entity |
| **Person path only** | Would mint `PER-*` + CONTRACTOR → ORG-0001 | **Insufficient alone** — operator label identifies **ИП** business subject, not person name |
| **Organization + Legal Entity path** | `ORG-*` + `LE-*` (ИП) + deferred `PER-*` for natural person | **Primary recommended path** |

**Decision: Organization + Legal Entity path (primary), with Person path as mandatory follow-on.**

**Rationale:**

1. **Operator label is ИП-shaped.** «ИП Дьяконов» signals an individual entrepreneur legal subject — the same class as LE-0001 (ИП Русецкий → ORG-0001) and LE-0002 (ИП Шваков → ORG-0003) in Wave 1 population. ATLAS models ИП as **Organization bound to Legal Entity**, not as a Person record alone.
2. **Contractor is a counterparty business unit.** External contractors operating as ИП are commercial counterparties — W1-B class acquisition path applies ([ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) §3.2).
3. **Person path is secondary, not alternative.** After CC review, the natural person behind the ИП should be proposed as `PER-*` with structural links: **OWNER** (or **REPRESENTATIVE**) → own ИП Organization, and **CONTRACTOR** → ORG-0001 Полигон. Person-only intake would lose the ИП legal-entity boundary.
4. **Organization anchor is relationship context, not population origin.** ORG-0001 is the **engagement anchor** (who the contractor serves); it is **not** the subject being populated.

**Population sequence (future — out of scope here):**

```text
1. CC intake → extract ИП requisites
2. Duplicate review on INN / ОГРНИП
3. Mint ORG-* + LE-* (ИП)
4. Mint PER-* (natural person from CC director/owner field)
5. Wave 2B-class: PER ──CONTRACTOR──► ORG-0001
6. Wave 6+ (optional): contractor ORG ──VENDOR_OF──► ORG-0001 if org-level commercial edge preferred
```

### 4.2 Minimum evidence required

| # | Evidence item | Tier | Blocks population? | Notes |
|---|---------------|------|-------------------|-------|
| E-MIN-01 | **Counterparty Card** with legal name, INN, ОГРНИП | **E1+** | **Yes** | Primary acquisition artifact per OAR-01 |
| E-MIN-02 | **Legal form verification** (ИП confirmed on CC or registrar extract) | **E1+** | **Yes** | Operator label «ИП» is E0 signal only |
| E-MIN-03 | **Natural person full name** (from CC director/owner field) | **E1** | **Yes** for PER mint | CC-PER-01 human review |
| E-MIN-04 | **Duplicate review** on INN / ОГРНИП vs ORG-0001..0006 + LE-0001..0002 | **E1+** | **Yes** | EFV-05 |
| E-MIN-05 | **Operator/steward confirmation** of contractor role and Polygon anchor | **E0** | **No** — already present | EV-DYAK-OP-01/02 |
| E-MIN-06 | **Contract or engagement letter** (scope corroboration) | **E1–E2** | **No** — recommended | Supports CONTRACTOR vs EMPLOYEE boundary; OPS domain |
| E-MIN-07 | **Contact channel** (phone / email / messenger) | **E1** | **No** | Operational; PersonContacts at population |
| E-MIN-08 | **Project participation list** | **E1** | **No** | Enables PARTICIPATES edges — currently SAFE UNKNOWN |

**Minimum gate for population proposal:** E-MIN-01 through E-MIN-04 **must** be satisfied.

### 4.3 Future Counterparty Card requirements

| Requirement | Detail |
|-------------|--------|
| **Storage path** | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\dyakonov\` |
| **Accepted formats** | PDF (preferred), DOCX, XLSX, image, structured text per CC model |
| **Must extract** | Legal name (полное наименование ИП), INN, ОГРНИП, legal address |
| **Should extract** | Director / owner natural-person name → proposed Person; bank details (corroboration); contact phone/email |
| **Must not infer** | Project scope, employment vs contract status, Polygon engagement dates |
| **Provenance** | Document who provided the card and intake date |
| **Tier expectation** | **E1** minimum for external ИП counterparty (W1-B class) |
| **Review gate** | CC-PER-01 if director name extracted; duplicate review mandatory on INN |

### 4.4 Candidate relationship families

| Family | Subject → Object | Type code *(candidate)* | Wave *(target)* | Evidence needed | Created here? |
|--------|------------------|-------------------------|-----------------|-----------------|---------------|
| Person ↔ Organization | Person → ORG-0001 Полигон | **CONTRACTOR** | Wave 2B-class | E1 CC + operator confirm | **No** |
| Person ↔ Organization | Person → own ИП Organization | **OWNER** or **REPRESENTATIVE** | Wave 2B-class | E1 CC director field | **No** |
| Organization ↔ Organization | Contractor ORG → ORG-0001 | **VENDOR_OF** *(optional)* | Wave 6+ | E1 CC + commercial review | **No** |
| Person ↔ Project | Person → PRJ-* | **PARTICIPATES** | Wave 3+ | E1 project scope evidence | **No** — scope unknown |
| Organization ↔ Project | Contractor ORG → PRJ-* | **EXECUTES** | Wave 3B+ | E1 delivery attestation | **No** — scope unknown; unlikely without explicit attestation |

**Informational context (no edges):**

| Field | Value | evidence_ref |
|-------|-------|--------------|
| Engagement anchor | ORG-0001 Веб-студия «Полигон» | EV-DYAK-OP-01 |
| Operational role signal | Programmer / developer | EV-DYAK-OP-01 |
| Business role signal | Polygon contractor | EV-DYAK-OP-02 |

### 4.5 Classification — Contractor vs alternatives

| Classification | Fit | Rationale | Verdict |
|----------------|-----|-----------|---------|
| **Contractor** | **Strong** | Operator states «Polygon contractor»; operational role is developer; taxonomy type **CONTRACTOR** = Person provides services under contract to org ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §1); precedent PER-0009 (developer, EMPLOYEE vs CONTRACTOR resolved at 2B) | **Primary** |
| **Subcontractor** | **Weak** | Not a taxonomy type code; would require attested intermediary chain (e.g. Polygon → agency → Dyakonov). No subcontract chain evidence. Wave 3B notes on «i-SEO subcontractor» are operational narrative only — not a model precedent for this intake | **Reject as primary** |
| **Vendor** | **Secondary** | **VENDOR_OF** is Organization → Organization commercial direction. Applicable if ИП Дьяконов is modeled as separate org providing services to Polygon — Wave 6+ commercial edge, not primary business_role | **Secondary / deferred** |
| **Representative** | **None** | No evidence of external representation authority for Polygon or any client org | **Reject** |
| **Other** | **Fallback only** | Would apply only if CC contradicts contractor posture (e.g. reveals employment) | **Hold** — pending CC |

**Classification verdict: Contractor (primary).**

**business_role (target):** `CONTRACTOR`  
**relationship_type (target):** `CONTRACTOR` (Person → ORG-0001)  
**commercial_org_edge (optional, deferred):** `VENDOR_OF` (contractor ORG → ORG-0001)

**Boundary note:** EMPLOYEE vs CONTRACTOR resolution follows Wave 2B precedent (PER-0009). Current E0 evidence favours **CONTRACTOR** because operator explicitly says «contractor» and candidate is an external ИП — but final lock requires CC + engagement document review. If CC reveals employment relationship, classification must be corrected before attestation.

---

## 5. Contractor intake candidates *(not minted)*

### 5.1 DYAKONOV-INTAKE-CAND-O01 — ИП Дьяконов *(Organization candidate)*

| Field | Value |
|-------|-------|
| **Intake label** | DYAKONOV-INTAKE-CAND-O01 |
| **org_slug** | `dyakonov` |
| **Proposed display name** | **ИП Дьяконов** |
| **Proposed canonical_name** | **ИП Дьяконов** *(steward may refine after CC)* |
| **Class** | **Contractor Organization intake candidate** |
| **wave_tier (target)** | **W1-B class counterparty** *(proposed — pending CC)* |
| **business_role (target)** | **CONTRACTOR** |
| **legal_entity_id** | **SAFE UNKNOWN** — no CC; expected ИП |
| **org_id** | **None** — **INTAKE ONLY** |
| **lifecycle_state** | **intake** — not `proposed` / not `active` |
| **Evidence tier (intake)** | **E0** — operator-direct statement only |
| **Attestation readiness** | **Not ready** — blocked by missing CC |

### 5.2 DYAKONOV-INTAKE-CAND-LE01 — Legal Entity candidate *(ИП)*

| Field | Value |
|-------|-------|
| **Intake label** | DYAKONOV-INTAKE-CAND-LE01 |
| **Proposed legal form** | **ИП** *(E0 signal — unverified)* |
| **Proposed legal name** | **SAFE UNKNOWN** |
| **INN** | **SAFE UNKNOWN** |
| **ОГРНИП** | **SAFE UNKNOWN** |
| **le_id** | **None** — **INTAKE ONLY** |
| **org_binding** | DYAKONOV-INTAKE-CAND-O01 *(proposed)* |
| **Evidence** | **E0** EV-DYAK-OP-01 |

### 5.3 DYAKONOV-INTAKE-CAND-P01 — Natural person candidate *(reference only)*

| Field | Value |
|-------|-------|
| **Intake label** | DYAKONOV-INTAKE-CAND-P01 |
| **Proposed surname signal** | **Дьяконов** *(from ИП label only)* |
| **Given name / patronymic** | **SAFE UNKNOWN** |
| **Full canonical name** | **SAFE UNKNOWN** |
| **Role signal** | ИП owner / contractor developer *(operator)* |
| **person_id** | **None** — **not minted** |
| **Evidence** | **E0** EV-DYAK-OP-01 |
| **W2-E-03 note** | Surname-only from ИП label — **hold** until CC provides director/owner full name |

**Rule:** Do **not** mint Person from ИП label alone at intake.

---

## 6. Duplicate review

### 6.1 vs attested Organizations

| review_id | Compare | Identifiers used | Verdict | Merge? |
|-----------|---------|------------------|---------|--------|
| DYAK-D-01 | vs ORG-0001 Полигон | No shared identity | **Distinct** — engagement anchor, not same subject | **No** |
| DYAK-D-02 | vs ORG-0002 MetaCode | No overlap | **Distinct** | **No** |
| DYAK-D-03 | vs ORG-0003 i-SEO | No overlap | **Distinct** | **No** |
| DYAK-D-04 | vs ORG-0004 Триумф | No overlap | **Distinct** | **No** |
| DYAK-D-05 | vs ORG-0005 ЗПМ | No overlap | **Distinct** | **No** |
| DYAK-D-06 | vs ORG-0006 SIBCAR | No overlap | **Distinct** | **No** |

### 6.2 vs attested Legal Entities

| review_id | Compare | Identifiers used | Verdict | Merge? |
|-----------|---------|------------------|---------|--------|
| DYAK-D-07 | vs LE-0001 ИП Русецкий (ORG-0001) | Surname differs; no CC | **Distinct** | **No** |
| DYAK-D-08 | vs LE-0002 ИП Шваков (ORG-0003) | No overlap | **Distinct** | **No** |

### 6.3 vs attested Persons

| review_id | Compare | Identifiers used | Verdict | Merge? |
|-----------|---------|------------------|---------|--------|
| DYAK-D-09 | vs PER-0001..0013 | Surname «Дьяконов» not in Wave 2 register | **Distinct** *(preliminary)* | **No** |
| DYAK-D-10 | vs PER-0009 Антон Кораблёв (developer precedent) | Different subject; role class may overlap | **Distinct** | **No** |

### 6.4 INN / ОГРНИП / legal name cross-check

| Field | Status |
|-------|--------|
| INN | **SAFE UNKNOWN** — CC absent (CPV-01) |
| ОГРНИП | **SAFE UNKNOWN** |
| Legal entity name | **SAFE UNKNOWN** |

**Duplicate review summary:** **Open** — cannot close to **Pass** on legal identity until CC (EFV-05). Preliminary distinctness vs all attested entities **Pass** on available E0 signals.

**Integrity checks:** ORG-0001 **unchanged** · ZPM (ORG-0005) **Pass** · SIBCAR (ORG-0006) **Pass** · No merge proposed **Pass**

---

## 7. SAFE UNKNOWN inventory

| id | topic | blocks_intake |
|----|-------|---------------|
| SU-DYAK-01 | Legal form verification (ИП vs other) | **Yes** — active attestation |
| SU-DYAK-02 | INN | **Yes** |
| SU-DYAK-03 | ОГРНИП | **Yes** |
| SU-DYAK-04 | Legal vs trade name mapping | **Yes** |
| SU-DYAK-05 | Natural person full name (given, patronymic) | **Yes** — Person mint |
| SU-DYAK-06 | Contacts (phone, email, messenger) | **No** |
| SU-DYAK-07 | Websites | **No** — none supplied |
| SU-DYAK-08 | Domains | **No** — none supplied |
| SU-DYAK-09 | Project participation | **No** — PARTICIPATES deferred |
| SU-DYAK-10 | Contractual scope (deliverables, dates, rate model) | **No** — recommended for CONTRACTOR lock |
| SU-DYAK-11 | EMPLOYEE vs CONTRACTOR final classification | **No** — resolve at population review; E0 favours CONTRACTOR |
| SU-DYAK-12 | Subcontract intermediary chain | **No** — no evidence of intermediary |

---

## 8. Validation checklist

| Check | Result |
|-------|--------|
| ORG-0001 (Полигон) intact — anchor only, not modified | **Pass** |
| ZPM (ORG-0005) intact | **Pass** |
| SIBCAR (ORG-0006) intact | **Pass** |
| No merge with existing organizations | **Pass** |
| No Organization entities minted | **Pass** |
| No Legal Entity entities minted | **Pass** |
| No Person entities minted | **Pass** |
| No Website entities minted | **Pass** |
| No Domain entities minted | **Pass** |
| No Relationships created | **Pass** |
| No Project creation | **Pass** |
| No graph changes | **Pass** |
| No lifecycle changes | **Pass** |
| EFV applied | **Pass** |
| CPV inventory performed | **Pass** — folder absent documented |
| CC requirement explicit | **Pass** — path `…\dyakonov\` |

---

## 9. Readiness verdict

| Gate | Status |
|------|--------|
| Intake analysis | **Complete** |
| Contractor candidate defined | **Yes** — DYAKONOV-INTAKE-CAND-O01 + LE01 + P01 |
| Population path determined | **Yes** — Organization + Legal Entity (primary) |
| Classification determined | **Yes** — Contractor (primary) |
| CC present | **No** |
| Population proposal | **Deferred** |
| Active attestation | **Blocked** |

**Overall verdict:** **READY FOR EVIDENCE COLLECTION**

**Population deferred** until minimum evidence gate (E-MIN-01..04) is satisfied.

**Next steps (out of scope for this pass):**

1. Steward places CC artifacts in `dyakonov\` folder.
2. Re-run CPV-01 inventory + EFV-04 extraction.
3. Close duplicate review on CC-backed INN / ОГРНИП.
4. Separate population package — mint `ORG-*` + `LE-*` + `PER-*` only after evidence review.

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md](ATLAS-DYAKONOV-INTAKE-REGISTER-v1.md) | Tabular register |
| [ATLAS-DYAKONOV-INTAKE-SUMMARY-v1.md](ATLAS-DYAKONOV-INTAKE-SUMMARY-v1.md) | Executive summary |

---

*ATLAS Dyakonov Contractor Intake Analysis v1 — intake only; documentation only.*
