# Programs Canvas Refresh v1

**Date:** 2026-06-03  
**Lane:** B — MARS Visual Brain Refresh 2026-06  
**Artifact:** `docs/visualization/obsidian-canvas/programs.canvas`

---

## Verification

| Entity | Required status | Canvas representation |
|--------|-----------------|----------------------|
| **GitGuard** | REGISTERED · Repository Survivability Layer | Node `n-prog-gitguard` with REGISTERED label; entry path under `mars-survivability`; explicit **not** `projects/gitguard/` · **no** `project_id` |
| **IdeaBox** | Incubation Layer · optional | Node `n-prog-ideabox` — `continuity/` · optional · human-maintained |

**Evidence SoT:**

- `projects/mars-survivability/registries/gitguard-system-entry-v1.md`
- `continuity/README.md`
- `governance/canonical-terminology-registry.md` § GitGuard / IdeaBox

---

## Relationships added

| Edge | From | To | Label | Invented? |
|------|------|-----|-------|-----------|
| `e-surv-gitguard` | MARS Survivability | GitGuard | REGISTERED entry | **No** — GitGuard registered via mars-survivability pack |

**Not added:** IdeaBox → Program edges (optional path; no mandatory topology edge in governance).

---

## Other program nodes

Existing program nodes retained (ORCA, Factory, WPilot, …). Triumph label clarified as client pack + Factory execution case (no new `project_id` implication).

---

## Node counts (post-regen)

14 nodes · 13 edges (includes hub + new entities).

---

*Programs canvas refresh v1 — Task 2 evidence.*
