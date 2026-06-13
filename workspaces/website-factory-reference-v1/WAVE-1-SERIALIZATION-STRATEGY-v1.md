# REPORT — Wave 1 Serialization Strategy v1

**Версия:** v1  
**Дата:** 2026-06-07  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `C:\AI MARS` (MARS monorepo)  
**Эра:** Physical MVP Artifact Creation Era — **serialization strategy only**  
**Контекст:** Foundation **COMPLETE**; Engine **COMPLETE**; Doctrine **COMPLETE**; Operational Design **COMPLETE**; Implementation Planning **COMPLETE**; Implementation Standards **COMPLETE**; Physical Artifact Specifications **COMPLETE**; Physical Artifact Specifications Consolidation Review **COMPLETE**; ATLAS Adoption **COMPLETE**; Physical MVP Artifact Creation Strategy **COMPLETE**; Wave 1 Bootstrap Execution Plan **COMPLETE**; Physical MVP Artifact Creation Era **AUTHORIZED**; **no physical artifacts created yet**  
**Тип:** serialization strategy only — **без** artifact creation, folder creation, records, bindings, layouts, runtime, automation  
**Primary inputs:** [WAVE-1-BOOTSTRAP-EXECUTION-PLAN-v1.md](WAVE-1-BOOTSTRAP-EXECUTION-PLAN-v1.md), [WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-CREATION-STRATEGY-v1.md](WEBSITE-FACTORY-PHYSICAL-MVP-ARTIFACT-CREATION-STRATEGY-v1.md), [RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G04-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md](RT-G10-PHYSICAL-ARTIFACT-SPECIFICATION-v1.md), [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md), [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md), [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md), [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md)  
**Owner decision (authoritative):** Documentation-first; human-readable; AI-readable; **Markdown preferred** unless a specific artifact class demonstrates strong need for machine-oriented serialization. Primary consumers: human operator, Cursor, ChatGPT — **not** runtime, workflow engine, API, automation.

---

## Executive Summary

**Вердикт:** Wave 1 **может быть реализована** с **Markdown-first** сериализацией. Решение владельца **подтверждается** и **не требует переопределения**.

**Рекомендация блокировки:** **Markdown-first** — основной формат сериализации для всех Wave 1 artifact classes; **обязательных** исключений (JSON, YAML, Spreadsheet) для Wave 1 **нет**.

**Ключевой вывод:** Нормативное требование спецификаций — **разделение record classes** (COL-01…COL-04, POC-RULE-02, MOC-RULE-02), **не** выбор формата. Markdown с **отдельными физическими носителями per class** удовлетворяет C2, C3 и всем Wave 1 obligations.

**Исключения:** Для Wave 1 **нет** классов с объективной необходимостью machine-oriented serialization. Опциональный YAML frontmatter в Markdown-файлах **допустим**, но **не обязателен** и **не является** отдельным lock-вариантом.

**Блокеры Wave 1 после этой стратегии:** остаётся только **Gate 0-3** (explicit operator authorization for disk writes). Gate **G1-1** (serialization convention lock) **может быть закрыт** принятием этой стратегии оператором.

**Следующий шаг:** Physical MVP Artifact Creation — Wave 1 Bootstrap Execution (отдельная задача, **не** часть этого deliverable).

---

## Serialization Consumer Review

### Primary consumers (owner-assumed, validated)

| Consumer | Wave 1 role | Reads which classes |
|----------|---------------|---------------------|
| **Human operator** | Авторитетный writer/reader; Playbook 01 enrollment; manifest bind; R-M* verification | LOC-ZONE, LOC-HOME, POC-01, POC-02(m), POC-09, MOC-01…MOC-05, MOC-08, MOC-10, MOC-12 (+ MOC-06 when mandated) |
| **Cursor** | Assisted read/write; navigation; checklist verification; ATLAS ref lookup support | Те же классы — read-heavy; write только по operator act |
| **ChatGPT** | Assisted reasoning; enrollment discipline; topology orientation; duplication-risk review | Те же классы — read-only assistance |

