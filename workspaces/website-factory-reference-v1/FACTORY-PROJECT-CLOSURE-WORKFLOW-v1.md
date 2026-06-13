# REPORT — Factory Project Closure Workflow v1

**Версия:** v1  
**Дата:** 2026-06-05  
**Область:** `workspaces/website-factory-reference-v1/`  
**Эра:** Operational Design — **Operational Playbook 05** (Project Closure Workflow)  
**Контекст:** Foundation Era **COMPLETE**; Factory Engine Architecture v1 **COMPLETE**; Post-Engine Doctrine **COMPLETE**; [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) **COMPLETE**; Playbooks 01–04 **COMPLETE**  
**Тип:** operational workflow only — **без** runtime, automation, implementation, storage, schemas, agents, UI  
**Не переопределяет:** Engine Stages 1–6, Runtime Architecture, Manifest/Registry/Tracking Surface charters, Playbooks 01–04  

---

## Purpose

### Зачем существует Project Closure Workflow

**Project Closure Workflow** — пятый операционный playbook Website Factory. Он описывает **человеко-исполняемую** дисциплину, по которой Factory Project **операционно закрывается** — достигает одного из **допустимых terminal или terminal-equivalent outcomes** в scope charter, с явной фиксацией того, **какой класс закрытия** применён и **какие planes** Factory затронуты.

Workflow закрывает координационную проблему **неоднозначного «конца» Factory-track**:

| Проблема | Как workflow решает |
|----------|---------------------|
| Оператор не может отличить «проект готов к deploy» от «Factory-track закрыт» | Нормативные **классы closure** и критерии **COMPLETE vs partial vs suspended** |
| Registry withdrawal, git archive, client go-live подменяют Factory closure | Разделение **Factory-track closure** и **catalog discoverability** |
| Partial charter endpoint смешивается с mid-chain «почти готово» | **Partial closure** требует charter-explicit endpoint + gate-complete prefix |
| Playbook 04 описывает closure как declaration class, но не ритуал **решения о закрытии** | Этот playbook — **специализированный operational path** от assessment до valid closure outcome |
| Rollback history, reconciliation gaps, suspension остаются неявными при «закрытии» | **Prerequisites** и **invalid closure** principles до любого terminal act |

Оператор после применения workflow должен уметь ответить **без чтения всего workspace**:

- Когда closure **разрешён**?
- Когда closure **запрещён**?
- Какие **классы evidence** поддерживают closure?
- Чем **COMPLETE** отличается от **partial closure**, **withdrawal**, **suspension**?
- Как closure влияет на **Manifest**, **Registry**, **Tracking**, **Lifecycle**?

### Что closure workflow **решает** и **не решает**

| Closure workflow **решает** | Closure workflow **не решает** |
|-----------------------------|--------------------------------|
| Когда и как Factory Project **операционно закрывается** в charter scope | Автоматическое исполнение terminal transition — нет enforcement engine |
| Какой **класс closure** применим к данному case | Определение pass/fail criteria gates — Runtime + layers |
| Какие **prerequisites** и **evidence** обязательны перед closure act | Production deploy, hosting, DNS, client go-live |
| Как closure **отражается** в Lifecycle, Tracking, Surface, Manifest orientation, Registry category | Удаление layer artefact bodies или git history |
| Когда closure **invalid** и требует remediation или reconciliation | Catalog enrollment (Playbook 02) как substitute for Engine closure |
| Связь closure с **Playbook 04** declaration bundle (DC-04) | Physical closure forms, closure registry, closure storage |

**Граница playbook:** от **оценки closure readiness** (типично после Playbook 03 session с closure intent) до **valid closure outcome** в логической модели Engine + сопутствующих catalog/Manifest orientation decisions — **без** определения формата записи, хранилища или автоматизации.

```text
  PLAYBOOKS 01–02 (entry)     PLAYBOOK 03 (assessment)     PLAYBOOK 04 (declare)     THIS WORKFLOW (05)
  manifest / catalog                 │                           │                         │
        │                            ▼                           ▼                         ▼
        └──────────▶  Active track ──▶  Closure readiness ──▶  Closure declaration ──▶  Closed Factory track
              (enrolled)              (blockers, class)         (Playbook 04 acts)        (terminal metadata)
```

---

## Foundation Dependencies

Workflow **наследует** принятые артефакты **без их изменения**. При конфликте — побеждает более специфичный model (State, Gate, Lifecycle, Tracking), затем Operational Model.

### Tier 0 — Operational model and Playbooks 01–04

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) | Completion model (OCM-*); exit kinds; human-only closure decisions; Registry/Manifest/Tracking path |
| [FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md](FACTORY-MANIFEST-ENROLLMENT-WORKFLOW-v1.md) | Manifest-enrolled prerequisite; enrollment **не** closure |
| [FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md](FACTORY-REGISTRY-ENROLLMENT-WORKFLOW-v1.md) | Withdrawal vs archived vs closure; RW-05 suspension ≠ auto-withdrawal |
| [FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md](FACTORY-TRACKING-SURFACE-SESSION-WORKFLOW-v1.md) | Типичный **предшественник**: closure readiness assessment |
| [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md) | Closure decision class (DC-04); CL-* principles; declaration prerequisites for closure |

