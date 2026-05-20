# MARS — Lightweight maintenance model (Phase 3)

**Status:** **documented** — human-operated discipline only.  
**Date:** 2026-05-19.  
**Not:** a governance bureaucracy, ticketing system, automation platform, or registry engine.

**Purpose:** Prevent future entropy explosions during **complexity-stage maintenance** — small, repeatable human decisions.

---

## 1. Principles

1. **Stabilize before expand** ([stabilization-vs-expansion.md](stabilization-vs-expansion.md)).  
2. **Indexes over new philosophy** ([documentation-entropy-rules.md](documentation-entropy-rules.md)).  
3. **Link duplicates; don’t rewrite honesty** ([AGENTS.md](../AGENTS.md)).  
4. **REPORT closeouts** for non-trivial passes ([context-continuity-rules.md](context-continuity-rules.md)).  
5. **SAFE UNKNOWN** when ownership or evidence is missing.

---

## 2. Maintenance triggers (when to act)

| Trigger | What to run | Output |
|---------|-------------|--------|
| **Stabilization needed** | Drift visible: registry ≠ README; broken links; contradictory status; onboarding fails at “where to look?” | Reconcile rows, fix links, deprecation banners — **no new subsystem** |
| **Compression needed** | OPERATIONAL-INDEX or pack README wider without new operational failure mode; duplicate triads; checklist fatigue reports | Index tiers, dedupe rows, taxonomy link appendix, tiered QA — per [survivability-documentation-fatigue-review-v0.md](survivability-documentation-fatigue-review-v0.md) |
| **Lifecycle sync needed** | Stage/master-build-map claims disagree with lifecycle log; milestone recorded but map not updated | Update `master-build-map.md` and/or `logs/lifecycle-log.md` in **same human pass** |
| **Registry sync needed** | New agent/project/tool id used in prose but missing from registry; card exists without registry row | Add **minimal** row per [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md) — human only |
| **Topology review needed** | New pack, external system, or lane; repeated “where does X live?” questions | Update [ecosystem-topology-index.md](ecosystem-topology-index.md) + [mars-reality-index-v0.md](mars-reality-index-v0.md) — **one row each**, not a new map |
| **Reality / survivability pass** | Quarterly or post-major Factory/Forge expansion; operator overload signals | Short review artefact (like Phase 3) or section in REPORT — **not** standing committee |

---

## 3. When **NOT** to create new docs

Apply [documentation-entropy-rules.md](documentation-entropy-rules.md) — especially:

- One-line fix → edit authoritative file.  
- Navigation problem → index row, not new philosophy.  
- Restating AGENTS/README → link only.  
- New concern already has governance + taxonomy + model → **extend** governance; don’t add a fourth sibling without evidence.  
- Visibility for a single task → lifecycle line or REPORT, not new `*-principles.md`.

**Red flag:** New doc title contains “framework,” “engine,” “platform,” or “ontology” without in-repo implementation proof.

---

## 4. Cadence (suggested, not mandatory)

| Cadence | Activity | Max scope |
|---------|----------|-----------|
| **Per task** | REPORT if requested; one registry touch if ids changed | Minutes |
| **Per merge-worthy slice** | Link check for edited files; registry row if new entity | Small |
| **Monthly (if active)** | Operator load self-check ([operator-load-management.md](operator-load-management.md)) | 15 min |
| **After large pack expansion** | Compression + entrypoint review ([survivability-architecture-weight-review-v0.md](survivability-architecture-weight-review-v0.md) pattern) | 1–2 pages, human-written |
| **When governance/README grows** | Ask: can this be a **row** instead of a new file? | Before writing |

No calendar automation — **human remembers** or task charter includes maintenance.

---

## 5. Lane-specific maintenance minimums

| Lane | Minimum upkeep |
|------|----------------|
| **MARS core** | AGENTS + governance README row accuracy |
| **Website Factory** | OPERATIONAL-INDEX reflects new concerns; README honesty boundary intact |
| **Forge** | New checklist ↔ Factory governance link pair; README does not duplicate Gulp |
| **Runtime R1** | Qualifiers in README; no new forbidden claims ([enforcement/forbidden-runtime-claims.md](enforcement/forbidden-runtime-claims.md)) |
| **External (MetaBOT, ORCA, WPilot)** | [external-system-boundaries.md](external-system-boundaries.md) row current |

---

## 6. Escalation (human only)

| Situation | Action |
|-----------|--------|
| Conflicting SoT | State SAFE UNKNOWN; human picks precedence per [registry-source-of-truth.md](registry-source-of-truth.md) |
| Mythology pressure | [reality-vs-mythology-warnings.md](reality-vs-mythology-warnings.md) + terminology registry |
| Expansion vs stabilization dispute | [stabilization-vs-expansion.md](stabilization-vs-expansion.md) — default **stabilize** |
| Prune / delete request | Explicit user instruction + lifecycle note — repo default is **no silent delete** |

---

## 7. Success signals (lightweight)

- New operator reaches **one correct authoritative file** in &lt; 10 minutes (Path A–E).  
- OPERATIONAL-INDEX row count grows **slower** than governance triad count.  
- Fewer duplicate honesty paragraphs in new commits.  
- Registries match prose **ids** for active work.  
- No new “start here” without retiring or downgrading another.

---

## 8. Failure signals (entropy returning)

- Multiple parallel “architecture initiatives” without owners.  
- New taxonomies without observed failure mode.  
- Indexes not updated but README essays added.  
- Chat-only handoffs without REPORT or lifecycle line.  
- Experimental R1 paths described as product runtime in new docs.

---

## 9. Phase 3 artefact set (this pass)

| File | Role |
|------|------|
| [survivability-architecture-weight-review-v0.md](survivability-architecture-weight-review-v0.md) | Weight / risk map |
| [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md) | Orientation paths |
| [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md) | Tier 0–3 routing |
| [survivability-documentation-fatigue-review-v0.md](survivability-documentation-fatigue-review-v0.md) | Fatigue + compression |
| [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md) | This model |

**Next passes:** execute P0 editorial items (Factory INDEX tiers, dedupe) only when chartered — not automatic.

---

*Human-operated maintenance — no product claims.*
