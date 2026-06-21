# ATLAS Wave 4 ZPM Website Register v1

**Status:** **documented** — canonical Website roster after Wave 4 ZPM population, model correction, and attestation (**active**; attestation complete).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07 · **sync:** 2026-06-07 (ZPM documentation sync)  
**Organization anchor:** ORG-0005 **ЗПМ**  
**Parent:** [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) · [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) · [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md)  
**Is not:** relationship registry, Domain registry, runtime export, database table, attested canonical export until attestation act completes.

---

## 1. Purpose

Канонический **реестр Website population** Wave 4 tranche **ZPM**. Одна строка — одна approved Website record для attestation.

**Register summary:**

| Metric | Count |
|--------|-------|
| Total in scope | **1** |
| Lifecycle **active** | **1** (WEB-ZPM-01) |
| Retired / not minted | **1** (WEB-ZPM-02 — COR-ZPM-WEB-01) |
| Relationship edges *(Wave 4B)* | **3** attested — REL-ZPM-WB-01, 03, 04 |
| Attestation | **Complete** — AT-W4-ZPM-01 |

---

## 2. Population roster — full table

| website_id | canonical_name | website_kind | url | primary_org_candidate | primary_project_candidate | evidence_tier | lifecycle_state | attestation_readiness | notes |
|------------|----------------|--------------|-----|----------------------|---------------------------|---------------|-----------------|----------------------|-------|
| WEB-ZPM-01 | bzpm.ru | corporate *(catalog platform)* | `https://bzpm.ru` | ORG-0005 ЗПМ | PRJ-0009 Каталог-платформа bzpm.ru | **E0** | **active** | AT-W4-ZPM-01 | Sole real web property for `bzpm.ru`; Triumph analog WEB-0006 |

**Display-only fields** (`primary_org_candidate`, `primary_project_candidate`) — superseded by attested Wave 4B edges REL-ZPM-WB-01, 03, 04.

**Retired (not in roster):**

| website_id | canonical_name | disposition | reason |
|------------|----------------|-------------|--------|
| WEB-ZPM-02 | bzpm.ru (исходная версия) | **rejected / not minted** | COR-ZPM-WEB-01 — historical delivery held by PRJ-0010 only |

---

## 3. Population roster — by lifecycle target

### 3.1 Active (1)

| website_id | canonical_name | website_kind | evidence_tier | attestation_readiness |
|------------|----------------|--------------|---------------|----------------------|
| WEB-ZPM-01 | bzpm.ru | corporate *(catalog platform)* | **E0** | **ready** |

### 3.2 Deprecated (0)

*No Website entities target **deprecated** lifecycle in corrected ZPM model. PRJ-0010 holds historical delivery at Project layer.*

---

## 4. Single-property multi-project index

| Hostname | website_id | website lifecycle | project_id | project lifecycle | BELONGS_TO *(Wave 4B queue)* |
|----------|------------|-------------------|------------|-------------------|------------------------------|
| `bzpm.ru` | WEB-ZPM-01 | **active** | PRJ-0009 | **active** | REL-ZPM-WB-01 **active** |
| `bzpm.ru` | WEB-ZPM-01 | **active** | PRJ-0010 | **deprecated** | REL-ZPM-WB-03 **active** |

**Policy:** One Website per hostname property; delivery generations live in **Project** layer (operator decision; Triumph precedent REL-0027/0028).

---

## 5. Aliases index (informational — not Wave 4 edges)

| website_id | aliases | alias_type |
|------------|---------|------------|
| WEB-ZPM-01 | Сайт ЗПМ; Каталог bzpm.ru; Bzpm.ru | display / brand |

**Historical delivery aliases** (PRJ-0010 narrative — not Website): «Исходный сайт bzpm.ru»; «WP + The7 generation».

**Organization aliases (not Website):** BZPM · ООО ЗПМ · Завод Пищевого Машиностроения → ORG-0005 **ЗПМ** per RN-W1B-01.

Hostname string `bzpm.ru` attaches to **Domain** entity in Wave 5 — not a substitute for Website canonical_name ([ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) §6.4).

---

## 6. Platform metadata (consumer context — non-lifecycle)

| website_id | platform (operator narrative) | consumer_program_refs |
|------------|--------------------------------|----------------------|
| WEB-ZPM-01 | Polygon catalog-platform delivery *(current)*; historical WP + The7 context via PRJ-0010 | — |

Platform metadata does **not** substitute for lifecycle attestation.

---

## 7. Excluded register (not in population set)

