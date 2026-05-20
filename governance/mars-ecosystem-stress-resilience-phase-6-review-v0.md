# MARS — Ecosystem stress & resilience testing (Phase 6)

**Status:** **documented** — first ecosystem-wide **stress-test** and **resilience-validation** pass on the stabilized MARS ecosystem (post–Pass 4 compression, post–Pass 5 consistency). **Not** governance expansion, **not** architecture redesign, **not** runtime implementation, **not** testing infrastructure.  
**Date:** 2026-05-19.  
**Builds on:** [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md), [mars-consistency-survivability-pass-5-review-v0.md](mars-consistency-survivability-pass-5-review-v0.md), [editorial-compression-pass-4-operator-fatigue-review-v0.md](editorial-compression-pass-4-operator-fatigue-review-v0.md).

**Method:** Human-operated **scenario simulation** — onboarding personas, routing walks, topology growth projection, operator-overload patterns, drift-resistance sampling. **No** automated crawler, **no** new ontology, **no** test harness.

**Repo scale (stress context):** ~258 Factory `.md`, ~473 ORCA `.md`, ~83 governance `.md`, ~42 Forge checklists — counts are **navigation pressure**, not quality scores.

---

## Executive verdict

| Dimension | Verdict | Confidence |
|-----------|---------|------------|
| **Onboarding (disciplined)** | **Survivable** — Paths A–E + 4-file stop work when followed | High |
| **Onboarding (undisciplined)** | **High overload risk** — layout table, governance README, Factory Pack index, ORCA doc-map | High |
| **Routing Tier 0–2** | **Resilient** — precedence rules hold; circular loops **mitigated**, not eliminated | High |
| **Routing Tier 3 / Extended** | **Near cognitive limits** — Factory Extended, Forge checklist catalog, ORCA volume | High |
| **Topology (+3–5 systems)** | **Indexes collapse first** — topology/reality/governance README; Factory OPERATIONAL-INDEX Extended | Medium |
| **Operator overload** | **Fatigue loops remain** under parallel lanes + REPORT accumulation | High |
| **Drift resistance** | **Strong at Tier 0–2**; **weak** in chat memory, legacy import, triad sprawl | Medium–High |

**Overall:** Ecosystem is **navigable and coherent under realistic pressure** if Tier discipline holds. **Collapse risk** concentrates in **undisciplined breadth-first reading** and **Factory meta-governance growth**, not in broken Tier 0–2 chains.

---

## Task A — Onboarding stress test

Simulated paths use documented surfaces only ([onboarding-survivability.md](onboarding-survivability.md), [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md)).

**Rating key:** Nav = navigation clarity · OL = overload risk · WT = wrong-turn probability · SD = “where do I start?” · Read = excessive reading · DE = dead-end risk  
Scale: **Low / Med / High**

| Persona | Canonical path | Nav | OL | WT | SD | Read | DE | Stress notes |
|---------|----------------|-----|----|----|----|------|----|--------------|
| **New operator** | Path A (4 files + stop) | Med | Med | Med | **High** if skips stop 3 | Med | Low | Root README **layout table** (15+ folders) triggers architecture shock before Tier model; governance README **~90 rows** tempts full scan |
| **Factory-only** | Path B | **High** | Med | Low | Low | Med | Med | Core Run **strong**; WT rises if README Pack index (~200 lines) opened before INDEX; Extended rows feel mandatory |
| **Forge/frontend** | Path C | Med | **High** | Med | Med | **High** | Med | Gulp-first correct but **3 packs** (Gulp, Forge, Factory contracts); Forge README checklist catalog = Tier 3 opened early |
| **ORCA (PPC)** | Path E → ORCA INDEX | **High** | Med | Med | Low | Low | Low | **Best-in-class** live-first; FAST PATH + STOP cues; WT if `operator-entrypoints-v1.md` chosen for “live” session |
| **Governance operator** | Path A + governance/README **one row** | Med | **High** | Med | Med | **High** | Med | Phase S0–S7 + reality audit = encyclopedia; **no** single governance “Core Run” (by design) |
| **Runtime-curious** | Path D | Med | Med | **High** | Med | Med | **High** | `mars-runtime/` folder name implies product; Path D requires discipline; R1 scripts ≠ platform |