### Tier 1 — Engine composition (обязательные)

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-PROJECT-OBJECT-MODEL-v1.md](FACTORY-PROJECT-OBJECT-MODEL-v1.md) | Identity shell persists after closure; EO-03 declaration truth |
| [FACTORY-PROJECT-STATE-MODEL-v1.md](FACTORY-PROJECT-STATE-MODEL-v1.md) | Terminal `COMPLETE` (CS-03, FT-10); partial endpoint occupancy; `FACTORY_TRACK_SUSPENDED` metadata |
| [FACTORY-GATE-COMPOSITION-MODEL-v1.md](FACTORY-GATE-COMPOSITION-MODEL-v1.md) | Gate-complete (GCO-*); terminal `RG-PROJECT_COMPLETE`; partial endpoint gate-complete |
| [FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md](FACTORY-LIFECYCLE-COMPOSITION-MODEL-v1.md) | LC-13 full completion; LPC-* partial; `FACTORY_TRACK_CLOSED_PARTIAL`; `FACTORY_TRACK_SUSPENDED`; rollback cascade |
| [FACTORY-PROJECT-TRACKING-MODEL-v1.md](FACTORY-PROJECT-TRACKING-MODEL-v1.md) | Terminal display (SV-04); trackability at closure; suspension flag visibility |
| [FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md](FACTORY-ENGINE-SYSTEM-BOUNDARY-v1.md) | Factory ends at declaration + observability — deploy external |

### Tier 2 — Post-Engine doctrine (reference)

| Document | Workflow использует |
|----------|---------------------|
| [FACTORY-PROJECT-MANIFEST-CHARTER-v1.md](FACTORY-PROJECT-MANIFEST-CHARTER-v1.md) | MS-04 terminal COMPLETE ≠ deploy; ML-03 suspension/partial visibility categories |
| [FACTORY-PROJECT-REGISTRY-CHARTER-v1.md](FACTORY-PROJECT-REGISTRY-CHARTER-v1.md) | Archived after terminal/partial closure; withdrawn ≠ Engine deletion; RD cease discoverability |
| [FACTORY-TRACKING-SURFACE-CHARTER-v1.md](FACTORY-TRACKING-SURFACE-CHARTER-v1.md) | VP-03 authoritative = last declared; post-closure Surface must reflect terminal truth |

**Authority precedence:** Runtime + Foundation (criteria) → Engine Stages 1–6 → Operational Model → Playbooks 01–04 → **этот playbook** для **ритуала closure** → implementation charters **не могут** ослабить human-only closure authority.

---

## Closure Authority Principles

### Кто может авторизовать closure (v1)

| Actor | May authorize closure (v1) | May not authorize closure |
|-------|---------------------------|---------------------------|
| **Factory operator** | Все **Factory-track closure** classes по этому playbook; catalog **archived** category after closure; **withdrawal** (Playbook 02 plane) | — |
| **Reviewer / validator** | Attestation layer criteria **как input** к closure evidence | Terminal state, closure gates, `FACTORY_TRACK_*` metadata, catalog withdrawal |
| **Charter author / sponsor** | Charter endpoint / scope content **через** operator-mediated amendment | Direct closure without operator declaration |
| **Client / stakeholder** | Acceptance **как** charter-bound ref — не closure trigger alone | Factory terminal declaration |
| **External systems** (CI, deploy, MIG, agents) | **Никогда** — may prompt operator to **open** closure assessment | Any closure authorization |

### Authority principles (normative)

| ID | Principle |
|----|-----------|
| **CA-01** | **Factory operator** — единственный носитель **обязательных** Factory-track closure declarations (OA-ACT-01, DA-01 analog) |
| **CA-02** | **COMPLETE** transition to terminal state **требует** operator declaration — **never** automatic (OCM-02) |
| **CA-03** | **Partial closure** metadata (`FACTORY_TRACK_CLOSED_PARTIAL`) **требует** operator declaration — charter endpoint **не** inferred from progress alone |
| **CA-04** | **Suspension** (`FACTORY_TRACK_SUSPENDED`) и **lift** — operator declarations — **не** client silence or repo inactivity |
| **CA-05** | **Registry withdrawal** — operator declaration per Playbook 02 — **orthogonal** to Factory-track closure (CL-03) |
| **CA-06** | **Registry archived** category after closure — **отдельное** operator decision; `COMPLETE` **не** auto-archives catalog (RW-05 analog) |
| **CA-07** | One closure workflow instance = **один** logical Factory Project identity |