| Item | Reason | Belongs to |
|------|--------|------------|
| **WEB-ZPM-02** | Retired — COR-ZPM-WEB-01 | — |
| DOM-* `bzpm.ru` | Domain entity class | **Wave 5 ZPM** |
| REL-ZPM-WB-01, REL-ZPM-WB-03 BELONGS_TO | Relationship family | **Wave 4B-ZPM** |
| REL-ZPM-WB-02 | Cancelled — source Website retired | — |
| OWNS / OPERATES org↔website | Relationship family | **Wave 4B-ZPM** |
| PRIMARY_DOMAIN edges | Domain ↔ Website | **Wave 5B ZPM** |
| REL-0016 CLIENT_OF ORG-0005 → ORG-0001 | Org ↔ Org | **Wave 6** |
| Person ↔ Website edges | Out of operator scope | Future expansion |
| SITE-001 / SIBCAR dealership property | COR-W1B-03 rejected | — |
| BZPM as Organization | Alias only — ORG-0005 **ЗПМ** | Identity rule |
| Core Triumph WEB-0006..0009 | Distinct tranche — ORG-0004 | Core Wave 4 |

---

## 8. Evidence index (population references)

| Ref | Artifact | Routing *(corrected)* |
|-----|----------|----------------------|
| **EV-ZPM-OP-ACT-01** | Operator — current catalog rebuild | WEB-ZPM-01 · PRJ-0009 |
| **EV-ZPM-OP-HIST-01** | Operator — historical site delivery | **PRJ-0010 only** — BELONGS_TO context for WEB-ZPM-01 |
| **EV-W1B-CC-01** | `bzpm/Реквизиты.docx` §17 **Bzpm.ru** | WEB-ZPM-01 — indirect org corroboration |
| **AT-W1B-01** | ORG-0005 **active** | WEB-ZPM-01 — org anchor |
| **AT-W3-ZPM-01** | PRJ-0009 **active** | WEB-ZPM-01 — project pairing |
| **AT-W3-ZPM-02** | PRJ-0010 **deprecated** | PRJ-0010 — historical project; not Website mint |
| **AT-W3B-ZPM-01..02** | REL-ZPM-PJ-01..04 **active** | Commissioning / execution context |

**Primary evidence paths:**

```text
E0 operator — EV-ZPM-OP-ACT-01 (WEB-ZPM-01)
E0 operator — EV-ZPM-OP-HIST-01 (PRJ-0010 — Project layer only)
E1 CC — C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\bzpm\Реквизиты.docx
```

Evidence storage pointer: [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md).

---

## 9. Deferred register (Wave 5B+ and future)

| Item | Reason | Target wave |
|------|--------|-------------|
| DOM-* + **PRIMARY_DOMAIN** `bzpm.ru` → WEB-ZPM-01 | Hostname identity — singleton | **Wave 5B ZPM** |
| ORG-0001 **OPERATES** WEB-ZPM-01 | Execution operator context | **Wave 4B+** *(steward choice — SU-W4B-ZPM-01)* |
| REL-0016 CLIENT_OF | Commercial org edge | **Wave 6** |
| ZPM-INTAKE-FUT-01..04 | No start evidence | **Hold** |

**Completed (attested — see Wave 4B ZPM register):**

| Item | Attestation | Register |
|------|-------------|----------|
| REL-ZPM-WB-01 WEB-ZPM-01 → PRJ-0009 **BELONGS_TO** | Wave 4B ZPM | [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) |
| REL-ZPM-WB-03 WEB-ZPM-01 → PRJ-0010 **BELONGS_TO** | Wave 4B ZPM | Same |
| ORG-0005 **OWNS** WEB-ZPM-01 (REL-ZPM-WB-04) | Wave 4B ZPM | Same |

**Cancelled:**

| Item | Reason |
|------|--------|
| REL-ZPM-WB-02 | COR-ZPM-WEB-06 — WEB-ZPM-02 retired |
| ORG-0005 **OWNS** WEB-ZPM-02 | COR-ZPM-WEB-09 — target retired |
| AT-W4-ZPM-02 | COR-ZPM-WEB-05 — no Website to attest |

---

## 10. Namespace cross-check

| website_id namespace | Tranche | org anchor | Conflict |
|---------------------|---------|------------|----------|
| WEB-0001..0005 | Core Wave 4 — operator sites | ORG-0001..0003 | **None** — deferred |
| WEB-0006..0009 | Core Wave 4 — Triumph | ORG-0004 | **None** — distinct client |
| **WEB-ZPM-01** | **This register** | **ORG-0005 ЗПМ** | — |
| WEB-ZPM-02 | Retired id — not minted | — | IDP-03 — id unused |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-POPULATION-v1.md) | Per-website analysis and exclusions |
| [ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md](ATLAS-WAVE4-ZPM-WEBSITE-ATTESTATION-v1.md) | Attestation gates and verdict |
| [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | Correction execution record |
| [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | Project endpoints |
| [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md) | ORG-0005 canonical **ЗПМ** |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Core Wave 4 Triumph roster |

---

*ATLAS Wave 4 ZPM Website Register v1 — WEB-ZPM-01 **active**; WEB-ZPM-02 **retired / not minted**; synced 2026-06-07 per AT-W4-ZPM-01.*
