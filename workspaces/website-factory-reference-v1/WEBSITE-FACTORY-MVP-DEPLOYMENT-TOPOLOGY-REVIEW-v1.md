# REPORT — Website Factory MVP Deployment Topology Review v1

**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/` (канон) + контекст `projects/mars-website-factory/`, `C:\AI MARS` (MARS repo)  
**Тип:** deployment topology review only — **без** выбора топологии, **без** RT-G04 design, **без** storage/runtime/UI/implementation design  
**Метод:** синтез принятых артефактов (MVP Definition Review, Implementation Planning Review, Operational Model, Manifest/Registry/Tracking Surface charters, Playbooks 01–05) в decision-quality анализ физических вариантов размещения MVP  
**Принятая реальность (контекст задачи):** Foundation Era **COMPLETE**; Engine Architecture **COMPLETE**; Post-Engine Doctrine **COMPLETE**; Governance Synchronization **COMPLETE**; Operational Design **COMPLETE**; MVP Definition **COMPLETE**; RT-G04/05/10/12 implementation **NOT STARTED**; shipped Factory runtime **отсутствует**

---

## Executive Summary

**Вердикт review:** MVP Website Factory **должен где-то физически существовать**, но **ни одна топология не выбрана** в этом deliverable. Принятая MVP-граница требует **единого persistence substrate** (C2 / RT-G04) для Manifest, Registry, Tracking Surface visibility и manual declaration writes — при **одном operator**, **Core 5**, **без** workflow engine и **без** shipped Factory runtime product.

**Где MVP *может* жить (классы, не решение):**

| ID | Topology class | Краткая суть |
|----|----------------|--------------|
| **A** | Git + Markdown only | MVP как авторизованные markdown-артефакты в git; минимальная физическая привязка |
| **B** | Filesystem + structured artifacts | Локальный file-backed слой со structured records (format **не** определяется здесь) |
| **C** | Website Factory workspace inside MARS | Явная Factory-зона внутри `C:\AI MARS` (канон +/или operational pack) |
| **D** | HomeGateway-integrated MVP | Factory persistence/read path частично или полностью через HomeGateway program |
| **E** | Standalone Factory application | Отдельное приложение/сервис вне MARS repo discipline |
| **F** | Hybrid documentation-first | Документация-first baseline + точечная materialization bound planes |

**Ключевой вывод для RT-G04:** RT-G04 charter **не может** быть ответственно **авторизован** без **owner topology decision** по крайней мере по трём осям: **(1)** repo/host locus, **(2)** markdown vs structured substrate class, **(3)** integration stance (standalone vs MARS-embedded vs HomeGateway-adjacent). Этот review **закрывает анализ опций**; **не закрывает** owner decision.

**Final recommendation (одна):** **A — Topology decision required before RT-G04** (см. [Final Recommendation](#final-recommendation)).

**Explicit scope:** Этот документ **не выбирает** топологию, **не проектирует** RT-G04 и **не создаёт** implementation plans.

---

## Topology Requirements

Требования **только** из [WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md](WEBSITE-FACTORY-MVP-DEFINITION-REVIEW-v1.md) и связанных принятых артефактов. **Новые требования не добавляются.**

### Must support (MVP capability floor)

| Req ID | Requirement | MVP anchor | Topology implication |
|--------|-------------|------------|----------------------|
| **TR-01** | **Единый persistence substrate** для Factory Project records operator может **читать и вручную обновлять** | C2; RT-G04 | Нужен **один авторизованный physical locus** — не scatter |
| **TR-02** | **Per-project Manifest binding**: entry anchor + minimum understanding categories (MRDY-*) **стабильны** | C3; RT-G10 impl; Manifest Charter | Substrate хранит **per-project** manifest records; **не** live gate index (MT-01) |
| **TR-03** | **Registry binding**: portfolio catalog, distinction summaries, pointer to Manifest | C4; RT-G05 impl; Registry Charter; Playbook 02 | Substrate или согласованный index **перечисляет** enrolled projects |
| **TR-04** | **Surface binding**: operator отвечает на **все восемь** visibility questions **без** full workspace search | C5; RT-G12 impl; Surface Charter SRDY-* | Read path к bound data; **не** gate evaluation |
| **TR-05** | **Manual declaration path**: Playbook 04 writes — human/assisted, **не** automated | C6; DA-01; OA-ACT-04 | Write path под operator control; external systems **не** mutating indexes |
| **TR-06** | **Closure persistence**: Playbook 05 terminal outcomes **фиксируемы** | C7; OCM-* | Substrate принимает closure metadata |
| **TR-07** | **Single-operator scope**: один Factory operator; single-machine / single-repo discipline допустима | C8; OR-* | **Не** требует multi-tenant DB, RBAC, queue |
| **TR-08** | **Core 5 constraint** для MVP demonstration | C9; OR-06 | Topology **не** зависит от extended types |
| **TR-09** | **Full lifecycle** Playbooks 01→02→03↔04→05 **исполним** с bound planes | MVP success S1–S9 | Topology должна пропускать **весь** operator path |
| **TR-10** | **Authority preserved**: operator sole declarer; Surface read-only; Registry ≠ tracking depth | Charters MA-*, RA-*, TS-* | Topology **не** создаёт второй SoT или auto-mutation |

### Must NOT require (MVP exclusions — topology must not force)

| Excl ID | Exclusion | Topology must avoid |
|---------|-----------|---------------------|
| **TX-01** | Workflow engine (RT-G01) | Topology **не** предполагает orchestrator as locus |
| **TX-02** | Automation mutating indexes (RT-G03) | **Не** CI/git-triggered SoT |
| **TX-03** | Validator CLI as gate authority (RT-G11) | **Не** validation product as persistence owner |
| **TX-04** | Queue / multi-operator concurrency (RT-G06/G14) | **Не** shared multi-tenant runtime |
| **TX-05** | Engine runtime product (RT-G09 impl) | **Не** «Factory runtime» narrative from placement alone |
| **TX-06** | Database / multi-tenant storage **as MVP requirement** | MVP Definition: file-backed single-operator **sufficient** |
| **TX-07** | Operator dashboard product / SaaS | RT-G12 = minimum read binding only |
| **TX-08** | Registry enrollment by git folder scan | RAP-10, RD-04 — enrollment **declared**, not discovered |

### Dependency order (planning-level — from Implementation Planning Review)

```text
  Topology constraints (OWNER — this review informs)
           │
           ▼
  RT-G04 persistence substrate charter
           │
           ├──▶ RT-G10 manifest impl
           │         │
           │         ├──▶ RT-G05 registry impl
           │         │
           │         └──▶ RT-G12 surface read binding
           │
           └──▶ declaration/session writes (Playbooks 03–04)