### Decisions that can **never** be automatic (v1)

- Active state transition to `COMPLETE`  
- `RG-PROJECT_COMPLETE` and terminal handoff (`HO-13`) outcome declaration  
- `FACTORY_TRACK_CLOSED_PARTIAL` metadata declaration  
- `FACTORY_TRACK_SUSPENDED` or suspension lift  
- AP-09 lifecycle closure sign-off  
- Registry **archived** or **withdrawn** catalog category  
- Treating deploy, CI green, or git archive as Factory closure  

**Optional automation (FUTURE)** не меняет CA-01 — только implementation charters.

---

## Closure Classes

Классы — **категории операционных исходов Factory-track**, не Runtime states (кроме occupancy at `COMPLETE`), не шаблоны, не формы.

### Core closure classes (required analysis)

| Class | Operational meaning | Active state | Runtime terminal? | Factory-track metadata |
|-------|----------------------|--------------|-------------------|------------------------|
| **COMPLETE closure** | Full-chain charter endpoint reached; Factory architecture track **closed** | `COMPLETE` | **Yes** (FT-10) | Lifecycle LC-13 complete; no `FACTORY_TRACK_CLOSED_PARTIAL` |
| **Partial closure** | Charter-declared endpoint **before** full LC-13 path; prefix gate-complete | Last **applicable** in-scope state (e.g. `DESIGN_READY`) | **No** | `FACTORY_TRACK_CLOSED_PARTIAL` |
| **Withdrawal** (catalog) | Case **ceases default discoverability** in Factory portfolio | **Unchanged** — any active state or post-closure | **No** | **None** on Engine track — catalog category only |
| **Suspension** | Factory work **paused** by charter/operator; track **frozen** | **Frozen** at last declared | **No** | `FACTORY_TRACK_SUSPENDED` |
| **Suspension continuation (lift)** | Resume Factory work from frozen segment | Unfrozen — resumes progression eligibility | **No** | Suspension flag cleared |
| **Closure after reconciliation** | Terminal or partial closure **following** integrity gap remediation | Per closure class above | Per class | Valid only after reconciliation declaration (Playbook 04) |
| **Closure after rollback history** | Closure at endpoint after rollback cascade resolved and fresh gates satisfied | Per closure class above | Per class | Rollback history **visible**; downstream SUPERSEDED markers remain |

### Additional justified class

| Class | When justified | Notes |
|-------|----------------|-------|
| **Abandoned charter (non-terminal)** | Sponsor cancels Factory intent without partial/full closure declaration | Project **remains** at last active state; **not** suspension unless operator declares; continuity of **record** preserved (Lifecycle) — **not** a Runtime terminal state |

### Class distinction matrix

| Concept | Factory-track closed? | Active state moves? | Catalog default view | Deploy implied? |
|---------|----------------------|---------------------|----------------------|-----------------|
| **COMPLETE closure** | **Yes** (full) | → `COMPLETE` | Often → **archived** (operator) | **No** |
| **Partial closure** | **Yes** (charter prefix) | At endpoint state | Often → **archived** (operator) | **No** |
| **Withdrawal** | **No** | Unchanged | **Hidden** from discoverable set | **No** |
| **Suspension** | **No** | Frozen | Unchanged unless operator also withdraws | **No** |
| **Mid-chain active (not closed)** | **No** | Any non-terminal | **Discoverable** if enrolled | **No** |

### Class interaction rules

| Rule | ID | Statement |
|------|-----|-----------|
| Closure is composite | **CC-01** | COMPLETE closure **requires** declaration bundle: terminal state + closure gates + HO-13 path + AP-09 (DC-04) |
| Partial ≠ COMPLETE | **CC-02** | Partial closure **must not** occupy `COMPLETE` unless charter explicitly includes full LC-13 path (LPC-05, CL-02) |
| Withdrawal ≠ closure | **CC-03** | Catalog withdrawal **does not** declare Factory-track terminal (CL-03) |
| Suspension ≠ halt | **CC-04** | `FACTORY_TRACK_SUSPENDED` ≠ LS-* gate halt — different operator narratives (CL-05) |
| Reconciliation before terminal | **CC-05** | Integrity gap (ledger ≠ active, stale PASS as blocker) **blocks** closure until reconciliation |
| Rollback does not forbid closure | **CC-06** | Closure **allowed** after rollback if endpoint reachable with **fresh** ACTIVE gates — history preserved |
| Deploy ≠ closure | **CC-07** | Client deploy **never** triggers closure class selection (CL-04, OCM-01) |

**Запрещено в этом разделе:** closure templates, closure forms, closure registry entries, new Runtime state codes.

---

## Closure Prerequisites

Принципы **до** того, как closure act разрешён. **Не** file paths, **не** storage.

### Universal prerequisites (all closure classes)

