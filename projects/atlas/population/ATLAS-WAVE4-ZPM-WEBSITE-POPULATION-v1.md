# ATLAS Wave 4 ZPM Website Population v1

**Status:** **documented** — Wave 4 ZPM canonical Website population plan (normative for operators); **synced** with ZPM Website Model Correction 2026-06-07.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Organization anchor:** ORG-0005 **ЗПМ** · LE-0004 ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ»  
**Parent:** [ATLAS-WAVE4-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-WEBSITE-POPULATION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) · [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) · [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md)  
**Is not:** runtime, API, automation, database schema, relationship attestation, Domain population, Wave 4B execution, attested canonical export.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ZPM Organization ORG-0005: **active** — AT-W1B-01; canonical **ЗПМ** — RN-W1B-01
- Wave 2 ZPM Persons PER-0014, PER-0015: **active** — AT-W2-ZPM-01..02
- Wave 2B ZPM Person → Organization: **COMPLETE** — AT-W2B-ZPM-01..02
- Wave 3 ZPM Projects PRJ-0009, PRJ-0010: **attested** — AT-W3-ZPM-01..02
- Wave 3B ZPM Project ↔ Organization: **COMPLETE** — AT-W3B-ZPM-01..02
- ZPM Website Model Correction: **EXECUTED** — [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md)
- Population verdict (3B-ZPM): **READY FOR WAVE 4 ZPM WEBSITE POPULATION**

**Binding operator scope (this tranche):**

- Mint **1** Website record only — **WEB-ZPM-01** `bzpm.ru` (**active**).
- **One hostname → one Website**; historical delivery generations represented by **Projects** (PRJ-0010), not additional Website entities.
- **WEB-ZPM-02 retired** — do not mint, attest, or promote (COR-ZPM-WEB-01).
- **No** Domain (`DOM-*`), relationship edges, or Organization→Website / Person→Website edges.
- Org/project fields — **display candidates**; structural edges deferred to Wave 4B-ZPM / Wave 5 / Wave 6.

---

## 1. Purpose

Зафиксировать **канонический план population** класса **Website** для Wave 4 tranche **ZPM** (ORG-0005): состав, `WEB-ZPM-01` mint, lifecycle, evidence, org/project context, candidate relationships для Wave 4B-ZPM, границы foundation.

**Normative scope Wave 4 ZPM:**

```text
Website entity intake + attestation plan (1 record — WEB-ZPM-01)
Wave 4B-ZPM (отдельный пакет): Website ↔ Project BELONGS_TO — только после Website endpoint attested
Wave 5 ZPM: Domain entities + PRIMARY_DOMAIN family для bzpm.ru → WEB-ZPM-01
Wave 6: CLIENT_OF ORG-0005 → ORG-0001 и прочие org↔org
```

---

## 2. Identity rule (binding)

| Rule | Application |
|------|-------------|
| **ORG-0005 canonical name** | **ЗПМ** — per [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md) |
| **Domain stem `bzpm.ru`** | Corporate website hostname; not a separate organization |
| **BZPM** | Historical identifier · domain stem · **alias** — **not** a separate organization |
| **Do not create** any new Organization | ORG-0005 only |
| **EIR-W01** | One canonical website per business web property identity — **one** Website for `bzpm.ru` |
| **Not identity conflicts** | ЗПМ · ООО ЗПМ · Завод Пищевого Машиностроения · `bzpm.ru` — aliases / display / property context |

---

## 3. Evidence pre-check (mandatory)

**Governance:** EFV-01..06 · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) CPV-01.

