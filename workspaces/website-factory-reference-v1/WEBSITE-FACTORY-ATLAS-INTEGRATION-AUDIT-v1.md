# REPORT — Website Factory ATLAS Integration Audit v1

**Дата:** 2026-06-07  
**Тип:** integration audit only — **без** создания артефактов, **без** изменений существующих файлов, **без** integration documents  
**Область:** Website Factory (`workspaces/website-factory-reference-v1/`) ↔ ATLAS (`projects/atlas/`)  
**Метод:** review Foundation, Engine, charters, Operational Model, Playbooks 01–05, RT-G04/G05/G10/G12 Physical Artifact Specifications; ATLAS foundation + population; cross-references; keyword drift scan (ATLAS, Organization, Website, Project, Client, Business Reality, Registry, ownership, reference, canonical)

**Repo evidence:** оба корпуса — **documentation-first**; shipped Website Factory runtime и ATLAS runtime/API **отсутствуют** в репозитории.

---

## Executive Summary

**Вердикт:** Website Factory **может войти в Physical MVP Artifact Creation Era** без создания дублирующей canonical business reality, **при условии** соблюдения уже заложенных границ и **рекомендованных** уточнений до/во время первого physical bind.

**ATLAS остаётся canonical owner** бизнес-идентичности (Organization, Person, Website, Domain, ATLAS Project, Relationship). Website Factory владеет **операционной production reality** одного Factory Project: lifecycle state, gates, handoffs, artefact refs, legal production workflow, build/QA state.

**Ключевой риск дрейфа — не дублирование реестров, а параллельные артефакты org-фактов:** Factory **Legal Entity Card** vs ATLAS **Counterparty Card** — оба описывают юрлицо, но в разных доменах. Без явного crosswalk оператор может записать org-данные в Factory persistence **вместо** ссылки на `ORG-*`.

**Коррекции:** 3 рекомендации (см. Required Corrections) — **не блокируют** Creation Era, но снижают риск semantic fork при первых physical records.

| Вопрос | Ответ |
|--------|-------|
| Creation Era safe? | **Да — conditional GO** |
| ATLAS canonical? | **Да** |
| Corrections required? | **Рекомендованы, не блокирующие** |

---

## ATLAS Ownership Review

**Определение:** ATLAS = **Business Reality Registry** — cross-cutting registry infrastructure для canonical business identity and structure (`ATLAS-REALITY-MODEL-v1.md`).

> ATLAS maintains **who exists, what exists, and how things are related.** Other systems perform work.

### Ownership by entity class

| Entity | ATLAS owns | How ownership is expressed | Evidence |
|--------|------------|---------------------------|----------|
| **Organization** | Canonical identity (`ORG-*`), name, aliases, lifecycle | Structural edges: `Person ──OWNER──► Organization`; commercial client = `Organization ──CLIENT_OF──► Organization` | `ATLAS-ENTITY-TAXONOMY-v1.md`, `ATLAS-RELATIONSHIP-TAXONOMY-v1.md` |
| **Person** | Canonical identity (`PER-*`), multi-org participation | `EMPLOYEE`, `CONTRACTOR`, `OWNER`, `REPRESENTATIVE`, etc. | `ATLAS-IDENTITY-MODEL-v1.md` |
| **Website** | Web property identity (`WEB-*`) — brand/site concept, not deploy artifact | `Organization ──OWNS──► Website`; `Website ──BELONGS_TO──► Project` | `ATLAS-BOUNDARIES-v1.md` §6 |
| **Project** | Structural initiative container (`PRJ-*`) — **not** PM | `Organization ──OWNS──► Project`; `Project ──COMMISSIONED_BY──► Organization` | `ATLAS-ENTITY-TAXONOMY-v1.md` |
| **Relationship** | First-class typed edges (`REL-*`) | Cardinality: ≤1 active canonical per slot; disputed until resolved | `ATLAS-RELATIONSHIP-MODEL-v1.md` |
| **Client** | **Не отдельная сущность** | Client = **Organization** + `CLIENT_OF` или `COMMISSIONED_BY` | `ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md` |

### Canonical vs reference (ATLAS)

| Canonical | Reference / non-canonical |
|-----------|---------------------------|
| Active attested `ORG-*`, `PER-*`, `WEB-*`, `PRJ-*`, `DOM-*`, `REL-*` | Counterparty Cards (evidence only) |
| Human attestation + evidence tier E0–E3 | Consumer cache, proposals, `proposed`/`disputed` |
| | MIG SERP packs, MARS `project_id` rows, pilot folders |
| | Full evidence payloads (pointer only in ATLAS) |

