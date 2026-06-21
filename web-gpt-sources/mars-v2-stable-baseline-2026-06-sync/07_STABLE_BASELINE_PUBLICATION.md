# MARS v2 Stable Baseline — Publication & sync scope (2026-06)

**Status:** **CORE**  
**Pack role:** This file documents **what the sync pack aligns to** — not a new product release.

---

## Publication chain

| Stage | Name | Checkpoint | Evidence |
|-------|------|------------|----------|
| 1 | **Stable Baseline** | `45518bb` · `mars-v2-stable-baseline-2026-06` | `c2876cf` → `logs/releases/mars-v2-stable-baseline-2026-06.md` |
| 2 | **Post-Cleanup Alignment** | `aafacf8` · `post-cleanup-ecosystem-alignment-2026-06` | `38e7b64` → `logs/releases/post-cleanup-ecosystem-alignment-2026-06.md` |
| 3 | **Awareness Alignment Pass** | 2026-06-13 (working tree) | `logs/alignment/mars-awareness-alignment-pass-2026-06.md` |

**Branch at publication:** `mars/post-cycle8-live-tests`

---

## What each stage is / is not

| Stage | Is | Is not |
|-------|-----|--------|
| Stable Baseline | Documentation-first ecosystem freeze after Cycle 8 | MARS v3; shipped runtime |
| Post-Cleanup | Governance + cross-cutting alignment after Cleanup Program | Supersedes `45518bb`; new version |
| Awareness Pass | Visibility alignment (registry, topology, canvas, Web-GPT) | Runtime registration; architecture redesign |
| **This sync pack** | Fresh Web-GPT upload bundle reflecting stages 1–3 | New MARS version; repo SoT replacement |

---

## Stable Baseline scope (`45518bb`)

Representative included paths:

- `projects/mars-survivability/**` — protocols, guardrails, GitGuard contracts  
- `projects/ear-runtime/**` — charters, R1 scaffold  
- `projects/ocpilot/**` — metadata, policies (**not** vendor bulk)  
- `shared/external-access-runtime/**` — external-access patterns  
- `governance/` — structural coherence, operational survivability  
- `docs/visualization/obsidian-canvas/**` — Visualization Pack v1  
- `.gitignore` — OCPilot vendor tree protection  

**Excluded at baseline:** `workspaces/**` WIP, OCPilot `baselines/**/files/**`, HomeGateway design WIP, `incoming/**` staging.

---

## Post-Cleanup alignment scope (`aafacf8`)

Appended to baseline — **85 files** including:

| Area | Outcome |
|------|---------|
| Cleanup Program | Waves 1→2B complete; audit **PARTIAL PASS** |
| **GitGuard** | REGISTERED cross-cutting — no `project_id` |
| **IdeaBox** | Optional Incubation Layer — `continuity/` |
| **Incoming** | Hybrid charter — Active Incoming + Historical Bulk |
| **Lifecycle Log** | Key Event History; evt 0017–0021 backfilled |
| **ISBD** | Factory execution case #2 registered |
| **Triumph** | Canonical workspace **v6** authority map |
| Web-GPT pack | Initial `mars-v2-stable-baseline-2026-06/` folder created |

**State snapshot:** `logs/releases/mars-post-cleanup-ecosystem-state-2026-06.md` (point-in-time; may lag awareness pass).

---

## Awareness alignment scope (2026-06-13)

| Entity | Alignment outcome |
|--------|-------------------|
| **ATLAS** | Reality index §; maturity **FOUNDATION + POPULATION (docs)**; lifecycle `evt-2026-0024` |
| **OPS** | Reality index §; WF-01/WF-02 pilots PARTIAL; canvas node + edges |
| **BZPM** | Execution case #3 on canvas + maturity map |
| **LOC-ZONE** | Topology §; workspaces README; canvas; FP-0002 visibility (enrollment deferred) |
| **FP-0002** | Visibility-only — ROC-01 enrollment candidate |
| **AG-WP-001** | Seed documented in LOC-ZONE — not `agents/registry.md` row |

**Deferred (not in this pass):** consumer README ATLAS pointers; KC mirror refresh; post-cleanup state snapshot v2.

---

## Brain layer status

| Layer | Status |
|-------|--------|
| Knowledge Center | **READY** — operator vault; mirror refresh optional |
| Visual Brain | **READY** — git canvas + KC copies |
| Cold Brain | **MATERIALIZED** — `C:\AI MARS STORAGE\ARCHIVE` |

---

## Web-GPT pack relationship

| Pack | Role |
|------|------|
| `mars-v2-stable-baseline-2026-06/` | Baseline distillate at publication — **preserved, not overwritten** |
| `mars-v2-stable-baseline-2026-06-sync/` | **This pack** — upload when chat must reflect post-cleanup + awareness state |

Use `WEB-GPT-SOURCE-PACK-INDEX.md` in this folder for upload order.

---

## Operator notes

- Reading this pack **does not** imply commit or push — operator controls git.  
- Unstaged WIP in working tree is normal — baseline does not require clean tree.  
- Reconcile live `registry/project-registry.md` after any registration change.

---

*Publication + sync scope — documentation-first — Lane B evidence.*
