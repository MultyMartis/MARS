# MARS — Consistency & Survivability Pass 5 review

**Status:** **documented** — first ecosystem-wide consistency and survivability-hygiene pass **after** Editorial Compression Pass 4. **Not** governance expansion, **not** navigation redesign, **not** runtime implementation.  
**Date:** 2026-05-19.  
**Builds on:** [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md), [editorial-compression-pass-4-operator-fatigue-review-v0.md](editorial-compression-pass-4-operator-fatigue-review-v0.md).

**Method:** Human-operated audit of major routing surfaces, relative-link spot-check on Tier 0–2 entry files, cross-read of onboarding/survivability artefacts, semantic label sampling. **No** automated link crawler product; **no** full-repo rewrite.

---

## Task A — Routing consistency audit

### Surfaces audited

| Surface | Tier role | Post–Pass 4 posture |
|---------|-----------|---------------------|
| [README.md](../README.md) | Tier 0 | **Aligned** — Tier 0–3 one-liner + topology pointer |
| [AGENTS.md](../AGENTS.md) | Tier 0 | **Aligned** on honesty; **gap:** no Tier 0–3 routing line (acceptable — README carries it) |
| [governance/README.md](README.md) | Tier 1 router | **Aligned** — Tier 1 banner, one-row discipline |
| [ecosystem-topology-index.md](ecosystem-topology-index.md) | Tier 1 (entities) | **Aligned** — pick-one with reality index |
| [mars-reality-index-v0.md](mars-reality-index-v0.md) | Tier 1 (buckets) | **Aligned** — scoped Tier 1 |
| [onboarding-survivability.md](onboarding-survivability.md) | Tier 1 (onboarding) | **Aligned** — 4-file minimum + canonical entry model |
| [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md) | Paths A–E | **Drift (fixed in Pass 5)** — Path A lagged onboarding-survivability |
| [projects/mars-website-factory/OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Tier 2 session SoT | **Strong** — Core Run / Extended / Frontend once |
| [projects/mars-website-factory/README.md](../projects/mars-website-factory/README.md) | Tier 2 identity | **Aligned** — archival Pack index banner |
| [agents/mars-forge/README.md](../agents/mars-forge/README.md) | Tier 2 Forge | **Aligned** — Tier 2 + foundation map pointer |
| [agents/frontend-gulp-agent/README.md](../agents/frontend-gulp-agent/README.md) | Tier 2 foundation | **Minor gap** — no Tier banner (identity clear; optional later) |
| [projects/orca/OPERATIONAL-INDEX.md](../projects/orca/OPERATIONAL-INDEX.md) | Tier 2 ORCA live | **Strong** — live-first, STOP cues |
| [projects/orca/README.md](../projects/orca/README.md) | Tier 2 ORCA | **Aligned** — OPERATIONAL-INDEX first |
| [mars-runtime/README.md](../mars-runtime/README.md) | Tier 2 runtime | **Not deep-audited** — Path D defers here |

### Tier 0–3 consistency

| Tier | Rule source | Finding |
|------|-------------|---------|
| **0** | README + AGENTS only | **Consistent** across root and pack banners |
| **1** | One router per session question | **Consistent** in topology + reality index headers; ecosystem index Phase 2 table used scoped “start” wording (tightened in Pass 5) |
| **2** | Pack README → OPERATIONAL-INDEX | **Factory/ORCA strong**; ORCA `current-state-v1.md` entry list **conflicted** (fixed in Pass 5) |
| **3** | On demand | **Risk remains** — Factory Extended still large; acceptable if Core Run discipline holds |

### Contradictory “start here”

| Claim | Resolution |
|-------|------------|
| Topology vs reality index | **Not contradictory** when read as pick-one Tier 1 routers ([survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md) §4) |
| Factory README vs OPERATIONAL-INDEX | **Resolved** — README = identity/archival index; INDEX = session |
| ORCA OPERATIONAL-INDEX vs operator-entrypoints | **Tier model:** INDEX = live session; entrypoints = task-shaped deep links — **document** precedence in ORCA current-state |
| web-gpt-sources | **Historical** — not a start surface |

### Broken navigation chains

Relative-link spot-check on Tier 0–2 routing files: **no broken relative targets** in the audited set (2026-05-19).

### Circular onboarding

| Loop risk | Severity | Mitigation |
|-----------|----------|------------|
| governance/README → full table → another index → governance/README | Medium | Tier 1 one-row rule + onboarding stop after 4 files |
| Factory INDEX → README Pack index → INDEX | Medium | Banners + Core Run only |
| Topology + reality + governance README in one session | High | Documented anti-pattern in canonical entry model |

**Routing verdict:** **Coherent** at Tier 0–2 after Pass 4; **residual drift** in ORCA secondary entry doc and onboarding strategy Path A (addressed minimally in Pass 5).

---

## Task B — Stale reference detection

| Class | Example | Posture |
|-------|---------|---------|
| Forge “not created” body text | [mars-forge-operational-design-v0.md](mars-forge-operational-design-v0.md) | **Mitigated** — stabilization header + transition doc; body may retain historical phrasing |
| Foundation map §5 “pack not created” | [frontend-legacy-and-foundation-map-v0.md](frontend-legacy-and-foundation-map-v0.md) | **Fixed** (2026-05-19 stabilization) — live overlay documented |
| chat-migration operational state | [lifecycle-synchronization-review-v0.md](lifecycle-synchronization-review-v0.md) | **Labeled superseded** by `current-operational-state-v1.md` — optional header link on next touch |
| ORCA operator entry order | [projects/orca/current-state-v1.md](../projects/orca/current-state-v1.md) | **Stale vs live-first** — fixed Pass 5 |
| Onboarding Path A file list | onboarding-survivability vs onboarding-strategy | **Stale** — fixed Pass 5 |
| Pre-compression “read Pack index first” | Factory README | **Retired** — archival banner present |
| Root README *Last updated* 2026-05-15 | [README.md](../README.md) | **Cosmetic staleness** — content still accurate; date not blocking |

**No giant rewrite recommended.** Highest impact was **routing precedence** strings, not bulk terminology replacement.

---

## Task C — Survivability flow review

### Can a human navigate without overload?

**Yes, if discipline is followed:** Tier 0 → one Tier 1 → pack Core Run / ORCA FAST PATH → stop.

| Flow | Viable? | Friction |
|------|---------|----------|
| MARS core day one | **Yes** | governance/README temptation |
| Factory delivery | **Yes** | Extended table width if Core Run ignored |
| Forge overlay | **Yes** | Long checklist catalog in Forge README (Tier 3) |
| Runtime / R1 | **Yes** | Folder name implies product |
| ORCA live PPC | **Yes** | Secondary docs still list multi-entry starts |
| Governance orientation | **Partial** | README table growth — use one-row router |

### Overload loops

1. Factory README Pack index + OPERATIONAL-INDEX full scan.  
2. Forge README checklist enumeration before AGENT.md.  
3. Tier 1 topology + reality + governance README in one session.  
4. ORCA starter-core + live-pilot + INDEX (partially deduped in ORCA reality audits).

### Dead-ends / branch points

| Surface | Issue |
|---------|-------|
| Factory Pack index | **Archival** — not dead-end if banner read |
| web-gpt-sources deep tree | **Historical dead-end** without governance reconciliation |
| GitGuard in reality index | **UNKNOWN bucket** — intentional honesty |
| `projects/seo-content-agent/` | **Redirect** to metabot pack — OK |

### Unclear operational paths

- **ORCA:** OPERATIONAL-INDEX vs operator-entrypoints — clarify live vs task-shaped (Pass 5 touch to current-state).  
- **MetaBOT:** canonical pack vs legacy folder — **clear** in root README.  
- **Validation vocabulary:** Factory `validation-runtime-*` vs governance `validation-chain-semantics` — **parallel semantics**, not broken routing (see Task D).

**Survivability verdict:** **Navigable** with Pass 4 compression; **entropy** remains in Tier 3 Factory/Forge volume and ORCA doc gravity.

---

## Task D — Semantic consistency pass

| Label family | Canonical surface | Drift signal |
|--------------|-------------------|--------------|
| **operational_doc_pack** | [agents/registry.md](../agents/registry.md) | Generally consistent in Forge/Gulp cards |
| **planned / strategic planned** | Factory README, project registry | Consistent with AGENTS |
| **experimental (R1)** | mars-runtime, reality index | Repeated boundary prose — **healthy** repetition |
| **documentation-only validation** | Factory validation-runtime-overview + governance validation-chain-semantics | Filename “runtime” vs “chain” — **mitigated** by banners; link chain-semantics when teaching validation |
| **external / n8n / WP** | external-system-boundaries, topology index | **Aligned** |
| **overlay / foundation** | frontend-legacy-and-foundation-map | **Stabilized** post-transition |
| **legacy imported** | web-gpt-sources | **Consistent** warnings |

**Minimal wording fixes applied in Pass 5:** ORCA current-state entry order; onboarding strategy Path A; ecosystem index scoped Tier 1 label.

**Deferred (low urgency):** Gulp pack Tier 2 banner; root README last-updated date; Forge README checklist table compression (Pass 4 proposed).

---

## Task E — Ecosystem durability review

### Structurally stable (safe for continued growth)

| Area | Why stable |
|------|------------|
| Tier 0–3 entry model | Documented, referenced from root + packs + Factory INDEX |
| Registry / AGENTS precedence | Repeated across governance S2–S4 |
| Factory Core Run / Extended split | Clear session contract |
| Forge transition + foundation map | Existence drift addressed |
| ORCA OPERATIONAL-INDEX live-first pattern | Model for other operational packs |
| Phase S3–S7 governance semantics | Mature vocabulary; not runtime pretend |

### Still produces entropy

| Area | Entropy mechanism |
|------|-------------------|
| Factory governance triads | New `*-governance.md` + taxonomy + checklist clusters |
| Forge README checklist table | Grows with every QA domain |
| governance/README row count | New phase = new row |
| web-gpt-sources vs governance | Legacy contradiction risk |
| Parallel validation vocabulary | Factory “runtime” filenames |
| ORCA doc-map / entrypoints / INDEX | Partial duplication |

### Likely future drift zones

1. New Tier 1 “start” index without retiring another.  
2. Triumph / reference cases read as production proof.  
3. Stabilization audits cited as override of AGENTS.  
4. Registry rows without lifecycle log backfill.  
5. Chat-migration snapshots treated as live state.

### Safe for growth (with maintenance)

- Pack OPERATIONAL-INDEX **Extended** rows (grouped).  
- Agent cards + registry rows.  
- Continuity / IdeaBox capture (optional).  
- mars-runtime **experimental** scripts (isolated).  
- ORCA fast-path layer (if INDEX remains SoT).

### Periodic maintenance (human)

Per [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md) + Pass 5:

| Trigger | Action |
|---------|--------|
| New pack or major lane | One OPERATIONAL-INDEX row; path letter in README |
| New cross-cutting concept | One canonical explanation + pointers |
| Post-compression feature burst | Editorial pass (not new ontology) |
| Forge/governance existence change | Update transition doc + foundation map |
| Quarterly | Routing spot-check + reality index bucket refresh |

**Durability verdict:** MARS is **fit for long-term evolution** if Tier discipline and compression hygiene repeat; **governance explosion** risk remains in Factory meta-layers, not in Tier 0–2 routing.

---

## Pass 5 actions taken

| Action | File |
|--------|------|
| This review | `governance/mars-consistency-survivability-pass-5-review-v0.md` |
| Path A alignment | `governance/survivability-onboarding-strategy-v0.md` |
| ORCA live-session precedence | `projects/orca/current-state-v1.md` |
| Scoped Tier 1 label | `governance/ecosystem-topology-index.md` |
| Survivability index link | `governance/operational-survivability.md` |
| Governance README row | `governance/README.md` |

---

## Remaining entropy risks (summary)

1. Factory Extended governance width.  
2. Forge checklist catalog length.  
3. ORCA secondary entry docs vs INDEX.  
4. web-gpt-sources first-read anti-pattern.  
5. governance/README encyclopedia growth.

---

## SAFE UNKNOWN

| Topic | UNKNOWN | Would verify |
|-------|---------|--------------|
| Full-repo broken links | Not exhaustively scanned | Optional future helper / CI (human-gated) |
| GitGuard operational status | External | Operator evidence outside repo |
| Triumph production deployment | External hosting | Operator / charter only |
| All pack README tier banners | Not every pack audited | Per-pack spot-check when touched |
| Chat-migration file headers | May lack superseded banner | On next migration doc edit |

---

## Related

- [editorial-compression-pass-4-operator-fatigue-review-v0.md](editorial-compression-pass-4-operator-fatigue-review-v0.md)  
- [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md)  
- [documentation-entropy-rules.md](documentation-entropy-rules.md)  
- [mars-v2-structural-coherence-audit-v0.md](mars-v2-structural-coherence-audit-v0.md) (input audit)

---

*Pass 5 — consistency and survivability hygiene only; no commits implied.*