**Consumer contract (Website Factory):** `ATLAS-CONSUMER-CONTRACTS-v1.md` §8.3:

> Factory **produces** sites; ATLAS **identifies** them.

| Typical read | Client Organization, Project, Website, Domain |
| Typical suggest | New website/domain when pack created |
| Must not | CMS content, product catalog as ATLAS entities |

**Prohibitions relevant to Factory:**

- CC-P04: fork canonical org/person lists
- CC-02: invent parallel canonical registry when ATLAS has no id
- IGV 9.3: **Website Factory must not assume owner org** when domain ownership uncertain
- REL prohibition: inventing canonical OWNER to unblock Factory export

**Population evidence:** Wave 3/4 registers document Triumph/manipulator case — `PRJ-0008` (Манипулятор), `WEB-0009` (manipulator-triumph.ru), `ORG-0004` (Триумф). MARS packs `mars-website-factory`, `triumph-manipulator-landing` **explicitly excluded** from ATLAS Project register (`ATLAS-WAVE3-PROJECT-REGISTER-v1.md` §5).

---

## Factory Ownership Review

**Определение:** Website Factory = production system для одного Website Factory production case — от intake до terminal `COMPLETE` (`FACTORY-PROJECT-OBJECT-MODEL-v1.md`).

### Ownership by concern

| Concern | Factory owns | Factory does NOT own |
|---------|--------------|---------------------|
| **Factory Project** | Logical production case: identity shell, state instance, gate outcomes, handoff events, artefact refs, scope freeze, audit trail | Class-level definitions (`site_type_code`, Runtime 14 states, gate criteria) |
| **Organization (business)** | — | Canonical `ORG-*`; Factory holds **Legal Entity Card** for legal production only |
| **Person** | — | Canonical `PER-*`; Person mentions in Legal Pack = production content |
| **Website (identity)** | Build artifacts, QA state, handoff packages, `src/` workspaces | Canonical `WEB-*`; SEO schema `Organization`/`LocalBusiness` = SEO layer |
| **Project (business)** | — | Canonical `PRJ-*`; Factory Project ≠ ATLAS Project |
| **Relationship** | Charter-bound refs to external systems (MIG, ORCA) | Canonical `REL-*` graph |
| **Client** | External actor; brief/SOW as intake trigger; approvals as **charter-bound refs only** | Canonical state source; closure trigger alone |

### Engine boundary (`FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md`)

| Rule | Statement |
|------|-----------|
| EO-01 | Engine owns **instance**, never **definition** |
| EO-02 | Engine owns **refs and records**, never **artefact bodies** |
| ER-06 | External workspace pointers — charter-declared refs only |
| ES-03 | Registry entry ID ≠ Factory Project identity |
| OA-ACT-03 | Client не является источником canonical state |

### Physical artifact planes (Creation Era target)

| Plane | Classes | Owns |
|-------|---------|------|
| **Substrate** (RT-G04) | LOC-ZONE, LOC-HOME, POC-01…10 | Factory record home, binding carriers, tracking indexes |
| **Manifest** (RT-G10) | MOC-01…12 | Per-project entry anchor, charter categories, reference topology |
| **Registry** (RT-G05) | ROC-01…11 | Portfolio catalog of **Factory Projects** |
| **Surface** (RT-G12) | SOC-01…11 | Read composition for eight operator questions |

**Terminology guard:** Factory **Site Type Registry** (`registry/SITE-TYPE-REGISTRY-v1.md`) = classification (`site_type_code`). Factory **Project Registry** (RT-G05) = portfolio of Factory Projects. **Neither** = ATLAS Business Reality Registry.

### Legal Entity layer — special case

`legal-entity/LEGAL-ENTITY-CARD-v1.md` declares Legal Entity Card as «Primary source of truth» **для legal production workflow** (Legal Input Sheet, templates). Это **Factory-scoped production SoT**, не ATLAS canonical org registry.

ATLAS Counterparty Card (`ATLAS-COUNTERPARTY-CARD-MODEL-v1.md`):

> A Counterparty Card is a **business reality evidence artifact** … **not canonical record itself**.

**Drift risk:** оба артефакта могут содержать `legal_name`, `inn`, `ogrn` для одного юрлица без автоматической связи.

---

## Overlap Analysis

### Namespace collision matrix