| Ref | Artifact | Tier | Role in this population |
|-----|----------|------|-------------------------|
| **EV-ZPM-OP-ACT-01** | Operator statement — current catalog rebuild on `bzpm.ru` | **E0** | WEB-ZPM-01 **active** delivery |
| **EV-ZPM-OP-HIST-01** | Operator statement — historical `bzpm.ru` site delivery | **E0** | **PRJ-0010 only** — not Website mint basis |
| **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` §17 | **E1** | Org anchor; **Bzpm.ru** — indirect hostname corroboration for WEB-ZPM-01 |
| **AT-W1B-01** | [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | attestation | ORG-0005 **active** |
| **AT-W3-ZPM-01** | [ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE3-ZPM-PROJECT-ACTIVE-ATTESTATION-v1.md) | attestation | PRJ-0009 **active** |
| **AT-W3-ZPM-02** | Same | attestation | PRJ-0010 **deprecated** |
| **AT-W3B-ZPM-01..02** | [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-ATTESTATION-v1.md) | attestation | REL-ZPM-PJ-01..04 **active** |

**EFV application:**

| Rule | Application |
|------|-------------|
| **EFV-02** | SIBCAR / SITE-001 — **not** used as Website evidence |
| **EFV-03** | Two delivery phases on `bzpm.ru` → **two Projects** (PRJ-0009 + PRJ-0010); **one** Website — COR-ZPM-WEB-12 |
| **EFV-04** | CC §17 corroborates org website pointer — **not** delivery-generation boundary substitute |
| **EFV-06** | Each website: claim → evidence ref → operator block |

**Primary evidence paths:**

```text
E0 operator — EV-ZPM-OP-ACT-01 (WEB-ZPM-01)
E0 operator — EV-ZPM-OP-HIST-01 (PRJ-0010 — Project layer)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx (org anchor only)
```

**Dataset note:** [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx) Websites sheet — **no** ZPM rows. Mint from Wave 3 ZPM attestation chain + operator evidence only.

---

## 4. Population roster (canonical)

**Identifier scheme:** `WEB-ZPM-01` — ZPM tranche namespace (distinct from core Wave 4 Triumph roster WEB-0006..0009). `WEB-ZPM-02` **retired unused** per IDP-03.

### 4.1 Summary table

| website_id | canonical_name | website_kind | lifecycle_state *(target)* | roster_priority | primary_org_candidate | primary_project_candidate | evidence_tier | attestation_readiness |
|------------|----------------|--------------|------------------------------|-----------------|----------------------|---------------------------|---------------|----------------------|
| WEB-ZPM-01 | bzpm.ru | **corporate** *(catalog platform)* | **active** | **P0** | ORG-0005 ЗПМ | PRJ-0009 Каталог-платформа bzpm.ru | **E0** | **ready** |

**Lifecycle at population:** WEB-ZPM-01 minted as **proposed** pending steward attestation act AT-W4-ZPM-01.

---

## 5. Per-website analysis

### 5.1 WEB-ZPM-01 — bzpm.ru (sole real web property)

| Field | Value |
|-------|-------|
| **website_id** | WEB-ZPM-01 |
| **canonical_name** | bzpm.ru |
| **website_kind** | **corporate** — catalog-platform generation (ongoing property) |
| **url** | `https://bzpm.ru` *(production property — operator narrative; live probe not blocking at E0)* |
| **lifecycle_state (target)** | **active** — ongoing client web property; catalog-platform delivery almost complete |
| **roster_priority** | **P0** |
| **primary_org_candidate** | ORG-0005 ЗПМ |
| **primary_project_candidate** | PRJ-0009 Каталог-платформа bzpm.ru |
| **secondary_project_context** | PRJ-0010 Сайт bzpm.ru (исходная версия) — **deprecated** historical delivery; BELONGS_TO at Wave 4B (REL-ZPM-WB-03) |
| **aliases** | «Сайт ЗПМ»; «Каталог bzpm.ru»; «Bzpm.ru» *(CC case variant)* |
| **platform context** | Polygon catalog-platform delivery *(current)*; WP + The7 historical context via PRJ-0010 narrative |
| **related people (informational)** | PER-0014, PER-0015 — **no edges minted** |
| **evidence basis** | **E0** EV-ZPM-OP-ACT-01; PRJ-0009 **active** (AT-W3-ZPM-01); PRJ-0010 **deprecated** (AT-W3-ZPM-02); REL-ZPM-PJ-01..04 |
| **CC corroboration** | EV-W1B-CC-01 §17 — org website field **Bzpm.ru**; generation-agnostic |
| **attestation readiness** | **Ready** at **E0** — operator-confirmed ongoing property (Triumph analog: WEB-0006 single property, multi-Project BELONGS_TO) |

**Claim → evidence:**

- «Текущая версия `bzpm.ru` — каталог-платформа; почти завершено; active WIP» → **EV-ZPM-OP-ACT-01**
- «Историческая доставка ~5 лет назад» → **EV-ZPM-OP-HIST-01** → **PRJ-0010** (not separate Website)