| # | Prerequisite | Rationale |
|---|--------------|-----------|
| CP0 | **Factory-scoped** logical Factory Project exists | Playbook 01 recognition |
| CP1 | **Manifest-enrolled** (MRDY-*) | Orientability; closure without entry anchor = audit risk |
| CP2 | **Operator authority** per CA-01 | Authority violation → invalid closure |
| CP3 | **Closure class** identified — не смешивать COMPLETE, partial, suspension, withdrawal | CC-02, CC-03 |
| CP4 | **Assessed reality** — Playbook 03 или эквivalent: closure readiness, blockers enumerated | No closure on catalog/git assumption alone |
| CP5 | **Declared charter endpoint** explicit and current | MRDY-03, LPC-03 — implicit endpoint = invalid partial closure |
| CP6 | **No undeclared integrity gap** | Reconciliation precedes terminal closure (CC-05, RC-01) |
| CP7 | **Not** already terminal `COMPLETE` for outbound COMPLETE closure | CS-03 — terminal lock |

### Class-specific prerequisites (principles)

| Closure class | Must be true before closure allowed |
|---------------|-------------------------------------|
| **COMPLETE closure** | Active eligible for TR-13; history through `FRONTEND_READY`; `RG-FRONTEND_HANDOFF_APPROVED` + `RG-PROJECT_COMPLETE` satisfied ACTIVE; HO-12 + HO-13 cleared with Frontend ack; gate-complete full chain (GCO-01…GCO-06); AP-09; **not** suspended; scope mask includes full chain to LC-13 |
| **Partial closure** | Charter names **last applicable state** as factory deliverable boundary; active = that state (or operator declares final occupancy there); all **non-EXCLUDED** segments through endpoint **completed** in history; gate-complete for prefix through endpoint `RG-*` (GCO-02…GCO-05 for prefix); **not** `RG-PROJECT_COMPLETE` unless at `COMPLETE`; operator partial sign-off; **not** suspended unless lifting first |
| **Withdrawal** | Registry-enrolled or catalog intent documented; operator declares portfolio removal — **independent** of Engine gate completeness |
| **Suspension** | Operator charter or operational narrative for pause; active state known; forward progression declarations **deferred** until lift |
| **Suspension lift** | Prior suspension declared; operator assesses resume readiness; blocking gates at frozen segment understood |
| **Closure after reconciliation** | Reconciliation declaration **completed** (Playbook 04); TC-* coherent; then class-specific prerequisites re-evaluated |
| **Closure after rollback history** | Rollback cascade acknowledged; active at rollback target or forward path **re-established** to endpoint; exit gates for re-traversed segments **fresh** ACTIVE PASS |

### When closure is **prohibited**

| Condition | Prohibited closure |
|-----------|-------------------|
| Blocking gate open / STALE / INVALID for intended endpoint | COMPLETE or partial closure |
| Handoff blocked at closure boundary (HO-12, HO-13) | COMPLETE closure |
| Active `COMPLETE` with contradictory gate index | **Reconciliation** — not second closure |
| Charter endpoint ambiguous or silent for partial intent | Partial closure |
| `FACTORY_TRACK_SUSPENDED` without lift | COMPLETE, partial, or forward-implying closure |
| Integrity gap undeclared | Any terminal closure |
| Attempt `COMPLETE` from non-`FRONTEND_READY` without legal TR path | COMPLETE closure |
| Scope violation — endpoint state EXCLUDED in LR-07 mask | Partial closure at that state |
| Criteria not reviewed — evidence alone | Gate satisfaction for closure bundle |
| Catalog-only knowledge of «done» | Any Factory-track closure |

---

## Evidence Principles

Evidence поддерживает closure decision — **не** заменяет operator closure declaration. Только **классы**, не файлы и не storage.

### Evidence class catalogue (closure-oriented)

| Class | Supports closure classes | Operator use |
|-------|-------------------------|--------------|
| **CE1 — Charter & declared endpoint** | All Factory-track closure | Scope tier, exclusions, last applicable state for partial |
| **CE2 — Gate satisfaction chain** | COMPLETE, partial | ACTIVE PASS on required `RG-*` through endpoint; stale sweep clean |
| **CE3 — Handoff clearance chain** | COMPLETE (HO-12, HO-13); partial where HO applicable on path | CLEARED events; Frontend ack where required |
| **CE4 — Lifecycle composition alignment** | All Factory-track closure | Active LC-* coherent with endpoint; partial flag justified |
| **CE5 — Layer artefact refs** | Gate-backed closure | Authoritative bodies for criteria review — refs only |
| **CE6 — Validation / QA outcomes** | COMPLETE, partial at validation-heavy endpoints | E4 analog — PASS summaries |
| **CE7 — Reviewer attestation** | HITL gates on closure path | Input to operator — **not** automatic terminal |
| **CE8 — Session assessment (Playbook 03)** | All closure classes | Closure readiness outcome; blocker list |
| **CE9 — AP-* sign-off** | COMPLETE (AP-09); partial where charter requires | Lifecycle closure authorization |
| **CE10 — Reconciliation record** | Closure after reconciliation | Prior integrity gap closed |
| **CE11 — Rollback / cascade narrative** | Closure after rollback history | Cascade complete; fresh gates on re-forward path |
| **CE12 — Catalog enrollment context** | Withdrawal, archived | Prior enrollment declaration; distinction fields |
| **CE13 — External bound ref** | Charter-bound client acceptance | **Never** sole evidence for COMPLETE without operator binding |