### Onboarding stress findings (compact)

1. **Strongest survivability:** ORCA OPERATIONAL-INDEX, Factory Core Run (post–Pass 4), Path A stop rule.  
2. **Highest confusion:** new operator opening **topology + reality + governance README** in one session (documented anti-pattern, still likely).  
3. **Wrong-turn hotspots:** web-gpt-sources first; Factory Pack index as session nav; ORCA `operator-entrypoints-v1.md` for live PPC; Triumph charter as production proof.  
4. **Reading budget:** Forge/frontend and governance personas exceed **one session segment** without explicit task scope.  
5. **Dead-ends:** web-gpt-sources deep tree without governance reconciliation; runtime folder without README boundaries.

**Onboarding verdict:** **Pass** under Path A–E discipline; **Fail** under “read everything that looks canonical.”

---

## Task B — Routing resilience test

### Surfaces stressed

| Surface | Stress focus | Resilience |
|---------|--------------|------------|
| **Tier 0–3** | Model in [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md) | **Holds** — Tier 0 = 2 files only; Tier 1 pick-one enforced in headers |
| **OPERATIONAL-INDEX** | Factory Core/Extended; ORCA FAST PATH | Factory **Core resilient**; Extended **wide**; ORCA **strong** |
| **Topology / reality** | [ecosystem-topology-index.md](ecosystem-topology-index.md) vs [mars-reality-index-v0.md](mars-reality-index-v0.md) | **Not contradictory** when pick-one; **overload** if both + governance README |
| **Pack entrypoints** | Factory, ORCA, WPilot, MetaBOT, Forge, Gulp | **Two** OPERATIONAL-INDEX packs only — WPilot/MetaBOT use alternate maps (acceptable, adds branch memory) |
| **Governance entry** | [governance/README.md](README.md) | **Resilient as router** if one-row rule; **fragile** if table read end-to-end |
| **ORCA live-first** | INDEX vs operator-entrypoints vs starter-core | INDEX **wins** (Pass 5); secondary docs still **list** multi-entry starts |
| **Factory Core Run** | 8 concern rows + Frontend block once | **Resilient**; Frontend dedupe (Pass 4) reduced loop |

### Routing defect catalog

| Defect type | Found? | Severity | Example |
|-------------|--------|----------|---------|
| **Circular routing** | Partial | Med | governance/README → index → governance/README; Factory INDEX ↔ README Pack index |
| **Route ambiguity** | Yes | Med | ORCA live vs task-shaped entrypoints; validation “runtime” vs “chain” vocabulary |
| **Duplicated authority** | Contained | Low–Med | README vs INDEX (resolved); Forge vs Gulp (foundation wins) |
| **Hidden alternate paths** | Yes | Med | ORCA operator-entrypoints; web-gpt-sources; chat-migration |
| **Operator branch overload** | Yes | **High** | Tier 1 × 4 routers; Factory Extended domain groups; ORCA 473 md files |

### Routing resilience verdict

**Tier 0–2: resilient.** Precedence chain (AGENTS → registries → pack INDEX → governance over web-gpt) survives stress.  
**Tier 3 + alternate entry docs: stress-sensitive.** Discipline is the mitigation — not more indexes.

---

## Task C — Topology stress test

**Scenario:** Add **3–5 large systems** (e.g. second factory program, analytics pack, client-delivery monorepo, CI governance lane, external CRM bridge) without new ontology engine.

### Predicted overload order (first → last)

| Rank | Area | Why it fails first |
|------|------|-------------------|
| 1 | **ecosystem-topology-index** + **mars-reality-index** | Entity rows and bucket matrix grow linearly; pick-one rule harder to maintain |
| 2 | **governance/README** | New phase = new row; already ~90 table rows |
| 3 | **Factory OPERATIONAL-INDEX Extended** | Grouped tables absorb new `*-governance.md` clusters |
| 4 | **agents/registry** + **project-registry** | Identity rows multiply; README lag risk |
| 5 | **Forge README checklist table** | New QA domain = new checklist file + README row |
| 6 | **ORCA doc-map gravity** | Already 473 md — new subsystem amplifies “one more doc” risk |