### 5.2 WEB-ZPM-02 — retired (not minted)

| Field | Value |
|-------|-------|
| **website_id** | WEB-ZPM-02 |
| **disposition** | **Rejected / not minted** — COR-ZPM-WEB-01 |
| **reason** | Historical delivery generation modeled at **Project** layer (PRJ-0010); second Website violates EIR-W01 |
| **evidence re-route** | EV-ZPM-OP-HIST-01 → PRJ-0010 only |

---

## 6. Website policy — single-property model (corrected)

**Operator-approved pattern** (supersedes ZPM-WEB-POL-01):

```text
same hostname (bzpm.ru)
one Website entity (WEB-ZPM-01 — active)
multiple Projects (PRJ-0009 active + PRJ-0010 deprecated)
Triumph precedent: WEB-0006 + PRJ-0004 + PRJ-0006
```

| Layer | Current delivery | Historical delivery |
|-------|------------------|---------------------|
| **Project** | PRJ-0009 **active** | PRJ-0010 **deprecated** |
| **Website** | WEB-ZPM-01 **active** | *(none — history via Project)* |

| Check | Verdict |
|-------|---------|
| Mint WEB-ZPM-02 as historical Website | **Rejected** — COR-ZPM-WEB-01 |
| Merge PRJ-0010 into WEB-ZPM-01 lifecycle | **N/A** — class boundary preserved |
| Single hostname = single Website | **Pass** — EIR-W01 |
| Deprecated project + active website on same hostname | **Pass** — PRJ-0010 deprecated + WEB-ZPM-01 **active** (W3-LC-05 / Triumph REL-0027) |
| Multi-Project BELONGS_TO on one Website | **Pass** — REL-ZPM-WB-01 + REL-ZPM-WB-03 |

**Attestation ordering:** **AT-W4-ZPM-01 only** — single Website tranche.

---

## 7. Lifecycle decisions

| Rule | Application in Wave 4 ZPM |
|------|---------------------------|
| Live / ongoing client property → **active** | **WEB-ZPM-01** — catalog platform WIP |
| Completed historical delivery line → **deprecated Project** | **PRJ-0010** — not Website lifecycle |
| No CMS/deploy vocabulary at lifecycle | Structural lifecycle only (LC-BAN-01) |
| Same hostname = single Website | **EIR-W01** — one WEB-ZPM-01 |
| Website without attested org at **active** | **Not applicable** — ORG-0005 **active** (AT-W1B-01) |
| Hostname on Domain in Wave 5 | `bzpm.ru` → **DOM-*** → WEB-ZPM-01 **PRIMARY_DOMAIN** singleton |

---

## 8. Explicit exclusions (not in population set)

### 8.1 Relationship and edge exclusions (operator binding)

| Item | Treatment |
|------|-----------|
| Website → Project **BELONGS_TO** | **Not created** — Wave 4B-ZPM |
| Organization → Website **OWNS** / **OPERATES** | **Not created** — Wave 4B-ZPM |
| Domain → Website **PRIMARY_DOMAIN** / **SECONDARY_DOMAIN** | **Not created** — Wave 5 / 6C |
| Domain entities (`DOM-*`) | **Not created** — Wave 5 ZPM |
| REL-0016 **CLIENT_OF** ORG-0005 → ORG-0001 | **Deferred** — Wave 6 |
| Person ↔ Website edges | **Not created** |
| **WEB-ZPM-02** mint / attestation | **Forbidden** — COR-ZPM-WEB-01..05 |

### 8.2 Rejected candidates

| rejected_label | description | basis |
|----------------|-------------|-------|
| REJ-ZPM-WEB-01 | WEB-ZPM-02 historical Website mint | COR-ZPM-WEB-01; EIR-W01 |
| REJ-ZPM-WEB-02 | BZPM / SITE-001 OpenCart dealership property | COR-W1B-03; EFV-02 |
| REJ-ZPM-WEB-03 | `bzpm.ru` hostname as Organization | Entity taxonomy §3 |
| REJ-ZPM-WEB-04 | BZPM as separate Organization | Identity rule §2 |
| REJ-ZPM-WEB-05 | Dataset v0.4 draft Website rows | No ZPM Website rows |
| REJ-ZPM-WEB-06 | Staging / dev hostnames | EIR-W03 — staging excluded |
| REJ-ZPM-WEB-07 | Dual-generation Website policy ZPM-WEB-POL-01 | **Superseded** — operator decision |

