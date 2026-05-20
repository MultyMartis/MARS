# MARS — Canonical entrypoint model (Phase 3 proposal)

**Status:** **documented** — proposal only; **does not** supersede [AGENTS.md](../AGENTS.md), registries, or pack READMEs.  
**Date:** 2026-05-19.  
**Goal:** Fewer cognitive branches — **clarity and consistency**, not massive index rewrites.

---

## 1. Problem statement

The repo has **multiple legitimate entry surfaces** that grew for good reasons (honesty, pack autonomy, stabilization audits). Without a **thin routing model**, operators treat every index as mandatory and every map as “start here.”

**Symptoms observed:**

- `AGENTS.md` + `ecosystem-topology-index` + `mars-reality-index` + pack README + OPERATIONAL-INDEX + local workflow maps  
- Factory [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) competes with [README.md](../projects/mars-website-factory/README.md) Pack index  
- Forge README enumerates all checklists; foundation README is a separate entry  
- [governance/README.md](README.md) functions as encyclopedia and entrypoint  
- Root [README.md](../README.md) layout table implies depth-first exploration  

---

## 2. Canonical entrypoint model (compact)

### Tier 0 — Global honesty (always first for new humans/agents)

| Entry | Scope |
|-------|--------|
| [README.md](../README.md) | What the repo is / is not; current phase |
| [AGENTS.md](../AGENTS.md) | Documented vs planned vs legacy; SAFE UNKNOWN; closeout |

**Rule:** No other file is Tier 0.

### Tier 1 — Global routing (pick **one** per session question)

| Question | Canonical entry |
|----------|-----------------|
| Where do entities live? | [ecosystem-topology-index.md](ecosystem-topology-index.md) |
| What is operational vs conceptual today? | [mars-reality-index-v0.md](mars-reality-index-v0.md) |
| Post–Cycle 8 ecosystem posture? | [mars-operational-evolution-state-after-cycles-1-8-v0.md](mars-operational-evolution-state-after-cycles-1-8-v0.md) |
| How do I onboard? | [onboarding-survivability.md](onboarding-survivability.md) → [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md) |
| Governance topic lookup | [governance/README.md](README.md) — **one row**, not full scan (**maintenance tasks only**) |
| Registry / identity | [agents/registry.md](../agents/registry.md) or [registry/project-registry.md](../registry/project-registry.md) — task-scoped |

**Rule:** Tier 1 entries are **routers**, not deep reads.

### Tier 2 — Pack / lane entry (task-assigned)

| Lane | Canonical entry | Live session navigation |
|------|-----------------|-------------------------|
| Website Factory | [projects/mars-website-factory/README.md](../projects/mars-website-factory/README.md) | [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) — **one concern row** |
| Forge overlay | [agents/mars-forge/README.md](../agents/mars-forge/README.md) | [AGENT.md](../agents/mars-forge/AGENT.md) + [workflow.md](../agents/mars-forge/workflow.md) |
| Gulp foundation | [agents/frontend-gulp-agent/README.md](../agents/frontend-gulp-agent/README.md) | [workflow.md](../agents/frontend-gulp-agent/workflow.md) |
| ORCA | [projects/orca/README.md](../projects/orca/README.md) | [projects/orca/OPERATIONAL-INDEX.md](../projects/orca/OPERATIONAL-INDEX.md) |
| WPilot | [projects/wpilot/README.md](../projects/wpilot/README.md) | [plugin-mvp/reconciliation-map-v0.md](../projects/wpilot/plugin-mvp/reconciliation-map-v0.md) when touching plugin planning |
| Runtime / R1 | [mars-runtime/README.md](../mars-runtime/README.md) | Cited script + contract only |
| Legacy design import | [web-gpt-sources/README.md](../web-gpt-sources/README.md) if present | **Historical** — reconcile via governance |

**Rule:** Pack README = **identity + boundary**; OPERATIONAL-INDEX (or ORCA equivalent) = **session SoT**.

### Tier 3 — Deep semantics (on demand only)

