# MARS v2 Stable Baseline — Publication (2026-06)

**Status:** **CORE**  
**Evidence:** `logs/releases/mars-v2-stable-baseline-2026-06.md` (commit `c2876cf` docs evidence; checkpoint `45518bb`)

---

## Publication facts

| Field | Value |
|-------|--------|
| **Name** | MARS v2 Stable Baseline 2026-06 |
| **Date** | 2026-06-03 |
| **Branch** | `mars/post-cycle8-live-tests` |
| **Checkpoint commit** | `45518bb425a62ba7e4384daafe6dc1b1368ac2d1` |
| **Tag/checkpoint label** | `mars-v2-stable-baseline-2026-06` |
| **Remote** | Pushed to `origin/mars/post-cycle8-live-tests` at publication |

---

## Purpose

Official **documentation-first ecosystem freeze** after Cycle 8 stabilization.

| Is | Is not |
|----|--------|
| Published scope boundary for operators and Web-GPT | MARS v3 |
| Checkpoint for survivability, EAR, OCPilot metadata, governance touch | Architecture redesign |
| Includes Visualization Pack v1 in git | Claim of shipped MARS runtime / orchestrator |
| Aligns `web-gpt-sources/mars-v2-final/` at commit time | Replacement for in-repo governance SoT |

---

## Included scope (checkpoint assembly)

Representative paths per checkpoint (~412 files):

- `projects/mars-survivability/**` — protocols, guardrails, contracts, registries  
- `projects/ear-runtime/**` — charters, R1 scaffold, `runtime/cli.py`, config loader  
- `projects/ocpilot/**` — metadata, policies, knowledge skeleton, storage registries (**not** vendor bulk)  
- `shared/external-access-runtime/**` — external-access patterns  
- `governance/` — structural coherence audit touch, operational survivability  
- `web-gpt-sources/mars-v2-final/**` — Web-GPT alignment at commit time (**superseded for upload by this 2026-06 pack**)  
- `.gitignore` — OCPilot vendor tree protection  
- `logs/survivability/**`, `logs/rollback-history/**` — drill/rollback evidence  
- `archive/orca-lrl-foundation-v1/**` — archived LRL foundation  
- `docs/visualization/obsidian-canvas/**` — Visualization Pack v1 (Visual Brain git source)

---

## Excluded scope (remains WIP / out of checkpoint)

| Path / area | Reason |
|-------------|--------|
| `workspaces/**` | Delivery WIP |
| ORCA/Triumph operational churn | Content-packs, PPC tools, workspace exports |
| `incoming/**` | Staging materials |
| `projects/ocpilot/baselines/**/files/**` | Vendor bulk (~7600+ files) |
| Font Awesome Pro vendor assets | Licensed local assets |
| `projects/homegateway-v4-ai/**` design WIP | Outside checkpoint at publication |

Unstaged WIP in working tree is **allowed** (~590 entries at publication) — baseline does not require clean tree.

---

## Brain layer status at publication

| Layer | Status |
|-------|--------|
| Knowledge Center | **READY** — `C:\AI MARS STORAGE\MARS KNOWLEDGE CENTER` |
| Visual Brain | **READY** — git canvas pack + KC mirrors |
| Cold Brain | **MATERIALIZED** — `C:\AI MARS STORAGE\ARCHIVE` |

---

## Operator notes

- Staging at publication: **clean** (0 staged); unstaged WIP permitted.  
- Release evidence file is **post-checkpoint** operator documentation — not part of `45518bb`.  
- **No commit implied** by reading this Web-GPT pack — operator controls git.

---

## Web-GPT pack relationship

This folder (`mars-v2-stable-baseline-2026-06/`) is the **upload-facing** distillate of the published baseline. Use `WEB-GPT-SOURCE-PACK-INDEX.md` for human upload order.

---

*Official publication checkpoint — documentation-first — Lane B evidence.*