### Explicitly NOT consumers in Wave 1

| Non-consumer | Implication for serialization |
|--------------|-------------------------------|
| Runtime / workflow engine | Нет требования machine-parseable schema |
| API / automation | Нет contract-first JSON obligation |
| Validator CLI (RT-G11) | Post-MVP; human-operated integrity sufficient |
| ATLAS runtime service | Refs only (RC-01); no mechanical sync |

### Per-class consumer map

| Class | Primary reader(s) | Read pattern | Write authority |
|-------|-------------------|--------------|-----------------|
| **LOC-ZONE** | Operator | Navigate portfolio root | Operator authorization (Gate 0-3) |
| **LOC-HOME** | Operator, Cursor | Locate pilot project home | RT-G04 creation act |
| **POC-01** | Operator, Cursor | Identity shell discovery | Playbook 01 bind + RT-G10 |
| **POC-02(m)** | Operator, Cursor | Manifest binding carrier — hosts MOC-* | RT-G10 bind act |
| **POC-09** | Operator, Cursor, ChatGPT | Topology/external locators | Operator maintains refs |
| **MOC-01** | Operator, Cursor, ChatGPT | «Start here» entry anchor (MRDY-06, C3) | Operator manifest bind |
| **MOC-02** | Operator, Cursor | Factory Project identity (distinct from `atlas_project_ref`) | Operator bind |
| **MOC-03** | Operator, ChatGPT | Production scope categories — **not** org identity | Operator bind |
| **MOC-04** | Operator | Declared lifecycle endpoint category | Operator bind |
| **MOC-05** | Operator | Scope applicability doctrine | Operator bind |
| **MOC-06** | Operator | `site_type_code` etc. when mandated (Core 5 LANDING pilot) | Operator bind |
| **MOC-08** | Operator, Cursor | Topology map — pointers to index loci | Operator bind |
| **MOC-10** | Operator | Playbook 01 enrollment bind metadata | Operator bind |
| **MOC-12** | Operator, Cursor, ChatGPT | External refs + ATLAS `atlas_*_ref` when known | Operator bind |

### Consumer verdict

Все Wave 1 consumers — **human или AI-assist text consumers**. Markdown **оптимален** для этой аудитории. Machine-oriented formats **не требуются** ни одним primary consumer в Wave 1.

---

## Markdown Suitability Review

### Capability obligations

| Capability | Wave 1 proof | Markdown suitability |
|------------|--------------|----------------------|
| **C2** — Persistence substrate | LOC-ZONE exists; operator can read/write Factory Project records in authorized zone | **Sufficient.** LOC-ZONE/LOC-HOME — filesystem loci (directories). POC/MOC content — structured Markdown records within loci. DF-02 (filesystem + structured artifacts) satisfied. |
| **C3** — Manifest persistence | MOC-01 single canonical entry anchor; MRDY categories in MOC-02…05, 08, 10, 12 | **Sufficient.** All MOC classes carry categorical/text/pointer content per RT-G10 spec. Markdown headings, tables, lists, and labeled fields express MRDY categories without schema engine. |

### Normative constraints satisfied by Markdown

| Constraint | Source | How Markdown satisfies |
|------------|--------|--------------------------|
| Class separation on disk | COL-02, POC-RULE-02, MOC-RULE-02, REL-13 | **Separate physical files per record class** — format-agnostic rule; Markdown does not force mega-record |
| No mega-record anti-pattern | R-W1-08, R-08 | One file (or bounded file set) per class — not one file swallowing MOC + POC planes |
| ATLAS refs as pointers | RC-01, ENROLL-ATLAS-01, OBL-M-12 | Named fields (`atlas_client_org_ref: ORG-0004`) in Markdown — convention, not schema |
| Enrollment-before-bind | INT-M01, MOC-10 | Narrative + metadata sections in Markdown |
| Human-only mutation | INT-08, OA-ACT-04 | Operator edits Markdown — no parser gate required |
| Physical guarantees class-level | GUAR-02, GUAR-M02 | Guarantees explicitly **not format-specific** |