| Term | ATLAS meaning | Factory meaning | Collision? |
|------|---------------|-----------------|------------|
| **Project** | Structural client initiative (`PRJ-*`) | One production case (Engine logical unit) | **Yes — homonym**; documented in ATLAS, weak in Factory canon |
| **Registry** | Business Reality Registry | Site Type Registry + Factory Project Registry (ROC) | **Yes — homonym**; different domains |
| **Website** | Identity object (`WEB-*`) | Produced site / workspace / deploy target | **Partial** — Factory produces; ATLAS identifies |
| **Organization** | Canonical business unit | Legal Entity Card (production) | **Partial** — parallel facts, different authority |
| **Client** | Organization + relationship | External stakeholder | **Partial** — aligned if Client = org ref |
| **Canonical** | Human-attested business reality | Factory doctrine / Engine instance / per-plane SoT | **Yes — overloaded word**; context-dependent |

### Do Factory records duplicate ATLAS?

| Factory record plane | Duplicates ATLAS? | Rationale |
|---------------------|-------------------|-----------|
| **Manifest (MOC-*)** | **No** | Factory Project entry anchor + charter categories + reference topology — not org/site graph |
| **Registry (ROC-*)** | **No** | Portfolio catalog of Factory Projects — «which production cases exist», not «which businesses exist» |
| **Tracking (POC-03…07)** | **No** | Runtime 14-state progression, gate/handoff indexes — operational production lifecycle |
| **Surface (SOC-*)** | **No** | Read-only composition; explicitly not CRM, not dashboard |
| **Legal Entity Card** | **Risk — operational duplicate** | Org-identifying fields without mandatory `ORG-*` binding |
| **POC-09 / MOC-12 external refs** | **No — correct pattern** | Designed for locators/pointers; natural home for ATLAS ids |

### Cross-reference corpus

| Direction | Evidence |
|-----------|----------|
| ATLAS → Factory | `ATLAS-CONSUMER-CONTRACTS-v1.md` §8.3; `ATLAS-BOUNDARIES-v1.md` §6; population waves (PRJ-0008) |
| Factory → ATLAS | `WEBSITE-FACTORY-MVP-TOPOLOGY-DECISION-v1.md` — «ATLAS consumer alignment \| Future»; `WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md` — ATLAS not MVP-required |
| `projects/mars-website-factory/` | **No direct ATLAS references** found |

### Drift findings (keyword scan)

| Finding | Severity | Detail |
|---------|----------|--------|
| **D-01** Homonym «Project» | MEDIUM | Factory Project and ATLAS Project coexist; ATLAS Wave 3 excludes MARS program packs but Factory docs rarely cite `PRJ-*` |
| **D-02** Homonym «Registry» | MEDIUM | Three registries in Factory scope + ATLAS Business Reality Registry |
| **D-03** Legal Entity Card vs Counterparty Card | **HIGH** | Parallel org fact capture without documented crosswalk |
| **D-04** ATLAS binding not in physical specs | MEDIUM | MOC-12/POC-09 support external refs; no normative ATLAS id fields |
| **D-05** MVP defers ATLAS mechanically | LOW | By design; semantics still require no parallel canonical fork |
| **D-06** «Primary source of truth» on Legal Entity Card | LOW | Scoped to legal production; could misread as business SoT |

**No evidence** that Factory charters authorize a parallel canonical org/person/website/relationship registry.

---

## Reference Model

### Who owns what (normative)

```text
ATLAS (Business Reality)                    Website Factory (Production)
─────────────────────────                   ─────────────────────────────
ORG-*  Organization identity        ──ref──▶  Legal Entity Card (production)
PER-*  Person identity              ──ref──▶  (charter-bound only)
WEB-*  Website identity             ──ref──▶  build artifacts, QA, handoff
PRJ-*  Structural project           ──ref──▶  Factory Project (separate id)
DOM-*  Domain identity              ──ref──▶  charter endpoint / deploy ref
REL-*  Structural relationships     ──ref──▶  (suggest only; never invent OWNER)
Client = Org + CLIENT_OF            ──ref──▶  external actor; charter approvals

Factory OWNS (no ATLAS equivalent):
  • Factory Project identity shell (POC-01 / MOC-02)
  • Production state instance (POC-03) — 14 Runtime codes
  • Gate/handoff/declaration indexes (POC-04…07)
  • Manifest/Registry/Tracking/Surface physical bindings
  • Layer artefact refs, scope freeze, closure metadata
```

### What must remain reference-only

