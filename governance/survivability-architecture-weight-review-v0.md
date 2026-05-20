# MARS — Architecture weight review (Survivability Phase 3)

**Status:** **documented** — human-operated review artefact only.  
**Date:** 2026-05-19.  
**Scope:** First lightweight long-term survivability pass — **analysis**, not rewrite.  
**Method:** File counts, index structure review, cross-read of Phase 1–2 stabilization outputs ([ecosystem-topology-index.md](ecosystem-topology-index.md), [website-factory-compression-review-v0.md](website-factory-compression-review-v0.md), [mars-v2-structural-coherence-audit-v0.md](mars-v2-structural-coherence-audit-v0.md)).

**Counts (in-repo, approximate):**

| Area | `*.md` files |
|------|-------------:|
| `projects/mars-website-factory/` | 239 |
| `agents/mars-forge/` | 42 |
| `governance/` (root) | 71 |

---

## Executive summary

MARS has entered **complexity-stage maintenance**: the ecosystem is **operationally valuable** but **navigation-heavy**. Weight is concentrated in Website Factory governance triads, Forge checklist mirrors, and governance meta-layers (S1–S7 + reality audit). Mitigations should be **small** — index tiers, dedupe rows, banners, tiered QA — not mega-refactors.

---

## 1. Website Factory

| Signal | Why it became heavy | Operational risks | Lightweight mitigation |
|--------|---------------------|-------------------|------------------------|
| **~239 pack files** | Iterative governance expansion per concern (design, cadence, meta-governance, survivability) | “Any file might matter”; wrong doc opened for a simple run | Treat [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) as **stabilization** map; split mentally into **core run** (~10 concerns) vs **extended governance** (rest on demand) |
| **Governance + model + taxonomy triads** (~59 `*governance*`, ~34 `*taxonomy*`) | Repeatable pattern for semantic completeness | Triplication fatigue; taxonomy read before action | **Governance** = canonical semantics; taxonomies = **diagnosis appendix**; index-only link list in README (no new layer) |
| **OPERATIONAL-INDEX width** | Each new concern added a full table row + Forge links | Index itself became a long read; Frontend block **duplicated** (rows 19 vs 53) | Future editorial pass: **one** Frontend discipline row; dedupe repeated link blocks — **no** new index file |
| **Four topology/workflow entry points** | `system-overview`, `layer-map`, `workflow-map`, `website-factory-workflow-v0` each partially map the system | Operators pick wrong “architecture start” | Document **single** workflow start: `website-factory-workflow-v0.md` + `first-operational-runbook-v0.md`; others = reference |
| **Meta-governance stack** | Evolution, compression, minimalism, architecture integrity layered over time | Prestige-documentation; governance-for-governance | Use existing [governance-minimalism.md](../projects/mars-website-factory/governance-minimalism.md); **do not** add a fifth meta layer |
| **Validation vocabulary** | `validation-runtime-overview-v0`, execution semantics, artifact bus | Sounds executable; mythology pressure | Keep [safe-unknown-boundary.md](../projects/mars-website-factory/safe-unknown-boundary.md) in every runtime-adjacent read path |

---

## 2. MARS Forge

| Signal | Why it became heavy | Operational risks | Lightweight mitigation |
|--------|---------------------|-------------------|------------------------|
| **~38 mirrored checklists** | Factory governance → operational shorthand for Cursor QA | Checklist sprawl; battle-test treated as daily default | **Tiered modes** via [operational-modes-model.md](../projects/mars-website-factory/operational-modes-model.md): light / standard / battle (Triumph charter only) |
| **Long README “What Forge adds”** | Each checklist documented inline | README scroll fatigue | Entry: [AGENT.md](../agents/mars-forge/AGENT.md) + [qa-checklist.md](../agents/mars-forge/qa-checklist.md); README = orientation only |
| **Overlay vs foundation** | Thin overlay still looks like second SoT | Duplicate Gulp rules | Reinforce “Forge silent → foundation wins” ([mars-forge/README.md](../agents/mars-forge/README.md)); no third workflow file |

---

## 3. Governance meta-layers

| Signal | Why it became heavy | Operational risks | Lightweight mitigation |
|--------|---------------------|-------------------|------------------------|
| **71 governance files + S1–S7 + reality audit** | Phased honesty stack accumulated without retiring older explainers | New operators read governance README as mandatory encyclopedia | [onboarding-survivability.md](onboarding-survivability.md): **stop after four** global reads; governance README = **pick one topic** |
| **Parallel stabilization reviews** | Phase 1–2 audits (topology, compression, reality index, cross-system) | “Which map is SoT?” | **Lane pick:** ecosystem = [ecosystem-topology-index.md](ecosystem-topology-index.md); reality bucket = [mars-reality-index-v0.md](mars-reality-index-v0.md); deep audit = coherence audit — **not** all three per task |
| **Terminology + enforcement** | Anti-drift aids multiplied | Every delivery task feels governance-critical | Classify task: governance-critical vs pack-specific ([onboarding-survivability.md](onboarding-survivability.md) §5) |

---

## 4. Validation layers