### 8.3 Future candidates — hold

| intake_label | description | verdict |
|--------------|-------------|---------|
| ZPM-INTAKE-FUT-01..04 | SEO / advertising / AI / OCPilot | **Hold** — no Website mint without Project start evidence |

---

## 9. Duplicate review

| review_id | Signal | Analysis | Verdict | Blocking |
|-----------|--------|----------|---------|----------|
| **ZPM-WEB-D-01** | WEB-ZPM-01 vs WEB-ZPM-02 — same hostname `bzpm.ru` | Second Website for same property | **Fail** — WEB-ZPM-02 retired; COR-ZPM-WEB-11 | No *(resolved)* |
| **ZPM-WEB-D-02** | WEB-ZPM-01 vs PRJ-0009 | Website vs Project class boundary | **Class boundary** — complementary | No |
| **ZPM-WEB-D-03** | WEB-ZPM-01 vs PRJ-0010 | Historical delivery at Project layer | **Class boundary** — BELONGS_TO at 4B | No |
| **ZPM-WEB-D-04** | vs Triumph WEB-0006..0009 | Different org ORG-0005 vs ORG-0004 | **Distinct org context** | No |
| **ZPM-WEB-D-05** | vs SITE-001 / SIBCAR | Engagement context revoked | **Reject** — COR-W1B-03 | No |
| **ZPM-WEB-D-06** | Canonical name «bzpm.ru» | Single property name | **Resolved** — one Website | No |
| **ZPM-WEB-D-07** | ЗПМ / BZPM / bzpm.ru as org conflict | Alias discipline — RN-W1B-01 | **Not duplicate** — single ORG-0005 | No |
| **ZPM-WEB-D-08** | Merge with core WEB-0006 namespace | Distinct tranche ids WEB-ZPM-* | **Pass** — namespace separation | No |

**Duplicate review summary:** **Pass** — one Website record; WEB-ZPM-02 rejected.

---

## 10. Candidate relationships for Wave 4B-ZPM

**Not created in Wave 4 ZPM.** Prepared for separate Wave 4B-ZPM population pass after Website attestation.

### 10.1 Website → Project BELONGS_TO

| Draft rel_id | source_website | target_project | Prerequisite | Notes |
|--------------|----------------|----------------|--------------|-------|
| **REL-ZPM-WB-01** | WEB-ZPM-01 bzpm.ru | PRJ-0009 Каталог-платформа bzpm.ru | WEB-ZPM-01 **active**; PRJ-0009 **active** | Current delivery grouping |
| **REL-ZPM-WB-03** | WEB-ZPM-01 bzpm.ru | PRJ-0010 Сайт bzpm.ru (исходная версия) | WEB-ZPM-01 **active**; PRJ-0010 **deprecated** | Historical grouping — analog REL-0027 |

**Cancelled:**

| Draft rel_id | Reason |
|--------------|--------|
| **REL-ZPM-WB-02** | COR-ZPM-WEB-06 — WEB-ZPM-02 retired |

**Steward policy (corrected):** Multi-Project BELONGS_TO on **one** Website — Triumph precedent; cross-generation WEB-ZPM-01 → PRJ-0010 **required** (not rejected).

### 10.2 Organization → Website OWNS *(deferred — not in Wave 4)*

| Draft rel_id | source_organization | target_website | Type | Notes |
|--------------|---------------------|----------------|------|-------|
| *(TBD)* | ORG-0005 ЗПМ | WEB-ZPM-01 | **OWNS** | Client org owns sole property |
| *(TBD)* | ORG-0001 Полигон | WEB-ZPM-01 | **OPERATES** | Execution context — steward choice |

### 10.3 Domain → Website PRIMARY_DOMAIN *(Wave 5 prerequisite)*

| Hostname | target_website | Type | Wave |
|----------|----------------|------|------|
| bzpm.ru | WEB-ZPM-01 | **PRIMARY_DOMAIN** | **Wave 5B ZPM** — singleton (SU-W4-ZPM-03 **resolved**) |

