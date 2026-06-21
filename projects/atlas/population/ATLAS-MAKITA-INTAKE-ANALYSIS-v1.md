# ATLAS Makita Snab Intake Analysis v1

**Status:** **documented** — Organization intake analysis only (no population, no attestation).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Intake slug:** `makita-snab`  
**Parent:** [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) · [ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md](../foundation/ATLAS-INTAKE-AND-REVIEW-MODEL-v1.md) · [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md)  
**Is not:** Organization population, Organization attestation, relationship creation, Project creation, Website attestation, Domain population, `ORG-*` / `WEB-*` / `DOM-*` minting.

**Governance applied:** EFV-01..06 · CPV-01..05.

**Explicit exclusions (this package):**

- No `ORG-*` identifier assigned
- No `WEB-*` or `DOM-*` identifiers assigned
- No Person mint (`PER-*`)
- No Relationship edges (including CLIENT_OF i-SEO)
- No Project intake
- No website live capture or attestation

---

## 1. Purpose

Выполнить **Evidence-First Organization Intake** для операционного контрагента **Макита Снаб** — классификация кандидата, inventory evidence, duplicate review, и readiness verdict **до** population wave.

**Operator evidence scope (binding for this analysis):**

| Block | Content |
|-------|---------|
| Display name | **Макита Снаб** |
| Primary contact | **Артём** *(given name only)* |
| Phone | **8-926-022-30-91** |
| Websites *(operator: both exist)* | `https://makita-snab.ru/` · `https://makita-land.ru/` |
| Vendor context | Client of **i-SEO** (ORG-0003); i-SEO performs **SEO** on **both** websites |
| Service context | **SEO** (i-SEO) · **Yandex Direct** (steward) |
| Steward scope | **Yandex Direct** only; does **not** manage contracts, accounting, or document flow |
| Direct communication | Steward ↔ **Артём** |

---

## 2. Repository search — Makita references

### 2.1 Atlas population history

| Search term | Result |
|-------------|--------|
| `Makita` / `Макита` | **No** Organization, Person, Project, Website, or Domain entity in Atlas population registers |
| `Makita Snab` / `Макита Снаб` | **No** matches in `projects/atlas/` |
| `makita-snab.ru` | **No** Atlas entity; not in Wave 1 dataset |
| `makita-land.ru` | **No** Atlas entity; not in Wave 1 dataset |
| `ORG-*` for Makita | **None** — next available org id in documentation examples is ORG-0007 *(not assigned)* |

**Conclusion:** **No existing Organization** in Atlas population. Intake candidate only.

### 2.2 Non-Atlas references *(not Organization evidence)*

| Location | Content | EFV-02 treatment |
|----------|---------|------------------|
| `projects/orca/pilots/makita-lrl-*.md` | ORCA LRL pilot charter — generic «Makita» project placeholder | **Excluded** — pilot docs ≠ Organization identity |
| `archive/orca-lrl-foundation-v1/pilots/` | Archived pilot copies | **Excluded** |
| `projects/mig/contracts/research-pack-v1.md` | States Makita **not registered** in ATLAS | **Corroborates absence** — not identity proof |
| `projects/orca/intelligence/landing-readiness-layer-v1.md` | Post-pilot consideration note | **Excluded** |

**Rule:** ORCA / MIG / LRL pilot material may **correlate** with future work — it does **not** substitute for Organization intake evidence (EFV-02, EFV-03).

---

## 3. Evidence inventory

### 3.1 Counterparty Card — filesystem inventory (CPV-01)