| Signal | Why it became heavy | Operational risks | Lightweight mitigation |
|--------|---------------------|-------------------|------------------------|
| **validation-chain-semantics.md** + Factory validation models | Need to separate human vs CI vs governance read | “Validation mentioned” → assumed automation | Use vocabulary from [validation-chain-semantics.md](validation-chain-semantics.md); REPORT states **which** validation class |
| **QA matrices + page blueprint QA + Forge overlay** | Multiple QA surfaces for same page | Double or triple QA with no added signal | One **active** QA surface per phase: foundation QA → Forge overlay → governance read only when escalated |
| **Agent input contracts** | New explicit I/O discipline | Perceived runtime enforcement | Treat as **governance artifact**; pre-flight = human checklist |

---

## 5. Runtime research layers

| Signal | Why it became heavy | Operational risks | Lightweight mitigation |
|--------|---------------------|-------------------|------------------------|
| **Contracts + R1 JS in same folder** | Stage 8.5/13 contracts colocated with demos | `mars-runtime/` read as “live” | [mars-runtime/README.md](../mars-runtime/README.md) first; [runtime-registry-boundaries.md](runtime-registry-boundaries.md); [runtime-mythology-pressure-review-v0.md](runtime-mythology-pressure-review-v0.md) |
| **execution-* contract set** | Future vocabulary documented early | Orchestrator/queue implied | Qualify every mention: **CONCEPTUAL** / **EXPERIMENTAL (R1 only)** per [canonical-terminology-registry.md](canonical-terminology-registry.md) |
| **Root README layout table** | Lists many contract folders | Architecture shock for newcomers | Root README = **posture** only; depth = one lane doc |

---

## 6. Topology maps

| Signal | Why it became heavy | Operational risks | Lightweight mitigation |
|--------|---------------------|-------------------|------------------------|
| **ecosystem-topology-index + external-systems-map + dependency-map + master-build-map** | Each answers a different question; all look like “maps” | Map hopping without task | Task → **one** map: topology (where entities live), dependency (contract edges), build map (stage), external (MetaBOT/ORCA/WPilot) |
| **Factory local maps** | layer-map, workflow-map, agent-map, system-overview | Four local “starts” | OPERATIONAL-INDEX **By concern** row only |
| **ORCA healthy contrast** | ORCA enforces `OPERATIONAL-INDEX` as live-session SoT | Factory index grew wider than ORCA discipline | Borrow ORCA pattern: **live session = one index row**, not full pack |

---

## 7. Glossary density

| Signal | Why it became heavy | Operational risks | Lightweight mitigation |
|--------|---------------------|-------------------|------------------------|
| **canonical-terminology-registry.md** | Stabilization anti-mythology terms | Second glossary competing with web-gpt terminology map | AGENTS > web-gpt mars-v2 > terminology registry; **do not** spawn pack glossaries |
| **Per-concern taxonomies in Factory** | Drift diagnosis vocabulary | 34 taxonomies as onboarding reading | **Drift taxonomy index** (link list in README appendix) — navigation only |
| **system-signals-dictionary.md** | Cross-contract signal names | Signal name archaeology | Open only when editing contracts that reference signals |

---

## Highest cognitive-load zones (ranked)

1. **Website Factory OPERATIONAL-INDEX + governance triads**  
2. **Forge checklist set (full battle mode)**  
3. **governance/README.md** (full table scan)  
4. **Factory validation / execution semantics cluster**  
5. **Parallel topology maps (global + Factory local)**  

---

## Hardest onboarding zones

1. Choosing Factory vs Forge vs Gulp foundation vs workspace execution  
2. Distinguishing **documentation-only** validation from real CI/hosting  
3. Governance phase stack (S3–S7) vs task-sized need  
4. Legacy `web-gpt-sources/` vs current governance truth  
5. Triumph / reference case vs production delivery proof  

---

## Most duplicated explanations

| Topic | Surfaces |
|-------|----------|
| MARS is not live runtime | AGENTS, README, execution-model, safe-unknown-boundary, mars-runtime README, reality index |
| Registry ≠ deployed | AGENTS, terminology registry, registry-architecture, enforcement |
| Forge overlay posture | Forge README, transition doc, operational design v0, Factory OPERATIONAL-INDEX |
| Website Factory honesty | Factory README, OPERATIONAL-INDEX, governance-minimalism, compression review |

**Mitigation:** Duplicate **links**, not duplicate **prose** — one paragraph per repo level max.

---

## Highest navigation-cost clusters

- `projects/mars-website-factory/` (239 files, wide index)  
- `governance/` meta + stabilization review cluster  
- `agents/mars-forge/` checklist grid  
- `web-gpt-sources/` + `web-gpt-sources/mars-v2/` (legacy + v2)  
- Root contract folders (`control-plane/`, `workflows/`, `interfaces/`) for non-runtime tasks  

---

## Documentation surfaces likely to overload operators

- Full scan of [governance/README.md](README.md)  
- Full [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) in one sitting  
- [agents/mars-forge/README.md](../agents/mars-forge/README.md) checklist enumeration  
- [master-build-map.md](master-build-map.md) without a single stage target  
- Any `*-drift-taxonomy.md` before the governing `*-governance.md` for that concern  

---

## Explicit non-recommendations

- No ontology / semantic graph  
- No registry sync engine  
- No Factory or governance mega-rewrite  
- No autonomous compression tooling  

---

## Related Phase 3 outputs

- [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md)  
- [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md)  
- [survivability-documentation-fatigue-review-v0.md](survivability-documentation-fatigue-review-v0.md)  
- [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md)

---

*Review only — does not change pack authority or registry precedence.*