**Wave 4B-ZPM ordering note:** BELONGS_TO may proceed after Website attestation; OWNS requires ORG-0005 **active** (met) + Website endpoint attested; PRIMARY_DOMAIN requires **DOM-*** mint at Wave 5 ZPM.

---

## 11. SAFE UNKNOWN inventory

| ID | Topic | Impact | Posture | Blocks population |
|----|-------|--------|---------|-------------------|
| **SU-ZPM-PRJ-03** | Deployment replace vs coexistence on `bzpm.ru` | Wave 4B BELONGS_TO pairing | **Resolved structurally** — single Website | **No** |
| **SU-W3B-ZPM-01** | Dual BELONGS_TO for same hostname | Wave 4B steward policy | **Resolved** — REL-ZPM-WB-01 + REL-ZPM-WB-03 on WEB-ZPM-01 | **No** |
| **SU-ZPM-PRJ-08** | Production domain registrant ORG-0005 | Wave 5 DOM-* | **SAFE UNKNOWN** (ME-W1B-03 carry-forward) | **No** |
| **SU-ZPM-PRJ-01** | Historical contract / act dates | PRJ-0010 precision | **SAFE UNKNOWN** — operator «~5 years» narrative | **No** |
| **SU-ZPM-PRJ-02** | Formal acceptance document | E1 upgrade path | **SAFE UNKNOWN** — E0 sufficient | **No** |
| **SU-ZPM-PRJ-07** | CLIENT_OF ORG-0005 → ORG-0001 | Commercial graph | **Wave 6** | **No** |
| **SU-W4-ZPM-01** | Live URL probe timestamp for `bzpm.ru` | E1 upgrade optional | **SAFE UNKNOWN** — E0 operator path sufficient | **No** |
| **SU-W4-ZPM-02** | OWNS on deprecated Website | Wave 4B policy | **Obviated** — no deprecated Website | **No** |
| **SU-W4-ZPM-03** | Single DOM-* vs dual generation | Wave 5 | **Resolved** — DOM-* → WEB-ZPM-01 only | **No** |

**Blocking gaps remaining:** **None**

---

## 12. Foundation consistency

| Foundation doc | Wave 4 ZPM alignment |
|----------------|------------------------|
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4 Website | Web property identity — not deploy/CMS — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-W01..W04 | One property per hostname — **yes** |
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4 | Brand titles as aliases; hostname on DOM — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | **active** Website + **deprecated** Project — **yes** |
| [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](../foundation/ATLAS-LIFECYCLE-TRANSITIONS-v1.md) W3-LC-05 | PRJ-0010 deprecated + WEB-ZPM-01 **active** — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | E0 operator structural path — **yes** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) | Wave 4 after Project; org context available — **yes** |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | Multi-Project BELONGS_TO allowed — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **yes** |
| EFV-03 | Two-phase rule at **Project** layer only — **yes** (COR-ZPM-WEB-12) |

**No new entity types.** **No foundation modifications.** **No relationship edges created.**

---

## 13. Readiness verdict

```text
READY FOR WAVE 4 ZPM WEBSITE ATTESTATION — SINGLE WEBSITE (WEB-ZPM-01 ONLY)
```

**Conditions:**

1. Steward executes attestation tranche **AT-W4-ZPM-01** (WEB-ZPM-01 **active**) only.
2. **Do not** execute AT-W4-ZPM-02 — WEB-ZPM-02 retired (COR-ZPM-WEB-05).
3. Wave 4B-ZPM relationship population executes in a **separate pass** — REL-ZPM-WB-01 + REL-ZPM-WB-03 queued; REL-ZPM-WB-02 cancelled.
4. ORG-0005 canonical **ЗПМ**; **BZPM** remains alias only — no new Organization.
5. FUT-01..04 remain **hold**; SIBCAR/SITE-001 narratives remain **rejected** per COR-W1B-03.

---

## 14. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | Canonical website roster table |
| [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) | Attestation sequence and package verdict |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Correction execution record |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | COMMISSIONED_BY / EXECUTES context |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |

---

*ATLAS Wave 4 ZPM Website Population v1 — documentation only; WEB-ZPM-01 minted as **proposed** pending attestation act; corrected 2026-06-07.*
