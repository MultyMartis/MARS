# Website Factory — compression review v0

**Status:** **documented** — review artefact only. **Does not** rewrite Factory packs.  
**Date:** 2026-05-19.  
**Scope:** `projects/mars-website-factory/` density, duplication, navigation load.  
**Method:** file inventory + [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) / README structure review; aligned with [mars-v2-structural-coherence-audit-v0.md](mars-v2-structural-coherence-audit-v0.md).

**Counts (approximate, in-repo):**

| Pattern | Count |
|---------|------:|
| Pack markdown files (`*.md`) | ~239 |
| `*governance*.md` | ~59 |
| `*taxonomy*.md` | ~34 |
| Forge `*checklist*.md` mirrors | ~38 |

---

## Executive summary

Website Factory is **operationally valuable** but **topologically heavy**. Compression should target **navigation and triplication**, not removal of core workflow/artifact contracts. The pack already contains **governance-minimalism** and **compression** methodology — Phase 1 recommends **using** those docs rather than adding new governance layers.

---

## 1. Governance duplication

| Pattern | Symptom | Compression opportunity |
|---------|---------|-------------------------|
| **Governance + taxonomy + model triads** | Many concerns use three files (`*-governance.md`, `*-model.md`, `*-taxonomy.md`) | Treat **governance** as canonical; fold taxonomy tables into governance as **appendix sections** when editing; mark models **reference-only** in OPERATIONAL-INDEX |
| **Meta-governance stack** | `governance-evolution-governance.md`, `meta-governance-integrity.md`, `governance-architecture-model.md`, `governance-compression-governance.md` overlap philosophically | Single **“meta-governance entry”** row in OPERATIONAL-INDEX already clusters several — **do not** add a fifth meta layer; merge pointers in README Pack index over time |
| **Forge mirror checklists** | Factory governance doc ↔ `agents/mars-forge/*-checklist.md` | Keep **one operational surface** per concern: checklist for operators, governance for semantics — add **“checklist is operational shorthand”** banner on new governance docs (pattern exists on several Forge checklists) |
| **Validation runtime vocabulary** | `validation-runtime-overview-v0.md`, execution semantics, artifact bus — sound executable | Reinforce **documentation-only** banners (already in safe-unknown-boundary); **avoid** new “runtime” filenames |

**Not duplication (keep):** `website-factory-workflow-v0.md`, `frontend-handoff-contract-v0.md`, `artifact-architecture-overview-v0.md`, `agent-map.md`, `safe-unknown-boundary.md`.

---

## 2. Checklist proliferation

| Area | Observation | Compression opportunity |
|------|-------------|---------------------------|
| **Forge overlay** | ~38 checklists — high operator load | Introduce **tiered QA modes** using existing [operational-modes-model.md](../projects/mars-website-factory/operational-modes-model.md) — **light / standard / battle** — without deleting checklists |
| **OPERATIONAL-INDEX width** | Single table row per triad + Forge link — index itself became dense | Split index into **“core run”** (10 rows) vs **“extended governance”** (collapsed appendix) in a future edit — **do not** duplicate README Pack index |
| **Page blueprint QA** | `page-blueprint-qa-checklist-v0.md` vs QA matrix | Cross-link once; avoid third checklist variant |

---

## 3. Topology density (excessive layering)

| Layer family | Risk | Compression opportunity |
|--------------|------|-------------------------|
| **Semantic / artifact / execution** | Many `*-overview-v0.md` + stage models — correct but heavy | Preserve overviews; deprecate **redundant** mid-level docs only after human merge (per [documentation-entropy-rules.md](documentation-entropy-rules.md)) |
| **Reference project layer** | 6+ reference-project docs + templates | Keep model + lifecycle + QA matrix; consider **one** “reference layer quickstart” page linking the six |
| **Drift taxonomies** | 34 taxonomies — valuable for diagnosis, costly for onboarding | Index taxonomies under **one** “drift taxonomy index” section in README (link list only) |
| **Phase numbering** | `implementation-phase-1.md` “Phase 5–10” vs `roadmap.md` phases | Already documented — reinforce in onboarding reads; **no** renumbering in Phase 1 |

---

## 4. Navigation overload

| Surface | Issue | Mitigation (lightweight) |
|---------|-------|---------------------------|
| **README Pack index** | Full inventory ~200 lines | **OPERATIONAL-INDEX** is the intended stabilization path — prefer it over expanding README |
| **OPERATIONAL-INDEX** | Grew wide (governance rows duplicated Frontend block) | Future pass: dedupe repeated Frontend rows; keep **one** Frontend discipline row |
| **Cross-links to governance/** | Factory docs link many central governance files | Acceptable — ensure links are **stable paths**, not copies of governance prose |

---

## 5. Recommended compression actions (human-gated, not Phase 1 scope)

Priority **stabilize, don’t expand**:

1. **Collapse navigation** — OPERATIONAL-INDEX “core run” vs “extended” sections (editorial).  
2. **Taxonomy index** — README appendix linking all `*-taxonomy.md` (no new ontology).  
3. **Forge checklist tiers** — document which checklists are **battle-test only** (Triumph charter).  
4. **Merge triads** — only when a human editorial pass proves two files are near-duplicates (evidence required).  
5. **Prune** — use [governance-minimalism.md](../projects/mars-website-factory/governance-minimalism.md) criteria; log in lifecycle log if pruned.

**Explicitly out of scope:** autonomous compression tooling, semantic merge bots, registry auto-sync.

---

## 6. What not to compress

- Workflow + HITL + SAFE UNKNOWN boundaries  
- Frontend handoff + production rules v0  
- Agent map + registry cross-refs  
- Reference case **honesty** disclaimers (Triumph)  
- ORCA-style **anti-bloat** discipline already present in Factory minimalism docs — **use**, don’t duplicate centrally  

---

## SAFE UNKNOWN

- Which taxonomies are **actively used** in live operator runs vs authored speculatively — **requires human usage review**  
- Optimal checklist tier set per site type — **project charter**  

---

*Compression review — signals only; Factory rewrite deferred.*
