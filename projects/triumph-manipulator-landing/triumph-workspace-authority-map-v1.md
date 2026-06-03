# Triumph Manipulator Landing — Workspace Authority Map v1

**Status:** **authoritative** (single source of truth for Triumph workspace lineage)  
**Date:** 2026-06-03 (MARS Cleanup Wave 1A)  
**project_id:** `triumph-manipulator-landing`  
**Program pack:** `projects/triumph-manipulator-landing/` (governance — **not** build sources)

**Evidence:** [logs/cleanup/actions/triumph-authority-map-v1.md](../../logs/cleanup/actions/triumph-authority-map-v1.md) · upstream [logs/cleanup/discoveries/triumph-version-map-v1.md](../../logs/cleanup/discoveries/triumph-version-map-v1.md)

**Rule:** **No archival executed** in Wave 1A — archive candidates are documented recommendations only.

---

## Executive summary

| Question | Answer |
|----------|--------|
| **Canonical workspace** | `workspaces/triumph-manipulator-landing-v6/` |
| **Canonical program pack** | `projects/triumph-manipulator-landing/` |
| **Factory reference case (doc)** | `projects/mars-website-factory/reference-cases/triumph-manipulator-landing/` — simulated run, distinct from v6 delivery |
| **ORCA PPC toolkit** | `projects/orca/ppc/triumph-manipulator/` |

---

## Lineage table

| Version | Path | Purpose | Status | Relationship | Recommendation |
|---------|------|---------|--------|----------------|----------------|
| **v1 (base)** | `workspaces/triumph-manipulator-landing/` | Initial Gulp starter; frozen at tag `triumph-manipulator-v1` | **Historical** | Root generation | **Archive candidate** (Wave 2+) — tag-pinned |
| **v2** | `workspaces/triumph-manipulator-landing-v2/` | V2 product intent — design system + Forge rules | **Historical** | Evolved from v1 | **Archive candidate** — superseded |
| **v3** | `workspaces/triumph-manipulator-landing-v3/` | Clean Forge rebuild prep from V1 authority | **Abandoned / prep-only** | Branch from v1 line | **Archive candidate** — no rebuild proof |
| **v4** | `workspaces/triumph-manipulator-landing-v4/` | Reset-plan boundary for reconstruction | **Stale / planning residue** | Parallel planning fork | **Archive candidate** — `V4-RESET-PLAN.md` only |
| **v5** | `workspaces/triumph-manipulator-landing-v5/` | Index baseline; mailer MVP final; operator visual QA checkpoint | **Historical stable reference** | Precursor to v6; copied forward | **Archive candidate** after ORCA/calibration retarget complete — **keep** short term |
| **v6** | `workspaces/triumph-manipulator-landing-v6/` | **Active multi-page PPC rollout** (12 routes); production candidate | **Canonical** | Current edit surface; v6 README + freeze report | **KEEP** — canonical workspace |

---

## Related loci (not version workspaces)

| Path | Role |
|------|------|
| `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-v1/` | Filesystem freeze snapshot |
| `workspaces/_snapshots/snap-20260528-triumph-v5-mailer-mvp-final-stable/` | V5 recovery snapshot |
| `projects/mars-website-factory/reference-cases/triumph-manipulator-landing/` | Factory doc-simulation reference case #1 |
| `projects/orca/ppc/triumph-manipulator/` | ORCA semantic / export toolkit |

---

## Canonical verification (multi-source)

| Surface | Statement |
|---------|-----------|
| `workspaces/triumph-manipulator-landing-v6/README.md` | Canonical production base for multi-page PPC rollout |
| [frontend-workspace.md](frontend-workspace.md) | Recommended path v6 (2026-05-28) |
| [V6-PRODUCTION-CANDIDATE-STATE.md](V6-PRODUCTION-CANDIDATE-STATE.md) | Production candidate; 12 routes |
| [TRIUMPH-V6-CURRENT-FRONTEND-RULES.md](TRIUMPH-V6-CURRENT-FRONTEND-RULES.md) | Active frontend rules |

---

## Partial naming note

V6 retains directory convention `v5-ppc/<slug>/` and shared `v5-page01/*` — **folder names are legacy**, **workspace v6 is canonical**. Do not infer implementation target from `v5-` partial prefixes alone.

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Live production URL vs v6 build | External hosting |
| Whether v3 battle-test resumes | Operator charter |
| Git tags for v5/v6 beyond v1 | Not fully audited |

---

*Triumph workspace authority map v1 — Wave 1A.*