### Areas already near cognitive limits

| Area | Signal |
|------|--------|
| **Factory** | 258 md; Extended table spans semantics, strategic, meta-governance, production |
| **Forge** | 42 checklist files — catalog in README is Tier 3 volume |
| **ORCA** | Largest pack by file count; live-first INDEX mitigates but does not shrink corpus |
| **Governance S3–S7 + reality audit** | Mature vocabulary; growth is row/table expansion |
| **Topology layer** | Compact today (~235 lines) — **fragile under +5 entities** without editorial caps |

### Registry / index drift prediction

| Registry / index | Drift speed if unmanaged |
|------------------|--------------------------|
| **project-registry.md** | **Fast** — new `project_id` without lifecycle backfill |
| **agents/registry.md** | **Medium** — cards vs pack README status |
| **OPERATIONAL-INDEX Core** | **Slow** (human-gated rows) — **good** |
| **OPERATIONAL-INDEX Extended** | **Fast** — default sink for new governance docs |
| **continuity/master-index** | **Slow** — optional; low risk |

### Topology stress verdict

**Current topology is stable for ~2 new major entities** if each gets **one OPERATIONAL-INDEX row + path letter**, not a new Tier 1 “start here.” **Beyond ~5**, expect **index collapse** unless Pass 4-style compression repeats.

---

## Task D — Operator overload test

### Scenarios simulated

| Scenario | Overload hotspots | Survivability failure mode |
|----------|-------------------|----------------------------|
| **Long multi-chat session** | REPORT accumulation; repeated Tier 0 explanations in prompts | Semantic-memory overload — **chat ≠ SoT** |
| **Parallel governance + ORCA** | Lane A/B mix without [parallel-cursor-chat-work-mode-v0.md](parallel-cursor-chat-work-mode-v0.md) | Wrong lane edits; PPC doc opened in Factory session |
| **Factory + Forge + runtime** | Three SoT surfaces (Factory contracts, Forge overlay, mars-runtime) | Foundation/Forge/runtime boundary confusion |
| **Repeated context switching** | Tier 1 re-pick each switch; INDEX row re-derivation | Navigation fatigue loop |
| **Large REPORT accumulation** | No single REPORT index — search by date/chat | Prior decisions **invisible** unless lifecycle/continuity used |

### Navigation fatigue loops (confirmed)

1. Factory README Pack index → OPERATIONAL-INDEX full scan → Extended domain row → taxonomy sibling files.  
2. Forge README checklist enumeration → AGENT.md → back to checklist for “one more domain.”  
3. Tier 1 topology → reality → onboarding → governance row (4 routers).  
4. ORCA FAST PATH → Starter Core menu exhaustion → operator-entrypoints project path.  
5. Governance phase doc → linked triad → Factory Extended mirror doc.

### Lightweight mitigations (proposed — not implemented in Phase 6)

| Mitigation | Effort | Target |
|------------|--------|--------|
| **Session header template** (chat pin): lane + Tier 1 router + one INDEX row | Trivial | Context switching |
| **REPORT index row** in continuity or lifecycle pointer | Low | REPORT accumulation |
| **ORCA operator-entrypoints banner** “live session → OPERATIONAL-INDEX” | Low | ORCA wrong-turn |
| **Forge README checklist grouping** (Pass 4 deferred) | Med | Forge overload |
| **Quarterly routing spot-check** | Low | [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md) |
| **Cap Tier 1 routers** — no sixth “start here” without retirement | Policy | Topology drift |

**Operator overload verdict:** **Survivable** with lane discipline and STOP rules; **fails** when operators treat catalogs as syllabi or skip IdeaBox/lifecycle for decisions.

---

## Task E — Drift resilience review

### Drift resistance today