### Corpus precedent

Website Factory canonical corpus уже **Markdown-first**: charters, playbooks, physical specifications, ATLAS adoption, Legal Entity Card template. Wave 1 operational records **продолжают** установленную дисциплину — не вводят новый форматный контур.

### Markdown suitability verdict

**Markdown satisfies C2 and C3** for Wave 1 **without qualification**. No normative specification clause **requires** JSON, YAML, or binary serialization for Wave 1 inventory.

---

## Alternative Format Review

### JSON

| Dimension | Assessment |
|-----------|------------|
| Wave 1 necessity | **Not required.** No runtime consumer; no API contract; no validator CLI gate. |
| Advantage | Structured parsing for future automation |
| Disadvantage | Lower human readability; git diff noise; contradicts documentation-first owner decision without compensating Wave 1 benefit |
| Verdict | **Deferred** — may be reconsidered post-MVP if RT-G01/RT-G11 automation authorized |

### YAML

| Dimension | Assessment |
|-----------|------------|
| Wave 1 necessity | **Not required** as primary format. |
| Partial use | YAML frontmatter **optional** for repeated key-value fields (`atlas_*_ref`, identity ids) within Markdown files — **soft convenience**, not mandatory exception |
| Disadvantage | Indentation fragility; homonym risk with Passport anti-pattern (MAP-03) if YAML becomes mega-document |
| Verdict | **Optional adjunct only** — not a Wave 1 lock variant |

### Spreadsheet

| Dimension | Assessment |
|-----------|------------|
| Wave 1 necessity | **Not required.** Wave 1 has exactly one pilot project — no portfolio catalog (ROC-* deferred to Wave 2). |
| Wave 2+ note | Portfolio catalog **may** use spreadsheet for operator convenience — **out of Wave 1 scope** |
| Verdict | **Excluded** from Wave 1 serialization lock |

### Hybrid (Markdown + structured adjunct)

| Pattern | Wave 1 disposition |
|---------|---------------------|
| Markdown body + YAML frontmatter | **Permitted, not required** |
| Markdown per class + JSON sidecar | **Not recommended** — adds maintenance without Wave 1 consumer |
| Single hybrid mega-file | **Forbidden** — violates COL-02 / mega-record guard regardless of format mix |

### Alternative format verdict

**No alternative format is required for Wave 1.** Owner Markdown preference stands **unchallenged** by objective necessity.

---

## Artifact Class Review

Normative rule **SER-W1-01:** Each row below recommends **serialization class** (format family), **not** file layout, naming, or folder structure — explicitly out of scope for this strategy.

| Class | Physical role (Wave 1) | Recommended serialization class | Rationale | Exception? |
|-------|------------------------|--------------------------------|-----------|------------|
| **LOC-ZONE** | Authorized filesystem root | **Infrastructure locus** (directory) — not a serialized document | DF-03 bounded zone; C2 = zone existence | No |
| **LOC-HOME** | Per-project record home | **Infrastructure locus** (directory) — not a serialized document | P1, POC-RULE-01 | No |
| **POC-01** | Identity shell | **Markdown** | Stable identity reference; minimal fields; human-discoverable | No |
| **POC-02(m)** | Manifest binding carrier | **Markdown** (carrier manifest; hosts MOC-* as separate class files or clearly delimited sections **within separate class files**) | COL-02 requires distinct record class — carrier may be index file pointing to MOC files | No |
| **POC-09** | Topology/external ref index | **Markdown** | Locator lists; pointer-only discipline (RR-01…04) | No |
| **MOC-01** | Entry anchor | **Markdown** | MVP hinge; «start here» discoverability; MRDY-06 | No |
| **MOC-02** | Factory Project identity | **Markdown** | Categorical identity reference; distinct from `atlas_project_ref` | No |
| **MOC-03** | Scope categories | **Markdown** | Production intent tiers — not org registry duplication | No |
| **MOC-04** | Endpoint category | **Markdown** | Declared lifecycle endpoint as category | No |
| **MOC-05** | Applicability doctrine | **Markdown** | Full vs partial applicability text | No |
| **MOC-06** | Classification anchors | **Markdown** | `site_type_code: LANDING` etc. — key-value labels sufficient | No |
| **MOC-08** | Topology map | **Markdown** | Map-of-maps as structured lists/tables pointing to loci | No |
| **MOC-10** | Enrollment bind metadata | **Markdown** | Links to Playbook 01 doctrinal act; narrative + dates | No |
| **MOC-12** | External refs + ATLAS refs | **Markdown** | RC-01 named fields; pointer locators | No |