Governance triads, drift taxonomies, stage models, Forge specialist checklists, master-build-map stage tables, dependency-map edges.

**Rule:** Open Tier 3 only when Tier 2 row or a contract citation requires it.

---

## 3. Duplicated “main entry” docs (inventory)

| Doc | Claims / behaves as | Resolution in model |
|-----|---------------------|---------------------|
| Root README | Repo main entry | Tier 0 — keep |
| AGENTS.md | Agent/human rules | Tier 0 — keep |
| governance/README | Governance main catalog | Tier 1 router — **not** full read |
| ecosystem-topology-index | “Start here after AGENTS” | Tier 1 — ecosystem question only |
| mars-reality-index-v0 | “Start here for buckets” | Tier 1 — mythology/reality question only |
| Factory README + OPERATIONAL-INDEX | Both “canonical” | Tier 2 split: README vs INDEX |
| Factory system-overview / layer-map / workflow-map | Local architecture starts | Tier 3 — link from INDEX row only |
| Forge README | Pack main + checklist catalog | Tier 2 — shorten mental model to AGENT.md |
| web-gpt-sources chat-migration | Bridge to governance | Migration-only — not greenfield |
| ORCA operator-entrypoints-v1 | Practical starts | Tier 2 alternate to INDEX — prefer INDEX for live session |

---

## 4. Conflicting “start here” paths (resolution rules)

1. **AGENTS.md** wins on honesty and status claims.  
2. **Registries** win on identity rows — not README prose alone.  
3. **Pack OPERATIONAL-INDEX** wins for **live Factory/ORCA session** navigation — not Pack index full table.  
4. **governance/** wins over **web-gpt-sources/** on conflict — state SAFE UNKNOWN until reconciled.  
5. **Foundation (Gulp)** wins over **Forge** when Forge is silent.  
6. **Stabilization reviews** (topology, compression, Phase 3) are **input** — never override Tier 0–2 without human promotion.

---

## 5. Outdated or overloaded operational indexes

| Index | Issue | Lightweight fix (proposed, not done in Phase 3) |
|-------|-------|--------------------------------------------------|
| Factory OPERATIONAL-INDEX | Very wide; duplicate Frontend row block | Editorial: **Core run** section (~10 rows) + collapsed **Extended governance** |
| Factory README Pack index | Full inventory ~200 lines | Keep for search; banner: “session nav → OPERATIONAL-INDEX” |
| governance/README | Grows with every phase | Phase 3 links only — no table split |
| Root README layout | Many folders | Optional one-line: “explore via ecosystem-topology-index” |

---

## 6. Overlapping topology / navigation surfaces

```text
Tier 0: README + AGENTS
    │
    ├─ Tier 1 (pick ONE): topology-index │ reality-index │ onboarding │ governance-README-row
    │
    └─ Tier 2 (lane): pack-README → pack-OPERATIONAL-INDEX → workflow/runbook
            │
            └─ Tier 3: governance/taxonomy/checklists/contracts
```

**Anti-pattern:** Opening Tier 1 topology + reality + governance README + Factory INDEX in one session without a task.

---

## 7. Targeted consistency actions (minimal, human-gated)

Allowed **small** edits (not Phase 3 scope unless separately requested):

- One-line **Tier** banner in pack README headers (Factory, Forge, ORCA).  
- Factory OPERATIONAL-INDEX: dedupe Frontend duplicate block.  
- Point [operational-survivability.md](operational-survivability.md) to this model.  

**Applied (Editorial Compression Pass 4, 2026-05-19):** Tier banners; Factory OPERATIONAL-INDEX Core/Extended + Frontend dedupe; [editorial-compression-pass-4-operator-fatigue-review-v0.md](editorial-compression-pass-4-operator-fatigue-review-v0.md).

**Out of scope:** Renaming folders, merging packs, registry engine, new ontology index.

---

## Related

- [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md)  
- [website-factory-navigation-compression-strategy-v0.md](website-factory-navigation-compression-strategy-v0.md)
