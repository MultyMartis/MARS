# Lifecycle Log Deep Review v2

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2 Discovery  
**Mode:** Investigation + classification only (**no append**, **no backfill**, **no archive**)  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb` / `mars-v2-stable-baseline-2026-06`; evidence `c2876cf`)  
**Prior evidence:** [lifecycle-log-review-v1.md](lifecycle-log-review-v1.md) (Wave 1)  
**Primary SoT:** `logs/lifecycle-log.md`

---

## Executive determination

| Outcome band | Recommendation |
|--------------|----------------|
| **KEEP** | Yes — remain normative governance **event** SoT |
| **REDEFINE** | Yes — clarify boundaries vs `logs/cleanup/`, `logs/releases/`, project REPORTs, and optional `logs/decision-log.md` |
| **ARCHIVE CANDIDATE** | **No** — active mechanism with maintenance debt, not obsolete design |

Wave 2 deepens Wave 1: same classification, richer overlap analysis and operator decision prep.

---

## 1. Original intent

| Source | Statement |
|--------|-----------|
| `logs/lifecycle-log.md` header | **Single source of truth** for **documented lifecycle events**; human- and tool-maintained **append-only** log |
| Event schema | `event_id`, `timestamp`, `entity_id`, `event_type`, `description` — factual, no speculation |
| `governance/registry-architecture.md` §2 | Lifecycle / event registries = **what was recorded**, not implementation proof |
| `governance/registry-source-of-truth.md` (via registry-architecture) | Registry rows ≠ runtime; lifecycle complements registry with **events** |
| `governance/execution-phase-model.md` | Lifecycle records **events** and decisions; does **not** auto-advance phases |
| `governance/master-build-map.md` | Material build-map changes → lifecycle (or future decision log); Stages 9–15 milestones in evt 0004–0010 |
| `interfaces/self-describe-modes.md` | FULL mode **may** summarize recent lifecycle events when file exists |
| `observability/event-model-v0.md` §4 | Run-oriented **events** are **not** a substitute for lifecycle log |

**Design role (normative):** Governance audit trail for registry changes, stage/documentation milestones, and material policy moves — **separate** from execution run history, runtime state store, cleanup evidence, and release publication records.

---

## 2. Evolution

| Phase | Evidence |
|-------|----------|
| **v0 init** | `evt-2026-0001` (2026-04-27) — project-registry + lifecycle-log SoT established |
| **Stage gates** | `evt-2026-0002`–`0003` — Stage 7.5 / 8.5 documentation closure |
| **Stages 9–15 doc milestones** | `evt-2026-0004`–`0010` (2026-04-28) — explicitly documentation-only |
| **Program registration** | `evt-2026-0011` seo-content-agent; Factory normalization `0012`–`0014` |
| **Phase S0 truth repair** | `evt-2026-0015` (2026-05-14) |
| **Structural stabilization** | `evt-2026-0016` (2026-05-19) — reality index, sync review, clarity reviews |
| **Stall** | No events after 2026-05-19 despite registry/orca/wpilot/metabot activity through 2026-06-02 |
| **Sync review artefact** | `governance/lifecycle-synchronization-review-v0.md` — backlog **0017–0021** recommended, not appended |
| **Cleanup program** | `logs/cleanup/` (2026-06-03) — explicitly **not** lifecycle SoT per `logs/cleanup/README.md` |
| **Stable baseline publication** | `logs/releases/mars-v2-stable-baseline-2026-06.md` — checkpoint evidence, **not** lifecycle events |

**Evolution pattern:** Concept stable; **usage frequency** declined relative to `registry/project-registry.md` and program OPERATIONAL-INDEX updates.

---

## 3. Current implementation

| Aspect | State (verified 2026-06-03) |
|--------|------------------------------|
| **File** | `logs/lifecycle-log.md` — v0 schema |
| **Event count** | **16** rows (`evt-2026-0001` … `evt-2026-0016`) |
| **Last event** | `evt-2026-0016` — 2026-05-19 — Structural Stabilization Phase 2 |
| **Automation** | **None** — human-gated append only |
| **Decision log** | `logs/decision-log.md` — **not present**; master-build-map allows lifecycle until introduced |
| **Cleanup trail** | `logs/cleanup/**` — census/wave evidence; distinct purpose |
| **Release trail** | `logs/releases/**` — baseline publication; distinct purpose |
| **Survivability logs** | `logs/survivability/`, `logs/rollback-history/` — drill evidence; distinct |

---

## 4. Current usage (observed)

| Usage type | Observed |
|------------|----------|
| **Historical governance milestones** | Stages 7.5–15, Factory identity, Phase S0/S2 stabilization |
| **Project registration events** | Partial — seo-content-agent (0011); **missing** metabot, triumph, orca, wpilot, homegateway per sync review |
| **Registry maintenance pairing** | **Weak** — registry updated 2026-05-10 … 2026-06-02 without matching events |
| **Cleanup / census** | Census D-007 cites gap; cleanup program does **not** write lifecycle rows by default |
| **Runtime / agent execution** | Correctly **not** used |
| **Canvas classification** | `docs/visualization/obsidian-canvas/_generate_pack.py` labels Lifecycle Log as **archive-cand** node — **navigation drift** vs governance (KEEP) |

---

## 5. Overlap analysis

### 5.1 vs `logs/releases/`

| Dimension | Lifecycle log | Release evidence |
|-----------|---------------|------------------|
| **Purpose** | Append-only **governance events** | **Publication checkpoint** documentation (commit, scope, exclusions) |
| **Example** | `evt-2026-0016` stabilization pass | `logs/releases/mars-v2-stable-baseline-2026-06.md` |
| **Overlap risk** | Operator may duplicate “baseline frozen” narrative | **Low** if roles taught: lifecycle = *event*, release = *checkpoint record* |
| **Gap** | No lifecycle evt for 2026-06-03 baseline publication | Optional future `registry.updated` or `governance.baseline_published` — **operator decision** |

### 5.2 vs `logs/cleanup/`

| Dimension | Lifecycle log | Cleanup program |
|-----------|---------------|-----------------|
| **Purpose** | Governance **events** (registry, stages, policy) | Ecosystem **inventory / classification / proposed actions** |
| **Created** | Pre-cleanup (2026-04+) | 2026-06-03 census |
| **Overlap risk** | **Medium** — both are “logs under `logs/`” | Mitigated by `logs/cleanup/README.md` § discipline |
| **Unique value (lifecycle)** | Normative **event_id** schema referenced across governance spine | Cleanup is **investigation evidence**, not event SoT |

### 5.3 vs project / program REPORTs

| Dimension | Lifecycle log | REPORT / task closeout |
|-----------|---------------|------------------------|
| **Purpose** | Durable **cross-project** event index | **Scoped** task outcome (changed files, UNKNOWN) |
| **Overlap** | Lifecycle may **pointer-reference** REPORTs; should not paste full REPORT bodies ([artifact-lifecycle-rules.md](../../governance/artifact-lifecycle-rules.md)) |
| **Gap** | Many REPORTs never produce lifecycle rows | By design unless material registry/governance change |

### 5.4 vs `registry/project-registry.md`

| Dimension | Lifecycle log | Project registry |
|-----------|---------------|------------------|
| **Purpose** | **Events** (what happened when) | **Current row state** (status, phase, links) |
| **Drift** | **High** — registry ahead of log (0017–0021 backlog) | Registry is authoritative for **current** identity |
| **Unique value (lifecycle)** | Temporal audit trail; stage-completion **events** with documentation-only qualifiers |

### 5.5 vs `archive/` and Cold Brain

| Dimension | Lifecycle log | Archive (repo + storage) |
|-----------|---------------|--------------------------|
| **Purpose** | Record **decisions and transitions** | Store **retired bulk** / historical trees |
| **Overlap** | None operational — archive moves should **optionally** append lifecycle evt | Archive does not replace event log |
| **Gap** | Archival actions from cleanup waves not yet reflected in lifecycle | Future Wave 3+ **if** operator wants audit trail |

### 5.6 vs Knowledge Center

| Dimension | Lifecycle log | Knowledge Center |
|-----------|---------------|------------------|
| **Location** | In-git `logs/lifecycle-log.md` | Out-of-git `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` |
| **Role** | Governance **event SoT** | Operator **navigation** / Visual Brain mirror |
| **Overlap** | KC may **link** to lifecycle; must not become alternate event store |
| **Unique value (lifecycle)** | Git-tracked, citeable in governance and Web-GPT packs |

---

## 6. What unique value remains?

1. **Normative append-only governance event stream** — referenced in dependency map, risk register, memory-write-policy, release-gates, self-heal inputs.
2. **Documentation milestone honesty** — evt 0004–0010 explicitly mark documentation-only stage completion (anti-mythology).
3. **Registry change audit** — when maintained, pairs with `registry/project-registry.md` for *when* identity changed.
4. **Introspection binding** — `interfaces/self-describe-modes.md` allows FULL mode lifecycle summary from **this file only**.
5. **Distinct from cleanup and release trails** — prevents silent conflation if operator training holds.

**Value at risk if neglected:** Registry and OPERATIONAL-INDEX become de facto history; lifecycle loses trust as audit trail; canvas “archive-cand” label reinforces wrong mental model.

---

## 7. Recommended classification (Wave 2 — no execution)

| Action | Detail |
|--------|--------|
| **KEEP** | `logs/lifecycle-log.md` as governance event SoT |
| **REDEFINE** | Operator doc: three-log model — lifecycle (events) · cleanup (investigation) · releases (publication) |
| **REDEFINE** | Fix Visual Brain canvas node: lifecycle = **operational governance**, not archive candidate |
| **INVESTIGATE → operator** | Human-gated append **evt-2026-0017**–**0021** per `lifecycle-synchronization-review-v0.md` |
| **INVESTIGATE → operator** | Optional evt for baseline publication 2026-06-03 |
| **Do not** | Automate sync from registry; archive file; merge into cleanup program |

---

## 8. Proposed operator decisions (deferred)

| ID | Question | Options |
|----|----------|---------|
| L-01 | Backfill 0017–0021? | Yes (with confirmed timestamps) / No (accept drift) / Partial |
| L-02 | Introduce `logs/decision-log.md`? | Yes / Defer — lifecycle only |
| L-03 | Require lifecycle row on registry edit? | Policy tighten / status quo (recommended in sync review §5) |
| L-04 | Lifecycle evt on cleanup execution? | Yes / No — cleanup `fixes/` only |

---

## 9. SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Exact operator session dates for 0017–0021 | Not verified from git blame in this pass |
| Whether events were appended only in unpushed branches | Working tree may differ from `45518bb` snapshot |
| Full count of governance docs mandating lifecycle append | Sampled, not exhaustive grep |
| KC operator copies of lifecycle summary | Out-of-git — **SAFE UNKNOWN** |

---

*Lifecycle Log Deep Review v2 — Wave 2 Discovery evidence only. No filesystem changes.*