### Evidence principles (normative)

| ID | Principle |
|----|-----------|
| **CEV-01** | Evidence **classes** combine — **ни один** не auto-closes Factory track |
| **CEV-02** | Deploy success, DNS live, CI green — **не** CE2/CE3 unless charter explicitly binds — post-Factory by default |
| **CEV-03** | Global layer ACCEPTED (T5) — **не** per-project closure evidence |
| **CEV-04** | Playbook 03 **closure readiness** outcome **recommends** closure class — **≠** closure declaration |
| **CEV-05** | Partial closure **requires** CE1 explicit endpoint — progress alone insufficient |
| **CEV-06** | Gate-complete (GCO-*) **necessary** for Factory-track closure — **not sufficient** without operator act |

---

## Closure Outcomes

После **valid** closure act (via Playbook 04 declaration bundle) — **логические** последствия по planes. **Без** implementation.

### Effects by plane

| Plane | COMPLETE closure | Partial closure | Suspension | Withdrawal (catalog) |
|-------|------------------|-----------------|------------|---------------------|
| **Lifecycle** | LC-13; full chain narrative **closed** | Prefix **closed** at charter endpoint; downstream segments N_A or not applicable | **Frozen** narrative at last segment | **Unchanged** |
| **State** | Active = `COMPLETE`; terminal lock (CS-03) | Active = charter endpoint state; **not** terminal | Active **frozen** — displayed unchanged | **Unchanged** |
| **Gate** | All closure gates ACTIVE; no outbound eligibility | Prefix gates ACTIVE through endpoint; **no** `RG-PROJECT_COMPLETE` unless at `COMPLETE` | Gate set **frozen** until lift | **Unchanged** |
| **Handoff** | HO-13 cleared; closure boundary recorded | HO cleared through applicable prefix | **Frozen** | **Unchanged** |
| **Tracking** | SV-04 terminal display; full trackability at closure if criteria met | Partial closure flag visible; trackability for **reached** prefix | Suspension flag; eligibility **frozen** | **Unchanged** Engine; catalog snapshot may update |
| **Surface** | Eight questions show terminal truth; no forward eligibility | Shows partial closed + declared endpoint | Shows suspended + frozen segment | **Unchanged** per-project Engine truth |
| **Manifest** | Orientation may reflect **terminal Factory closure** category (MS-04) — **not** deploy | May reflect partial / endpoint summary (ML-03) | May require suspension visibility category | Entry anchor **may remain**; orientation unchanged unless amended |
| **Registry** | Operator **may** declare **archived** — separate act (CA-06) | Operator **may** declare **archived** | **No** auto-withdrawal (RW-05) | **Withdrawn** from default discoverable set |
| **Audit** | Append-only closure declaration chain (AT-01) | Same | Suspension/lift records | Catalog enrollment/withdrawal records |

### Outcome principles (normative)

| ID | Principle |
|----|-----------|
| **CO-01** | Closure **не** deletes project identity, history, or superseded rollback records |
| **CO-02** | COMPLETE closure **не** authorizes deploy or client go-live (OCM-01, DO-05) |
| **CO-03** | Partial closure **не** implies handoffs or generation occurred if segments EXCLUDED |
| **CO-04** | Terminal `COMPLETE` **implies** no outbound state progression — further work is post-Factory |
| **CO-05** | Registry orientation snapshot **updates** only on **catalog** declarations — not implicit from Engine closure |
| **CO-06** | Manifest **не** becomes gate index at closure (MT-01) — topology refs stable |
| **CO-07** | Suspension lift **restores** progression eligibility from frozen segment — **не** auto-complete |

---

## Invalid Closure Principles

**Invalid closure** — closure act или implied closure, который **не должен** становиться authoritative, или требует **немедленного supersession** через reconciliation.

### Invalidity categories

