# MARS v2 Stable Baseline

## Date

2026-06-03 (commit timestamp: 2026-06-03 00:19:21 +0700)

## Branch

`mars/post-cycle8-live-tests`

## Commit

`45518bb425a62ba7e4384daafe6dc1b1368ac2d1` — `checkpoint: mars-v2-stable-baseline-2026-06`

## Purpose

Official publication checkpoint for **MARS v2 Stable Baseline 2026-06**. Documentation-first ecosystem freeze after Cycle 8 stabilization — not MARS v3, not architecture redesign.

## Included scope

Per checkpoint commit message and assembly (412 files in commit):

- `projects/mars-survivability/**` — survivability pack (protocols, guardrails, contracts, registries)
- `projects/ear-runtime/**` — EAR runtime foundation (charters, R1 scaffold, `runtime/cli.py`, config loader)
- `projects/ocpilot/**` — metadata, policies, knowledge skeleton, storage registries (not vendor bulk)
- `shared/external-access-runtime/**` — external-access runtime patterns
- `governance/` updates — structural coherence audit touch, operational survivability
- `web-gpt-sources/mars-v2-final/**` — Web-GPT alignment pack
- `.gitignore` — OCPilot vendor tree (`baselines/**/files/**`) protection
- `logs/survivability/**`, `logs/rollback-history/**` — drill and rollback evidence
- `archive/orca-lrl-foundation-v1/**` — archived LRL foundation
- `docs/visualization/obsidian-canvas/**` — Visualization Pack v1 (Visual Brain source in Active Brain)

## Excluded scope

Per checkpoint commit message; remains unstaged WIP in working tree:

- `workspaces/**` — delivery WIP
- ORCA/Triumph operational churn (content-packs, PPC tools, workspace exports)
- `incoming/**` — staging materials
- `projects/ocpilot/baselines/**/files/**` — OCPilot baseline vendor bulk (~7600+ files)
- Font Awesome Pro vendor assets
- `projects/homegateway-v4-ai/**` design/atmosphere WIP (untracked/modified outside checkpoint)

## Knowledge Center status

**READY** — operator navigation system at `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER`.

Evidence (on-disk, session 2026-06-03):

- Root `README.md` defines KC as Visual Brain layer
- `00 START HERE/MARS DASHBOARD.md` — operator landing page
- Structure: `00 START HERE`, `01 ECOSYSTEM`, `02 PROGRAMS`, `03 EXECUTION CASES`, `04 GOVERNANCE`, `05 INFRASTRUCTURE`, `06 ARCHIVE`, `99 EXPORTS`
- Canvas mirrors under KC (e.g. `00 START HERE/canvas/master.canvas`)
- **Not in git** — bulk/navigation layer per [governance/mars-infrastructure-reality-v1.md](../../governance/mars-infrastructure-reality-v1.md)

## Visual Brain status

**READY** — dual surface:

| Surface | Path | Role |
|---------|------|------|
| Source (git) | `docs/visualization/obsidian-canvas/` | 6 `.canvas` files + README + generator — tracked at `45518bb` |
| Operator copy | `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` | Obsidian navigation, canvas copies, program cards |

Canonical pack: [docs/visualization/obsidian-canvas/README.md](../../docs/visualization/obsidian-canvas/README.md) (export pack v1, 2026-06-02).

## Cold Brain status

**MATERIALIZED** — `C:\AI MARS STORAGE\ARCHIVE` exists (7 top-level items verified on-disk 2026-06-03).

Per KC README: long-term bulk archives; operator-defined cold paths. Existence of individual archive contents and sync state — **SAFE UNKNOWN** unless verified per session.

## Operator notes

- Push executed: `git push origin mars/post-cycle8-live-tests` → `d6b67ea..45518bb` (12 commits).
- Remote tracking: `[origin/mars/post-cycle8-live-tests]` at `45518bb` — no ahead/behind after push.
- Staging area at publication time: **clean** (0 staged files); unstaged WIP allowed and present (~590 working-tree entries).
- This release evidence file is **post-checkpoint** operator documentation; not part of commit `45518bb`.
- Baseline is **documentation-first** — no claim of shipped MARS runtime, orchestrator, or autonomous agents.

---

*Publication evidence — MARS v2 Stable Baseline 2026-06 — Lane B.*