```

### Pre-MVP baseline (context, not requirement)

Documentation-first Factory **уже работает** без physical binding (Operational Design Consolidation; Implementation Planning §Operational Continuity). MVP topology **заменяет ad-hoc scatter**, **не** создаёт новую doctrine.

---

## Candidate Topology Review

Для каждого кандидата: **что это**, **сильные стороны**, **слабые стороны**, **риски**, **alignment с MVP boundaries**. **Выбор не делается.**

### A — Git + Markdown only

**Описание:** MVP живёт как **авторизованный набор markdown-документов** (и git history) в существующем репозитории. Manifest, Registry index, declaration/tracking notes — markdown files с operator-maintained structure. Read surface = markdown navigation / search / generated static index (**form не проектируется**).

| Dimension | Assessment |
|-----------|------------|
| **Strengths** | Наиболее **консervative**; нулевой deployment footprint; полная audit trail через git; идеально matches «single operator + single-repo»; Playbooks уже markdown-native; **не** создаёт runtime product |
| **Weaknesses** | Риск **ad-hoc scatter** если paths не авторизованы (OQ-OM01); structured queries для eight Surface questions **тяжелее** без convention; dual corpus (v0/v1) confusion без routing |
| **Risks** | SC-09 v0↔v1 ID mixing; operators treat **any** markdown as Registry (RAP-10); conflation with general MARS docs |
| **MVP alignment** | **High** для C2–C7 если paths **authorized**; C5 depends on disciplined index structure — **operator burden** |
| **Premature runtime** | **Low** — no app, no DB, no workflow |

**Typical locus (illustrative, not decision):** `workspaces/website-factory-reference-v1/` factory-records zone **or** dedicated subtree under MARS — **OWNER DECISION REQUIRED** (OQ-OM01).

---

### B — Filesystem + structured artifacts

**Описание:** MVP на **локальном file-backed слое** с **structured records** (JSON/YAML/SQLite file — **format explicitly out of scope**). Git may version artifacts. Operator reads/writes via editor, CLI helper, or lightweight local tool (**tool design out of scope**).

| Dimension | Assessment |
|-----------|------------|
| **Strengths** | Clear **RT-G04** semantics; easier machine-assisted read for RT-G12 **without** workflow engine; separates Factory SoT from narrative docs; evolution path to RT-G07 logs |
| **Weaknesses** | Higher **implementation pressure** than pure markdown; schema/format decisions **deferred but inevitable** at RT-G10/05 charter; risk of over-engineering structured store |
| **Risks** | SC-01 conflating persistence with «shipped runtime»; SC-06 smuggling storage design into doctrine; validators/CI writing structured files (TX-02) |
| **MVP alignment** | **High** if bounded to C2–C7; best supports C5 read binding **if** read path stays read-only |
| **Premature runtime** | **Medium** — structured artifacts invite tooling/scripts; discipline required to keep human-only writes |

---

### C — Website Factory workspace inside MARS

**Описание:** MVP **физически привязан** к явной **Factory workspace zone** внутри MARS monorepo — канонический контур `workspaces/website-factory-reference-v1/` и/или operational pack `projects/mars-website-factory/`, плюс per-client `workspaces/*` как **external pointers only**.

| Dimension | Assessment |
|-----------|------------|
| **Strengths** | Matches **existing two-contour architecture** (Architecture Consolidation Review); Foundation + Engine canon already colocated; git + operator Cursor sessions natural; ATLAS lists Website Factory as known consumer — **future** alignment possible without MVP scope |
| **Weaknesses** | **Dual corpus** tension: v1 canon vs v0 operational pack; client workspaces (`workspaces/triumph-*`) **не** Factory SoT; OQ-OM01/OQ-OM06 unresolved |
| **Risks** | Mixing **Site Type Registry** (`registry/`) with **Factory Project Registry** (RAP-11); lane A frontend (`src/`) mistaken for Factory persistence; repo size / unrelated MARS churn |
| **MVP alignment** | **High** as **placement** — independent of A vs B artifact class inside zone |
| **Premature runtime** | **Low–Medium** — MARS repo contains many programs; Factory must stay **bounded zone** |

**Note:** C is largely **location policy** combinable with A or B. **OWNER DECISION REQUIRED:** canon-only vs operational-pack vs new `factory-projects/` root.

---

### D — HomeGateway-integrated MVP

**Описание:** Factory MVP persistence and/or RT-G12 read surface **hosted by or routed through** HomeGateway program (`projects/homegateway-v4-ai/`, future `workspaces/homegateway-v4-ai/v1`).

| Dimension | Assessment |
|-----------|------------|
| **Strengths** | Unified operator cockpit narrative; HomeGateway README already positions Factory projects as **content overview**, not orchestration; potential future executive visibility |
| **Weaknesses** | HomeGateway registry status **planned** vs heavy WIP — **SAFE UNKNOWN** operational maturity; couples two programs' MVP timelines; HG consumer model **PARTIAL** (OPS-GOVERNANCE-READINESS) |
| **Risks** | **HIGH premature runtime/UI pressure** — HG is UI-forward; SC-07 over-built dashboard; Factory SoT **inside** another product violates Engine boundary if HG mutates indexes; ATLAS/HomeGateway consumption **SAFE UNKNOWN** |
| **MVP alignment** | **Partial** — HG aligns with portfolio **visibility** metaphor but MVP **must not** require dashboard product (TX-07); Playbook 03 **forbids** UI in playbook |
| **Premature runtime** | **HIGH** — integration implies shell, modules, MVP v1 tooling already in HG tree |

**Evidence boundary:** HomeGateway **does not** claim Factory orchestration today (`product-positioning-v0.1.md`). Integration is **future charter territory**, not proven runtime.

---

### E — Standalone Factory application

**Описание:** MVP as **separate application** — local desktop app, dedicated microservice, or **separate git repository** outside MARS monorepo discipline.

| Dimension | Assessment |
|-----------|------------|
| **Strengths** | Hard boundary from MARS noise; freedom to evolve post-MVP runtime (Tier 2) without repo coupling; clear «product» mental model for some operators |
| **Weaknesses** | **Highest** delivery surface: install, deploy, versioning, backup; splits canon docs (in MARS) from SoT (outside) — **reference topology** drift; contradicts single-repo MVP assumption (C8 **allows** but doesn't require) |
| **Risks** | SC-01 **strong** — standalone app **reads as** Factory runtime product (TX-05); duplicate governance; ATLAS/MARS consumer alignment harder |
| **MVP alignment** | **Medium** functionally, **Low** governance fit with accepted dual-contour MARS model |
| **Premature runtime** | **HIGH** — application shell ≈ RT-G09 narrative |

---

### F — Hybrid documentation-first topology

**Описание:** **Explicitly retain** documentation-first baseline; add **minimal authorized materialization** only for Manifest anchor, Registry catalog, and declaration index — rest stays in existing markdown/playbook discipline. Pre-MVP scatter **replaced incrementally**, not big-bang app.

| Dimension | Assessment |
|-----------|------------|
| **Strengths** | **Best matches** Implementation Planning «MVP delta» wording; lowest disruption to operators already running Playbooks; evolution toward B without forcing E; honors «MVP ≠ runtime» |
| **Weaknesses** | **Ambiguity** without owner rules on what stays doc-only vs bound; two-speed system during pilot; requires strict **authorized path list** (OQ-OM01) |
| **Risks** | Permanent hybrid if evolution never chartered; operators continue workspace archaeology for **non-bound** classes |
| **MVP alignment** | **Very high** — closest to accepted operational continuity review |
| **Premature runtime** | **Low** if materialization stays file/markdown-level |

**Note:** F often combines **C (MARS locus) + A or B (artifact class) + phased binding**.

---

### Additional candidate (justified): G — Per-project workspace colocation

**Описание:** Manifest/registry/tracking bindings **live inside each client workspace** (`workspaces/<client>/factory/`) with **optional** portfolio aggregator elsewhere.

| Justification | Registry Charter OQ-R01 («artefact vs distributed pointers») explicitly OPEN; some pilots (Triumph) already workspace-heavy |

| Dimension | Assessment |
|-----------|------------|
| **Strengths** | Colocation with layer work; natural external workspace pointers (ER-06) |
| **Weaknesses** | **C4 portfolio discoverability** harder without central catalog; violates spirit of «single substrate» (TR-01) unless aggregator mandatory |
| **Risks** | RAP-10 folder-as-enrollment; **Registry substitutes Tracking** if per-project files grow unchecked |
| **MVP alignment** | **Low–Medium** for full MVP mission (catalog in scope) |
| **Premature runtime** | **Low** |

Included for OQ-R01 decision space — **not recommended as default** by this review (no topology chosen).

---

## Complexity Review

| Topology | Operational complexity | Governance complexity | Implementation pressure | Maintenance burden |
|----------|------------------------|----------------------|-------------------------|-------------------|
| **A** Git+MD | **Low** — editor + git | **Medium** — path authority, dual corpus | **Low** | **Low** — operator markdown hygiene |
| **B** FS+structured | **Medium** — format + write discipline | **Medium** — charter for formats (RT-G10/05) | **Medium** | **Medium** — schema drift, migrations later |
| **C** MARS workspace | **Low–Medium** — repo navigation | **High** — v0/v1, canon vs pack, many programs | **Low** (placement only) | **Medium** — repo churn, unrelated edits |
| **D** HomeGateway | **High** — two programs | **High** — consumer contracts, HG maturity UNKNOWN | **High** | **High** — UI/product coupling |
| **E** Standalone app | **High** — deploy/install | **High** — split repo governance | **Very high** | **Very high** |
| **F** Hybrid doc-first | **Medium** — two tiers explicit | **Medium** — must define bound vs unbound | **Low–Medium** | **Medium** — risk of stuck hybrid |
| **G** Per-project colocation | **Medium** — N workspaces | **High** — distributed SoT | **Medium** | **High** — portfolio sync |

**Summary:** Lowest complexity = **A, F** (with authorized paths). Highest = **D, E**. **C** adds governance complexity even when artifact class is simple.

---

## MVP Alignment Review

Legend: **Strong** / **Adequate** / **Weak** / **Misaligned**

| Topology | Manifest (C3) | Registry (C4) | Tracking Surface (C5) | Single operator (C8) | Manual declarations (C6) |
|----------|---------------|---------------|-------------------------|----------------------|--------------------------|
| **A** Git+MD | **Strong** | **Adequate** | **Adequate** — depends on index discipline | **Strong** | **Strong** |
| **B** FS+structured | **Strong** | **Strong** | **Strong** | **Strong** | **Strong** — if writes manual |
| **C** MARS workspace | **Strong** (placement) | **Strong** | **Adequate–Strong** | **Strong** | **Strong** |
| **D** HomeGateway | **Weak–Adequate** | **Adequate** | **Misaligned risk** — dashboard creep | **Adequate** | **Weak** — mutation via UI risk |
| **E** Standalone app | **Adequate** | **Adequate** | **Adequate** | **Adequate** | **Weak** — app implies execution |
| **F** Hybrid | **Strong** | **Strong** | **Adequate** | **Strong** | **Strong** |
| **G** Per-project | **Adequate** | **Weak** without aggregator | **Adequate** | **Strong** | **Strong** |

### Playbook path fidelity (01–05)

| Topology | PB01 Manifest enroll | PB02 Registry | PB03 Surface session | PB04 Declarations | PB05 Closure |
|----------|---------------------|---------------|---------------------|-------------------|--------------|
| **A, B, C, F** | **Full** | **Full** | **Full** with bound read path | **Full** manual writes | **Full** |
| **D** | **Full** doctrinally | **Full** | **At risk** — UI scope creep | **At risk** | **Full** |
| **E** | **Full** | **Full** | **Full** if app read-only | **At risk** | **Full** |
| **G** | **Full** | **Partial** — catalog gap | **Full** per project | **Full** | **Full** |

---

## Premature Runtime Risk Review

| Topology | Runtime pressure | Automation pressure | Workflow engine pressure | UI pressure |
|----------|------------------|--------------------|-------------------------|-------------|
| **A** | **Minimal** | Low — git hooks temptation | **Minimal** | Low — static md index |
| **B** | Low | **Medium** — scripts writing records | Low | Low–Medium — CLI helpers |
| **C** | Low | Low–Medium — MARS CI | Low | Low |
| **D** | **High** | **Medium** — HG signals/automation | **Medium** | **Very high** |
| **E** | **Very high** | **High** | **High** | **High** |
| **F** | **Minimal** | Low if phased | **Minimal** | Low |
| **G** | Low | Low | Low | Low |

### Anti-pattern triggers by topology

| Anti-pattern | Most vulnerable topologies |
|--------------|---------------------------|
| MVP persistence = shipped Factory runtime (SC-01) | **D, E** |
| RT-G12 before RT-G10/04 stable (SC-02) | **D, E** (UI-first teams) |
| Validators/CI replace Playbook 04 (SC-03) | **B, E** (structured + CI) |
| Registry as dashboard / tracking substitute (SC-05) | **D, G** |
| Database before MVP proven (MVP exclusion) | **E**, aggressive **B** |

**Safest against premature runtime:** **A, F** (+ **C** as placement only).

---

## Evolution Review

Post-MVP Tier 1 (RT-G07 logs, RT-G11 validators, templates) and Tier 2 (RT-G01 workflow, RT-G03 automation, RT-G09 runtime product) per MVP Definition Review.

| Topology | Clean evolution toward post-MVP | Forces redesign risk |
|----------|--------------------------------|----------------------|
| **A** | **Good** — add structured layer or tooling incrementally | Markdown-only may **limit** RT-G07/G11 without migration |
| **B** | **Very good** — natural extension | Early schema lock-in |
| **C** | **Very good** — MARS as long-term home for canon + records | Must **separate** Factory zone from frontend `src/` |
| **D** | **Poor** — couples Factory SoT to HG release cycle | **High** if HG pivots |
| **E** | **Medium** — app may fork from MARS canon | **High** split-brain docs vs SoT |
| **F** | **Excellent** — phased materialization matches Tier 1/2 sequencing | Stuck hybrid if phases undefined |
| **G** | **Poor** for portfolio/ATLAS alignment | Central catalog retrofit |

**Evolution principle (from accepted docs):** MVP **closes physical binding gap**; post-MVP **adds** logs, validators, automation **via separate charters**. Topologies **F→B→(future runtime)** and **A→B** preserve this best **without** mandating either path here.

---

## Decision Factors

Factors requiring **owner decision** — **this review does not decide**.

| Factor ID | Decision question | Options space | Why owner-required |
|-----------|-------------------|---------------|-------------------|
| **DF-01** | **Primary repo locus** for Factory MVP records | MARS monorepo zone (C) vs separate repo (E) | OQ-OM01 OPEN; RT-G04 = physical placement |
| **DF-02** | **Artifact class** for substrate | Markdown-only (A) vs structured files (B) vs phased hybrid (F) | Affects RT-G04/10/05 charter scope; SC-06 guard |
| **DF-03** | **Canon vs operational pack** routing | `website-factory-reference-v1` only vs `mars-website-factory` vs new root | OQ-OM06; dual corpus BCP-019 |
| **DF-04** | **Manifest vs tracking co-location** | Same zone vs separated stores | OQ-M04 — implementation charter |
| **DF-05** | **Registry index shape** | Central catalog artefact vs distributed pointers + aggregator | OQ-R01 — affects TR-03 |
| **DF-06** | **HomeGateway integration depth** | None (standalone Factory) vs read-only consumer vs co-hosted UI | HG maturity SAFE UNKNOWN; TX-07 |
| **DF-07** | **RT-G12 read surface form factor** | Markdown index vs CLI vs static HTML vs local UI | Not storage topology but **coupled** to placement; MVP excludes dashboard **product** |
| **DF-08** | **Pilot workspace relationship** | Triumph/external workspaces as pointers only vs partial colocation | OQ-OM07 SAFE UNKNOWN |
| **DF-09** | **Network/hosting** | Single-machine local vs shared git remote only vs hosted service | E and D imply hosting; MVP excludes SLA |
| **DF-10** | **Git versioning policy** for SoT records | All records in git vs gitignore local state | Affects audit vs operator privacy |

**Label:** Each **DF-*** = **OWNER DECISION REQUIRED**

### Decisions explicitly NOT required for this review deliverable

- Field lists, schemas, folder trees (**forbidden**)
- RT-G04 charter text (**next authorized work after DF decisions**)
- Choice among A–G (**forbidden in this task**)

---

## Comparative Assessment

| Label | Topology(ies) | Rationale |
|-------|-----------------|-----------|
| **Most conservative** | **A** (Git + Markdown only) | Zero new runtime; matches pre-MVP operator tooling |
| **Most flexible (post-MVP)** | **B** or **F→B** | Structured evolution without standalone app |
| **Highest risk** | **D** (HomeGateway), **E** (Standalone app) | Runtime/UI narrative; split governance; SC-01/SC-07 |
| **Highest complexity** | **E**, then **D** | Deploy, product coupling, consumer UNKNOWNs |
| **Best MVP mission fit (class)** | **F** (Hybrid documentation-first) + **C** (MARS locus) | Matches Implementation Planning MVP delta and operational continuity |
| **Weakest catalog fit** | **G** (Per-project colocation) | TR-03 / C4 without mandatory aggregator |

### Pairwise notes (not rankings)

- **A vs B:** Same locus possible; B trades simplicity for C5 read fidelity and Tier 1 evolution.
- **C vs E:** C keeps canon and SoT under MARS governance; E severs link.
- **F vs A:** F is **policy** (what to materialize); A is **artifact class** — commonly combined.
- **D vs any:** D adds **program dependency** not required by MVP Definition.

---

## Readiness Review

| Question | Assessment |
|----------|------------|
| Is topology **analysis** complete enough for owner decision? | **Yes** — candidates A–G evaluated |
| Is **specific topology selected**? | **No** — intentional; owner must act on DF-01…DF-10 |
| Can operators run MVP **today** without topology decision? | **No** — pre-MVP baseline works **without** MVP; MVP **requires** physical binding (C2) |
| Does Implementation Planning Review assume topology? | **No** — RT-G04 explicitly **NOT STARTED**; charters defer storage |
| Is topology decision **same as** RT-G04 implementation design? | **No** — topology = **where/what class**; RT-G04 charter = **role, boundaries, non-goals** within owner constraints |
| Can RT-G04 **planning discussions** use this review? | **Yes** — immediately |
| Can RT-G04 charter be **authorized** without owner topology constraints? | **No** — would smuggle implicit choices (SC-06) |

### Deferral analysis

| Defer topology entirely? | **Not responsible** — RT-G04 is substrate; unbounded RT-G04 recreates OQ-OM01 scatter |
| Defer **full** topology to post-pilot? | **Partial** — pilot may inform DF-02/07 but **DF-01/03** needed before charter |
| Defer HomeGateway (DF-06)? | **Yes** — default stance for MVP: **no HG SoT** unless owner overrides |

---

## Final Recommendation

### **A — Topology decision required before RT-G04**

**Justification:**

1. **RT-G04 is persistence substrate** — Implementation Planning Review lists it **first** and **prerequisite for all physical bindings**. Substrate charter **cannot** define boundaries without knowing **repo locus** (DF-01), **artifact class** (DF-02), and **integration stance** (DF-06).

2. **Task mission explicitly states** RT-G04 cannot be planned responsibly until deployment topology **options are understood**. This review completes **options understanding**; **owner decision** is the remaining gate — not RT-G04 drafting in parallel with unbounded placement.

3. **MVP Definition requires C2** — without topology constraints, implementation risks **implicit** topology (continued ad-hoc scatter) — **defeats MVP purpose**.

4. **SC-06 guard** — starting RT-G04 charter without topology constraints invites storage/format design to **collapse into** doctrine.

5. **What may proceed now:** MVP Implementation Planning **track** remains authorized (per MVP Definition Review); **this review** is input to owner decision; RT-G04 **planning workshop** may begin **using** DF checklist — but RT-G04 **charter authorization** waits on **OWNER DECISION REQUIRED** for DF-01, DF-02, DF-03 minimum (DF-04–DF-10 may resolve **inside** RT-G04 charter **after** those three).

**Not chosen:** **B — RT-G04 planning may begin before topology selection** — would conflate «planning review complete» with «placement unbounded» and reproduce OQ-OM01 / dual-corpus failures.

---

## Explicit Non-Claims

This review **does not** claim:

- Any **topology was selected** — A–G are **candidates only**.
- Any **implementation spec**, storage model, UI design, schema, file format, folder layout, or code was created.
- A shipped Website Factory **runtime**, workflow engine, validator engine, persistence layer, or operator UI **exists** or **was designed**.
- RT-G04/05/10/12 **implementation** is complete, started, or authorized by this document.
- MVP **has been built** or **demonstrated** — only topology **options analyzed**.
- HomeGateway **is ready** as Factory SoT host — **SAFE UNKNOWN** (planned/WIP per ecosystem census).
- ATLAS integration is MVP-required — ATLAS foundation documents Website Factory as **consumer**; MVP Definition **excludes** MIG/MetaBOT/ORCA integrations.
- Physical manifest files, registry index, or declaration store **exist** in-repo today.
- `projects/mars-website-factory/` v0 registries supersede `website-factory-reference-v1` v1.
- Operators have updated NEXT-PRIORITIES to Implementation Planning / topology era (**UNKNOWN**).
- Triumph or pilot workspaces are deploy-authorized or Factory-terminal in production sense.
- Any accepted artefact was modified — **analysis deliverable only**.

This review **does** claim (evidence-based):

- MVP **must** support TR-01…TR-10 and **must not** force TX-01…TX-08.
- **Seven** evaluated candidates (A–G) span conservative (A, F) through high-risk (D, E).
- **Owner decisions DF-01…DF-10** remain before RT-G04 charter authorization.
- **Topology decision required before RT-G04** (option **A**) is the responsible sequencing recommendation.
- **Hybrid documentation-first (F) inside MARS workspace (C)** aligns best with accepted MVP delta **as a class** — **without selecting it** as the decision.

---

*Website Factory MVP Deployment Topology Review v1 — topology analysis only. Canonical location: `workspaces/website-factory-reference-v1/WEBSITE-FACTORY-MVP-DEPLOYMENT-TOPOLOGY-REVIEW-v1.md`. Git: no commit, no push.*

---

# REPORT — Website Factory MVP Deployment Topology Review v1
