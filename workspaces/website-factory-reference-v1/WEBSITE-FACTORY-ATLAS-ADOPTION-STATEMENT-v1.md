# Website Factory — ATLAS Adoption Statement v1

**Версия:** v1  
**Дата:** 2026-06-07  
**Область:** `workspaces/website-factory-reference-v1/` ↔ ATLAS (`projects/atlas/`)  
**Тип:** adoption statement only — **без** runtime, integration implementation, schema design, Creation Era authorization  
**Upstream:** [WEBSITE-FACTORY-ATLAS-INTEGRATION-AUDIT-v1.md](WEBSITE-FACTORY-ATLAS-INTEGRATION-AUDIT-v1.md), [WEBSITE-FACTORY-ATLAS-ADOPTION-ALIGNMENT-PASS-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-ALIGNMENT-PASS-v1.md)  
**ATLAS references:** [ATLAS-CONSUMER-CONTRACTS-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CONTRACTS-v1.md) §8.3, [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md), [ATLAS-CONSUMER-CERTIFICATION-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CERTIFICATION-v1.md)

---

## Purpose

**WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1** формально фиксирует позицию Website Factory как **ATLAS consumer**: Factory **потребляет** canonical business reality как **references** и **никогда** не становится параллельным business registry.

Это **alignment artifact**, не redesign и не новый architecture layer.

---

## ATLAS Canonical Ownership (Accepted)

Website Factory **принимает**, что ATLAS является **canonical owner** следующих классов business reality:

| Domain | ATLAS owns | Factory posture |
|--------|------------|-----------------|
| **Organization** | Canonical identity (`ORG-*`), name, aliases, lifecycle | **Reference only** — Legal Entity Card = production input, not registry |
| **Person** | Canonical identity (`PER-*`), multi-org participation | **Reference only** — charter-bound mentions in Legal Pack |
| **Website** | Web property identity (`WEB-*`) — brand/site concept | **Reference only** — Factory produces build artifacts; ATLAS identifies |
| **Project** | Structural initiative container (`PRJ-*`) — **not** PM | **Reference only** — Factory Project = separate production case id |
| **Relationship** | First-class typed edges (`REL-*`) | **Read / suggest** — never silent canonical write |
| **Client reality** | Organization + `CLIENT_OF` / `COMMISSIONED_BY` — **not** separate entity | **Reference only** — external actor via charter-bound refs |

**Normative rule ADOPT-01:** Factory **must not** fork canonical org/person/website/project/relationship lists (CC-P04, CC-02).

**Normative rule ADOPT-02:** Factory **produces** sites; ATLAS **identifies** them ([ATLAS-CONSUMER-CONTRACTS-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CONTRACTS-v1.md) §8.3).

---

## Factory Ownership (Preserved)

Website Factory **остаётся owner** operational production reality одного Factory Project:

| Concern | Factory owns |
|---------|--------------|
| Factory Project identity shell | Logical production case — distinct from `PRJ-*` |
| Production state instance | Runtime 14-state progression, gate/handoff indexes |
| Physical artifact bindings | POC/MOC/ROC/SOC classes per physical specs |
| Legal Entity Card | Production-support artifact for legal workflow |
| Layer artefact refs, scope freeze, closure metadata | Engine indexes — not business registry |

Factory **не претендует** на canonical business identity registry.

---

## ATLAS Reference Convention (RC-01)

Normative **field naming convention** for charter / MOC-12 / POC-09 bindings — **convention only**, без serialization и без schemas:

| Field name | ATLAS id pattern | Semantics |
|------------|------------------|-----------|
| `atlas_client_org_ref` | `ORG-*` | Commissioning / client organization |
| `atlas_person_ref` | `PER-*` | Person identity when charter-bound |
| `atlas_website_ref` | `WEB-*` | Structural website identity |
| `atlas_project_ref` | `PRJ-*` | Structural ATLAS project — **not** Factory Project id |
| `atlas_relationship_ref` | `REL-*` | Structural relationship edge when relevant |
| `atlas_domain_ref` | `DOM-*` | Domain identity when relevant |

### Disposition rules

| Condition | Required posture |
|-----------|------------------|
| Active attested canonical exists | Field **SHOULD** be populated (ref only) |
| Unknown or disputed ownership | Explicit **SAFE UNKNOWN**; **MUST NOT** invent OWNER/ORG (IGV 9.3) |
| No ATLAS population yet | Field absent or marked proposed; **MUST NOT** fork parallel registry |
| Factory Project identity (MOC-02) | **MUST remain distinct** from `atlas_project_ref` |

**Normative rule REF-01:** ATLAS refs are **pointers**, not authoritative identity restatement inside Factory records.

---

## Legal Entity Card ↔ Counterparty Card Crosswalk (RC-02)

| Artifact | Authority | Role |
|----------|-----------|------|
| **ATLAS Counterparty Card** | Evidence only — **not** canonical record | Supports Organization proposal → attestation → `ORG-*` |
| **ATLAS Organization (`ORG-*`)** | Canonical business identity | Wins on identity conflict |
| **Legal Entity Card (LEC)** | Production SoT for **legal production workflow only** | Templates, Input Sheet, footer — **not** business registry |

```text
Counterparty Card (ATLAS evidence)
       │ propose / attest
       ▼
ORG-* (ATLAS canonical) ◀──ref── Legal Entity Card (Factory production)
       │
       └── LEC holds production fields; ORG-* wins on identity conflict
```