| Category | Description | Typical response |
|----------|-------------|------------------|
| **Unresolved blockers** | COMPLETE/partial declared while blocking gate, HO, or LS halt active | Supersede; restore pre-closure active truth |
| **Unsupported completion** | `COMPLETE` without `FRONTEND_READY` history or missing `RG-PROJECT_COMPLETE` | Invalidate; reconciliation |
| **Authority violation** | Non-operator or external system as closure declarer | Reject; no authoritative closure index |
| **Contradictory reality** | Active `COMPLETE` while gate index gate-incomplete | Reconciliation before trust |
| **Implicit partial closure** | `FACTORY_TRACK_CLOSED_PARTIAL` without charter endpoint | Invalidate partial metadata |
| **Wrong class** | Withdrawal treated as Factory-track terminal | Correct catalog category; Engine unchanged |
| **Suspended closure** | Terminal closure while `FACTORY_TRACK_SUSPENDED` active | Invalidate; lift or reconcile first |
| **Integrity gap closure** | Terminal declared while ledger ≠ active | Reconciliation (RC-01) |
| **Scope violation** | Partial closure at EXCLUDED state | Invalidate; amend charter or rollback |
| **Criteria bypass** | Closure gates PASS without operator criteria review | Invalidate; re-declare after review |
| **Phantom closure** | Assumed closed from deploy/git/archive only | **Undeclared** — remediate with explicit closure workflow |
| **Rollback residue** | Closure with STALE downstream gates treated active | Invalidate; fresh gates or reconciliation |

### Invalidity principles (normative)

| ID | Principle |
|----|-----------|
| **IC-01** | Invalid closure **не** silently erased — supersession or reconciliation record (AT-01, IV-01 analog) |
| **IC-02** | **Cannot** rollback from `COMPLETE` (LRC-06) — erroneous COMPLETE requires reconciliation narrative, not RB-* |
| **IC-03** | Partial closure at wrong state **invalid** even if «work feels done» |
| **IC-04** | Registry archived **without** valid Factory-track closure **misleading** — operator should align categories |
| **IC-05** | Operator **must not** declare COMPLETE to «unblock» portfolio reporting while gates open |

---

## Partial Closure Principles

Без переопределения Lifecycle model (LPC-*) — операционная дисциплина **partial closure** class.

### How partial closure differs from COMPLETE

| Dimension | COMPLETE closure | Partial closure |
|-----------|------------------|-----------------|
| **Charter endpoint** | Full LC-00…LC-13 chain (default) | Explicit **earlier** last applicable state |
| **Active state** | `COMPLETE` | e.g. `DESIGN_READY`, `VALIDATED` — **not** `COMPLETE` unless charter includes LC-13 |
| **Runtime terminal** | **Yes** | **No** |
| **Metadata** | LC-13 complete | `FACTORY_TRACK_CLOSED_PARTIAL` |
| **Terminal gate** | `RG-PROJECT_COMPLETE` ACTIVE | **Not** required unless at `COMPLETE` |
| **Handoffs** | Through HO-13 | Through applicable prefix only |
| **Registry** | Typically **archived** (operator) | Typically **archived** (operator) |
| **Downstream work** | Post-Factory relative to full chain | EXCLUDED segments **never** occupied — may never occur |

### How partial closure differs from withdrawal

| Dimension | Partial closure | Withdrawal |
|-----------|-----------------|------------|
| **Factory-track** | **Closed** per charter prefix | **Open or closed independently** — Engine track unchanged by withdrawal |
| **Purpose** | Declare factory deliverable boundary reached | Remove from default portfolio discoverability |
| **Active state** | At charter endpoint | **Unchanged** |
| **Metadata** | `FACTORY_TRACK_CLOSED_PARTIAL` | Catalog **withdrawn** category only |
| **Reversible** | Charter amendment + rollback path — **heavy** | Re-enrollment declaration (Playbook 02) |

### How partial closure differs from suspension

| Dimension | Partial closure | Suspension |
|-----------|-----------------|------------|
| **Intent** | Deliverable boundary **reached** | Work **paused** mid-track |
| **Endpoint** | Charter endpoint **achieved** | Endpoint **not** reached |
| **Active state** | At declared last state | **Frozen** at pause point |
| **Forward work** | **None** in Factory scope for excluded downstream | **May resume** after lift |
| **Metadata** | `FACTORY_TRACK_CLOSED_PARTIAL` | `FACTORY_TRACK_SUSPENDED` |

### Partial closure principles (normative)

| ID | Principle |
|----|-----------|
| **PC-01** | Partial closure **must** be charter-explicit (LPC-03, CL-01, OCM-03) |
| **PC-02** | Gate-complete **relative to declared endpoint** — not full chain (GCO-01, LPC-04) |
| **PC-03** | EXCLUDED segments visible as N_A — not hidden (LPC-02) |
| **PC-04** | Partial closure **≠** «stuck mid-chain» — blocked project is **not** partial closed |
| **PC-05** | Operator **must** declare partial metadata — reaching endpoint state occupancy alone insufficient without closure act |

---

## Registry And Discoverability Impact

Без удаления project reality — только **catalog lifecycle** и **discoverability** doctrine.

### Impact by closure class

