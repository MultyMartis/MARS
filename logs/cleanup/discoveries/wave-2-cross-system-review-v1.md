# Wave 2 Cross-System Review v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2 Discovery  
**Mode:** Comparative analysis only — **no subsystem creation**, **no redesign**  
**Entities:** Lifecycle Log · GitGuard · IdeaBox · Incoming  
**Evidence inputs:** [lifecycle-log-deep-review-v2.md](lifecycle-log-deep-review-v2.md), [gitguard-deep-review-v2.md](gitguard-deep-review-v2.md), [ideabox-deep-review-v2.md](ideabox-deep-review-v2.md), [incoming-deep-review-v2.md](incoming-deep-review-v2.md)

---

## 1. Role summary (one line each)

| Entity | Canonical surface | One-line role |
|--------|-------------------|---------------|
| **Lifecycle Log** | `logs/lifecycle-log.md` | Append-only **governance event** audit trail |
| **GitGuard** | `projects/mars-survivability/**` (concept) | **Survivability advisory** + human-operated git/filesystem helpers |
| **IdeaBox** | `continuity/**` | **Session continuity** — ideas/discoveries/decisions markdown |
| **Incoming** | `incoming/**` (+ program-scoped `projects/*/incoming/`) | **Quarantine / transport** for external material before promotion |

---

## 2. Overlap matrix

|  | Lifecycle | GitGuard | IdeaBox | Incoming |
|--|-----------|----------|---------|----------|
| **Lifecycle** | — | Policy changes may warrant evt; survivability drills rarely logged | Idea promotion could warrant evt — **not practiced** | Intake promotion **not** logged — gap |
| **GitGuard** | — | — | Protects `continuity/` | No automation on drops; validator may scan paths |
| **IdeaBox** | — | — | — | Both “capture” — **different trust**: ideabox=authored notes; incoming=untrusted external |
| **Incoming** | — | — | — | — |

### 2.1 Duplicates (conceptual, not file duplicates)

| Duplicate risk | Entities involved | Resolution |
|----------------|-------------------|------------|
| “Another log under `logs/`” | Lifecycle vs `logs/cleanup/` vs `logs/releases/` | **REDEFINE** three-log model (lifecycle / cleanup / releases) |
| “Human capture” | IdeaBox vs Incoming vs continuity-style program notes | **REDEFINE** charters: ideabox=thought; incoming=artefact drop |
| “Checkpoint” language | GitGuard vs GIT CHECKPOINT signal vs ORCA git-checkpoint docs | **MERGE** narrative — GitGuard ≠ git commit signal |
| “Discovery” folders | `continuity/discoveries/` vs `logs/cleanup/discoveries/` | **REDEFINE** — cleanup = ecosystem audit; continuity = operator session |
| “Archive” mental model | Incoming stale packs vs `archive/` vs canvas lifecycle=archive-cand | **REDEFINE** labels — lifecycle is **KEEP**, not archive |

### 2.2 Gaps (missing relationships)

| Gap | Impact | Proposed link (documentation only) |
|-----|--------|-------------------------------------|
| No root `incoming/README.md` | Operators lack ecosystem intake map | Link from topology index + ORCA/MIG/OCPilot charters |
| Registry changes without lifecycle | Audit trail drift | Same-session append rule (existing in sync review) |
| IdeaBox → program promotion | Ideas stall in `continuity/ideabox/` | Incubation path doc (REDEFINE) |
| Incoming triage → lifecycle | No evt when raw pack promoted | Optional `intake.promoted` event_type |
| GitGuard → lifecycle | Stabilization phases partially logged | Optional evt when G3+ pilot starts |
| Canvas mislabels lifecycle | Wrong cleanup band | Fix generator node category |

---

## 3. Could they form a coherent subsystem?

**Yes — as a documented “Operator Evidence & Intake Lane” (conceptual only, not implemented).**

```text
                    ┌─────────────────────────────────────┐
                    │   Operator Evidence & Intake Lane    │
                    │   (human-operated, no runtime)       │
                    └─────────────────────────────────────┘
                                      │
        ┌──────────────┬──────────────┼──────────────┬──────────────┐
        ▼              ▼              ▼              ▼              │
   Incoming        IdeaBox        GitGuard      Lifecycle Log      │
   (untrusted      (trusted       (risk          (governance       │
    external        session         reduction      events           │
    drops)          capture)        advisory)      recorded)        │
        │              │              │              │              │
        └──────promote─┴──incubate───┴──protect─────┴──audit───────┘
                              │
                              ▼
                    projects/* · registry · governance SoT
```

### 3.1 Coherence properties (if documented together)

| Property | How the four entities cooperate |
|----------|--------------------------------|
| **Trust gradient** | Incoming (low) → IdeaBox (medium, human-authored) → Registry/Governance (high) |
| **Time axis** | Incoming = point of entry; IdeaBox = session span; Lifecycle = durable events; GitGuard = pre-mutation safety |
| **Enforcement** | All four: **human-operated** — no autonomous merge |
| **Non-goals** | Not runtime, not KC, not cleanup program, not n8n SoT |

### 3.2 What this subsystem is NOT

- Not a new `project_id` or MCP service  
- Not a replacement for Observability run history  
- Not Knowledge Center (out-of-git navigation)  
- Not Cold Brain bulk store (though Incoming **retirees** may move there)

**Wave 2 action:** **Do not create** folder or registry row — record coherence here for Wave 3 charter decision.

---

## 4. Recommended relationships (documentation graph)

```text
incoming/README.md (future)
    → incoming/mig/README.md
    → projects/ocpilot/incoming/README.md
    → orca-universal-intake-architecture-v0.md

continuity/README.md
    → ideabox-protocol-v1.md
    → logs/cleanup/README.md  (clarify: not IdeaBox)

logs/lifecycle-log.md
    → registry-source-of-truth.md
    → logs/cleanup/README.md
    → logs/releases/

projects/mars-survivability/registries/gitguard-system-entry-v1.md
    → protected-zones-registry-v1.md (includes continuity/, governance/)
    → destructive-operations-policy-v1.md
```

---

## 5. Unified classification table (Wave 2)

| Entity | KEEP | REDEFINE | REGISTER | MERGE | ARCHIVE CANDIDATE | Operator decision |
|--------|------|----------|----------|-------|-------------------|-------------------|
| Lifecycle Log | ✓ | ✓ (boundaries) | — | — | ✗ | Backfill 0017–0021 |
| GitGuard | ✓ (in survivability) | — | Defer | ✓ (entity model narrative) | ✗ | Separate project_id? |
| IdeaBox | ✓ | ✓ (incubation path) | ✗ | — | ✗ | Promotion checklist |
| Incoming | ✓ (hybrid) | ✓ (README + SOP) | ✗ | — | Subfolders only (post-triage) | Hybrid policy N-01 |

---

## 6. Cross-system risks

| Risk | Severity |
|------|----------|
| Conflating lifecycle with cleanup discoveries | Medium |
| Treating GitGuard as deployed blocker | Medium (mythology) |
| Treating IdeaBox as agent memory | High (terminology violation) |
| Leaving normalized raw packs in Incoming forever | Medium (repo noise) |
| Destructive cleanup of `incoming/` without GitGuard/survivability review | High |

---

*Wave 2 Cross-System Review v1 — evidence only.*