| ATLAS entity / fact | Factory posture |
|--------------------|-----------------|
| `ORG-*`, `PER-*`, `WEB-*`, `PRJ-*`, `DOM-*` | Store as **ref** in MOC-12 / POC-09 / charter; use when active canonical exists |
| Structural relationships | **Read** from ATLAS; **propose** corrections; never silent canonical write |
| Client commercial role | Ref to commissioning `ORG-*` via `COMMISSIONED_BY` / `CLIENT_OF` — not CRM deal |
| Counterparty / legal facts | Legal Entity Card = production input; ATLAS CC = evidence for org proposal — **not interchangeable SoT** |
| MARS program packs | External workspace pointers (ER-06, ROC-11) — not ATLAS Project duplicates |

### May Factory create its own copies?

| Artifact | Allowed? | Condition |
|----------|----------|-----------|
| Factory Project record | **Yes** | Own namespace; distinct from `PRJ-*` |
| Legal Entity Card | **Yes** | Production workflow only; should link `ORG-*` when known |
| Org/person/website **canonical registry** | **No** | CC-P04; CC-02 |
| Cached ATLAS read | **Yes** | Non-canonical; ATLAS wins on conflict |
| SEO/content copies of org name | **Yes** | Content layer — not identity registry |

### Binding Factory Project ↔ ATLAS entities

**Architecturally supported** via:

- MOC-12 External refs (Category 7 topology locators)
- POC-09 Reference index (external workspace, layer, Runtime pointers)
- ROC-11 External workspace pointer (optional catalog card)
- Charter amendments with explicit ATLAS id documentation (CR-01)

**Not yet normatively specified:** field names, mandatory vs optional ATLAS refs at enrollment, reconciliation workflow.

**Precedent:** `PRJ-0008` / `WEB-0009` / `ORG-0004` (Манипулятор case) — ATLAS population documents Factory/ORCA as downstream; Factory physical record **should** reference these ids, not recreate them.

---

## Creation Era Impact

### Can Creation Era proceed?

**Yes.** Physical Artifact Specifications (RT-G04, G10, G05, G12) define **Factory-scoped** classes (POC/MOC/ROC/SOC) that do **not** model ATLAS entity registries. Consolidation review (`WEBSITE-FACTORY-PHYSICAL-ARTIFACT-SPECIFICATIONS-CONSOLIDATION-REVIEW-v1.md`) confirms internal coherence; `workspaces/website-factory-operations/` **не существует** on disk — expected pre-Creation.

### What Creation Era will create (and what it won't)

| Will create | Will NOT create |
|-------------|-----------------|
| `website-factory-operations/` zone (DF-03) | ATLAS org/person/website/project records |
| Per-project LOC-HOME + POC/MOC bindings | Parallel business reality graph |
| Portfolio ROC catalog of Factory Projects | Duplicate ATLAS Project register |
| SOC read surfaces | CRM/client pipeline |
| Operator declaration/closure indexes | Canonical relationship edges |

### ATLAS alignment status at Creation Era entry

| Dimension | Status |
|-----------|--------|
| Semantic boundaries | **Aligned** — ATLAS consumer contract satisfied by design |
| Mechanical integration | **Deferred** — MVP topology: «ATLAS consumer alignment \| Future» |
| Adoption level | **C1** (documented consumer) per `ATLAS-FOUNDATION-AUDIT-v1.md` §3.7; target C1→C2 |
| Runtime dependency | **None required** — both systems documentation-first |

### First Factory Project scenario

**Can an ATLAS project become the first Factory Project?**

**Yes — as reference anchor, not as identity merge.**

Example: `PRJ-0008` (Манипулятор) + `WEB-0009` + commissioning `ORG-0004`.

- Factory Playbook 01 creates **new** Factory Project identity (MOC-02 / POC-01)
- Charter binds `atlas_project_ref: PRJ-0008`, `atlas_website_ref: WEB-0009`, `atlas_client_org_ref: ORG-0004` (recommended convention — not yet in specs)
- `projects/triumph-manipulator-landing/` remains **external workspace pointer** — not Factory SoT, not ATLAS Project duplicate

**Must not:** use `PRJ-0008` as Factory Project id or store org registry row in ROC/MOC as canonical business entity.

---

## Required Corrections

**Severity key:** BLOCK = stop Creation Era; REC = recommended before/at first bind; DOC = documentation pass.