**Normative rule LEC-01:** Legal Entity Card creation **follows** RC-02 crosswalk — production input, not registry entry.

**Normative rule LEC-02:** When `ORG-*` is attested, LEC **SHOULD** cite `atlas_org_ref` and optional `counterparty_evidence_ref`.

Details: [legal-entity/LEGAL-ENTITY-CARD-v1.md](legal-entity/LEGAL-ENTITY-CARD-v1.md) § ATLAS crosswalk.

---

## Terminology Guards (RC-03)

| Term (Factory) | Term (ATLAS) | Guard |
|----------------|--------------|-------|
| **Factory Project** | **ATLAS Project** (`PRJ-*`) | Homonym — **different entities**. Factory Project = one production case; ATLAS Project = structural initiative container. |
| **Factory Registry** (ROC portfolio) | **ATLAS Business Reality Registry** | Homonym — **different domains**. Factory Registry catalogs Factory Projects; ATLAS Registry catalogs business entities. |
| **Factory Identity** (MOC-02 / POC-01 shell) | **ATLAS Identity** (`ORG-*`, `PER-*`, …) | Homonym — **different authority**. Factory identity = production case shell; ATLAS identity = canonical business facts. |

**Normative rule TG-ATLAS-01:** Operator **must not** conflate homonyms in charter, manifest, or enrollment without explicit disambiguation.

**Existing guard preserved:** Site Type Registry ≠ Factory Project Registry (RAP-11) — unrelated to ATLAS; remains in force.

---

## ATLAS-First Enrollment Discipline (RC-05)

Before populating scope categories (MOC-03 / charter) with **org-identifying facts** (`legal_name`, `inn`, client org name as identity):

1. Check ATLAS population / steward for active `ORG-*`, `WEB-*`, `PRJ-*` for this case.
2. If active canonical exists → bind refs in MOC-12 (RC-01 fields); MOC-03 carries **production scope**, not canonical identity.
3. If unknown → **SAFE UNKNOWN**; do not invent OWNER or parallel org registry row.
4. Legal Entity Card creation follows RC-02 crosswalk.

**Normative rule ENROLL-ATLAS-01:** When organization already exists in ATLAS — **reference first, copy second**. New business facts **never** become primary inside Factory.

Details: [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) § ATLAS-first enrollment.

---

## Adoption Level — C1 Attestation

Per [ATLAS-CONSUMER-CERTIFICATION-v1.md](../../projects/atlas/foundation/ATLAS-CONSUMER-CERTIFICATION-v1.md):

| Criterion | Evidence in this statement |
|-----------|------------------------------|
| **C0** — Aware, no parallel canonical list | ADOPT-01; Engine boundary EO-02 |
| **Adoption owner named** | **Website Factory program operator** (Factory-scoped; ATLAS steward validates C2+) |
| **Semantic contract accepted** | ADOPT-02; link to ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1 |
| **Phase 4 consumer contracts acknowledged** | ADOPT-02; ATLAS-CONSUMER-CONTRACTS-v1 §8.3 |
| **No MAP-B01–B09 in documented design** | Integration audit confirms no fork authorization |
| **Business Scope ≠ identity partition** | Factory scope = production case; ATLAS scope = business identity |

**Declared adoption level:** **C1 — Aligned** (documentation consumer).

**Target (future, not claimed here):** C2 — published mapping table, steward review.

---

## Related Factory Documents

| Document | RC coverage |
|----------|-------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | RC-03 terminology guards; pointer to this statement |
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | RC-01 Category 7 ATLAS ref convention |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | RC-05 ATLAS-first enrollment |
| [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md) | RC-01 MOC-12 / OBL-M-12 |
| [legal-entity/LEGAL-ENTITY-CARD-v1.md](legal-entity/LEGAL-ENTITY-CARD-v1.md) | RC-02 LEC ↔ CC crosswalk |

---

## Explicit Non-Claims

This adoption statement **does not** claim:

- Website Factory **runtime**, workflow engine, automation, validator, or dashboard **exist**
- ATLAS **runtime**, API, database, or live attestation service **exist** in-repo
- **Mechanical** ATLAS integration is MVP-required — explicitly deferred per topology decision
- **C2 or C3** certification — C1 attestation only
- Field **serialization**, JSON/YAML schemas, or storage paths for `atlas_*_ref` fields
- Legal Entity Card and Counterparty Card **are synchronized** automatically
- This statement **authorizes** Creation Era or physical artifact creation — separate authorization governs execution

**Physical artifact note (documentation drift correction):** Factory structured records under `workspaces/website-factory-operations/` **exist on disk** per Wave 1–3 execution records. That operational fact is **not** asserted or governed by this C1 adoption statement — see `workspaces/website-factory-operations/WAVE-*-PHYSICAL-ARTIFACT-CREATION-EXECUTION-v1.md`.

**SAFE UNKNOWN:**

- Exact serialization of `atlas_*_ref` in MOC-12 — deferred to Creation Era operator choice under class separation rules
- Whether Triumph/manipulator wave records are **live attested canonical** on a service — population docs are documentation-level
- External Counterparty Card storage at `C:\AI MARS STORAGE\atlas\evidence\` — referenced by ATLAS, not verified here

---

*Website Factory ATLAS Adoption Statement v1 — adoption alignment only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md`. Last refreshed: 2026-06-07 — MVP certification remediation (F-05).*