| Drift type | Resistance | Mechanism |
|------------|------------|-----------|
| **Registry drift** | **Strong** | [registry-source-of-truth.md](registry-source-of-truth.md), AGENTS precedence |
| **Terminology drift** | **Strong** | [canonical-terminology-registry.md](canonical-terminology-registry.md), enforcement boundaries |
| **Topology drift** | **Medium** | ecosystem-topology-index + entropy rules; **no** auto-sync |
| **Lifecycle drift** | **Medium** | lifecycle log vs implementation; chat-migration supersession labels |
| **Operational-state drift** | **Medium** | current-operational-state-v1; pack README may lag registry |

### Silent drift zones (still dangerous)

1. **Chat memory** — decisions not in REPORT / lifecycle / continuity.  
2. **Factory governance triads** — new `*-governance.md` + taxonomy without INDEX discipline → Extended sprawl.  
3. **web-gpt-sources** — legacy vocabulary contradicts governance if read first.  
4. **Stabilization audits cited as override** — audits are input, not Tier 0 (documented; still misused).  
5. **ORCA secondary entry docs** — partial duplication with INDEX.  
6. **Validation vocabulary** — Factory `validation-runtime-*` vs governance `validation-chain-semantics` (parallel, not broken).  
7. **Triumph / reference cases** — charter read as deployment proof.

### Self-stabilizing areas (Pass 5 + Phase 6 confirm)

- Tier 0–3 entry model cross-linked from root, packs, Factory INDEX.  
- Factory Core Run / Extended split.  
- Forge transition + foundation map (Gulp wins).  
- ORCA live-first INDEX pattern.  
- AGENTS three-way split + SAFE UNKNOWN.

### Future additions — highest danger

| Addition | Risk |
|----------|------|
| New Tier 1 “start here” index | Onboarding collapse |
| New pack without OPERATIONAL-INDEX row | Hidden entry sprawl |
| Automated “helpful” governance generator | Triad explosion |
| Second Forge-like overlay | SoT fork |
| CI link checker without human gating | False confidence |

**Drift verdict:** **Resistant at spine**; **permeable at volume layers** (Factory Extended, ORCA corpus, chat).

---

## Highest future collapse-risk zones (ranked)

1. **Undisciplined breadth-first onboarding** (ignoring 4-file stop + pick-one Tier 1).  
2. **Factory meta-governance triad sprawl** (Extended table as default sink).  
3. **ORCA document gravity** (473 md; “one more checklist” despite STOP cues).  
4. **governance/README encyclopedia growth** (new phase rows without compression pass).  
5. **web-gpt-sources first-read** (legacy contradicts live governance).  
6. **Multi-lane parallel chat without lane headers** (Lane A/B mix).  
7. **New Tier 1 router without retiring another** (topology/reality proliferation).  
8. **Registry row without lifecycle backfill** (claim vs evidence gap).

---

## SAFE UNKNOWN (Phase 6)

| Topic | UNKNOWN | Would verify |
|-------|---------|--------------|
| Full-repo link graph under stress | Not exhaustively crawled | Human spot-check or future helper (gated) |
| Real operator time-on-task per persona | Not measured | Timed onboarding walk with human |
| ORCA md count growth rate | Snapshot only | Periodic count / editorial pass |
| External systems (GitGuard, live n8n) | Out of repo | Operator evidence |
| Effectiveness of proposed mitigations | Not tested | Adopt one mitigation; re-run Phase 6 slice |
| WPilot/MetaBOT routing under +5 systems stress | Lighter simulation | Per-pack stress when touched |

---

## Related

- [mars-consistency-survivability-pass-5-review-v0.md](mars-consistency-survivability-pass-5-review-v0.md)  
- [editorial-compression-pass-4-operator-fatigue-review-v0.md](editorial-compression-pass-4-operator-fatigue-review-v0.md)  
- [documentation-entropy-rules.md](documentation-entropy-rules.md)  
- [operator-load-management.md](operator-load-management.md)

---

*Phase 6 — stress and resilience validation only; no commits implied.*