| Closure class | Registry discoverability (default doctrine) | Manifest enrollment | Project discoverability |
|---------------|---------------------------------------------|---------------------|-------------------------|
| **COMPLETE closure** | Operator **may** declare **archived** — historical portfolio | **Remains** — entry anchor persists | **Archived** extended view; not active portfolio |
| **Partial closure** | Same as COMPLETE — **archived** typical | **Remains** | Same |
| **Withdrawal** | **Ceases** default discoverability | **May remain** manifest-enrolled | Hidden from default view — **exists** in Engine |
| **Suspension** | **Unchanged** unless operator also withdraws | **Unchanged** | **Unchanged** unless catalog act |
| **Mid-chain active** | **Discoverable** if enrolled | Enrolled | Active portfolio |

### Registry principles (normative)

| ID | Principle |
|----|-----------|
| **RI-01** | Closure **не** deletes Engine history, Tracking audit, or Manifest anchor |
| **RI-02** | **Archived** = catalog distinction — **not** «project never existed» |
| **RI-03** | **Withdrawn** ≠ Factory-track closure — project **may** be COMPLETE and withdrawn, or active and withdrawn |
| **RI-04** | **Archived** without Engine closure metadata **misleading** — operator aligns narrative (IC-04) |
| **RI-05** | Re-enrollment after withdrawal **≠** reopening COMPLETE track — new catalog declaration only (Playbook 02) |
| **RI-06** | Site Type Registry paths **do not** affect Factory Project discoverability (RD-05) |
| **RI-07** | Registry orientation snapshot **non-authoritative** for Engine closure state — reconcile RS-03 if edited separately |

### Manifest impact summary

| Event | Manifest effect |
|-------|-----------------|
| COMPLETE closure | Orientation **may** reflect terminal Factory closure — **not** deploy go-live (MS-04) |
| Partial closure | Endpoint summary **may** update; partial flag category (ML-03, OQ-M02) |
| Suspension | Visibility category **may** be required (ML-03) |
| Withdrawal | **No** Engine mutation — manifest anchor **persists** unless separate amendment |

**Manifest enrollment (Playbook 01) is never revoked by closure** — only orientation categories may evolve.

---

## Workflow Completion

### When Project Closure Workflow is considered complete (document)

**Playbook 05** как документ **complete** когда организация приняла его как норматив для операционного закрытия Factory Project — deliverable = этот файл.

### Per-closure instance completion

Один **closure workflow instance** завершён когда:

| # | Criterion |
|---|-----------|
| 1 | Closure class **named** (CC-*) |
| 2 | Prerequisites CP0–CP7 and class-specific **attested** |
| 3 | Evidence classes **cited** (CE*) where required |
| 4 | Operator with CA-01 authority **performed** closure via Playbook 04 declaration bundle |
| 5 | Valid closure **produced** outcomes (CO-*) or invalidity **handled** (IC-*) |
| 6 | Catalog **archived** or **withdrawal** declared **if** portfolio visibility change intended — separate acts |
| 7 | Playbook 03 follow-up **scheduled** if post-closure trackability review needed |

### Operational flow (conceptual)

```text
  Playbook 03 session (closure intent)
        │
        ▼
  Select closure class (CC-*)
        │
        ▼
  Verify prerequisites (CP*) + evidence (CE*)
        │
        ├── integrity gap? ──▶ Playbook 04 reconciliation FIRST
        ├── suspended? ──▶ lift OR choose suspension class only
        └── ready ──▶ Playbook 04 closure declaration bundle
                │
                ▼
  Optional: Playbook 02 archived / withdrawal (catalog plane)
                │
                ▼
  Surface reflects terminal / partial / suspended truth
```

### Relationship to Playbooks 01–04

```text
  Playbook 01  Manifest enrollment     ──▶  Factory-scoped + manifest-enrolled (CP0–CP1)
  Playbook 02  Registry enrollment     ──▶  optional discoverability; withdrawal/archived parallel
  Playbook 03  Surface session         ──▶  closure readiness assessment (CP4, CE8)
  Playbook 04  Project declaration     ──▶  executes closure declaration bundle (DC-04, CL-*)
  Playbook 05  Project closure         ──▶  THIS: class selection + prerequisites + outcomes discipline
```

| Playbook | Feeds Playbook 05 | Playbook 05 feeds |
|----------|-------------------|-------------------|
| **01** | Valid enrolled project | Cannot close pre-Factory case |
| **02** | Catalog context for withdrawal/archived | Post-closure catalog decisions |
| **03** | Closure readiness, blockers | Terminal Surface truth on next session |
| **04** | Declaration execution | Specialized closure **decision** path before declare |

### Future artifacts (reference only)

| Future artifact | Relationship |
|-----------------|--------------|
| Registry withdrawal micro-playbook | May **narrow** withdrawal steps — **не** replace CC-03 |
| RT-G04 / RT-G10 implementation | May **persist** closure outcomes — **не** change closure semantics |
| Operator Display (RT-G12) | May **show** closure status — **не** authorize closure |

