# MARS Cleanup Wave 2 Discovery v1

**Date:** 2026-06-03  
**Lane:** B  
**Charter:** MARS Cleanup Wave 2 Discovery — **investigate and classify only**  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb` / `mars-v2-stable-baseline-2026-06`; evidence `c2876cf`)  
**Prerequisites:** Census v1 ✓ · Cleanup Wave 1 ✓ · Wave 1A ✓  
**Rule:** No cleanup · no archive · no delete · no move · no redesign

---

## Scope completed

| Task | Deliverable | Status |
|------|-------------|--------|
| Task 1 — Lifecycle Log deep review | [discoveries/lifecycle-log-deep-review-v2.md](discoveries/lifecycle-log-deep-review-v2.md) | ✓ |
| Task 2 — GitGuard deep review | [discoveries/gitguard-deep-review-v2.md](discoveries/gitguard-deep-review-v2.md) | ✓ |
| Task 3 — IdeaBox deep review | [discoveries/ideabox-deep-review-v2.md](discoveries/ideabox-deep-review-v2.md) | ✓ |
| Task 4 — Incoming deep review | [discoveries/incoming-deep-review-v2.md](discoveries/incoming-deep-review-v2.md) | ✓ |
| Task 5 — Cross-system review | [discoveries/wave-2-cross-system-review-v1.md](discoveries/wave-2-cross-system-review-v1.md) | ✓ |
| Task 6 — Summary | This file | ✓ |

---

## Findings (consolidated)

### Lifecycle Log

- **KEEP** — normative governance event SoT (`logs/lifecycle-log.md`); 16 events; last `evt-2026-0016` (2026-05-19).
- **REDEFINE** — distinguish from `logs/cleanup/`, `logs/releases/`, and task REPORTs; fix canvas “archive-cand” drift.
- **Under-maintained** — registry ahead of log; backlog **0017–0021** documented, not appended.
- **Not** ARCHIVE CANDIDATE.

### GitGuard

- **Not** mere git discipline — **survivability advisory framework** (G0–G4 done as docs + human CLI).
- **Not** autonomous Backup/Checkpoint/Rollback product — no `projects/gitguard/`.
- **KEEP** under `projects/mars-survivability/`; **MERGE** entity-model “Program example” with reality-index honesty.
- **REGISTER** as separate `project_id` — **deferred** (operator).

### IdeaBox

- **KEEP** — `continuity/` operational discipline; intentionally not in project registry.
- **Low volume, clear boundaries** — 2 substantive markdown captures + protocols.
- **REDEFINE** — optional canonical **incubation** path vs cleanup discoveries.
- **Not** ARCHIVE CANDIDATE.

### Incoming

- **Hybrid placement recommended** — operational `incoming/mig/` stays in Active Brain; stale bulk (e.g. orca-triumph-raw-pack) → Cold Brain **after** triage.
- **No** root `incoming/README.md` — governance gap.
- **Excluded** from stable baseline checkpoint — staging by design.
- Subfolders: mig (active), orca pack (stale), metabot (sync unknown), mars-bridge (stub), legal-cleanup (pending).

### Cross-system

- Four entities can form coherent **“Operator Evidence & Intake Lane”** (conceptual) — **do not implement** in Wave 2.
- Main duplicate risk: multiple `logs/` and `discoveries/` folders — resolve by **charter**, not merge on disk.

---

## Recommendations

| Priority | Recommendation |
|----------|----------------|
| P0 | **KEEP** all four entities — none are obsolete concepts |
| P1 | **REDEFINE** documentation boundaries (lifecycle / cleanup / releases / IdeaBox vs cleanup discoveries) |
| P1 | **REDEFINE** Incoming — ecosystem README + hybrid storage policy (doc only) |
| P2 | Operator: lifecycle backfill **0017–0021** (human-gated) |
| P2 | Operator: Incoming triage (orca raw pack, legal-cleanup, metabot freshness) |
| P3 | Operator: GitGuard separate `project_id` vs stay in mars-survivability |
| P3 | Operator: IdeaBox incubation promotion checklist |

---

## Evidence created (this wave)

| File | Purpose |
|------|---------|
| `logs/cleanup/discoveries/lifecycle-log-deep-review-v2.md` | Intent, evolution, overlaps, KEEP/REDEFINE |
| `logs/cleanup/discoveries/gitguard-deep-review-v2.md` | Purpose, artefacts, maturity, KEEP/MERGE/REGISTER defer |
| `logs/cleanup/discoveries/ideabox-deep-review-v2.md` | Workflow, differentiation, incubation potential |
| `logs/cleanup/discoveries/incoming-deep-review-v2.md` | Contents, hybrid model, triage candidates |
| `logs/cleanup/discoveries/wave-2-cross-system-review-v1.md` | Overlaps, gaps, coherent subsystem sketch |
| `logs/cleanup/MARS-CLEANUP-WAVE-2-DISCOVERY-v1.md` | This summary |

---

## Proposed next actions (not executed)

| ID | Action | Owner |
|----|--------|-------|
| W2-A01 | Append lifecycle events 0017–0021 (confirmed timestamps) | Operator |
| W2-A02 | Author `incoming/README.md` ecosystem charter | Operator / Lane B doc pass |
| W2-A03 | Triage `incoming/orca-triumph-raw-pack/` — archive candidate AC-10 | Operator |
| W2-A04 | Resolve `incoming/website-factory-legal-cleanup/` promote vs intake (A-030) | Operator + Factory |
| W2-A05 | Fix Obsidian canvas lifecycle node category in `_generate_pack.py` | Lane B doc |
| W2-A06 | Draft `continuity/INCUBATION-PATH-v0.md` (optional) | Operator |
| W2-A07 | GitGuard entity-model ↔ survivability cross-link paragraph | Lane B doc |
| W2-A08 | Wave 3 Cleanup charter: Incoming hybrid moves (if N-01 approved) | Operator |

Add rows to [actions/cleanup-wave-1-action-registry-v1.md](actions/cleanup-wave-1-action-registry-v1.md) or new Wave 2 action file on operator request — **not done automatically**.

---

## Actions executed

**None** — discovery-only charter honored.

---

## Risks

| Risk | Notes |
|------|-------|
| Lifecycle drift continues | Registry changes without events erode audit trust |
| GitGuard over-claim | Language implying autonomous block/recovery |
| IdeaBox mythology | “Remembers context” violates terminology registry |
| Incoming bloat | Normalized raw packs retained indefinitely in git |
| Path break on hybrid move | Moving `incoming/mig/` without adapter doc update would break MIG |

---

## SAFE UNKNOWN

| Topic |
|-------|
| Live n8n vs `incoming/metabot/` export parity |
| Operator Cold Brain contents for retired incoming packs |
| Exact dates for lifecycle backfill rows |
| Cursor G3+ hook feasibility |
| Full count of unpromoted ideas in chat-only form |

---

## Final classification (operator summary)

| Entity | Keep | Redefine | Archive | Operator decision required |
|--------|------|----------|---------|----------------------------|
| Lifecycle Log | ✓ | ✓ | ✗ | Backfill 0017–0021; optional baseline evt |
| GitGuard | ✓ | — | ✗ | Separate `project_id`?; G3+ pilot |
| IdeaBox | ✓ | ✓ | ✗ | Incubation checklist; index policy |
| Incoming | ✓ | ✓ | Subfolders post-triage | Hybrid model N-01; per-folder triage |

---

*MARS Cleanup Wave 2 Discovery v1 — no filesystem mutations.*
