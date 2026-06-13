# REPORT — Website Factory Physical MVP Artifact Creation Strategy v1

**Версия:** v1  
**Дата:** 2026-06-07  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical MVP Artifact Creation Era — **strategy definition only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE**; Physical Artifact Specifications **COMPLETE**; Physical Artifact Specifications Consolidation Review **COMPLETE**; ATLAS Integration Audit **COMPLETE**; ATLAS Adoption Finalization **COMPLETE**; Physical MVP Artifact Creation Era **AUTHORIZED**  
**Тип:** creation strategy only — **без** artifact creation, folder creation, operational zone files, runtime design, automation design, workflow engine design, dashboard/UI design  
**Primary inputs:** [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-DEFINITION-REVIEW-v1.md), [WEBSITE-FACTORY-PHYSICAL-ARTIFACT-SPECIFICATIONS-CONSOLIDATION-REVIEW-v1.md](WEBSITE-FACTORY-PHYSICAL-ARTIFACT-SPECIFICATIONS-CONSOLIDATION-REVIEW-v1.md), [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G05-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G12-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G12-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [WEBSITE-FACTORY-ATLAS-INTEGRATION-AUDIT-v1.md](WEBSITE-FACTORY-ATLAS-INTEGRATION-AUDIT-v1.md), [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md)

---

## Executive Summary

**Вердикт:** Physical MVP Artifact Creation Era организуется как **три последовательные creation waves** поверх уже принятой модели фаз A–F, с **одним Core 5 pilot case** на **реальных ATLAS references** (Triumph / Манипулятор), **без** synthetic test project и **без** расширения MVP scope.

**Цель эры:** перевести Website Factory от **specification-complete** к **first physical MVP demonstration** — минимальная авторизованная привязка Manifest + Registry + Tracking Surface на едином persistence substrate для одного Factory operator.

**Нормативная последовательность track-ов:** RT-G04 → RT-G10 → RT-G05 → RT-G04 (index scaffold) → RT-G12 → Playbooks 03↔04→05. Пример RT-G04→RT-G10→RT-G05→RT-G12 **подтверждён** с уточнением: между RT-G05 и RT-G12 обязателен **index scaffold** (POC-03…POC-05); рекомендуется **один цикл Playbook 04** до первой демонстрации Playbook 03.

**MVP success:** один pilot проходит Playbooks 01→02→03↔04→05 с bound planes **без workspace archaeology**, **без workflow engine**, **без automation** — evidence-based walkthrough, не runtime metrics.

**Следующий authorized task:** **Physical MVP Artifact Creation — Wave 1 Bootstrap Execution** (operator authorization + serialization convention lock + LOC-ZONE / LOC-HOME / manifest bind) — **отдельная задача**, не часть этого deliverable.

**Verified repo state:** `workspaces/website-factory-operations/` **не существует** on disk — ожидаемо; strategy **не создаёт** файлы.

---

## Creation Era Scope

### Что входит в Creation Era

| # | In-scope | Обоснование |
|---|----------|-------------|
| 1 | **Физическое материализаование Wave 1 class inventory** — POC/MOC/ROC/SOC в `workspaces/website-factory-operations/` | C2–C7 capability floor |
| 2 | **Operator-controlled disk writes** — human/assisted, не automated | DA-01, OA-ACT-01 |
| 3 | **Serialization / layout / naming convention selection** — operator choice под COL-* class separation | DF-01…07 resolved; format — creation-era |
| 4 | **One Core 5 pilot** — LANDING / CORPORATE / ECOMMERCE / PORTFOLIO / SERVICE | OR-06; MVP Definition |
| 5 | **ATLAS reference binding** — `atlas_*_ref` в MOC-12 / POC-09 per Adoption Statement | C1 consumer; RC-01…05 |
| 6 | **Playbook-driven population** — 01 enrolled → bind → 02 enrolled → bind → 04 declarations → 03 sessions → 05 closure | Phases A–F operational cycle |
| 7 | **MVP success evidence capture** — operator walkthrough narrative, checklists R-M*/R-R*/R-S* | S1–S9 без runtime metrics |
| 8 | **Explicit non-claims preservation** — no false runtime/automation narrative | SC-01 guard |
| 9 | **Creation-era hygiene** — RUNTIME-GAPS status sync, NEXT-PRIORITIES update (recommended, not blocking) | Post-specification hygiene |

### Что не входит в Creation Era

| # | Out-of-scope | Куда отложено |
|---|--------------|---------------|
| 1 | Workflow engine (RT-G01), agent execution (RT-G02), automation mutating indexes (RT-G03) | Post-MVP Tier 2 |
| 2 | Queue (RT-G06), MIG execution binding (RT-G08), Engine runtime product (RT-G09) | Post-MVP |
| 3 | Validator CLI as gate authority (RT-G11), execution logs as SoT (RT-G07) | Post-MVP Tier 1 |
| 4 | Operator dashboard / SaaS / widget product | RT-G12 FF-02, TX-07 |
| 5 | Database / multi-tenant storage as requirement | DF-02 filesystem sufficient |
| 6 | Extended site types без blueprint parity | Architecture charter |
| 7 | Layer artefact bodies, Legal Pack generation, deploy/go-live | External / post-Factory |
| 8 | Mechanical ATLAS API/runtime integration | MVP topology: Future |
| 9 | Second+ Factory Projects как **обязательное** условие MVP | Optional generality signal |
| 10 | Redesign Foundation / Engine / Playbooks / accepted specifications | Forbidden |

### Scope boundary statement

Creation Era **закрывает physical binding gap** для single-operator Core 5 MVP — **не** закрывает automation, multi-operator ops, integration, или Factory runtime product.

```text
  Specification-complete (today)
           │
           ▼
  Creation Era ──▶ physical records on disk + pilot evidence
           │
           ▼
  MVP declared complete ──▶ post-MVP charter queue (RT-G07, RT-G11, …)
```

---

## Wave Structure

### Модель: три creation waves (обоснование)

Physical MVP Definition Review определяет **Wave 1 inventory** как единый MVP physical set. Для **управления риском и governance gates** Creation Era **декомпозирует** Wave 1 inventory на **три последовательные creation waves** — каждая wave завершается **verification gate** перед следующей.

**Альтернатива «single wave» отклонена:** единовременное создание всех классов A–E повышает риск ordering violation (SC-02), mega-record anti-pattern и false «MVP shipped» narrative без промежуточной верификации.

### Wave 1 — Substrate & Manifest Bootstrap

**Соответствие фазам:** A (substrate) + B (manifest)  
**Track:** RT-G04 + RT-G10  
**Доказывает:** C2, C3 (S2 partial)

| Deliverable | Class focus |
|-------------|-------------|
| Authorized zone | LOC-ZONE |
| Pilot record home | LOC-HOME, POC-01 |
| Manifest binding | POC-02(m), MOC-01…MOC-05, MOC-08, MOC-10, MOC-12, POC-09 |
| ATLAS refs | `atlas_*_ref` в MOC-12 when known |

**Wave 1 gate:** MOC-01 discoverable; Playbook 01 doctrinal enrolled attested in MOC-10; no registry/surface yet required.

### Wave 2 — Portfolio & Visibility Scaffold

**Соответствие фазам:** C (registry) + D (index scaffold) + E (surface read bind)  
**Track:** RT-G05 + RT-G04 (index loci) + RT-G12  
**Доказывает:** C4, C5 scaffold (S3, S4 partial — empty-allowed signals OK)

| Deliverable | Class focus |
|-------------|-------------|
| Portfolio catalog | POC-02(r), ROC-01…ROC-07, ROC-09; ROC-05→MOC-01 |
| Index scaffold | POC-03…POC-05 (empty shells at NEW_PROJECT) |
| Surface read bind | SOC-01…SOC-08 (+ SOC-09 when applicable) |
| Optional | SOC-10 portfolio select assist (recommended for S3 path) |

**Wave 2 gate:** Operator path Registry → Manifest → Surface **structurally wired**; eight questions **answerable** (depth may be shallow until Wave 3).

### Wave 3 — Pilot Demonstration & MVP Evidence

**Соответствие фазе:** F (pilot operation)  
**Track:** Playbooks 03↔04→05 population on existing bindings  
**Доказывает:** C6, C7; S1–S9 full

| Deliverable | Class focus |
|-------------|-------------|
| First+ Playbook 04 declarations | POC-03…POC-07, POC-06, POC-07, POC-10 |
| Playbook 03 sessions | SOC-* read path with index depth |
| Playbook 05 closure | POC-08 |
| Optional catalog update | ROC-07 archived (orthogonal to POC-08) |
| MVP evidence | Operator walkthrough narrative |

**Wave 3 gate:** Full lifecycle Playbooks 01–05 executable with bound planes; S1–S9 evidence captured.

### Wave dependency diagram

```text
  Wave 1 (RT-G04 + RT-G10)
       │  C2, C3
       ▼
  Wave 2 (RT-G05 + index scaffold + RT-G12)
       │  C4, C5
       ▼
  Wave 3 (Playbooks 03↔04→05)
       │  C6, C7 → S1–S9
       ▼
  Creation Era exit → MVP completion declaration
```

---

## Creation Order

### Normative track sequence (validated)

Пример RT-G04 → RT-G10 → RT-G05 → RT-G12 **подтверждён** с обязательным **index scaffold** между RT-G05 и RT-G12:

```text
  RT-G04  Substrate zone + per-project home
     │
     ▼
  RT-G10  Manifest bind (requires Playbook 01 doctrinal enrolled)
     │
     ▼
  RT-G05  Registry bind (requires Playbook 02 doctrinal enrolled; MOC-01 stable)
     │
     ▼
  RT-G04  Index scaffold POC-03…POC-05 (empty OK at NEW_PROJECT)
     │
     ├──▶ [RECOMMENDED] First Playbook 04 declaration cycle
     │
     ▼
  RT-G12  Surface read bind (requires MOC-01 + index loci)
     │
     ▼
  Playbooks 03↔04 (repeat) → Playbook 05 → POC-08
```

### Forbidden orderings

| Violation | Why forbidden |
|-----------|---------------|
| RT-G12 before RT-G04 substrate | SC-02; no read feed |
| RT-G05 before RT-G10 MOC-01 | G04-IMPL-02; ROC-05 orphan |
| Registry bind before manifest anchor | REL-12 broken |
| Physical bind before Playbook 01/02 doctrinal enrollment | INT-M01, INT-R01; discovery bind forbidden |
| Surface auto-mutating POC-* | TRK-REL-01; authority drift |
| Playbook 03 **demonstration** before index loci exist | OBL-S-SUB-04 |
| Meaningful Playbook 03 **session** before any Playbook 04 (recommended guard) | COMP-02; shallow-only demo insufficient for S4 |

### Per-wave creation checklist (operator execution reference)

| Step | Wave | Action | Playbook precondition |
|------|------|--------|----------------------|
| 1 | Pre-W1 | Operator authorization for disk writes | Governance |
| 2 | Pre-W1 | Serialization convention lock (format + COL-* layout) | Operator workshop |
| 3 | W1 | Create LOC-ZONE | — |
| 4 | W1 | Create LOC-HOME + POC-01 for pilot | — |
| 5 | W1 | Playbook 01 doctrinal manifest-enrolled | 01 |
| 6 | W1 | Manifest bind: POC-02(m), MOC-*, POC-09 | 01 enrolled |
| 7 | W2 | Playbook 02 doctrinal registry-enrolled | 02 |
| 8 | W2 | Registry bind: POC-02(r), ROC-* | 02 enrolled; MOC-01 stable |
| 9 | W2 | Index scaffold: POC-03…POC-05 | — |
| 10 | W2 | [Recommended] First Playbook 04 declaration | 04 |
| 11 | W2 | Surface read bind: SOC-01…SOC-08 | MOC-01 + loci |
| 12 | W3 | Playbook 03 sessions (repeat) | 03 |
| 13 | W3 | Playbook 04 declarations (repeat) | 04 |
| 14 | W3 | Playbook 05 → POC-08 | 05 |

---

## Pilot Strategy

### Decision: real ATLAS-anchored case — not synthetic test project

**Рекомендация:** первый physical pilot **SHOULD** использовать **реальные ATLAS population references** для Triumph / Манипулятор case, **не** synthetic «TEST-PROJECT-001».

### Justification

| Criterion | Real ATLAS case | Synthetic test project |
|-----------|-----------------|------------------------|
| ATLAS C1 adoption proof | **Validates** RC-01 refs, ENROLL-ATLAS-01, no parallel registry | **Avoids** integration discipline; false comfort |
| Evidence tier | PRJ-0008, WEB-0009, ORG-0004 documented in ATLAS waves | No external reality anchor |
| Core 5 fit | manipulator-triumph.ru — LANDING-class case | Arbitrary; may miss legal/scope realism |
| External workspace pointer | `projects/triumph-manipulator-landing/` — natural POC-09 / ROC-11 ref | No meaningful ER-06 exercise |
| Duplication risk test | Forces LEC ↔ CC crosswalk (RC-02) under real INN/OGRN context | Skips highest drift risk (D-03) |
| MVP scope | Within Core 5 + single operator | Same — but lower governance value |

### Pilot binding model (normative)

Factory Project **получает собственный identity shell** (MOC-02 / POC-01) — **не** merges with ATLAS Project id.

**Recommended ATLAS refs** (per Adoption Statement RC-01):

| Field | Pilot value (documentation-level) | Role |
|-------|-----------------------------------|------|
| `atlas_project_ref` | `PRJ-0008` | Structural ATLAS project — **not** Factory Project id |
| `atlas_website_ref` | `WEB-0009` | Website identity |
| `atlas_client_org_ref` | `ORG-0004` | Commissioning / client organization |
| External workspace | triumph-manipulator-landing path | POC-09 / MOC-12 / optional ROC-11 |

**Site type:** LANDING (Core 5) — `site_type_code` in MOC-06 when charter mandates.

### Pilot constraints

| Constraint | Rule |
|------------|------|
| Single operator | One Factory operator for entire demonstration |
| Core 5 only | No extended types |
| No canonical fork | **MUST NOT** create org/person/website/project registry rows in Factory zone |
| Uncertain ownership | SAFE UNKNOWN per IGV 9.3 — no invented OWNER |
| Legal Entity Card | Production input only; cite `atlas_client_org_ref` when ORG-* attested |
| Deploy authorization | **SAFE UNKNOWN** — Factory closure ≠ deploy authorization |

### Synthetic pilot — when permitted

Synthetic case **MAY** be used **only** if operator explicitly requires zero ATLAS coupling for isolation testing — **not** as default MVP demonstration path. Synthetic pilot **does not satisfy** ATLAS adoption validation dimension of Creation Era.

---

## Minimum Artifact Set

### Scope note

Задача запрашивает minimum set для **C2–C5** без расширения scope. C6–C7 **входят в Wave 3** как completion path, но **не расширяют** class inventory beyond Wave 1 definition.

### Tier 0 — Infrastructure (C2)

| Class | Mandatory | Notes |
|-------|-----------|-------|
| **LOC-ZONE** | Yes | `workspaces/website-factory-operations/` |
| **LOC-HOME** | Yes | One per pilot Factory Project |

### Tier 1 — Manifest (C3)

| Class | Mandatory | Notes |
|-------|-----------|-------|
| **POC-01** | Yes | Identity shell |
| **POC-02** manifest facet | Yes | Binding carrier |
| **MOC-01** | Yes | Entry anchor — MVP hinge |
| **MOC-02…MOC-05** | Yes | Minimum understanding categories |
| **MOC-06** | Conditional | When site_type binding mandated — expected for Core 5 pilot |
| **MOC-08** | Yes | Topology map |
| **MOC-10** | Yes | Playbook 01 enrollment link |
| **MOC-12** | Yes | External refs + ATLAS `atlas_*_ref` |
| **POC-09** | Yes | Topology refs to index loci |

### Tier 2 — Registry (C4)

| Class | Mandatory | Notes |
|-------|-----------|-------|
| **POC-02** registry facet | Yes | Portfolio scope |
| **ROC-01** | Yes | Catalog aggregate |
| **ROC-02…ROC-07** | Yes | Per pilot entry |
| **ROC-09** | Yes | Playbook 02 enrollment link |
| **ROC-05 → MOC-01** | Yes | Hard pointer chain |

### Tier 3 — Surface (C5)

| Class | Mandatory | Notes |
|-------|-----------|-------|
| **SOC-01** | Yes | Read convergence point |
| **SOC-02…SOC-08** | Yes | Eight operator questions |
| **SOC-09** | When detected | Integrity warnings |

### Tier 4 — Index scaffold (C5 depth prerequisite — Wave 2)

| Class | Mandatory for C5 demo | Notes |
|-------|----------------------|-------|
| **POC-03…POC-05** | Yes (empty OK at bootstrap) | Required before credible Playbook 03 |

### Explicitly excluded from minimum set

| Class / role | Why excluded |
|--------------|--------------|
| POC-08 | Wave 3 / Playbook 05 — not C2–C5 |
| POC-06, POC-07, POC-10 populated | C6 — Wave 3 |
| MOC-07, MOC-09, MOC-11 | Optional / event-triggered |
| ROC-08, ROC-11, ROC-X1 | Optional |
| SOC-10, SOC-11, SOC-D1, SOC-O1 | Optional (SOC-10 recommended for S3 path) |
| POC-D1, POC-O1, POC-O2 | Optional / non-authoritative |
| All forbidden classes | Runtime, automation, dashboard, analytics |

### Capability proof matrix (C2–C5 only)

| Capability | Minimum physical proof |
|------------|-------------------------|

| **C2** | LOC-ZONE exists; operator can read/write Factory Project records in one zone |

| **C3** | MOC-01 is single canonical entry; MRDY categories present in MOC-02…05/08/10/12 |

| **C4** | ROC-01 lists pilot; ROC-05 resolves to MOC-01 without per-workspace search |

| **C5** | SOC-01…08 compose eight questions from bound POC/MOC data — not full-repo grep |



---



## Success Demonstration



### What constitutes MVP success (without runtime)



MVP success = **evidence-based operator walkthrough** satisfying **S1–S9** on one Core 5 pilot — **not** uptime, performance benchmarks, or shipped product narrative.



### Primary success evidence



| ID | Criterion | How demonstrated (no runtime) |

|----|-----------|--------------------------------|

| **S1** | One Core 5 pilot completes full operator path | Narrated walkthrough: Playbooks 01→02→03↔04→05 with bound artefacts |

| **S2** | Manifest-enrolled with persisted entry anchor | Operator identifies **one** MOC-01 per project |

| **S3** | Catalog-discoverable | Operator finds pilot in ROC-01 **without** opening each workspace |

| **S4** | Eight Surface questions answerable | Playbook 03 session completed via SOC-02…08 — not full-repo search |

| **S5** | Declarations reflected | Playbook 04 acts visible in POC-03…07; next SOC read shows updated truth |

| **S6** | Closure persistable | Playbook 05 terminal outcome in POC-08 |

| **S7** | No workflow engine required | Entire path = human declarations only |

| **S8** | Authority preserved | No automated gate PASS or state transition |

| **S9** | Explicit non-claims intact | No «shipped Factory runtime» or «automation exists» claims |



### Success evidence artifacts (creation era deliverables — not code)



| Evidence type | Content |

|---------------|---------|

| Operator walkthrough narrative | Step-by-step path with file/class references |

| Checklist completion | R-M* (manifest), R-R* (registry), R-S* (surface) per specifications |

| Pilot case record | Which Core 5 type; which ATLAS refs bound |

| Scope audit | Forbidden classes absent |

| Non-claims acknowledgment | Signed/attested operator statement |



### What does NOT count as success



| Non-success | Why |

|-------------|-----|

| Zone folder exists but pilot incomplete | Infrastructure ≠ MVP |

| Documentation-only operation | Pre-MVP baseline — already works |

| Validator CLI or CI pipeline shipped | Post-MVP scope creep |

| Frontend deployed | Post-Factory |

| Second pilot mandatory | One demonstration sufficient per MVP Definition |



### Success vs completion



| Term | Meaning |

|------|---------|

| **MVP successful** | S1–S9 evidence exists on pilot |

| **MVP complete** | Organization declares MVP closed — capabilities demonstrated, exclusions verified, post-MVP boundary active |

| **Creation Era complete** | Physical artefacts exist + MVP successful + era exit criteria met |



---



## Risk Review



### Risk register



| ID | Risk | Severity | Mitigation |

|----|------|----------|------------|

| **R-01** | **Ownership drift** — unclear who writes MOC vs ROC vs POC vs SOC | **MEDIUM** | Ownership matrix from Consolidation Review; Playbook 04 → POC-03…07 only; bind acts per track |

| **R-02** | **Scope creep** — MVP conflated with Factory runtime product | **HIGH** | SC-01 guard; explicit non-claims; MVP ≠ RT-G09 |

| **R-03** | **Runtime pressure** — «we have files, add workflow engine» | **HIGH** | RT-G01 forbidden; transitions declared not executed |

| **R-04** | **Dashboard pressure** — RT-G12 becomes UX program | **HIGH** | FF-02, TX-07; SOC = read composition only |

| **R-05** | **Parallel registry risk** — Factory catalog confused with ATLAS Business Reality Registry | **MEDIUM** | TG-ATLAS-01 terminology guards; ROC ≠ ORG registry |

| **R-06** | **ATLAS duplication risk** — org facts in MOC-03 instead of refs | **HIGH** | ENROLL-ATLAS-01; RC-02 LEC↔CC crosswalk; MOC-12 refs |

| **R-07** | **Ordering violation** — surface before manifest stable | **HIGH** | Wave gates; sequence validation matrix |

| **R-08** | **Mega-record anti-pattern** — single file swallows planes | **HIGH** | POC-RULE-02, MOC-RULE-02, ROC-RULE-03, SOC-RULE-02 |

| **R-09** | **Registry before manifest** — broken ROC-05 chain | **HIGH** | Wave 1 before Wave 2; MOC-01 gate |

| **R-10** | **Shallow Playbook 03 demo** — empty indexes, fake S4 | **MEDIUM** | Recommended Playbook 04 cycle before 03 demonstration |

| **R-11** | **False «MVP shipped» narrative** | **HIGH** | S9; creation ≠ runtime; era exit ≠ product launch |

| **R-12** | **Serialization lock-in** — format choice breaks COL-* separation | **MEDIUM** | Class separation normative regardless of JSON/YAML/markdown |

| **R-13** | **v0↔v1 corpus mixing** | **LOW** | AZ-04; OQ-OM06 routing before assisted writes |

| **R-14** | **Triumph workspace ref ambiguity** | **LOW** | DF-08 per-case; pointer-only in POC-09/MOC-12 |



### Risk summary



| Category | HIGH | MEDIUM | LOW |

|----------|------|--------|-----|

| Creation-era risks | 6 | 4 | 2 |



**Interpretation:** HIGH risks **preventable** via wave gates, sequence discipline, ATLAS-first enrollment, and explicit non-claims — **not** indicators that Creation Era should be delayed.



---



## Readiness Gates



### Gate 0 — Era authorization (pre-first byte on disk)



| # | Condition | Verification |

|---|-----------|--------------|

| G0-1 | Physical Artifact Specification Era **COMPLETE** | Consolidation Review verdict |

| G0-2 | Physical MVP Artifact Creation Era **AUTHORIZED** | Governance acknowledgment |

| G0-3 | **Separate operator authorization** for disk writes | Explicit operator act — not automatic from era authorization |

| G0-4 | ATLAS Adoption Statement **accepted** (C1) | WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1 |

| G0-5 | No BLOCK corrections from ATLAS audit | Integration Audit: conditional GO |

| G0-6 | `workspaces/website-factory-operations/` **absent or intentionally empty** | Repo verify |



### Gate 1 — Pre-Wave 1 (substrate & manifest)



| # | Condition | Verification |

|---|-----------|--------------|

| G1-1 | Serialization convention **locked** for pilot | Operator documents format + COL-* layout choice |

| G1-2 | Pilot case **selected** — Core 5 site class identified | Operator charter |

| G1-3 | ATLAS refs **researched** for pilot (ENROLL-ATLAS-01) | ORG/WEB/PRJ lookup or SAFE UNKNOWN documented |

| G1-4 | Playbook 01 **doctrinally ready** to execute | Operator attestation |

| G1-5 | Terminology guards **acknowledged** | TG-ATLAS-01 — Factory Project ≠ ATLAS Project |



### Gate 2 — Pre-Wave 2 (registry & surface)



| # | Condition | Verification |

|---|-----------|--------------|

| G2-1 | Wave 1 **complete** — MOC-01 stable, R-M* checklist pass | Operator verification |

| G2-2 | Playbook 02 **doctrinally ready** | Operator attestation |

| G2-3 | ROC-05 → MOC-01 pointer **plannable** | MOC-01 path known |

| G2-4 | DF-07 form factor **chosen** for SOC read bind | Markdown index / CLI / static HTML — operator choice |

| G2-5 | Index loci paths **declared** in POC-09 / MOC-08 | Topology wired |



### Gate 3 — Pre-Wave 3 (pilot demonstration)



| # | Condition | Verification |

|---|-----------|--------------|

| G3-1 | Wave 2 **complete** — ROC-*, SOC-01…08 wired, R-R* + R-S* pass | Operator verification |

| G3-2 | POC-03…POC-05 loci **exist** | Index scaffold |

| G3-3 | [Recommended] At least **one Playbook 04 declaration** recorded | POC-06/07 populated |

| G3-4 | Operator **trained** on Playbook 03 read-only discipline | SE-03 |



### Gate 4 — Pre-era exit



| # | Condition | Verification |

|---|-----------|--------------|

| G4-1 | S1–S9 evidence **captured** | Walkthrough narrative |

| G4-2 | C1–C9 capabilities **demonstrated** | MVP Definition mapping |

| G4-3 | Forbidden artefacts **absent** | Scope audit |

| G4-4 | Explicit non-claims **published and honored** | Operator attestation |

| G4-5 | Post-MVP boundary **acknowledged** | Tier 1/2/3 separation documented |



---



## Creation Era Exit Criteria



Creation Era **ends** when **all** conditions below are true:



| # | Exit condition | Evidence |

|---|----------------|----------|

| E-1 | **Wave 1–3 complete** — all mandatory classes materialized per pilot | Physical records in authorized zone |

| E-2 | **One Core 5 pilot** satisfies S1–S9 | Operator walkthrough |

| E-3 | **C2–C7 demonstrated** on pilot | Capability mapping |

| E-4 | **Dependency order respected** — no surface-before-manifest violation | Sequence audit |

| E-5 | **MVP exclusions verified absent** — no RT-G01/02/03/06/08/09/11/13/14/15 artefacts | Scope audit |

| E-6 | **Authority model preserved** — DA-01, OA-ACT-01, OA-ACT-04 | No automated declarer |

| E-7 | **ATLAS alignment honored** — refs not forks; no parallel canonical registry | RC-01…05 discipline |

| E-8 | **Explicit non-claims intact** | No runtime/automation false narrative |

| E-9 | **Handoff to post-MVP queue** documented | RT-G07, RT-G11, etc. — separate authorization |



### Exit is NOT conditioned on



| Not required | Reason |

|--------------|--------|

| Production uptime SLA | No runtime product |

| Performance benchmarks | Out of scope |

| Second pilot | Optional generality signal |

| OQ-R02 card template finalized | Optional |

| Mechanical ATLAS integration | Deferred |

| C2 ATLAS consumer certification | Target future; C1 sufficient |

| Git commit of operational zone | DF-10 operator policy |



### Era transition diagram



```text

  Physical Artifact Specification Era ──COMPLETE──▶

  Physical MVP Artifact Creation Era ──ACTIVE──▶

       │

       ├── Wave 1 → Wave 2 → Wave 3

       │

       └── Exit criteria E-1…E-9 met

                 │

                 ▼

  MVP Complete declaration (organizational)

                 │

                 ▼

  Post-MVP Implementation Charter Queue

```



---



## Next Authorized Task



### Recommended exact next task



**Task name:** `Physical MVP Artifact Creation — Wave 1 Bootstrap Execution`



**Type:** implementation execution (first authorized disk writes) — **not** strategy, **not** specification



**Scope of next task:**



1. Obtain **explicit operator authorization** for physical creation (Gate 0-3).

2. **Lock serialization convention** — format + per-class layout under COL-* rules (Gate 1-1).

3. Confirm **pilot case** — Triumph / Манипулятор ATLAS-anchored LANDING (Gate 1-2, 1-3).

4. Execute **Wave 1 only:**

   - Create LOC-ZONE at `workspaces/website-factory-operations/`

   - Create LOC-HOME + POC-01 for pilot

   - Execute Playbook 01 doctrinal enrollment

   - Manifest bind: POC-02(m), MOC-01…MOC-12 per mandatory rules, POC-09, ATLAS refs in MOC-12

5. Complete **R-M* readiness checklist** from RT-G10 specification.

6. **Stop at Wave 1 gate** — do not proceed to registry/surface until Wave 1 verified.



**Explicitly NOT in next task:**



- Wave 2 (ROC, SOC) or Wave 3 (pilot population)

- Runtime, automation, workflow engine, dashboard

- Validator CLI, execution logs

- Git commit/push (unless operator separately requests)



**Prerequisite documents for executor:** RT-G04 + RT-G10 Physical Artifact Specifications; Playbook 01; ATLAS Adoption Statement; this strategy.



---



## Explicit Non-Claims



This strategy **does not** claim:



- Any **physical artifact**, folder, manifest, registry entry, tracking record, or surface bind **was created** — strategy only.

- `workspaces/website-factory-operations/` **exists** on disk — verified absent; creation awaits separate execution task.

- Website Factory **runtime**, workflow engine, automation layer, validator engine, database, or operator dashboard **exist** or **were designed** in this deliverable.

- MVP **has been built**, **demonstrated**, or **declared complete** — only **creation approach defined**.

- Serialization format, internal folder layout, DF-08/09/10 **resolved** — assigned to Wave 1 bootstrap execution.

- Mechanical ATLAS integration **is MVP-required** — explicitly deferred; refs are convention-only.

- Triumph / PRJ-0008 / WEB-0009 / ORG-0004 are **live attested canonical** on a runtime service — population docs are documentation-level (**SAFE UNKNOWN** for live service).

- ATLAS C2+ certification **achieved** — C1 attestation only per Adoption Statement.

- This strategy **authorizes** disk writes — **separate operator authorization** required per Gate 0-3.

- Any **git commit, push, tag, or branch** was performed.

- Accepted architecture, specifications, or doctrine **were modified** — strategy deliverable only.



This strategy **does** claim (evidence-based):



- Creation Era scope, three-wave model, and track sequence **derive from** accepted MVP Definition, Physical MVP Definition Review, Consolidation Review, four Physical Artifact Specifications, and ATLAS Adoption Statement **without contradiction**.

- RT-G04 → RT-G10 → RT-G05 → RT-G12 sequence **validated** with index scaffold between RT-G05 and RT-G12.

- Real ATLAS-anchored pilot **preferred** over synthetic for MVP demonstration.

- Minimum artifact set for C2–C5 **defined** without scope expansion.

- MVP success **evidence-based** without runtime metrics.

- Next authorized task **identified** as Wave 1 Bootstrap Execution.



Human-operated declaration path (Playbook 04 DA-01, OA-ACT-04) remains the v1 normative model.



---



*Website Factory Physical MVP Artifact Creation Strategy v1 — strategy definition only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-CREATION-STRATEGY-v1.md`. Git: no commit, no push.*



---



# REPORT — Website Factory Physical MVP Artifact Creation Strategy v1



**Stage:** Physical MVP Artifact Creation Era — Strategy Definition  

**Deliverable:** `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-CREATION-STRATEGY-v1.md`  

**Changed files:** `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-CREATION-STRATEGY-v1.md` (created)  

**Summary:** Определена стратегия Physical MVP Artifact Creation Era: scope in/out, три creation waves (substrate+manifest → registry+surface scaffold → pilot demonstration), подтверждённый порядок RT-G04→RT-G10→RT-G05→index scaffold→RT-G12→Playbooks, pilot на реальных ATLAS refs (Triumph/Манипулятор), minimum set для C2–C5, success demonstration S1–S9 без runtime, risk register, readiness gates, exit criteria, next task = Wave 1 Bootstrap Execution — без создания артефактов и operational zone.  

**Git:** no commit, no push (per task).  

**UNKNOWN:** live attestation status ATLAS wave records on runtime service; operator calendar for Wave 1 execution.