**Target path:** `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\makita-snab\`

**Filesystem check:** 2026-06-07 — **folder does not exist**.

| # | File | Path | Format | Size | Role |
|---|------|------|--------|------|------|
| — | *(none)* | `…\counterparty-cards\makita-snab\` | — | — | **Folder absent** |

**Existing CC folders at storage root (for context):** `polygon`, `metacode`, `i-seo`, `triumph`, `moscow-serm`, `metallka`, `bzpm`, `sibcar` — **no** `makita-snab`.

**CPV verdict:** Inventory **complete** — **zero** non-placeholder files. **STOP-CPV-03** would block **active** Organization attestation; intake correctly stops at **PARTIALLY READY**.

**Required future path (explicit):**

```text
C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\makita-snab\
```

### 3.2 Steward-supplied operational evidence (E0)

| Ref | Artifact | Tier | Role |
|-----|----------|------|------|
| **EV-MAKITA-OP-01** | Steward intake inputs (2026-06-07) | **E0** | Display name, contact given name, phone, website URLs, operational context, steward scope boundaries |
| **EV-MAKITA-OP-02** | Steward statement — both websites **currently exist** | **E0** | Website **candidate** corroboration only — **not** live capture in this pass |
| **EV-MAKITA-OP-03** | Intake enrichment pass — operational reality consolidation (2026-06-07) | **E0** | Service context, boundaries, both-site SEO, document-flow exclusion — see [ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md) |

**Not in evidence set:**

- Counterparty Card / requisites (INN, OGRN, legal name)
- Contract, act, or invoice
- Live HTTP snapshot or registrar extract
- Full legal name of contact **Артём**
- Confirmation that «Макита Снаб» = legal entity trade name

### 3.3 Evidence-first pre-check

| Rule | Application |
|------|-------------|
| **EFV-01** | «Макита Снаб» recorded as **proposed display name** only — **not** attested alias without CC |
| **EFV-02** | ORCA Makita pilot **not** used as org merge or identity source |
| **EFV-03** | Hostnames `makita-snab.ru` / `makita-land.ru` → **Website / Domain candidates** only |
| **EFV-04** | CC **absent** — all legal-entity fields remain **SAFE UNKNOWN** |
| **EFV-05** | Duplicate review **cannot** close on INN/OGRN — CC not reviewed |
| **EFV-06** | All claims below cite EV-MAKITA-OP-01/02 or search result |

---

## 4. Organization intake candidate

### 4.1 MAKITA-INTAKE-CAND-O01 — Макита Снаб

| Field | Value |
|-------|-------|
| **Intake label** | MAKITA-INTAKE-CAND-O01 |
| **org_slug** | `makita-snab` |
| **Proposed display name** | **Макита Снаб** |
| **Proposed canonical_name** | **Макита Снаб** *(steward may refine after CC)* |
| **Class** | **Organization intake candidate** |
| **wave_tier (target)** | **W1-B class client** *(proposed — pending CC)* |
| **business_role (target)** | **CLIENT** *(operator context: i-SEO SEO client)* |
| **legal_entity_id** | **SAFE UNKNOWN** — no CC |
| **org_id** | **None** — **INTAKE ONLY** |
| **lifecycle_state** | **intake** — not `proposed` / not `active` |
| **primary_contact_person_id** | **SAFE UNKNOWN** — Person not minted |
| **Evidence tier (intake)** | **E0** — operational steward inputs only |
| **Attestation readiness** | **Not ready** — blocked by missing CC |

**Claim → evidence:**

- «Organization display name Макита Снаб» → **EV-MAKITA-OP-01**
- «Client of i-SEO; SEO work» → **EV-MAKITA-OP-01** → vendor context ORG-0003 — **no edge created**
- «Steward: Yandex Direct only; no contracts/accounting/document flow» → **EV-MAKITA-OP-01**, **EV-MAKITA-OP-03** → scope boundary
- «i-SEO SEO on both websites» → **EV-MAKITA-OP-03** → vendor service context — **no edge created**

---

## 5. Person intake candidate *(reference only — not minted)*

| Field | Value |
|-------|-------|
| **Intake label** | MAKITA-INTAKE-CAND-P01 |
| **Proposed given name** | **Артём** |
| **Full canonical name** | **SAFE UNKNOWN** — patronymic, surname not supplied |
| **Role signal** | Operational owner / primary contact *(operator)* |
| **Phone** | 8-926-022-30-91 |
| **Email / Telegram** | **SAFE UNKNOWN** |
| **person_id** | **None** — **not minted** |
| **Evidence** | **E0** EV-MAKITA-OP-01 |
| **W2-E-03 note** | Email-only mint prohibited — name incomplete; **hold** until CC or fuller identity |

**Rule:** Do **not** mint Person from phone + given name alone at intake.

---

## 6. Candidate Website assets *(not WEB-*)*

| intake_label | hostname | url | evidence | mint |
|--------------|----------|-----|----------|------|
| MAKITA-INTAKE-WEB-C01 | `makita-snab.ru` | https://makita-snab.ru/ | E0 EV-MAKITA-OP-01, EV-MAKITA-OP-02 | **No WEB-*** |
| MAKITA-INTAKE-WEB-C02 | `makita-land.ru` | https://makita-land.ru/ | E0 EV-MAKITA-OP-01, EV-MAKITA-OP-02 | **No WEB-*** |

**Notes:**

- Recorded as **candidates** for future Wave 4 Website intake.
- Operator states both sites **exist** — **not** verified by live fetch in this pass.
- Ownership / org binding **SAFE UNKNOWN** until CC.

---

## 7. Candidate Domain assets *(not DOM-*)*

| intake_label | registrable_domain | derived_from | evidence | mint |
|--------------|-------------------|--------------|----------|------|
| MAKITA-INTAKE-DOM-C01 | `makita-snab.ru` | MAKITA-INTAKE-WEB-C01 | E0 EV-MAKITA-OP-01 | **No DOM-*** |
| MAKITA-INTAKE-DOM-C02 | `makita-land.ru` | MAKITA-INTAKE-WEB-C02 | E0 EV-MAKITA-OP-01 | **No DOM-*** |

**Rule:** Hostname stems do **not** prove alias equivalence or legal identity (EFV-01, EFV-03).

---

## 8. Duplicate review

### 8.1 vs attested Organizations

| review_id | Compare | Identifiers used | Verdict | Merge? |
|-----------|---------|------------------|---------|--------|
| MAKITA-D-01 | vs ORG-0001 Полигон | No shared CC / INN | **Distinct** | **No** |
| MAKITA-D-02 | vs ORG-0002 MetaCode | No overlap | **Distinct** | **No** |
| MAKITA-D-03 | vs ORG-0003 i-SEO | Vendor context only — **not** same subject | **Distinct** | **No** |
| MAKITA-D-04 | vs ORG-0004 Триумф | No overlap | **Distinct** | **No** |
| MAKITA-D-05 | vs ORG-0005 ЗПМ | No overlap | **Distinct** | **No** |
| MAKITA-D-06 | vs ORG-0006 SIBCAR | No overlap | **Distinct** | **No** |
| MAKITA-D-07 | `makita-snab.ru` vs `bzpm.ru` / SIBCAR hosts | Hostname only | **Distinct** | **No** |
| MAKITA-D-08 | ORCA «Makita» pilot generic | Class boundary | **Not an Organization** | **No** |

**ZPM integrity:** ORG-0005 **ЗПМ** — **unchanged**; no alias or merge proposed.  
**SIBCAR integrity:** ORG-0006 **SIBCAR** — **unchanged**; no alias or merge proposed.

### 8.2 INN / OGRN / legal name cross-check

| Field | Status |
|-------|--------|
| INN | **SAFE UNKNOWN** — CC absent (CPV-01) |
| OGRN | **SAFE UNKNOWN** |
| Legal entity name | **SAFE UNKNOWN** |

**Duplicate review summary:** **Open — low** on trade-name collision with global «Makita» tool brand; **cannot** close to **Pass** on legal identity until CC (EFV-05).

---

## 9. SAFE UNKNOWN inventory

| id | topic | blocks_intake |
|----|-------|---------------|
| SU-MAKITA-01 | Legal entity form (ООО / ИП / etc.) | **Yes** — active attestation |
| SU-MAKITA-02 | INN, KPP, OGRN | **Yes** |
| SU-MAKITA-03 | Legal vs trade name mapping | **Yes** |
| SU-MAKITA-04 | Full name of contact Артём | **No** — Person deferred |
| SU-MAKITA-05 | Email / Telegram for Артём | **No** |
| SU-MAKITA-06 | Which website is primary org property | **No** — Wave 4 |
| SU-MAKITA-07 | Relationship MAKITA ↔ i-SEO (commercial edge) | **No** — Wave 6; not created here |
| SU-MAKITA-08 | Relationship MAKITA ↔ steward (Polygon) | **No** — scope: Yandex Direct only per steward |
| SU-MAKITA-09 | Contract / accounting ownership | **No** — explicitly out of steward scope |
| SU-MAKITA-10 | Live site technical verification | **No** — optional future evidence |
| SU-MAKITA-11 | Document-flow ownership | **No** — explicitly out of steward scope (EV-MAKITA-OP-03) |

---

## 10. Validation checklist

| Check | Result |
|-------|--------|
| ZPM (ORG-0005) intact | **Pass** |
| SIBCAR (ORG-0006) intact | **Pass** |
| No merge with existing organizations | **Pass** |
| No Website entities minted | **Pass** |
| No Domain entities minted | **Pass** |
| No Relationships created | **Pass** |
| No Project creation | **Pass** |
| EFV applied | **Pass** |
| CPV inventory performed | **Pass** — folder absent documented |
| CC requirement explicit | **Pass** — path `…\makita-snab\` |

---

## 11. Readiness verdict

| Gate | Status |
|------|--------|
| Intake analysis | **Complete** |
| Organization candidate defined | **Yes** — MAKITA-INTAKE-CAND-O01 |
| CC present | **No** |
| Population proposal | **Blocked** |
| Active attestation | **Blocked** |

**Overall verdict:** **PARTIALLY READY**

**Blocker:** Missing Counterparty Card at required path:

```text
C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\makita-snab\
```

**Next steps (out of scope for this pass):**

1. Steward places CC artifacts in `makita-snab\` folder.
2. Re-run CPV-01 inventory + EFV-04 extraction.
3. Separate Organization population package — mint `ORG-*` only after duplicate review on CC-backed identifiers.

---

## 12. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-MAKITA-INTAKE-REGISTER-v1.md](ATLAS-MAKITA-INTAKE-REGISTER-v1.md) | Tabular register |
| [ATLAS-MAKITA-INTAKE-SUMMARY-v1.md](ATLAS-MAKITA-INTAKE-SUMMARY-v1.md) | Executive summary |
| [ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md) | Operational enrichment — **INTAKE ENRICHED** |

---

*ATLAS Makita Snab Intake Analysis v1 — intake only; documentation only.*