| ID | Correction | Severity | Rationale |
|----|------------|----------|-----------|
| **RC-01** | Add normative **ATLAS reference binding convention** for charter / MOC-12 / POC-09 (field names, optional vs mandatory when ids known, SAFE UNKNOWN handling) | **REC** | Physical specs support external refs but lack ATLAS-specific discipline; prevents ad-hoc org duplication at first bind |
| **RC-02** | Document **Legal Entity Card ↔ ATLAS Counterparty Card crosswalk** (evidence flow: CC → ATLAS proposal; LEC → legal production; LEC should cite `ORG-*` + `evidence_ref` when attested) | **REC** | Highest drift risk (D-03); both systems can capture same INN/OGRN independently |
| **RC-03** | Add **terminology guard** in Factory onboarding: «Factory Project ≠ ATLAS Project»; «Factory Registry ≠ ATLAS Registry»; «Site Type Registry ≠ Business Reality Registry» | **DOC** | Homonym collisions D-01, D-02 |
| **RC-04** | Create `ATLAS-ADOPTION-STATEMENT` for Website Factory per `ATLAS-CONSUMER-CERTIFICATION-v1.md` (C1→C2 checklist) | **DOC** | ATLAS audit recommends before C2 claims; not blocking C1 Creation Era |
| **RC-05** | Playbook 01 enrollment checklist: verify ATLAS ids for client org / website / structural project **before** writing org-identifying fields into MOC-03 charter | **REC** | Operationalizes IGV 9.3 and CC-02 at human step |

**No BLOCK corrections identified.** Architecture permits Creation Era; risks are operational/terminological.

### Physical Artifact Specifications — ATLAS alignment check

| Spec | ATLAS-aligned? | Notes |
|------|----------------|-------|
| RT-G04 (POC/LOC) | **Yes** | Substrate hosts Factory indexes only; POC-09 = ref index |
| RT-G10 (MOC) | **Yes** | MOC-12 external refs; no org/site entity classes |
| RT-G05 (ROC) | **Yes** | Portfolio of Factory Projects; ROC-11 optional external pointer |
| RT-G12 (SOC) | **Yes** | Explicitly forbids CRM/client pipeline on Surface |

**Gap:** none of the four specs **name** ATLAS — alignment is implicit via external-ref classes and MVP deferral. RC-01 closes this gap without spec rewrite.

---

## Final Recommendation

### Decision

| Criterion | Result |
|-----------|--------|
| Factory can safely enter Creation Era? | **YES — conditional GO** |
| ATLAS remains canonical reality owner? | **YES** |
| Corrections required? | **REC-01, REC-02, REC-05 recommended**; RC-03, RC-04 documentation |

### Conditional GO conditions

1. First physical records **must not** include canonical org/person/website/project/relationship **registry rows** — only Factory classes (POC/MOC/ROC/SOC) + **refs** to ATLAS ids.
2. When ATLAS active canonical exists (e.g. Triumph case), Factory charter **should reference** `ORG-*` / `WEB-*` / `PRJ-*` — not restate as authoritative identity.
3. Legal Entity Card creation **should follow** RC-02 crosswalk — production input, not business registry entry.
4. On uncertain domain/org ownership: **SAFE UNKNOWN** per ATLAS IGV 9.3 — no invented OWNER to unblock export.

### Sequencing

```text
[Now]  Creation Era authorized — physical Factory artifacts only
       │
       ├─▶ RC-01/02/05 as operator discipline at first bind (no spec era required)
       │
       └─▶ RC-03/04 as parallel documentation (C1→C2 adoption)
```

---

## Explicit Non-Claims

This audit **does not** claim:

- Website Factory **runtime**, workflow engine, or `website-factory-operations/` **exist** on disk today
- ATLAS **runtime**, API, database, or live registry service **exist** in-repo
- RC-01…RC-05 have been **implemented** — recommendations only
- Triumph/manipulator ATLAS wave records are **attested active canonical** on a live service — population docs are documentation-level
- Legal Entity Card and Counterparty Card **are synchronized** in any automated way
- MVP **requires** mechanical ATLAS integration — explicitly excluded per topology decision
- This audit **authorizes** disk creation under `website-factory-operations/` — separate creation authorization
- Any **git commit or push** was performed

**SAFE UNKNOWN:**

- Whether operators already maintain ad-hoc Factory manifest/registry files — Factory docs mark **UNKNOWN**
- Exact field serialization for POC/MOC/ROC/SOC — deferred to Creation Era operator choice under class separation rules
- External Counterparty Card storage at `C:\AI MARS STORAGE\atlas\evidence\` — referenced by ATLAS, not verified in this audit

---

*Website Factory ATLAS Integration Audit v1 — audit only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-ATLAS-INTEGRATION-AUDIT-v1.md`. Git: no commit, no push.*