### Class separation rule (normative for execution, not layout)

```text
  COL-* discipline (inherited):
    ├── Each POC record class → distinct physical carrier
    ├── Each MOC record class → distinct physical carrier (or MOC set within POC-02(m) carrier as separate files)
    └── Forbidden: one serialized blob = POC-02(m) + MOC-08 + POC-03 proxy
```

**COL-04:** Serialization format choice **does not** determine co-location — class separation **is normative**. Markdown-first **does not relax** this rule.

### Artifact class verdict

**All Wave 1 artifact classes: Markdown** (or infrastructure directory for LOC-*). **Zero exceptions** with strong machine-serialization need.

---

## Risk Review

| ID | Risk | Severity | Markdown-first mitigation |
|----|------|----------|---------------------------|
| **R-SER-01** | Mega-record — single Markdown file swallows multiple classes | **HIGH** | Enforce COL-02 at execution: one class per carrier; strategy locks class separation regardless of format |
| **R-SER-02** | ATLAS duplication — org facts in MOC-03 prose instead of MOC-12 refs | **HIGH** | RC-01, ENROLL-ATLAS-01 — format-agnostic; ChatGPT assist reviews field placement |
| **R-SER-03** | Serialization lock-in blocks future runtime | **MEDIUM** | GUAR-02/GUAR-M02: guarantees are class-level; future migration path = extract/transform, not spec violation |
| **R-SER-04** | AI parse ambiguity — inconsistent Markdown field labels | **MEDIUM** | Adopt RC-01 field names literally; operator template discipline at execution |
| **R-SER-05** | Git diff noise on large Markdown amendments | **LOW** | MOC-11 append-oriented amendments; separate files per class limit blast radius |
| **R-SER-06** | False «machine-ready» narrative from YAML frontmatter | **LOW** | Frontmatter optional; S9 non-claims preserved — no runtime implied |
| **R-SER-07** | v0↔v1 corpus mixing during assisted writes | **LOW** | OQ-OM06 routing; reference-v1 zone only for operational records |
| **R-SER-08** | Inconsistent Markdown dialect breaks Cursor/ChatGPT reads | **LOW** | Follow existing repo conventions (headings, tables, `key: value` labels) |

### Risk summary

| Category | HIGH | MEDIUM | LOW |
|----------|------|--------|-----|
| Serialization risks | 2 | 2 | 4 |

**Interpretation:** HIGH risks are **preventable at execution** via COL-* discipline and ATLAS-first enrollment — **not** indicators that Markdown-first should be rejected.

---

## Future Compatibility Review

### Wave 2 (Registry + Surface scaffold)

| Element | Markdown-first impact |
|---------|----------------------|
| ROC-* catalog (RT-G05) | Markdown portfolio index **compatible** — Consolidation Review lists Markdown index as DF-07 option |
| POC-03…05 index scaffold | Empty Markdown shells sufficient at NEW_PROJECT |
| SOC-* read bind (RT-G12) | FF-01…05 form-factor **agnostic** — Markdown index explicitly supported |

**Verdict:** Markdown-first **does not block** Wave 2.

