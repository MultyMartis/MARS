# ATLAS Wave 1D Shpigovsky Organization Attestation v1

**Status:** **documented** — Wave 1D Shpigovsky Organization attestation sequence, evidence gates, readiness verdict.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md) · [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md)  
**Is not:** attestation runtime, signature platform, Legal Entity attestation, Person population, relationship creation.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations (ORG-0001..0004): **COMPLETE**
- Wave 1B ЗПМ (ORG-0005): **active** — unchanged
- Wave 1C SIBCAR (ORG-0006): **active** — unchanged
- Wave 1D Makita (ORG-0007): **active** — unchanged
- Shpigovsky intake: **complete** — EV-SHPIG-OP-01; EV-SHPIG-WEB-01..02
- Counterparty Card: **absent** — Category A operational-public path authorized

---

## 1. Purpose

Зафиксировать **порядок attestation** для Wave 1D Organization **ООО «Сознание»** under **Operational Organization Evidence Path (OOEP)**: evidence gates, layer separation, brand/organization discipline, downstream deferrals, и **итоговый verdict**.

**Attestation contract** ([ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1):

> Nothing is canonical until a qualified human attests under documented evidence discipline.

**Layer contract (Wave 1D):**

> Organization **active** at E1/E2 operational-public tier **does not** attest Legal Entity. Legal Entity remains **SAFE UNKNOWN**.

---

## 2. Wave 1D attestation scope

| In scope | Out of scope |
|----------|--------------|
| Organization ORG-0008 → **active** at **E1/E2 operational-public** | Legal Entity LE-* |
| Operational-public evidence tier assignment | Person entities (PER-*) |
| Duplicate review sign-off (display-name / class boundary) | Project entities (PRJ-*) |
| Category A Polygon / OOEP gate closure | Website / Domain entities (WEB-* / DOM-*) |
| Brand notes (Шпиговский Дом) — no separate Organization | Relationship edges (REL-*) |
| Supersede intake-only hold for Organization layer | CLIENT_OF ORG-0008 → ORG-0001 (Wave 6+) |
| Explicit SAFE UNKNOWN legal fields | Foundation amendments |
| | Runtime / API / database |
| | Separate Organization for brand |

---

## 3. Attestation readiness

| org_id | Organization | Target state | Min tier (W1-D) | Readiness | Blocker |
|--------|--------------|--------------|-----------------|-----------|---------|
| ORG-0008 | ООО «Сознание» | **active** | **E1/E2** (operational-public) | **Ready** | — |
| LE-* | *(none)* | **not created** | E1+ required | **Deferred** | CC absent — **expected** |

**Readiness legend:**

- **Ready (active)** — OOEP operational-public signals satisfy Category A extension; steward attestation authorized at E1/E2.
- **Deferred (Legal Entity)** — LE-* creation **prohibited** until E1+ documentary evidence with identifiers — **not** a blocker for Organization **active**.

---

## 4. Attestation sequence

### 4.1 Tranche AT-W1D-SHPIG-00 — Population record

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Verify ORG-0001..0007 **unchanged** | Steward | Prior wave registers | **Done** |
| 2 | Classify Category A — Polygon client | Steward | OOEP Category A extension | **Done** |
| 3 | Inventory operational-public evidence | Steward | EV-SHPIG-OP-01; EV-SHPIG-WEB-01..02 | **Done** |
| 4 | Duplicate batch W1D-SHPIG-D-01..09 | Steward | Population §7 | **Done** |
| 5 | Propose ORG-0008 canonical name **ООО «Сознание»** | Steward | EV-SHPIG-WEB-02 | **Done** |
| 6 | Record brand notes — **Шпиговский Дом**; no separate org | Steward | EV-SHPIG-WEB-01 | **Done** |
| 7 | Record legal fields **SAFE UNKNOWN** | Steward | OOEP layer separation | **Done** |
| 8 | Register website / domain **candidates only** | Steward | Register §6 | **Done** |
| 9 | Confirm i-SEO project channel **excluded** | Steward | EV-SHPIG-OP-01 | **Done** |

### 4.2 Tranche AT-W1D-SHPIG-01 — Active attest (Organization layer)

| Step | Action | Attestor | Evidence ref | Status |
|------|--------|----------|--------------|--------|
| 1 | Confirm OOEP operational signals ≥2 | Steward | EV-SHPIG-OP-01; EV-SHPIG-WEB-01..02 | **Done** |
| 2 | Confirm E2 public legal-operator signal present | Steward | EV-SHPIG-WEB-02 | **Done** |
| 3 | Confirm no LE-* mint attempted | Steward | STOP-OOER-02 | **Done** |
| 4 | Duplicate review sign-off (distinct from ORG-0001..0007) | Steward | W1D-SHPIG-D-01..08 | **Done** |
| 5 | Attest Organization ORG-0008 **active** at **E1/E2 operational-public** | Steward (delegated) or Owner | OAR-HUM-01 | **Done** |
| 6 | Record Legal Entity **SAFE UNKNOWN** — no LE attestation | Steward | OOEP §4 | **Done** |

**Category A operational-public authorization:** CC absence **does not** block step 5 when E1/E2 public evidence and operator delivery context satisfy OOEP gates per approved policy extension.

---

## 5. Evidence gates

| Gate ID | Rule | ORG-0008 status |
|---------|------|-----------------|
| **W1D-SHPIG-EG-01** | Category A Polygon client — operational-public path | **Pass** — EV-SHPIG-OP-01; EV-SHPIG-WEB-01..02 |
| **W1D-SHPIG-EG-02** | OOEP operational signals ≥2 | **Pass** — five signals documented |
| **W1D-SHPIG-EG-03** | E2 public legal-operator corroboration | **Pass** — EV-SHPIG-WEB-02 |
| **W1D-SHPIG-EG-04** | No hostname-only org (OOER-05) | **Pass** — delivery relationship + work scope cited |
| **W1D-SHPIG-EG-05** | Duplicate batch before **active** | **Pass** — W1D-SHPIG-D-01..09 |
| **W1D-SHPIG-EG-06** | Human attest mandatory (OAR-HUM-01) | **Pass** — AT-W1D-SHPIG-01 |
| **W1D-SHPIG-EG-07** | Legal Entity fields not invented | **Pass** — all **SAFE UNKNOWN** |
| **W1D-SHPIG-EG-08** | No REL-* inferred from service context (OOER-06) | **Pass** |
| **W1D-SHPIG-EG-09** | LE-* not created without E1+ identifiers (STOP-OOER-02) | **Pass** |
| **W1D-SHPIG-EG-10** | No separate Organization for brand | **Pass** — brand notes only |
| **W1D-SHPIG-EG-11** | i-SEO project channel excluded | **Pass** — EV-SHPIG-OP-01 |

---

## 6. Attested Organization record

### 6.1 ORG-0008 — ООО «Сознание»

| Field | Value |
|-------|-------|
| **org_id** | ORG-0008 |
| **canonical_name** | **ООО «Сознание»** |
| **lifecycle_state** | **active** |
| **wave_tier** | W1-D |
| **classification** | **Polygon client** |
| **business_role** | **CLIENT** |
| **legal_entity_id** | **SAFE UNKNOWN** |
| **evidence_tier** | **E1/E2** *(operational-public)* |
| **brand_notes** | **Шпиговский Дом** = brand; **ООО «Сознание»** = organization |
| **attestation_ref** | **AT-W1D-SHPIG-01** |
| **attestation_date** | 2026-06-10 |

### 6.2 Legal Entity — not attested

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
| **LE-* id** | **none** — not created |

---

## 7. Missing evidence register (non-blocking for Organization active)

| ID | Topic | Severity | Blocks org active? | Mitigation |
|----|-------|----------|-------------------|------------|
| ME-W1D-SHPIG-01 | Legal entity form | **Deferred** | **No** | Future CC wave |
| ME-W1D-SHPIG-02 | INN / KPP / OGRN | **Deferred** | **No** | Future CC wave |
| ME-W1D-SHPIG-03 | Legal vs trade name (Сознание ↔ Шпиговский Дом) | **Deferred** | **No** | Future CC wave |
| ME-W1D-SHPIG-04 | CC folder absent | **Expected** | **No** | Category A operational-public path |
| ME-W1D-SHPIG-05 | Contract data | **Deferred** | **No** | Future commercial wave |
| ME-W1D-SHPIG-06 | Ownership structure | **Deferred** | **No** | Future CC |
| ME-W1D-SHPIG-07 | Internal contacts | **Deferred** | **No** | Future CC / steward |
| ME-W1D-SHPIG-08 | Primary website (display) | Low | **No** | Wave 4 |
| ME-W1D-SHPIG-09 | Commercial CLIENT_OF edges | Medium | **No** | Wave 6+ |
| ME-W1D-SHPIG-10 | Delivery phase | Low | **No** | Wave 3 |
| ME-W1D-SHPIG-11 | Person mint (Шпиговский С.Ю.; client contacts) | Low | **No** | Wave 2 |

---

## 8. Foundation consistency check

| Check | Result |
|-------|--------|
| No new entity types | **Pass** |
| No Foundation modification | **Pass** |
| ORG-0001..0007 unchanged | **Pass** |
| Makita (ORG-0007) intact | **Pass** |
| ZPM (ORG-0005) intact | **Pass** |
| SIBCAR (ORG-0006) intact | **Pass** |
| No merge operations | **Pass** |
| No LE-* creation | **Pass** |
| No PER-* / WEB-* / DOM-* / PRJ-* / REL-* mint | **Pass** |
| No graph redesign | **Pass** |
| OOEP / Category A operational-public rules followed | **Pass** |
| SAFE UNKNOWN — no invented legal identifiers | **Pass** |
| Brand/org separation enforced | **Pass** |
| Documentation only | **Pass** |

---

## 9. Downstream readiness (post-attestation)

| Wave | Candidate | Prerequisite | Status |
|------|-----------|--------------|--------|
| Legal Entity | LE-* TBD | E1+ CC or E2 registry extract with identifiers | **Deferred** |
| Wave 2 | PER-* client representatives | Separate Person wave decision | **Not authorized** |
| Wave 3 | PRJ-* «Сайт shpigovsky.ru» | ORG-0008 **active** | **Unblocked** — candidate registered at intake |
| Wave 3B | EXECUTES / COMMISSIONED_BY | Project + org endpoints | **Deferred** |
| Wave 4 | WEB-* shpigovsky.ru paths | ORG-0008 **active** | **Unblocked** — candidates registered |
| Wave 5 | DOM-* shpigovsky.ru | Wave 4 + registrar E1 | **Deferred** |
| Wave 6+ | REL-* CLIENT_OF | Commercial review | **Deferred** |

---

## 10. Verdict options

| Verdict | Meaning |
|---------|---------|
| **NO EVIDENCE FOUND** | Operational-public signals insufficient |
| **NOT READY** | Population or duplicate review failed |
| **INTAKE ONLY** | Superseded posture — **not selected** |
| **ACTIVE ORGANIZATION — Operational Evidence Path** | ORG-0008 **active** at E1/E2; Legal Entity **SAFE UNKNOWN** |

---

## 11. Verdict

```text
ACTIVE ORGANIZATION
Operational Evidence Path
Legal Entity: SAFE UNKNOWN
```

**Conditions:**

1. **ORG-0008 ООО «Сознание»** attested **active** at evidence tier **E1/E2 operational-public** under Category A Polygon / OOEP.
2. Classification: **Polygon client** — delivery via ORG-0001 Полигон channel; i-SEO project classification **excluded**.
3. **Legal Entity not attested** — INN, KPP, OGRN, legal signatory, EDO, ownership, contract data, internal contacts remain **SAFE UNKNOWN**; **no LE-* created**.
4. **Шпиговский Дом** recorded as **brand** only — **no** separate Organization minted.
5. Prior **INTAKE ONLY / AWAITING CC** posture **superseded** for Organization layer — CC remains path for **future Legal Entity wave**, not Organization existence.
6. ORG-0001..0007, Makita, ZPM, SIBCAR — **unchanged**; no merge; no relationships; no projects.

**Not selected:**

| Verdict | Reason |
|---------|--------|
| **NO EVIDENCE FOUND** | Five operational signals + E2 public corroboration |
| **NOT READY** | OOEP gates and duplicate review pass |
| **INTAKE ONLY** | Superseded by Wave 1D population |
| **READY FOR LEGAL ENTITY POPULATION** | CC absent — LE deferred |

---

## 12. Package lineage

```text
Shpigovsky Intake (INTAKE ONLY) ──► superseded for Organization layer
        │
        ▼
Wave 1D Shpigovsky Population (AT-W1D-SHPIG-00) ──► ORG-0008 proposed fields
        │
        ▼
Wave 1D Shpigovsky Attestation (THIS PACKAGE — AT-W1D-SHPIG-01) ──► ORG-0008 active
        │
        ▼
Future CC arrival ──► Legal Entity wave (LE-* TBD)
Future Wave 2–6 ──► Person / Project / Website / Domain / Relationships
```

---

## 13. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-POPULATION-v1.md) | Population plan |
| [ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md](ATLAS-WAVE1D-SHPIGOVSKY-ORGANIZATION-REGISTER-v1.md) | Register row |
| [ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md](ATLAS-OPERATIONAL-ORGANIZATION-EVIDENCE-RULE-v1.md) | Category A operational-public path |
| [ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md](ATLAS-SHPIGOVSKY-INTAKE-ANALYSIS-v1.md) | E0/E2 evidence source |

---

*ATLAS Wave 1D Shpigovsky Organization Attestation v1 — documentation only.*