---

## Explicit Non-Claims

This playbook and Project Closure Workflow v1:

- **are not** a Website Factory **runtime**, workflow engine, orchestrator, or shipped product;
- **are not** **automation**, **agent workflow**, n8n, CI-driven closure, or orchestrator;
- **are not** **storage**, **database**, **file format**, **YAML**, **JSON**, **schemas**, or folder standards;
- **are not** **implementation** of manifest (RT-G10), registry (RT-G05), tracking storage (RT-G04), or display (RT-G12);
- **are not** a **closure template**, **closure form**, **closure registry**, or **closure database**;
- **are not** **UI**, **dashboard**, **CLI**, or operator display product;
- **do not** redefine Engine Stages 1–6, Runtime states/`RG-*`/`HO-*`, Gate/Lifecycle/State/Tracking models, or Playbooks 01–04;
- **do not** define physical closure artefacts, serialization, or central closure catalog;
- **do not** claim automated enforcement, Gate Results System, or Lifecycle System exists in-repo;
- **do not** authorize deploy or client go-live by Factory closure.

Human-operated closure remains the v1 operating reality per [FACTORY-OPERATIONAL-MODEL-v1.md](FACTORY-OPERATIONAL-MODEL-v1.md) and [FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md](FACTORY-PROJECT-DECLARATION-WORKFLOW-v1.md).

---

## Open Questions

Bounded for **future operational artifacts** — not resolved in Playbook 05.

| ID | Question | Disposition |
|----|----------|-------------|
| **OQ-CL01** | Minimum evidence bundle for partial closure (CE1+CE2 always?) | **OPEN** — operator convention; extends OQ-PD07 |
| **OQ-CL02** | Manifest category for partial closure vs Tracking flag only | **OPEN** — OQ-M02, OQ-S6-09 |
| **OQ-CL03** | Default vs extended portfolio view for archived after closure | **OPEN** — OQ-R03 |
| **OQ-CL04** | Single session: Playbook 03 closure assessment + Playbook 04 declare + catalog archived | **OPEN** — OQ-TSW05 analog |
| **OQ-CL05** | Abandoned charter: standard metadata vs last-state-only | **OPEN** — no Runtime terminal state |
| **OQ-CL06** | PHASE_SLICE: closure per shell vs per generation slice | **OPEN** — OQ-S6-03 |
| **OQ-CL07** | Erroneous COMPLETE recovery narrative without rollback | **OPEN** — IC-02 reconciliation depth |
| **OQ-CL08** | Triumph / pilot: external deploy vs Factory closure alignment | **SAFE UNKNOWN** per case |

---

## Recommended Next Step

1. **Operator acknowledgment:** Treat **Project Closure Workflow v1** as Operational Playbook 05 **complete** — use when Factory-track reaches charter endpoint or catalog visibility must change at end of life.
2. **Operational Design continuation (separate tasks):**
   - Registry index card template (OQ-R02) — archived/withdrawn fields
   - Registry withdrawal session micro-playbook (optional)
   - Tracking surface operator workflow updates — closure readiness outcome tie-in
3. **Per active Factory Project:** Never treat deploy or git archive as closure; declare closure class explicitly; align catalog **archived** with Engine terminal metadata.
4. **Do not start:** closure storage, closure registry product, automation agents, runtime — unless explicitly authorized.
5. **Optional P3:** Reference Playbook 05 from [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md) Operational Design row — operator action.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether operators already run ad-hoc closure discipline | **UNKNOWN** — no canonical closure store |
| Physical serialization of `FACTORY_TRACK_CLOSED_PARTIAL` | **NOT DEFINED** — RT-G10 FUTURE |
| Calendar for RT-G04/10 persistence of closure records | **not scheduled** |
| Pilot workspaces catalog treatment at closure | **UNKNOWN** per case charter (OQ-OM07) |

---

*Factory Project Closure Workflow v1 — Operational Playbook 05. Canonical location: `workspaces/website-factory-reference-v1/`. Git: no commit, no push.*

---

# REPORT — Factory Project Closure Workflow v1

**Stage:** Operational Design — Operational Playbook 05 (Project Closure Workflow)  
**Deliverable:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md`  
**Changed files:** `workspaces/website-factory-reference-v1/FACTORY-PROJECT-CLOSURE-WORKFLOW-v1.md` (created)  
**Summary:** Определён операционный workflow закрытия Factory Project: authority (factory operator, human-only), классы closure (COMPLETE, partial, withdrawal, suspension, post-reconciliation, post-rollback), prerequisites, evidence classes, outcomes по Lifecycle/Tracking/Surface/Manifest/Registry, invalid closure и partial closure principles, discoverability impact без удаления project reality, связь с Playbooks 01–04 — без runtime, automation, storage, templates, closure registry, implementation.  
**Git:** no commit, no push (per task charter).