### Wave 3 (Playbook 04/05 population)

| Element | Markdown-first impact |
|---------|----------------------|
| POC-06 declaration records | Append-oriented Markdown sections satisfy INT-01/P7 |
| POC-07 progression ledger | Chronological Markdown entries — human-auditable |
| POC-08 closure | Markdown metadata sufficient |

**Verdict:** Markdown-first **does not block** Wave 3. Append-heavy indexes may later adopt JSONL **if** automation authorized — **optional evolution**, not Wave 1 prerequisite.

### Registry / Surface / Future runtime

| Future system | Compatibility posture |
|---------------|----------------------|
| RT-G11 Validator CLI | May ingest Markdown or derived JSON — **post-MVP**; specs defer validators |
| RT-G01 Workflow engine | Would require adapter layer — **not designed**; SC-01 guard |
| ATLAS mechanical integration | Ref fields extractable from Markdown — RC-01 naming stable |
| Database / multi-tenant | Explicitly out of MVP scope (DF-02, TX-06) |

**Principle FC-01:** Physical guarantees (GUAR-02, GUAR-M02) are **class-level and locus-level — not format-specific**. Markdown-first **does not foreclose** future machine formats; it **defers** them until a consumer with objective need exists.

### Future compatibility verdict

Markdown-first **does not block** Wave 2, Wave 3, Registry, Surface, or hypothetical future runtime. **Migration cost acknowledged** (MEDIUM, R-SER-03) — acceptable under documentation-first owner decision and MVP human-operated model.

---

## Serialization Lock Recommendation

### Options evaluated

| Option | Assessment |
|--------|------------|
| **Markdown-only** | Valid for Wave 1; slightly over-constrains optional YAML frontmatter convenience |
| **Markdown-first** | **Recommended** — aligns with owner decision; permits optional structured adjunct without mandatory JSON/YAML |
| **Hybrid** (mandatory mix) | **Not justified** — no Wave 1 class requires mandatory non-Markdown serialization |
| **Other** | **Not applicable** |

### Recommendation

**Lock: Markdown-first**

| Lock element | Normative content |
|--------------|-------------------|
| **Primary format** | Markdown (`.md`) for all Wave 1 serialized record classes |
| **Infrastructure** | LOC-ZONE, LOC-HOME as directories — not format decision |
| **Class separation** | COL-01…COL-04 mandatory — **separate physical carrier per record class** |
| **ATLAS fields** | RC-01 literal field names in Markdown body or optional YAML frontmatter |
| **Optional adjunct** | YAML frontmatter **permitted** for key-value blocks — **not required**, **not a separate class format** |
| **Forbidden** | JSON/YAML/Spreadsheet as **mandatory** Wave 1 formats; mega-record; Passport pattern |
| **Deferred** | Machine-oriented serialization for RT-G01/RT-G11/post-MVP — separate authorization |

### Justification

1. Owner decision is **authoritative** and **validated** against all primary inputs — no strong counter-evidence.
2. All Wave 1 consumers are **text/human/AI-assist** — not machine parsers.
3. Specifications **explicitly defer** serialization format to creation era and state guarantees are **format-agnostic**.
4. Canonical corpus **already Markdown-first** — consistency reduces R-SER-07.
5. COL-* class separation is the **binding constraint** — satisfied by Markdown with disciplined file/class mapping at execution.

### Operator acknowledgment (closes Gate G1-1)

Operator **should explicitly acknowledge** this lock before Wave 1 Step 1. Acknowledgment = adoption of **Markdown-first** + **COL-* class separation** — **not** adoption of specific file layout (deferred to execution task).

---

## Creation Era Impact

### Gates affected

| Gate | Status after strategy approval |
|------|-------------------------------|
| **G0-1…G0-2, G0-4…G0-6** | Already met per Bootstrap Execution Plan |
| **G0-3** | **Pending** — explicit operator authorization for disk writes |
| **G1-1** | **Resolvable** — this strategy provides serialization convention; operator acknowledgment closes gate |
| **G1-2…G1-5** | Unchanged — pilot selection, ATLAS research, Playbook 01 readiness |

