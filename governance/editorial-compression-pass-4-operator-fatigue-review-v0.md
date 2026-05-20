# MARS — Editorial Compression Pass 4: operator fatigue review

**Status:** **documented** — human-operated review only. **Not** governance expansion, **not** automation, **not** a new navigation product.  
**Date:** 2026-05-19.  
**Scope:** First focused **editorial-compression** pass outcomes and ongoing hygiene — complements [survivability-documentation-fatigue-review-v0.md](survivability-documentation-fatigue-review-v0.md).

---

## 1. Highest fatigue-producing entry surfaces

| Surface | Fatigue mechanism | Pass 4 mitigation |
|---------|-------------------|-------------------|
| [projects/mars-website-factory/OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) | Single table mixed Core + 40+ governance rows; **duplicate Frontend block** (~2× link density) | **Core Run** vs **Extended**; one **Frontend & Forge** canonical block |
| [projects/mars-website-factory/README.md](../projects/mars-website-factory/README.md) Pack index | ~200-line inventory reads like mandatory onboarding | Banner: session nav → OPERATIONAL-INDEX; Pack index = search/archival |
| [agents/mars-forge/README.md](../agents/mars-forge/README.md) | Full checklist catalog + overlay prose | Tier 2 entry; inherit table points to Gulp; INDEX no longer duplicates every checklist link |
| [governance/README.md](README.md) | Encyclopedia + implicit “read all rows” | Tier 1 router — **one row** per question, not full scan |
| [governance/ecosystem-topology-index.md](ecosystem-topology-index.md) + [mars-reality-index-v0.md](mars-reality-index-v0.md) | Two Tier-1 “start” surfaces | Tier hints: pick **one** per session after AGENTS |
| Root [README.md](../README.md) layout table | Depth-first folder exploration | Tier 0 + pointer to topology index for entity questions |

---

## 2. Highest repeated explanation surfaces

| Topic | Canonical explanation (after Pass 4) | Defer / reference elsewhere |
|-------|--------------------------------------|-----------------------------|
| **Gulp vs Forge vs Factory** | [frontend-legacy-and-foundation-map-v0.md](frontend-legacy-and-foundation-map-v0.md) §1, §5, §6 | OPERATIONAL-INDEX Frontend block; mars-forge README opening; card inheritance table |
| **Forge not parallel SoT** | Same map §5–6 | Short pointer only in Forge README, transition doc, topology Forge row |
| **Tier 0–3 routing** | [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md) | OPERATIONAL-INDEX header; pack README banners |
| **What MARS is / is not** | [AGENTS.md](../AGENTS.md), root README Phase 1 | Do not restate in pack indexes |
| **Forge overlay QA vs foundation QA** | [agents/mars-forge/qa-checklist.md](../agents/mars-forge/qa-checklist.md) + Gulp [qa-checklist.md](../agents/frontend-gulp-agent/qa-checklist.md) | Not per-domain in OPERATIONAL-INDEX |

---

## 3. Documentation spiral risks (remain elevated)

| Risk | Signal | Lightweight guard |
|------|--------|-------------------|
| **Governance triad sprawl** | New `*-governance.md` + taxonomy + checklist per session theme | Add to Extended table group only; no new OPERATIONAL-INDEX Core row without human review |
| **INDEX ↔ README competition** | Operator opens both fully at session start | Core Run in INDEX; README Pack index labeled archival |
| **Checklist catalog growth** | Forge README row count ↑ | Index checklists in Forge README only; Factory INDEX links to README |
| **Stabilization doc drift** | Design doc says “pack not created” while pack exists | [mars-forge-transition-stabilization-v0.md](mars-forge-transition-stabilization-v0.md) wins on existence |
| **Topology + reality + governance README** | Three Tier-1 reads in one session | [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md) paths A–E |

---

## 4. Easiest high-impact readability wins (done or next)

| Win | Status (Pass 4) |
|-----|-----------------|
| Factory OPERATIONAL-INDEX Core / Extended split | **Done** |
| Remove duplicate Frontend row in INDEX | **Done** |
| Tier banners on Factory README, Forge README | **Done** |
| Root README one-line Tier 1 pointer | **Done** |
| agents/README → foundation map for Forge | **Done** |
| governance/README Tier routing banner | **Done** |
| ecosystem-topology-index Tier 1 label | **Done** |
| Pack README Pack index “archival” one-liner | **Done** |
| Next (human-gated): shorten Forge README checklist table to grouped index | **Proposed** |
| Next: ORCA OPERATIONAL-INDEX Core/Extended pattern | **Proposed** |

---

## 5. Ongoing hygiene practices (not new governance systems)

1. **One canonical explanation** per cross-cutting topic (map above); other files get **one-line pointers**.  
2. **No new “start here”** without retiring or downgrading another ([documentation-entropy-rules.md](documentation-entropy-rules.md)).  
3. **Session open:** Tier 0 (if new) → **one** Tier 1 router → pack OPERATIONAL-INDEX **Core Run** row only.  
4. **INDEX edits:** add links in **Extended** groups; resist new Core rows unless runbook-critical.  
5. **Forge checklist links:** maintain in `agents/mars-forge/README.md`, not Factory INDEX per domain.  
6. **Compression passes:** editorial only — no ontology, no registry engine, no runtime semantics ([website-factory-navigation-compression-strategy-v0.md](website-factory-navigation-compression-strategy-v0.md)).

---

## Related

- [survivability-canonical-entrypoint-model-v0.md](survivability-canonical-entrypoint-model-v0.md)  
- [website-factory-navigation-compression-strategy-v0.md](website-factory-navigation-compression-strategy-v0.md)  
- [operational-survivability.md](operational-survivability.md) §6  
- [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md)