### May Wave 1 begin?

| Condition | Status |
|-----------|--------|
| Serialization strategy complete | **Yes** — this document |
| Serialization objectively sufficient | **Yes** — Markdown-first validated |
| Exceptions identified | **None mandatory** |
| Physical artifacts exist | **No** — correct; strategy only |
| Operator disk-write authorization | **Pending** (G0-3) |

**Verdict:** Wave 1 creation **may proceed immediately after**:

1. Operator acknowledgment of **Markdown-first** lock (G1-1), and  
2. Explicit operator authorization for physical creation (G0-3).

No additional serialization specification track is **required** before Wave 1 bootstrap execution.

### What this strategy does NOT authorize

- Disk writes  
- Folder creation  
- Record materialization  
- Git commit/push  

---

## Explicit Non-Claims

This serialization strategy **does not** claim:

- Any **physical artifact**, folder, manifest record, registry entry, or binding **was created**.
- `workspaces/website-factory-operations/` **exists** on disk — verified **absent** per Bootstrap Execution Plan.
- **Specific file names**, folder trees, internal layouts, or naming conventions **were defined** — execution-time operator/tooling choice under COL-* rules.
- **JSON schemas**, YAML schemas, database structures, or APIs **were designed**.
- Website Factory **runtime**, workflow engine, automation, or validator CLI **exist** or **were required** for Wave 1.
- **Markdown-only** lock — recommendation is **Markdown-first** with optional frontmatter adjunct.
- Mechanical ATLAS integration **is Wave 1-required** — refs are convention-only (RC-01).
- ORG-0004 / PRJ-0008 / WEB-0009 are **live attested canonical on a runtime ATLAS service** — **SAFE UNKNOWN** (documentation-level only).
- This strategy **authorizes** disk writes — **separate operator authorization** required (Gate 0-3).
- Any **git commit, push, tag, or branch** was performed.
- Accepted architecture, specifications, playbooks, or owner decision **were overridden**.

This strategy **does** claim (evidence-based):

- Wave 1 **can** be implemented with **Markdown-first** serialization.
- **No mandatory exceptions** exist for Wave 1 artifact classes.
- **C2** and **C3** obligations are **satisfied** by Markdown with COL-* class separation.
- **Markdown-first does not block** Wave 2, Wave 3, Registry, Surface, or future runtime evolution.
- Gate **G1-1** **can be closed** upon operator acknowledgment of this lock.
- Wave 1 **may begin** after G0-3 + G1-1 acknowledgment — **no further serialization design** required.

---

*Website Factory Wave 1 Serialization Strategy v1 — strategy only. Canonical location: `workspaces/website-factory-reference-v1/WAVE-1-SERIALIZATION-STRATEGY-v1.md`. Git: no commit, no push.*

---

# REPORT — Wave 1 Serialization Strategy v1

**Stage:** Physical MVP Artifact Creation Era — Wave 1 Serialization Strategy  
**Deliverable:** `workspaces/website-factory-reference-v1/WAVE-1-SERIALIZATION-STRATEGY-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/WAVE-1-SERIALIZATION-STRATEGY-v1.md` (created)  
**Summary:** Проведён serialization consumer review; подтверждена достаточность Markdown для C2/C3; альтернативные форматы (JSON/YAML/Spreadsheet) не обязательны для Wave 1; для всех 14 Wave 1 artifact classes рекомендован Markdown (LOC-* как directory loci); риски и future compatibility оценены; рекомендован lock **Markdown-first**; Wave 1 может начаться после G0-3 + operator acknowledgment G1-1 — без создания артефактов.  
**Git:** no commit, no push (per task).  
**UNKNOWN:** operator calendar for G0-3 acknowledgment; whether operator will adopt optional YAML frontmatter adjunct at execution.
